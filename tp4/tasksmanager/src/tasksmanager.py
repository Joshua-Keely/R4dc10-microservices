import flask
import flask_restx

app = flask.Flask(__name__)
api = flask_restx.Api(app = app)


taches = {
    "tache-1": "Préparer le TP microservices",
    "tache-2": "Préparer l'examen du module microservices",
}
@api.route('/tasks')
class Tasks(flask_restx.Resource):
    def get(self):
        liste = []
        for key, value in taches.items():
            liste.append({
               'id': key,
                'description': value
            })
        return liste, 200

    def generation_tache_id(self):
        try:
            tache_id = int(max(taches.keys()).lstrip('tache-')) + 1
            return f"tache-{tache_id}"
        except ValueError:
            return "Error"

    def post(self):
        h = flask.request.headers['Content-Type']
        if h == 'application/json':
            json_data = flask.request.get_json()
            tache_id = self.generation_tache_id()
            taches[tache_id] = json_data["description"]
            return {
                "message": f"La tâche {tache_id} à été crée",
                "description": f"{taches[tache_id]}"
            }, 201


@api.route('/tasks/<tid>')
class Task(flask_restx.Resource):
    def get(self, tid):
        if tid in taches:
            return {
                'id': tid,
                'description': taches[tid]
            }, 200
        else:
            flask_restx.abort(404, "Tache non trouvée")

    def delete(self, tid):
        if tid in taches:
            del taches[tid]
            return {
                'message': f"Tache {tid} supprimée"
            }, 200
        else:
            flask_restx.abort(404, "Tache non trouvée")

    def put(self, tid):
        if tid not in taches:
            return {
                "message": f"La tâche {tid} n'existe pas"
            }, 404
        else:
            h = flask.request.headers['Content-Type']
            if h == 'application/json':
                json_data = flask.request.get_json()
                data = json_data["description"]
                taches[tid] = data

            return {
                "message": f"La tâche {tid} à été mise à jour",
                "description": f"{taches[tid]}"
            }, 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)




import flask
import flask_restx

app = flask.Flask(__name__)
api = flask_restx.Api(app = app)
@api.route('/hello')
class Hello(flask_restx.Resource):
    """Réponse aux requêtes HTTP GET"""
    def get(self):
        return {
            'message': 'hello world'
        }, 200

@api.route('/hello2/<string:name>')
class Hello2(flask_restx.Resource):
    """Réponse aux requêtes HTTP GET"""
    def get(self, name):
        return {
            'message': f"hello {name}"
        }, 200

@api.route('/sayhello')
class SayHello(flask_restx.Resource):
    def post(self):
        h = flask.request.headers['Content-Type']
        if h == 'application/json':
            json_data = flask.request.get_json()
            msg = json_data["message"]
            print(msg)
        elif h == 'text/plain':
            data = flask.request.data
            msg = data.decode("utf-8")
            print(msg)
        else:
            flask_restx.abort(406, "Format incorrect")


if __name__ == '__main__':
    app.run(debug=True, port=5000)

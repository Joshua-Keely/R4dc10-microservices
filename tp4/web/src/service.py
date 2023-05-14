import json

import requests

URL = "http://127.0.0.1:5000"


def get_tasks():
    """
    Récupère (toute) la liste des tâches.

    :return: la liste des tâches au format :

        [
          {
            "id": "tache-1",
            "description": "Preparer le TP microservices"
          },
          {
            "id": "tache-2",
            "description": "Preparer l'examen du module microservices"
          }
        ]

    """
    pass


def get_task(task_id):
    """
    Récupère la tâche identifiée par `task_id`.

    :param task_id: l'identifiant de la tâche (par exemple `tache-1`)
    :return: la tâche au format

          {
            "id": "tache-2",
            "description": "Preparer l'examen du module microservices"
          }

          ou `None` si la tâche n'existe pas
    """
    pass

def delete_task(task_id):
    """
    Supprime la tâche identifiée par task_id.

    :param task_id: l'identifiant de la tâche (par exemple `tache-1`)
    :return: True si la tâche a été supprimée
    """
    pass

def update_task(task):
    """
    Met à jour la tâche donnée en paramètre.

    :param task: la tâche au format

          {
            "id": "tache-2",
            "description": "Preparer l'examen du module microservices"
          }

    :return: `True` si la tâche a été mise à jour, `False` sinon
    """
    pass

def add_task(task):
    """
    Met à jour la tâche donnée en paramètre.

    :param task: la tâche au format

          {
            "description": "Preparer l'examen du module microservices"
          }

    :return: True si la tâche a été mise à jour
    """
    pass

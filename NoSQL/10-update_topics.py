#!/usr/bin/env python3
"""
Módulo para actualizar los temas (topics) de una escuela en MongoDB
"""


def update_topics(mongo_collection, name, topics):
    """
    Cambia todos los temas de un documento escolar basado en su nombre.
    
    Args:
        mongo_collection: El objeto de la colección de pymongo.
        name (str): El nombre de la escuela a actualizar.
        topics (list of str): La lista de temas a agregar a la escuela.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

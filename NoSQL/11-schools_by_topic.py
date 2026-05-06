#!/usr/bin/env python3
"""
Módulo para buscar escuelas por un tema (topic) específico
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retorna la lista de escuelas que tienen un tema en específico.
    
    Args:
        mongo_collection: El objeto de la colección de pymongo.
        topic (str): El tema que se va a buscar.
        
    Returns:
        Una lista de documentos (diccionarios) que coinciden con el tema.
    """
    # Buscamos documentos donde el arreglo 'topics' contenga el string 'topic'
    return list(mongo_collection.find({"topics": topic}))

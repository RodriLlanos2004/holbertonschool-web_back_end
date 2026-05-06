#!/usr/bin/env python3
"""
Script que provee estadísticas sobre los logs de Nginx almacenados en MongoDB.
La base de datos es 'logs' y la colección es 'nginx'.
"""
from pymongo import MongoClient


def log_stats():
    """
    Se conecta a MongoDB, extrae los datos y los imprime en el formato exacto requerido.
    """
    # Conexión al servidor local de MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Acceso a la colección nginx dentro de la base de datos logs
    nginx_collection = client.logs.nginx

    # 1. Contar el número total de logs (documentos)
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Imprimir las estadísticas por método HTTP
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        # Cuenta cuántos documentos tienen ese método específico
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Contar los status checks (método GET y path /status)
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()

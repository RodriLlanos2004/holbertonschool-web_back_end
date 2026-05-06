# NoSQL

Este proyecto es una introducción a las bases de datos NoSQL utilizando **MongoDB**. Incluye scripts para interactuar directamente con el motor de base de datos y scripts en **Python** usando la librería `pymongo` para realizar operaciones CRUD, filtros y manipulación de datos.

## Repositorio
* **GitHub repository:** `holbertonschool-web_back_end`
* **Directory:** `NoSQL`

## Lista de Tareas y Archivos

### Scripts de MongoDB (Comandos crudos)
* **0-list_databases**: Lista todas las bases de datos en MongoDB.
* **1-use_or_create_database**: Crea o cambia el contexto a la base de datos `my_db`.
* **2-insert**: Inserta un nuevo documento en la colección `school`.
* **3-all**: Lista todos los documentos dentro de la colección `school`.
* **4-match**: Lista todos los documentos que coinciden con un atributo específico (ej. nombre).
* **5-count**: Cuenta y muestra el número de documentos en la colección `school`.
* **6-update**: Actualiza un documento añadiendo un nuevo atributo.
* **7-delete**: Elimina todos los documentos que coinciden con una condición dada.

### Scripts de Python (`pymongo`)
* **8-all.py**: Función que lista todos los documentos de una colección dada.
* **9-insert_school.py**: Función que inserta un nuevo documento en una colección usando `**kwargs`.
* **10-update_topics.py**: Función que actualiza todos los temas (`topics`) de un documento escolar basándose en el nombre de la escuela.
* **11-schools_by_topic.py**: Función que busca y devuelve una lista de escuelas que contienen un tema específico.
* **12-log_stats.py**: Script que se conecta a la base de datos `logs`, analiza la colección `nginx` y provee estadísticas detalladas sobre los métodos HTTP y peticiones de estado.


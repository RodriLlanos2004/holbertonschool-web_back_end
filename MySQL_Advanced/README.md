# MySQL Advanced

Este proyecto abarca conceptos avanzados de bases de datos relacionales en MySQL, tales como la creación de Triggers, Procedimientos Almacenados (Stored Procedures), Funciones personalizadas, Vistas e Índices para optimización de consultas.

## Repositorio
* **GitHub repository:** `holbertonschool-web_back_end`
* **Directory:** `MySQL_Advanced`

## Lista de Tareas y Archivos

* **0-uniq_users.sql**: Crea una tabla `users` con un correo electrónico único.
* **1-country_users.sql**: Añade un atributo tipo `ENUM` (`US`, `CO`, `TN`) a la tabla `users`.
* **2-fans.sql**: Agrupa y ordena bandas de metal según su país de origen por el total de fans.
* **3-glam_rock.sql**: Lista bandas de *Glam rock* ordenadas por la cantidad de años activos.
* **4-store.sql**: Implementa un **Trigger** que disminuye el inventario tras crear una orden.
* **5-valid_email.sql**: Implementa un **Trigger** que resetea la validación de un correo si este se actualiza.
* **6-bonus.sql**: Crea un **Procedimiento Almacenado** (`AddBonus`) para registrar la calificación de un estudiante, creando el proyecto si no existe.
* **7-average_score.sql**: Crea un **Procedimiento Almacenado** (`ComputeAverageScoreForUser`) que calcula y actualiza el promedio de un estudiante.
* **8-index_my_names.sql**: Crea un **Índice** sobre la primera letra del nombre en una tabla de nombres para acelerar búsquedas.
* **9-index_name_score.sql**: Crea un **Índice Compuesto** sobre la primera letra del nombre y el puntaje.
* **10-div.sql**: Crea una **Función** (`SafeDiv`) para realizar divisiones seguras, retornando `0` si el divisor es `0`.
* **11-need_meeting.sql**: Crea una **Vista** (`need_meeting`) para filtrar estudiantes que requieren una reunión de seguimiento.

---
*Nota: Todos los scripts están diseñados para ser ejecutables directamente desde la consola usando `cat script.sql | mysql -uroot -p holberton`.*

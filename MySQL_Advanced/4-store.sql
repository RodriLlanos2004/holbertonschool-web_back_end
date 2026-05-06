-- Crea un trigger que disminuye la cantidad de un artículo tras agregar una nueva orden.
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;

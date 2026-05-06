-- Crea un trigger que reinicia el atributo valid_email a 0 solo si el email ha sido cambiado.
DELIMITER $$
CREATE TRIGGER reset_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;

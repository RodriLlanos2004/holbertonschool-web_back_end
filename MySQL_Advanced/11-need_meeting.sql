-- Crea una vista need_meeting con estudiantes con score < 80 y sin reunión en más de un mes.
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));

-- Crea un índice idx_name_first sobre la primera letra del campo name en la tabla names.
CREATE INDEX idx_name_first ON names (name(1));

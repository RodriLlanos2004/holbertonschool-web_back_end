-- Crea un índice sobre la primera letra de name y el score.
CREATE INDEX idx_name_first_score ON names (name(1), score);

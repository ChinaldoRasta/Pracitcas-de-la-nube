CREATE DATABASE IF NOT EXISTS biblioteca_crud
USE biblioteca_crud;

-- tabla editoriales
CREATE TABLE IF NOT EXISTS editoriales (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(120) NOT NULL UNIQUE,
  activo TINYINT(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB;

-- tabla libros
CREATE TABLE IF NOT EXISTS libros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_libro VARCHAR(180) NOT NULL,
  autor VARCHAR(160) NOT NULL,
  fecha_lanzamiento DATE NOT NULL,
  editorial_id INT NOT NULL,
  costo DECIMAL(10,2) NOT NULL,
  activo TINYINT(1) NOT NULL DEFAULT 1,
  creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  actualizado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_libros_editorial
    FOREIGN KEY (editorial_id) REFERENCES editoriales(id)
) ENGINE=InnoDB;

-- ejemplos para editoriales
INSERT INTO editoriales(nombre) VALUES
('Planeta'),
('Penguin Random House'),
('Alfaguara'),
('Anagrama'),
('Santillana');


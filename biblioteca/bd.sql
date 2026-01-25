CREATE DATABASE IF NOT EXISTS biblioteca_crud
USE biblioteca_crud;

-- Catálogo de editoriales
CREATE TABLE IF NOT EXISTS editoriales (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(120) NOT NULL UNIQUE,
  activo TINYINT(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB;

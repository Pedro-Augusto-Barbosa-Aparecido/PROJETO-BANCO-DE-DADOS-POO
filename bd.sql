-- -----------------------------------------------------
-- Schema projeto_lab
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema projeto_lab
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `proj_lab`;
CREATE SCHEMA IF NOT EXISTS `proj_lab` DEFAULT CHARACTER SET utf8 ;
USE `proj_lab` ;


-- -----------------------------------------------------
-- Table `projeto_lab`.`Veterinario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj_lab`.`Veterinario` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL UNIQUE,
  `endereco` VARCHAR(45) NULL,
  `telefone` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `projeto_lab`.`Localidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj_lab`.`Localidade` (
  `id` INT NOT NULL auto_increment,
  `rua` VARCHAR(45) NULL,
  `bairro` VARCHAR(45) NULL,
  `cidade` VARCHAR(45) NULL,
  `numero` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `projeto_lab`.`Clinica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj_lab`.`Clinica` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) not null,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  `endereco` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Clinica_Localidade1`
    FOREIGN KEY (`endereco`)
    REFERENCES `proj_lab`.`Localidade` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `projeto_lab`.`Clinica_has_Veterinario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj_lab`.`Clinica_has_Veterinario` (
  `clinica` INT NOT NULL,
  `veterinario` INT NOT NULL,
  PRIMARY KEY (`clinica`, `veterinario`),
  CONSTRAINT `fk_Clinica_has_Veterinario_Clinica1`
    FOREIGN KEY (`clinica`)
    REFERENCES `proj_lab`.`Clinica` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Clinica_has_Veterinario_Veterinario1`
    FOREIGN KEY (`veterinario`)
    REFERENCES `proj_lab`.`Veterinario` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `projeto_lab`.`Agendamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `proj_lab`.`Agendamento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NOT NULL,
  `created_at` DATETIME NULL,
  `modified_by` DATETIME NULL,
  `clinica` INT NOT NULL,
  `animal` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Agendamento_Clinica1`
    FOREIGN KEY (`clinica`)
    REFERENCES `proj_lab`.`Clinica` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE DATABASE IF NOT EXISTS `moodle2`;
USE `moodle2`;

###########################################
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(32) NOT NULL UNIQUE KEY,
    `firstName` varchar(100) NOT NULL,
    `secondName` varchar(100) not null,
    `firstLastName` varchar(100) not null,
    `secondLastName` varchar(100)not null,
    `password` VARCHAR(32) NOT NULL,
    `role` ENUM('teacher', 'student', 'admin') NOT NULL
);
CREATE TABLE IF NOT EXISTS `groups` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
    `shift` ENUM('Mat','Ves'),
    `desc` TEXT
);
CREATE TABLE IF NOT EXISTS `courses` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL,
    `user_owner` INT NOT NULL,
    FOREIGN KEY (`user_owner`)
        REFERENCES `users` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS `teams` (
    `id` INT NOT NULL,
    `team_no` INT NOT NULL,
    PRIMARY KEY (`id`)
);
CREATE TABLE IF NOT EXISTS `tasks` (
    `id` INT NOT NULL,
    `course_id` INT NOT NULL,
    `group_id` INT NOT NULL,
    `name` VARCHAR(100) NOT NULL,
    `type` ENUM('single','team'),
    `creationDate` DATE NOT NULL,
    `expireDate` DATE NOT NULL
);

##############################################
CREATE TABLE IF NOT EXISTS `group_members` ( # Lista: Alumnos en cada Grupo
    `user_id` INT NOT NULL,
    `group_id` INT NOT NULL,
    FOREIGN KEY (`user_id`)
        REFERENCES `users` (`id`),
    FOREIGN KEY (`group_id`)
        REFERENCES `groups` (`id`),
    UNIQUE KEY (`user_id`)
);
CREATE TABLE IF NOT EXISTS `team_members` ( # Lista: Alumnos en los diferentes equipos de trabajo de todas las materias
    `team_id` INT NOT NULL,
    FOREIGN KEY (`team_id`)
        REFERENCES `teams` (`id`),
    `group_id` INT NOT NULL,
    FOREIGN KEY (`group_id`)
        REFERENCES `groups` (`id`),
    `course_id` INT NOT NULL,
    FOREIGN KEY (`course_id`)
        REFERENCES `courses` (`id`)
);

INSERT INTO `groups` (`id`,`name`,`shift`,`desc`) VALUES(NULL,"3A","Mat","tercero A"),(NULL,"4A","Mat","Cuarto A");
INSERT INTO `users` (`id`,`username`,`firstName`,`secondName`,`firstLastName`,`secondLastName`,`password`,`role`) values (NULL, "Kevinazzzo","Kevin","","Miranda","Luna","1234","student");

SELECT * FROM `groups`;
SELECT `username`, `password` FROM `users` WHERE `username`="Kevinazzzo" AND `password`="1234";

DELETE from `groups` WHERE `id` >0;
DROP DATABASE `moodle2`;
SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `countsclean`;
CREATE TABLE `countclean` (
  `year` int NOT NULL,
  `month` int NOT NULL,
  `day` int NOT NULL,
  `hour` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `count` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
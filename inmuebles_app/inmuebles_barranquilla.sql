-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-05-2025 a las 23:47:03
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inmuebles_barranquilla`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registros_inmuebles`
--

CREATE TABLE `registros_inmuebles` (
  `id` int(11) NOT NULL,
  `registro_scuep` varchar(50) DEFAULT NULL,
  `anio` int(11) DEFAULT NULL,
  `proyecto` varchar(255) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `unidades` int(11) DEFAULT NULL,
  `enajenador` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registros_inmuebles`
--

INSERT INTO `registros_inmuebles` (`id`, `registro_scuep`, `anio`, `proyecto`, `direccion`, `unidades`, `enajenador`) VALUES
(2, '573-01', 2008, 'PoloAS', 'Cr22 D', 20, 'Pol');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `registros_inmuebles`
--
ALTER TABLE `registros_inmuebles`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `registros_inmuebles`
--
ALTER TABLE `registros_inmuebles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

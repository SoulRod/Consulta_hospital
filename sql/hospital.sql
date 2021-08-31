-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-08-2021 a las 04:37:13
-- Versión del servidor: 10.4.19-MariaDB
-- Versión de PHP: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hospital`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consulta`
--

CREATE TABLE `consulta` (
  `id` int(11) NOT NULL,
  `cantPacientes` int(11) NOT NULL,
  `nombreEspecialista` varchar(100) NOT NULL,
  `tipoConsulta` varchar(100) NOT NULL,
  `estado` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `nombre` varchar(100) NOT NULL,
  `edad` int(100) NOT NULL,
  `nhistoriaclinica` int(11) NOT NULL,
  `tieneDieta` varchar(100) NOT NULL,
  `relacionPeso` int(11) NOT NULL,
  `fumador` varchar(100) NOT NULL,
  `prioridad` int(11) NOT NULL,
  `riesgo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`nhistoriaclinica`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `nhistoriaclinica` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

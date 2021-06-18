-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2020 at 09:13 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `militarya`
--

-- --------------------------------------------------------

--
-- Table structure for table `camp`
--

CREATE TABLE `camp` (
  `Camp_ID` varchar(100) NOT NULL,
  `Camp_Name` varchar(100) NOT NULL,
  `Camp_No` int(100) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `contact` int(100) NOT NULL,
  `Tent_No` int(100) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `camp`
--

INSERT INTO `camp` (`Camp_ID`, `Camp_Name`, `Camp_No`, `Title`, `contact`, `Tent_No`, `address`) VALUES
('12', 'ktm', 1, 'Defense', 132, 1, 'balaju'),
('17', 'ktm', 1, 'Defense', 132, 1, 'balaju'),
('18', 'ktm', 1, 'Defense', 132, 1, 'balaju'),
('2', 'Pokhara', 10, 'Sniper', 1234, 5, 'New Road'),
('3', 'Pokhara', 3, 'Sniper', 1234, 4, 'Zero Km'),
('4', 'pkra', 3, 'Sniper', 1234, 4, 'pkr'),
('5', 'k', 2, 'Peace', 8, 324, 'd'),
('7', 'ktm', 1, 'Defense', 132, 1, 'balaju');

-- --------------------------------------------------------

--
-- Table structure for table `info`
--

CREATE TABLE `info` (
  `Citizenship_No` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `Camp_ID` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` int(100) NOT NULL,
  `height` int(100) NOT NULL,
  `post` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `info`
--

INSERT INTO `info` (`Citizenship_No`, `name`, `Camp_ID`, `gender`, `contact`, `height`, `post`) VALUES
('11', 'jimi', '5', 'Male', 1234, 5, 'Senior'),
('2', 'fg', '2', 'Female', 86, 76, 'hg'),
('5', 'fg', '2', 'Female', 657, 6, 'jg'),
('56', 'ram', '2', 'Male', 132, 5, 'Captain'),
('6', 'fg', '3', 'Male', 657, 6, 'jg');

-- --------------------------------------------------------

--
-- Table structure for table `iq`
--

CREATE TABLE `iq` (
  `Citi_ID` int(11) NOT NULL,
  `NAME` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `wep`
--

CREATE TABLE `wep` (
  `Weapon_type` varchar(100) NOT NULL,
  `Weapon_Name` varchar(100) NOT NULL,
  `Weapon_No` int(100) NOT NULL,
  `Bullet_qty` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wep`
--

INSERT INTO `wep` (`Weapon_type`, `Weapon_Name`, `Weapon_No`, `Bullet_qty`) VALUES
('AR', 'm416', 1, 180),
('Sniper', 'kr98', 2, 180),
('SMG', 'uzi', 3, 180),
('LMG', 'm249', 4, 180),
('Grenade', 'Smoke', 5, 180),
('Air', 'zet72', 6, 180),
('Land', 'BRDM', 7, 180),
('AR', 'akm', 9, 180),
('AR', 'm416', 71, 100),
('AR', 'm416', 72, 100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `camp`
--
ALTER TABLE `camp`
  ADD PRIMARY KEY (`Camp_ID`);

--
-- Indexes for table `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`Citizenship_No`),
  ADD KEY `Camp_ID` (`Camp_ID`);

--
-- Indexes for table `iq`
--
ALTER TABLE `iq`
  ADD PRIMARY KEY (`Citi_ID`);

--
-- Indexes for table `wep`
--
ALTER TABLE `wep`
  ADD PRIMARY KEY (`Weapon_No`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `info`
--
ALTER TABLE `info`
  ADD CONSTRAINT `info_ibfk_1` FOREIGN KEY (`Camp_ID`) REFERENCES `camp` (`Camp_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

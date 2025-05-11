-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 11, 2025 at 07:27 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ai_fitness_tracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `bicep_curls`
--

CREATE TABLE `bicep_curls` (
  `id` int(11) NOT NULL,
  `left_count` int(11) NOT NULL DEFAULT 0,
  `right_count` int(11) NOT NULL DEFAULT 0,
  `total_count` int(11) NOT NULL DEFAULT 0,
  `date_time` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bicep_curls`
--

INSERT INTO `bicep_curls` (`id`, `left_count`, `right_count`, `total_count`, `date_time`) VALUES
(1, 5, 6, 11, '2025-04-13 18:41:22'),
(2, 5, 6, 11, '2025-04-13 18:42:40'),
(3, 1, 1, 2, '2025-04-13 18:46:05'),
(4, 3, 3, 6, '2025-04-13 19:22:44'),
(5, 0, 0, 0, '2025-04-13 19:31:24'),
(6, 0, 0, 0, '2025-04-14 11:52:10'),
(7, 0, 0, 0, '2025-04-14 11:54:17'),
(8, 3, 3, 6, '2025-04-14 12:51:23'),
(9, 3, 3, 6, '2025-04-14 12:51:25'),
(10, 3, 3, 6, '2025-04-14 12:52:11'),
(11, 3, 3, 6, '2025-04-14 12:52:13'),
(12, 2, 2, 4, '2025-04-14 12:55:43'),
(13, 1, 1, 2, '2025-04-14 12:55:58'),
(14, 2, 2, 4, '2025-04-14 13:00:13'),
(15, 6, 9, 15, '2025-04-14 13:02:55'),
(16, 1, 2, 3, '2025-04-14 19:42:46'),
(17, 4, 4, 8, '2025-04-14 20:00:24'),
(18, 2, 2, 4, '2025-04-15 22:00:53'),
(19, 2, 2, 4, '2025-04-15 22:00:53'),
(20, 2, 2, 4, '2025-04-16 14:27:43'),
(21, 2, 2, 4, '2025-04-16 14:27:43'),
(22, 4, 5, 9, '2025-04-17 01:51:52'),
(23, 11, 9, 20, '2025-04-17 01:53:43'),
(24, 1, 1, 2, '2025-04-17 01:56:17'),
(25, 2, 2, 4, '2025-04-20 15:39:20'),
(26, 1, 1, 2, '2025-04-25 17:33:05'),
(27, 3, 3, 6, '2025-04-25 17:33:29'),
(28, 5, 5, 10, '2025-04-26 10:41:45'),
(29, 1, 1, 2, '2025-04-26 10:47:26'),
(30, 2, 2, 4, '2025-04-26 10:51:00');

-- --------------------------------------------------------

--
-- Table structure for table `deadlifts`
--

CREATE TABLE `deadlifts` (
  `id` int(11) NOT NULL,
  `left_count` int(11) NOT NULL DEFAULT 0,
  `right_count` int(11) NOT NULL DEFAULT 0,
  `total_count` int(11) NOT NULL DEFAULT 0,
  `date_time` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `deadlifts`
--

INSERT INTO `deadlifts` (`id`, `left_count`, `right_count`, `total_count`, `date_time`) VALUES
(1, 3, 4, 7, '2025-04-13 18:42:40'),
(2, 1, 1, 2, '2025-04-13 19:06:11'),
(3, 1, 1, 2, '2025-04-13 19:07:55'),
(4, 0, 0, 0, '2025-04-13 19:32:12'),
(5, 1, 1, 2, '2025-04-13 19:34:32'),
(6, 0, 0, 0, '2025-04-14 11:52:31'),
(7, 0, 0, 0, '2025-04-14 11:53:52'),
(8, 1, 3, 4, '2025-04-14 12:15:04'),
(9, 3, 3, 6, '2025-04-14 12:52:39'),
(10, 2, 2, 4, '2025-04-14 12:53:02'),
(11, 1, 1, 2, '2025-04-17 01:39:42'),
(12, 1, 1, 2, '2025-04-17 01:49:31'),
(13, 2, 10, 12, '2025-04-17 01:55:34'),
(14, 1, 1, 2, '2025-04-25 20:41:57'),
(15, 2, 2, 4, '2025-04-25 20:46:45'),
(16, 2, 2, 4, '2025-04-26 10:41:15'),
(17, 1, 1, 2, '2025-04-26 10:43:09'),
(18, 3, 3, 6, '2025-04-26 10:46:56');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bicep_curls`
--
ALTER TABLE `bicep_curls`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `deadlifts`
--
ALTER TABLE `deadlifts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bicep_curls`
--
ALTER TABLE `bicep_curls`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `deadlifts`
--
ALTER TABLE `deadlifts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

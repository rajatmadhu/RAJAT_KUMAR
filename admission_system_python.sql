-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2018 at 08:43 PM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `admission_system_python`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(5) NOT NULL,
  `admin_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `admin_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `admin_pass` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `admin_id`, `admin_name`, `admin_pass`) VALUES
(1, 'admin_20181', 'admin', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(5) NOT NULL,
  `user_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `user_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `security_question` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `security_answer` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `user_pass` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `date_of_birth` varchar(100) DEFAULT NULL,
  `mother_name` varchar(100) DEFAULT NULL,
  `father_name` varchar(100) DEFAULT NULL,
  `occupation` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `blood_group` varchar(100) DEFAULT NULL,
  `marital_status` varchar(100) DEFAULT NULL,
  `total_marks_10` varchar(100) DEFAULT NULL,
  `board_10` varchar(100) DEFAULT NULL,
  `institute_10` varchar(100) DEFAULT NULL,
  `year_of_passing_10` varchar(100) DEFAULT NULL,
  `percentage_10` varchar(100) DEFAULT NULL,
  `total_marks_12` varchar(100) DEFAULT NULL,
  `board_12` varchar(100) DEFAULT NULL,
  `institute_12` varchar(100) DEFAULT NULL,
  `year_of_passing_12` varchar(100) DEFAULT NULL,
  `percentage_12` varchar(100) DEFAULT NULL,
  `total_marks_grad` varchar(100) DEFAULT NULL,
  `board_grad` varchar(100) DEFAULT NULL,
  `institute_grad` varchar(100) DEFAULT NULL,
  `year_of_passing_grad` varchar(100) DEFAULT NULL,
  `percentage_grad` varchar(100) DEFAULT NULL,
  `jeca_roll` varchar(100) DEFAULT NULL,
  `jeca_rank` varchar(100) DEFAULT NULL,
  `jeca_reg` varchar(100) DEFAULT NULL,
  `dd_no` varchar(100) DEFAULT NULL,
  `dd_bank_name` varchar(100) DEFAULT NULL,
  `dd_branch_name` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `distict` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `mobile_number` varchar(100) DEFAULT NULL,
  `is_submitted` int(5) DEFAULT '0',
  `is_pending` int(5) DEFAULT '0',
  `is_verified` int(5) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `user_id`, `user_name`, `security_question`, `security_answer`, `user_pass`, `first_name`, `middle_name`, `last_name`, `date_of_birth`, `mother_name`, `father_name`, `occupation`, `gender`, `blood_group`, `marital_status`, `total_marks_10`, `board_10`, `institute_10`, `year_of_passing_10`, `percentage_10`, `total_marks_12`, `board_12`, `institute_12`, `year_of_passing_12`, `percentage_12`, `total_marks_grad`, `board_grad`, `institute_grad`, `year_of_passing_grad`, `percentage_grad`, `jeca_roll`, `jeca_rank`, `jeca_reg`, `dd_no`, `dd_bank_name`, `dd_branch_name`, `address`, `city`, `distict`, `state`, `pincode`, `mobile_number`, `is_submitted`, `is_pending`, `is_verified`) VALUES
(3, 'reg_20181', 'sam', 'country?', 'Indian', '1234', 'Sumon', '', 'Das', '05/01/1996', 'Sova Das', 'Tapan Das', 'student', 'Male', 'A+', 'single', '656', 'WBBSE', 'SPBN', '2011', '82', '373', 'WBCHSE', 'svm', '2013', '72.6', '508', 'Burdwan', 'BB', '2016', '63.25', '123456', '1234567', '1234568', '123456789', 'BOI', 'BURNPUR', 'BURNPUR1', 'ASANSOL', 'BURDWAN', 'WB', '713325', '8293156938', 1, 0, 1),
(4, 'reg_20182', 'samson', 'pet?', 'cat', '12345678', 'sam', '', 'Doe', '12/05/1997', 'maary', 'jombie', 'nothing', 'Female', 'o-', 'Single', '100', 'wbcs', 'abcd', '2012', '25', '200', 'ches', 'defg', '2014', '25', '300', 'ass', 'uerrue', '2017', '50', '1234', '100', '12345', '123336', 'burn', 'pur', 'askajkasjkaj', 'burnpur', 'burdwan', 'W BENGAL', '713325', '8945806271', 1, 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `admin_id` (`admin_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

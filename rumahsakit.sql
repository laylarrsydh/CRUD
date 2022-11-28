-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2022 at 06:09 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rumahsakit`
--

-- --------------------------------------------------------

--
-- Table structure for table `dokter`
--

CREATE TABLE `dokter` (
  `ID_dokter` int(5) NOT NULL,
  `Nama_dokter` varchar(25) NOT NULL,
  `Spesialis` int(25) NOT NULL,
  `No_telepon` int(13) NOT NULL,
  `Alamat` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dokter`
--

INSERT INTO `dokter` (`ID_dokter`, `Nama_dokter`, `Spesialis`, `No_telepon`, `Alamat`) VALUES
(142, 'Lee Jeno', 1331, 8429345, 'Seoul. Korea');

-- --------------------------------------------------------

--
-- Table structure for table `kamar`
--

CREATE TABLE `kamar` (
  `No_kamar` int(2) NOT NULL,
  `Nama` varchar(25) NOT NULL,
  `Jenis` varchar(20) NOT NULL,
  `Kapasitas` varchar(15) NOT NULL,
  `Fasilitas` varchar(10) NOT NULL,
  `Harga` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kamar`
--

INSERT INTO `kamar` (`No_kamar`, `Nama`, `Jenis`, `Kapasitas`, `Fasilitas`, `Harga`) VALUES
(11, 'Ruang Anggrek', 'VVIP', '5 Orang', '1 Bed', 'Rp3.000.000'),
(21, 'Ruang Melati', 'Kelas I', '6 orang', '2 Bed', 'Rp750.000'),
(33, 'Ruang Aster', 'Kelas II', '8 Orang', '4 Bed', 'Rp500.000');

-- --------------------------------------------------------

--
-- Table structure for table `obat`
--

CREATE TABLE `obat` (
  `Kode_obat` int(2) NOT NULL,
  `Nama_obat` varchar(225) NOT NULL,
  `jenis` varchar(20) NOT NULL,
  `tahun_produksi` year(4) NOT NULL,
  `masa_berlaku` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `obat`
--

INSERT INTO `obat` (`Kode_obat`, `Nama_obat`, `jenis`, `tahun_produksi`, `masa_berlaku`) VALUES
(11, 'Decolgen', 'Tablet', 2022, 'Jan 2024'),
(12, 'Antasida', 'Tablet', 2022, 'Mei 2024'),
(15, 'Oralit', 'Serbuk', 2022, 'Jan 2025'),
(17, 'Antasida', 'Tablet', 2022, 'Mei 2024'),
(19, 'Paracetamol', 'Tablet', 2022, 'Jan 2024'),
(20, 'Vit D3 1000IU', 'Kapsul', 2022, 'Juli 2024'),
(23, 'Omeprazol', 'Kapsul', 2022, 'Mei 2024'),
(25, 'Fluimucin', 'Dry Syrup', 2022, 'Mar 2024'),
(30, 'Azithromycin', 'Tablet', 2022, 'Mei 2024'),
(31, 'Acetylsisteine', 'Kapsul', 2022, 'Mei 2024'),
(32, 'Ponstan', 'Salut Selaput', 2022, 'Mar 2024'),
(33, 'Ataroc', 'Syrup', 2022, 'Nov 2023');

-- --------------------------------------------------------

--
-- Table structure for table `pasien`
--

CREATE TABLE `pasien` (
  `ID` int(5) NOT NULL,
  `Nama` varchar(25) NOT NULL,
  `Tanggal_Lahir` date NOT NULL,
  `Jenis_Kelamin` char(1) NOT NULL,
  `No_Telepon` int(13) NOT NULL,
  `Alamat` varchar(15) NOT NULL,
  `Status` int(2) NOT NULL,
  `Obat` varchar(225) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT current_timestamp(),
  `Updated` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `perawat`
--

CREATE TABLE `perawat` (
  `ID_perawat` int(5) NOT NULL,
  `Nama` varchar(15) NOT NULL,
  `Jenis_kelamin` char(1) NOT NULL,
  `No_telepon` int(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `perawat`
--

INSERT INTO `perawat` (`ID_perawat`, `Nama`, `Jenis_kelamin`, `No_telepon`) VALUES
(471, 'Kim Jungwoo', 'L', 812834632),
(484, 'Xiao Dejun', 'L', 81284252);

-- --------------------------------------------------------

--
-- Table structure for table `rekammedis`
--

CREATE TABLE `rekammedis` (
  `ID_RM` int(3) NOT NULL,
  `Tanggal` date NOT NULL,
  `Keluhan` varchar(20) NOT NULL,
  `Pemeriksaan` varchar(10) NOT NULL,
  `Pengobatan` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rekammedis`
--

INSERT INTO `rekammedis` (`ID_RM`, `Tanggal`, `Keluhan`, `Pemeriksaan`, `Pengobatan`) VALUES
(101, '2022-11-15', 'Demam', 'Lab Darah', 'Rawat Jalan'),
(102, '2022-11-20', 'Sesak Nafas', 'Rontgen', 'Rawat Jalan'),
(106, '2022-11-14', 'Anemia', 'Lab Darah', 'Rawat Jalan'),
(108, '2022-11-19', 'Sakit Perut', 'USG', 'Rawat Jalan'),
(120, '2022-11-20', 'Gastritis', 'Endoskopi', 'Rawat Inap'),
(203, '2022-11-18', 'Fracture', 'Rontgen', 'Rawat Inap'),
(205, '2022-11-20', 'Batuk', 'Tes Lendir', 'Rawat Inap');

-- --------------------------------------------------------

--
-- Table structure for table `spesialis`
--

CREATE TABLE `spesialis` (
  `ID_spesialis` int(10) NOT NULL,
  `Nama_spesialis` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `spesialis`
--

INSERT INTO `spesialis` (`ID_spesialis`, `Nama_spesialis`) VALUES
(1034, 'Onkologi'),
(1293, 'Paru Paru'),
(1331, 'Anak'),
(4921, 'Patologi'),
(5431, 'Jantung');

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `ID_stp` int(2) NOT NULL,
  `Ket` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`ID_stp`, `Ket`) VALUES
(2, 'Rawat Inap'),
(1, 'Rawat Jalan');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `username` varchar(25) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`username`, `password`) VALUES
('laylarsydh', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dokter`
--
ALTER TABLE `dokter`
  ADD PRIMARY KEY (`ID_dokter`),
  ADD KEY `Spesialis` (`Spesialis`);

--
-- Indexes for table `kamar`
--
ALTER TABLE `kamar`
  ADD PRIMARY KEY (`No_kamar`);

--
-- Indexes for table `obat`
--
ALTER TABLE `obat`
  ADD PRIMARY KEY (`Kode_obat`),
  ADD KEY `Nama_obat` (`Nama_obat`);

--
-- Indexes for table `pasien`
--
ALTER TABLE `pasien`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `Status` (`Status`),
  ADD KEY `Obat` (`Obat`);

--
-- Indexes for table `perawat`
--
ALTER TABLE `perawat`
  ADD PRIMARY KEY (`ID_perawat`);

--
-- Indexes for table `rekammedis`
--
ALTER TABLE `rekammedis`
  ADD PRIMARY KEY (`ID_RM`),
  ADD KEY `Pengobatan` (`Pengobatan`);

--
-- Indexes for table `spesialis`
--
ALTER TABLE `spesialis`
  ADD PRIMARY KEY (`ID_spesialis`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`ID_stp`),
  ADD KEY `Ket` (`Ket`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dokter`
--
ALTER TABLE `dokter`
  MODIFY `ID_dokter` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=503;

--
-- AUTO_INCREMENT for table `kamar`
--
ALTER TABLE `kamar`
  MODIFY `No_kamar` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `obat`
--
ALTER TABLE `obat`
  MODIFY `Kode_obat` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `pasien`
--
ALTER TABLE `pasien`
  MODIFY `ID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22068;

--
-- AUTO_INCREMENT for table `rekammedis`
--
ALTER TABLE `rekammedis`
  MODIFY `ID_RM` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=292;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `dokter`
--
ALTER TABLE `dokter`
  ADD CONSTRAINT `dokter_ibfk_1` FOREIGN KEY (`Spesialis`) REFERENCES `spesialis` (`ID_spesialis`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `pasien`
--
ALTER TABLE `pasien`
  ADD CONSTRAINT `pasien_ibfk_1` FOREIGN KEY (`Status`) REFERENCES `status` (`ID_stp`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

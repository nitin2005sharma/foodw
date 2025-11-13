<<<<<<< HEAD
<p align = "center">
<h1> 
  FAPP Database

</h1>
</p>



<p align ="center">
    
</p>

## About the Project 🚀
FAPP is a food delivery app that connects customers with multiple restaurants and displays their menus, user-ratings and provides a vast number of food delivery options. The database centralizes the operations of FAPP and provides a smooth user interface wherein donors can easily donate items without any hassle, and the users can select and order from the best restaurants with unbiased ratings from other customers who have ordered before.

Through this project, we aim to reduce food wastage and help the organizations which work for the welfare of people get easier access to resources and create a platform that incentivizes and makes it easy to donate.



=======
# food-and-waste-managment-system
>>>>>>> d3d9ed0ae7a402f6f17a416f071d557a61999e3a
-- MySQL dump 10.13  )
--
-- Host: localhost    Database: fdatabse
-- ------------------------------------------------------
-

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Contains`
--

DROP TABLE IF EXISTS `Contains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Contains` (
  `foodID` varchar(8) NOT NULL,
  `orderID` varchar(8) NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`foodID`,`orderID`),
  KEY `foodID` (`foodID`),
  KEY `orderID` (`orderID`),
  CONSTRAINT `Contains_ibfk_1` FOREIGN KEY (`foodID`) REFERENCES `Food` (`itemID`),
  CONSTRAINT `Contains_ibfk_2` FOREIGN KEY (`orderID`) REFERENCES `Orders` (`orderID`),
  CONSTRAINT `Contains_chk_1` CHECK ((`quantity` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contains`
--


--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `phone` char(10) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `email` varchar(50) NOT NULL,
  `customerType` varchar(20) NOT NULL,
  `dob` date DEFAULT NULL,
  PRIMARY KEY (`phone`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  KEY `nearby_cust` (`area`),
  CONSTRAINT `typeContraint` CHECK (((`customerType` = _utf8mb4'normal') or (`customerType` = _utf8mb4'premium')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--



--
-- Temporary view structure for view `CustomerDetails`
--

DROP TABLE IF EXISTS `CustomerDetails`;
/*!50001 DROP VIEW IF EXISTS `CustomerDetails`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `CustomerDetails` AS SELECT 
 1 AS `phone`,
 1 AS `fName`,
 1 AS `lName`,
 1 AS `email`,
 1 AS `state`,
 1 AS `customerType`,
 1 AS `dob`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `DeliveryWorker`
--

DROP TABLE IF EXISTS `DeliveryWorker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DeliveryWorker` (
  `employeeID` varchar(8) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `phone` char(10) NOT NULL,
  `salary` int NOT NULL,
  `dob` date NOT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `socialCause` tinyint(1) NOT NULL DEFAULT '0',
  `tips` int NOT NULL DEFAULT '0',
  `supervisorID` varchar(8) NOT NULL,
  `fuelAmt` int NOT NULL DEFAULT '2000',
  PRIMARY KEY (`employeeID`),
  UNIQUE KEY `phone` (`phone`),
  KEY `supervisorID` (`supervisorID`),
  CONSTRAINT `DeliveryWorker_ibfk_1` FOREIGN KEY (`supervisorID`) REFERENCES `Management` (`employeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DeliveryWorker`
--



--
-- Temporary view structure for view `DeliveryWorkerDetails`
--

DROP TABLE IF EXISTS `DeliveryWorkerDetails`;
/*!50001 DROP VIEW IF EXISTS `DeliveryWorkerDetails`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `DeliveryWorkerDetails` AS SELECT 
 1 AS `employeeID`,
 1 AS `fName`,
 1 AS `lName`,
 1 AS `phone`,
 1 AS `socialCause`,
 1 AS `supervisorID`,
 1 AS `dob`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Donation`
--

DROP TABLE IF EXISTS `Donation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Donation` (
  `donationID` varchar(9) NOT NULL,
  `donorID` varchar(8) NOT NULL,
  `receiverID` varchar(8) DEFAULT NULL,
  `deliveryWorkerID` varchar(8) NOT NULL,
  `dateTime` date DEFAULT NULL,
  `category` varchar(10) NOT NULL,
  `status` varchar(15) NOT NULL DEFAULT 'active',
  `quantity` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`donationID`),
  KEY `donorID` (`donorID`),
  KEY `receiverID` (`receiverID`),
  KEY `deliveryWorkerID` (`deliveryWorkerID`),
  KEY `delivery` (`deliveryWorkerID`),
  CONSTRAINT `Donation_ibfk_1` FOREIGN KEY (`donorID`) REFERENCES `Donor` (`donorID`),
  CONSTRAINT `Donation_ibfk_2` FOREIGN KEY (`receiverID`) REFERENCES `Receiver` (`receiverID`),
  CONSTRAINT `Donation_ibfk_3` FOREIGN KEY (`deliveryWorkerID`) REFERENCES `DeliveryWorker` (`employeeID`),
  CONSTRAINT `Donation_chk_2` CHECK (((`status` = _utf8mb4'active') or (`status` = _utf8mb4'delivered'))),
  CONSTRAINT `donationType` CHECK (((`category` = _utf8mb4'Meals') or (`category` = _utf8mb4'Clothes') or (`category` = _utf8mb4'Money')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Donation`
--



--
-- Table structure for table `Donor`
--

DROP TABLE IF EXISTS `Donor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Donor` (
  `donorID` varchar(8) NOT NULL,
  `phone` char(10) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `points` int DEFAULT '0',
  PRIMARY KEY (`donorID`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Donor`
--


--
-- Temporary view structure for view `DonorDetails`
--

DROP TABLE IF EXISTS `DonorDetails`;
/*!50001 DROP VIEW IF EXISTS `DonorDetails`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `DonorDetails` AS SELECT 
 1 AS `donorID`,
 1 AS `phone`,
 1 AS `name`,
 1 AS `state`,
 1 AS `points`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Food`
--

DROP TABLE IF EXISTS `Food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Food` (
  `itemID` varchar(8) NOT NULL,
  `name` varchar(100) NOT NULL,
  `price` decimal(7,2) NOT NULL,
  `isAvailable` tinyint(1) NOT NULL DEFAULT '1',
  `imagePath` varchar(200) DEFAULT NULL,
  `isVeg` tinyint(1) NOT NULL,
  `category` varchar(20) DEFAULT NULL,
  `discount` int DEFAULT '0',
  `restaurantID` varchar(8) NOT NULL,
  PRIMARY KEY (`itemID`),
  KEY `restaurantID` (`restaurantID`),
  KEY `served_by` (`restaurantID`),
  CONSTRAINT `Food_ibfk_1` FOREIGN KEY (`restaurantID`) REFERENCES `Restaurant` (`restaurantID`),
  CONSTRAINT `Food_chk_1` CHECK (((`category` = _utf8mb4'Dessert') or (`category` = _utf8mb4'Main Course') or (`category` = _utf8mb4'Beverage') or (`category` = _utf8mb4'Starter')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Food`
--



--
-- Table structure for table `Management`
--

DROP TABLE IF EXISTS `Management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Management` (
  `employeeID` varchar(8) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `phone` char(10) NOT NULL,
  `salary` int NOT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`employeeID`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Management`
--


/*!40000 ALTER TABLE `Management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `ManagementDetails`
--

DROP TABLE IF EXISTS `ManagementDetails`;
/*!50001 DROP VIEW IF EXISTS `ManagementDetails`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ManagementDetails` AS SELECT 
 1 AS `employeeID`,
 1 AS `fName`,
 1 AS `lName`,
 1 AS `phone`,
 1 AS `state`,
 1 AS `dob`,
 1 AS `designation`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `orderID` varchar(8) NOT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'Active',
  `dateTime` datetime NOT NULL,
  `billAmt` decimal(6,2) NOT NULL,
  `paymentMode` varchar(20) NOT NULL,
  `customerID` char(10) NOT NULL,
  `restaurantID` varchar(8) NOT NULL,
  `deliveryWorkerID` varchar(8) NOT NULL,
  `discount` int DEFAULT '0',
  `tip` decimal(5,2) DEFAULT (0),
  PRIMARY KEY (`orderID`),
  KEY `customerID` (`customerID`),
  KEY `restaurantID` (`restaurantID`),
  KEY `deliveryWorkerID` (`deliveryWorkerID`),
  KEY `delivery` (`deliveryWorkerID`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`phone`),
  CONSTRAINT `Orders_ibfk_2` FOREIGN KEY (`restaurantID`) REFERENCES `Restaurant` (`restaurantID`),
  CONSTRAINT `Orders_ibfk_3` FOREIGN KEY (`deliveryWorkerID`) REFERENCES `DeliveryWorker` (`employeeID`),
  CONSTRAINT `Orders_chk_1` CHECK (((`status` = _utf8mb4'active') or (`status` = _utf8mb4'delivered')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--



--
-- Table structure for table `Rates`
--

DROP TABLE IF EXISTS `Rates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Rates` (
  `ratings` int DEFAULT NULL,
  `customerID` char(10) NOT NULL,
  `restaurantID` varchar(8) NOT NULL,
  PRIMARY KEY (`customerID`,`restaurantID`),
  KEY `customerID` (`customerID`),
  KEY `restaurantID` (`restaurantID`),
  KEY `rating_rest` (`restaurantID`,`ratings`),
  CONSTRAINT `Rates_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`phone`),
  CONSTRAINT `Rates_ibfk_2` FOREIGN KEY (`restaurantID`) REFERENCES `Restaurant` (`restaurantID`),
  CONSTRAINT `Rates_chk_1` CHECK (((`ratings` > 0) and (`ratings` < 6)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rates`
--


--
-- Table structure for table `Receiver`
--

DROP TABLE IF EXISTS `Receiver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Receiver` (
  `receiverID` varchar(8) NOT NULL,
  `phone` char(10) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `hNo` varchar(6) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` char(6) NOT NULL,
  `accepts` varchar(20) NOT NULL,
  PRIMARY KEY (`receiverID`),
  UNIQUE KEY `phone` (`phone`),
  KEY `nearby_rec` (`area`),
  KEY `accepted` (`accepts`),
  CONSTRAINT `Receiver_chk_1` CHECK (((`accepts` = _utf8mb4'Meals') or (`accepts` = _utf8mb4'Money') or (`accepts` = _utf8mb4'Clothes')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Receiver`
--


--
-- Temporary view structure for view `ReceiverDetails`
--

DROP TABLE IF EXISTS `ReceiverDetails`;
/*!50001 DROP VIEW IF EXISTS `ReceiverDetails`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ReceiverDetails` AS SELECT 
 1 AS `receiverID`,
 1 AS `name`,
 1 AS `phone`,
 1 AS `state`,
 1 AS `accepts`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Restaurant`
--

DROP TABLE IF EXISTS `Restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Restaurant` (
  `restaurantID` varchar(8) NOT NULL,
  `type` varchar(30) DEFAULT NULL,
  `dayOfOpening` date DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `phone` char(10) NOT NULL,
  `street` varchar(20) DEFAULT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `area` varchar(20) NOT NULL,
  `isDineIn` tinyint(1) DEFAULT NULL,
  `sNo` varchar(6) NOT NULL,
  PRIMARY KEY (`restaurantID`),
  KEY `nearby_rest` (`area`),
  CONSTRAINT `checkRestaurantType` CHECK (((`type` = _utf8mb4'South Indian') or (`type` = _utf8mb4'Mexican') or (`type` = _utf8mb4'Continental') or (`type` = _utf8mb4'Fast Food') or (`type` = _utf8mb4'Mughlai') or (`type` = _utf8mb4'North Indian') or (`type` = _utf8mb4'Chinese')))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Restaurant`
--

/*!50001 VIEW `CustomerDetails` AS select `Customer`.`phone` AS `phone`,`Customer`.`fName` AS `fName`,`Customer`.`lName` AS `lName`,`Customer`.`email` AS `email`,`Customer`.`state` AS `state`,`Customer`.`customerType` AS `customerType`,`Customer`.`dob` AS `dob` from `Customer` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `DeliveryWorkerDetails`
--

/*!50001 DROP VIEW IF EXISTS `DeliveryWorkerDetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `DeliveryWorkerDetails` AS select `DeliveryWorker`.`employeeID` AS `employeeID`,`DeliveryWorker`.`fName` AS `fName`,`DeliveryWorker`.`lName` AS `lName`,`DeliveryWorker`.`phone` AS `phone`,`DeliveryWorker`.`socialCause` AS `socialCause`,`DeliveryWorker`.`supervisorID` AS `supervisorID`,`DeliveryWorker`.`dob` AS `dob` from `DeliveryWorker` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `DonorDetails`
--

/*!50001 DROP VIEW IF EXISTS `DonorDetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `DonorDetails` AS select `Donor`.`donorID` AS `donorID`,`Donor`.`phone` AS `phone`,`Donor`.`name` AS `name`,`Donor`.`state` AS `state`,`Donor`.`points` AS `points` from `Donor` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `ManagementDetails`
--

/*!50001 DROP VIEW IF EXISTS `ManagementDetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ManagementDetails` AS select `Management`.`employeeID` AS `employeeID`,`Management`.`fName` AS `fName`,`Management`.`lName` AS `lName`,`Management`.`phone` AS `phone`,`Management`.`state` AS `state`,`Management`.`dob` AS `dob`,`Management`.`designation` AS `designation` from `Management` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `ReceiverDetails`
--

/*!50001 DROP VIEW IF EXISTS `ReceiverDetails`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ReceiverDetails` AS select `Receiver`.`receiverID` AS `receiverID`,`Receiver`.`name` AS `name`,`Receiver`.`phone` AS `phone`,`Receiver`.`state` AS `state`,`Receiver`.`accepts` AS `accepts` from `Receiver` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-08 17:34:35


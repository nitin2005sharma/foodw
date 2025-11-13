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

from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta, datetime
from random import randint

import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Nitin@200527", database="fdatabase" )
app = Flask (__name__)
app.permanent_session_lifetime = timedelta(days = 1)
app.secret_key = "khidmatDB"
mycursor = mydb.cursor()

@app.route("/", methods= ["POST", "GET"])
def login():
    if(request.method == "GET"):
        return render_template("login.html")
    else:
        print(request.form)
        username = request.form["username"]
        password = request.form["password"]
        typeOf = request.form["typeOf"] 
        q=""
        if(typeOf == "Customer"):
            q=f"SELECT * FROM Customer WHERE phone='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    temp = session["user"]
                    print(temp)
                    print(temp[0])
                    return redirect(url_for("customer"))
            return  redirect(url_for("login"))
                
        elif(typeOf=="Restaurant"):
            q=f"SELECT * FROM Restaurant WHERE restaurantID='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("restaurant"))
            return  redirect(url_for("login"))
                
        elif(typeOf=="Management"):
            q=f"SELECT * FROM Management WHERE employeeID='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("management"))
            return  redirect(url_for("login"))

        elif(typeOf == "DeliveryWorker"):
            q=f"SELECT * FROM DeliveryWorker WHERE employeeID='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("delivery"))
            return  redirect(url_for("login"))

        elif(typeOf == "Donor"):
            q=f"SELECT * FROM Donor WHERE donorID ='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("donor"))
            return  redirect(url_for("login"))

        elif(typeOf == "Receiver"):
            q=f"SELECT * FROM Receiver WHERE receiverID='{username}';"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            if (len(myresult)==1):
                temp = typeOf[0]+username
                if(temp == password):
                    session.permanent = True
                    session["user"] = myresult[0]
                    return  redirect(url_for("receiver"))
            return  redirect(url_for("login"))

        else:
            return redirect(url_for("login"))
        
@app.route("/customer", methods= ["POST", "GET"])
def customer():
    if "user" in session:
        mycursor = mydb.cursor()
        mycursor.execute("Select r.name, r.description, r.city, r.type, a.av from Restaurant r, (Select restaurantID, avg(ratings) as av from Rates group by restaurantID)a where a.restaurantID = r.restaurantID;")
        myresult = mycursor.fetchall()

        return render_template("customer.html", x = myresult)
    else:
        return redirect(url_for("login"))
    
@app.route("/customer/profile")
def custprof():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from Customer where phone = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("customerProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/customer/orders")
def pastorders():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select o.orderID, o.customerID, o.restaurantID, o.billAmt, o.tip, o.status, o.dateTime, o.paymentMode, r.name from Orders o, Restaurant r where o.restaurantID = r.restaurantID and customerID = '{user}'")
        myresult = mycursor.fetchall()

        return render_template("customerOrders.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/management", methods= ["POST", "GET"])
def management():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT  Receiver.accepts, COUNT(Receiver.accepts) FROM Receiver GROUP BY  Receiver.accepts WITH ROLLUP;")
        myresult = mycursor.fetchall()
        mycursor.execute(f"SELECT TIMESTAMPDIFF( YEAR, dob,  CURDATE()) AS Age,   COUNT(TIMESTAMPDIFF( YEAR, dob,  CURDATE())) FROM Customer  GROUP BY  Age WITH ROLLUP;")
        myresult2 = mycursor.fetchall()
        mycursor.execute("select count(*) as Premium_Customers from Customer where customerType = 'premium';")
        myresult3 = mycursor.fetchall()
        mycursor.execute("select count(*) as Normal_Customers from Customer where customerType = 'normal';")
        myresult4 = mycursor.fetchall()
        print(myresult3, myresult4)
        
        return render_template("management.html", x = myresult, y1= myresult2, a = myresult3, b = myresult4)
    else:
        return redirect(url_for("login"))

@app.route("/management/profile")
def management_prof():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from Management where employeeID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("managementProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))
    
@app.route("/management/profile/edit", methods= ["POST", "GET"])
def management_prof_edit():
    if "user" in session:
        user = session["user"][0]
        q = f"SELECT * FROM Management WHERE employeeID = '{user}'"
        print(q)
        mycursor.execute(q)
        myresult = mycursor.fetchall()
        if request.method == "POST":
            # read data
            phone_no = request.form.get("phone_no")

            hNo = request.form.get("hNo")
            street = request.form.get("street")
            area = request.form.get("area")
            city = request.form.get("city")
            state = request.form.get("state")
            pin = request.form.get("pin")

            if(hNo != "" and street != "" and area != "" and city != "" and state != "" and pin != ""):
                # The user wants to change the address
                if(phone_no != ""):
                    q = f"UPDATE Management SET hNo = '{hNo}', street = '{street}', area = '{area}', city = '{city}', state = '{state}', pin = '{pin}', phone = '{phone_no}' WHERE employeeID = '{user}';"
                    print(q)
                    mycursor.execute(q)
                    res = mycursor.fetchall()
                    mydb.commit()
                else:
                    q = f"UPDATE Management SET hNo = '{hNo}', street = '{street}', area = '{area}', city = '{city}', state = '{state}', pin = '{pin}' WHERE employeeID = '{user}';"
                    print(q)
                    mycursor.execute(q)
                    res = mycursor.fetchall()
                    mydb.commit()

            elif(hNo == "" and street == "" and area == "" and city == "" and state == "" and pin == ""):
                # The user doesn't want to change address
                if(phone_no != ""):
                    q = f"UPDATE Management SET phone = '{phone_no}' WHERE employeeID = '{user}';"
                    print(q)
                    mycursor.execute(q)
                    res = mycursor.fetchall()
                    mydb.commit()
            else:
                print("All address details are not entered")
            return redirect(url_for("management_prof_edit"))

        else:
            print("The management logged in is: ",session.get("user"))

        return render_template("managementEditProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/delivery", methods= ["POST", "GET"])
def delivery():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select o.OrderID, r.name, r.street, r.city, r.state, r.pin, c.phone, c.hNo, c.street, c.area, c.city, c.pin, o.paymentMode, o.billAmt from Orders o, Restaurant r, Customer c where c.phone = o.customerID and r.restaurantID = o.restaurantID and o.deliveryWorkerID = '{user}'")
        myresult = mycursor.fetchall()
        mycursor.execute(f"Select d.donationID, do.phone, do.hNo, do.area, do.city, do.state, do.pin, r.name, r.street, r.area, r.city, r.state, r.pin from Donation d, Donor do, Receiver r where r.receiverID = d.receiverID and d.donorID = do.donorID and d.deliveryWorkerID = '{user}'")
        myresult2 = mycursor.fetchall()
        mycursor.execute(f"SELECT  fName FROM  DeliveryWorker where employeeID='{user}';")
        myresult3 = mycursor.fetchall()
        return render_template("delivery.html", x = myresult, y = myresult2, z = myresult3)
    else:
        return redirect(url_for("login"))
    
@app.route("/delivery/profile")
def delivery_profile():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from DeliveryWorker where employeeID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("deliveryProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/delivery/profile/edit", methods= ["POST", "GET"])
def delivery_prof_edit():
    if "user" in session:
        user = session["user"][0]
        q = f"SELECT * FROM DeliveryWorker WHERE employeeID = '{user}'"
        mycursor.execute(q)
        myresult = mycursor.fetchall()
        if request.method == "POST":
            phone = myresult[0][3]
            tip = myresult[0][13]
            hNo = myresult[0][6]
            street = myresult[0][7]
            city = myresult[0][8]
            area = myresult[0][9]
            state = myresult[0][10]
            pin = myresult[0][11]
            if(request.form.get("phone_no") != ""):
                phone = request.form.get("phone_no")
            if(request.form.get("tip") != ""):
                tip = request.form.get("tip")
            if(request.form.get("hNo") != ""):
                hNo = request.form.get("hNo")
            if(request.form.get("street") != ""):
                street = request.form.get("street")
            if(request.form.get("area") != ""):
                area = request.form.get("area")
            if(request.form.get("city") != ""):
                city = request.form.get("city")
            if(request.form.get("state") != ""):
                state = request.form.get("state")
            if(request.form.get("pin") != ""):
                pin = request.form.get("pin")

            q = f"UPDATE DeliveryWorker SET phone = '{phone}', tips = {tip}, hNo = {hNo}, street = '{street}', area = '{area}', city = '{city}', state = '{state}', pin = '{pin}' WHERE employeeID = '{user}';"
            print(q)
            mycursor.execute(q)
            res = mycursor.fetchall()
            mydb.commit()
            
            return redirect(url_for("delivery_prof_edit"))

        else:
            print("The delivery worker logged in is: ",session.get("user"))
        return render_template("deliveryEditProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/donor", methods= ["POST", "GET"])
def donor():
    if "user" in session:
        donorID = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute("Select * from Receiver;")
        myresult = mycursor.fetchall()
        mycursor.execute(f"SELECT name from Donor where donorID = '{donorID}';")
        myresult2 = mycursor.fetchall()
        return render_template("donor.html", x= myresult, y = myresult2)
    else:
        return redirect(url_for("login"))

@app.route("/donor/profile")
def donor_prof():
    if "user" in session:
        user = session["user"][0]
        mycursor.execute(f"Select * from Donor where donorID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("donorProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/donor/donations")
def donor_donations():
    if "user" in session:
        user = session["user"][0]
        mycursor.execute(f"SELECT d.donationID, d.deliveryWorkerID, d.dateTime, d.category, d.status, d.quantity, r.name FROM Receiver r, Donation d WHERE  d.receiverID = r.receiverID AND donorID = '{user}'")
        myresult = mycursor.fetchall()
        mycursor.execute(f"SELECT name from Donor where donorID = '{user}';")
        myresult2 = mycursor.fetchall()
        mycursor.execute(f"SELECT d.donationID, d.deliveryWorkerID, d.dateTime, d.category, d.status, d.quantity FROM Donation d WHERE d.receiverID IS NULL AND donorID = '{user}';")
        myresult3 = mycursor.fetchall()
        return render_template("donorDonations.html", x = myresult, y= myresult2, z= myresult3)
    else:
        return redirect(url_for("login"))

@app.route("/restaurant", methods= ["POST", "GET"])
def restaurant():
    if "user" in session:
        restaurantID = session.get("user")[0]
        q = f"SELECT name, price, discount, category, isVeg FROM Food WHERE restaurantID = '{restaurantID}';"
        mycursor.execute(q)
        myresult = mycursor.fetchall()
        mycursor.execute(f"SELECT name from Restaurant WHERE restaurantID='{restaurantID}';")
        myresult2 = mycursor.fetchall()
        myresult.append(session.get("user")[3])
        return render_template("restaurant.html", x = myresult, y = myresult2)
    else:
        return redirect(url_for("login"))

@app.route("/restaurant/profile")
def restaurant_prof():
    if "user" in session:
        user = session["user"][0]
        q = f"SELECT * FROM Restaurant WHERE restaurantID = '{user}'"
        mycursor.execute(q)
        myresult = mycursor.fetchall()
        return render_template("restaurantProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/restaurant/profile/edit", methods= ["POST", "GET"])
def restaurant_prof_edit():
    if "user" in session:
        user = session["user"][0]
        q = f"SELECT * FROM Restaurant WHERE restaurantID = '{user}'"
        mycursor.execute(q)
        myresult = mycursor.fetchall()
        if request.method == "POST":
            phone = myresult[0][5]
            name = myresult[0][4]
            description = myresult[0][3]
            dinein = myresult[0][11]
            if(dinein == 1):
                dinein = "yes"
            else:
                dinein = "no"
            street = myresult[0][6]
            city = myresult[0][7]
            area = myresult[0][8]
            state = myresult[0][8]
            pin = myresult[0][9]

            if(request.form.get("phone_no") != ""):
                phone_no = request.form.get("phone_no")
            if(request.form.get("restaurant_name") != ""):
                name = request.form.get("restaurant_name")
            if(request.form.get("description") != ""):
                description = request.form.get("description")
            if(request.form.get("dinein1") != None):
                dinein = request.form.get("dinein1")
            if(request.form.get("dinein2") != None):
                dinein = request.form.get("dinein2")
            if(request.form.get("street") != ""):
                street = request.form.get("street")
            if(request.form.get("area") != ""):
                area = request.form.get("area")
            if(request.form.get("city") != ""):
                city = request.form.get("city")
            if(request.form.get("state") != ""):
                state = request.form.get("state")
            if(request.form.get("pin") != ""):
                pin = request.form.get("pin")
            if(str.lower(dinein) == "yes"):
                q = f"UPDATE Restaurant SET isDineIn = 1, phone = '{phone}', description = '{description}', name = '{name}', street = '{street}', area = '{area}', city = '{city}', state = '{state}', pin = '{pin}' WHERE restaurantID = '{user}';"
            else:
                q = f"UPDATE Restaurant SET isDineIn = 0, phone = '{phone}', description = '{description}', name = '{name}', street = '{street}', area = '{area}', city = '{city}', state = '{state}', pin = '{pin}' WHERE restaurantID = '{user}';"
            print(q)
            mycursor.execute(q)
            res = mycursor.fetchall()
            mydb.commit()    
            return redirect(url_for("restaurant_prof_edit"))

        else:
            print("The restaurant logged in is: ",session.get("user"))

        return render_template("restaurantEditProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))

@app.route("/restaurant/orders", methods= ["POST", "GET"])
def restaurant_orders():
    if "user" in session:
        restaurantID = session.get("user")[0]
        q = f"SELECT f.name, f.isVeg, c.quantity, o.dateTime, o.customerID, o.deliveryWorkerID from Orders o, Contains c, Food f WHERE o.restaurantID = '{restaurantID}' AND o.status = 'Active' AND c.orderID = o.orderID AND c.foodID = f.itemID;"
        mycursor.execute(q)
        myresult = mycursor.fetchall()
        myresult.append(session.get("user")[3])
        mycursor.execute(f"SELECT name from Restaurant WHERE restaurantID='{restaurantID}';")
        myresult2 = mycursor.fetchall()
        return render_template("restaurantOrders.html", x = myresult, y = myresult2)
    else:
        return redirect(url_for("login"))

@app.route("/receiver", methods= ["POST", "GET"])
def receiver():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select d.donationID, d.deliveryWorkerID, d.dateTime, d.category, d.status, d.quantity, r.name from Donor r, Donation d where d.donorID = r.donorID and receiverID = '{user}'")
        myresult = mycursor.fetchall()
        mycursor.execute(f"SELECT name from Receiver where receiverID='{user}';")
        myresult2 = mycursor.fetchall()
        return render_template("receiver.html", x= myresult, y = myresult2)
    else:
        return redirect(url_for("login"))

@app.route("/receiver/profile")
def receiver_prof():
    if "user" in session:
        user = session["user"][0]
        mycursor = mydb.cursor()
        mycursor.execute(f"Select * from Receiver where receiverID = '{user}'")
        myresult = mycursor.fetchall()
        return render_template("receiverProfile.html", x = myresult)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/customer/place", methods= ["POST", "GET"])
def place():
    if "user" in session:
        if request.method == "POST":
            user = session.get("user")[0]
            payment_mode = request.form.get("payment_mode")
            food1 = request.form.get("food1")
            food2 = request.form.get("food2")
            food3 = request.form.get("food3")
            quantity1 = request.form.get("quantity1")
            quantity2 = request.form.get("quantity2")
            quantity3 = request.form.get("quantity3")

            rating = request.form.get("rating")

            if (food1 != "" and quantity1 == ""):
                print("quantity1 empty")
                return redirect(url_for("place"))
            if (food2 != "" and quantity2 == ""):
                print("quantity2 empty")
                return redirect(url_for("place"))
            if (food3 != "" and quantity3 == ""):
                print("quantity3  empty")
                return redirect(url_for("place"))
            flag = False
            q=f"SELECT * FROM Customer WHERE phone='{user}';"
            mycursor.execute(q)
            res = mycursor.fetchall()
            if(len(res) != 1):
                flag = True

            q=f"SELECT itemID FROM Food;"
            mycursor.execute(q)
            res = mycursor.fetchall()
            if (food1 != "" and (food1,) not in res):
                flag = True
            if (food2 != "" and (food2,) not in res):
                flag = True
            if (food3 != "" and (food3,) not in res):
                flag = True
            if(flag):
                print("Invalid details")
                return  redirect(url_for("place"))

            q=f"SELECT orderID FROM Orders;"
            mycursor.execute(q)
            res = mycursor.fetchall()
            mx = 0
            for i in res:
                if(int(i[0][1:]) > mx):
                    mx = int(i[0][1:])

            next_order = 'O'+str(mx+1)
            q=f"SELECT itemID, restaurantID, price FROM Food;"
            mycursor.execute(q)
            res = mycursor.fetchall()
            restaurant_name1 = ''
            restaurant_name2 = ''
            restaurant_name3 = ''
            bill_amount = 0

            for i in res:
                if (food1 != "" and food1 in i):
                    restaurant_name1 = i[1]
                    bill_amount += i[2] * int(quantity1)
                if (food2 != "" and food2 in i):
                    restaurant_name2 = i[1] 
                    bill_amount += i[2] * int(quantity2)
                if (food3 != "" and food3 in i):
                    restaurant_name3 = i[1]
                    bill_amount += i[2] * int(quantity3)
            if(food1 != "" and food2 != "" and food1 == food2):
                return redirect(url_for("place"))
            if(food2 != "" and food3 != "" and food2 == food3):
                return redirect(url_for("place"))
            if(food1 != "" and food3 != "" and food1 == food3):
                return redirect(url_for("place"))
            if(food1 != "" and food2 != "" and restaurant_name1 != restaurant_name2):
                print("Restaurant names don't match for 1 and 2")
                return redirect(url_for("place"))
            if(food1 != "" and food3 != "" and restaurant_name1 != restaurant_name3):
                print("Restaurant names don't match for 1 and 3")
                return redirect(url_for("place"))
            if(food2 != "" and food3 != "" and restaurant_name2 != restaurant_name3):
                print("Restaurant names don't match for 2 and 3")
                return redirect(url_for("place"))
            dt = datetime.now()
            dt = dt.strftime("%Y-%m-%d %H-%M-%S")
            discount_value = str(randint(1,30))
            q=f"INSERT INTO Orders(orderID, status, dateTime, billAmt, paymentMode, customerID, restaurantID, deliveryWorkerID, discount, tip) VALUES('{next_order}', 'Active', '{dt}', {str(bill_amount)}, '{payment_mode}', '{user}', '{restaurant_name1}', 'E250{800+2*randint(0,49)}', {discount_value}, 0);"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            mydb.commit()

            q = f"INSERT INTO Rates(ratings, customerID, restaurantID) VALUES({rating}, '{user}', '{restaurant_name1}')"
            print(q)
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            mydb.commit()

            if(food1 != ""):
                q=f"INSERT INTO Contains(foodID, orderID, quantity) VALUES('{food1}', '{next_order}', {quantity1});"
                print(q)
                mycursor.execute(q)
                myresult = mycursor.fetchall()
                mydb.commit()
                print(myresult)
            if(food2 != ""):
                q=f"INSERT INTO Contains(foodID, orderID, quantity) VALUES('{food2}', '{next_order}', {quantity2});"
                print(q)
                mycursor.execute(q)
                myresult = mycursor.fetchall()
                mydb.commit()
                print(myresult)
            if(food3 != ""):
                q=f"INSERT INTO Contains(foodID, orderID, quantity) VALUES('{food3}', '{next_order}', {quantity3});"
                print(q)
                mycursor.execute(q)
                myresult = mycursor.fetchall()
                mydb.commit()
                print(myresult)
        else:
            print("The User logged in is: ",session.get("user"))

        return render_template("customerPlace.html")
    else:
        return redirect(url_for("login"))

@app.route("/donor/makeDonation", methods= ["POST", "GET"])
def make():
    if "user" in session:
        if request.method == "POST":
            donorID = session.get("user")[0]
            category = request.form.get("category")
            quantity = request.form.get("quantity")
            
            try:
                if(int(quantity) <= 0):
                    print("Cannot make donation with quantity:",quantity)
            except:
                print("Wrong Quantity Input Format")
                return redirect(url_for("make"))

            q = f"SELECT donationID FROM Donation;"
            mycursor.execute(q)
            res = mycursor.fetchall()
            mx = 0
            for i in res:
                if(int(i[0][2:]) > mx):
                    mx = int(i[0][2:])

            donationID = "DO"+str(mx+1)
            dt = datetime.now()
            dt = dt.strftime("%Y-%m-%d %H-%M-%S")
            q = f"INSERT INTO Donation(donationID, donorID, receiverID, deliveryWorkerID, dateTime, category, status, quantity) VALUES('{donationID}', '{donorID}', NULL, 'E250{800+2*randint(0,49)}', '{dt}', '{category}', 'active', {quantity});"
            mycursor.execute(q)
            myresult = mycursor.fetchall()
            mydb.commit()
            q = f"SELECT points FROM Donor WHERE donorID = '{donorID}';"
            mycursor.execute(q)
            res = mycursor.fetchall()
            new_points = str((int(res[0][0]))+randint(10,50))
            q = f"UPDATE Donor SET points = {new_points} WHERE donorID = '{donorID}';"
            mycursor.execute(q)
            res = mycursor.fetchall()
            mydb.commit()
        else:
            print("The Donor logged in is: ",session.get("user"))
        return render_template("donorMake.html")
    else:
        return redirect(url_for("login"))
        

if __name__ == "__main__":
    app.run(debug=True)


    import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Nitin@200527" ,database = "fdatabase")

mycursor = mydb.cursor()
query="SHOW INDEX FROM fdatabase.Contains;"
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Contains: ')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Customer; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Customer:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.DeliveryWorker; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for DeliveryWorker:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Donation; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Donation:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Donor; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Donor:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Food; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Food:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Management; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Management:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Orders; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Orders:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Rates; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Rates:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Receiver; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Receiver:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Restaurant; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Restaurant:')
for x in myresult:
   print(x)

   

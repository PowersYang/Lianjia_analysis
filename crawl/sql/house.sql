/*
Navicat MySQL Data Transfer

Source Server         : mysql_127.0.0.1_local
Source Server Version : 50722
Source Host           : 127.0.0.1:3306
Source Database       : crawl

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-07-17 10:56:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for house
-- ----------------------------
DROP TABLE IF EXISTS `house`;
CREATE TABLE `house` (
  `houseId` int(11) NOT NULL AUTO_INCREMENT,
  `houseTitle` longtext,
  `houseTotalMoney` longtext,
  `houseSinglePrice` longtext,
  `houseDownPayment` longtext,
  `houseGardenName` longtext,
  `houseLocation` longtext,
  `houseNumber` longtext,
  `houseType` longtext,
  `houseFloor` longtext,
  `houseBuildingArea` longtext,
  `houseStructure` longtext,
  `houseInnerArea` longtext,
  `houseBuildingType` longtext,
  `houseOrientation` longtext,
  `houseBuildingStructure` longtext,
  `houseDecoration` longtext,
  `houseElevatorRatio` longtext,
  `houseElevator` longtext,
  `housePrivilege` longtext,
  `houseListDate` longtext,
  `houseTradeProperty` longtext,
  `houseLastTrade` longtext,
  `houseUsage` longtext,
  `houseAgeLimit` longtext,
  `housePrivilegeProperty` longtext,
  `housePledge` longtext,
  `houseRecord` longtext,
  `houseImg` longtext,
  `houseUrl` longtext,
  `houseRefererUrl` longtext,
  `houseCrawlTime` longtext,
  PRIMARY KEY (`houseId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

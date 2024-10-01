 ```mysql
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddRoom`(IN `id` INT(11), IN `seater` INT(11), IN `room_no` INT(11), IN `fees` INT(11),  IN `posting_date` date)
INSERT INTO rooms(`id`,`seater`,`room_no`,`fees`,`posting_date`)VALUES(id,seater,room_no,fees,posting_date)$$
DELIMITER ;

call AddRoom(5,4,106,7000,2021-07-06);
DELIMITER $$ 
CREATE TRIGGER check_room_availability_count
BEFORE INSERT ON registration
FOR EACH ROW
BEGIN
  IF (SELECT COUNT(*) FROM registration WHERE roomno = NEW.roomno) >= (NEW.seater) THEN
     SIGNAL SQLSTATE '50001' SET MESSAGE_TEXT = 'Not more than 5 members allowed in a room';
  END IF;
END;$$
DELIMITER ;


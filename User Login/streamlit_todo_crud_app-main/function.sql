create view loginlimit as (Select userId,userEmail,count(userId) as count from userlog group by userId );
select * from loginlimit;
DELIMITER $$
CREATE FUNCTION validate_loginlimit(userId varchar(50))
RETURNS VARCHAR(50)
DETERMINISTIC

BEGIN
	declare maxloginlimit int;
    declare d date;
    DECLARE VALUE varchar(50);
	select count into maxloginlimit from loginlimit where loginlimit.userId=userId;
	
	
	IF maxloginlimit>6 then
		set VALUE="Please change your password. Account may be hacked.";
    ELSE     
		set VALUE ="Welcome to Hostel Management System";	
  end if;
  return value;      
  
END;$$
DELIMITER ;

select DISTINCT userId,validate_loginlimit(userId) as validate,count(userId) as no_of_logins from userlog group by userId;
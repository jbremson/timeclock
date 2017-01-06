#Expects a db with root user.
CREATE DATABASE IF NOT EXISTS fm;
GRANT SELECT, UPDATE, DELETE, INSERT on `fm`.* TO 'fm_admin'@'%' IDENTIFIED BY 'fm_pass';




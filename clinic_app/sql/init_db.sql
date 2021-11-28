DROP DATABASE IF EXISTS clinic;
DROP DATABASE IF EXISTS clinic_test;
DROP USER IF EXISTS 'clinic_admin'@'localhost';

CREATE DATABASE clinic;
CREATE DATABASE clinic_test;
CREATE USER 'clinic_admin'@'localhost' IDENTIFIED BY 'clinic_pwd';
GRANT ALL ON clinic.* TO 'clinic_admin'@'localhost';
GRANT ALL ON clinic_test.* TO 'clinic_admin'@'localhost';

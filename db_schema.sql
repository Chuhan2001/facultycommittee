CREATE TABLE committee (
designation VARCHAR(255), 
committee_code VARCHAR(255) PRIMARY KEY, 
committee_name VARCHAR(255), 
committee_type);

CREATE TABLE faculty (
faculty_email VARCHAR(255) PRIMARY KEY, 
faculty_name VARCHAR(255));


CREATE TABLE faculty_committee(
committee_code VARCHAR(255) ,
faculty_email VARCHAR(255),
faculty_start_semester VARCHAR(255),
membership_type VARCHAR(255),
designation VARCHAR(255),
academic_year VARCHAR(255),
PRIMARY KEY (committee_code, faculty_email, academic_year)) ;

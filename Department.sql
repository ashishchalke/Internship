create database department;
use department;

drop database department;

create table Depart
(
    dept_id int primary key auto_increment,
    dept_name varchar(100),
    description varchar(300),
    created_at datetime,
    updated_at datetime,
    status varchar(50)
);

INSERT INTO Depart (dept_name, description, created_at, updated_at, status)
VALUES ("IT", "Tester", "2024-05-21 21:25:25", "2024-09-10 10:10:10", "Active");

INSERT INTO Depart (dept_name, description, created_at, updated_at, status) 
VALUES 
("IT", "Handles software development", "2024-05-21 09:00:00", "2024-09-10 10:10:10", "Active"),
("HR", "Manages recruitment and employee relations", "2024-05-22 09:30:00", "2024-09-11 11:00:00", "Active"),
("Finance", "Handles budgeting and accounts", "2024-05-23 10:00:00", "2024-09-12 12:00:00", "Active"),
("Marketing", "Promotes products and services", "2024-05-24 10:30:00", "2024-09-13 13:00:00", "Active"),
("Support", "Provides customer assistance", "2024-05-25 11:00:00", "2024-09-14 14:00:00", "Active");


select * from Depart;

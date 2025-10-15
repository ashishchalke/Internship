create database Design;
use Design;

drop database Design;

create table Department
(
id int primary key auto_increment,
name varchar(100)
);

insert into Department 
(name) values('Operation'),
             ('Sales'),
             ('Accounts'),
             ('IT');
             
drop table Department;

create table Roles
(
id int primary key auto_increment,
name varchar(100)
);

insert into Roles (name) values
('Admin'),
('Manager'),
('Team Leader'),
('Employee');

create table User
(
employee_id int primary key auto_increment,
first_name varchar(100),
username varchar(100),
Password varchar(100),
last_name varchar(100),
email varchar(100),
mobile varchar(100),
dept_id int,
role_id int,
reporting_manager_id int,
date_of_joining date,
created_at datetime,
updated_at datetime,
foreign key (dept_id) references department(id),
foreign key(role_id) references Roles(id),
foreign key(reporting_manager_id) references User(employee_id)
);


insert into User (
first_name,
username,Password,
last_name,
email,mobile,
dept_id,
role_id,
reporting_manager_id,
date_of_joining,
created_at,
updated_at
)
values(
'Ashish','Ashish@1998','123','Chalke','ashish@gmail.com','9653209745',1,2,1,'2024-4-20','2024-4-28','2025-5-26'
);

INSERT INTO User (first_name, last_name, username, password, email, mobile, dept_id, role_id, reporting_manager_id, date_of_joining)
VALUES
('Ashish', 'Chalke', 'ashish01', 'pass123', 'ashish@example.com', '9876543210', 1, 1, NULL, '2025-01-01'),
('Rahul', 'Sharma', 'rahul01', 'pass123', 'rahul@example.com', '9876543211', 2, 2, 1, '2025-02-01'),
('Sita', 'Patel', 'sita01', 'pass123', 'sita@example.com', '9876543212', 3, 3, 2, '2025-03-01');


insert into User (
first_name,
username,Password,
last_name,
email,mobile,
dept_id,
role_id,
reporting_manager_id,
date_of_joining,
created_at,
updated_at
)
values(
'Hemant','Hemant@1977','123','Kumar','Kumar@gmail.com','8853209745',1,2,1,'2024-4-20','2024-4-28','2025-5-26'
);

insert into User (
first_name,
username,Password,
last_name,
email,mobile,
dept_id,
role_id,
reporting_manager_id,
date_of_joining,
created_at,
updated_at
)
values(
'Tanvi','Tanvi@1977','123','Lad','Las@gmail.com','8853209589',3,1,2,'2024-4-20','2024-6-28',null
);
select * from User;


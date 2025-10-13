create database Design;
use Design;

create table roles
(
  role_id int primary key auto_increment,
  role_name varchar(100),
  description varchar(200),
  created_at datetime,
  update_at datetime
);

INSERT INTO roles (role_name, description, created_at, update_at)
VALUES
('Admin', 'Has full access to all system features', NOW(), NOW()),
('Manager', 'Can manage users and view reports', NOW(), NOW()),
('Editor', 'Can edit content and approve submissions', NOW(), NOW()),
('User', 'Can view and interact with content', NOW(), NOW()),
('Guest', 'Has limited access to view-only pages', NOW(), NOW());

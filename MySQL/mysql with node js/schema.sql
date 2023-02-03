
drop table users;
create TABLE users(
    email varchar(255) primary key,
    created_at TIMESTAMP default now()
);

insert into users(email) values
('katie34@yahoo.com'),('tunde@gmail.com');
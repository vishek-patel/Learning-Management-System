show databases;

create database library2;
use library2;
create table books (bname varchar(50),bcode varchar(10),total int,subject varchar(50));
create table issue (name varchar(50),regno varchar(10),bcode int,issue varchar(50));
create table submit (name varchar(50),regno varchar(10),bcode int,submit varchar(50));

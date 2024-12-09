CREATE TABLE users(
    userID int UNSIGNED AUTO_INCREMENT,
    fullname varchar(255) NOT NULL,
    username varchar(255) NOT NULL,
    userPassword varchar(255) NOT NULL,
    hashedpassword varchar(255) NOT NULL,
    UNIQUE(username),
    PRIMARY KEY(userID)

);

CREATE TABLE categories(
    categoryID int UNSIGNED AUTO_INCREMENT,
    categoryName varchar(255) NOT NULL,
    categoryOwner varchar(255) NOT NULL,
    UNIQUE(categoryName),
    PRIMARY KEY(categoryID),
    FOREIGN KEY(categoryOwner) REFERENCES users(username)

);

CREATE TABLE tasks(
    taskID int UNSIGNED AUTO_INCREMENT,
    taskName varchar(255) NOT NULL,
    taskDescription text(255) NOT NULL,
    taskCategory varchar(255) NOT NULL,        
    taskCreationDate date DEFAULT (CURRENT_DATE),
    taskStatus int DEFAULT 0,
    UNIQUE(taskName),
    UNIQUE(taskCategory),
    PRIMARY KEY(taskID),
    FOREIGN KEY(taskCategory) REFERENCES categories(categoryName)
    

);


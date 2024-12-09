

CREATE TABLE tasks(
    taskID int UNSIGNED AUTO_INCREMENT,
    taskCategory varchar(255) NOT NULL,
    taskOwner varchar(255) NOT NULL,
    taskName varchar(255) NOT NULL,
    taskDescription text(255) NOT NULL, 
    taskScheduledFor date NOT NULL,         
    taskCreationDate date DEFAULT (CURRENT_DATE),
    taskStatus int DEFAULT 0,    
    PRIMARY KEY(taskID)
        
);


-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE numberOfStudents INT;
    DECLARE count INT DEFAULT 1;

    SELECT COUNT(id)
    INTO numberOfStudents
    FROM users;

    WHILE count <= numberOfStudents DO
        CALL ComputeAverageWeightedScoreForUser(count);
        SET count = count + 1;
    END WHILE;

END //
DELIMITER ;
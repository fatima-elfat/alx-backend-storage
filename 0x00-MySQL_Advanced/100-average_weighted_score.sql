-- Task 12:  Average weighted score.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SELECT SUM(score * weight) / SUM(weight)
        INTO avg_score
        FROM users
        JOIN corrections ON users.id=corrections.user_id
        JOIN projects ON corrections.project_id=projects.id 
        WHERE users.id=user_id;
    UPDATE users SET users.average_score = avg_score WHERE users.id=user_id;
END //
DELIMITER ;

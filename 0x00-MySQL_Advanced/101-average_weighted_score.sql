-- Task 13:   Average weighted score for all!
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE avg_score FLOAT;
    DECLARE u_id INT;
    SELECT SUM(score * weight) / SUM(weight)
        INTO avg_score
        FROM users
        JOIN corrections ON users.id=corrections.user_id 
        JOIN projects ON corrections.project_id=projects.id 
        GROUP BY users.id
    SELECT users.id
        INTO u_id
        FROM users
        JOIN corrections ON users.id=corrections.user_id 
        JOIN projects ON corrections.project_id=projects.id 
        GROUP BY users.id
    UPDATE users SET users.average_score = avg_score WHERE users.id=u_id;
END //
DELIMITER ;

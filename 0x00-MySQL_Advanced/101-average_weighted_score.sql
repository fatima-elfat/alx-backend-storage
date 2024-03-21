-- Task 13:   Average weighted score for all!
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    UPDATE users SET users.average_score = avg_score WHERE users.id=u_id;
    UPDATE users, (SELECT users.id, SUM(score * weight) / SUM(weight) AS avg_score 
            FROM users
            JOIN corrections ON users.id=corrections.user_id 
            JOIN projects ON corrections.project_id=projects.id 
            GROUP BY users.id)
        AS joined_tables
        SET users.average_score = joined_tables.avg_score 
        WHERE users.id=joined_tables.id;
END //
DELIMITER ;

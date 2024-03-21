-- Task 6:  Add bonus.
DELIMITER //
CREATE PROCEDURE AddBonus(
    IN user_id INT, 
    IN project_name VARCHAR(255), 
    IN score FLOAT)
BEGIN
    DECLARE p_id INT;
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
    THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF;
    SELECT id INTO p_id FROM projects WHERE name = project_name;
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, p_id, score);
END //
DELIMITER ;

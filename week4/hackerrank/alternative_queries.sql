--P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):
--
--* * * * *
--* * * *
--* * *
--* *
--*
--Write a query to print the pattern P(20).
DELIMITER $$
CREATE PROCEDURE print_stars()
BEGIN
    DECLARE var INT DEFAULT 20;

    WHILE var > 0 DO
        SELECT REPEAT('* ', var) AS stars;
        SET var = var - 1;
    END WHILE;
END$$
DELIMITER ;
CALL print_stars();


--P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):
--*
--* *
--* * *
--* * * *
--* * * * *
--Write a query to print the pattern P(20).
CREATE PROCEDURE print_stars()
BEGIN
    DECLARE var INT DEFAULT 0;

    WHILE var < 20 DO
        SET var = var + 1;
        SELECT REPEAT('* ', var) AS stars;
    END WHILE;
END$$

DELIMITER ;
CALL print_stars();


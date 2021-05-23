-- email: skam@berkeley.edu


-- You are a car rental shop owner.

-- To run your shop smoothly, you created some tables
-- related to your shop.
--      `car` table to keep track of basic information about the cars
--      `inventory` table to keep track of the inventory in the shop.
--          NOTE: the total can be greater than the sum of available and rented,
--          meaning that there can be some missing copies.
--      `april_rental` table to keep track of rental history of the month of april
--
-- This question is in 2 parts.
--
-- NOTE: The tests for this question are NOT comprehensive, as they only
-- refer to the data tables as shown below. We will be grading this question
-- manually.
--
-- NOTE: In all scheme/sql questions you can put a multi-line answer
-- in a blank


CREATE TABLE car AS
    SELECT "car a" AS name, "*****" AS qualitys, 2017 AS year UNION
    SELECT "car b" , "*" , 1988 UNION
    SELECT "car c" , "***" , 2010 UNION
    SELECT "car d" , "***" , 2018 UNION
    SELECT "car e" , "***" , 2020 UNION
    SELECT "car f" , "*****" , 2019;

CREATE TABLE inventory AS
    SELECT "car a" AS name, 1 AS available, 2 AS rented, 3 AS total UNION
    SELECT "car b" , 2 , 3 , 10 UNION
    SELECT "car c" , 4 , 1 , 9 UNION
    SELECT "car d" , 7 , 2 , 11 UNION
    SELECT "car f" , 0 , 12, 20;

CREATE TABLE april_rental AS
    SELECT "car c" AS name, 1 AS rented_date, 5 AS return_date UNION
    SELECT "car f" , 4 , 10 UNION
    SELECT "car a" , 5 , 8 UNION
    SELECT "car b" , 5 , 9 UNION
    SELECT "car d" , 9 , 13 UNION
    SELECT "car f" , 10 , 15 UNION
    SELECT "car a" , 18, 26;

-- Part a : Complete the SQL statement below to select a one-column table
-- of car names whose release year is 2010 or later and have at least 1 copy
-- missing. Order your results by the number of missing copies, biggest to
-- smallest.
--
-- To run tests just for this part run
--      python3 ok -q a

CREATE TABLE parta AS
    SELECT a.name 
    from car as a , inventory as b
    where a.year >=2010 and a.name = b.name and b.total -( b.rented +b.available)>=1
    group by a.name
    order by b.total -( b.rented +b.available) DESC;

-- Part b : We are interested in seeing how renting behavior correlates with
--      quality.
--
-- Complete the SQL statement below to create a two-column table that shows
-- how many cars per star quality have been rented out for a period of more
-- than 3 days.
--
-- For example, if a car was rented out on april 3 and returned on april 6,
-- that would not count as being rented out for more than 3 days, but if it
-- was returned on april 7 that would count as more than 3 days.
--
-- Each row should contain the star quality and number of cars. Only include quality
-- categories that have at least 2 cars satisfying the condition.
--
-- To run tests just for this part run
--      python3 ok -q b

CREATE TABLE partb AS
    SELECT qualitys , count(*)
    from car as a , april_rental as b
    where b.return_date - b.rented_date >3 and a.name = b.name 
    group by qualitys
    having count(*)>=2;


-- ORIGINAL SKELETON FOLLOWS


-- -- You are a car rental shop owner.

-- -- To run your shop smoothly, you created some tables
-- -- related to your shop.
-- --      `car` table to keep track of basic information about the cars
-- --      `inventory` table to keep track of the inventory in the shop.
-- --          NOTE: the total can be greater than the sum of available and rented,
-- --          meaning that there can be some missing copies.
-- --      `april_rental` table to keep track of rental history of the month of april
-- --
-- -- This question is in 2 parts.
-- --
-- -- NOTE: The tests for this question are NOT comprehensive, as they only
-- -- refer to the data tables as shown below. We will be grading this question
-- -- manually.
-- --
-- -- NOTE: In all scheme/sql questions you can put a multi-line answer
-- -- in a blank


-- CREATE TABLE car AS
--     SELECT "car a" AS name, "*****" AS qualitys, 2017 AS year UNION
--     SELECT "car b" , "*" , 1988 UNION
--     SELECT "car c" , "***" , 2010 UNION
--     SELECT "car d" , "***" , 2018 UNION
--     SELECT "car e" , "***" , 2020 UNION
--     SELECT "car f" , "*****" , 2019;

-- CREATE TABLE inventory AS
--     SELECT "car a" AS name, 1 AS available, 2 AS rented, 3 AS total UNION
--     SELECT "car b" , 2 , 3 , 10 UNION
--     SELECT "car c" , 4 , 1 , 9 UNION
--     SELECT "car d" , 7 , 2 , 11 UNION
--     SELECT "car f" , 0 , 12, 20;

-- CREATE TABLE april_rental AS
--     SELECT "car c" AS name, 1 AS rented_date, 5 AS return_date UNION
--     SELECT "car f" , 4 , 10 UNION
--     SELECT "car a" , 5 , 8 UNION
--     SELECT "car b" , 5 , 9 UNION
--     SELECT "car d" , 9 , 13 UNION
--     SELECT "car f" , 10 , 15 UNION
--     SELECT "car a" , 18, 26;

-- -- Part a : Complete the SQL statement below to select a one-column table
-- -- of car names whose release year is 2010 or later and have at least 1 copy
-- -- missing. Order your results by the number of missing copies, biggest to
-- -- smallest.
-- --
-- -- To run tests just for this part run
-- --      python3 ok -q a

-- CREATE TABLE parta AS
--     SELECT "replace this;";

-- -- Part b : We are interested in seeing how renting behavior correlates with
-- --      quality.
-- --
-- -- Complete the SQL statement below to create a two-column table that shows
-- -- how many cars per star quality have been rented out for a period of more
-- -- than 3 days.
-- --
-- -- For example, if a car was rented out on april 3 and returned on april 6,
-- -- that would not count as being rented out for more than 3 days, but if it
-- -- was returned on april 7 that would count as more than 3 days.
-- --
-- -- Each row should contain the star quality and number of cars. Only include quality
-- -- categories that have at least 2 cars satisfying the condition.
-- --
-- -- To run tests just for this part run
-- --      python3 ok -q b

-- CREATE TABLE partb AS
--     SELECT "replace this;";


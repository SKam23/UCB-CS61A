-- email: skam@berkeley.edu

-- Su 18 Mock Final q6
-- Chae decides to open a tea house, called ADTeas, where customers can build their own custom drinks.
-- A drink is defined as some combination of a tea from the teas table as the base, a syrup from the syrups table,
-- and a topping from the toppings table.
-- Each tea variety belongs to some tea type, either green, black, oolong, or white. Each syrup has a popularity level
-- from 1-5 (5 being the most popular). Each topping has a particular tea type that it complements the most as well
-- as a popularity level from 1-5.

CREATE TABLE teas AS
  SELECT "jasmine" AS tea, "green" AS tea_type UNION
  SELECT "high mountain" , "oolong"            UNION
  SELECT "silver needle" , "white"             UNION
  SELECT "assam"         , "black"             UNION
  SELECT "osmanthus"     , "oolong"            UNION
  SELECT "gong fu"       , "black";

CREATE TABLE syrups AS
  SELECT "honey" AS syrup, "3" AS popularity UNION
  SELECT "mango"         , "4"               UNION
  SELECT "peach"         , "5"               UNION
  SELECT "passionfruit"  , "4"               UNION
  SELECT "grapefruit"    , "2";

CREATE TABLE toppings AS
  SELECT "lychee jelly" AS topping, "green" AS tea_type, "4" AS popularity UNION
  SELECT "tapioca pearl"          , "black"            , "5"               UNION
  SELECT "milk pudding"           , "oolong"           , "4"               UNION
  SELECT "red bean"               , "green"            , "2"               UNION
  SELECT "grass jelly"            , "white"            , "3";

-- Part (a) (2 pt)
-- Ryan needs help deciding what drink to get at ADTeas. He has no preference for the tea base or syrup,
-- but only wants drinks with toppings that complement the type of the tea base and with combinations of toppings
-- and syrups that have a combined average popularity of at least 4.5. Create a table called ryans_drinks, which
-- contains all drinks that Ryan would like given by some tea, a syrup, and a topping.
--
-- To run tests just for this part run
--      python3 ok -q a

CREATE TABLE ryans_drinks AS
    SELECT tea AS tea, syrup AS syrup, topping AS topping
        FROM teas , syrups , toppings 
            WHERE ((syrups.popularity +toppings.popularity)/2.0 >=4.5) and 
                teas.tea_type = toppings.tea_type ;

-- Part (b) (4 pt)
-- Chae creates the table special_drinks to represent a special menu of popular drink combinations.
-- It has 4 columns, each representing a tea base for the drink, a syrup, a topping, and a popularity value,
-- which is the average of the popularity values of the topping and syrup in the drink.
--
-- To run tests just for this part run
--      python3 ok -q b

CREATE TABLE special_drinks(tea, syrup, topping, popularity);

-- Kavi and Ryan happen to like the exact same types of drinks. The table kavis_drinks is an identical copy of ryans_drinks.

CREATE TABLE kavis_drinks AS
    SELECT * FROM ryans_drinks;

-- Kavi decides to hold their office hours at ADTeas and shares their drink choices with the students, which they love!
-- Insert one drink of each tea type from kavis_drinks into special_drinks. Specifically, for each tea type,
-- insert the drink that has the highest topping and syrup popularity average value out of all of the drinks of that
-- type in kavis_drinks. Assume there is at most one drink of each tea type that fits this description.

INSERT INTO special_drinks
    SELECT d.tea, d.syrup, d.topping, max((t.popularity + s.popularity)/2.0)
        FROM kavis_drinks AS d, toppings as t, syrups as s
        WHERE d.topping = t.topping and d.syrup = s.syrup
        GROUP BY t.tea_type;

-- Part (c) (1 pt)
-- Chae notices that not many people are purchasing drinks with grass jelly and that red bean is becoming
-- more popular. She wants to remove grass jelly as an topping option to cut costs and raise red bean’s popularity
-- level to 3. Fill in the statements below to reflect this.
--
-- To run tests just for this part run
--      python3 ok -q c

DELETE FROM toppings WHERE topping = "grass jelly" ;
UPDATE toppings SET popularity = 3 WHERE topping = "red bean" ;


-- ORIGINAL SKELETON FOLLOWS

-- -- Su 18 Mock Final q6
-- -- Chae decides to open a tea house, called ADTeas, where customers can build their own custom drinks.
-- -- A drink is defined as some combination of a tea from the teas table as the base, a syrup from the syrups table,
-- -- and a topping from the toppings table.
-- -- Each tea variety belongs to some tea type, either green, black, oolong, or white. Each syrup has a popularity level
-- -- from 1-5 (5 being the most popular). Each topping has a particular tea type that it complements the most as well
-- -- as a popularity level from 1-5.

-- CREATE TABLE teas AS
--   SELECT "jasmine" AS tea, "green" AS tea_type UNION
--   SELECT "high mountain" , "oolong"            UNION
--   SELECT "silver needle" , "white"             UNION
--   SELECT "assam"         , "black"             UNION
--   SELECT "osmanthus"     , "oolong"            UNION
--   SELECT "gong fu"       , "black";

-- CREATE TABLE syrups AS
--   SELECT "honey" AS syrup, "3" AS popularity UNION
--   SELECT "mango"         , "4"               UNION
--   SELECT "peach"         , "5"               UNION
--   SELECT "passionfruit"  , "4"               UNION
--   SELECT "grapefruit"    , "2";

-- CREATE TABLE toppings AS
--   SELECT "lychee jelly" AS topping, "green" AS tea_type, "4" AS popularity UNION
--   SELECT "tapioca pearl"          , "black"            , "5"               UNION
--   SELECT "milk pudding"           , "oolong"           , "4"               UNION
--   SELECT "red bean"               , "green"            , "2"               UNION
--   SELECT "grass jelly"            , "white"            , "3";

-- -- Part (a) (2 pt)
-- -- Ryan needs help deciding what drink to get at ADTeas. He has no preference for the tea base or syrup,
-- -- but only wants drinks with toppings that complement the type of the tea base and with combinations of toppings
-- -- and syrups that have a combined average popularity of at least 4.5. Create a table called ryans_drinks, which
-- -- contains all drinks that Ryan would like given by some tea, a syrup, and a topping.
-- --
-- -- To run tests just for this part run
-- --      python3 ok -q a

-- CREATE TABLE ryans_drinks AS
--     SELECT ______ AS tea, ______ AS syrup, ______ AS topping
--         FROM ______
--             WHERE ______
--                 ______;

-- -- Part (b) (4 pt)
-- -- Chae creates the table special_drinks to represent a special menu of popular drink combinations.
-- -- It has 4 columns, each representing a tea base for the drink, a syrup, a topping, and a popularity value,
-- -- which is the average of the popularity values of the topping and syrup in the drink.
-- --
-- -- To run tests just for this part run
-- --      python3 ok -q b

-- CREATE TABLE special_drinks(tea, syrup, topping, popularity);

-- -- Kavi and Ryan happen to like the exact same types of drinks. The table kavis_drinks is an identical copy of ryans_drinks.

-- CREATE TABLE kavis_drinks AS
--     SELECT * FROM ryans_drinks;

-- -- Kavi decides to hold their office hours at ADTeas and shares their drink choices with the students, which they love!
-- -- Insert one drink of each tea type from kavis_drinks into special_drinks. Specifically, for each tea type,
-- -- insert the drink that has the highest topping and syrup popularity average value out of all of the drinks of that
-- -- type in kavis_drinks. Assume there is at most one drink of each tea type that fits this description.

-- INSERT INTO special_drinks
--     SELECT d.tea, d.syrup, d.topping, ______
--         FROM kavis_drinks AS d, ______, ______
--         WHERE ______
--         GROUP BY ______;

-- -- Part (c) (1 pt)
-- -- Chae notices that not many people are purchasing drinks with grass jelly and that red bean is becoming
-- -- more popular. She wants to remove grass jelly as an topping option to cut costs and raise red bean’s popularity
-- -- level to 3. Fill in the statements below to reflect this.
-- --
-- -- To run tests just for this part run
-- --      python3 ok -q c

-- DELETE FROM ______ WHERE ______;
-- UPDATE toppings SET ______ WHERE ______;


-- SQL script to print the full description of the books table

USE alx_book_store;  -- Use the correct databasej

SELECT *
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'books';  -- This retrieves the table information

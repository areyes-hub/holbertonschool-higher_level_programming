-- creates user user_0d_1 in mysql server
-- Create user with the specified password (IF NOT EXISTS to avoid errors)
CREATE USER
IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd!2025';

-- Grant necessary privileges
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER ON *.* TO 'user_0d_1'@'localhost';

-- Optionally, grant more specific privileges (depending on your needs)
GRANT APPLICATION_PASSWORD_ADMIN, XA_RECOVER_ADMIN ON *.* TO 'user_0d_1'@'localhost';

-- Make sure privileges are refreshed
FLUSH PRIVILEGES;

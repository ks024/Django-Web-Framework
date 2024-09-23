# Commonly used PostgreSQL commands

## Connecting to a Database

- **Connect to a database:**

  ```bash
  psql -h hostname -U username -d database_name
  ```

### Basic Commands

- **List all databases:**

  ```sql
  \l
  ```

- **Connect to a specific database:**

  ```sql
  \c database_name
  ```

- **List all tables in the current database:**

  ```sql
  \dt
  ```

### Table Operations

- **Show table structure:**

  ```sql
  \d table_name
  ```

- **Create a new table:**

  ```sql
  CREATE TABLE table_name (column1 datatype, column2 datatype, ...);
  ```

### Data Manipulation

- **Insert data into a table:**

  ```sql
  INSERT INTO table_name (column1, column2) VALUES (value1, value2);
  ```

- **Update existing data:**

  ```sql
  UPDATE table_name SET column1 = value1 WHERE condition;
  ```

- **Delete data:**

  ```sql
  DELETE FROM table_name WHERE condition;
  ```

### Querying Data

- **Select all records:**

  ```sql
  SELECT * FROM table_name;
  ```

- **Select specific columns:**

  ```sql
  SELECT column1, column2 FROM table_name;
  ```

- **Using conditions:**

  ```sql
  SELECT * FROM table_name WHERE condition;
  ```

### Indexing

- **Create an index:**

  ```sql
  CREATE INDEX index_name ON table_name (column_name);
  ```

### Transaction Control

- **Begin a transaction:**

  ```sql
  BEGIN;
  ```

- **Commit a transaction:**

  ```sql
  COMMIT;
  ```

- **Rollback a transaction:**

  ```sql
  ROLLBACK;
  ```

### User Management

- **Create a new user:**

  ```sql
  CREATE USER username WITH PASSWORD 'password';
  ```

- **Grant privileges to a user:**

  ```sql
  GRANT ALL PRIVILEGES ON database_name TO username;
  ```

### Exiting

- **Exit psql:**

  ```sql
  \q
  ```

These commands cover the essentials for managing and interacting with PostgreSQL databases.

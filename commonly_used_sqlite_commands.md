## Getting Started with SQLite

1. **Open SQLite CLI**
   To start, open your terminal and type:

   ```bash
   sqlite3 mydatabase.db
   ```

   This command opens (or creates) a database named `mydatabase.db`.

### Basic Commands

2. **.help**
   Use this command to display a list of available commands:

   ```sql
   .help
   ```

3. **.tables**
   To see all the tables in the current database:

   ```sql
   .tables
   ```

4. **Create a Table**
   You can create a new table with a command like:

   ```sql
   CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);
   ```

5. **Insert Data**
   Add records to your table with:

   ```sql
   INSERT INTO users (name, age) VALUES ('Alice', 30);
   INSERT INTO users (name, age) VALUES ('Bob', 25);
   ```

6. **Read Data**
   To retrieve data, use the `SELECT` statement:

   ```sql
   SELECT * FROM users;
   ```

   This command retrieves all records from the `users` table.

7. **Update Data**
   To modify existing records:

   ```sql
   UPDATE users SET age = 31 WHERE name = 'Alice';
   ```

8. **Delete Data**
   To remove a record from the table:

   ```sql
   DELETE FROM users WHERE name = 'Bob';
   ```

### Advanced Commands

9. **.schema**
   To view the structure of a table:

   ```sql
   .schema users
   ```

10. **.exit** or **.quit**
    To close the SQLite CLI:

    ```sql
    .exit
    ```

### Tips for Usage

- **Use .mode to format output:** You can change how results are displayed. For example:

  ```sql
  .mode column
  .header ON
  ```

- **Exporting Data:** You can export a table's data to a file using:

  ```sql
  .output mydata.csv
  .mode csv
  SELECT * FROM users;
  .output stdout
  ```

**Additional Resources:**

- [sqlitetutorial.net](https://www.sqlitetutorial.net/sqlite-commands/)

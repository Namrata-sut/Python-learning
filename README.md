Python learning:

[//]: # (week1:)
"Day 1: Python Basics
* Expression: A combination of values and operators that evaluates to a single value.
* Operator: A symbol (e.g., +, -, *, /, **, %, //) used to perform operations on values.
* Order of Operations (Precedence): Parentheses (), Exponentiation **, Multiplication *, Division /, Floor Division //, Modulus %, Addition +, Subtraction - (evaluated left to right within the same precedence).
* Data Type: A category for values (e.g., integer, float, string).
   * Integer (int): Whole numbers (e.g., -2, 30, 42).
   * Floating-Point (float): Numbers with decimal points (e.g., 3.14, 42.0, -7.5).
   * String (str): Sequences of characters (e.g., 'Hello', ""Python"", '123').
* String Concatenation: Combining two or more strings using the + operator.
* String Replication: Repeating a string a specified number of times using the * operator.
* Variable: A container for storing values.
* Assignment Statement: Assigns a value to a variable using the = operator.
* Variable Names: Can use letters, numbers, and underscores, but cannot start with a number. Case-sensitive.
* Key Python Functions:
   * print(): Displays text or values to the screen.
   * input(): Pauses the program and waits for user input.
   * len(): Returns the length of a string.
   * str(), int(), float(): Convert values between data types.
   
Day 2: Flow Control
* Flowchart: A visual representation of the flow of instructions in a program.
* Boolean Value: A data type with two possible values: True and False.
* Comparison Operators: Compare two values and return a Boolean value (e.g., ==, !=, <, >, <=, >=).
* Boolean Operators:
   * and: Evaluates to True if both values are True.
   * or: Evaluates to True if at least one value is True.
   * not: Negates the value.
* Condition: A Boolean expression that determines whether a block of code should execute.
* Block of Code: A group of indented lines of code.
* if Statement: Executes a block of code if the condition is True.
* else Statement: Executes a block of code if the if condition is False.
* elif Statement: Used for multiple conditions.
* while Loop: Repeats a block of code as long as a specified condition is True.
   * Condition: The expression that determines whether the loop continues.
   * Loop Iteration: Each execution of the loop body.
* break Statement: Exits the loop immediately.
* continue Statement: Skips the current iteration and moves to the next.
* for Loop: Used to loop a fixed number of times.
* range() Function: Generates a sequence of numbers.
* Importing Modules: Using the import statement to access functions from other modules.
* sys.exit(): Terminates the program early.

Day 3: Functions
* Function: A block of code that performs a specific task.
* def Statement: Used to define a function.
* Function Call: Executing a function by writing its name followed by parentheses.
* Parameter: A variable listed in the function definition.
* Argument: A value passed to a function when it is called.
* Return Statement: Sends a value back from a function.
* Return Value: The value returned by a function.
* None: Represents the absence of a value (default return value).
* Local Scope: The area within a function where parameters and variables are defined.
* Keyword Arguments: Arguments passed by specifying the parameter name.
* Call Stack: Stores information about currently executing functions.
* Global Scope: The scope outside of all functions.
* Local Variables: Variables defined within a function.
* Global Variables: Variables defined outside of all functions.
* global Statement: Declares that a variable inside a function refers to a global variable.

Day 4: Lists
* List: An ordered sequence of values.
* List Syntax: Defined using square brackets [].
* Indexing: Accessing elements in a list using their position (0-based).
* Negative Indexing: Accessing elements from the end of the list.
* Slicing: Extracting a sublist from a list.
* List Length: Determined using the len() function.
* Modifying Lists: Changing values, adding elements, removing elements.
* Concatenation: Combining lists using the + operator.
* Replication: Repeating a list using the * operator.
* List Methods:
   * append(): Adds an item to the end.
   * insert(): Adds an item at a specified index.
   * remove(): Removes the first occurrence of a value.
   * index(): Returns the index of the first occurrence.
   * sort(): Sorts the items in the list.
   * reverse(): Reverses the order of elements.
* Sequence Data Types: Lists, strings, tuples, range objects.
* Immutable Sequences: Strings and tuples.
* Mutable Sequences: Lists.

Day 5: Dictionaries and Structuring Data
* Dictionary: A mutable collection of key-value pairs.
* Dictionary Syntax: Defined using braces {}.
* Accessing Values: Retrieve values using their keys.
* Dictionary Methods:
   * keys(): Returns all keys.
   * values(): Returns all values.
   * items(): Returns key-value pairs as tuples.
   * get(): Safely retrieves values with a default.
   * setdefault(): Sets a value for a key if it does not exist.
* Checking Key/Value Existence: Using in and not in operators.

[//]: # (week 2)
* Chapter 6: Manipulating Strings  
- isupper(): Checks if all alphabetic characters are uppercase.  
- islower(): Checks if all alphabetic characters are lowercase.  
- upper(): Converts all characters to uppercase.  
- lower(): Converts all characters to lowercase.  
- swapcase(): Swaps the case of all characters.  
- capitalize(): Capitalizes the first character, makes the rest lowercase.  

Chapter 7: Pattern Matching with Regular Expressions  
- Regex: Patterns for matching text (e.g., `\d` for digits).  
- re.compile(): Creates a regex object.  
- search(): Finds the first match; returns a Match object or None.  
- Groups: `group()` retrieves matches; `groups()` returns all groups.  
- Special Characters: Escape with `\`.  
- Pipe (|): Matches one of several patterns.  
- Optional Matching (?): Matches zero or one occurrence.  
- Repetition: `*` (0+), `+` (1+), `{n,m}` (between n and m).  
- Greedy/Non-Greedy: Add `?` for shortest matches.  
- findall(): Returns all matches as a list.  
- Character Classes: Predefined (`\d`, `\w`, etc.) and custom (`[a-z]`).  
- Anchors: `^` (start), `$` (end), `^...$` (entire string).  

Chapter 8: Input Validation with PyInputPlus  
- inputStr(): Validates string input.  
- inputNum(): Validates numbers.  
- inputChoice(): Ensures input matches options.  
- inputMenu(): Displays options as a menu.  
- inputDatetime(): Validates date/time input.  
- inputYesNo(): Accepts ""yes""/""no"".  
- inputEmail(): Validates email addresses.  
- inputFilepath(): Validates file paths.  
- inputPassword(): Masks sensitive input.  
- Custom Validation: Use `inputCustom()` for custom rules.  
- Limits/Timeouts: `limit`, `timeout`, and `default` control retries and time.                                                                                                                                                Chapter 9: Reading and Writing Files in Python
- Files and File Paths: Files have names, paths, and extensions; case sensitivity varies by OS.
- pathlib Basics: Use / for paths, Path.cwd() for working directory, and Path.home() for home directory.
- Absolute vs. Relative Paths: Check or convert with is_absolute() or os.path.abspath().
- Path Components: Extract parts like name and suffix using pathlib or os.path.
- File Sizes & Contents: Get sizes with os.path.getsize() and list contents with os.listdir().
- Glob Patterns: Filter files using pathlib.glob() and rglob().
- File Operations: Read, overwrite ('w'), or append ('a') data.
- shelve Module: Save variables as persistent, dictionary-like objects.
- pprint.pformat(): Format data as reusable Python code."	
- 

[//]: # (week 3)
"I created a simple Pokemon API using Python and FastAPI with the following endpoints:

load_data: Loads Pokemon JSON data from a URL into the pokemon_data dictionary. It uses requests.get(URL) to fetch the data in JSON format and stores it in a dictionary.

get_pokemon_by_id: Retrieves Pokemon data by ID. It checks if the key pokemon_id exists in pokemon_data and returns the corresponding data.

get_pokemon_by_name: Retrieves Pokemon data by name. It iterates through all Pokemon in pokemon_data and compares the name with the user input.

get_all_pokemon: Retrieves all Pokemon data if pokemon_data is not empty.

add_pokemon: Adds a new Pokemon to pokemon_data. It automatically generates a new ID by finding the highest current key, incrementing it, and then adding the new Pokemon.

update_pokemon: Updates existing Pokemon data by ID. It checks if pokemon_data is not empty, retrieves the Pokemon by ID, and updates it using pokemon_data[pokemon_id].update(update_pokemon).

delete_pokemon: Deletes a Pokemon by ID. It checks if the Pokemon exists in pokemon_data, and if so, removes it using pokemon_data.pop(pokemon_id).

Custom Exceptions Added:

PokemonNotFound: This exception is raised when a Pokemon with a specific ID is not found. It returns a 404 Not Found error with a message indicating the Pokemon ID is not found.

PokemonEmptyDataError: This exception is raised when the Pokemon data is empty. It returns a 404 Not Found error with a message indicating the data is empty."	


[//]: # (week 4)
"1. SELECT Queries
Definition: Retrieves data from a database table, selecting specific columns or all columns.
Syntax:
Specific columns: SELECT column1, column2 FROM table;
All columns: SELECT * FROM table;

2. SQL Queries with Constraints
Definition: Filters rows based on conditions using WHERE with logical operators (AND, OR) and comparison operators.
Examples:
Specific id: SELECT * FROM movies WHERE id = 6;
Range of years: SELECT title, year FROM movies WHERE year BETWEEN 2000 AND 2010;
Not within range: SELECT title, year FROM movies WHERE year NOT BETWEEN 2000 AND 2010;

3. SQL Queries with Text Constraints
Definition: Filters text data using operators like =, !=, LIKE, and IN.
Pattern matching: Use % (any characters) and _ (single character) in LIKE.

4. Filtering and Sorting Query Results
Removing Duplicates: Use DISTINCT to eliminate duplicates.
SELECT DISTINCT director FROM movies;

Sorting: Use ORDER BY for ascending (ASC) or descending (DESC) order.
SELECT title, year FROM movies ORDER BY year DESC;

Limiting and Paginating Results: Use LIMIT to restrict the number of results, OFFSET for pagination.
SELECT title FROM movies ORDER BY title ASC LIMIT 5 OFFSET 5;

5. JOINs - Multi-table Queries
Definition: Combines data from multiple tables based on a related column.
INNER JOIN: Retrieves rows where there is a match in both tables.
SELECT column1 FROM table1 INNER JOIN table2 ON table1.column = table2.column;

6. OUTER JOINs
Definition: Includes rows that may not have a match in the other table.

LEFT JOIN: All from the left table, matching from the right.
SELECT * FROM table1 LEFT JOIN table2 ON table1.column = table2.column;

RIGHT JOIN: All from the right table, matching from the left.

FULL JOIN: All rows from both tables, unmatched rows filled with NULLs.

7. NULLs in SQL
Definition: Represents missing or undefined data.
Use IS NULL or IS NOT NULL for filtering NULL values.

Example: Find employees without assigned buildings.
SELECT role, name FROM employees WHERE building IS NULL;"	

[//]: # (week 5)

"SQL queries with expression and aggregate Functions
1. Expressions in SQL: A combination of columns, constants, and functions that transform or compute new values.
	Example: SELECT particle_speed / 2.0 AS half_particle_speed FROM physics_data;

2. Aliases for Readability: Temporary, user-friendly names for columns or tables, created using AS in queries.
	Example: SELECT column AS better_column_name FROM long_table_name AS mytable;

3. Aggregate Functions: Functions that summarize data across rows, such as COUNT(), SUM(), AVG(), MIN(), MAX().
	Example: SELECT COUNT(*) AS total_movies FROM pixar_movies;

4. Using Aggregate Functions With GROUP BY: Groups rows by specified columns and applies aggregate functions to each group.
	Example: SELECT genre, SUM(box_office) AS total_sales FROM movies GROUP BY genre;

5. HAVING Clause: Filters groups of rows after the GROUP BY clause has been applied, typically used with aggregate functions.
	Example: SELECT genre, COUNT(*) AS movie_count FROM movies GROUP BY genre HAVING COUNT(*) > 5;

6. Query Execution Order: The sequence in which SQL query clauses are processed: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.
	Example: SELECT genre, COUNT(*) FROM movies WHERE release_year > 2000 GROUP BY genre HAVING COUNT(*) > 5 ORDER BY COUNT(*) DESC LIMIT 10;


SQL Table Concepts
1. Data Types:  
   - INTEGER: Whole numbers  
   - FLOAT, DOUBLE, REAL: Floating-point numbers  
   - CHARACTER(n), VARCHAR(n): Fixed/variable-length strings  
   - TEXT: Unbounded strings  
   - DATE, DATETIME: Date and time values  
   - BLOB: Binary data (images, files, etc.)  

2. Table Constraints:  
   - PRIMARY KEY: Unique identifier for rows  
   - AUTOINCREMENT: Automatically increments integer values  
   - UNIQUE: Ensures values in a column are unique  
   - NOT NULL: Prevents NULL values in a column  
   - CHECK(expression): Validates column values with a condition  
   - FOREIGN KEY: References values in another table.

3. CREATE TABLE Statement: Defines a new table with columns and constraints.  
   Example: CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT);

4. INSERT Statement: Adds new rows to a table.  
   Example: INSERT INTO movies VALUES (1, 'Inception', 9.0);

5. UPDATE Statement: Modifies existing rows in a table.  
   Example:UPDATE movies SET rating = 9.5 WHERE title = 'Inception';

6. DELETE Statement: Removes rows from a table.  
   Example: DELETE FROM movies WHERE title = 'Inception';

7. ALTER TABLE Statement: Modifies the structure of an existing table.  
   Example: ALTER TABLE movies ADD genre TEXT;

8. DROP TABLE Statement: Deletes a table and all its data.  
   Example: DROP TABLE IF EXISTS movies;"	

[//]: # (week 6)

"This week, I implemented FastAPI routes for Pokemon operations using a repository pattern. I used PostgreSQL as the database and the psycopg2 driver to write a context manager for managing the database connection. I defined the Pokemon input and update schemas using Pydantic's BaseModel. To interact with the database, I utilized raw SQL queries.

The following routes were implemented:

load_pokemon_data():
Loads Pokemon data from an external API, removes IDs, cleans the data, and inserts it into the database.

get_by_id(pokemon_id: int):
Retrieves a single Pokemon record by its ID.

get_all():
Retrieves all Pokemon records.

add(payload: PokemonSchema):
Creates a new Pokemon record.

delete(pokemon_id: int):
Deletes a Pokemon record by its ID.

update(pokemon_id: int, payload: PokemonUpdateSchema):
Updates an existing Pokemon record."


[//]: # (week 7)

"Implemented FastAPI Routes:
Developed multiple REST API endpoints for CRUD operations on Pokemon data.
Implemented GET(get_all, get_by_id, get_by_name), POST, PUT, and DELETE methods with appropriate status codes and error handling.
 
Database Integration:
Integrated SQLAlchemy with AsyncSession for efficient asynchronous database operations.
Used SQLAlchemy models as an ORM to interact with the PostgreSQL database seamlessly.
 
Data Loading Feature:
Added an API(load_data) to load Pokemon data from an external URL and insert it into the database after cleaning unnecessary fields (like removing IDs).
 
Code Reusability:
Utilized dependency injection with Depends(get_db) for database session management across routes.
Structured code using service layers (PokemonService) to separate business logic from API routes.

[//]: # (week 8)

Pokemon API Enhancements
This week, I worked on improving the Pokemon API by integrating Jinja2 templates for all relevant API endpoints and implementing database migrations using Alembic. 

1. Jinja2 Template Integration
Implemented dynamic templates for displaying Pokemon data, search results, and error messages.
Templates added for:
create_pokemon.html – Form for adding new Pokemon
pokemon_list.html – Displays all Pokemon and search results(by id and name)
update_pokemon.html – Form for updating Pokemon details
Redirect-based search implementation for Pokemon by name and ID.
2. Database Migration with Alembic
Set up Alembic for database version control.
Created migration scripts to handle Pokemon table modifications smoothly.


[//]: # (Week 9)

Quiz Application with Database and Migrations
I have developed a Quiz Application where users can browse a list of quizzes. When a user selects a quiz, the quiz starts, and they are presented with questions in a paginated format (5 questions per page).

Quiz Selection: Users can choose from a list of available quizzes.
Question Pagination: Each quiz contains multiple questions, but only 5 questions are displayed per page to improve user experience.
Quiz Submission & Result: After answering all the questions, users submit their responses.
Pass/Fail Criteria:
If the score is 50% or higher, the user passes the quiz.
If the score is below 50%, the user fails the quiz.

technology and tools used:
FastApi with SQLAlchemy for database integration
Jinja templates for rendering HTML
Alembic for managing schema changes"		

Hackerank: https://www.hackerrank.com/domains/python
problem 1: Loops

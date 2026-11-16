# SQL Interview Questions and Answers

_Last updated: October 28, 2026_

450 SQL interview questions with answers, split into three levels: 150 easy, 150 moderate and 150 advanced. Most answers include a short code example.

The examples follow standard SQL where possible. The current standard is SQL:2023 (ISO/IEC 9075:2023). When something works differently in PostgreSQL, MySQL, SQL Server, Oracle or SQLite, the answer points that out. Version notes refer to PostgreSQL 18, MySQL 8.4 / 9.x, SQL Server 2022 / 2025, Oracle 23ai and SQLite 3.4x.

Most examples use these tables:

```sql
CREATE TABLE departments (
    id   INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    id            INT PRIMARY KEY,
    first_name    VARCHAR(50)  NOT NULL,
    last_name     VARCHAR(50)  NOT NULL,
    email         VARCHAR(255) UNIQUE,
    department_id INT REFERENCES departments(id),
    manager_id    INT REFERENCES employees(id),
    salary        DECIMAL(10, 2),
    hire_date     DATE
);

CREATE TABLE customers (
    id         INT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    country    VARCHAR(50),
    created_at TIMESTAMP
);

CREATE TABLE products (
    id       INT PRIMARY KEY,
    name     VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price    DECIMAL(10, 2)
);

CREATE TABLE orders (
    id          INT PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    order_date  DATE,
    status      VARCHAR(20),
    total       DECIMAL(10, 2)
);

CREATE TABLE order_items (
    order_id   INT REFERENCES orders(id),
    product_id INT REFERENCES products(id),
    quantity   INT,
    unit_price DECIMAL(10, 2),
    PRIMARY KEY (order_id, product_id)
);
```

## Table of Contents

- [Easy Questions (1-150)](#easy-questions-1-150)
  - [SQL Basics (1-20)](#sql-basics)
  - [Data Types (21-35)](#data-types)
  - [Creating and Changing Tables (36-55)](#creating-and-changing-tables)
  - [Constraints and Keys (56-70)](#constraints-and-keys)
  - [Selecting and Filtering Data (71-95)](#selecting-and-filtering-data)
  - [Sorting and Limiting Results (96-105)](#sorting-and-limiting-results)
  - [Basic Functions (106-125)](#basic-functions)
  - [Basic Aggregation (126-137)](#basic-aggregation)
  - [Join Basics (138-150)](#join-basics)
- [Moderate Questions (151-300)](#moderate-questions-151-300)
  - [Joins in Depth (151-168)](#joins-in-depth)
  - [Grouping and Pivoting (169-180)](#grouping-and-pivoting)
  - [Subqueries (181-198)](#subqueries)
  - [Common Table Expressions (199-208)](#common-table-expressions)
  - [Window Functions (209-230)](#window-functions)
  - [Set Operations (231-238)](#set-operations)
  - [Indexes (239-255)](#indexes)
  - [Views (256-263)](#views)
  - [Transactions and Locking Basics (264-277)](#transactions-and-locking-basics)
  - [Inserting, Updating and Merging Data (278-290)](#inserting-updating-and-merging-data)
  - [Dates, Strings and NULL Handling (291-300)](#dates-strings-and-null-handling)
- [Advanced Questions (301-450)](#advanced-questions-301-450)
  - [Query Execution and Performance (301-318)](#query-execution-and-performance)
  - [Advanced Indexing (319-332)](#advanced-indexing)
  - [Concurrency and Isolation (333-352)](#concurrency-and-isolation)
  - [Advanced Analytics with Window Functions (353-368)](#advanced-analytics-with-window-functions)
  - [Recursive Queries and Hierarchies (369-378)](#recursive-queries-and-hierarchies)
  - [JSON, Arrays and Vectors (379-392)](#json-arrays-and-vectors)
  - [Partitioning, Replication and Scaling (393-405)](#partitioning-replication-and-scaling)
  - [Procedures, Functions and Triggers (406-418)](#procedures-functions-and-triggers)
  - [Database Design and Normalization (419-430)](#database-design-and-normalization)
  - [Security (431-438)](#security)
  - [Practical Query Problems (439-450)](#practical-query-problems)

### Easy Questions (1-150)

- [1: What is SQL?](#1-what-is-sql)
- [2: What is a database?](#2-what-is-a-database)
- [3: What is a relational database?](#3-what-is-a-relational-database)
- [4: What is the difference between a DBMS and an RDBMS?](#4-what-is-the-difference-between-a-dbms-and-an-rdbms)
- [5: What are tables, rows and columns?](#5-what-are-tables-rows-and-columns)
- [6: What are the main groups of SQL commands?](#6-what-are-the-main-groups-of-sql-commands)
- [7: What is the difference between SQL and MySQL (or PostgreSQL)?](#7-what-is-the-difference-between-sql-and-mysql-or-postgresql)
- [8: Is SQL case sensitive?](#8-is-sql-case-sensitive)
- [9: What is the latest version of the SQL standard?](#9-what-is-the-latest-version-of-the-sql-standard)
- [10: What is a query?](#10-what-is-a-query)
- [11: What is a schema?](#11-what-is-a-schema)
- [12: In what order do you write the clauses of a SELECT statement?](#12-in-what-order-do-you-write-the-clauses-of-a-select-statement)
- [13: In what order does the database logically process a SELECT statement?](#13-in-what-order-does-the-database-logically-process-a-select-statement)
- [14: How do you write comments in SQL?](#14-how-do-you-write-comments-in-sql)
- [15: What is NULL?](#15-what-is-null)
- [16: What is the difference between NULL, zero and an empty string?](#16-what-is-the-difference-between-null-zero-and-an-empty-string)
- [17: What is the semicolon used for in SQL?](#17-what-is-the-semicolon-used-for-in-sql)
- [18: What is the difference between single quotes and double quotes in SQL?](#18-what-is-the-difference-between-single-quotes-and-double-quotes-in-sql)
- [19: How do you put a single quote inside a string?](#19-how-do-you-put-a-single-quote-inside-a-string)
- [20: What is an alias?](#20-what-is-an-alias)
- [21: What are the main categories of SQL data types?](#21-what-are-the-main-categories-of-sql-data-types)
- [22: What is the difference between CHAR and VARCHAR?](#22-what-is-the-difference-between-char-and-varchar)
- [23: What is the difference between VARCHAR and TEXT?](#23-what-is-the-difference-between-varchar-and-text)
- [24: What is the difference between INT, SMALLINT and BIGINT?](#24-what-is-the-difference-between-int-smallint-and-bigint)
- [25: What is the difference between DECIMAL and FLOAT?](#25-what-is-the-difference-between-decimal-and-float)
- [26: Why should you not store money in a FLOAT column?](#26-why-should-you-not-store-money-in-a-float-column)
- [27: What are the DATE, TIME and TIMESTAMP types?](#27-what-are-the-date-time-and-timestamp-types)
- [28: What is the difference between TIMESTAMP and TIMESTAMP WITH TIME ZONE?](#28-what-is-the-difference-between-timestamp-and-timestamp-with-time-zone)
- [29: Does SQL have a BOOLEAN type?](#29-does-sql-have-a-boolean-type)
- [30: How do you store binary data such as images?](#30-how-do-you-store-binary-data-such-as-images)
- [31: What is a UUID and when would you use it?](#31-what-is-a-uuid-and-when-would-you-use-it)
- [32: Is there a JSON data type in SQL?](#32-is-there-a-json-data-type-in-sql)
- [33: How do you convert a value from one data type to another?](#33-how-do-you-convert-a-value-from-one-data-type-to-another)
- [34: What is the difference between implicit and explicit conversion?](#34-what-is-the-difference-between-implicit-and-explicit-conversion)
- [35: What new numeric literal formats did SQL:2023 add?](#35-what-new-numeric-literal-formats-did-sql2023-add)
- [36: How do you create a database?](#36-how-do-you-create-a-database)
- [37: How do you create a table?](#37-how-do-you-create-a-table)
- [38: How do you add a column to an existing table?](#38-how-do-you-add-a-column-to-an-existing-table)
- [39: How do you remove a column?](#39-how-do-you-remove-a-column)
- [40: How do you rename a table or a column?](#40-how-do-you-rename-a-table-or-a-column)
- [41: How do you change the data type of a column?](#41-how-do-you-change-the-data-type-of-a-column)
- [42: What is the difference between DELETE, TRUNCATE and DROP?](#42-what-is-the-difference-between-delete-truncate-and-drop)
- [43: What do IF EXISTS and IF NOT EXISTS do?](#43-what-do-if-exists-and-if-not-exists-do)
- [44: How do you insert a row into a table?](#44-how-do-you-insert-a-row-into-a-table)
- [45: How do you insert several rows at once?](#45-how-do-you-insert-several-rows-at-once)
- [46: How do you copy data from one table into another?](#46-how-do-you-copy-data-from-one-table-into-another)
- [47: How do you update data?](#47-how-do-you-update-data)
- [48: How do you delete data?](#48-how-do-you-delete-data)
- [49: What happens if you run UPDATE or DELETE without a WHERE clause?](#49-what-happens-if-you-run-update-or-delete-without-a-where-clause)
- [50: What is a DEFAULT value?](#50-what-is-a-default-value)
- [51: How do you create a new table from the result of a query?](#51-how-do-you-create-a-new-table-from-the-result-of-a-query)
- [52: What is an identity (auto-increment) column?](#52-what-is-an-identity-auto-increment-column)
- [53: What is a temporary table?](#53-what-is-a-temporary-table)
- [54: What is a generated (computed) column?](#54-what-is-a-generated-computed-column)
- [55: How do you create an empty copy of a table's structure?](#55-how-do-you-create-an-empty-copy-of-a-tables-structure)
- [56: What is a constraint?](#56-what-is-a-constraint)
- [57: What is a primary key?](#57-what-is-a-primary-key)
- [58: Can a primary key contain NULL? Can a table have two primary keys?](#58-can-a-primary-key-contain-null-can-a-table-have-two-primary-keys)
- [59: What is a composite key?](#59-what-is-a-composite-key)
- [60: What is a foreign key?](#60-what-is-a-foreign-key)
- [61: What is a UNIQUE constraint?](#61-what-is-a-unique-constraint)
- [62: What is the difference between a primary key and a unique key?](#62-what-is-the-difference-between-a-primary-key-and-a-unique-key)
- [63: What is a NOT NULL constraint?](#63-what-is-a-not-null-constraint)
- [64: What is a CHECK constraint?](#64-what-is-a-check-constraint)
- [65: What does ON DELETE CASCADE do?](#65-what-does-on-delete-cascade-do)
- [66: What other actions can a foreign key take on delete or update?](#66-what-other-actions-can-a-foreign-key-take-on-delete-or-update)
- [67: What is the difference between a natural key and a surrogate key?](#67-what-is-the-difference-between-a-natural-key-and-a-surrogate-key)
- [68: What are super keys, candidate keys and alternate keys?](#68-what-are-super-keys-candidate-keys-and-alternate-keys)
- [69: How do you add a constraint to a table that already exists?](#69-how-do-you-add-a-constraint-to-a-table-that-already-exists)
- [70: Why should you give constraints names?](#70-why-should-you-give-constraints-names)
- [71: How do you select all columns, and why is SELECT \* often discouraged?](#71-how-do-you-select-all-columns-and-why-is-select--often-discouraged)
- [72: How do you select specific columns?](#72-how-do-you-select-specific-columns)
- [73: What does DISTINCT do?](#73-what-does-distinct-do)
- [74: What is the WHERE clause?](#74-what-is-the-where-clause)
- [75: What comparison operators does SQL have?](#75-what-comparison-operators-does-sql-have)
- [76: How do AND, OR and NOT work together?](#76-how-do-and-or-and-not-work-together)
- [77: How does BETWEEN work?](#77-how-does-between-work)
- [78: How does the IN operator work?](#78-how-does-the-in-operator-work)
- [79: How does LIKE work?](#79-how-does-like-work)
- [80: How do you search for a literal % or \_ with LIKE?](#80-how-do-you-search-for-a-literal--or-_-with-like)
- [81: How do you do a case-insensitive search?](#81-how-do-you-do-a-case-insensitive-search)
- [82: Why does `WHERE column = NULL` return no rows?](#82-why-does-where-column--null-return-no-rows)
- [83: What is IS DISTINCT FROM?](#83-what-is-is-distinct-from)
- [84: Can you use expressions in the SELECT list?](#84-can-you-use-expressions-in-the-select-list)
- [85: What is a CASE expression?](#85-what-is-a-case-expression)
- [86: What is the difference between a simple CASE and a searched CASE?](#86-what-is-the-difference-between-a-simple-case-and-a-searched-case)
- [87: Can you use a column alias in the WHERE clause?](#87-can-you-use-a-column-alias-in-the-where-clause)
- [88: Can you ORDER BY a column that is not in the SELECT list?](#88-can-you-order-by-a-column-that-is-not-in-the-select-list)
- [89: Can you run a SELECT without a FROM clause?](#89-can-you-run-a-select-without-a-from-clause)
- [90: How do you join strings together?](#90-how-do-you-join-strings-together)
- [91: What is the difference between WHERE and HAVING?](#91-what-is-the-difference-between-where-and-having)
- [92: What is three-valued logic in SQL?](#92-what-is-three-valued-logic-in-sql)
- [93: Why can NOT IN return no rows when the list contains NULL?](#93-why-can-not-in-return-no-rows-when-the-list-contains-null)
- [94: How do you filter rows by date?](#94-how-do-you-filter-rows-by-date)
- [95: What is a table alias and why use it?](#95-what-is-a-table-alias-and-why-use-it)
- [96: How do you sort query results?](#96-how-do-you-sort-query-results)
- [97: How do you sort by several columns and in different directions?](#97-how-do-you-sort-by-several-columns-and-in-different-directions)
- [98: Where do NULL values appear when sorting?](#98-where-do-null-values-appear-when-sorting)
- [99: How do you return only the first N rows?](#99-how-do-you-return-only-the-first-n-rows)
- [100: How do you skip rows for pagination?](#100-how-do-you-skip-rows-for-pagination)
- [101: What does FETCH FIRST ... WITH TIES do?](#101-what-does-fetch-first--with-ties-do)
- [102: Can you sort by column position? Should you?](#102-can-you-sort-by-column-position-should-you)
- [103: Is the order of rows guaranteed without ORDER BY?](#103-is-the-order-of-rows-guaranteed-without-order-by)
- [104: How do you find the row with the highest value in a column?](#104-how-do-you-find-the-row-with-the-highest-value-in-a-column)
- [105: How do you pick random rows?](#105-how-do-you-pick-random-rows)
- [106: What is the difference between scalar functions and aggregate functions?](#106-what-is-the-difference-between-scalar-functions-and-aggregate-functions)
- [107: How do you change text to upper or lower case?](#107-how-do-you-change-text-to-upper-or-lower-case)
- [108: How do you get the length of a string?](#108-how-do-you-get-the-length-of-a-string)
- [109: How do you get part of a string?](#109-how-do-you-get-part-of-a-string)
- [110: How do you remove spaces from the start or end of a string?](#110-how-do-you-remove-spaces-from-the-start-or-end-of-a-string)
- [111: How do you replace part of a string?](#111-how-do-you-replace-part-of-a-string)
- [112: How do you pad a string to a fixed length?](#112-how-do-you-pad-a-string-to-a-fixed-length)
- [113: How do you find the position of a substring?](#113-how-do-you-find-the-position-of-a-substring)
- [114: How do ROUND, CEILING, FLOOR and TRUNC differ?](#114-how-do-round-ceiling-floor-and-trunc-differ)
- [115: What common math functions does SQL have?](#115-what-common-math-functions-does-sql-have)
- [116: Why does 5 / 2 return 2 in some databases?](#116-why-does-5--2-return-2-in-some-databases)
- [117: How do you get the current date and time?](#117-how-do-you-get-the-current-date-and-time)
- [118: How do you get the year, month or day from a date?](#118-how-do-you-get-the-year-month-or-day-from-a-date)
- [119: How do you add days or months to a date?](#119-how-do-you-add-days-or-months-to-a-date)
- [120: What does COALESCE do?](#120-what-does-coalesce-do)
- [121: What does NULLIF do?](#121-what-does-nullif-do)
- [122: What do GREATEST and LEAST do?](#122-what-do-greatest-and-least-do)
- [123: How do you format a date as text?](#123-how-do-you-format-a-date-as-text)
- [124: What is the difference between deterministic and nondeterministic functions?](#124-what-is-the-difference-between-deterministic-and-nondeterministic-functions)
- [125: How do you avoid a division by zero error?](#125-how-do-you-avoid-a-division-by-zero-error)
- [126: What are aggregate functions?](#126-what-are-aggregate-functions)
- [127: What is the difference between COUNT(\*), COUNT(column) and COUNT(DISTINCT column)?](#127-what-is-the-difference-between-count-countcolumn-and-countdistinct-column)
- [128: How do SUM and AVG treat NULL values?](#128-how-do-sum-and-avg-treat-null-values)
- [129: Can MIN and MAX work on text and dates?](#129-can-min-and-max-work-on-text-and-dates)
- [130: What does GROUP BY do?](#130-what-does-group-by-do)
- [131: Why do you get an error like "column must appear in the GROUP BY clause"?](#131-why-do-you-get-an-error-like-column-must-appear-in-the-group-by-clause)
- [132: What does HAVING do?](#132-what-does-having-do)
- [133: Can you group by more than one column?](#133-can-you-group-by-more-than-one-column)
- [134: What do aggregate functions return on an empty table?](#134-what-do-aggregate-functions-return-on-an-empty-table)
- [135: How do you count only the rows that match a condition?](#135-how-do-you-count-only-the-rows-that-match-a-condition)
- [136: What is ANY_VALUE?](#136-what-is-any_value)
- [137: Can you put one aggregate inside another, like MAX(AVG(salary))?](#137-can-you-put-one-aggregate-inside-another-like-maxavgsalary)
- [138: What is a join?](#138-what-is-a-join)
- [139: What types of joins are there?](#139-what-types-of-joins-are-there)
- [140: What does INNER JOIN return?](#140-what-does-inner-join-return)
- [141: What does LEFT JOIN return?](#141-what-does-left-join-return)
- [142: What does RIGHT JOIN return?](#142-what-does-right-join-return)
- [143: What does FULL OUTER JOIN return?](#143-what-does-full-outer-join-return)
- [144: What is a CROSS JOIN?](#144-what-is-a-cross-join)
- [145: What is a self join?](#145-what-is-a-self-join)
- [146: What is the difference between ON and USING?](#146-what-is-the-difference-between-on-and-using)
- [147: What is a NATURAL JOIN and why is it risky?](#147-what-is-a-natural-join-and-why-is-it-risky)
- [148: What happens to NULL values in join columns?](#148-what-happens-to-null-values-in-join-columns)
- [149: How do you join more than two tables?](#149-how-do-you-join-more-than-two-tables)
- [150: What is the difference between the old comma join syntax and the JOIN syntax?](#150-what-is-the-difference-between-the-old-comma-join-syntax-and-the-join-syntax)

### Moderate Questions (151-300)

- [151: In a LEFT JOIN, what is the difference between putting a condition in ON and putting it in WHERE?](#151-in-a-left-join-what-is-the-difference-between-putting-a-condition-in-on-and-putting-it-in-where)
- [152: How do you find rows in one table that have no match in another table?](#152-how-do-you-find-rows-in-one-table-that-have-no-match-in-another-table)
- [153: What is a semi-join?](#153-what-is-a-semi-join)
- [154: Why does a join sometimes return more rows than expected?](#154-why-does-a-join-sometimes-return-more-rows-than-expected)
- [155: How do you join on more than one column?](#155-how-do-you-join-on-more-than-one-column)
- [156: What is a non-equi join?](#156-what-is-a-non-equi-join)
- [157: How do you find employees who earn more than their managers?](#157-how-do-you-find-employees-who-earn-more-than-their-managers)
- [158: What is a LATERAL join?](#158-what-is-a-lateral-join)
- [159: What is the difference between CROSS APPLY and OUTER APPLY in SQL Server?](#159-what-is-the-difference-between-cross-apply-and-outer-apply-in-sql-server)
- [160: Why can SUM give a wrong total after a join, and how do you fix it?](#160-why-can-sum-give-a-wrong-total-after-a-join-and-how-do-you-fix-it)
- [161: How do you find duplicate rows?](#161-how-do-you-find-duplicate-rows)
- [162: How do you delete duplicate rows but keep one copy?](#162-how-do-you-delete-duplicate-rows-but-keep-one-copy)
- [163: What is a Cartesian product, and how can you create one by accident?](#163-what-is-a-cartesian-product-and-how-can-you-create-one-by-accident)
- [164: Does the order of tables in a join matter?](#164-does-the-order-of-tables-in-a-join-matter)
- [165: How do you write a FULL OUTER JOIN in MySQL?](#165-how-do-you-write-a-full-outer-join-in-mysql)
- [166: How do you UPDATE a table using values from another table?](#166-how-do-you-update-a-table-using-values-from-another-table)
- [167: How do you DELETE rows based on another table?](#167-how-do-you-delete-rows-based-on-another-table)
- [168: Which is faster, a JOIN or a subquery?](#168-which-is-faster-a-join-or-a-subquery)
- [169: Can you GROUP BY an expression?](#169-can-you-group-by-an-expression)
- [170: What is the difference between GROUP BY and DISTINCT?](#170-what-is-the-difference-between-group-by-and-distinct)
- [171: What does ROLLUP do?](#171-what-does-rollup-do)
- [172: What does CUBE do?](#172-what-does-cube-do)
- [173: What are GROUPING SETS?](#173-what-are-grouping-sets)
- [174: What does the GROUPING() function do?](#174-what-does-the-grouping-function-do)
- [175: What is conditional aggregation?](#175-what-is-conditional-aggregation)
- [176: How do you pivot rows into columns?](#176-how-do-you-pivot-rows-into-columns)
- [177: How do you unpivot columns into rows?](#177-how-do-you-unpivot-columns-into-rows)
- [178: How do you combine values from many rows into one string?](#178-how-do-you-combine-values-from-many-rows-into-one-string)
- [179: How do you find departments whose average salary is above the company average?](#179-how-do-you-find-departments-whose-average-salary-is-above-the-company-average)
- [180: How do you count distinct combinations of several columns?](#180-how-do-you-count-distinct-combinations-of-several-columns)
- [181: What is a subquery?](#181-what-is-a-subquery)
- [182: What kinds of subqueries are there by the shape of their result?](#182-what-kinds-of-subqueries-are-there-by-the-shape-of-their-result)
- [183: What is the difference between a correlated and a non-correlated subquery?](#183-what-is-the-difference-between-a-correlated-and-a-non-correlated-subquery)
- [184: How do you use a subquery in the SELECT list?](#184-how-do-you-use-a-subquery-in-the-select-list)
- [185: What is a derived table?](#185-what-is-a-derived-table)
- [186: What is the difference between IN and EXISTS?](#186-what-is-the-difference-between-in-and-exists)
- [187: What is the difference between NOT IN and NOT EXISTS?](#187-what-is-the-difference-between-not-in-and-not-exists)
- [188: What do ANY, SOME and ALL do?](#188-what-do-any-some-and-all-do)
- [189: How do you find the second highest salary?](#189-how-do-you-find-the-second-highest-salary)
- [190: How do you find the Nth highest salary?](#190-how-do-you-find-the-nth-highest-salary)
- [191: What happens if a scalar subquery returns more than one row?](#191-what-happens-if-a-scalar-subquery-returns-more-than-one-row)
- [192: How do you find employees who earn more than the average in their own department?](#192-how-do-you-find-employees-who-earn-more-than-the-average-in-their-own-department)
- [193: Can you use ORDER BY inside a subquery?](#193-can-you-use-order-by-inside-a-subquery)
- [194: When might a subquery be slower than a join?](#194-when-might-a-subquery-be-slower-than-a-join)
- [195: How do you compare several columns at once against a subquery?](#195-how-do-you-compare-several-columns-at-once-against-a-subquery)
- [196: Is EXISTS (SELECT 1 ...) faster than EXISTS (SELECT \* ...)?](#196-is-exists-select-1--faster-than-exists-select--)
- [197: How do you use a subquery in an UPDATE?](#197-how-do-you-use-a-subquery-in-an-update)
- [198: Can you use a subquery in HAVING?](#198-can-you-use-a-subquery-in-having)
- [199: What is a CTE?](#199-what-is-a-cte)
- [200: What is the difference between a CTE, a derived table and a temporary table?](#200-what-is-the-difference-between-a-cte-a-derived-table-and-a-temporary-table)
- [201: Can you define more than one CTE in a query?](#201-can-you-define-more-than-one-cte-in-a-query)
- [202: Can a CTE be referenced more than once in the same query?](#202-can-a-cte-be-referenced-more-than-once-in-the-same-query)
- [203: What is a recursive CTE?](#203-what-is-a-recursive-cte)
- [204: Are CTEs always materialized?](#204-are-ctes-always-materialized)
- [205: What is a data-modifying CTE?](#205-what-is-a-data-modifying-cte)
- [206: What is the scope of a CTE?](#206-what-is-the-scope-of-a-cte)
- [207: How do you use a recursive CTE to list an employee hierarchy?](#207-how-do-you-use-a-recursive-cte-to-list-an-employee-hierarchy)
- [208: How do you stop a recursive CTE from looping forever?](#208-how-do-you-stop-a-recursive-cte-from-looping-forever)
- [209: What is a window function?](#209-what-is-a-window-function)
- [210: What is the difference between a window function and GROUP BY?](#210-what-is-the-difference-between-a-window-function-and-group-by)
- [211: What are the parts of the OVER clause?](#211-what-are-the-parts-of-the-over-clause)
- [212: What does ROW_NUMBER() do?](#212-what-does-row_number-do)
- [213: What is the difference between ROW_NUMBER, RANK and DENSE_RANK?](#213-what-is-the-difference-between-row_number-rank-and-dense_rank)
- [214: How do you get the top N rows per group?](#214-how-do-you-get-the-top-n-rows-per-group)
- [215: What do LAG and LEAD do?](#215-what-do-lag-and-lead-do)
- [216: Why does LAST_VALUE often return the current row instead of the last row?](#216-why-does-last_value-often-return-the-current-row-instead-of-the-last-row)
- [217: What does NTH_VALUE do?](#217-what-does-nth_value-do)
- [218: What does NTILE do?](#218-what-does-ntile-do)
- [219: How do you calculate a running total?](#219-how-do-you-calculate-a-running-total)
- [220: How do you calculate a moving average?](#220-how-do-you-calculate-a-moving-average)
- [221: What is the difference between ROWS, RANGE and GROUPS in a window frame?](#221-what-is-the-difference-between-rows-range-and-groups-in-a-window-frame)
- [222: What is the default window frame?](#222-what-is-the-default-window-frame)
- [223: What do PERCENT_RANK and CUME_DIST do?](#223-what-do-percent_rank-and-cume_dist-do)
- [224: How do you calculate each row's percentage of the total?](#224-how-do-you-calculate-each-rows-percentage-of-the-total)
- [225: What is the WINDOW clause?](#225-what-is-the-window-clause)
- [226: Can you filter on a window function result in WHERE?](#226-can-you-filter-on-a-window-function-result-in-where)
- [227: How do you calculate the difference between a row and the previous row?](#227-how-do-you-calculate-the-difference-between-a-row-and-the-previous-row)
- [228: Can you use FILTER or CASE inside a window aggregate?](#228-can-you-use-filter-or-case-inside-a-window-aggregate)
- [229: How do you calculate year-over-year growth?](#229-how-do-you-calculate-year-over-year-growth)
- [230: How do you keep only the latest row per key?](#230-how-do-you-keep-only-the-latest-row-per-key)
- [231: What is the difference between UNION and UNION ALL?](#231-what-is-the-difference-between-union-and-union-all)
- [232: What does INTERSECT do?](#232-what-does-intersect-do)
- [233: What does EXCEPT do?](#233-what-does-except-do)
- [234: What are the rules for combining queries with UNION, INTERSECT and EXCEPT?](#234-what-are-the-rules-for-combining-queries-with-union-intersect-and-except)
- [235: How do you sort the result of a UNION?](#235-how-do-you-sort-the-result-of-a-union)
- [236: What are INTERSECT ALL and EXCEPT ALL?](#236-what-are-intersect-all-and-except-all)
- [237: What is the difference between UNION and JOIN?](#237-what-is-the-difference-between-union-and-join)
- [238: How do you compare two tables to find rows that differ?](#238-how-do-you-compare-two-tables-to-find-rows-that-differ)
- [239: What is an index?](#239-what-is-an-index)
- [240: How does a B-tree index work?](#240-how-does-a-b-tree-index-work)
- [241: What is the difference between a clustered and a non-clustered index?](#241-what-is-the-difference-between-a-clustered-and-a-non-clustered-index)
- [242: How do you create and drop an index?](#242-how-do-you-create-and-drop-an-index)
- [243: What is the difference between a unique index and a unique constraint?](#243-what-is-the-difference-between-a-unique-index-and-a-unique-constraint)
- [244: What is a composite index, and what is the leftmost prefix rule?](#244-what-is-a-composite-index-and-what-is-the-leftmost-prefix-rule)
- [245: How do you choose the column order in a composite index?](#245-how-do-you-choose-the-column-order-in-a-composite-index)
- [246: What is a covering index?](#246-what-is-a-covering-index)
- [247: Why would a query not use an index?](#247-why-would-a-query-not-use-an-index)
- [248: What are the downsides of indexes?](#248-what-are-the-downsides-of-indexes)
- [249: Should you index foreign key columns?](#249-should-you-index-foreign-key-columns)
- [250: What is a partial (filtered) index?](#250-what-is-a-partial-filtered-index)
- [251: What is an expression (function-based) index?](#251-what-is-an-expression-function-based-index)
- [252: What are selectivity and cardinality, and why do they matter for indexes?](#252-what-are-selectivity-and-cardinality-and-why-do-they-matter-for-indexes)
- [253: What is the difference between a hash index and a B-tree index?](#253-what-is-the-difference-between-a-hash-index-and-a-b-tree-index)
- [254: How do you check whether a query uses an index?](#254-how-do-you-check-whether-a-query-uses-an-index)
- [255: Is it useful to index a column with very few distinct values?](#255-is-it-useful-to-index-a-column-with-very-few-distinct-values)
- [256: What is a view?](#256-what-is-a-view)
- [257: Why use views?](#257-why-use-views)
- [258: Can you insert, update or delete through a view?](#258-can-you-insert-update-or-delete-through-a-view)
- [259: What does WITH CHECK OPTION do?](#259-what-does-with-check-option-do)
- [260: What is a materialized view?](#260-what-is-a-materialized-view)
- [261: How do you refresh a materialized view?](#261-how-do-you-refresh-a-materialized-view)
- [262: What is the difference between a table, a view and a materialized view?](#262-what-is-the-difference-between-a-table-a-view-and-a-materialized-view)
- [263: Do views make queries faster?](#263-do-views-make-queries-faster)
- [264: What is a transaction?](#264-what-is-a-transaction)
- [265: What does ACID mean?](#265-what-does-acid-mean)
- [266: What do COMMIT and ROLLBACK do?](#266-what-do-commit-and-rollback-do)
- [267: What is a SAVEPOINT?](#267-what-is-a-savepoint)
- [268: What is autocommit?](#268-what-is-autocommit)
- [269: What is a lock?](#269-what-is-a-lock)
- [270: What is a deadlock?](#270-what-is-a-deadlock)
- [271: What are the standard transaction isolation levels?](#271-what-are-the-standard-transaction-isolation-levels)
- [272: What is a dirty read?](#272-what-is-a-dirty-read)
- [273: What is a non-repeatable read?](#273-what-is-a-non-repeatable-read)
- [274: What is a phantom read?](#274-what-is-a-phantom-read)
- [275: What are the default isolation levels in popular databases?](#275-what-are-the-default-isolation-levels-in-popular-databases)
- [276: What does SELECT ... FOR UPDATE do?](#276-what-does-select--for-update-do)
- [277: What is the difference between optimistic and pessimistic locking?](#277-what-is-the-difference-between-optimistic-and-pessimistic-locking)
- [278: What is an upsert?](#278-what-is-an-upsert)
- [279: How do you write an upsert in PostgreSQL?](#279-how-do-you-write-an-upsert-in-postgresql)
- [280: How do you write an upsert in MySQL?](#280-how-do-you-write-an-upsert-in-mysql)
- [281: What is the MERGE statement?](#281-what-is-the-merge-statement)
- [282: What does WHEN NOT MATCHED BY SOURCE do in MERGE?](#282-what-does-when-not-matched-by-source-do-in-merge)
- [283: How do you get back the rows that an INSERT, UPDATE or DELETE changed?](#283-how-do-you-get-back-the-rows-that-an-insert-update-or-delete-changed)
- [284: How do you load a lot of data quickly?](#284-how-do-you-load-a-lot-of-data-quickly)
- [285: How do you update different rows with different values in one statement?](#285-how-do-you-update-different-rows-with-different-values-in-one-statement)
- [286: How do you delete millions of rows without causing problems?](#286-how-do-you-delete-millions-of-rows-without-causing-problems)
- [287: Does TRUNCATE reset identity columns, and can it be rolled back?](#287-does-truncate-reset-identity-columns-and-can-it-be-rolled-back)
- [288: How do you insert rows but skip the ones that already exist?](#288-how-do-you-insert-rows-but-skip-the-ones-that-already-exist)
- [289: How do you swap the values of two columns?](#289-how-do-you-swap-the-values-of-two-columns)
- [290: What is a sequence?](#290-what-is-a-sequence)
- [291: How do you calculate the difference between two dates?](#291-how-do-you-calculate-the-difference-between-two-dates)
- [292: How do you round a date down to the start of the month?](#292-how-do-you-round-a-date-down-to-the-start-of-the-month)
- [293: How do you generate a list of dates?](#293-how-do-you-generate-a-list-of-dates)
- [294: How do you show days with zero sales in a daily report?](#294-how-do-you-show-days-with-zero-sales-in-a-daily-report)
- [295: How do you convert a timestamp between time zones?](#295-how-do-you-convert-a-timestamp-between-time-zones)
- [296: How do you use regular expressions in SQL?](#296-how-do-you-use-regular-expressions-in-sql)
- [297: How do you split a comma-separated string into rows?](#297-how-do-you-split-a-comma-separated-string-into-rows)
- [298: How are NULLs treated in UNIQUE constraints, and what is NULLS NOT DISTINCT?](#298-how-are-nulls-treated-in-unique-constraints-and-what-is-nulls-not-distinct)
- [299: What is the difference between COALESCE, ISNULL, IFNULL and NVL?](#299-what-is-the-difference-between-coalesce-isnull-ifnull-and-nvl)
- [300: What is a collation?](#300-what-is-a-collation)

### Advanced Questions (301-450)

- [301: What happens inside the database when you run a query?](#301-what-happens-inside-the-database-when-you-run-a-query)
- [302: What is a cost-based optimizer?](#302-what-is-a-cost-based-optimizer)
- [303: How do you read an execution plan?](#303-how-do-you-read-an-execution-plan)
- [304: What is the difference between EXPLAIN and EXPLAIN ANALYZE?](#304-what-is-the-difference-between-explain-and-explain-analyze)
- [305: What are the different ways a database can read a table?](#305-what-are-the-different-ways-a-database-can-read-a-table)
- [306: What are nested loop, hash join and merge join?](#306-what-are-nested-loop-hash-join-and-merge-join)
- [307: What are database statistics and how are they kept up to date?](#307-what-are-database-statistics-and-how-are-they-kept-up-to-date)
- [308: Why are row estimates sometimes very wrong, and what can you do?](#308-why-are-row-estimates-sometimes-very-wrong-and-what-can-you-do)
- [309: What does "sargable" mean?](#309-what-does-sargable-mean)
- [310: What is parameter sniffing?](#310-what-is-parameter-sniffing)
- [311: What are prepared statements and why use them?](#311-what-are-prepared-statements-and-why-use-them)
- [312: Why is OFFSET pagination slow for large page numbers, and what is keyset pagination?](#312-why-is-offset-pagination-slow-for-large-page-numbers-and-what-is-keyset-pagination)
- [313: What is the N+1 query problem?](#313-what-is-the-n1-query-problem)
- [314: How do you approach tuning a slow query?](#314-how-do-you-approach-tuning-a-slow-query)
- [315: Why can rewriting OR as UNION ALL make a query faster?](#315-why-can-rewriting-or-as-union-all-make-a-query-faster)
- [316: Why is COUNT(\*) slow on a large PostgreSQL table, and what can you do?](#316-why-is-count-slow-on-a-large-postgresql-table-and-what-can-you-do)
- [317: How can an implicit type conversion make a query slow?](#317-how-can-an-implicit-type-conversion-make-a-query-slow)
- [318: What are query hints and when should you use them?](#318-what-are-query-hints-and-when-should-you-use-them)
- [319: What is an index-only scan and what does it depend on in PostgreSQL?](#319-what-is-an-index-only-scan-and-what-does-it-depend-on-in-postgresql)
- [320: What is a GIN index?](#320-what-is-a-gin-index)
- [321: What are GiST and BRIN indexes?](#321-what-are-gist-and-brin-indexes)
- [322: How does full-text search work in SQL databases?](#322-how-does-full-text-search-work-in-sql-databases)
- [323: How do you index fields inside JSON documents?](#323-how-do-you-index-fields-inside-json-documents)
- [324: What is index bloat or fragmentation, and how do you fix it?](#324-what-is-index-bloat-or-fragmentation-and-how-do-you-fix-it)
- [325: How do you create an index on a busy production table without blocking writes?](#325-how-do-you-create-an-index-on-a-busy-production-table-without-blocking-writes)
- [326: What is an index skip scan?](#326-what-is-an-index-skip-scan)
- [327: What is a columnstore index?](#327-what-is-a-columnstore-index)
- [328: How do you find indexes that are never used?](#328-how-do-you-find-indexes-that-are-never-used)
- [329: How can an index make ORDER BY ... LIMIT fast?](#329-how-can-an-index-make-order-by--limit-fast)
- [330: Is one composite index better than several single-column indexes?](#330-is-one-composite-index-better-than-several-single-column-indexes)
- [331: When do you need a descending index?](#331-when-do-you-need-a-descending-index)
- [332: What are HOT updates in PostgreSQL?](#332-what-are-hot-updates-in-postgresql)
- [333: What is MVCC?](#333-what-is-mvcc)
- [334: What is the difference between snapshot isolation and serializable?](#334-what-is-the-difference-between-snapshot-isolation-and-serializable)
- [335: What is write skew?](#335-what-is-write-skew)
- [336: What is a lost update and how do you prevent it?](#336-what-is-a-lost-update-and-how-do-you-prevent-it)
- [337: How does SERIALIZABLE work in PostgreSQL?](#337-how-does-serializable-work-in-postgresql)
- [338: What is Read Committed Snapshot Isolation (RCSI) in SQL Server?](#338-what-is-read-committed-snapshot-isolation-rcsi-in-sql-server)
- [339: What lock types and lock modes exist?](#339-what-lock-types-and-lock-modes-exist)
- [340: What is lock escalation?](#340-what-is-lock-escalation)
- [341: How do you build a job queue in SQL with SKIP LOCKED?](#341-how-do-you-build-a-job-queue-in-sql-with-skip-locked)
- [342: What does NOWAIT do?](#342-what-does-nowait-do)
- [343: What are advisory locks?](#343-what-are-advisory-locks)
- [344: How do you reduce deadlocks?](#344-how-do-you-reduce-deadlocks)
- [345: What are gap locks and next-key locks in MySQL InnoDB?](#345-what-are-gap-locks-and-next-key-locks-in-mysql-innodb)
- [346: Why are long-running transactions a problem?](#346-why-are-long-running-transactions-a-problem)
- [347: What does VACUUM do in PostgreSQL?](#347-what-does-vacuum-do-in-postgresql)
- [348: What is transaction ID wraparound in PostgreSQL?](#348-what-is-transaction-id-wraparound-in-postgresql)
- [349: How should an application handle serialization failures and deadlocks?](#349-how-should-an-application-handle-serialization-failures-and-deadlocks)
- [350: What does it mean for a database operation to be idempotent, and why does it matter?](#350-what-does-it-mean-for-a-database-operation-to-be-idempotent-and-why-does-it-matter)
- [351: What is two-phase commit?](#351-what-is-two-phase-commit)
- [352: How do you stop queries from running too long or waiting too long for locks?](#352-how-do-you-stop-queries-from-running-too-long-or-waiting-too-long-for-locks)
- [353: What is the gaps and islands problem, and how do you solve it?](#353-what-is-the-gaps-and-islands-problem-and-how-do-you-solve-it)
- [354: How do you find each user's longest streak of consecutive login days?](#354-how-do-you-find-each-users-longest-streak-of-consecutive-login-days)
- [355: How do you calculate a running total that resets when a condition happens?](#355-how-do-you-calculate-a-running-total-that-resets-when-a-condition-happens)
- [356: How do you calculate a median?](#356-how-do-you-calculate-a-median)
- [357: How do you find the most common value (mode)?](#357-how-do-you-find-the-most-common-value-mode)
- [358: How do you group events into sessions?](#358-how-do-you-group-events-into-sessions)
- [359: How do you calculate a running count of distinct values?](#359-how-do-you-calculate-a-running-count-of-distinct-values)
- [360: How do you build a monthly retention cohort table?](#360-how-do-you-build-a-monthly-retention-cohort-table)
- [361: How do you calculate a conversion funnel?](#361-how-do-you-calculate-a-conversion-funnel)
- [362: How do you return the top 3 values per group, including ties?](#362-how-do-you-return-the-top-3-values-per-group-including-ties)
- [363: How do you find which products make up 80% of revenue (Pareto analysis)?](#363-how-do-you-find-which-products-make-up-80-of-revenue-pareto-analysis)
- [364: What does the EXCLUDE clause do in a window frame?](#364-what-does-the-exclude-clause-do-in-a-window-frame)
- [365: What is MATCH_RECOGNIZE?](#365-what-is-match_recognize)
- [366: How do you fill NULLs with the last known value (forward fill)?](#366-how-do-you-fill-nulls-with-the-last-known-value-forward-fill)
- [367: How do you calculate a rolling sum over a time period instead of a number of rows?](#367-how-do-you-calculate-a-rolling-sum-over-a-time-period-instead-of-a-number-of-rows)
- [368: How do you compare each row to the best value in its group?](#368-how-do-you-compare-each-row-to-the-best-value-in-its-group)
- [369: How does a recursive CTE actually run?](#369-how-does-a-recursive-cte-actually-run)
- [370: How do you build the full path of each node in a hierarchy?](#370-how-do-you-build-the-full-path-of-each-node-in-a-hierarchy)
- [371: How do you find all ancestors of a node (walk up the tree)?](#371-how-do-you-find-all-ancestors-of-a-node-walk-up-the-tree)
- [372: How do you detect cycles in hierarchical data?](#372-how-do-you-detect-cycles-in-hierarchical-data)
- [373: What does the SEARCH clause do in recursive CTEs?](#373-what-does-the-search-clause-do-in-recursive-ctes)
- [374: What are the different ways to store a tree in SQL?](#374-what-are-the-different-ways-to-store-a-tree-in-sql)
- [375: What is the ltree type in PostgreSQL?](#375-what-is-the-ltree-type-in-postgresql)
- [376: How do you calculate total quantities in a bill of materials?](#376-how-do-you-calculate-total-quantities-in-a-bill-of-materials)
- [377: Can you find the shortest path between two nodes in SQL?](#377-can-you-find-the-shortest-path-between-two-nodes-in-sql)
- [378: What is SQL/PGQ?](#378-what-is-sqlpgq)
- [379: What is the difference between json and jsonb in PostgreSQL?](#379-what-is-the-difference-between-json-and-jsonb-in-postgresql)
- [380: How do you read values out of a JSON column?](#380-how-do-you-read-values-out-of-a-json-column)
- [381: What is the difference between JSON_VALUE and JSON_QUERY?](#381-what-is-the-difference-between-json_value-and-json_query)
- [382: What is JSON_TABLE?](#382-what-is-json_table)
- [383: How do you check whether a JSON document contains a key or value?](#383-how-do-you-check-whether-a-json-document-contains-a-key-or-value)
- [384: How do you build JSON output from SQL?](#384-how-do-you-build-json-output-from-sql)
- [385: What JSON improvements did SQL:2023 bring?](#385-what-json-improvements-did-sql2023-bring)
- [386: How do you update one field inside a JSON column?](#386-how-do-you-update-one-field-inside-a-json-column)
- [387: When should you use a JSON column, and when should you use normal columns?](#387-when-should-you-use-a-json-column-and-when-should-you-use-normal-columns)
- [388: How do you check if a string is valid JSON?](#388-how-do-you-check-if-a-string-is-valid-json)
- [389: How do you work with arrays in PostgreSQL?](#389-how-do-you-work-with-arrays-in-postgresql)
- [390: How do you turn a JSON array into rows?](#390-how-do-you-turn-a-json-array-into-rows)
- [391: How do you store and search vector embeddings in SQL databases?](#391-how-do-you-store-and-search-vector-embeddings-in-sql-databases)
- [392: What is the difference between exact and approximate nearest neighbor search?](#392-what-is-the-difference-between-exact-and-approximate-nearest-neighbor-search)
- [393: What is table partitioning?](#393-what-is-table-partitioning)
- [394: What partitioning methods are there?](#394-what-partitioning-methods-are-there)
- [395: What is partition pruning?](#395-what-is-partition-pruning)
- [396: What is the difference between partitioning and sharding?](#396-what-is-the-difference-between-partitioning-and-sharding)
- [397: What is database replication, and what is the difference between synchronous and asynchronous replication?](#397-what-is-database-replication-and-what-is-the-difference-between-synchronous-and-asynchronous-replication)
- [398: What is replication lag and how does it affect applications?](#398-what-is-replication-lag-and-how-does-it-affect-applications)
- [399: What is the difference between vertical and horizontal scaling for databases?](#399-what-is-the-difference-between-vertical-and-horizontal-scaling-for-databases)
- [400: Why is connection pooling important?](#400-why-is-connection-pooling-important)
- [401: How do you archive or remove old data from a very large table?](#401-how-do-you-archive-or-remove-old-data-from-a-very-large-table)
- [402: When does denormalization make sense for performance?](#402-when-does-denormalization-make-sense-for-performance)
- [403: What is the difference between OLTP and OLAP?](#403-what-is-the-difference-between-oltp-and-olap)
- [404: Why are columnar databases faster for analytics?](#404-why-are-columnar-databases-faster-for-analytics)
- [405: What does the CAP theorem say, and how does it apply to distributed SQL databases?](#405-what-does-the-cap-theorem-say-and-how-does-it-apply-to-distributed-sql-databases)
- [406: What is the difference between a stored procedure and a function?](#406-what-is-the-difference-between-a-stored-procedure-and-a-function)
- [407: How do you create a function?](#407-how-do-you-create-a-function)
- [408: How do you write a stored procedure with transaction control?](#408-how-do-you-write-a-stored-procedure-with-transaction-control)
- [409: What is a trigger, and what kinds are there?](#409-what-is-a-trigger-and-what-kinds-are-there)
- [410: How do you write an audit trigger?](#410-how-do-you-write-an-audit-trigger)
- [411: What is an INSTEAD OF trigger?](#411-what-is-an-instead-of-trigger)
- [412: What are the downsides of triggers?](#412-what-are-the-downsides-of-triggers)
- [413: What is dynamic SQL, and how do you write it safely?](#413-what-is-dynamic-sql-and-how-do-you-write-it-safely)
- [414: What is a cursor, and why are cursors often discouraged?](#414-what-is-a-cursor-and-why-are-cursors-often-discouraged)
- [415: How do you handle errors in stored procedures?](#415-how-do-you-handle-errors-in-stored-procedures)
- [416: What is a table-valued function?](#416-what-is-a-table-valued-function)
- [417: What do IMMUTABLE, STABLE and VOLATILE mean for PostgreSQL functions?](#417-what-do-immutable-stable-and-volatile-mean-for-postgresql-functions)
- [418: What are system-versioned temporal tables?](#418-what-are-system-versioned-temporal-tables)
- [419: What is normalization and why do it?](#419-what-is-normalization-and-why-do-it)
- [420: What is First Normal Form (1NF)?](#420-what-is-first-normal-form-1nf)
- [421: What is Second Normal Form (2NF)?](#421-what-is-second-normal-form-2nf)
- [422: What is Third Normal Form (3NF)?](#422-what-is-third-normal-form-3nf)
- [423: What is Boyce-Codd Normal Form (BCNF)?](#423-what-is-boyce-codd-normal-form-bcnf)
- [424: What are 4NF and 5NF?](#424-what-are-4nf-and-5nf)
- [425: When is it OK to denormalize?](#425-when-is-it-ok-to-denormalize)
- [426: What is the difference between a star schema and a snowflake schema?](#426-what-is-the-difference-between-a-star-schema-and-a-snowflake-schema)
- [427: What are slowly changing dimensions (SCD)?](#427-what-are-slowly-changing-dimensions-scd)
- [428: How do you model a many-to-many relationship?](#428-how-do-you-model-a-many-to-many-relationship)
- [429: What are the pros and cons of soft deletes?](#429-what-are-the-pros-and-cons-of-soft-deletes)
- [430: What is the Entity-Attribute-Value (EAV) pattern and why is it usually avoided?](#430-what-is-the-entity-attribute-value-eav-pattern-and-why-is-it-usually-avoided)
- [431: What is SQL injection?](#431-what-is-sql-injection)
- [432: How do you prevent SQL injection?](#432-how-do-you-prevent-sql-injection)
- [433: How do GRANT and REVOKE work?](#433-how-do-grant-and-revoke-work)
- [434: What are roles and why use them?](#434-what-are-roles-and-why-use-them)
- [435: What is row-level security?](#435-what-is-row-level-security)
- [436: What does the principle of least privilege mean for databases?](#436-what-does-the-principle-of-least-privilege-mean-for-databases)
- [437: How do you protect sensitive data stored in a database?](#437-how-do-you-protect-sensitive-data-stored-in-a-database)
- [438: How do you audit who changed or read data?](#438-how-do-you-audit-who-changed-or-read-data)
- [439: How do you find customers who bought every product in a category?](#439-how-do-you-find-customers-who-bought-every-product-in-a-category)
- [440: How do you find the department with the highest total salary, including ties?](#440-how-do-you-find-the-department-with-the-highest-total-salary-including-ties)
- [441: How do you calculate month-over-month revenue change, including months with no revenue?](#441-how-do-you-calculate-month-over-month-revenue-change-including-months-with-no-revenue)
- [442: How do you find overlapping bookings?](#442-how-do-you-find-overlapping-bookings)
- [443: How do you merge overlapping time ranges into continuous periods?](#443-how-do-you-merge-overlapping-time-ranges-into-continuous-periods)
- [444: How do you calculate a running account balance?](#444-how-do-you-calculate-a-running-account-balance)
- [445: How do you find each customer's first order and what they bought in it?](#445-how-do-you-find-each-customers-first-order-and-what-they-bought-in-it)
- [446: How do you get the top 2 products by revenue in each category for the last 30 days?](#446-how-do-you-get-the-top-2-products-by-revenue-in-each-category-for-the-last-30-days)
- [447: How do you calculate the percentage of late deliveries per month?](#447-how-do-you-calculate-the-percentage-of-late-deliveries-per-month)
- [448: How do you find duplicate customers whose emails differ only in case or spaces?](#448-how-do-you-find-duplicate-customers-whose-emails-differ-only-in-case-or-spaces)
- [449: How do you find 3 or more consecutive free seats in a row?](#449-how-do-you-find-3-or-more-consecutive-free-seats-in-a-row)
- [450: How do you suggest friends based on mutual friends?](#450-how-do-you-suggest-friends-based-on-mutual-friends)

---

## Easy Questions (1-150)

### SQL Basics

#### 1: What is SQL?

SQL (Structured Query Language) is the language used to work with relational databases. You use it to create tables, add and change data, read data back, and control who can access what. It is a declarative language: you describe the result you want, and the database decides how to get it.

```sql
SELECT first_name, last_name
FROM employees
WHERE department_id = 3;
```

#### 2: What is a database?

A database is an organized collection of data stored so that it can be easily read, searched and updated. In practice the word usually means both the data and the software that manages it.

#### 3: What is a relational database?

A relational database stores data in tables (relations). Each table has columns with fixed types and rows that hold the actual records. Tables are linked to each other through keys, for example `orders.customer_id` points to `customers.id`. PostgreSQL, MySQL, SQL Server, Oracle and SQLite are all relational databases.

#### 4: What is the difference between a DBMS and an RDBMS?

A DBMS (Database Management System) is any software that stores and manages data. It could store data as documents, key-value pairs, graphs or files. An RDBMS is a DBMS that stores data in related tables and uses SQL. MongoDB is a DBMS but not an RDBMS. PostgreSQL is an RDBMS.

#### 5: What are tables, rows and columns?

- A **table** holds data about one kind of thing, like customers or orders.
- A **column** is one attribute of that thing, like `email`, and has a data type.
- A **row** is one record, like a single customer.

The value where a row and column meet is sometimes called a field or a cell.

#### 6: What are the main groups of SQL commands?

| Group | Meaning                      | Commands                              |
| ----- | ---------------------------- | ------------------------------------- |
| DDL   | Data Definition Language     | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| DML   | Data Manipulation Language   | `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| DQL   | Data Query Language          | `SELECT`                              |
| DCL   | Data Control Language        | `GRANT`, `REVOKE`                     |
| TCL   | Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT`     |

Some people put `SELECT` under DML. Both ways are fine in an interview as long as you know what each command does.

#### 7: What is the difference between SQL and MySQL (or PostgreSQL)?

SQL is the language. MySQL, PostgreSQL, SQL Server and Oracle are database products that understand SQL. Each product follows the SQL standard to a different degree and adds its own extensions. For example, MySQL and PostgreSQL use `LIMIT`, while SQL Server uses `TOP`, and the standard way is `FETCH FIRST n ROWS ONLY`.

#### 8: Is SQL case sensitive?

SQL keywords are not case sensitive. `SELECT`, `select` and `SeLeCt` are the same. Identifiers (table and column names) depend on the database:

- PostgreSQL folds unquoted names to lowercase. `"Users"` with quotes is a different name than `users`.
- MySQL table names can be case sensitive on Linux because tables map to files.
- SQL Server depends on the collation.

String comparisons depend on the collation. In MySQL and SQL Server the default is usually case-insensitive. In PostgreSQL it is case-sensitive.

#### 9: What is the latest version of the SQL standard?

The latest version is **SQL:2023** (ISO/IEC 9075:2023). Earlier versions were SQL-86, SQL-89, SQL-92, SQL:1999, SQL:2003, SQL:2006, SQL:2008, SQL:2011 and SQL:2016.

Things added in SQL:2023 include:

- A native `JSON` data type and simpler JSON access
- Property graph queries (SQL/PGQ, a new Part 16)
- `GREATEST` and `LEAST`
- `LPAD`, `RPAD`, `LTRIM`, `RTRIM`, `BTRIM`
- `ANY_VALUE` aggregate
- `UNIQUE NULLS NOT DISTINCT`
- Hex, octal and binary integer literals like `0xFF`, and underscores in numbers like `1_000_000`

No database implements the whole standard. Each one picks parts of it.

#### 10: What is a query?

A query is a request for data from the database. Most of the time it means a `SELECT` statement, but people also call `INSERT`, `UPDATE` and `DELETE` statements queries.

#### 11: What is a schema?

A schema is a named container inside a database that holds tables, views, functions and other objects. It helps group objects and manage permissions. In PostgreSQL the default schema is `public`, in SQL Server it is `dbo`. In MySQL, schema and database mean the same thing.

```sql
CREATE SCHEMA sales;
CREATE TABLE sales.invoices (id INT PRIMARY KEY, amount DECIMAL(10,2));
```

The word "schema" is also used for the overall structure of a database (all its tables and relationships).

#### 12: In what order do you write the clauses of a SELECT statement?

```sql
SELECT    column_list
FROM      table_name
JOIN      other_table ON ...
WHERE     row_condition
GROUP BY  columns
HAVING    group_condition
ORDER BY  columns
OFFSET    n ROWS
FETCH FIRST m ROWS ONLY;
```

Only `SELECT` is required in most databases. `FROM` is needed when you read from a table.

#### 13: In what order does the database logically process a SELECT statement?

The logical order is different from the written order:

1. `FROM` and `JOIN`
2. `WHERE`
3. `GROUP BY`
4. `HAVING`
5. `SELECT` (including window functions)
6. `DISTINCT`
7. `ORDER BY`
8. `OFFSET` / `FETCH` / `LIMIT`

This explains a lot of common errors. For example, you can't use a `SELECT` alias in `WHERE`, because `WHERE` runs before `SELECT`. You can use it in `ORDER BY`, because `ORDER BY` runs after. The optimizer may run things in a different physical order, but the result must be the same as this logical order.

#### 14: How do you write comments in SQL?

```sql
-- This is a single-line comment

/* This is a
   multi-line comment */

SELECT id, name  -- comment at the end of a line
FROM customers;
```

MySQL also accepts `#` for single-line comments, and needs a space after `--`.

#### 15: What is NULL?

`NULL` means a value is missing or unknown. It is not zero, not an empty string and not false. Any comparison with `NULL` using `=`, `<>`, `<` or `>` gives `UNKNOWN`, not `TRUE`. That is why you must use `IS NULL` and `IS NOT NULL`.

```sql
SELECT * FROM employees WHERE manager_id IS NULL;
```

#### 16: What is the difference between NULL, zero and an empty string?

- `0` is a real number.
- `''` is a real string with length zero.
- `NULL` means there is no value at all.

`NULL + 5` returns `NULL`, but `0 + 5` returns `5`. One thing to watch out for: Oracle treats an empty string `''` as `NULL`. Other databases do not.

#### 17: What is the semicolon used for in SQL?

The semicolon ends a statement. It lets you run several statements in one batch. Some tools let you skip it for a single statement, but it's a good habit to always use it. SQL Server requires it before some statements, for example before a `WITH` (CTE) if a previous statement exists in the batch, and at the end of `MERGE`.

#### 18: What is the difference between single quotes and double quotes in SQL?

In standard SQL:

- Single quotes are for string values: `'London'`
- Double quotes are for identifiers (names of tables and columns): `"order"`

```sql
SELECT "order", 'text value' AS label FROM "my table";
```

MySQL uses backticks for identifiers by default and treats double quotes as strings unless `ANSI_QUOTES` mode is on. SQL Server also accepts square brackets: `[my table]`.

#### 19: How do you put a single quote inside a string?

Write it twice.

```sql
SELECT 'It''s raining' AS message;
-- Result: It's raining
```

PostgreSQL also has dollar quoting (`$$It's raining$$`) and MySQL accepts a backslash (`'It\'s'`), but doubling the quote works everywhere.

#### 20: What is an alias?

An alias is a temporary name for a column or a table inside one query.

```sql
SELECT e.first_name AS name,
       e.salary * 12 AS yearly_salary
FROM employees AS e;
```

The `AS` keyword is optional for columns in most databases. Oracle does not allow `AS` before a table alias.

### Data Types

#### 21: What are the main categories of SQL data types?

- **Numeric**: `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`/`NUMERIC`, `REAL`, `DOUBLE PRECISION`
- **Character**: `CHAR`, `VARCHAR`, `TEXT` (or `CLOB`)
- **Date and time**: `DATE`, `TIME`, `TIMESTAMP`, `INTERVAL`
- **Boolean**: `BOOLEAN`
- **Binary**: `BINARY`, `VARBINARY`, `BLOB`, `BYTEA`
- **Other**: `JSON`, `UUID`, `XML`, arrays, spatial types, and vector types in newer versions

#### 22: What is the difference between CHAR and VARCHAR?

`CHAR(n)` is fixed length. If you store `'abc'` in `CHAR(10)`, it is padded with spaces to 10 characters. `VARCHAR(n)` is variable length and stores only what you give it, up to `n` characters.

Use `CHAR` only for values that always have the same length, such as country codes (`'US'`, `'GE'`). Use `VARCHAR` for almost everything else.

#### 23: What is the difference between VARCHAR and TEXT?

It depends on the database:

- **PostgreSQL**: `TEXT` and `VARCHAR` without a limit work the same and perform the same. `VARCHAR(n)` just adds a length check.
- **MySQL**: `TEXT` is stored differently, can't have a default value (before 8.0.13), and needs a prefix length when indexed. `VARCHAR` is usually better for short strings.
- **SQL Server**: `TEXT` is deprecated. Use `VARCHAR(MAX)` or `NVARCHAR(MAX)`.

#### 24: What is the difference between INT, SMALLINT and BIGINT?

They store whole numbers with different ranges:

| Type              | Size    | Range                                     |
| ----------------- | ------- | ----------------------------------------- |
| `SMALLINT`        | 2 bytes | -32,768 to 32,767                         |
| `INT` / `INTEGER` | 4 bytes | about -2.1 billion to 2.1 billion         |
| `BIGINT`          | 8 bytes | about -9.2 quintillion to 9.2 quintillion |

For primary keys on tables that may grow large, `BIGINT` is a safe choice. Running out of `INT` values on a busy table is a real and painful problem.

#### 25: What is the difference between DECIMAL and FLOAT?

`DECIMAL(p, s)` (same as `NUMERIC`) stores exact numbers. `p` is the total number of digits and `s` is the number of digits after the decimal point. `DECIMAL(10, 2)` can store `12345678.90`.

`FLOAT`, `REAL` and `DOUBLE PRECISION` store approximate numbers in binary. They are faster and cover a wider range, but can't represent many decimal values exactly.

```sql
SELECT 0.1::float8 + 0.2::float8;   -- 0.30000000000000004 (PostgreSQL)
SELECT 0.1::numeric + 0.2::numeric; -- 0.3
```

#### 26: Why should you not store money in a FLOAT column?

Because floating point values are approximate. Small rounding errors add up when you sum many values, and comparisons like `amount = 0.3` can fail. Use `DECIMAL`/`NUMERIC` with a fixed scale, or store the amount as an integer number of cents.

#### 27: What are the DATE, TIME and TIMESTAMP types?

- `DATE` stores a calendar date: `2026-03-15`
- `TIME` stores a time of day: `14:30:00`
- `TIMESTAMP` stores both: `2026-03-15 14:30:00`

SQL Server calls its timestamp type `DATETIME2` (the old `DATETIME` is less precise). In SQL Server, the type named `TIMESTAMP` is something else: it's a row version number, also called `ROWVERSION`.

```sql
SELECT DATE '2026-03-15', TIMESTAMP '2026-03-15 14:30:00';
```

#### 28: What is the difference between TIMESTAMP and TIMESTAMP WITH TIME ZONE?

`TIMESTAMP` (without time zone) stores a date and time with no information about which time zone it belongs to. `TIMESTAMP WITH TIME ZONE` represents an exact moment in time.

In PostgreSQL, `timestamptz` converts the input to UTC when storing and converts it back to the session time zone when reading. It does not store the original zone. SQL Server's `DATETIMEOFFSET` stores the offset with the value.

For events that happen at a specific moment (logins, payments), use the time zone aware type.

#### 29: Does SQL have a BOOLEAN type?

The standard has `BOOLEAN` with values `TRUE`, `FALSE` and `UNKNOWN` (`NULL`). Support differs:

- PostgreSQL and SQLite (which stores it as 0/1) support it.
- MySQL accepts `BOOLEAN` but it is really `TINYINT(1)`.
- SQL Server uses `BIT` (0 or 1).
- Oracle added a real `BOOLEAN` type for tables in Oracle 23ai.

```sql
CREATE TABLE tasks (id INT PRIMARY KEY, is_done BOOLEAN DEFAULT FALSE);
```

#### 30: How do you store binary data such as images?

Use a binary type: `BYTEA` in PostgreSQL, `BLOB` in MySQL and Oracle, `VARBINARY(MAX)` in SQL Server. In most real applications, large files are stored in object storage (like S3) and the table keeps only the file path or URL and some metadata. This keeps the database smaller and backups faster.

#### 31: What is a UUID and when would you use it?

A UUID is a 128-bit identifier, written like `550e8400-e29b-41d4-a716-446655440000`. It can be generated anywhere without asking the database, which is useful in distributed systems.

Random UUIDs (version 4) are bad for B-tree indexes because new values land in random places in the index. UUID version 7 starts with a timestamp, so new values are roughly in order. PostgreSQL 18 added a built-in `uuidv7()` function.

```sql
CREATE TABLE events (
    id      UUID PRIMARY KEY DEFAULT uuidv7(),  -- PostgreSQL 18
    payload TEXT
);
```

#### 32: Is there a JSON data type in SQL?

Yes. SQL:2023 added a `JSON` type to the standard. In practice:

- PostgreSQL has `json` (stores text as is) and `jsonb` (binary, indexable, usually the better choice).
- MySQL has `JSON` (stored in a binary format).
- SQL Server 2025 added a native `json` type. Older versions store JSON in `NVARCHAR`.
- Oracle 21c and later have a native `JSON` type.

```sql
CREATE TABLE settings (user_id INT PRIMARY KEY, prefs JSONB);
```

#### 33: How do you convert a value from one data type to another?

Use `CAST`, which is standard SQL.

```sql
SELECT CAST('2026-01-15' AS DATE);
SELECT CAST(salary AS INT) FROM employees;
```

PostgreSQL also has the `::` shortcut (`'42'::int`). SQL Server has `CONVERT` and `TRY_CAST`, which returns `NULL` instead of an error if the conversion fails.

#### 34: What is the difference between implicit and explicit conversion?

Explicit conversion is when you write `CAST` yourself. Implicit conversion is when the database converts a value on its own, like comparing a `VARCHAR` column to a number. Implicit conversion can give surprising results and can stop the database from using an index. It's better to compare values of the same type.

```sql
-- phone is VARCHAR. This can force a conversion on every row:
SELECT * FROM customers WHERE phone = 5551234;
-- Better:
SELECT * FROM customers WHERE phone = '5551234';
```

#### 35: What new numeric literal formats did SQL:2023 add?

You can now write integers in hexadecimal, octal and binary, and use underscores to make big numbers easier to read. PostgreSQL 16 and later support these.

```sql
SELECT 0xFF;        -- 255
SELECT 0o17;        -- 15
SELECT 0b1010;      -- 10
SELECT 1_000_000;   -- 1000000
```

### Creating and Changing Tables

#### 36: How do you create a database?

```sql
CREATE DATABASE shop;
```

Creating a database is not fully covered by the SQL standard, so options differ. In PostgreSQL you can't run `CREATE DATABASE` inside a transaction. In MySQL, `CREATE DATABASE` and `CREATE SCHEMA` are the same.

#### 37: How do you create a table?

```sql
CREATE TABLE customers (
    id         INT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    email      VARCHAR(255) UNIQUE,
    country    VARCHAR(50) DEFAULT 'Unknown',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

You list each column with its type and optional constraints.

#### 38: How do you add a column to an existing table?

```sql
ALTER TABLE customers ADD COLUMN phone VARCHAR(20);
```

SQL Server and Oracle don't use the word `COLUMN`: `ALTER TABLE customers ADD phone VARCHAR(20);`. Adding a nullable column, or one with a constant default, is fast in modern PostgreSQL, MySQL 8 and SQL Server because they don't need to rewrite the table.

#### 39: How do you remove a column?

```sql
ALTER TABLE customers DROP COLUMN phone;
```

If a view, index or constraint depends on the column, the database may refuse. In PostgreSQL you can add `CASCADE` to drop the dependent objects too, but be careful with that.

#### 40: How do you rename a table or a column?

```sql
ALTER TABLE customers RENAME TO clients;
ALTER TABLE clients RENAME COLUMN name TO full_name;
```

This works in PostgreSQL, MySQL 8, Oracle and SQLite. SQL Server uses a stored procedure:

```sql
EXEC sp_rename 'customers', 'clients';
EXEC sp_rename 'clients.name', 'full_name', 'COLUMN';
```

#### 41: How do you change the data type of a column?

```sql
-- PostgreSQL
ALTER TABLE products ALTER COLUMN price TYPE DECIMAL(12, 2);

-- MySQL
ALTER TABLE products MODIFY COLUMN price DECIMAL(12, 2);

-- SQL Server
ALTER TABLE products ALTER COLUMN price DECIMAL(12, 2);
```

Changing a type can rewrite the whole table and lock it, so on big tables plan this carefully.

#### 42: What is the difference between DELETE, TRUNCATE and DROP?

|                       | `DELETE`               | `TRUNCATE`                                                                 | `DROP`             |
| --------------------- | ---------------------- | -------------------------------------------------------------------------- | ------------------ |
| What it removes       | Rows (all or filtered) | All rows                                                                   | The whole table    |
| `WHERE` allowed       | Yes                    | No                                                                         | No                 |
| Fires row triggers    | Yes                    | No                                                                         | No                 |
| Speed on large tables | Slow (row by row)      | Fast                                                                       | Fast               |
| Table structure kept  | Yes                    | Yes                                                                        | No                 |
| Can be rolled back    | Yes                    | Yes in PostgreSQL and SQL Server; no in MySQL and Oracle (implicit commit) | Same as `TRUNCATE` |

```sql
DELETE FROM orders WHERE status = 'cancelled';
TRUNCATE TABLE order_log;
DROP TABLE old_orders;
```

#### 43: What do IF EXISTS and IF NOT EXISTS do?

They prevent an error if the object already exists (or does not exist).

```sql
CREATE TABLE IF NOT EXISTS audit_log (id INT, msg TEXT);
DROP TABLE IF EXISTS temp_import;
```

PostgreSQL, MySQL and SQLite support both. SQL Server supports `DROP ... IF EXISTS` (since 2016) but not `CREATE TABLE IF NOT EXISTS`. Oracle added both in Oracle 23ai.

#### 44: How do you insert a row into a table?

```sql
INSERT INTO customers (id, name, email, country)
VALUES (1, 'Anna Smith', 'anna@example.com', 'UK');
```

Always list the column names. If you skip them, the insert depends on the column order and breaks when someone adds a column.

#### 45: How do you insert several rows at once?

```sql
INSERT INTO products (id, name, category, price)
VALUES
    (1, 'Keyboard', 'Accessories', 49.99),
    (2, 'Mouse',    'Accessories', 19.99),
    (3, 'Monitor',  'Displays',   199.00);
```

This is much faster than separate inserts because it means fewer round trips and less overhead per statement. Oracle supports this syntax from 23ai. Older Oracle versions use `INSERT ALL` or `INSERT ... SELECT ... UNION ALL`.

#### 46: How do you copy data from one table into another?

Use `INSERT ... SELECT`.

```sql
INSERT INTO customers_archive (id, name, email)
SELECT id, name, email
FROM customers
WHERE created_at < DATE '2020-01-01';
```

#### 47: How do you update data?

```sql
UPDATE employees
SET salary = salary * 1.05,
    department_id = 4
WHERE id = 17;
```

You can change many columns in one statement. The `WHERE` clause decides which rows are changed.

#### 48: How do you delete data?

```sql
DELETE FROM orders
WHERE status = 'cancelled'
  AND order_date < DATE '2024-01-01';
```

#### 49: What happens if you run UPDATE or DELETE without a WHERE clause?

Every row in the table is changed or deleted. This is a classic mistake. A few habits help:

- Run the same `WHERE` with a `SELECT` first to see what will be affected.
- Run the change inside a transaction so you can roll back.
- MySQL clients have a `--safe-updates` option that blocks updates and deletes without a key in `WHERE`.

```sql
BEGIN;
UPDATE employees SET salary = 0;   -- oops
ROLLBACK;
```

#### 50: What is a DEFAULT value?

A default is the value used when an insert doesn't give a value for that column.

```sql
CREATE TABLE orders (
    id         INT PRIMARY KEY,
    status     VARCHAR(20) DEFAULT 'new',
    created_at TIMESTAMP   DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO orders (id) VALUES (1);  -- status = 'new'
```

Note that if you explicitly insert `NULL`, the column gets `NULL`, not the default. Use the `DEFAULT` keyword to ask for the default: `VALUES (2, DEFAULT, DEFAULT)`.

#### 51: How do you create a new table from the result of a query?

```sql
-- Standard, PostgreSQL, MySQL, Oracle, SQLite
CREATE TABLE high_earners AS
SELECT id, first_name, salary
FROM employees
WHERE salary > 100000;

-- SQL Server
SELECT id, first_name, salary
INTO high_earners
FROM employees
WHERE salary > 100000;
```

The new table gets the columns and data, but usually not the primary key, indexes or other constraints.

#### 52: What is an identity (auto-increment) column?

It's a column that gets an automatically increasing number for each new row. The standard syntax is `GENERATED ... AS IDENTITY`, which works in PostgreSQL, Oracle and DB2.

```sql
-- Standard (PostgreSQL, Oracle)
CREATE TABLE tickets (
    id    BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title TEXT
);

-- MySQL
CREATE TABLE tickets (id BIGINT AUTO_INCREMENT PRIMARY KEY, title TEXT);

-- SQL Server
CREATE TABLE tickets (id BIGINT IDENTITY(1,1) PRIMARY KEY, title NVARCHAR(MAX));
```

In PostgreSQL, the older `SERIAL` type still works, but identity columns are now the recommended way. Identity values can have gaps (after rollbacks or restarts), so don't rely on them being continuous.

#### 53: What is a temporary table?

A temporary table exists only for the current session (or transaction) and is dropped automatically. Other sessions can't see it.

```sql
-- PostgreSQL, MySQL
CREATE TEMPORARY TABLE tmp_totals AS
SELECT customer_id, SUM(total) AS total
FROM orders
GROUP BY customer_id;

-- SQL Server: local temp tables start with #
CREATE TABLE #tmp_totals (customer_id INT, total DECIMAL(12,2));
```

#### 54: What is a generated (computed) column?

A generated column gets its value from an expression on other columns in the same row. You can't write to it directly.

```sql
CREATE TABLE order_items (
    order_id   INT,
    product_id INT,
    quantity   INT,
    unit_price DECIMAL(10, 2),
    line_total DECIMAL(12, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED
);
```

- `STORED` columns are computed on write and saved on disk.
- `VIRTUAL` columns are computed when read.

MySQL supports both. PostgreSQL supported only `STORED` until PostgreSQL 18, which added `VIRTUAL` and made it the default. SQL Server calls them computed columns, with `PERSISTED` for the stored kind.

#### 55: How do you create an empty copy of a table's structure?

```sql
-- PostgreSQL (copies columns, and with INCLUDING ALL also defaults, constraints and indexes)
CREATE TABLE customers_copy (LIKE customers INCLUDING ALL);

-- MySQL (copies columns and indexes)
CREATE TABLE customers_copy LIKE customers;

-- Works almost everywhere, columns only
CREATE TABLE customers_copy AS SELECT * FROM customers WHERE 1 = 0;
```

### Constraints and Keys

#### 56: What is a constraint?

A constraint is a rule on a column or table that the database enforces. If an insert or update breaks the rule, the statement fails. The common ones are `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`, `CHECK` and `DEFAULT` (though `DEFAULT` sets a value rather than blocking anything).

Constraints keep bad data out no matter which application writes to the database.

#### 57: What is a primary key?

A primary key is a column, or set of columns, that uniquely identifies each row. Its values must be unique and can't be `NULL`. Each table can have only one primary key.

```sql
CREATE TABLE departments (
    id   INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

Most databases create a unique index for the primary key automatically. In SQL Server and MySQL (InnoDB), the primary key is also the clustered index by default, which means the table data is stored in primary key order.

#### 58: Can a primary key contain NULL? Can a table have two primary keys?

No to both. Primary key columns are always `NOT NULL`. A table has at most one primary key, but that key can include several columns (a composite key). If you need other unique columns, use `UNIQUE` constraints.

A table without a primary key is allowed, but it's almost always a bad idea.

#### 59: What is a composite key?

A key made of two or more columns. The combination must be unique, but each column alone can repeat.

```sql
CREATE TABLE order_items (
    order_id   INT,
    product_id INT,
    quantity   INT,
    PRIMARY KEY (order_id, product_id)
);
```

Here one order can have many products and one product can appear in many orders, but the same product can appear only once per order.

#### 60: What is a foreign key?

A foreign key is a column that refers to the primary key (or a unique key) of another table. It makes sure you can't point to a row that doesn't exist.

```sql
CREATE TABLE orders (
    id          INT PRIMARY KEY,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

Now inserting an order with `customer_id = 999` fails if no customer 999 exists. Deleting a customer who has orders also fails, unless you set a referential action like `ON DELETE CASCADE`.

#### 61: What is a UNIQUE constraint?

It makes sure no two rows have the same value in a column (or the same combination in several columns).

```sql
ALTER TABLE customers ADD CONSTRAINT uq_customers_email UNIQUE (email);
```

By default, `NULL` values don't count as duplicates, so most databases allow many `NULL`s in a unique column. SQL Server is the exception: it allows only one `NULL` in a unique constraint.

#### 62: What is the difference between a primary key and a unique key?

|                      | Primary key                        | Unique key                   |
| -------------------- | ---------------------------------- | ---------------------------- |
| How many per table   | One                                | Many                         |
| Allows NULL          | No                                 | Yes                          |
| Purpose              | Main identity of the row           | Extra rule for other columns |
| Clustered by default | Yes in SQL Server and MySQL InnoDB | No                           |

Both can be targets of a foreign key.

#### 63: What is a NOT NULL constraint?

It stops a column from holding `NULL`.

```sql
CREATE TABLE users (
    id    INT PRIMARY KEY,
    email VARCHAR(255) NOT NULL
);
```

Make columns `NOT NULL` unless you have a real reason to allow missing values. It makes queries simpler and helps the optimizer.

#### 64: What is a CHECK constraint?

A rule written as a condition that each row must pass.

```sql
CREATE TABLE products (
    id    INT PRIMARY KEY,
    price DECIMAL(10, 2) CHECK (price >= 0),
    stock INT,
    CONSTRAINT chk_stock CHECK (stock >= 0)
);
```

A check passes if the condition is `TRUE` or `UNKNOWN`. So `CHECK (price >= 0)` still allows `NULL`. MySQL ignored `CHECK` constraints before 8.0.16, so older MySQL databases may have them defined but not enforced.

#### 65: What does ON DELETE CASCADE do?

When the parent row is deleted, the child rows that point to it are deleted too.

```sql
CREATE TABLE order_items (
    order_id   INT REFERENCES orders(id) ON DELETE CASCADE,
    product_id INT REFERENCES products(id),
    quantity   INT
);

DELETE FROM orders WHERE id = 10;  -- also deletes its order_items
```

It's handy for data that has no meaning without its parent, like order lines. Be careful using it for important data, since one delete can remove a lot of rows across several tables.

#### 66: What other actions can a foreign key take on delete or update?

- `NO ACTION` (default): fail if child rows exist. The check happens at the end of the statement, and can be deferred in some databases.
- `RESTRICT`: fail right away if child rows exist.
- `CASCADE`: delete or update the child rows too.
- `SET NULL`: set the foreign key in child rows to `NULL`.
- `SET DEFAULT`: set it to the column's default value.

```sql
FOREIGN KEY (manager_id) REFERENCES employees(id) ON DELETE SET NULL
```

`ON UPDATE CASCADE` is also possible, but primary keys rarely change, so it's used less.

#### 67: What is the difference between a natural key and a surrogate key?

- A **natural key** comes from the real data, like an email, ISBN or tax number.
- A **surrogate key** has no meaning outside the database, like an identity number or UUID.

Surrogate keys are usually preferred as primary keys because they never change and are small. Natural keys can change (people change emails) and may be long. A common approach is to use a surrogate primary key and add a `UNIQUE` constraint on the natural key.

#### 68: What are super keys, candidate keys and alternate keys?

- **Super key**: any set of columns that uniquely identifies a row. `(id, email)` is a super key even though `id` alone is enough.
- **Candidate key**: a minimal super key. You can't remove any column and still keep it unique. Both `id` and `email` could be candidate keys.
- **Primary key**: the candidate key you pick as the main one.
- **Alternate key**: a candidate key that wasn't picked as the primary key. Usually enforced with `UNIQUE`.

#### 69: How do you add a constraint to a table that already exists?

```sql
ALTER TABLE employees
    ADD CONSTRAINT fk_employees_department
    FOREIGN KEY (department_id) REFERENCES departments(id);

ALTER TABLE employees
    ADD CONSTRAINT chk_salary_positive CHECK (salary > 0);
```

If existing rows break the rule, the statement fails. PostgreSQL lets you add the constraint as `NOT VALID` so it applies only to new rows, then check old rows later with `VALIDATE CONSTRAINT`.

#### 70: Why should you give constraints names?

If you don't, the database makes up a name like `employees_department_id_fkey` or `FK__employees__3A81B327`. Named constraints give clearer error messages and are easier to drop or change later.

```sql
CONSTRAINT pk_orders PRIMARY KEY (id),
CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers(id)
```

### Selecting and Filtering Data

#### 71: How do you select all columns, and why is SELECT \* often discouraged?

```sql
SELECT * FROM customers;
```

`SELECT *` is fine for a quick look. In application code it's better to list columns because:

- It reads less data and sends less over the network.
- The database may be able to answer from an index alone if you only ask for indexed columns.
- Your code won't break or change silently when someone adds, removes or reorders columns.

#### 72: How do you select specific columns?

```sql
SELECT first_name, last_name, salary
FROM employees;
```

#### 73: What does DISTINCT do?

It removes duplicate rows from the result.

```sql
SELECT DISTINCT country FROM customers;

SELECT DISTINCT country, city FROM customers;  -- unique combinations
```

`DISTINCT` applies to the whole row, not to one column. Two rows count as duplicates only if every selected column matches. For `DISTINCT`, `NULL` values are treated as equal to each other.

#### 74: What is the WHERE clause?

It filters rows. Only rows where the condition is `TRUE` are kept. Rows where it's `FALSE` or `UNKNOWN` are dropped.

```sql
SELECT * FROM orders
WHERE status = 'shipped'
  AND total > 100;
```

#### 75: What comparison operators does SQL have?

`=`, `<>` (not equal), `<`, `>`, `<=`, `>=`. Most databases also accept `!=`, but `<>` is the standard form.

```sql
SELECT * FROM products WHERE category <> 'Accessories';
```

#### 76: How do AND, OR and NOT work together?

`NOT` is evaluated first, then `AND`, then `OR`. Use parentheses to make your meaning clear.

```sql
-- Probably wrong: returns all UK customers plus German customers created after 2025
SELECT * FROM customers
WHERE country = 'UK' OR country = 'DE' AND created_at > '2025-01-01';

-- What was meant:
SELECT * FROM customers
WHERE (country = 'UK' OR country = 'DE') AND created_at > '2025-01-01';
```

#### 77: How does BETWEEN work?

`BETWEEN a AND b` includes both ends. It's the same as `>= a AND <= b`.

```sql
SELECT * FROM products WHERE price BETWEEN 10 AND 50;
```

Be careful with timestamps. `order_time BETWEEN '2026-01-01' AND '2026-01-31'` misses everything on January 31 after midnight. For time ranges, use a half-open range:

```sql
WHERE order_time >= '2026-01-01' AND order_time < '2026-02-01'
```

#### 78: How does the IN operator work?

It checks if a value matches any value in a list.

```sql
SELECT * FROM customers WHERE country IN ('UK', 'DE', 'FR');
```

It's a shorter way to write several `OR` conditions. The list can also be a subquery:

```sql
SELECT * FROM customers
WHERE id IN (SELECT customer_id FROM orders WHERE total > 1000);
```

#### 79: How does LIKE work?

`LIKE` matches text against a pattern:

- `%` matches any number of characters (including none)
- `_` matches exactly one character

```sql
SELECT * FROM customers WHERE name LIKE 'An%';     -- starts with An
SELECT * FROM customers WHERE email LIKE '%@gmail.com';
SELECT * FROM products WHERE name LIKE '_ouse';    -- Mouse, House...
```

A pattern that starts with `%` can't use a normal B-tree index, so it's slow on large tables.

#### 80: How do you search for a literal % or \_ with LIKE?

Use an escape character.

```sql
SELECT * FROM products WHERE name LIKE '%50\%%' ESCAPE '\';  -- contains "50%"
```

`ESCAPE` is standard. PostgreSQL and MySQL use backslash as the default escape character even without the `ESCAPE` clause. SQL Server also lets you use brackets: `LIKE '%50[%]%'`.

#### 81: How do you do a case-insensitive search?

There are a few ways:

```sql
-- Works everywhere
SELECT * FROM customers WHERE LOWER(name) = LOWER('anna smith');

-- PostgreSQL
SELECT * FROM customers WHERE name ILIKE 'anna%';
```

In MySQL and SQL Server, the default collations are usually case-insensitive already, so a plain `=` or `LIKE` ignores case. In PostgreSQL you can also use a case-insensitive collation or the `citext` extension. If you search with `LOWER(name)` often, create an index on `LOWER(name)`.

#### 82: Why does `WHERE column = NULL` return no rows?

Because comparing anything with `NULL` gives `UNKNOWN`, and `WHERE` only keeps rows where the condition is `TRUE`. Even `NULL = NULL` is `UNKNOWN`.

```sql
-- Wrong: returns nothing
SELECT * FROM employees WHERE manager_id = NULL;

-- Right
SELECT * FROM employees WHERE manager_id IS NULL;
```

#### 83: What is IS DISTINCT FROM?

It compares two values and treats `NULL`s as equal to each other. It always returns `TRUE` or `FALSE`, never `UNKNOWN`.

```sql
SELECT * FROM employees
WHERE manager_id IS DISTINCT FROM 5;   -- includes rows where manager_id is NULL
```

| a    | b    | `a <> b` | `a IS DISTINCT FROM b` |
| ---- | ---- | -------- | ---------------------- |
| 1    | 2    | TRUE     | TRUE                   |
| 1    | NULL | UNKNOWN  | TRUE                   |
| NULL | NULL | UNKNOWN  | FALSE                  |

Supported in PostgreSQL, SQL Server 2022+, DuckDB and others. MySQL has the `<=>` operator for "null-safe equal", and SQLite has `IS` / `IS NOT`.

#### 84: Can you use expressions in the SELECT list?

Yes. You can use math, functions and string operations.

```sql
SELECT first_name || ' ' || last_name AS full_name,
       salary * 12                    AS yearly_salary,
       EXTRACT(YEAR FROM hire_date)   AS hire_year
FROM employees;
```

#### 85: What is a CASE expression?

`CASE` returns different values based on conditions, like if/else.

```sql
SELECT name,
       price,
       CASE
           WHEN price < 20  THEN 'cheap'
           WHEN price < 100 THEN 'normal'
           ELSE 'expensive'
       END AS price_group
FROM products;
```

Conditions are checked in order and the first `TRUE` one wins. If nothing matches and there's no `ELSE`, the result is `NULL`. You can use `CASE` almost anywhere an expression is allowed: `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, inside aggregates.

#### 86: What is the difference between a simple CASE and a searched CASE?

A simple `CASE` compares one expression to several values:

```sql
CASE status
    WHEN 'new'     THEN 1
    WHEN 'shipped' THEN 2
    ELSE 0
END
```

A searched `CASE` checks a separate condition in each branch:

```sql
CASE
    WHEN total > 1000 AND status = 'new' THEN 'priority'
    WHEN total > 1000 THEN 'large'
    ELSE 'normal'
END
```

A simple `CASE` can't match `NULL`, because `WHEN NULL` uses `=` internally. Use the searched form with `IS NULL` for that.

#### 87: Can you use a column alias in the WHERE clause?

No, in most databases. `WHERE` runs before `SELECT`, so the alias doesn't exist yet.

```sql
-- Error
SELECT salary * 12 AS yearly FROM employees WHERE yearly > 100000;

-- Repeat the expression
SELECT salary * 12 AS yearly FROM employees WHERE salary * 12 > 100000;

-- Or use a subquery / CTE
SELECT * FROM (SELECT salary * 12 AS yearly FROM employees) t WHERE yearly > 100000;
```

SQLite and a few others are more relaxed, but don't count on it. Aliases do work in `ORDER BY`. MySQL and PostgreSQL also allow them in `GROUP BY`, and Oracle 23ai added this too.

#### 88: Can you ORDER BY a column that is not in the SELECT list?

Yes, in most cases.

```sql
SELECT first_name, last_name FROM employees ORDER BY hire_date;
```

The exception is `SELECT DISTINCT`. There, the `ORDER BY` columns must appear in the select list, because after removing duplicates there may be several possible values to sort by.

#### 89: Can you run a SELECT without a FROM clause?

Yes, in PostgreSQL, MySQL, SQL Server and SQLite. It's useful for testing expressions.

```sql
SELECT 2 + 2, CURRENT_DATE, UPPER('hello');
```

Oracle used to require the dummy table `DUAL` (`SELECT 1 FROM DUAL`). Oracle 23ai allows `SELECT` without `FROM`.

#### 90: How do you join strings together?

The standard operator is `||`.

```sql
SELECT first_name || ' ' || last_name AS full_name FROM employees;
```

- PostgreSQL, Oracle, SQLite: `||` works.
- MySQL: `||` means logical OR by default, so use `CONCAT(first_name, ' ', last_name)`.
- SQL Server: traditionally uses `+`. SQL Server 2025 also supports `||`. `CONCAT()` works in all versions since 2012.

Watch out for `NULL`s. `||` and `+` return `NULL` if any part is `NULL` (except in Oracle, which treats `NULL` as an empty string). `CONCAT()` skips `NULL`s in PostgreSQL and SQL Server, but in MySQL it returns `NULL` if any argument is `NULL`. `CONCAT_WS(', ', a, b, c)` adds a separator and skips `NULL`s in PostgreSQL, MySQL and SQL Server.

#### 91: What is the difference between WHERE and HAVING?

`WHERE` filters individual rows before grouping. `HAVING` filters groups after `GROUP BY` and can use aggregate functions.

```sql
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
WHERE hire_date >= DATE '2020-01-01'   -- filter rows
GROUP BY department_id
HAVING AVG(salary) > 60000;            -- filter groups
```

If a condition doesn't use an aggregate, put it in `WHERE`. It removes rows earlier, so there's less to group.

#### 92: What is three-valued logic in SQL?

SQL conditions can be `TRUE`, `FALSE` or `UNKNOWN`. `UNKNOWN` comes from comparisons with `NULL`.

- `TRUE AND UNKNOWN` = `UNKNOWN`
- `FALSE AND UNKNOWN` = `FALSE`
- `TRUE OR UNKNOWN` = `TRUE`
- `FALSE OR UNKNOWN` = `UNKNOWN`
- `NOT UNKNOWN` = `UNKNOWN`

`WHERE` and `HAVING` keep only `TRUE` rows. `CHECK` constraints reject only `FALSE`, so `UNKNOWN` passes.

#### 93: Why can NOT IN return no rows when the list contains NULL?

`x NOT IN (1, 2, NULL)` means `x <> 1 AND x <> 2 AND x <> NULL`. The last part is always `UNKNOWN`, so the whole condition can never be `TRUE`.

```sql
-- If any order has customer_id = NULL, this returns nothing
SELECT * FROM customers
WHERE id NOT IN (SELECT customer_id FROM orders);

-- Safe version
SELECT * FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

#### 94: How do you filter rows by date?

Use date literals and half-open ranges.

```sql
-- Orders from March 2026
SELECT * FROM orders
WHERE order_date >= DATE '2026-03-01'
  AND order_date <  DATE '2026-04-01';
```

Avoid wrapping the column in a function, like `WHERE YEAR(order_date) = 2026`. It works, but the database usually can't use an index on `order_date` that way.

#### 95: What is a table alias and why use it?

A table alias is a short name for a table in a query. It makes queries shorter and is required when you join a table to itself.

```sql
SELECT e.first_name, d.name
FROM employees e
JOIN departments d ON d.id = e.department_id;
```

Once you give a table an alias, use the alias everywhere in that query instead of the table name.

### Sorting and Limiting Results

#### 96: How do you sort query results?

Use `ORDER BY`.

```sql
SELECT name, price FROM products ORDER BY price;
```

#### 97: How do you sort by several columns and in different directions?

```sql
SELECT first_name, last_name, salary, department_id
FROM employees
ORDER BY department_id ASC, salary DESC, last_name;
```

Rows are sorted by the first column. Ties are broken by the second column, and so on. `ASC` is the default.

#### 98: Where do NULL values appear when sorting?

It depends on the database:

- PostgreSQL and Oracle: `NULL`s are treated as larger than any value, so they come last in `ASC` and first in `DESC`.
- MySQL, SQL Server and SQLite: `NULL`s are treated as smaller, so they come first in `ASC`.

You can control this with `NULLS FIRST` / `NULLS LAST` in PostgreSQL, Oracle and SQLite:

```sql
SELECT * FROM employees ORDER BY manager_id NULLS FIRST;
```

In MySQL and SQL Server, sort by an extra expression:

```sql
SELECT * FROM employees ORDER BY CASE WHEN manager_id IS NULL THEN 1 ELSE 0 END, manager_id;
```

#### 99: How do you return only the first N rows?

```sql
-- Standard SQL (PostgreSQL, Oracle 12c+, DB2)
SELECT * FROM products ORDER BY price DESC FETCH FIRST 5 ROWS ONLY;

-- PostgreSQL, MySQL, SQLite
SELECT * FROM products ORDER BY price DESC LIMIT 5;

-- SQL Server
SELECT TOP (5) * FROM products ORDER BY price DESC;
```

Without `ORDER BY`, "first 5" just means any 5 rows.

#### 100: How do you skip rows for pagination?

```sql
-- Standard (also SQL Server 2012+, which requires ORDER BY)
SELECT * FROM products
ORDER BY id
OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;

-- PostgreSQL, MySQL, SQLite
SELECT * FROM products ORDER BY id LIMIT 10 OFFSET 20;
```

This returns rows 21 to 30. Large offsets are slow because the database still reads and throws away all the skipped rows. For deep pagination, keyset pagination is better (see question 312).

#### 101: What does FETCH FIRST ... WITH TIES do?

It returns the first N rows plus any rows that tie with the last one on the `ORDER BY` values.

```sql
SELECT name, price
FROM products
ORDER BY price DESC
FETCH FIRST 3 ROWS WITH TIES;
```

If the 3rd and 4th most expensive products have the same price, you get 4 rows. Supported in PostgreSQL 13+ and Oracle. SQL Server has `TOP (3) WITH TIES`.

#### 102: Can you sort by column position? Should you?

Yes, `ORDER BY 2` sorts by the second column in the select list.

```sql
SELECT name, price FROM products ORDER BY 2 DESC;
```

It's handy for quick queries, but avoid it in code you keep. If someone changes the select list, the sort quietly changes too.

#### 103: Is the order of rows guaranteed without ORDER BY?

No. Without `ORDER BY`, the database can return rows in any order, and the order can change between runs, after an index is added, after a version upgrade, or when the query runs in parallel. If order matters, always use `ORDER BY`. Also, an `ORDER BY` inside a subquery or view does not guarantee the order of the outer query's result.

#### 104: How do you find the row with the highest value in a column?

```sql
-- The highest salary value
SELECT MAX(salary) FROM employees;

-- The employee(s) with the highest salary
SELECT *
FROM employees
ORDER BY salary DESC
FETCH FIRST 1 ROWS WITH TIES;

-- Another way
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```

#### 105: How do you pick random rows?

```sql
-- PostgreSQL, SQLite
SELECT * FROM products ORDER BY RANDOM() LIMIT 5;

-- MySQL
SELECT * FROM products ORDER BY RAND() LIMIT 5;

-- SQL Server
SELECT TOP (5) * FROM products ORDER BY NEWID();
```

These sort the whole table, which is slow on big tables. For a rough sample of a large table, use `TABLESAMPLE`:

```sql
SELECT * FROM orders TABLESAMPLE SYSTEM (1);  -- about 1% of the table
```

### Basic Functions

#### 106: What is the difference between scalar functions and aggregate functions?

A scalar function works on one value and returns one value for each row, like `UPPER(name)` or `ROUND(price, 0)`. An aggregate function works on a group of rows and returns one value for the whole group, like `SUM(total)` or `COUNT(*)`.

```sql
SELECT UPPER(name) FROM customers;      -- one result per row
SELECT COUNT(*)    FROM customers;      -- one result for the table
```

#### 107: How do you change text to upper or lower case?

```sql
SELECT UPPER(name), LOWER(email) FROM customers;
```

`INITCAP()` in PostgreSQL and Oracle capitalizes the first letter of each word.

#### 108: How do you get the length of a string?

```sql
-- Standard, PostgreSQL, MySQL
SELECT CHAR_LENGTH(name) FROM customers;

-- PostgreSQL, MySQL, Oracle, SQLite
SELECT LENGTH(name) FROM customers;

-- SQL Server
SELECT LEN(name) FROM customers;
```

In MySQL, `LENGTH()` returns bytes and `CHAR_LENGTH()` returns characters, so they differ for non-ASCII text like `'é'`. In SQL Server, `LEN()` ignores trailing spaces, and `DATALENGTH()` returns bytes.

#### 109: How do you get part of a string?

```sql
-- Standard
SELECT SUBSTRING(phone FROM 1 FOR 3) FROM customers;

-- Common form (PostgreSQL, MySQL, SQL Server)
SELECT SUBSTRING(phone, 1, 3) FROM customers;

-- Oracle, SQLite
SELECT SUBSTR(phone, 1, 3) FROM customers;
```

Positions start at 1, not 0. `LEFT(s, n)` and `RIGHT(s, n)` are also available in PostgreSQL, MySQL and SQL Server.

#### 110: How do you remove spaces from the start or end of a string?

```sql
SELECT TRIM('   hello   ');              -- 'hello'
SELECT LTRIM('   hello');                -- 'hello'
SELECT RTRIM('hello   ');                -- 'hello'
SELECT TRIM(BOTH 'x' FROM 'xxhixx');     -- 'hi'
SELECT TRIM(LEADING '0' FROM '000123');  -- '123'
```

SQL:2023 added `LTRIM`, `RTRIM` and `BTRIM` to the standard with an optional second argument for the characters to remove, for example `LTRIM('000123', '0')`. SQL Server 2022 also added these extra arguments.

#### 111: How do you replace part of a string?

```sql
SELECT REPLACE(phone, '-', '') FROM customers;
-- '555-123-4567' becomes '5551234567'
```

`REPLACE` swaps every match. For patterns, use regular expression functions like `REGEXP_REPLACE`.

#### 112: How do you pad a string to a fixed length?

Use `LPAD` and `RPAD`. They were added to the standard in SQL:2023 and have existed for a long time in PostgreSQL, MySQL and Oracle.

```sql
SELECT LPAD(CAST(id AS VARCHAR(10)), 6, '0') FROM orders;  -- 42 becomes '000042'
SELECT RPAD('abc', 6, '.');                                 -- 'abc...'
```

SQL Server doesn't have them. A common workaround is `RIGHT('000000' + CAST(id AS VARCHAR(10)), 6)`.

#### 113: How do you find the position of a substring?

```sql
-- Standard, PostgreSQL, MySQL
SELECT POSITION('@' IN email) FROM customers;

-- SQL Server
SELECT CHARINDEX('@', email) FROM customers;

-- Oracle, MySQL
SELECT INSTR(email, '@') FROM customers;
```

All return 0 if the substring is not found.

#### 114: How do ROUND, CEILING, FLOOR and TRUNC differ?

```sql
SELECT ROUND(12.567, 2);   -- 12.57
SELECT ROUND(12.5);        -- 13
SELECT CEILING(12.1);      -- 13  (CEIL in PostgreSQL, Oracle, MySQL)
SELECT FLOOR(12.9);        -- 12
SELECT TRUNC(12.567, 1);   -- 12.5 (TRUNCATE in MySQL)
SELECT FLOOR(-12.5);       -- -13
SELECT TRUNC(-12.5);       -- -12
```

`FLOOR` goes down, `CEILING` goes up, `TRUNC` cuts toward zero. In SQL Server, use `ROUND(x, 1, 1)` to truncate.

#### 115: What common math functions does SQL have?

```sql
SELECT ABS(-5);         -- 5
SELECT MOD(17, 5);      -- 2  (SQL Server uses 17 % 5)
SELECT POWER(2, 10);    -- 1024
SELECT SQRT(16);        -- 4
SELECT SIGN(-3);        -- -1
SELECT EXP(1), LN(10), LOG10(100);
```

#### 116: Why does 5 / 2 return 2 in some databases?

When both numbers are integers, PostgreSQL, SQL Server and SQLite do integer division and drop the decimal part. MySQL returns `2.5000` and Oracle returns `2.5`.

```sql
SELECT 5 / 2;          -- 2 in PostgreSQL / SQL Server
SELECT 5 / 2.0;        -- 2.5
SELECT CAST(5 AS DECIMAL(10,2)) / 2;  -- 2.5
```

This often causes bugs when calculating percentages, such as `COUNT(...) / COUNT(*)` returning 0. Multiply by `1.0` or cast first.

#### 117: How do you get the current date and time?

```sql
SELECT CURRENT_DATE;       -- standard
SELECT CURRENT_TIMESTAMP;  -- standard
SELECT NOW();              -- PostgreSQL, MySQL
SELECT GETDATE();          -- SQL Server
SELECT SYSDATE FROM DUAL;  -- Oracle
```

SQL Server 2025 added `CURRENT_DATE`. In PostgreSQL, `NOW()` and `CURRENT_TIMESTAMP` return the start time of the current transaction, so they don't change during the transaction. Use `clock_timestamp()` if you need the actual current time.

#### 118: How do you get the year, month or day from a date?

```sql
-- Standard, PostgreSQL, MySQL, Oracle
SELECT EXTRACT(YEAR FROM hire_date), EXTRACT(MONTH FROM hire_date)
FROM employees;

-- SQL Server
SELECT YEAR(hire_date), MONTH(hire_date), DATEPART(quarter, hire_date)
FROM employees;
```

MySQL also has `YEAR()`, `MONTH()` and `DAY()`.

#### 119: How do you add days or months to a date?

```sql
-- Standard, PostgreSQL, Oracle
SELECT order_date + INTERVAL '7' DAY FROM orders;

-- PostgreSQL
SELECT order_date + INTERVAL '1 month' FROM orders;

-- MySQL
SELECT DATE_ADD(order_date, INTERVAL 1 MONTH) FROM orders;

-- SQL Server
SELECT DATEADD(month, 1, order_date) FROM orders;
```

Watch out for month ends. Adding one month to January 31 gives February 28 (or 29) in most databases.

#### 120: What does COALESCE do?

It returns the first argument that is not `NULL`.

```sql
SELECT name, COALESCE(phone, email, 'no contact') AS contact
FROM customers;
```

`COALESCE` is standard and works everywhere. It takes any number of arguments.

#### 121: What does NULLIF do?

`NULLIF(a, b)` returns `NULL` if `a = b`, otherwise it returns `a`.

```sql
SELECT NULLIF(status, '') FROM orders;  -- turns empty strings into NULL
```

Its most common use is avoiding division by zero (see question 125).

#### 122: What do GREATEST and LEAST do?

They return the largest or smallest value from a list of arguments in the same row. This is different from `MAX` and `MIN`, which work across rows.

```sql
SELECT GREATEST(10, 25, 7);  -- 25
SELECT LEAST(price, discount_price) FROM products;
```

They became part of the standard in SQL:2023. PostgreSQL, MySQL and Oracle have had them for years, and SQL Server added them in 2022. In PostgreSQL they ignore `NULL`s. In MySQL and Oracle, any `NULL` argument makes the result `NULL`.

#### 123: How do you format a date as text?

```sql
-- PostgreSQL, Oracle
SELECT TO_CHAR(order_date, 'YYYY-MM-DD') FROM orders;

-- MySQL
SELECT DATE_FORMAT(order_date, '%Y-%m-%d') FROM orders;

-- SQL Server
SELECT FORMAT(order_date, 'yyyy-MM-dd') FROM orders;     -- slow on many rows
SELECT CONVERT(VARCHAR(10), order_date, 23) FROM orders; -- faster
```

It's usually better to return dates as dates and format them in the application.

#### 124: What is the difference between deterministic and nondeterministic functions?

A deterministic function always returns the same result for the same input, like `UPPER('a')` or `ABS(-3)`. A nondeterministic function can return different results, like `RANDOM()`, `NOW()` or `NEWID()`.

This matters because many databases only let you use deterministic (immutable) functions in indexes and generated columns.

#### 125: How do you avoid a division by zero error?

Use `NULLIF` on the divisor. If it's zero, it becomes `NULL` and the division returns `NULL` instead of an error.

```sql
SELECT product_id,
       revenue / NULLIF(units_sold, 0) AS price_per_unit
FROM sales;

-- Show 0 instead of NULL
SELECT COALESCE(revenue / NULLIF(units_sold, 0), 0) FROM sales;
```

MySQL returns `NULL` for division by zero by default (with a warning), but other databases raise an error.

### Basic Aggregation

#### 126: What are aggregate functions?

Functions that take many rows and return one value. The basic ones are:

- `COUNT` - number of rows or values
- `SUM` - total
- `AVG` - average
- `MIN` - smallest value
- `MAX` - largest value

```sql
SELECT COUNT(*), SUM(total), AVG(total), MIN(order_date), MAX(order_date)
FROM orders;
```

All of them, except `COUNT(*)`, ignore `NULL` values.

#### 127: What is the difference between COUNT(\*), COUNT(column) and COUNT(DISTINCT column)?

- `COUNT(*)` counts all rows.
- `COUNT(column)` counts rows where that column is not `NULL`.
- `COUNT(DISTINCT column)` counts unique non-`NULL` values.

```sql
SELECT COUNT(*)                   AS all_employees,
       COUNT(manager_id)          AS with_manager,
       COUNT(DISTINCT department_id) AS departments_used
FROM employees;
```

`COUNT(1)` is the same as `COUNT(*)`. There's no speed difference in modern databases.

#### 128: How do SUM and AVG treat NULL values?

They skip them. This affects `AVG` in a way people often miss:

```sql
-- bonus values: 100, 200, NULL
SELECT AVG(bonus) FROM t;                -- 150, divides by 2
SELECT AVG(COALESCE(bonus, 0)) FROM t;   -- 100, divides by 3
```

Decide whether a missing value should count as zero or be left out, and write the query to match.

#### 129: Can MIN and MAX work on text and dates?

Yes. On dates they return the earliest and latest. On text they use alphabetical order based on the collation.

```sql
SELECT MIN(hire_date), MAX(hire_date), MIN(last_name), MAX(last_name)
FROM employees;
```

#### 130: What does GROUP BY do?

It puts rows with the same values into groups, so you can run aggregates on each group.

```sql
SELECT department_id, COUNT(*) AS employees, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;
```

You get one row per department. All rows with `NULL` in the grouping column end up in one group.

#### 131: Why do you get an error like "column must appear in the GROUP BY clause"?

Every column in `SELECT` must either be in `GROUP BY` or be inside an aggregate. Otherwise the database doesn't know which value to show for the group.

```sql
-- Error: which first_name should be shown for each department?
SELECT department_id, first_name, COUNT(*) FROM employees GROUP BY department_id;
```

There is one exception from the standard: if you group by a table's primary key, you can select other columns from that table, because they are determined by the key. PostgreSQL and MySQL 5.7+ support this.

```sql
SELECT d.id, d.name, COUNT(e.id)
FROM departments d
LEFT JOIN employees e ON e.department_id = d.id
GROUP BY d.id;   -- d.name is allowed because d.id is the primary key
```

#### 132: What does HAVING do?

It filters groups after aggregation.

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 5;
```

#### 133: Can you group by more than one column?

Yes. A group is made for each unique combination.

```sql
SELECT department_id, EXTRACT(YEAR FROM hire_date) AS hire_year, COUNT(*)
FROM employees
GROUP BY department_id, EXTRACT(YEAR FROM hire_date)
ORDER BY department_id, hire_year;
```

#### 134: What do aggregate functions return on an empty table?

`COUNT` returns 0. `SUM`, `AVG`, `MIN` and `MAX` return `NULL`.

```sql
SELECT COUNT(*), SUM(total) FROM orders WHERE 1 = 0;
-- 0, NULL

SELECT COALESCE(SUM(total), 0) FROM orders WHERE 1 = 0;
-- 0
```

Also, without `GROUP BY`, an aggregate query always returns exactly one row, even on an empty table. With `GROUP BY`, an empty table gives no rows.

#### 135: How do you count only the rows that match a condition?

```sql
-- Standard FILTER clause (PostgreSQL, SQLite, DuckDB)
SELECT COUNT(*) FILTER (WHERE status = 'shipped')   AS shipped,
       COUNT(*) FILTER (WHERE status = 'cancelled') AS cancelled
FROM orders;

-- Works everywhere
SELECT SUM(CASE WHEN status = 'shipped'   THEN 1 ELSE 0 END) AS shipped,
       SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled
FROM orders;
```

`COUNT(CASE WHEN status = 'shipped' THEN 1 END)` also works, because `COUNT` skips the `NULL` returned when the condition is false.

#### 136: What is ANY_VALUE?

An aggregate that returns any one value from the group. It's useful when you know all values in the group are the same, or you don't care which one you get. It became standard in SQL:2023. PostgreSQL 16+, MySQL, BigQuery and Snowflake support it.

```sql
SELECT customer_id, ANY_VALUE(c.name) AS name, COUNT(*) AS orders
FROM orders o
JOIN customers c ON c.id = o.customer_id
GROUP BY customer_id;
```

#### 137: Can you put one aggregate inside another, like MAX(AVG(salary))?

Not in standard SQL. (Oracle allows it as an extension.) Use a subquery or CTE:

```sql
SELECT MAX(avg_salary)
FROM (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
) t;
```

### Join Basics

#### 138: What is a join?

A join combines rows from two or more tables based on a related column.

```sql
SELECT o.id, o.order_date, c.name
FROM orders o
JOIN customers c ON c.id = o.customer_id;
```

#### 139: What types of joins are there?

- `INNER JOIN` - only rows that match in both tables
- `LEFT [OUTER] JOIN` - all rows from the left table, plus matches from the right
- `RIGHT [OUTER] JOIN` - all rows from the right table, plus matches from the left
- `FULL [OUTER] JOIN` - all rows from both tables
- `CROSS JOIN` - every row of one table combined with every row of the other
- Self join - a table joined to itself (uses any join type)

#### 140: What does INNER JOIN return?

Only rows where the join condition is true in both tables. Rows with no match on either side are left out.

```sql
SELECT e.first_name, d.name AS department
FROM employees e
INNER JOIN departments d ON d.id = e.department_id;
```

Employees with no department (`department_id IS NULL`) don't appear. `JOIN` without a type means `INNER JOIN`.

#### 141: What does LEFT JOIN return?

All rows from the left table. When there's a matching row in the right table, its columns are filled in. When there's no match, the right side columns are `NULL`.

```sql
SELECT c.name, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id;
```

Customers with no orders appear once, with `order_id` as `NULL`.

#### 142: What does RIGHT JOIN return?

The mirror of `LEFT JOIN`: all rows from the right table plus matches from the left. `A RIGHT JOIN B` gives the same rows as `B LEFT JOIN A`. Most people just use `LEFT JOIN` and put the main table first, because it's easier to read.

#### 143: What does FULL OUTER JOIN return?

All rows from both tables. Where rows match, they are combined. Where they don't, the missing side is filled with `NULL`.

```sql
SELECT e.first_name, d.name
FROM employees e
FULL OUTER JOIN departments d ON d.id = e.department_id;
```

This shows employees without a department and departments without employees. MySQL doesn't support `FULL OUTER JOIN` (see question 165 for a workaround).

#### 144: What is a CROSS JOIN?

It returns every combination of rows from both tables (a Cartesian product). If one table has 10 rows and the other has 5, you get 50 rows.

```sql
SELECT s.size, c.color
FROM sizes s
CROSS JOIN colors c;
```

It's useful for generating combinations, like every product for every store, or every date for every user.

#### 145: What is a self join?

A table joined to itself. You need two different aliases.

```sql
-- Each employee with their manager's name
SELECT e.first_name AS employee, m.first_name AS manager
FROM employees e
LEFT JOIN employees m ON m.id = e.manager_id;
```

`LEFT JOIN` keeps the top boss, who has no manager.

#### 146: What is the difference between ON and USING?

`ON` takes any condition. `USING` is a shortcut when the columns have the same name in both tables.

```sql
-- Column names differ (orders.id vs order_items.order_id), so use ON
SELECT * FROM orders o JOIN order_items i ON i.order_id = o.id;

-- Both tables have a column named product_id, so USING works
SELECT * FROM order_items JOIN product_stock USING (product_id);
```

With `USING`, the join column appears only once in `SELECT *`. SQL Server doesn't support `USING`.

#### 147: What is a NATURAL JOIN and why is it risky?

`NATURAL JOIN` joins automatically on all columns with the same name in both tables. It's risky because if someone later adds a column with the same name to both tables (like `created_at` or `name`), the join condition changes without anyone noticing. It's better to always write the join condition.

```sql
SELECT * FROM orders NATURAL JOIN customers;  -- avoid this
```

#### 148: What happens to NULL values in join columns?

`NULL` never equals anything, including another `NULL`. So rows with `NULL` in the join column never match in an inner join. In a `LEFT JOIN`, the left row still shows up, but with no match.

If you really need `NULL`s to match each other, use `IS NOT DISTINCT FROM` in the join condition. This can be slower because some databases can't use an index for it.

#### 149: How do you join more than two tables?

Add one join after another. Each join connects a new table to the tables already in the query.

```sql
SELECT c.name, o.id AS order_id, p.name AS product, i.quantity
FROM customers c
JOIN orders o      ON o.customer_id = c.id
JOIN order_items i ON i.order_id = o.id
JOIN products p    ON p.id = i.product_id
WHERE o.order_date >= DATE '2026-01-01';
```

#### 150: What is the difference between the old comma join syntax and the JOIN syntax?

The old style lists tables with commas and puts the join condition in `WHERE`:

```sql
-- Old style
SELECT e.first_name, d.name
FROM employees e, departments d
WHERE e.department_id = d.id;

-- Explicit JOIN (SQL-92)
SELECT e.first_name, d.name
FROM employees e
JOIN departments d ON e.department_id = d.id;
```

For inner joins, both give the same result and usually the same plan. The `JOIN` syntax is preferred because it keeps join conditions apart from filters, makes it harder to forget a condition (which would create an accidental cross join), and is the only standard way to write outer joins. The old Oracle `(+)` and SQL Server `*=` outer join syntax should not be used.

---

## Moderate Questions (151-300)

### Joins in Depth

#### 151: In a LEFT JOIN, what is the difference between putting a condition in ON and putting it in WHERE?

A condition in `ON` decides which right-side rows match. Left rows are kept either way. A condition in `WHERE` runs after the join and can throw away left rows, which turns the `LEFT JOIN` into an inner join.

```sql
-- All customers, with only their 2026 orders (others get NULL)
SELECT c.name, o.id
FROM customers c
LEFT JOIN orders o
       ON o.customer_id = c.id
      AND o.order_date >= DATE '2026-01-01';

-- Only customers who have a 2026 order (behaves like INNER JOIN)
SELECT c.name, o.id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.order_date >= DATE '2026-01-01';
```

For inner joins it makes no difference to the result.

#### 152: How do you find rows in one table that have no match in another table?

This is called an anti-join. Two common ways:

```sql
-- NOT EXISTS (usually the best choice)
SELECT c.*
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.id
);

-- LEFT JOIN ... IS NULL
SELECT c.*
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;
```

Avoid `NOT IN` with a subquery unless the column is `NOT NULL` (see question 93). Most optimizers turn both of the forms above into the same anti-join plan.

#### 153: What is a semi-join?

A semi-join returns rows from the first table that have at least one match in the second table, without repeating rows when there are several matches. You write it with `EXISTS` or `IN`.

```sql
-- Customers who have placed at least one order (each customer once)
SELECT c.*
FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

A plain `JOIN` here would return a customer once per order.

#### 154: Why does a join sometimes return more rows than expected?

Because the join is one-to-many or many-to-many. If a customer has 5 orders, joining customers to orders gives 5 rows for that customer. Joining two child tables of the same parent multiplies rows: 5 orders times 3 addresses gives 15 rows per customer.

To fix it:

- Check the join keys. Are you joining on the full key?
- Aggregate each child table before joining.
- Use `EXISTS` if you only need to know if a match exists.

#### 155: How do you join on more than one column?

Combine the conditions with `AND`.

```sql
SELECT *
FROM shipments s
JOIN order_items i
  ON i.order_id   = s.order_id
 AND i.product_id = s.product_id;
```

#### 156: What is a non-equi join?

A join that uses something other than `=`, such as `BETWEEN`, `<` or `>`.

```sql
-- Find the salary grade of each employee
SELECT e.first_name, e.salary, g.grade
FROM employees e
JOIN salary_grades g
  ON e.salary BETWEEN g.min_salary AND g.max_salary;
```

Non-equi joins are common for date ranges, price bands and "find the price that was valid on the order date".

#### 157: How do you find employees who earn more than their managers?

Use a self join.

```sql
SELECT e.first_name AS employee, e.salary,
       m.first_name AS manager,  m.salary AS manager_salary
FROM employees e
JOIN employees m ON m.id = e.manager_id
WHERE e.salary > m.salary;
```

#### 158: What is a LATERAL join?

A `LATERAL` subquery can refer to columns from tables that come before it in the `FROM` clause. It runs once for each row of the left side, like a loop. It's very handy for "top N per row" problems.

```sql
-- The 3 most recent orders for each customer (PostgreSQL, MySQL 8.0.14+, Oracle)
SELECT c.name, recent.id, recent.order_date
FROM customers c
CROSS JOIN LATERAL (
    SELECT o.id, o.order_date
    FROM orders o
    WHERE o.customer_id = c.id
    ORDER BY o.order_date DESC
    FETCH FIRST 3 ROWS ONLY
) AS recent;
```

Use `LEFT JOIN LATERAL (...) ON TRUE` to keep customers with no orders. SQL Server uses `CROSS APPLY` and `OUTER APPLY` for the same thing.

#### 159: What is the difference between CROSS APPLY and OUTER APPLY in SQL Server?

`CROSS APPLY` works like an inner join with a lateral subquery: left rows with no result from the subquery are dropped. `OUTER APPLY` works like a left join: left rows are kept and get `NULL`s.

```sql
SELECT c.name, o.id
FROM customers c
OUTER APPLY (
    SELECT TOP (1) id
    FROM orders
    WHERE customer_id = c.id
    ORDER BY order_date DESC
) o;
```

#### 160: Why can SUM give a wrong total after a join, and how do you fix it?

When you join a parent to a child table, the parent's columns repeat for every child row. If you then sum a parent column, you count it several times.

```sql
-- Wrong: o.total is counted once per order item
SELECT o.customer_id, SUM(o.total)
FROM orders o
JOIN order_items i ON i.order_id = o.id
GROUP BY o.customer_id;
```

Fix it by aggregating before joining, or by not joining tables you don't need:

```sql
WITH item_counts AS (
    SELECT order_id, SUM(quantity) AS items
    FROM order_items
    GROUP BY order_id
)
SELECT o.customer_id, SUM(o.total) AS revenue, SUM(ic.items) AS items
FROM orders o
JOIN item_counts ic ON ic.order_id = o.id
GROUP BY o.customer_id;
```

#### 161: How do you find duplicate rows?

Group by the columns that should be unique and look for groups with more than one row.

```sql
SELECT email, COUNT(*) AS cnt
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;
```

To see the full duplicate rows:

```sql
SELECT *
FROM (
    SELECT c.*, COUNT(*) OVER (PARTITION BY email) AS cnt
    FROM customers c
) t
WHERE cnt > 1
ORDER BY email;
```

#### 162: How do you delete duplicate rows but keep one copy?

Number the rows in each duplicate group and delete all but the first.

```sql
-- PostgreSQL, SQL Server, Oracle, MySQL 8
DELETE FROM customers
WHERE id IN (
    SELECT id
    FROM (
        SELECT id,
               ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
        FROM customers
    ) t
    WHERE rn > 1
);
```

In SQL Server you can also delete through a CTE:

```sql
WITH d AS (
    SELECT ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM customers
)
DELETE FROM d WHERE rn > 1;
```

After cleaning up, add a `UNIQUE` constraint so it can't happen again.

#### 163: What is a Cartesian product, and how can you create one by accident?

A Cartesian product is every row of one table combined with every row of another. You get one by accident when you forget the join condition, mostly with the old comma syntax:

```sql
-- Forgot the WHERE condition: 10,000 customers x 1,000,000 orders = 10 billion rows
SELECT * FROM customers, orders;
```

A missing or wrong `ON` condition, like `ON 1 = 1` or joining on the wrong column, has the same effect.

#### 164: Does the order of tables in a join matter?

For inner joins, no. The result is the same, and the optimizer chooses the actual join order itself.

For outer joins, yes. `A LEFT JOIN B` is not the same as `B LEFT JOIN A`. When you mix inner and outer joins, the order and placement of conditions can change the result:

```sql
-- Orders with no items get NULL in i.product_id, so the inner join to
-- products drops them. This quietly undoes the LEFT JOIN.
SELECT *
FROM orders o
LEFT JOIN order_items i ON i.order_id = o.id
JOIN products p        ON p.id = i.product_id;
```

To keep all orders, make the second join a `LEFT JOIN` too, or group the joins with parentheses.

#### 165: How do you write a FULL OUTER JOIN in MySQL?

Combine a `LEFT JOIN` with the unmatched rows from a `RIGHT JOIN`, using `UNION ALL`.

```sql
SELECT e.first_name, d.name
FROM employees e
LEFT JOIN departments d ON d.id = e.department_id

UNION ALL

SELECT e.first_name, d.name
FROM employees e
RIGHT JOIN departments d ON d.id = e.department_id
WHERE e.id IS NULL;
```

Using `UNION` instead of `UNION ALL` without the `WHERE` also works, but it would also remove real duplicate rows.

#### 166: How do you UPDATE a table using values from another table?

The syntax differs between databases.

```sql
-- Standard / any database: correlated subquery
UPDATE orders
SET status = 'vip'
WHERE customer_id IN (SELECT id FROM customers WHERE country = 'US');

-- PostgreSQL
UPDATE products p
SET price = n.new_price
FROM new_prices n
WHERE n.product_id = p.id;

-- MySQL
UPDATE products p
JOIN new_prices n ON n.product_id = p.id
SET p.price = n.new_price;

-- SQL Server
UPDATE p
SET p.price = n.new_price
FROM products p
JOIN new_prices n ON n.product_id = p.id;
```

`MERGE` is another standard option (see question 281). If the source has more than one row for a target row, results can be unpredictable, so make sure the join is one-to-one.

#### 167: How do you DELETE rows based on another table?

```sql
-- Works everywhere
DELETE FROM orders
WHERE customer_id IN (SELECT id FROM customers WHERE is_test = TRUE);

-- PostgreSQL
DELETE FROM orders o
USING customers c
WHERE c.id = o.customer_id AND c.is_test = TRUE;

-- MySQL
DELETE o
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE c.is_test = TRUE;

-- SQL Server
DELETE o
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE c.is_test = 1;
```

#### 168: Which is faster, a JOIN or a subquery?

There is no fixed answer. Modern optimizers often rewrite `IN` and `EXISTS` subqueries into joins, so the plans end up the same. Pick the form that clearly says what you mean:

- Need columns from both tables? Use a join.
- Only checking whether a match exists? Use `EXISTS`.

When performance matters, look at the execution plan instead of guessing.

### Grouping and Pivoting

#### 169: Can you GROUP BY an expression?

Yes.

```sql
SELECT EXTRACT(YEAR FROM order_date) AS year, SUM(total)
FROM orders
GROUP BY EXTRACT(YEAR FROM order_date)
ORDER BY year;
```

PostgreSQL, MySQL, SQLite and Oracle 23ai also let you write `GROUP BY year` using the alias. SQL Server doesn't, so you have to repeat the expression there.

#### 170: What is the difference between GROUP BY and DISTINCT?

Without aggregates, they give the same result:

```sql
SELECT DISTINCT department_id FROM employees;
SELECT department_id FROM employees GROUP BY department_id;
```

Use `DISTINCT` when you just want unique rows. Use `GROUP BY` when you need aggregates per group. Performance is usually the same.

#### 171: What does ROLLUP do?

`ROLLUP` adds subtotal rows and a grand total row to a grouped result. It goes from the most detailed level up to the total.

```sql
SELECT country, EXTRACT(YEAR FROM created_at) AS year, COUNT(*)
FROM customers
GROUP BY ROLLUP (country, EXTRACT(YEAR FROM created_at));
```

This returns counts per (country, year), subtotals per country (year is `NULL`), and a grand total (both `NULL`). MySQL uses `GROUP BY country, year WITH ROLLUP`, and supports the standard form from 8.0.

#### 172: What does CUBE do?

`CUBE` produces subtotals for every combination of the listed columns. For `CUBE (a, b)` you get groups for (a, b), (a), (b) and the grand total.

```sql
SELECT category, status, SUM(i.quantity * i.unit_price) AS revenue
FROM order_items i
JOIN products p ON p.id = i.product_id
JOIN orders o   ON o.id = i.order_id
GROUP BY CUBE (category, status);
```

MySQL doesn't support `CUBE`.

#### 173: What are GROUPING SETS?

`GROUPING SETS` lets you list exactly which groupings you want in one query. It's like running several `GROUP BY` queries and combining them with `UNION ALL`, but in one pass over the data.

```sql
SELECT country, status, COUNT(*)
FROM orders o
JOIN customers c ON c.id = o.customer_id
GROUP BY GROUPING SETS (
    (country),
    (status),
    ()          -- grand total
);
```

`ROLLUP` and `CUBE` are shortcuts for common sets of groupings.

#### 174: What does the GROUPING() function do?

In `ROLLUP`, `CUBE` and `GROUPING SETS` results, a `NULL` in a grouping column could mean "this is a subtotal row" or "the data really is NULL". `GROUPING(col)` returns 1 when the `NULL` is from a subtotal and 0 otherwise.

```sql
SELECT CASE WHEN GROUPING(country) = 1 THEN 'All countries' ELSE country END AS country,
       COUNT(*)
FROM customers
GROUP BY ROLLUP (country);
```

#### 175: What is conditional aggregation?

Putting a condition inside an aggregate so you get several totals in one pass.

```sql
SELECT customer_id,
       SUM(CASE WHEN status = 'shipped' THEN total ELSE 0 END)   AS shipped_total,
       SUM(CASE WHEN status = 'cancelled' THEN total ELSE 0 END) AS cancelled_total,
       COUNT(*) FILTER (WHERE total > 500)                       AS big_orders  -- PostgreSQL
FROM orders
GROUP BY customer_id;
```

This is the most portable way to pivot data.

#### 176: How do you pivot rows into columns?

The portable way is conditional aggregation:

```sql
SELECT product_id,
       SUM(CASE WHEN EXTRACT(QUARTER FROM o.order_date) = 1 THEN quantity END) AS q1,
       SUM(CASE WHEN EXTRACT(QUARTER FROM o.order_date) = 2 THEN quantity END) AS q2,
       SUM(CASE WHEN EXTRACT(QUARTER FROM o.order_date) = 3 THEN quantity END) AS q3,
       SUM(CASE WHEN EXTRACT(QUARTER FROM o.order_date) = 4 THEN quantity END) AS q4
FROM order_items i
JOIN orders o ON o.id = i.order_id
GROUP BY product_id;
```

SQL Server and Oracle also have a `PIVOT` operator:

```sql
-- SQL Server
SELECT product_id, [1] AS q1, [2] AS q2, [3] AS q3, [4] AS q4
FROM (
    SELECT i.product_id, DATEPART(quarter, o.order_date) AS q, i.quantity
    FROM order_items i JOIN orders o ON o.id = i.order_id
) src
PIVOT (SUM(quantity) FOR q IN ([1], [2], [3], [4])) p;
```

In both cases the columns must be known when you write the query. For dynamic columns you need dynamic SQL.

#### 177: How do you unpivot columns into rows?

```sql
-- Portable: UNION ALL
SELECT product_id, 'q1' AS quarter, q1 AS qty FROM quarterly_sales
UNION ALL
SELECT product_id, 'q2', q2 FROM quarterly_sales
UNION ALL
SELECT product_id, 'q3', q3 FROM quarterly_sales;

-- PostgreSQL / SQL Server / Oracle: join to a VALUES list (one pass over the table)
-- (SQL Server: use CROSS APPLY (VALUES ...) instead of CROSS JOIN LATERAL)
SELECT s.product_id, v.quarter, v.qty
FROM quarterly_sales s
CROSS JOIN LATERAL (VALUES ('q1', s.q1), ('q2', s.q2), ('q3', s.q3)) AS v(quarter, qty);
```

SQL Server and Oracle also have an `UNPIVOT` operator.

#### 178: How do you combine values from many rows into one string?

```sql
-- Standard (LISTAGG): Oracle, DB2, Snowflake
SELECT department_id,
       LISTAGG(first_name, ', ') WITHIN GROUP (ORDER BY first_name)
FROM employees GROUP BY department_id;

-- PostgreSQL, SQL Server 2017+
SELECT department_id, STRING_AGG(first_name, ', ' ORDER BY first_name)  -- PostgreSQL
FROM employees GROUP BY department_id;

SELECT department_id, STRING_AGG(first_name, ', ') WITHIN GROUP (ORDER BY first_name)  -- SQL Server
FROM employees GROUP BY department_id;

-- MySQL, SQLite
SELECT department_id, GROUP_CONCAT(first_name ORDER BY first_name SEPARATOR ', ')
FROM employees GROUP BY department_id;
```

In MySQL, `GROUP_CONCAT` cuts results at 1024 bytes by default. Increase `group_concat_max_len` if you need more.

#### 179: How do you find departments whose average salary is above the company average?

```sql
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);
```

#### 180: How do you count distinct combinations of several columns?

```sql
-- MySQL accepts several columns directly
SELECT COUNT(DISTINCT o.customer_id, i.product_id)
FROM orders o
JOIN order_items i ON i.order_id = o.id;

-- PostgreSQL can count distinct row values
SELECT COUNT(DISTINCT (o.customer_id, i.product_id))
FROM orders o
JOIN order_items i ON i.order_id = o.id;

-- Portable
SELECT COUNT(*)
FROM (
    SELECT DISTINCT o.customer_id, i.product_id
    FROM orders o
    JOIN order_items i ON i.order_id = o.id
) t;
```

Don't concatenate columns into a string to count them. `'1' || '23'` and `'12' || '3'` both give `'123'`.

### Subqueries

#### 181: What is a subquery?

A query inside another query. It can appear in `SELECT`, `FROM`, `WHERE`, `HAVING`, and in `INSERT`, `UPDATE` and `DELETE` statements.

```sql
SELECT first_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

#### 182: What kinds of subqueries are there by the shape of their result?

- **Scalar subquery**: returns one row and one column. Can be used anywhere a single value goes.
- **Row subquery**: returns one row with several columns. Used in comparisons like `(a, b) = (SELECT x, y ...)`.
- **Table subquery**: returns many rows and columns. Used in `FROM`, `IN`, `EXISTS`, `ANY` or `ALL`.

#### 183: What is the difference between a correlated and a non-correlated subquery?

A non-correlated subquery doesn't depend on the outer query. It can run once by itself.

A correlated subquery uses a column from the outer query, so conceptually it runs once for every outer row.

```sql
-- Non-correlated
SELECT * FROM employees
WHERE department_id IN (SELECT id FROM departments WHERE name = 'Sales');

-- Correlated: uses e.department_id from the outer query
SELECT * FROM employees e
WHERE salary > (
    SELECT AVG(salary) FROM employees x WHERE x.department_id = e.department_id
);
```

Optimizers often turn correlated subqueries into joins, so "runs once per row" is the logical meaning, not always what actually happens.

#### 184: How do you use a subquery in the SELECT list?

It must return a single value (a scalar subquery).

```sql
SELECT c.name,
       (SELECT COUNT(*) FROM orders o WHERE o.customer_id = c.id) AS order_count
FROM customers c;
```

If it returns no rows, the value is `NULL`. If it returns more than one row, you get an error. For many columns from the same table, a join or `LATERAL` is usually cleaner and faster.

#### 185: What is a derived table?

A subquery in the `FROM` clause. It works like a temporary table for the query. Most databases require an alias for it (PostgreSQL 16 and later made it optional).

```sql
SELECT dept_stats.department_id, dept_stats.avg_salary
FROM (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
) AS dept_stats
WHERE dept_stats.avg_salary > 70000;
```

#### 186: What is the difference between IN and EXISTS?

`IN` checks if a value is in a list or subquery result. `EXISTS` checks if a subquery returns any row at all.

```sql
SELECT * FROM customers
WHERE id IN (SELECT customer_id FROM orders);

SELECT * FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

For positive checks, both give the same result, and modern optimizers usually produce the same plan. `EXISTS` can stop as soon as it finds one match. The big difference is with negation and `NULL`s (next question).

#### 187: What is the difference between NOT IN and NOT EXISTS?

If the subquery returns any `NULL`, `NOT IN` returns no rows, because `x <> NULL` is `UNKNOWN`. `NOT EXISTS` doesn't have this problem.

```sql
-- Dangerous if orders.customer_id can be NULL
SELECT * FROM customers WHERE id NOT IN (SELECT customer_id FROM orders);

-- Safe
SELECT * FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

`NOT EXISTS` is also easier for many optimizers to run as an efficient anti-join. Use `NOT EXISTS` by default.

#### 188: What do ANY, SOME and ALL do?

They compare a value with every value returned by a subquery.

- `> ANY (...)`: true if greater than at least one value. `SOME` is the same as `ANY`.
- `> ALL (...)`: true if greater than every value.

```sql
-- Employees who earn more than everyone in department 3
SELECT * FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE department_id = 3);
```

`= ANY` is the same as `IN`. `<> ALL` is the same as `NOT IN`, with the same `NULL` problem. If the subquery returns no rows, `ALL` is true and `ANY` is false.

#### 189: How do you find the second highest salary?

```sql
-- Using a subquery
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Using DENSE_RANK (handles ties)
SELECT DISTINCT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk = 2;

-- Using OFFSET
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
OFFSET 1 ROW FETCH NEXT 1 ROW ONLY;
```

The first query returns `NULL` if there is no second salary, which is often what interviewers want.

#### 190: How do you find the Nth highest salary?

Use `DENSE_RANK`, so that equal salaries count as one level.

```sql
SELECT DISTINCT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk = 3;   -- N = 3
```

A version without window functions:

```sql
SELECT DISTINCT e1.salary
FROM employees e1
WHERE 3 - 1 = (
    SELECT COUNT(DISTINCT e2.salary)
    FROM employees e2
    WHERE e2.salary > e1.salary
);
```

#### 191: What happens if a scalar subquery returns more than one row?

You get a runtime error like "more than one row returned by a subquery used as an expression". It often happens when data changes and a query that used to return one row now returns two. Fix the logic so it is guaranteed to return one row, for example by using an aggregate, filtering on a unique key, or using `IN` instead of `=`.

#### 192: How do you find employees who earn more than the average in their own department?

```sql
-- Correlated subquery
SELECT e.first_name, e.department_id, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(x.salary) FROM employees x WHERE x.department_id = e.department_id
);

-- Window function (reads the table once)
SELECT first_name, department_id, salary
FROM (
    SELECT e.*, AVG(salary) OVER (PARTITION BY department_id) AS dept_avg
    FROM employees e
) t
WHERE salary > dept_avg;
```

#### 193: Can you use ORDER BY inside a subquery?

Some databases allow it, but it doesn't control the order of the final result. Only the outermost `ORDER BY` does. It does matter when combined with `LIMIT`/`FETCH FIRST`/`TOP` inside the subquery, because then it decides which rows are picked. SQL Server rejects `ORDER BY` in subqueries and views unless `TOP`, `OFFSET` or `FOR XML` is also used.

#### 194: When might a subquery be slower than a join?

Older optimizers, and MySQL before 5.6, ran some `IN` subqueries as correlated subqueries, once per outer row. Modern optimizers mostly turn them into semi-joins. A correlated scalar subquery in the `SELECT` list can still be slow if it can't be turned into a join and the inner query has no supporting index. If a query is slow, check the plan. Don't assume one form is always faster.

#### 195: How do you compare several columns at once against a subquery?

Use a row value (tuple) comparison.

```sql
-- Each employee whose salary is the highest in their department
SELECT *
FROM employees
WHERE (department_id, salary) IN (
    SELECT department_id, MAX(salary)
    FROM employees
    GROUP BY department_id
);
```

PostgreSQL, MySQL, Oracle and SQLite support this. SQL Server doesn't, so use `EXISTS` with a correlated condition or a join instead.

#### 196: Is EXISTS (SELECT 1 ...) faster than EXISTS (SELECT \* ...)?

No. `EXISTS` only checks whether a row exists. It ignores the select list, so `SELECT 1`, `SELECT *` and `SELECT NULL` all perform the same. `SELECT 1` is common because it makes it clear that no columns are needed.

#### 197: How do you use a subquery in an UPDATE?

```sql
-- Set each order's total from its items
UPDATE orders o
SET total = (
    SELECT COALESCE(SUM(i.quantity * i.unit_price), 0)
    FROM order_items i
    WHERE i.order_id = o.id
);
```

Without `COALESCE`, orders with no items would get `NULL`. MySQL has a restriction: you can't select from the same table you're updating in a subquery, unless you wrap it in another derived table.

#### 198: Can you use a subquery in HAVING?

Yes.

```sql
-- Customers who spent more than the average customer
SELECT customer_id, SUM(total) AS spent
FROM orders
GROUP BY customer_id
HAVING SUM(total) > (
    SELECT AVG(customer_total)
    FROM (SELECT SUM(total) AS customer_total FROM orders GROUP BY customer_id) t
);
```

### Common Table Expressions

#### 199: What is a CTE?

A Common Table Expression is a named temporary result set defined with `WITH` at the start of a query. It exists only for that one statement.

```sql
WITH dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT e.first_name, e.salary, d.avg_salary
FROM employees e
JOIN dept_avg d ON d.department_id = e.department_id
WHERE e.salary > d.avg_salary;
```

CTEs make long queries easier to read by splitting them into named steps.

#### 200: What is the difference between a CTE, a derived table and a temporary table?

|                              | CTE           | Derived table      | Temporary table       |
| ---------------------------- | ------------- | ------------------ | --------------------- |
| Lives for                    | One statement | One statement      | The session           |
| Can be referenced many times | Yes           | No, must repeat it | Yes                   |
| Can be recursive             | Yes           | No                 | No                    |
| Can have indexes             | No            | No                 | Yes                   |
| Has statistics               | No            | No                 | Yes in most databases |

Use a temp table when you want to reuse a large intermediate result across several statements, or when an index on it would help.

#### 201: Can you define more than one CTE in a query?

Yes. Separate them with commas. Later CTEs can use earlier ones.

```sql
WITH monthly AS (
    SELECT DATE_TRUNC('month', order_date) AS month, SUM(total) AS revenue
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
),
with_prev AS (
    SELECT month, revenue, LAG(revenue) OVER (ORDER BY month) AS prev_revenue
    FROM monthly
)
SELECT month, revenue, revenue - prev_revenue AS change
FROM with_prev
ORDER BY month;
```

#### 202: Can a CTE be referenced more than once in the same query?

Yes. That's one of the main advantages over derived tables.

```sql
WITH totals AS (
    SELECT customer_id, SUM(total) AS spent
    FROM orders
    GROUP BY customer_id
)
SELECT *
FROM totals
WHERE spent > (SELECT AVG(spent) FROM totals);
```

Whether the database computes it once or twice depends on the product (see question 204).

#### 203: What is a recursive CTE?

A CTE that refers to itself. It has an anchor part (the starting rows) and a recursive part that runs again and again on the previous step's rows until it returns nothing.

```sql
-- Numbers 1 to 10
WITH RECURSIVE nums (n) AS (
    SELECT 1                    -- anchor
    UNION ALL
    SELECT n + 1 FROM nums      -- recursive part
    WHERE n < 10
)
SELECT n FROM nums;
```

PostgreSQL, MySQL and SQLite need the `RECURSIVE` keyword. SQL Server and Oracle don't use it.

#### 204: Are CTEs always materialized?

It depends on the database:

- **PostgreSQL 12+**: a CTE that is used once and has no side effects is inlined into the main query like a subquery. You can control this with `AS MATERIALIZED` or `AS NOT MATERIALIZED`. Before version 12, CTEs were always materialized, which sometimes made them slow.
- **SQL Server**: CTEs are always inlined. If used twice, the query runs twice.
- **MySQL 8**: the optimizer can either merge or materialize them.
- **Oracle**: decides by itself, and you can force it with the `MATERIALIZE` hint.

```sql
WITH big AS MATERIALIZED (
    SELECT * FROM orders WHERE total > 1000
)
SELECT ... FROM big ...;
```

#### 205: What is a data-modifying CTE?

In PostgreSQL, a CTE can contain `INSERT`, `UPDATE` or `DELETE` with `RETURNING`, and the main query can use the returned rows. It's a neat way to move rows between tables in one statement.

```sql
WITH moved AS (
    DELETE FROM orders
    WHERE order_date < DATE '2020-01-01'
    RETURNING *
)
INSERT INTO orders_archive
SELECT * FROM moved;
```

All parts of the statement see the same snapshot of the data, so they can't see each other's changes to the same table.

#### 206: What is the scope of a CTE?

A CTE is visible only inside the single statement that defines it. You can't use it in the next statement. If you need the result again, use a view, a temporary table, or repeat the CTE.

#### 207: How do you use a recursive CTE to list an employee hierarchy?

```sql
WITH RECURSIVE org AS (
    -- Start with the top manager(s)
    SELECT id, first_name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Add each person's direct reports
    SELECT e.id, e.first_name, e.manager_id, o.level + 1
    FROM employees e
    JOIN org o ON e.manager_id = o.id
)
SELECT * FROM org ORDER BY level, first_name;
```

#### 208: How do you stop a recursive CTE from looping forever?

If the data has a cycle (A manages B, B manages A), the recursion never ends. Ways to protect against this:

- Add a depth limit: `WHERE o.level < 20`.
- Track the visited path and skip rows already in it.
- Use the standard `CYCLE` clause (PostgreSQL 14+, Oracle).
- In SQL Server, the default `MAXRECURSION` is 100. You can change it with `OPTION (MAXRECURSION n)`.
- In MySQL, `cte_max_recursion_depth` defaults to 1000.

```sql
WITH RECURSIVE org AS (
    SELECT id, manager_id FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.manager_id FROM employees e JOIN org o ON e.manager_id = o.id
) CYCLE id SET is_cycle USING path
SELECT * FROM org WHERE NOT is_cycle;
```

Using `UNION` instead of `UNION ALL` also stops loops in simple cases, because duplicate rows are dropped.

### Window Functions

#### 209: What is a window function?

A window function calculates a value for each row using a set of related rows (the "window"), without collapsing those rows into one. You recognize it by the `OVER` clause.

```sql
SELECT first_name, department_id, salary,
       AVG(salary) OVER (PARTITION BY department_id) AS dept_avg
FROM employees;
```

Each employee row stays in the result, and each gets its department's average next to it.

#### 210: What is the difference between a window function and GROUP BY?

`GROUP BY` returns one row per group, and you lose the details of each row. A window function keeps every row and adds the calculated value to it.

```sql
-- One row per department
SELECT department_id, SUM(salary) FROM employees GROUP BY department_id;

-- One row per employee, with the department total on each row
SELECT first_name, department_id, salary,
       SUM(salary) OVER (PARTITION BY department_id) AS dept_total
FROM employees;
```

#### 211: What are the parts of the OVER clause?

```sql
function() OVER (
    PARTITION BY ...   -- split rows into groups (optional)
    ORDER BY ...       -- order rows inside each group (optional)
    ROWS/RANGE/GROUPS BETWEEN ... AND ...   -- frame (optional)
)
```

- `PARTITION BY` works like `GROUP BY`, but rows aren't merged.
- `ORDER BY` sets the order for ranking and running calculations.
- The frame picks which rows around the current row are used.

`OVER ()` with nothing inside means the whole result is one window.

#### 212: What does ROW_NUMBER() do?

It gives each row a unique number, starting at 1, in the order set by `ORDER BY`. With `PARTITION BY`, the numbering restarts for each group.

```sql
SELECT first_name, department_id, salary,
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rn
FROM employees;
```

If two rows tie on the `ORDER BY` values, which one gets the lower number is not defined. Add a unique column like `id` to the `ORDER BY` to make it stable.

#### 213: What is the difference between ROW_NUMBER, RANK and DENSE_RANK?

They differ in how they handle ties:

| salary | ROW_NUMBER | RANK | DENSE_RANK |
| ------ | ---------- | ---- | ---------- |
| 9000   | 1          | 1    | 1          |
| 8000   | 2          | 2    | 2          |
| 8000   | 3          | 2    | 2          |
| 7000   | 4          | 4    | 3          |

- `ROW_NUMBER` always gives unique numbers.
- `RANK` gives ties the same number and then skips numbers.
- `DENSE_RANK` gives ties the same number and doesn't skip.

```sql
SELECT salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,
       RANK()       OVER (ORDER BY salary DESC) AS rnk,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rnk
FROM employees;
```

#### 214: How do you get the top N rows per group?

Rank rows in each group, then filter in an outer query.

```sql
-- Top 3 earners in each department
SELECT *
FROM (
    SELECT e.*,
           ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rn
    FROM employees e
) t
WHERE rn <= 3;
```

Use `DENSE_RANK` instead if you want to include ties. A `LATERAL` join (question 158) is another option and can be faster when there's a good index and only a few rows per group are needed.

#### 215: What do LAG and LEAD do?

`LAG` reads a value from a previous row, and `LEAD` reads from a following row, based on the window order.

```sql
SELECT order_date, total,
       LAG(total)  OVER (ORDER BY order_date) AS prev_total,
       LEAD(total) OVER (ORDER BY order_date) AS next_total,
       LAG(total, 7, 0) OVER (ORDER BY order_date) AS total_7_rows_back
FROM daily_sales;
```

The second argument is how many rows to look back or ahead (default 1). The third is the default value when no such row exists (default `NULL`).

#### 216: Why does LAST_VALUE often return the current row instead of the last row?

Because of the default frame. When a window has `ORDER BY`, the default frame is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. So the "last" row of the frame is the current row (or its last tie).

```sql
-- Wrong: returns the current row's salary
SELECT first_name, salary,
       LAST_VALUE(salary) OVER (ORDER BY salary) AS wrong
FROM employees;

-- Right: frame covers the whole partition
SELECT first_name, salary,
       LAST_VALUE(salary) OVER (
           ORDER BY salary
           ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS highest
FROM employees;
```

An easier way is often `FIRST_VALUE` with the order reversed, or `MAX(...) OVER (...)`.

#### 217: What does NTH_VALUE do?

It returns the value from the Nth row of the window frame.

```sql
SELECT department_id, first_name, salary,
       NTH_VALUE(salary, 2) OVER (
           PARTITION BY department_id
           ORDER BY salary DESC
           ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS second_highest
FROM employees;
```

Supported in PostgreSQL, MySQL 8, Oracle and SQLite. SQL Server doesn't have it.

#### 218: What does NTILE do?

`NTILE(n)` splits the ordered rows into `n` groups of roughly equal size and returns the group number.

```sql
-- Split customers into 4 groups by spending (quartiles)
SELECT customer_id, spent,
       NTILE(4) OVER (ORDER BY spent DESC) AS quartile
FROM customer_totals;
```

If the rows don't divide evenly, the first groups get one extra row.

#### 219: How do you calculate a running total?

```sql
SELECT order_date, total,
       SUM(total) OVER (ORDER BY order_date, id
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM orders;
```

Add `PARTITION BY customer_id` for a running total per customer. Use `ROWS` and a unique sort key. With the default `RANGE` frame, rows that have the same `order_date` all get the same total.

#### 220: How do you calculate a moving average?

```sql
-- 7-day moving average (one row per day)
SELECT sale_date, revenue,
       AVG(revenue) OVER (
           ORDER BY sale_date
           ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
       ) AS avg_7_days
FROM daily_sales;
```

`ROWS` counts rows, not days. If some days are missing, the window covers more than 7 calendar days. To work on actual dates, use `RANGE` with an interval (question 367) or fill in missing dates first.

#### 221: What is the difference between ROWS, RANGE and GROUPS in a window frame?

- `ROWS` counts physical rows. `1 PRECEDING` is the row just before.
- `RANGE` works on values of the `ORDER BY` column. `RANGE BETWEEN INTERVAL '7' DAY PRECEDING AND CURRENT ROW` covers all rows with dates in the last 7 days. Rows with the same value are treated as peers and always included together.
- `GROUPS` counts groups of peers (rows with equal sort values). `1 PRECEDING` is the previous group of tied rows.

`GROUPS` is supported in PostgreSQL 11+, SQLite and Oracle 21c+. MySQL and SQL Server support `ROWS` and `RANGE`, and SQL Server's `RANGE` only allows `UNBOUNDED` and `CURRENT ROW`.

#### 222: What is the default window frame?

- With no `ORDER BY` in `OVER`: the whole partition.
- With `ORDER BY`: `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.

That's why `SUM(x) OVER (ORDER BY d)` gives a running total, and `SUM(x) OVER ()` gives the grand total. In SQL Server, the `RANGE` default can also be slower than `ROWS`, so writing `ROWS` explicitly is a good habit.

#### 223: What do PERCENT_RANK and CUME_DIST do?

- `PERCENT_RANK()` = (rank - 1) / (total rows - 1). Goes from 0 to 1.
- `CUME_DIST()` = (rows with value <= current) / total rows. Goes from just above 0 to 1.

```sql
SELECT first_name, salary,
       PERCENT_RANK() OVER (ORDER BY salary) AS pct_rank,
       CUME_DIST()    OVER (ORDER BY salary) AS cume_dist
FROM employees;
```

They answer questions like "what percent of employees earn the same as or less than this person?"

#### 224: How do you calculate each row's percentage of the total?

```sql
SELECT category,
       SUM(price) AS category_total,
       ROUND(100.0 * SUM(price) / SUM(SUM(price)) OVER (), 2) AS pct_of_total
FROM products
GROUP BY category;
```

`SUM(SUM(price)) OVER ()` is a window function over the grouped result: it adds up all the group totals. This is allowed because window functions run after `GROUP BY`.

#### 225: What is the WINDOW clause?

It lets you name a window definition and reuse it, instead of repeating the same `OVER (...)` many times.

```sql
SELECT first_name, salary,
       RANK()       OVER w AS rnk,
       AVG(salary)  OVER w AS running_avg
FROM employees
WINDOW w AS (PARTITION BY department_id ORDER BY salary DESC);
```

Supported in PostgreSQL, MySQL 8, SQLite, and SQL Server 2022+.

#### 226: Can you filter on a window function result in WHERE?

No. Window functions are calculated after `WHERE`, `GROUP BY` and `HAVING`. Wrap the query in a subquery or CTE and filter outside.

```sql
WITH ranked AS (
    SELECT e.*, RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees e
)
SELECT * FROM ranked WHERE rnk <= 10;
```

Snowflake, BigQuery, Databricks, DuckDB and Teradata have a `QUALIFY` clause that filters on window results directly:

```sql
SELECT * FROM employees
QUALIFY RANK() OVER (ORDER BY salary DESC) <= 10;
```

#### 227: How do you calculate the difference between a row and the previous row?

```sql
SELECT sale_date, revenue,
       revenue - LAG(revenue) OVER (ORDER BY sale_date) AS change_from_prev_day
FROM daily_sales;
```

The first row gets `NULL` because it has no previous row.

#### 228: Can you use FILTER or CASE inside a window aggregate?

Yes.

```sql
-- PostgreSQL: running count of cancelled orders per customer
SELECT id, customer_id, status,
       COUNT(*) FILTER (WHERE status = 'cancelled')
           OVER (PARTITION BY customer_id ORDER BY order_date) AS cancels_so_far
FROM orders;

-- Portable
SELECT id, customer_id, status,
       SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END)
           OVER (PARTITION BY customer_id ORDER BY order_date) AS cancels_so_far
FROM orders;
```

#### 229: How do you calculate year-over-year growth?

```sql
WITH yearly AS (
    SELECT EXTRACT(YEAR FROM order_date) AS year, SUM(total) AS revenue
    FROM orders
    GROUP BY EXTRACT(YEAR FROM order_date)
)
SELECT year, revenue,
       LAG(revenue) OVER (ORDER BY year) AS prev_revenue,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY year))
             / NULLIF(LAG(revenue) OVER (ORDER BY year), 0), 2) AS growth_pct
FROM yearly
ORDER BY year;
```

If a year is missing entirely, `LAG` compares with the year before the gap. Generate a full list of years first if that matters.

#### 230: How do you keep only the latest row per key?

```sql
-- Latest order for each customer
SELECT *
FROM (
    SELECT o.*,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC, id DESC) AS rn
    FROM orders o
) t
WHERE rn = 1;
```

PostgreSQL also has `DISTINCT ON`, which is short and fast:

```sql
SELECT DISTINCT ON (customer_id) *
FROM orders
ORDER BY customer_id, order_date DESC, id DESC;
```

### Set Operations

#### 231: What is the difference between UNION and UNION ALL?

Both stack the results of two queries on top of each other. `UNION` removes duplicate rows, which needs a sort or hash step. `UNION ALL` keeps everything and is faster.

```sql
SELECT email FROM customers
UNION
SELECT email FROM newsletter_subscribers;
```

Use `UNION ALL` unless you actually need duplicates removed.

#### 232: What does INTERSECT do?

It returns rows that appear in both query results, without duplicates.

```sql
-- Customers who ordered in both 2025 and 2026
SELECT customer_id FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2025
INTERSECT
SELECT customer_id FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2026;
```

MySQL added `INTERSECT` and `EXCEPT` in version 8.0.31.

#### 233: What does EXCEPT do?

It returns rows from the first query that are not in the second.

```sql
-- Products that have never been ordered
SELECT id FROM products
EXCEPT
SELECT product_id FROM order_items;
```

Oracle used to call it `MINUS`. Oracle 21c and later also accept `EXCEPT`. Unlike `NOT IN`, `EXCEPT` treats `NULL`s as equal, so it doesn't have the `NULL` problem.

#### 234: What are the rules for combining queries with UNION, INTERSECT and EXCEPT?

- Each query must have the same number of columns.
- Columns in the same position must have compatible types.
- Column names in the result come from the first query.
- `ORDER BY` goes at the very end and applies to the whole result.
- `INTERSECT` is evaluated before `UNION` and `EXCEPT` unless you use parentheses.

#### 235: How do you sort the result of a UNION?

Put one `ORDER BY` at the end. It sorts the combined result.

```sql
SELECT name, 'customer' AS type FROM customers
UNION ALL
SELECT name, 'supplier' FROM suppliers
ORDER BY name;
```

To sort or limit each part separately, wrap each part in parentheses or a subquery.

#### 236: What are INTERSECT ALL and EXCEPT ALL?

The `ALL` versions keep duplicates by counting them. If a value appears 3 times in the first result and once in the second:

- `INTERSECT ALL` returns it once (the smaller count).
- `EXCEPT ALL` returns it twice (3 - 1).

Supported in PostgreSQL, MySQL 8.0.31+, and DB2. SQL Server and Oracle (before 21c) don't support them.

#### 237: What is the difference between UNION and JOIN?

`UNION` combines rows vertically: it adds the rows of one query below the other, and the columns must line up. `JOIN` combines columns horizontally: it puts matching rows from two tables side by side.

#### 238: How do you compare two tables to find rows that differ?

Use `EXCEPT` in both directions.

```sql
(SELECT * FROM products_prod EXCEPT SELECT * FROM products_staging)
UNION ALL
(SELECT * FROM products_staging EXCEPT SELECT * FROM products_prod);
```

The first part shows rows only in production, the second shows rows only in staging. A changed row shows up in both parts. A `FULL OUTER JOIN` on the key with `IS DISTINCT FROM` checks on each column gives a more detailed comparison.

### Indexes

#### 239: What is an index?

An index is a separate data structure that helps the database find rows quickly without scanning the whole table, much like the index at the back of a book.

```sql
CREATE INDEX idx_orders_customer_id ON orders (customer_id);

-- This query can now jump straight to the matching rows
SELECT * FROM orders WHERE customer_id = 42;
```

Indexes speed up reads but take disk space and slow down inserts, updates and deletes, since every index has to be updated too.

#### 240: How does a B-tree index work?

A B-tree keeps keys in sorted order in a balanced tree of pages. The top (root) page points to pages below it, and the bottom (leaf) pages hold the keys with pointers to the table rows. To find a value, the database walks from the root down to a leaf, which takes only a few page reads even for millions of rows.

Because the keys are sorted, a B-tree helps with:

- Equality: `=`, `IN`
- Ranges: `<`, `>`, `BETWEEN`
- Prefix searches: `LIKE 'abc%'`
- `ORDER BY` and `MIN`/`MAX` on the indexed column

B-tree is the default index type in almost every relational database.

#### 241: What is the difference between a clustered and a non-clustered index?

- A **clustered index** decides the physical order of the table data. The leaf level of the index is the table rows. A table can have only one.
- A **non-clustered index** is a separate structure that points back to the table rows. A table can have many.

In SQL Server and MySQL InnoDB, the primary key is the clustered index by default. In InnoDB, secondary indexes store the primary key value as the pointer, so a large primary key makes every secondary index larger.

PostgreSQL doesn't have clustered indexes in this sense. Tables are heaps. The `CLUSTER` command reorders a table once, but the order isn't kept as new rows come in.

#### 242: How do you create and drop an index?

```sql
CREATE INDEX idx_employees_last_name ON employees (last_name);
CREATE UNIQUE INDEX uq_customers_email ON customers (email);

DROP INDEX idx_employees_last_name;                 -- PostgreSQL, Oracle, SQLite
DROP INDEX idx_employees_last_name ON employees;    -- MySQL, SQL Server
```

#### 243: What is the difference between a unique index and a unique constraint?

They enforce the same thing. Most databases build a unique index to enforce a unique constraint. The differences are small:

- A constraint is part of the logical design and can be the target of a foreign key.
- A unique index can have extra options, such as a `WHERE` condition (partial index) or expressions.

Use a constraint for business rules and a unique index when you need these extra options.

#### 244: What is a composite index, and what is the leftmost prefix rule?

A composite index covers several columns. It's sorted by the first column, then by the second within that, and so on, like a phone book sorted by last name then first name.

```sql
CREATE INDEX idx_orders_cust_date ON orders (customer_id, order_date);
```

This index helps:

- `WHERE customer_id = 5`
- `WHERE customer_id = 5 AND order_date >= '2026-01-01'`
- `WHERE customer_id = 5 ORDER BY order_date`

It usually doesn't help `WHERE order_date >= '2026-01-01'` alone, because `order_date` is not the leading column. Some databases can do a "skip scan" in that case (question 326), but don't count on it.

#### 245: How do you choose the column order in a composite index?

General rules:

1. Put columns used with `=` first.
2. Then the column used for a range (`>`, `<`, `BETWEEN`) or for sorting.
3. Columns after a range condition can't be used to narrow the search.

```sql
-- Query
SELECT * FROM orders WHERE status = 'new' AND order_date >= '2026-01-01';

-- Good: equality column first, range column second
CREATE INDEX idx_orders_status_date ON orders (status, order_date);
```

Also think about which other queries could reuse the same index.

#### 246: What is a covering index?

An index that has all the columns a query needs, so the database can answer from the index alone without visiting the table. In PostgreSQL this is called an index-only scan.

```sql
-- PostgreSQL 11+, SQL Server: INCLUDE adds non-key columns to the leaf level
CREATE INDEX idx_orders_customer ON orders (customer_id) INCLUDE (order_date, total);

SELECT order_date, total FROM orders WHERE customer_id = 42;
```

`INCLUDE` columns are stored but not used for sorting or searching, so they make the index less expensive than adding them as key columns. MySQL doesn't have `INCLUDE`, so you add them as key columns at the end.

#### 247: Why would a query not use an index?

Common reasons:

- **A function or math on the column**: `WHERE LOWER(email) = 'x'` or `WHERE salary * 2 > 100`.
- **A leading wildcard**: `LIKE '%son'`.
- **Type mismatch**: comparing a `VARCHAR` column to a number.
- **Low selectivity**: the condition matches a large part of the table, so a full scan is cheaper.
- **The leading column of a composite index isn't used.**
- **`OR` across different columns**, in some databases.
- **Old statistics**, so the optimizer misjudges the number of rows.
- **Small tables**, where scanning is just as fast.

```sql
-- Can't use an index on order_date
WHERE EXTRACT(YEAR FROM order_date) = 2026

-- Can
WHERE order_date >= DATE '2026-01-01' AND order_date < DATE '2027-01-01'
```

#### 248: What are the downsides of indexes?

- Every `INSERT`, `DELETE`, and `UPDATE` of an indexed column must also update the index.
- They use disk space and memory.
- Too many similar indexes make the optimizer's job harder and waste resources.
- They need maintenance (bloat, fragmentation, statistics).

Add indexes for real query patterns, and remove ones nobody uses.

#### 249: Should you index foreign key columns?

Usually yes. Most databases don't do it automatically (MySQL InnoDB is the exception: it requires an index and creates one if needed). Without an index:

- Joins from parent to child need to scan the child table.
- Deleting or updating a parent row needs to scan the child table to check for references, and this can cause lock problems.

```sql
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
```

#### 250: What is a partial (filtered) index?

An index with a `WHERE` condition, so it only covers some rows. It's smaller and faster when queries always target that subset.

```sql
-- PostgreSQL, SQLite
CREATE INDEX idx_orders_pending ON orders (order_date) WHERE status = 'pending';

-- SQL Server (filtered index)
CREATE INDEX idx_orders_pending ON orders (order_date) WHERE status = 'pending';
```

It's also useful for "unique among active rows":

```sql
CREATE UNIQUE INDEX uq_active_email ON users (email) WHERE deleted_at IS NULL;
```

MySQL doesn't support partial indexes.

#### 251: What is an expression (function-based) index?

An index on the result of an expression instead of a plain column.

```sql
-- PostgreSQL, Oracle, SQLite
CREATE INDEX idx_customers_lower_email ON customers (LOWER(email));

-- MySQL 8.0.13+ (note the extra parentheses)
CREATE INDEX idx_customers_lower_email ON customers ((LOWER(email)));

-- Now this can use the index
SELECT * FROM customers WHERE LOWER(email) = 'anna@example.com';
```

The query must use the same expression as the index. SQL Server does this with an indexed computed column.

#### 252: What are selectivity and cardinality, and why do they matter for indexes?

**Cardinality** is the number of distinct values in a column. **Selectivity** is how small a fraction of rows a condition returns. A condition that returns 0.1% of rows is highly selective.

Indexes help most with selective conditions. An index on `email` (almost unique) is very useful. An index on `is_active` (two values, 95% true) usually isn't, because reading 95% of rows through an index is slower than a full scan. It can still help when you search for the rare value, and a partial index is often better in that case.

#### 253: What is the difference between a hash index and a B-tree index?

A hash index stores a hash of each key. It's good only for equality (`=`) checks. A B-tree keeps keys sorted, so it also supports ranges, sorting and prefix searches.

In PostgreSQL, hash indexes are crash-safe since version 10 and can be a bit smaller and faster for equality on long values. In practice, B-tree is almost always the right choice. MySQL InnoDB doesn't let you create real hash indexes (it has an internal "adaptive hash index").

#### 254: How do you check whether a query uses an index?

Look at the execution plan.

```sql
-- PostgreSQL, MySQL
EXPLAIN SELECT * FROM orders WHERE customer_id = 42;
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 42;  -- actually runs it

-- SQL Server
SET SHOWPLAN_XML ON;   -- or "Display Estimated Execution Plan" in SSMS

-- Oracle
EXPLAIN PLAN FOR SELECT * FROM orders WHERE customer_id = 42;
SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```

Look for "Index Scan" or "Index Seek" versus "Seq Scan", "Table Scan" or "Full Table Scan".

#### 255: Is it useful to index a column with very few distinct values?

Usually not by itself. A boolean or a status column with 3 values matches too many rows per value. Exceptions:

- The data is skewed and you search for the rare value (`status = 'failed'` when 0.1% of rows fail). A partial index works well here.
- The column is part of a composite index with more selective columns.
- In data warehouses, bitmap indexes (Oracle) work well on low-cardinality columns, but they're a bad fit for tables with lots of concurrent writes.

### Views

#### 256: What is a view?

A view is a saved query that you can use like a table. It doesn't store data by itself (unless it's a materialized view). Every time you query the view, its query runs.

```sql
CREATE VIEW active_customers AS
SELECT id, name, email
FROM customers
WHERE is_active = TRUE;

SELECT * FROM active_customers WHERE name LIKE 'A%';
```

Use `CREATE OR REPLACE VIEW` to change it (in SQL Server 2016 SP1+, `CREATE OR ALTER VIEW`).

#### 257: Why use views?

- **Simplify queries**: hide complex joins behind a simple name.
- **Security**: give users access to the view but not the underlying tables, so they only see certain columns or rows.
- **Stable interface**: you can change table structure and keep the view the same for applications and reports.
- **Reuse**: business logic like "what counts as an active customer" lives in one place.

#### 258: Can you insert, update or delete through a view?

Yes, if the view is simple enough. In general a view is updatable when:

- It selects from one table.
- It has no `DISTINCT`, `GROUP BY`, `HAVING`, aggregates, window functions, `UNION` or `LIMIT`.
- The columns you change map directly to table columns.

```sql
UPDATE active_customers SET email = 'new@example.com' WHERE id = 5;
```

For more complex views, use `INSTEAD OF` triggers (PostgreSQL, SQL Server, Oracle) or rules to define what an insert or update should do.

#### 259: What does WITH CHECK OPTION do?

It stops inserts and updates through a view that would create rows the view itself can't see.

```sql
CREATE VIEW uk_customers AS
SELECT * FROM customers WHERE country = 'UK'
WITH CHECK OPTION;

-- Fails, because the new row wouldn't be visible in uk_customers
INSERT INTO uk_customers (id, name, country) VALUES (100, 'Hans', 'DE');
```

#### 260: What is a materialized view?

A materialized view stores the result of its query on disk, like a table. Reading it is fast, but the data can be out of date until it's refreshed.

```sql
-- PostgreSQL, Oracle
CREATE MATERIALIZED VIEW monthly_revenue AS
SELECT DATE_TRUNC('month', order_date) AS month, SUM(total) AS revenue
FROM orders
GROUP BY DATE_TRUNC('month', order_date);
```

It's good for expensive reports that don't need up-to-the-second data. SQL Server has indexed views instead, which are kept up to date automatically but have many restrictions. MySQL doesn't have materialized views, so people use summary tables updated by jobs or triggers.

#### 261: How do you refresh a materialized view?

```sql
-- PostgreSQL: blocks reads while refreshing
REFRESH MATERIALIZED VIEW monthly_revenue;

-- PostgreSQL: lets reads continue, needs a unique index on the view
CREATE UNIQUE INDEX ON monthly_revenue (month);
REFRESH MATERIALIZED VIEW CONCURRENTLY monthly_revenue;
```

PostgreSQL only does full refreshes. Oracle supports fast (incremental) refresh using materialized view logs, and can refresh on commit or on a schedule.

#### 262: What is the difference between a table, a view and a materialized view?

|                  | Table | View                                 | Materialized view   |
| ---------------- | ----- | ------------------------------------ | ------------------- |
| Stores data      | Yes   | No                                   | Yes                 |
| Always current   | Yes   | Yes                                  | No, until refreshed |
| Read speed       | Fast  | Same as its query                    | Fast                |
| Can have indexes | Yes   | No (except SQL Server indexed views) | Yes                 |

#### 263: Do views make queries faster?

A normal view doesn't. It's replaced by its query when you use it, so performance is the same as writing the query yourself. Views can even make things slower if they hide unneeded joins or if you stack views on top of views and the optimizer can't simplify them. Materialized views and indexed views can make reads faster because the result is stored.

### Transactions and Locking Basics

#### 264: What is a transaction?

A transaction is a group of statements that run as one unit. Either all of them take effect or none of them do.

```sql
BEGIN;  -- START TRANSACTION in MySQL, BEGIN TRANSACTION in SQL Server

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;
```

If something fails between the two updates, a `ROLLBACK` undoes the first one, so money is never lost.

#### 265: What does ACID mean?

- **Atomicity**: all or nothing. A transaction is never left half done.
- **Consistency**: a transaction moves the database from one valid state to another. Constraints are always respected.
- **Isolation**: transactions running at the same time don't see each other's unfinished work (how strictly depends on the isolation level).
- **Durability**: once committed, changes survive crashes. This is usually done with a write-ahead log.

#### 266: What do COMMIT and ROLLBACK do?

`COMMIT` saves all changes made in the transaction and makes them visible to others. `ROLLBACK` throws all changes away.

```sql
BEGIN;
DELETE FROM orders WHERE status = 'test';
-- Check the result...
ROLLBACK;  -- changed my mind
```

#### 267: What is a SAVEPOINT?

A savepoint marks a point inside a transaction that you can roll back to without undoing the whole transaction.

```sql
BEGIN;
INSERT INTO orders (id, customer_id) VALUES (1, 10);
SAVEPOINT before_items;
INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 999, 1);  -- fails
ROLLBACK TO SAVEPOINT before_items;
COMMIT;  -- the order is saved, the bad item isn't
```

SQL Server uses `SAVE TRANSACTION name` and `ROLLBACK TRANSACTION name`.

#### 268: What is autocommit?

In autocommit mode, every statement is its own transaction and is committed right away. It's the default in PostgreSQL, MySQL and SQL Server clients. To group statements, start a transaction explicitly. Oracle works the other way: a transaction starts automatically, and you must commit (although many tools turn on autocommit).

#### 269: What is a lock?

A lock stops other transactions from doing something with data you're using, so they don't interfere with each other. The two basic kinds are:

- **Shared (read) locks**: many transactions can hold them at the same time.
- **Exclusive (write) locks**: only one transaction can hold it, and it blocks others from writing (and, in some databases, from reading).

Locks are usually taken and released automatically. Databases that use MVCC (PostgreSQL, Oracle, MySQL InnoDB) don't need read locks for normal `SELECT`s, so readers and writers don't block each other.

#### 270: What is a deadlock?

A deadlock happens when two transactions each hold a lock the other one needs, so neither can continue.

```text
Transaction A: locks row 1, then wants row 2
Transaction B: locks row 2, then wants row 1
```

The database detects this and cancels one of them with a deadlock error. The application should retry it. To reduce deadlocks, access rows and tables in the same order everywhere and keep transactions short.

#### 271: What are the standard transaction isolation levels?

From weakest to strongest:

1. **Read Uncommitted**: can see uncommitted changes from others (dirty reads).
2. **Read Committed**: only sees committed data, but the same query can return different results within a transaction.
3. **Repeatable Read**: rows you've read won't change if you read them again. The standard still allows phantoms.
4. **Serializable**: transactions behave as if they ran one after another.

```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

#### 272: What is a dirty read?

Reading data that another transaction has changed but not committed. If that transaction rolls back, you've read data that never really existed. It can only happen at `READ UNCOMMITTED`. In SQL Server, the `NOLOCK` hint does the same thing. PostgreSQL never allows dirty reads, even if you ask for `READ UNCOMMITTED`.

#### 273: What is a non-repeatable read?

You read a row, another transaction updates and commits it, and when you read the same row again you get a different value. It can happen at `READ COMMITTED`. `REPEATABLE READ` prevents it.

#### 274: What is a phantom read?

You run a query with a condition, another transaction inserts (or deletes) rows that match it and commits, and running the same query again returns a different set of rows. The standard prevents it only at `SERIALIZABLE`. In practice, PostgreSQL's `REPEATABLE READ` (snapshot isolation) also prevents phantoms, and MySQL InnoDB prevents them for locking reads using gap locks.

#### 275: What are the default isolation levels in popular databases?

| Database       | Default                                                                        |
| -------------- | ------------------------------------------------------------------------------ |
| PostgreSQL     | Read Committed                                                                 |
| MySQL (InnoDB) | Repeatable Read                                                                |
| SQL Server     | Read Committed (with locking; Azure SQL Database uses Read Committed Snapshot) |
| Oracle         | Read Committed                                                                 |
| SQLite         | Serializable                                                                   |

#### 276: What does SELECT ... FOR UPDATE do?

It reads rows and locks them, so other transactions can't change or lock them until you commit. It's used for "read, then update" logic.

```sql
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;
-- application checks the balance...
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;
```

Without the lock, two sessions could read the same balance and both subtract from it. SQL Server uses the hints `WITH (UPDLOCK, ROWLOCK)` instead.

#### 277: What is the difference between optimistic and pessimistic locking?

- **Pessimistic locking** locks rows when you read them (`FOR UPDATE`), assuming conflicts are likely. Safe, but others have to wait.
- **Optimistic locking** doesn't lock. It checks at update time that nobody else changed the row, usually with a version column. If someone did, the update affects 0 rows and the app retries or shows an error.

```sql
-- Optimistic
UPDATE products
SET price = 25.00, version = version + 1
WHERE id = 7 AND version = 3;
-- 0 rows updated means someone else changed it first
```

Optimistic locking works well when conflicts are rare, such as in web forms.

### Inserting, Updating and Merging Data

#### 278: What is an upsert?

An upsert inserts a row, or updates it if a row with the same key already exists. Every database has its own syntax: `ON CONFLICT` in PostgreSQL and SQLite, `ON DUPLICATE KEY UPDATE` in MySQL, and the standard `MERGE` statement.

#### 279: How do you write an upsert in PostgreSQL?

```sql
INSERT INTO product_stock (product_id, quantity)
VALUES (7, 10)
ON CONFLICT (product_id)
DO UPDATE SET quantity = product_stock.quantity + EXCLUDED.quantity;
```

`EXCLUDED` is the row you tried to insert. The conflict target must match a unique index or constraint. SQLite uses the same syntax. This is safe under concurrency: two sessions can't both insert the same key.

#### 280: How do you write an upsert in MySQL?

```sql
INSERT INTO product_stock (product_id, quantity)
VALUES (7, 10) AS new
ON DUPLICATE KEY UPDATE quantity = product_stock.quantity + new.quantity;
```

The row alias (`AS new`) was added in MySQL 8.0.19. The older `VALUES(quantity)` function still works but is deprecated. `ON DUPLICATE KEY UPDATE` reacts to any unique key, not just the primary key, which can give surprises on tables with several unique keys.

#### 281: What is the MERGE statement?

`MERGE` compares a source with a target table and inserts, updates or deletes rows depending on whether they match. It's part of the SQL standard and is supported in SQL Server, Oracle, DB2, PostgreSQL 15+ and Snowflake. MySQL doesn't have it.

```sql
MERGE INTO product_stock AS t
USING incoming_stock AS s
    ON t.product_id = s.product_id
WHEN MATCHED AND s.quantity = 0 THEN
    DELETE
WHEN MATCHED THEN
    UPDATE SET quantity = s.quantity
WHEN NOT MATCHED THEN
    INSERT (product_id, quantity) VALUES (s.product_id, s.quantity);
```

If several source rows match the same target row, `MERGE` raises an error. Also, unlike `INSERT ... ON CONFLICT`, `MERGE` in PostgreSQL and SQL Server can still fail with a duplicate key error under heavy concurrency, because two sessions can both decide "not matched" at the same time.

#### 282: What does WHEN NOT MATCHED BY SOURCE do in MERGE?

It handles target rows that have no matching source row. It's useful when syncing a table with a full copy of the source.

```sql
MERGE INTO products AS t
USING products_feed AS s ON t.id = s.id
WHEN MATCHED THEN UPDATE SET name = s.name, price = s.price
WHEN NOT MATCHED BY TARGET THEN INSERT (id, name, price) VALUES (s.id, s.name, s.price)
WHEN NOT MATCHED BY SOURCE THEN DELETE;
```

SQL Server has supported it for a long time, and PostgreSQL added it in version 17. `WHEN NOT MATCHED` alone means `BY TARGET`.

#### 283: How do you get back the rows that an INSERT, UPDATE or DELETE changed?

```sql
-- PostgreSQL, SQLite 3.35+, MariaDB (INSERT/DELETE)
INSERT INTO customers (name, email)
VALUES ('Anna', 'anna@example.com')
RETURNING id, created_at;

-- SQL Server
INSERT INTO customers (name, email)
OUTPUT inserted.id, inserted.created_at
VALUES ('Anna', 'anna@example.com');

-- Oracle (into bind variables or PL/SQL variables)
UPDATE products SET price = price * 1.1 WHERE id = 7
RETURNING price INTO :new_price;
```

PostgreSQL 18 and Oracle 23ai let `RETURNING` show both old and new values. SQL Server has `deleted` and `inserted` in `OUTPUT` for the same thing:

```sql
-- PostgreSQL 18
UPDATE products SET price = price * 1.1
WHERE category = 'Books'
RETURNING id, old.price AS old_price, new.price AS new_price;
```

MySQL doesn't support `RETURNING`. Use `LAST_INSERT_ID()` for generated keys.

#### 284: How do you load a lot of data quickly?

Use the bulk loading tool for your database instead of many single-row inserts:

```sql
-- PostgreSQL
COPY orders FROM '/data/orders.csv' WITH (FORMAT csv, HEADER true);
-- (\copy in psql to read a file from the client machine)

-- MySQL
LOAD DATA INFILE '/data/orders.csv' INTO TABLE orders
FIELDS TERMINATED BY ',' IGNORE 1 LINES;

-- SQL Server
BULK INSERT orders FROM 'C:\data\orders.csv' WITH (FORMAT = 'CSV', FIRSTROW = 2);
```

Other tips: use multi-row inserts, commit in batches instead of per row, and for very large loads drop indexes before loading and recreate them after.

#### 285: How do you update different rows with different values in one statement?

Use `CASE`:

```sql
UPDATE products
SET price = CASE id
                WHEN 1 THEN 10.00
                WHEN 2 THEN 20.00
                WHEN 3 THEN 30.00
            END
WHERE id IN (1, 2, 3);
```

Don't forget the `WHERE`, or all other rows get `NULL`. For many rows, join with a `VALUES` list or a staging table:

```sql
-- PostgreSQL
UPDATE products p
SET price = v.price
FROM (VALUES (1, 10.00), (2, 20.00), (3, 30.00)) AS v(id, price)
WHERE p.id = v.id;
```

#### 286: How do you delete millions of rows without causing problems?

Deleting in one huge transaction can lock the table for a long time, grow the transaction log, and cause replication lag. Delete in batches instead:

```sql
-- SQL Server
WHILE 1 = 1
BEGIN
    DELETE TOP (10000) FROM logs WHERE created_at < '2025-01-01';
    IF @@ROWCOUNT = 0 BREAK;
END;

-- PostgreSQL (run repeatedly until 0 rows)
DELETE FROM logs
WHERE id IN (
    SELECT id FROM logs WHERE created_at < '2025-01-01' LIMIT 10000
);

-- MySQL
DELETE FROM logs WHERE created_at < '2025-01-01' LIMIT 10000;
```

If the table is partitioned by date, dropping an old partition is much faster than deleting rows.

#### 287: Does TRUNCATE reset identity columns, and can it be rolled back?

- **Identity reset**: SQL Server and MySQL reset the counter. PostgreSQL keeps it unless you write `TRUNCATE ... RESTART IDENTITY`. Oracle keeps it, and you reset it with `ALTER TABLE ... MODIFY ... GENERATED AS IDENTITY (START WITH ...)`.
- **Rollback**: PostgreSQL and SQL Server can roll back a `TRUNCATE` inside a transaction. MySQL and Oracle commit right away, so it can't be undone.

`TRUNCATE` also fails if other tables have foreign keys pointing to the table (PostgreSQL has `TRUNCATE ... CASCADE`).

#### 288: How do you insert rows but skip the ones that already exist?

```sql
-- PostgreSQL, SQLite
INSERT INTO tags (name) VALUES ('sql'), ('postgres')
ON CONFLICT (name) DO NOTHING;

-- MySQL (careful: IGNORE also hides other errors, like bad data)
INSERT IGNORE INTO tags (name) VALUES ('sql'), ('postgres');

-- Portable
INSERT INTO tags (name)
SELECT 'sql'
WHERE NOT EXISTS (SELECT 1 FROM tags WHERE name = 'sql');
```

The portable version can still fail under concurrency if two sessions run it at the same time, so keep a unique constraint as the final protection.

#### 289: How do you swap the values of two columns?

```sql
UPDATE t SET a = b, b = a;
```

In standard SQL, PostgreSQL, SQL Server and Oracle, all expressions on the right side use the values from before the update, so this works.

MySQL is different: it applies the assignments left to right, so `a` already has the new value when `b = a` runs, and both columns end up with `b`'s old value. In MySQL, use a temporary value or a self-join.

#### 290: What is a sequence?

A sequence is a database object that generates unique numbers, independently of any table.

```sql
CREATE SEQUENCE invoice_number_seq START WITH 1000 INCREMENT BY 1;

-- PostgreSQL
SELECT nextval('invoice_number_seq');

-- SQL Server, standard
SELECT NEXT VALUE FOR invoice_number_seq;

-- Oracle
SELECT invoice_number_seq.NEXTVAL FROM DUAL;
```

Identity columns usually use a sequence behind the scenes. Sequence values aren't rolled back, so gaps are normal. MySQL doesn't have sequences (MariaDB does).

### Dates, Strings and NULL Handling

#### 291: How do you calculate the difference between two dates?

```sql
-- PostgreSQL: date - date returns an integer number of days
SELECT DATE '2026-03-15' - DATE '2026-03-01';    -- 14
SELECT AGE(TIMESTAMP '2026-03-15', TIMESTAMP '2024-01-01');  -- 2 years 2 mons 14 days

-- MySQL
SELECT DATEDIFF('2026-03-15', '2026-03-01');     -- 14
SELECT TIMESTAMPDIFF(MONTH, '2024-01-01', '2026-03-15');  -- 26

-- SQL Server
SELECT DATEDIFF(day, '2026-03-01', '2026-03-15'); -- 14
```

Note that SQL Server's `DATEDIFF` counts boundaries crossed, not full periods. `DATEDIFF(year, '2025-12-31', '2026-01-01')` returns 1.

#### 292: How do you round a date down to the start of the month?

```sql
-- PostgreSQL, Snowflake, DuckDB
SELECT DATE_TRUNC('month', order_date) FROM orders;

-- SQL Server 2022+
SELECT DATETRUNC(month, order_date) FROM orders;

-- Oracle
SELECT TRUNC(order_date, 'MM') FROM orders;

-- MySQL
SELECT DATE_FORMAT(order_date, '%Y-%m-01') FROM orders;   -- returns a string
SELECT DATE_SUB(order_date, INTERVAL DAYOFMONTH(order_date) - 1 DAY) FROM orders;
```

This is the usual way to group data by month.

#### 293: How do you generate a list of dates?

```sql
-- PostgreSQL
SELECT d::date AS day
FROM generate_series(DATE '2026-01-01', DATE '2026-01-31', INTERVAL '1 day') AS d;

-- SQL Server 2022+
SELECT DATEADD(day, value, '2026-01-01') AS day
FROM GENERATE_SERIES(0, 30);

-- MySQL 8 and others: recursive CTE
WITH RECURSIVE days AS (
    SELECT DATE '2026-01-01' AS day
    UNION ALL
    SELECT day + INTERVAL 1 DAY FROM days WHERE day < DATE '2026-01-31'
)
SELECT day FROM days;
```

Many teams also keep a permanent calendar table with one row per day and useful columns like weekday, holiday flag and fiscal period.

#### 294: How do you show days with zero sales in a daily report?

Start from a full list of dates and `LEFT JOIN` the sales to it.

```sql
SELECT d.day, COALESCE(SUM(o.total), 0) AS revenue
FROM generate_series(DATE '2026-01-01', DATE '2026-01-31', INTERVAL '1 day') AS d(day)
LEFT JOIN orders o ON o.order_date = d.day
GROUP BY d.day
ORDER BY d.day;
```

If you just group the orders table, days with no orders are missing entirely.

#### 295: How do you convert a timestamp between time zones?

```sql
-- PostgreSQL: timestamptz to local time in a zone
SELECT created_at AT TIME ZONE 'Europe/London' FROM events;

-- SQL Server 2016+
SELECT created_at AT TIME ZONE 'UTC' AT TIME ZONE 'GMT Standard Time' FROM events;

-- MySQL (needs time zone tables loaded)
SELECT CONVERT_TZ(created_at, 'UTC', 'Europe/London') FROM events;
```

Use zone names like `'Europe/London'` instead of fixed offsets like `'+01:00'`, so daylight saving time is handled for you. A good rule: store times in UTC (or a time zone aware type) and convert only for display.

#### 296: How do you use regular expressions in SQL?

```sql
-- PostgreSQL
SELECT * FROM customers WHERE email ~* '^[a-z0-9._%+-]+@example\.com$';
SELECT REGEXP_REPLACE(phone, '[^0-9]', '', 'g') FROM customers;

-- MySQL 8, Oracle
SELECT * FROM customers WHERE REGEXP_LIKE(email, '^[a-z]+@example\\.com$');

-- SQL Server 2025
SELECT * FROM customers WHERE REGEXP_LIKE(email, '^[a-z]+@example\.com$');
```

The standard defines `LIKE_REGEX`, `REGEXP_LIKE`, `REGEXP_SUBSTR`, `REGEXP_REPLACE` and others, and most databases now offer functions with these names. Older SQL Server versions had no regex support, only `LIKE` patterns. Regex conditions can't use normal indexes.

#### 297: How do you split a comma-separated string into rows?

```sql
-- PostgreSQL 14+
SELECT string_to_table('red,green,blue', ',') AS color;
-- or: SELECT unnest(string_to_array('red,green,blue', ','));

-- SQL Server 2016+ (enable_ordinal added in 2022)
SELECT value FROM STRING_SPLIT('red,green,blue', ',');

-- MySQL 8: JSON_TABLE trick
SELECT j.color
FROM JSON_TABLE(
    CONCAT('["', REPLACE('red,green,blue', ',', '","'), '"]'),
    '$[*]' COLUMNS (color VARCHAR(50) PATH '$')
) AS j;
```

If you have to split strings often, that's a sign the data should be stored in a separate table with one value per row.

#### 298: How are NULLs treated in UNIQUE constraints, and what is NULLS NOT DISTINCT?

By default, `NULL`s are considered distinct in unique constraints, so a unique column can have many `NULL`s (SQL Server allows only one). SQL:2023 added a way to choose:

```sql
-- PostgreSQL 15+: only one NULL allowed
CREATE TABLE users (
    id    INT PRIMARY KEY,
    phone VARCHAR(20) UNIQUE NULLS NOT DISTINCT
);
```

`UNIQUE NULLS DISTINCT` is the default behavior. In SQL Server, to allow many `NULL`s, use a filtered unique index: `CREATE UNIQUE INDEX ... WHERE phone IS NOT NULL`.

#### 299: What is the difference between COALESCE, ISNULL, IFNULL and NVL?

All of them replace `NULL` with another value.

- `COALESCE(a, b, c, ...)`: standard, works everywhere, any number of arguments.
- `ISNULL(a, b)`: SQL Server. Two arguments. The result type is the type of the first argument, which can cut off longer values.
- `IFNULL(a, b)`: MySQL, SQLite.
- `NVL(a, b)`: Oracle.

In SQL Server, `COALESCE` is turned into a `CASE` expression, so a subquery inside it can run more than once. In most code, just use `COALESCE`.

#### 300: What is a collation?

A collation is a set of rules for comparing and sorting text: whether case matters, whether accents matter, and the alphabetical order for a language.

```sql
-- SQL Server: case-insensitive, accent-sensitive
SELECT * FROM customers WHERE name = 'anna' COLLATE Latin1_General_CI_AS;

-- MySQL 8 default
-- utf8mb4_0900_ai_ci = accent-insensitive, case-insensitive

-- PostgreSQL: pick a collation for sorting
SELECT name FROM customers ORDER BY name COLLATE "de-DE-x-icu";
```

Collation affects `=`, `LIKE`, `ORDER BY`, `GROUP BY`, `DISTINCT` and unique constraints. Joining columns with different collations can cause errors or stop index use. In MySQL, use `utf8mb4` rather than the old `utf8` (which is really `utf8mb3` and can't store emoji).

---

## Advanced Questions (301-450)

### Query Execution and Performance

#### 301: What happens inside the database when you run a query?

Roughly these steps:

1. **Parse**: check the syntax and build a parse tree.
2. **Analyze / bind**: look up tables, columns and types, and check permissions.
3. **Rewrite**: expand views, apply rules, simplify expressions.
4. **Optimize / plan**: consider different ways to run the query (join orders, join methods, which indexes) and pick the one with the lowest estimated cost.
5. **Execute**: run the plan, reading pages from memory (the buffer cache) or disk, and return rows.

Many databases cache plans so that steps 1 to 4 can be skipped for repeated queries.

#### 302: What is a cost-based optimizer?

It's the part of the database that chooses the execution plan. It estimates the cost of many possible plans using statistics about the data (row counts, distinct values, value distribution) plus cost settings for disk reads, CPU and memory, then picks the cheapest one.

Its choices are only as good as its estimates. Most bad plans come from wrong row count estimates, which are often caused by old statistics, correlated columns, or conditions the optimizer can't estimate well.

#### 303: How do you read an execution plan?

Take PostgreSQL as an example:

```sql
EXPLAIN ANALYZE
SELECT c.name, SUM(o.total)
FROM customers c
JOIN orders o ON o.customer_id = c.id
WHERE c.country = 'UK'
GROUP BY c.name;
```

```text
HashAggregate  (cost=2410.55..2420.55 rows=1000 width=40) (actual time=35.1..35.4 rows=812 loops=1)
  ->  Hash Join  (cost=48.50..2310.55 rows=20000 width=18) (actual time=0.9..29.8 rows=21455 loops=1)
        Hash Cond: (o.customer_id = c.id)
        ->  Seq Scan on orders o  (cost=0.00..1834.00 rows=100000 width=14) (actual ...)
        ->  Hash  (cost=36.00..36.00 rows=1000 width=30) (actual ...)
              ->  Index Scan using idx_customers_country on customers c (...)
```

Things to look at:

- Read it from the innermost (most indented) nodes up. Each node feeds its parent.
- `cost` is in arbitrary units: startup cost..total cost.
- Compare estimated `rows` with actual `rows`. A big difference points to a statistics problem.
- `loops` tells you how many times a node ran. Multiply actual time and rows by loops.
- Look for the nodes that take most of the time, sequential scans on big tables, and sorts or hashes that spill to disk.

#### 304: What is the difference between EXPLAIN and EXPLAIN ANALYZE?

`EXPLAIN` shows the plan the optimizer would use, with estimated costs and row counts. The query doesn't run.

`EXPLAIN ANALYZE` actually runs the query and shows real times and row counts next to the estimates. Be careful with it on `INSERT`, `UPDATE` and `DELETE`, because the changes really happen. Wrap it in a transaction and roll back:

```sql
BEGIN;
EXPLAIN ANALYZE DELETE FROM orders WHERE status = 'test';
ROLLBACK;
```

In PostgreSQL 18, `EXPLAIN ANALYZE` shows buffer usage by default. MySQL 8.0.18+ has `EXPLAIN ANALYZE` too. In SQL Server, the "actual execution plan" gives the same information.

#### 305: What are the different ways a database can read a table?

- **Sequential (full table) scan**: reads every page. Best when you need a large part of the table.
- **Index scan / seek**: walks the index to find matching keys, then fetches each row from the table. Best for a small number of rows.
- **Index-only scan**: gets everything from the index without touching the table (needs a covering index).
- **Bitmap index scan** (PostgreSQL): collects matching row locations from one or more indexes into a bitmap, then reads the table pages in physical order. A middle ground for medium-sized results, and it can combine several indexes.

For small results, index access wins. For large ones, a full scan is cheaper, because random reads cost more than sequential ones.

#### 306: What are nested loop, hash join and merge join?

- **Nested loop**: for each row of the outer input, look up matching rows in the inner input (ideally with an index). Great when the outer side is small. The only method that works for any join condition.
- **Hash join**: build a hash table from the smaller input, then scan the larger one and look up matches. Good for large inputs with equality joins. Needs memory, and spills to disk if the hash table is too big.
- **Merge join**: sort both inputs on the join key (or use already sorted input from an index), then walk through both together. Good for large inputs that are already sorted.

The optimizer picks the method based on estimated row counts. A nested loop chosen because the optimizer expected 1 row, when there are actually 100,000, is a classic cause of slow queries.

#### 307: What are database statistics and how are they kept up to date?

Statistics describe the data: number of rows, number of distinct values per column, most common values, histograms of value distribution, and how many `NULL`s there are. The optimizer uses them to estimate how many rows each step returns.

```sql
-- PostgreSQL (autovacuum also does this automatically)
ANALYZE orders;

-- MySQL
ANALYZE TABLE orders;

-- SQL Server
UPDATE STATISTICS orders;
```

After a large data load or delete, run it manually instead of waiting for the automatic process, especially before running heavy queries on that data.

#### 308: Why are row estimates sometimes very wrong, and what can you do?

Common causes:

- **Correlated columns**: the optimizer assumes conditions are independent. `city = 'Paris' AND country = 'France'` gets estimated far too low.
- **Functions or expressions** on columns that have no statistics.
- **Old statistics** after big data changes.
- **Skewed data** that a histogram doesn't capture well.
- **Table variables or functions** with fixed guesses.

Fixes include running `ANALYZE`, increasing the statistics target for a column, creating extended statistics for correlated columns, or adding an expression index (which also gets statistics).

```sql
-- PostgreSQL: teach the optimizer that city and country are related
CREATE STATISTICS st_city_country (dependencies) ON city, country FROM customers;
ANALYZE customers;
```

SQL Server builds multi-column statistics automatically for composite indexes and you can add them with `CREATE STATISTICS`.

#### 309: What does "sargable" mean?

A sargable (Search ARGument ABLE) condition is one the database can use an index for. Generally, the indexed column must appear alone on one side of the comparison.

```sql
-- Not sargable
WHERE YEAR(order_date) = 2026
WHERE total * 1.2 > 100
WHERE LEFT(name, 3) = 'Ann'
WHERE COALESCE(status, 'new') = 'new'

-- Sargable versions
WHERE order_date >= '2026-01-01' AND order_date < '2027-01-01'
WHERE total > 100 / 1.2
WHERE name LIKE 'Ann%'
WHERE status = 'new' OR status IS NULL
```

#### 310: What is parameter sniffing?

In SQL Server, when a stored procedure or parameterized query runs for the first time, the plan is built for the parameter values used in that first call and then cached. If later calls use values with very different selectivity, the cached plan can be a bad fit.

For example, a plan built for a customer with 5 orders (index seek and nested loop) is terrible for a customer with 5 million orders.

Fixes include `OPTION (RECOMPILE)`, `OPTIMIZE FOR`, splitting the logic into separate procedures, and the parameter sensitive plan optimization in SQL Server 2022+, which can keep several plans for one query. PostgreSQL has a similar issue with prepared statements: after five executions it may switch to a generic plan. You can control this with `plan_cache_mode`.

#### 311: What are prepared statements and why use them?

A prepared statement is a query sent once with placeholders, then executed many times with different values.

```sql
-- PostgreSQL
PREPARE get_orders (INT) AS
    SELECT * FROM orders WHERE customer_id = $1;

EXECUTE get_orders(42);
EXECUTE get_orders(43);
```

Benefits:

- **Security**: values are sent separately from the SQL text, which prevents SQL injection.
- **Speed**: parsing and planning can be done once and reused.

In application code you normally get this through your driver's parameter binding, not by writing `PREPARE` yourself.

#### 312: Why is OFFSET pagination slow for large page numbers, and what is keyset pagination?

With `OFFSET 100000 LIMIT 20`, the database still has to find and skip the first 100,000 rows, so each page gets slower. Results can also shift if rows are added while the user pages through.

Keyset (seek) pagination remembers the last row of the previous page and continues from there, using an index:

```sql
-- First page
SELECT id, created_at, title
FROM posts
ORDER BY created_at DESC, id DESC
FETCH FIRST 20 ROWS ONLY;

-- Next page: pass the last row's created_at and id
SELECT id, created_at, title
FROM posts
WHERE (created_at, id) < (TIMESTAMP '2026-05-01 10:00:00', 98765)
ORDER BY created_at DESC, id DESC
FETCH FIRST 20 ROWS ONLY;
```

With an index on `(created_at, id)`, every page is equally fast. The downside is you can't jump straight to page 500. SQL Server doesn't support row value comparison, so write it as `created_at < @t OR (created_at = @t AND id < @id)`.

#### 313: What is the N+1 query problem?

It happens when code runs one query to get a list, then one more query for each item in the list.

```text
SELECT * FROM orders WHERE customer_id = 42;   -- returns 100 orders
SELECT * FROM order_items WHERE order_id = 1;
SELECT * FROM order_items WHERE order_id = 2;
... 100 more queries
```

Each query may be fast, but the round trips add up. It's common with ORMs that load related data lazily. Fix it with a join, or with one query for all children:

```sql
SELECT * FROM order_items WHERE order_id IN (SELECT id FROM orders WHERE customer_id = 42);
```

Most ORMs have an "eager loading" option for this.

#### 314: How do you approach tuning a slow query?

A practical order:

1. **Measure**: find the actual slow queries using `pg_stat_statements`, the MySQL slow query log, or SQL Server Query Store. Look at total time (calls x average time), not just the slowest single run.
2. **Get the actual plan** with `EXPLAIN ANALYZE` or the actual execution plan.
3. **Check row estimates** against actual counts. If they're far off, fix statistics first.
4. **Look for the costly step**: full scans of big tables, nested loops with many iterations, sorts or hashes spilling to disk, functions on indexed columns.
5. **Fix the cause**: add or change an index, rewrite the condition to be sargable, remove unneeded joins or columns, aggregate earlier, or split the query.
6. **Check side effects**: a new index helps one query but slows writes.
7. **Measure again** with realistic data.

#### 315: Why can rewriting OR as UNION ALL make a query faster?

An `OR` across different columns often stops the optimizer from using either index well, so it falls back to a full scan.

```sql
-- May do a full scan
SELECT * FROM orders WHERE customer_id = 42 OR coupon_code = 'SPRING';

-- Each part can use its own index
SELECT * FROM orders WHERE customer_id = 42
UNION ALL
SELECT * FROM orders WHERE coupon_code = 'SPRING' AND customer_id <> 42;
```

The second part excludes rows the first part already returned. If `customer_id` can be `NULL`, use `customer_id IS DISTINCT FROM 42` there. PostgreSQL can often handle `OR` with a bitmap OR of two indexes, so check the plan first.

#### 316: Why is COUNT(\*) slow on a large PostgreSQL table, and what can you do?

Because of MVCC, PostgreSQL doesn't keep an exact row count. Different transactions can see different numbers of rows, so `COUNT(*)` has to scan the table (or an index, if the visibility map allows an index-only scan).

Options:

- Use an estimate if exact isn't needed:
  ```sql
  SELECT reltuples::bigint FROM pg_class WHERE relname = 'orders';
  ```
- Keep a counter table updated by triggers (adds write contention).
- Count only what you need with a selective `WHERE` and an index.
- For "is there at least one row?", use `EXISTS` instead of `COUNT(*) > 0`.

MySQL InnoDB has the same issue for the same reason.

#### 317: How can an implicit type conversion make a query slow?

If you compare a column to a value of a different type, the database may convert the column on every row, which turns an index seek into a full scan.

```sql
-- SQL Server: account_no is VARCHAR, but the parameter is NVARCHAR
-- The column is converted to NVARCHAR on every row
SELECT * FROM accounts WHERE account_no = N'12345';

-- MySQL: phone is VARCHAR, compared to a number
SELECT * FROM customers WHERE phone = 5551234;
```

This often comes from application drivers that send all strings as Unicode. Match parameter types to column types.

#### 318: What are query hints and when should you use them?

Hints tell the optimizer how to run a query, overriding its choices.

```sql
-- SQL Server
SELECT * FROM orders WITH (INDEX(idx_orders_customer)) WHERE customer_id = 42;
SELECT ... OPTION (RECOMPILE);

-- MySQL
SELECT * FROM orders FORCE INDEX (idx_orders_customer) WHERE customer_id = 42;

-- Oracle
SELECT /*+ INDEX(o idx_orders_customer) */ * FROM orders o WHERE customer_id = 42;
```

PostgreSQL doesn't have built-in hints (the `pg_hint_plan` extension adds them). Use hints as a last resort. They freeze a decision that might be wrong later when the data changes. Fix statistics, indexes or the query first. SQL Server's Query Store lets you force a plan without changing the code.

### Advanced Indexing

#### 319: What is an index-only scan and what does it depend on in PostgreSQL?

An index-only scan answers a query from the index alone. In PostgreSQL there's a catch: the index doesn't store visibility information, so the database must check whether each row is visible to the current transaction. It uses the visibility map, which marks pages where all rows are visible to everyone. For those pages it can skip the table. For other pages it still has to visit the table.

So index-only scans work best on tables that are vacuumed regularly. In `EXPLAIN ANALYZE`, check `Heap Fetches`. A high number means the visibility map isn't helping much.

#### 320: What is a GIN index?

GIN (Generalized Inverted Index) is a PostgreSQL index type for values that contain many parts, like arrays, `jsonb` documents and full-text search vectors. It maps each element to the rows that contain it, like the index of a book.

```sql
CREATE INDEX idx_products_tags ON products USING GIN (tags);          -- text[]
CREATE INDEX idx_events_payload ON events USING GIN (payload jsonb_path_ops);

SELECT * FROM products WHERE tags @> ARRAY['sale'];
SELECT * FROM events WHERE payload @> '{"type": "click"}';
```

GIN indexes are fast to search but slower to update than B-trees. The `pg_trgm` extension with GIN also speeds up `LIKE '%word%'` searches.

#### 321: What are GiST and BRIN indexes?

**GiST** (Generalized Search Tree) supports data where "overlaps", "contains" or "nearest" make sense: geometric shapes, ranges, PostGIS geometries and full-text search. It's also what enforces exclusion constraints.

```sql
-- No overlapping bookings for the same room
CREATE EXTENSION btree_gist;
CREATE TABLE bookings (
    room_id INT,
    during  TSTZRANGE,
    EXCLUDE USING GIST (room_id WITH =, during WITH &&)
);
```

**BRIN** (Block Range Index) stores only the min and max value for each range of table pages. It's tiny and works well for huge tables where the column follows the physical order, like an append-only log table with `created_at`.

```sql
CREATE INDEX idx_logs_created_brin ON logs USING BRIN (created_at);
```

#### 322: How does full-text search work in SQL databases?

Full-text search breaks text into words, reduces them to base forms (so "running" matches "run"), drops common words, and indexes the result. You can then search for words and rank results by relevance.

```sql
-- PostgreSQL
ALTER TABLE articles ADD COLUMN search tsvector
    GENERATED ALWAYS AS (to_tsvector('english', title || ' ' || body)) STORED;
CREATE INDEX idx_articles_search ON articles USING GIN (search);

SELECT title, ts_rank(search, q) AS rank
FROM articles, websearch_to_tsquery('english', 'database indexing') AS q
WHERE search @@ q
ORDER BY rank DESC;

-- MySQL
CREATE FULLTEXT INDEX ft_articles ON articles (title, body);
SELECT * FROM articles WHERE MATCH(title, body) AGAINST ('database indexing');

-- SQL Server: CREATE FULLTEXT INDEX, then CONTAINS() / FREETEXT()
```

It's much faster and smarter than `LIKE '%word%'`. For advanced needs like typo tolerance and facets, teams often use a separate search engine.

#### 323: How do you index fields inside JSON documents?

```sql
-- PostgreSQL: GIN index on the whole document (for @>, ?, ?| queries)
CREATE INDEX idx_events_payload ON events USING GIN (payload);

-- PostgreSQL: B-tree on one extracted field (for =, <, > and sorting)
CREATE INDEX idx_events_user ON events ((payload ->> 'user_id'));

-- MySQL: functional index on an extracted value
CREATE INDEX idx_events_user ON events ((CAST(payload->>'$.user_id' AS UNSIGNED)));

-- MySQL: multi-valued index on a JSON array
CREATE INDEX idx_tags ON products ((CAST(attrs->'$.tags' AS CHAR(30) ARRAY)));

-- SQL Server: computed column, then index it
ALTER TABLE events ADD user_id AS CAST(JSON_VALUE(payload, '$.user_id') AS INT);
CREATE INDEX idx_events_user ON events (user_id);
```

The query must use the exact same expression for the index to be used. If you search on a field a lot, it may be better as a real column.

#### 324: What is index bloat or fragmentation, and how do you fix it?

Over time, updates and deletes leave empty space in index pages, and page splits leave pages half full or out of order. The index grows larger than needed and scans read more pages.

```sql
-- PostgreSQL: rebuild without blocking writes (12+)
REINDEX INDEX CONCURRENTLY idx_orders_customer_id;

-- SQL Server
ALTER INDEX idx_orders_customer_id ON orders REORGANIZE;   -- light
ALTER INDEX idx_orders_customer_id ON orders REBUILD WITH (ONLINE = ON);

-- MySQL
OPTIMIZE TABLE orders;   -- rebuilds table and indexes
```

`FILLFACTOR` leaves free space in each page, which reduces page splits on tables with many updates. Don't rebuild indexes on a fixed schedule just because. Check bloat or fragmentation levels first.

#### 325: How do you create an index on a busy production table without blocking writes?

A plain `CREATE INDEX` blocks writes to the table while it builds.

```sql
-- PostgreSQL
CREATE INDEX CONCURRENTLY idx_orders_status ON orders (status);

-- SQL Server (Enterprise edition, Azure SQL)
CREATE INDEX idx_orders_status ON orders (status) WITH (ONLINE = ON);

-- MySQL InnoDB: online by default for most index operations
ALTER TABLE orders ADD INDEX idx_orders_status (status), ALGORITHM=INPLACE, LOCK=NONE;
```

In PostgreSQL, `CONCURRENTLY` takes longer, can't run inside a transaction, and if it fails it leaves an invalid index that you need to drop and create again. For other schema changes on very large MySQL tables, tools like `gh-ost` or `pt-online-schema-change` are common.

#### 326: What is an index skip scan?

A skip scan lets the database use a composite index even when the query doesn't filter on the leading column. It jumps through each distinct value of the leading column and searches the rest of the index inside each one.

```sql
CREATE INDEX idx_orders_status_date ON orders (status, order_date);

-- No condition on status, but a skip scan can still use the index
SELECT * FROM orders WHERE order_date = DATE '2026-03-01';
```

It only works well when the leading column has few distinct values. Oracle and MySQL 8.0.13+ have had it for a while. PostgreSQL added skip scan for B-tree indexes in version 18.

#### 327: What is a columnstore index?

A columnstore stores data column by column instead of row by row, and compresses each column. Analytic queries that read a few columns from millions of rows become much faster, because they read less data and can process values in batches.

```sql
-- SQL Server
CREATE CLUSTERED COLUMNSTORE INDEX cci_sales ON sales_fact;
CREATE NONCLUSTERED COLUMNSTORE INDEX ncci_orders ON orders (order_date, customer_id, total);
```

Columnstores are great for reporting and bad for frequent single-row updates. Oracle has the In-Memory column store, and PostgreSQL relies on extensions (like Citus columnar or pg_duckdb) or separate analytic databases.

#### 328: How do you find indexes that are never used?

```sql
-- PostgreSQL
SELECT schemaname, relname AS table_name, indexrelname AS index_name,
       idx_scan, pg_size_pretty(pg_relation_size(indexrelid)) AS size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;

-- SQL Server
SELECT OBJECT_NAME(i.object_id) AS table_name, i.name, s.user_seeks, s.user_scans, s.user_updates
FROM sys.indexes i
LEFT JOIN sys.dm_db_index_usage_stats s
       ON s.object_id = i.object_id AND s.index_id = i.index_id AND s.database_id = DB_ID()
WHERE OBJECTPROPERTY(i.object_id, 'IsUserTable') = 1;
```

Before dropping one, check that the stats cover a long enough period (stats reset on restart in SQL Server), look at replicas too, and remember that unique indexes enforce rules even if no query reads them.

#### 329: How can an index make ORDER BY ... LIMIT fast?

If an index is already sorted the way the query needs, the database can read the first N entries and stop, with no sort step.

```sql
CREATE INDEX idx_orders_customer_date ON orders (customer_id, order_date DESC);

-- Reads only 10 index entries
SELECT * FROM orders
WHERE customer_id = 42
ORDER BY order_date DESC
FETCH FIRST 10 ROWS ONLY;
```

Without such an index, the database must find all orders for the customer and sort them before returning 10.

#### 330: Is one composite index better than several single-column indexes?

For a query that filters on several columns together, a composite index in the right order is usually best. It goes straight to the matching rows.

Several single-column indexes can be combined (PostgreSQL bitmap AND/OR, MySQL index merge, SQL Server index intersection), but that is usually slower than one good composite index. Single-column indexes are more flexible for queries on just one column. In practice you design indexes around your most important queries.

#### 331: When do you need a descending index?

A B-tree can be read in either direction, so a single-column index works for both `ASC` and `DESC`. Descending matters in composite indexes when the query sorts columns in mixed directions:

```sql
-- Query
SELECT * FROM products ORDER BY category ASC, price DESC;

-- Index that matches the mixed order
CREATE INDEX idx_products_cat_price ON products (category ASC, price DESC);
```

MySQL ignored `DESC` in index definitions before 8.0. It's supported now.

#### 332: What are HOT updates in PostgreSQL?

In PostgreSQL, an `UPDATE` writes a new version of the row. Normally every index then needs a new entry pointing to the new version. A HOT (Heap-Only Tuple) update avoids that: if no indexed column changed and there's free space on the same page, the new version goes on that page and the indexes stay untouched.

To get more HOT updates:

- Don't index columns that change often unless you really need it.
- Set a lower `fillfactor` (like 80 or 90) on tables with many updates to leave room on each page.

You can check the ratio in `pg_stat_user_tables` (`n_tup_hot_upd` vs `n_tup_upd`). PostgreSQL 16 extended HOT so that changes to columns covered only by BRIN indexes still count as HOT.

### Concurrency and Isolation

#### 333: What is MVCC?

MVCC (Multi-Version Concurrency Control) keeps several versions of a row. When a transaction changes a row, it creates a new version instead of overwriting the old one. Each transaction reads from a snapshot and sees the versions that were committed when its snapshot was taken.

The main benefit is that readers don't block writers and writers don't block readers. PostgreSQL, Oracle, MySQL InnoDB, and SQL Server (with snapshot isolation turned on) all use it. The cost is cleanup: old versions must be removed later (VACUUM in PostgreSQL, undo logs and purge in InnoDB and Oracle, the version store in tempdb in SQL Server).

#### 334: What is the difference between snapshot isolation and serializable?

Under **snapshot isolation**, each transaction sees a consistent snapshot of the database from when it started, and a write fails if another transaction already changed the same row. It prevents dirty reads, non-repeatable reads and phantoms. But it still allows **write skew** (next question).

**Serializable** guarantees the result is the same as running the transactions one at a time, so write skew is also prevented.

PostgreSQL's `REPEATABLE READ` is snapshot isolation. Oracle's `SERIALIZABLE` is actually snapshot isolation too. PostgreSQL's `SERIALIZABLE` is real serializable.

#### 335: What is write skew?

Two transactions read the same data, make decisions based on it, and then each update different rows. Neither sees the other's change, so together they break a rule that each one checked.

The classic example: at least one doctor must be on call. Two doctors are on call.

```text
T1: SELECT COUNT(*) FROM doctors WHERE on_call;  -- 2
T2: SELECT COUNT(*) FROM doctors WHERE on_call;  -- 2
T1: UPDATE doctors SET on_call = false WHERE name = 'Alice';
T2: UPDATE doctors SET on_call = false WHERE name = 'Bob';
Both commit. Nobody is on call.
```

Snapshot isolation allows this because the two updates touch different rows. Fixes: use `SERIALIZABLE`, lock the rows you read with `SELECT ... FOR UPDATE`, or turn the rule into a constraint.

#### 336: What is a lost update and how do you prevent it?

Two transactions read the same value, both compute a new value from it, and both write. The second write silently overwrites the first.

```text
T1: SELECT stock FROM products WHERE id = 1;   -- 10
T2: SELECT stock FROM products WHERE id = 1;   -- 10
T1: UPDATE products SET stock = 9 WHERE id = 1;
T2: UPDATE products SET stock = 9 WHERE id = 1;  -- should be 8
```

Ways to prevent it:

- Do the math in SQL: `UPDATE products SET stock = stock - 1 WHERE id = 1 AND stock > 0;`
- Lock the row when reading: `SELECT ... FOR UPDATE`.
- Optimistic locking with a version column.
- Use `REPEATABLE READ` in PostgreSQL, where the second update fails with a serialization error. MySQL's `REPEATABLE READ` doesn't catch this for plain reads.

#### 337: How does SERIALIZABLE work in PostgreSQL?

PostgreSQL uses Serializable Snapshot Isolation (SSI). Transactions run on snapshots like in `REPEATABLE READ` and don't take extra blocking locks. PostgreSQL tracks read/write dependencies between concurrent transactions. If it finds a pattern that could lead to a non-serializable result, it aborts one transaction with:

```text
ERROR: could not serialize access due to read/write dependencies among transactions
SQLSTATE 40001
```

The application must catch error `40001` and retry the whole transaction. SSI gives strong guarantees with good concurrency, but it can have false positives, and it works best with short transactions.

#### 338: What is Read Committed Snapshot Isolation (RCSI) in SQL Server?

By default, SQL Server's `READ COMMITTED` uses locks, so readers wait for writers. With RCSI turned on, `READ COMMITTED` reads the last committed version of each row from the version store instead of waiting.

```sql
ALTER DATABASE shop SET READ_COMMITTED_SNAPSHOT ON;
```

This removes most reader/writer blocking and is often a better fix than adding `NOLOCK` hints everywhere. `NOLOCK` allows dirty reads and can even return rows twice or skip rows. RCSI uses space in tempdb for row versions. Azure SQL Database has it on by default.

#### 339: What lock types and lock modes exist?

Common lock modes (names from SQL Server, other databases are similar):

- **Shared (S)**: for reading. Many can be held together.
- **Exclusive (X)**: for writing. Blocks other S and X locks.
- **Update (U)**: taken when reading a row you plan to update. Only one U lock at a time, which prevents a common deadlock where two readers both try to upgrade to X.
- **Intent locks (IS, IX)**: placed on the table or page to say "I hold locks lower down". They let the database quickly check whether a table lock would conflict with row locks.

PostgreSQL has eight table-level lock modes (from `ACCESS SHARE` used by `SELECT` to `ACCESS EXCLUSIVE` used by most `ALTER TABLE` forms) and row-level modes (`FOR UPDATE`, `FOR NO KEY UPDATE`, `FOR SHARE`, `FOR KEY SHARE`).

#### 340: What is lock escalation?

When a statement holds a very large number of row or page locks, SQL Server may replace them with one table lock to save memory. The threshold is around 5,000 locks on one object. This can suddenly block other users of the whole table.

Ways to avoid it: change data in smaller batches, use RCSI, or control it with `ALTER TABLE ... SET (LOCK_ESCALATION = AUTO | TABLE | DISABLE)`. PostgreSQL and Oracle don't escalate row locks. PostgreSQL stores row locks in the rows themselves.

#### 341: How do you build a job queue in SQL with SKIP LOCKED?

`SKIP LOCKED` tells a locking `SELECT` to ignore rows that another transaction already locked instead of waiting. Several workers can then take different jobs at the same time without blocking each other.

```sql
-- PostgreSQL, MySQL 8, Oracle
BEGIN;

SELECT id, payload
FROM jobs
WHERE status = 'pending'
ORDER BY created_at
FETCH FIRST 1 ROWS ONLY      -- LIMIT 1 in MySQL
FOR UPDATE SKIP LOCKED;

-- process the job...
UPDATE jobs SET status = 'done' WHERE id = :id;

COMMIT;
```

SQL Server uses the `READPAST` hint: `SELECT TOP (1) ... FROM jobs WITH (UPDLOCK, READPAST, ROWLOCK)`. A partial index on pending jobs keeps the search fast.

#### 342: What does NOWAIT do?

`NOWAIT` makes a locking statement fail immediately if the row is locked, instead of waiting.

```sql
SELECT * FROM accounts WHERE id = 1 FOR UPDATE NOWAIT;
-- ERROR: could not obtain lock on row in relation "accounts"
```

Useful when the app would rather show "someone else is editing this" than hang. You can also set a lock timeout (`SET lock_timeout = '2s'` in PostgreSQL, `SET LOCK_TIMEOUT 2000` in SQL Server, `innodb_lock_wait_timeout` in MySQL).

#### 343: What are advisory locks?

Locks on numbers or names chosen by the application, not tied to any row or table. The database only manages who holds them. They're used to make sure only one process runs a job at a time, for example.

```sql
-- PostgreSQL
SELECT pg_try_advisory_lock(12345);   -- true if acquired
SELECT pg_advisory_unlock(12345);
SELECT pg_advisory_xact_lock(12345);  -- released automatically at commit/rollback

-- MySQL
SELECT GET_LOCK('nightly_report', 0);
SELECT RELEASE_LOCK('nightly_report');

-- SQL Server
EXEC sp_getapplock @Resource = 'nightly_report', @LockMode = 'Exclusive';
```

Be careful with session-level advisory locks and connection poolers: the lock belongs to the database connection, not to your app request.

#### 344: How do you reduce deadlocks?

- **Access objects in the same order**: if every transaction updates `accounts` before `ledger`, and rows in order of `id`, cycles can't form.
- **Keep transactions short**: no user input or slow API calls inside a transaction.
- **Have the right indexes**: without them, updates scan and lock more rows than needed.
- **Lock what you need up front**: `SELECT ... FOR UPDATE` on all needed rows at the start.
- **Use a lower isolation level** or row versioning where it's safe.
- **Retry**: deadlocks can't be avoided completely, so the app should retry the transaction when it gets a deadlock error.

To investigate, check the deadlock reports: the PostgreSQL log, `SHOW ENGINE INNODB STATUS` in MySQL, or the `system_health` Extended Events session in SQL Server.

#### 345: What are gap locks and next-key locks in MySQL InnoDB?

At `REPEATABLE READ`, InnoDB locks not just matching index records but also the gaps between them, so other transactions can't insert new rows into a range you've read with a locking read. This prevents phantoms.

- **Record lock**: locks one index entry.
- **Gap lock**: locks the space between two index entries.
- **Next-key lock**: a record lock plus the gap before it.

```sql
-- Locks existing rows with id 10 to 20 and the gaps around them
SELECT * FROM orders WHERE id BETWEEN 10 AND 20 FOR UPDATE;
-- Another session's INSERT of id 15 waits
```

Gap locks are a common cause of unexpected blocking and deadlocks in MySQL. Using `READ COMMITTED` turns most gap locking off.

#### 346: Why are long-running transactions a problem?

- They hold locks, blocking other sessions.
- In MVCC databases they keep old row versions alive. In PostgreSQL, VACUUM can't remove dead rows that the old transaction might still need, so tables and indexes bloat. In MySQL, the undo log (history list) grows.
- On replicas, long queries can conflict with replication.
- A transaction that sits "idle in transaction" while the app does something else is the worst case.

Monitor them (`pg_stat_activity` in PostgreSQL, `information_schema.innodb_trx` in MySQL) and set limits like `idle_in_transaction_session_timeout` and `statement_timeout` in PostgreSQL.

#### 347: What does VACUUM do in PostgreSQL?

Because of MVCC, updates and deletes leave old row versions (dead tuples) in the table. `VACUUM`:

- Marks the space from dead tuples as reusable.
- Updates the visibility map (needed for index-only scans).
- Freezes old transaction IDs to prevent wraparound.

```sql
VACUUM orders;
VACUUM (ANALYZE, VERBOSE) orders;
VACUUM FULL orders;   -- rewrites the table to shrink it; takes an exclusive lock
```

Autovacuum runs this automatically. On tables with heavy writes, it's common to tune it per table so it runs more often. `VACUUM FULL` blocks all access, so tools like `pg_repack` are used on production to shrink tables online.

#### 348: What is transaction ID wraparound in PostgreSQL?

PostgreSQL uses 32-bit transaction IDs, so about 4 billion of them, and they wrap around. To compare which transaction is older, it uses a window of about 2 billion. Rows with very old IDs must be "frozen" (marked as visible to everyone) by VACUUM before the counter wraps, or their visibility would become wrong.

If freezing falls too far behind, PostgreSQL first warns, then refuses new transactions to protect the data. This can happen on very busy databases if autovacuum is blocked by long transactions or turned off. Monitor `age(datfrozenxid)` per database and make sure autovacuum keeps up.

#### 349: How should an application handle serialization failures and deadlocks?

Treat them as normal and retry the whole transaction from the start, not just the last statement.

```text
for attempt in 1..5:
    try:
        BEGIN
        ... all reads and writes ...
        COMMIT
        break
    catch error with SQLSTATE 40001 (serialization failure) or 40P01 (deadlock):
        ROLLBACK
        wait a short random time (backoff)
```

Everything in the transaction must be safe to repeat, and no outside side effects (like sending an email) should happen until after the commit. SQL Server deadlock victims get error 1205, and MySQL uses error 1213.

#### 350: What does it mean for a database operation to be idempotent, and why does it matter?

An idempotent operation gives the same result if you run it once or several times. It matters because networks fail: a client may not know whether its commit succeeded and may retry.

Ways to make writes idempotent:

```sql
-- Use an idempotency key with a unique constraint
INSERT INTO payments (idempotency_key, order_id, amount)
VALUES ('a1b2c3', 42, 99.00)
ON CONFLICT (idempotency_key) DO NOTHING;

-- Set values instead of incrementing them
UPDATE orders SET status = 'paid' WHERE id = 42;          -- safe to repeat
UPDATE accounts SET balance = balance - 99 WHERE id = 1;  -- not safe to repeat
```

#### 351: What is two-phase commit?

Two-phase commit (2PC) is a way to commit one transaction across several databases so they all commit or all roll back.

1. **Prepare**: the coordinator asks each database to get ready. Each one writes everything needed to disk and votes yes or no.
2. **Commit**: if all voted yes, the coordinator tells all to commit. Otherwise, all roll back.

```sql
-- PostgreSQL (max_prepared_transactions must be > 0)
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
PREPARE TRANSACTION 'tx_42';
-- later, from the coordinator
COMMIT PREPARED 'tx_42';
```

The downside is that if the coordinator dies after the prepare step, participants hold locks until someone resolves the transaction. Many modern systems avoid 2PC and use patterns like the outbox pattern or sagas instead.

#### 352: How do you stop queries from running too long or waiting too long for locks?

```sql
-- PostgreSQL
SET statement_timeout = '30s';
SET lock_timeout = '5s';
SET idle_in_transaction_session_timeout = '60s';

-- MySQL
SET SESSION max_execution_time = 30000;   -- SELECT only, in milliseconds
SET SESSION innodb_lock_wait_timeout = 5; -- seconds

-- SQL Server
SET LOCK_TIMEOUT 5000;   -- milliseconds
-- Query timeouts are usually set in the client driver
```

A short `lock_timeout` is especially important for schema changes in PostgreSQL. An `ALTER TABLE` waiting for a lock also blocks every query that comes after it, so it's better to fail fast and retry.

### Advanced Analytics with Window Functions

#### 353: What is the gaps and islands problem, and how do you solve it?

You have a sequence (of numbers or dates) and need to find continuous runs ("islands") and the breaks between them ("gaps").

The trick: subtract `ROW_NUMBER()` from the value. Within a continuous run, the difference stays the same, so you can group by it.

```sql
-- seat numbers taken: 1,2,3,7,8,10
WITH t AS (
    SELECT seat_no,
           seat_no - ROW_NUMBER() OVER (ORDER BY seat_no) AS grp
    FROM taken_seats
)
SELECT MIN(seat_no) AS start_seat, MAX(seat_no) AS end_seat, COUNT(*) AS length
FROM t
GROUP BY grp
ORDER BY start_seat;
-- 1-3, 7-8, 10-10
```

For gaps, use `LEAD`:

```sql
SELECT seat_no + 1 AS gap_start, next_seat - 1 AS gap_end
FROM (SELECT seat_no, LEAD(seat_no) OVER (ORDER BY seat_no) AS next_seat FROM taken_seats) t
WHERE next_seat - seat_no > 1;
```

#### 354: How do you find each user's longest streak of consecutive login days?

Same idea as gaps and islands, but with dates.

```sql
WITH days AS (
    SELECT DISTINCT user_id, CAST(login_at AS DATE) AS d
    FROM logins
),
grouped AS (
    SELECT user_id, d,
           d - CAST(ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY d) AS INT) AS grp
    FROM days
)
SELECT user_id, MAX(streak) AS longest_streak
FROM (
    SELECT user_id, grp, COUNT(*) AS streak
    FROM grouped
    GROUP BY user_id, grp
) s
GROUP BY user_id;
```

`DISTINCT` is important: two logins on the same day would break the logic. The date minus integer syntax works in PostgreSQL. In SQL Server use `DATEADD(day, -ROW_NUMBER() OVER (...), d)`, and in MySQL `DATE_SUB(d, INTERVAL ROW_NUMBER() OVER (...) DAY)`.

#### 355: How do you calculate a running total that resets when a condition happens?

First build a group number that increases every time the reset condition is met, using a running count. Then do the running total inside each group.

```sql
-- Running total of deposits that resets after every withdrawal
WITH marked AS (
    SELECT *,
           SUM(CASE WHEN type = 'withdrawal' THEN 1 ELSE 0 END)
               OVER (PARTITION BY account_id ORDER BY created_at, id) AS grp
    FROM transactions
)
SELECT account_id, created_at, type, amount,
       SUM(CASE WHEN type = 'deposit' THEN amount ELSE 0 END)
           OVER (PARTITION BY account_id, grp ORDER BY created_at, id) AS deposits_since_withdrawal
FROM marked;
```

This "running count of events as a group key" pattern solves many problems that look like they need loops.

#### 356: How do you calculate a median?

Use the ordered-set aggregates `PERCENTILE_CONT` and `PERCENTILE_DISC`.

```sql
-- PostgreSQL, Oracle (as aggregate)
SELECT department_id,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary
FROM employees
GROUP BY department_id;

-- SQL Server (only as a window function)
SELECT DISTINCT department_id,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary)
           OVER (PARTITION BY department_id) AS median_salary
FROM employees;
```

`PERCENTILE_CONT` interpolates between the two middle values when the count is even. `PERCENTILE_DISC` returns an actual value from the data. Oracle and DuckDB also have `MEDIAN()`. MySQL has no percentile functions, so you calculate it with `ROW_NUMBER` and `COUNT`:

```sql
SELECT AVG(salary) AS median_salary
FROM (
    SELECT salary,
           ROW_NUMBER() OVER (ORDER BY salary) AS rn,
           COUNT(*) OVER () AS cnt
    FROM employees
) t
WHERE rn IN (FLOOR((cnt + 1) / 2), CEIL((cnt + 1) / 2));
```

#### 357: How do you find the most common value (mode)?

```sql
-- PostgreSQL
SELECT MODE() WITHIN GROUP (ORDER BY product_id) AS most_ordered
FROM order_items;

-- Portable, including ties
SELECT product_id, cnt
FROM (
    SELECT product_id, COUNT(*) AS cnt,
           RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
    FROM order_items
    GROUP BY product_id
) t
WHERE rnk = 1;
```

Here the window function is applied to the grouped result, so `COUNT(*)` inside `OVER` is allowed.

#### 358: How do you group events into sessions?

A new session starts when the time since the previous event is more than a timeout, like 30 minutes.

```sql
WITH flagged AS (
    SELECT user_id, event_time,
           CASE
               WHEN event_time - LAG(event_time) OVER (PARTITION BY user_id ORDER BY event_time)
                    <= INTERVAL '30 minutes'
               THEN 0 ELSE 1
           END AS is_new_session
    FROM events
),
sessions AS (
    SELECT user_id, event_time,
           SUM(is_new_session) OVER (PARTITION BY user_id ORDER BY event_time) AS session_no
    FROM flagged
)
SELECT user_id, session_no,
       MIN(event_time) AS session_start,
       MAX(event_time) AS session_end,
       COUNT(*)        AS events
FROM sessions
GROUP BY user_id, session_no;
```

The first event for each user has `LAG = NULL`, so the comparison is unknown and the `ELSE 1` marks it as a new session.

#### 359: How do you calculate a running count of distinct values?

`COUNT(DISTINCT ...) OVER (ORDER BY ...)` isn't supported in most databases. Instead, mark the first time each value appears, then do a running sum of those marks.

```sql
-- Running number of unique customers by day
WITH firsts AS (
    SELECT customer_id, MIN(order_date) AS first_order
    FROM orders
    GROUP BY customer_id
)
SELECT first_order AS day,
       SUM(COUNT(*)) OVER (ORDER BY first_order) AS cumulative_customers
FROM firsts
GROUP BY first_order
ORDER BY day;
```

#### 360: How do you build a monthly retention cohort table?

Group users by the month of their first activity (their cohort), then count how many are still active N months later.

```sql
WITH first_month AS (
    SELECT customer_id, DATE_TRUNC('month', MIN(order_date)) AS cohort
    FROM orders
    GROUP BY customer_id
),
activity AS (
    SELECT DISTINCT o.customer_id, f.cohort,
           DATE_TRUNC('month', o.order_date) AS active_month
    FROM orders o
    JOIN first_month f ON f.customer_id = o.customer_id
)
SELECT cohort,
       (EXTRACT(YEAR FROM active_month) - EXTRACT(YEAR FROM cohort)) * 12
         + EXTRACT(MONTH FROM active_month) - EXTRACT(MONTH FROM cohort) AS month_number,
       COUNT(*) AS active_customers
FROM activity
GROUP BY cohort, month_number
ORDER BY cohort, month_number;
```

Divide each row by the month 0 count of its cohort (with `FIRST_VALUE` or a join) to get retention percentages.

#### 361: How do you calculate a conversion funnel?

Count how many users reached each step, making sure each step happens after the previous one.

```sql
WITH steps AS (
    SELECT user_id,
           MIN(CASE WHEN event = 'view_product' THEN event_time END) AS viewed,
           MIN(CASE WHEN event = 'add_to_cart'  THEN event_time END) AS added,
           MIN(CASE WHEN event = 'purchase'     THEN event_time END) AS purchased
    FROM events
    WHERE event_time >= DATE '2026-03-01' AND event_time < DATE '2026-04-01'
    GROUP BY user_id
)
SELECT COUNT(viewed)                                          AS step1_viewed,
       COUNT(CASE WHEN added > viewed THEN 1 END)             AS step2_added,
       COUNT(CASE WHEN purchased > added AND added > viewed THEN 1 END) AS step3_purchased
FROM steps;
```

This uses the first time of each event. For stricter funnels (like within one session), group by session instead of user.

#### 362: How do you return the top 3 values per group, including ties?

```sql
SELECT category, name, price
FROM (
    SELECT p.*,
           DENSE_RANK() OVER (PARTITION BY category ORDER BY price DESC) AS rnk
    FROM products p
) t
WHERE rnk <= 3
ORDER BY category, price DESC;
```

`DENSE_RANK` returns the top 3 price levels, which could be more than 3 rows. `RANK` would return at least 3 rows but could skip levels. `ROW_NUMBER` returns exactly 3 rows and drops ties in an unpredictable way. Ask the interviewer which one they want.

#### 363: How do you find which products make up 80% of revenue (Pareto analysis)?

```sql
WITH revenue AS (
    SELECT product_id, SUM(quantity * unit_price) AS rev
    FROM order_items
    GROUP BY product_id
),
running AS (
    SELECT product_id, rev,
           SUM(rev) OVER (ORDER BY rev DESC, product_id
                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_rev,
           SUM(rev) OVER () AS total_rev
    FROM revenue
)
SELECT product_id, rev,
       ROUND(100.0 * running_rev / total_rev, 2) AS cumulative_pct
FROM running
WHERE running_rev - rev < 0.8 * total_rev   -- include the product that crosses 80%
ORDER BY rev DESC;
```

#### 364: What does the EXCLUDE clause do in a window frame?

It removes some rows from the frame:

- `EXCLUDE CURRENT ROW`
- `EXCLUDE GROUP` (the current row and its peers)
- `EXCLUDE TIES` (peers but not the current row)
- `EXCLUDE NO OTHERS` (default)

```sql
-- Compare each employee to the average of everyone else in the department
SELECT first_name, department_id, salary,
       AVG(salary) OVER (
           PARTITION BY department_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
           EXCLUDE CURRENT ROW
       ) AS avg_of_others
FROM employees;
```

Supported in PostgreSQL, SQLite and Oracle 21c+. Not in MySQL or SQL Server.

#### 365: What is MATCH_RECOGNIZE?

`MATCH_RECOGNIZE` (row pattern recognition, added in SQL:2016) finds patterns across ordered rows using something like regular expressions over rows. It's useful for things like finding V-shaped price movements or event sequences.

```sql
-- Oracle, Snowflake, Trino: find periods where a stock price fell then rose
SELECT *
FROM stock_prices
MATCH_RECOGNIZE (
    PARTITION BY symbol
    ORDER BY trade_date
    MEASURES FIRST(down.trade_date) AS fall_start,
             LAST(up.trade_date)    AS rise_end
    ONE ROW PER MATCH
    PATTERN (down+ up+)
    DEFINE
        down AS price < PREV(price),
        up   AS price > PREV(price)
);
```

PostgreSQL, MySQL and SQL Server don't support it, so there you'd use window functions and the grouping tricks shown above.

#### 366: How do you fill NULLs with the last known value (forward fill)?

Where `IGNORE NULLS` is supported (Oracle, SQL Server 2022+, Snowflake, BigQuery, DuckDB):

```sql
SELECT reading_time,
       LAST_VALUE(temperature) IGNORE NULLS OVER (ORDER BY reading_time) AS temp_filled
FROM sensor_readings;
```

PostgreSQL (as of version 18) and MySQL don't support `IGNORE NULLS`, so use the running count trick: count the non-`NULL` values so far to create groups, then take the one non-`NULL` value from each group.

```sql
WITH g AS (
    SELECT reading_time, temperature,
           COUNT(temperature) OVER (ORDER BY reading_time) AS grp
    FROM sensor_readings
)
SELECT reading_time,
       MAX(temperature) OVER (PARTITION BY grp) AS temp_filled
FROM g;
```

`COUNT(temperature)` only goes up on non-`NULL` rows, so each group starts with a real value followed by its `NULL`s.

#### 367: How do you calculate a rolling sum over a time period instead of a number of rows?

Use a `RANGE` frame with an interval. It looks at values, not row positions, so missing days and multiple rows per day are handled correctly.

```sql
-- PostgreSQL 11+, MySQL 8, Oracle
SELECT order_date, total,
       SUM(total) OVER (
           ORDER BY order_date
           RANGE BETWEEN INTERVAL '6' DAY PRECEDING AND CURRENT ROW
       ) AS revenue_last_7_days
FROM orders;
```

SQL Server doesn't support `RANGE` with an offset, so there you'd use a self-join on a date range or fill in the missing days and use `ROWS`.

#### 368: How do you compare each row to the best value in its group?

```sql
SELECT name, category, price,
       MAX(price) OVER (PARTITION BY category)          AS top_price_in_category,
       price - MAX(price) OVER (PARTITION BY category)  AS diff_from_top,
       ROUND(100.0 * price / SUM(price) OVER (PARTITION BY category), 1) AS pct_of_category
FROM products;
```

Window aggregates let you mix row-level and group-level values in one pass with no self-join.

### Recursive Queries and Hierarchies

#### 369: How does a recursive CTE actually run?

1. Run the anchor query. Its rows become the first "working table" and are added to the result.
2. Run the recursive part using only the working table (the rows from the last step), not the whole result so far.
3. The new rows become the next working table and are added to the result.
4. Repeat until the recursive part returns no rows.

With `UNION` (instead of `UNION ALL`), rows that already appeared in the result are thrown away at each step. The recursive part can't use aggregates, `DISTINCT`, or refer to the CTE more than once in most databases.

#### 370: How do you build the full path of each node in a hierarchy?

```sql
WITH RECURSIVE tree AS (
    SELECT id, name, parent_id,
           CAST(name AS VARCHAR(1000)) AS path,
           1 AS depth
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    SELECT c.id, c.name, c.parent_id,
           CAST(t.path || ' > ' || c.name AS VARCHAR(1000)),
           t.depth + 1
    FROM categories c
    JOIN tree t ON c.parent_id = t.id
)
SELECT id, path, depth FROM tree ORDER BY path;
-- Electronics > Computers > Laptops
```

The `CAST` is needed because the anchor sets the column type. Without it, the database may complain that types don't match, or cut the path off at the anchor's length.

#### 371: How do you find all ancestors of a node (walk up the tree)?

Start from the node and join to parents instead of children.

```sql
WITH RECURSIVE ancestors AS (
    SELECT id, first_name, manager_id, 0 AS levels_up
    FROM employees
    WHERE id = 57

    UNION ALL

    SELECT e.id, e.first_name, e.manager_id, a.levels_up + 1
    FROM employees e
    JOIN ancestors a ON e.id = a.manager_id
)
SELECT * FROM ancestors ORDER BY levels_up;
```

An index on the parent key (`manager_id`) helps for going down, and the primary key helps for going up.

#### 372: How do you detect cycles in hierarchical data?

Keep the path of visited IDs and stop when you meet one again.

```sql
-- PostgreSQL with arrays
WITH RECURSIVE walk AS (
    SELECT id, manager_id, ARRAY[id] AS path, FALSE AS is_cycle
    FROM employees
    WHERE id = 1

    UNION ALL

    SELECT e.id, e.manager_id, w.path || e.id, e.id = ANY(w.path)
    FROM employees e
    JOIN walk w ON e.manager_id = w.id
    WHERE NOT w.is_cycle
)
SELECT * FROM walk WHERE is_cycle;
```

The standard `CYCLE` clause does this for you (PostgreSQL 14+, Oracle):

```sql
WITH RECURSIVE walk AS (
    SELECT id, manager_id FROM employees WHERE id = 1
    UNION ALL
    SELECT e.id, e.manager_id FROM employees e JOIN walk w ON e.manager_id = w.id
) CYCLE id SET is_cycle USING path
SELECT * FROM walk;
```

#### 373: What does the SEARCH clause do in recursive CTEs?

It controls the order of the results: depth first (each branch fully before the next, like a file tree) or breadth first (level by level). It adds a column you can `ORDER BY`.

```sql
-- PostgreSQL 14+
WITH RECURSIVE tree AS (
    SELECT id, name, parent_id FROM categories WHERE parent_id IS NULL
    UNION ALL
    SELECT c.id, c.name, c.parent_id FROM categories c JOIN tree t ON c.parent_id = t.id
) SEARCH DEPTH FIRST BY name SET ord
SELECT name FROM tree ORDER BY ord;
```

Without it, you'd build a sortable path yourself, like in question 370.

#### 374: What are the different ways to store a tree in SQL?

| Model             | How it works                                       | Good at                      | Weak at                                |
| ----------------- | -------------------------------------------------- | ---------------------------- | -------------------------------------- |
| Adjacency list    | Each row has `parent_id`                           | Simple, easy writes, moves   | Reading whole subtrees needs recursion |
| Materialized path | Each row stores its path, like `/1/4/9/`           | Subtree with `LIKE '/1/4/%'` | Moving a subtree rewrites all paths    |
| Nested sets       | Each row has `lft` and `rgt` numbers               | Very fast subtree reads      | Inserts and moves renumber many rows   |
| Closure table     | Separate table with every ancestor/descendant pair | Fast reads, flexible queries | Extra table, more rows to maintain     |

The adjacency list plus recursive CTEs is the default choice today. Use a closure table or materialized path when the tree is read heavily and is deep.

#### 375: What is the ltree type in PostgreSQL?

`ltree` is an extension that stores materialized paths like `Top.Science.Physics` and gives operators and GiST index support for tree queries.

```sql
CREATE EXTENSION ltree;
CREATE TABLE categories (id INT PRIMARY KEY, path LTREE);
CREATE INDEX idx_categories_path ON categories USING GIST (path);

-- All descendants of Science
SELECT * FROM categories WHERE path <@ 'Top.Science';

-- All ancestors of Physics
SELECT * FROM categories WHERE path @> 'Top.Science.Physics';
```

SQL Server has a similar built-in type called `hierarchyid`.

#### 376: How do you calculate total quantities in a bill of materials?

Each part is made of sub-parts with quantities. The total needed for a sub-part is its quantity multiplied by all the quantities above it.

```sql
-- components(parent_part, child_part, qty)
WITH RECURSIVE bom AS (
    SELECT child_part AS part, qty AS total_qty
    FROM components
    WHERE parent_part = 'BIKE'

    UNION ALL

    SELECT c.child_part, b.total_qty * c.qty
    FROM components c
    JOIN bom b ON c.parent_part = b.part
)
SELECT part, SUM(total_qty) AS total_needed
FROM bom
GROUP BY part
ORDER BY part;
```

The final `SUM` is needed because the same part (like a screw) can appear in several branches.

#### 377: Can you find the shortest path between two nodes in SQL?

Yes, with a recursive CTE that explores paths and keeps track of the distance and visited nodes. It works for small graphs but grows fast on large ones.

```sql
-- edges(src, dst, cost)
WITH RECURSIVE paths AS (
    SELECT dst AS node, cost AS total_cost, ARRAY['A', dst] AS path
    FROM edges
    WHERE src = 'A'

    UNION ALL

    SELECT e.dst, p.total_cost + e.cost, p.path || e.dst
    FROM edges e
    JOIN paths p ON e.src = p.node
    WHERE NOT e.dst = ANY(p.path)     -- no cycles
      AND array_length(p.path, 1) < 10
)
SELECT path, total_cost
FROM paths
WHERE node = 'F'
ORDER BY total_cost
FETCH FIRST 1 ROWS ONLY;
```

For real graph workloads, use `pgRouting`, SQL Server graph tables with `SHORTEST_PATH`, or a graph database.

#### 378: What is SQL/PGQ?

SQL/PGQ (Property Graph Queries) is Part 16 of SQL:2023. It lets you define a graph on top of existing tables (some tables are vertices, some are edges) and query it with a pattern-matching syntax inside `GRAPH_TABLE`, similar to Cypher.

```sql
CREATE PROPERTY GRAPH social
    VERTEX TABLES (people KEY (id))
    EDGE TABLES (
        follows KEY (follower_id, followee_id)
            SOURCE KEY (follower_id) REFERENCES people (id)
            DESTINATION KEY (followee_id) REFERENCES people (id)
    );

SELECT *
FROM GRAPH_TABLE (social
    MATCH (a IS people WHERE a.name = 'Anna') -[IS follows]-> (b IS people)
    COLUMNS (b.name AS follows_name)
);
```

Oracle 23ai supports it. Other databases are still adding it, so check your version before relying on it.

### JSON, Arrays and Vectors

#### 379: What is the difference between json and jsonb in PostgreSQL?

|                                             | `json`                       | `jsonb`                        |
| ------------------------------------------- | ---------------------------- | ------------------------------ |
| Storage                                     | Text, exactly as given       | Parsed binary format           |
| Keeps whitespace, key order, duplicate keys | Yes                          | No (last duplicate key wins)   |
| Insert speed                                | Slightly faster              | Slightly slower (has to parse) |
| Query speed                                 | Slower (re-parses each time) | Faster                         |
| Indexing (GIN) and containment `@>`         | No                           | Yes                            |

Use `jsonb` unless you need to keep the exact original text.

#### 380: How do you read values out of a JSON column?

```sql
-- PostgreSQL
SELECT payload -> 'user' ->> 'name'     AS name,     -- ->> returns text
       payload #>> '{user,address,city}' AS city,
       (payload ->> 'amount')::numeric   AS amount
FROM events;

-- MySQL
SELECT payload->>'$.user.name' AS name,
       JSON_EXTRACT(payload, '$.amount') AS amount
FROM events;

-- Standard SQL/JSON (PostgreSQL 17+, Oracle, SQL Server, MySQL)
SELECT JSON_VALUE(payload, '$.user.name') AS name
FROM events;
```

In PostgreSQL, `->` returns JSON and `->>` returns text. Comparing the result of `->` with a string gives an error or wrong result, which is a common bug.

#### 381: What is the difference between JSON_VALUE and JSON_QUERY?

- `JSON_VALUE` extracts a single scalar value (string, number, boolean) and returns it as an SQL value. You can choose the type with `RETURNING`.
- `JSON_QUERY` extracts an object or array and returns it as JSON.

```sql
SELECT JSON_VALUE(doc, '$.price' RETURNING DECIMAL(10,2)) AS price,
       JSON_QUERY(doc, '$.tags')                            AS tags_json
FROM products_raw;
```

`JSON_VALUE` on an object returns `NULL` by default (or an error with `ERROR ON ERROR`). Both are in the SQL standard and supported in Oracle, SQL Server, MySQL (JSON_VALUE since 8.0.21) and PostgreSQL 17+.

#### 382: What is JSON_TABLE?

`JSON_TABLE` turns JSON data into rows and columns so you can query it like a normal table.

```sql
-- PostgreSQL 17+, MySQL 8, Oracle
SELECT o.id, items.*
FROM orders_json o,
     JSON_TABLE(
         o.doc, '$.items[*]'
         COLUMNS (
             product_id INT            PATH '$.product_id',
             qty        INT            PATH '$.qty',
             price      DECIMAL(10,2)  PATH '$.price'
         )
     ) AS items;
```

SQL Server uses `OPENJSON` with a `WITH` clause for the same thing. Before version 17, PostgreSQL users used `jsonb_array_elements` and `jsonb_to_recordset`.

#### 383: How do you check whether a JSON document contains a key or value?

```sql
-- Standard: JSON_EXISTS (PostgreSQL 17+, Oracle)
SELECT * FROM events WHERE JSON_EXISTS(payload, '$.coupon');

-- SQL Server 2022+
SELECT * FROM events WHERE JSON_PATH_EXISTS(payload, '$.coupon') = 1;

-- PostgreSQL jsonb operators
SELECT * FROM events WHERE payload ? 'coupon';                 -- has key
SELECT * FROM events WHERE payload @> '{"type": "purchase"}';  -- contains
SELECT * FROM events WHERE payload @? '$.items[*] ? (@.qty > 5)';  -- JSON path

-- MySQL
SELECT * FROM events WHERE JSON_CONTAINS_PATH(payload, 'one', '$.coupon');
SELECT * FROM events WHERE JSON_CONTAINS(payload, '"purchase"', '$.type');
```

In PostgreSQL, `@>`, `?` and `@?` can use a GIN index.

#### 384: How do you build JSON output from SQL?

```sql
-- JSON_OBJECT (PostgreSQL 16+, MySQL, Oracle, SQL Server 2022+)
SELECT JSON_OBJECT('id': c.id, 'name': c.name) FROM customers c;   -- PostgreSQL, Oracle, SQL Server
SELECT JSON_OBJECT('id', c.id, 'name', c.name) FROM customers c;   -- MySQL style

-- Aggregate rows into a JSON array (standard syntax: PostgreSQL 16+, Oracle)
SELECT c.id,
       JSON_ARRAYAGG(JSON_OBJECT('order_id' VALUE o.id, 'total' VALUE o.total)) AS orders
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.id;

-- PostgreSQL specific
SELECT jsonb_build_object('id', id, 'name', name) FROM customers;
SELECT jsonb_agg(c) FROM customers c;

-- SQL Server
SELECT id, name FROM customers FOR JSON PATH;
```

Building JSON in the database can save a lot of work in the application, especially for nested API responses.

#### 385: What JSON improvements did SQL:2023 bring?

- A native `JSON` data type (SQL:2016 only defined functions on strings).
- A simplified accessor syntax using dots and brackets, like `t.doc.customer.name` or `t.doc.items[0]`.
- More item methods in JSON path expressions, such as `.boolean()`, `.integer()`, `.string()` and `.date()`.
- `JSON_SERIALIZE`, `JSON_SCALAR` and the `JSON()` constructor.

```sql
-- Simplified accessor (Oracle supports this dot notation)
SELECT o.doc.customer.name, o.doc.items[0].price
FROM orders_json o;
```

PostgreSQL 17 added `JSON()`, `JSON_SCALAR()` and `JSON_SERIALIZE()`. Support for the dot syntax varies, so check your database.

#### 386: How do you update one field inside a JSON column?

```sql
-- PostgreSQL
UPDATE users
SET prefs = jsonb_set(prefs, '{theme}', '"dark"')
WHERE id = 1;

UPDATE users SET prefs = prefs || '{"lang": "en"}' WHERE id = 1;   -- merge
UPDATE users SET prefs = prefs - 'old_key' WHERE id = 1;            -- remove key

-- MySQL
UPDATE users SET prefs = JSON_SET(prefs, '$.theme', 'dark') WHERE id = 1;
UPDATE users SET prefs = JSON_REMOVE(prefs, '$.old_key') WHERE id = 1;

-- SQL Server
UPDATE users SET prefs = JSON_MODIFY(prefs, '$.theme', 'dark') WHERE id = 1;
```

In PostgreSQL, changing one key still writes a new version of the whole row. Large, often-changed JSON documents can cause a lot of write traffic.

#### 387: When should you use a JSON column, and when should you use normal columns?

Use JSON for:

- Data with a shape that really varies, like product attributes that differ by category.
- Raw payloads from outside systems that you store as-is.
- Data you always read and write as a whole and rarely filter on.

Use normal columns for:

- Fields you filter, join, sort or aggregate on often.
- Data that needs constraints (`NOT NULL`, foreign keys, `CHECK`).
- Data that changes often field by field.

A common mix: core fields as columns, and an extra JSON column for the flexible part. If a JSON field becomes important, move it into its own column.

#### 388: How do you check if a string is valid JSON?

The SQL:2016 `IS JSON` predicate does this. PostgreSQL added it in version 16.

```sql
-- PostgreSQL 16+, Oracle
SELECT * FROM raw_imports WHERE body IS JSON;
SELECT * FROM raw_imports WHERE body IS JSON OBJECT;     -- also ARRAY, SCALAR
SELECT * FROM raw_imports WHERE body IS JSON WITH UNIQUE KEYS;

-- MySQL
SELECT * FROM raw_imports WHERE JSON_VALID(body);

-- SQL Server
SELECT * FROM raw_imports WHERE ISJSON(body) = 1;
```

You can use it in a `CHECK` constraint when storing JSON in a text column.

#### 389: How do you work with arrays in PostgreSQL?

```sql
CREATE TABLE posts (id INT PRIMARY KEY, tags TEXT[]);

INSERT INTO posts VALUES (1, ARRAY['sql', 'postgres']), (2, '{sql,mysql}');

SELECT * FROM posts WHERE 'sql' = ANY(tags);         -- contains element
SELECT * FROM posts WHERE tags @> ARRAY['sql'];      -- contains (can use GIN index)
SELECT * FROM posts WHERE tags && ARRAY['mysql', 'oracle'];  -- overlaps
SELECT id, unnest(tags) AS tag FROM posts;           -- array to rows
SELECT array_agg(name ORDER BY name) FROM products;  -- rows to array
SELECT tags[1] FROM posts;                           -- arrays start at 1
```

Arrays are handy for small lists like tags, but a separate table is better when the items have their own data or need foreign keys.

#### 390: How do you turn a JSON array into rows?

```sql
-- PostgreSQL
SELECT o.id, item ->> 'sku' AS sku, (item ->> 'qty')::int AS qty
FROM orders_json o
CROSS JOIN LATERAL jsonb_array_elements(o.doc -> 'items') AS item;

-- SQL Server
SELECT o.id, j.sku, j.qty
FROM orders_json o
CROSS APPLY OPENJSON(o.doc, '$.items') WITH (sku VARCHAR(20) '$.sku', qty INT '$.qty') j;

-- MySQL 8, Oracle, PostgreSQL 17+
SELECT o.id, j.sku, j.qty
FROM orders_json o,
     JSON_TABLE(o.doc, '$.items[*]' COLUMNS (sku VARCHAR(20) PATH '$.sku', qty INT PATH '$.qty')) j;
```

#### 391: How do you store and search vector embeddings in SQL databases?

Embeddings are arrays of numbers produced by machine learning models. Similar items have vectors that are close to each other, which is used for semantic search and recommendations.

```sql
-- PostgreSQL with the pgvector extension
CREATE EXTENSION vector;
CREATE TABLE documents (id BIGINT PRIMARY KEY, content TEXT, embedding VECTOR(1536));
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops);

SELECT id, content
FROM documents
ORDER BY embedding <=> '[0.12, -0.03, ...]'   -- cosine distance
LIMIT 5;
```

Other databases now have this built in: SQL Server 2025 has a `VECTOR` type and `VECTOR_DISTANCE()`, Oracle 23ai has `VECTOR` and `VECTOR_DISTANCE()`, and MySQL 9 added a `VECTOR` type. Approximate indexes like HNSW and IVFFlat trade a little accuracy for a lot of speed.

#### 392: What is the difference between exact and approximate nearest neighbor search?

**Exact** search compares the query vector with every row and returns the true closest matches. It's accurate but slow on large tables.

**Approximate** (ANN) search uses an index like HNSW (a graph of neighbors) or IVFFlat (clusters) to look at only part of the data. It's much faster but can miss some true matches. You can usually tune the trade-off:

```sql
-- pgvector: search more of the HNSW graph for better accuracy
SET hnsw.ef_search = 100;
```

Filtering with `WHERE` together with an ANN index can return fewer rows than asked for, because the index finds the nearest vectors first and the filter removes some afterwards. pgvector 0.8 added iterative index scans to help with this.

### Partitioning, Replication and Scaling

#### 393: What is table partitioning?

Partitioning splits one large table into smaller pieces (partitions) by the value of a column, while queries still see one table.

```sql
-- PostgreSQL declarative partitioning
CREATE TABLE events (
    id         BIGINT,
    created_at TIMESTAMPTZ NOT NULL,
    payload    JSONB
) PARTITION BY RANGE (created_at);

CREATE TABLE events_2026_01 PARTITION OF events
    FOR VALUES FROM ('2026-01-01') TO ('2026-02-01');
CREATE TABLE events_2026_02 PARTITION OF events
    FOR VALUES FROM ('2026-02-01') TO ('2026-03-01');
```

Benefits: queries can skip partitions they don't need, old data can be removed by dropping a partition, and maintenance (vacuum, index rebuilds) works on smaller pieces. It doesn't automatically make every query faster. Queries that don't filter on the partition key may get slower.

#### 394: What partitioning methods are there?

- **Range**: by ranges of values, usually dates. Best for time-series data.
- **List**: by specific values, like `country IN ('UK', 'IE')`.
- **Hash**: by a hash of the key, to spread rows evenly when there's no natural range.
- **Composite (sub-partitioning)**: for example range by month, then hash by customer.

```sql
CREATE TABLE customers_part (id INT, region TEXT) PARTITION BY LIST (region);
CREATE TABLE customers_eu PARTITION OF customers_part FOR VALUES IN ('EU');

CREATE TABLE sessions (id BIGINT, user_id BIGINT) PARTITION BY HASH (user_id);
CREATE TABLE sessions_p0 PARTITION OF sessions FOR VALUES WITH (MODULUS 4, REMAINDER 0);
```

#### 395: What is partition pruning?

The optimizer skips partitions that can't contain matching rows, based on the `WHERE` condition on the partition key.

```sql
EXPLAIN SELECT * FROM events WHERE created_at >= '2026-02-10' AND created_at < '2026-02-11';
-- Only events_2026_02 is scanned
```

Pruning only works if the query filters on the partition key in a way the optimizer understands. Wrapping the key in a function, like `WHERE DATE(created_at) = ...`, can stop it. PostgreSQL can also prune at execution time, when values come from parameters or joins.

#### 396: What is the difference between partitioning and sharding?

**Partitioning** splits a table into pieces inside one database server. **Sharding** splits data across several servers, each holding a part of the data (a shard).

Sharding lets you scale writes and storage beyond one machine, but makes many things harder: queries across shards, joins, transactions that touch several shards, rebalancing, and unique constraints across shards. Tools like Citus (PostgreSQL) and Vitess (MySQL), and distributed databases like CockroachDB, YugabyteDB, TiDB and Spanner handle much of this for you.

#### 397: What is database replication, and what is the difference between synchronous and asynchronous replication?

Replication copies data from a primary server to one or more replicas, for high availability, read scaling or backups.

- **Asynchronous**: the primary commits without waiting for replicas. Fast, but if the primary crashes, the last few transactions may not have reached the replica.
- **Synchronous**: the primary waits for at least one replica to confirm before the commit returns. No data loss on failover, but every commit is slower, and if the replica is unavailable writes can stall.

PostgreSQL uses WAL (write-ahead log) streaming. MySQL uses binlog replication, with semi-synchronous mode as a middle option. SQL Server has Always On availability groups.

#### 398: What is replication lag and how does it affect applications?

Replication lag is the delay between a change on the primary and when it shows up on a replica. If your app writes to the primary and immediately reads from a replica, the user may not see their own change.

Ways to handle it:

- Read your own writes from the primary for a short time after writing.
- Track the position (LSN/GTID) of the write and wait until the replica has caught up.
- Send only reads that can tolerate staleness (reports, search) to replicas.
- Monitor lag and remove a replica from the pool if it falls too far behind.

#### 399: What is the difference between vertical and horizontal scaling for databases?

- **Vertical scaling (scale up)**: a bigger server with more CPU, RAM and faster disks. Simple, no code changes, but there's a limit and it gets expensive.
- **Horizontal scaling (scale out)**: more servers. Read replicas spread reads easily. Spreading writes needs sharding or a distributed database.

The usual order is: tune queries and indexes, scale up, add read replicas and caching, then partition, and shard only when nothing else is enough.

#### 400: Why is connection pooling important?

Opening a database connection is expensive. In PostgreSQL each connection is a separate operating system process using several megabytes of memory. Hundreds of app instances each opening many connections can overload the server even when most connections are idle.

A pool keeps a small number of connections open and shares them between requests. Pools can live in the app (HikariCP, the pool in your driver) or in a separate proxy (PgBouncer, ProxySQL, RDS Proxy).

PgBouncer in transaction mode gives a connection to a client only for one transaction. Session features like temporary tables, session-level advisory locks and `SET` commands don't work as expected in that mode. Recent PgBouncer versions do support prepared statements in transaction mode.

#### 401: How do you archive or remove old data from a very large table?

- **With partitioning**: detach or drop old partitions. It's almost instant and creates no dead rows.
  ```sql
  ALTER TABLE events DETACH PARTITION events_2024_01;   -- PostgreSQL (add CONCURRENTLY to avoid blocking)
  DROP TABLE events_2024_01;
  ```
- **Without partitioning**: copy old rows to an archive table and delete them in small batches (question 286), with pauses between batches to keep replication lag low.
- Export old data to cheap storage, like Parquet files in object storage, if it's rarely queried.

Plan data retention when designing the table. Adding partitioning later to a huge table is much harder.

#### 402: When does denormalization make sense for performance?

When reads are much more frequent than writes and the joins or aggregations are expensive. Examples:

- Keeping `order_count` on the customers table instead of counting each time.
- Copying `customer_name` into an orders reporting table.
- Summary tables for dashboards.

The cost is that you now have the same data in two places and must keep it in sync with triggers, application code or scheduled jobs. Materialized views are a more controlled form of denormalization.

#### 403: What is the difference between OLTP and OLAP?

|          | OLTP                                   | OLAP                                              |
| -------- | -------------------------------------- | ------------------------------------------------- |
| Purpose  | Day-to-day transactions                | Analysis and reporting                            |
| Queries  | Short, touch few rows, many per second | Long, scan millions of rows                       |
| Writes   | Constant small inserts and updates     | Bulk loads                                        |
| Schema   | Normalized                             | Often star schema, denormalized                   |
| Storage  | Row-oriented                           | Usually column-oriented                           |
| Examples | PostgreSQL, MySQL, SQL Server          | Snowflake, BigQuery, ClickHouse, Redshift, DuckDB |

Running heavy analytics on the OLTP database can hurt the app, so data is usually copied into a separate analytics system.

#### 404: Why are columnar databases faster for analytics?

- A query reads only the columns it needs, not entire rows.
- Values in one column are similar, so they compress very well, often 5 to 10 times. Less data means less I/O.
- Engines process batches of values at a time (vectorized execution), which uses the CPU efficiently.
- They keep min and max values per block, so whole blocks can be skipped.

The downside is that updating or inserting single rows is slow, so they're a bad fit for OLTP.

#### 405: What does the CAP theorem say, and how does it apply to distributed SQL databases?

CAP says that when a network partition happens, a distributed system has to choose between consistency (every read sees the latest write) and availability (every request gets a response). You can't fully have both during a partition.

Distributed SQL databases like Spanner, CockroachDB and YugabyteDB choose consistency. They use consensus protocols (Paxos or Raft) so a majority of replicas must agree on each write. If a region can't reach the majority, it stops accepting writes instead of returning stale or conflicting data. The PACELC extension adds that even without partitions, there's a trade-off between latency and consistency, which is why cross-region writes in these systems are slower.

### Procedures, Functions and Triggers

#### 406: What is the difference between a stored procedure and a function?

|                                       | Function                                                       | Stored procedure                                             |
| ------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------ |
| Returns                               | A value or a table                                             | Nothing required (can have output parameters or result sets) |
| Used in a query                       | Yes, `SELECT my_func(x)`                                       | No, called with `CALL` or `EXEC`                             |
| Can change data                       | Depends. SQL Server functions can't. PostgreSQL functions can. | Yes                                                          |
| Transaction control (`COMMIT` inside) | No                                                             | Yes in PostgreSQL 11+, SQL Server, Oracle, MySQL             |

Use functions for calculations you want inside queries. Use procedures for multi-step operations and batch jobs.

#### 407: How do you create a function?

```sql
-- PostgreSQL (SQL language)
CREATE OR REPLACE FUNCTION order_total(p_order_id INT)
RETURNS NUMERIC
LANGUAGE sql
STABLE
AS $$
    SELECT COALESCE(SUM(quantity * unit_price), 0)
    FROM order_items
    WHERE order_id = p_order_id;
$$;

SELECT id, order_total(id) FROM orders;

-- SQL Server
CREATE OR ALTER FUNCTION dbo.order_total (@order_id INT)
RETURNS DECIMAL(12, 2)
AS
BEGIN
    RETURN (SELECT COALESCE(SUM(quantity * unit_price), 0)
            FROM order_items WHERE order_id = @order_id);
END;
```

Calling a scalar function for each row can be slow, because it may run a separate query per row. SQL Server 2019+ can inline simple scalar functions, and PostgreSQL can inline simple SQL functions.

#### 408: How do you write a stored procedure with transaction control?

```sql
-- PostgreSQL 11+
CREATE OR REPLACE PROCEDURE archive_old_orders(p_before DATE)
LANGUAGE plpgsql
AS $$
DECLARE
    v_rows INT;
BEGIN
    LOOP
        WITH moved AS (
            DELETE FROM orders
            WHERE id IN (SELECT id FROM orders WHERE order_date < p_before LIMIT 5000)
            RETURNING *
        )
        INSERT INTO orders_archive SELECT * FROM moved;

        GET DIAGNOSTICS v_rows = ROW_COUNT;
        COMMIT;                -- commit each batch
        EXIT WHEN v_rows = 0;
    END LOOP;
END;
$$;

CALL archive_old_orders(DATE '2024-01-01');
```

`COMMIT` inside a procedure only works when the procedure is called outside an explicit transaction block.

#### 409: What is a trigger, and what kinds are there?

A trigger is code that runs automatically when something happens to a table.

- **Timing**: `BEFORE` (can change or reject the row), `AFTER` (sees the final row), `INSTEAD OF` (for views).
- **Event**: `INSERT`, `UPDATE`, `DELETE`, and `TRUNCATE` in PostgreSQL.
- **Level**: `FOR EACH ROW` (once per changed row) or `FOR EACH STATEMENT` (once per statement).

SQL Server only has statement-level `AFTER` and `INSTEAD OF` triggers, which see all changed rows through the `inserted` and `deleted` pseudo-tables. MySQL only has row-level triggers. Many databases also have DDL or event triggers for schema changes.

#### 410: How do you write an audit trigger?

```sql
-- PostgreSQL
CREATE TABLE salary_audit (
    employee_id INT,
    old_salary  NUMERIC,
    new_salary  NUMERIC,
    changed_by  TEXT        DEFAULT current_user,
    changed_at  TIMESTAMPTZ DEFAULT now()
);

CREATE OR REPLACE FUNCTION log_salary_change() RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO salary_audit (employee_id, old_salary, new_salary)
    VALUES (OLD.id, OLD.salary, NEW.salary);
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_salary_audit
AFTER UPDATE OF salary ON employees
FOR EACH ROW
WHEN (OLD.salary IS DISTINCT FROM NEW.salary)
EXECUTE FUNCTION log_salary_change();
```

```sql
-- SQL Server: handles many rows at once through inserted/deleted
CREATE OR ALTER TRIGGER trg_salary_audit ON employees
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO salary_audit (employee_id, old_salary, new_salary)
    SELECT d.id, d.salary, i.salary
    FROM inserted i
    JOIN deleted d ON d.id = i.id
    WHERE i.salary <> d.salary;
END;
```

A common SQL Server mistake is writing a trigger that assumes only one row changed, for example `SELECT @id = id FROM inserted`.

#### 411: What is an INSTEAD OF trigger?

It replaces the original action. It's mostly used to make complex views updatable.

```sql
-- SQL Server
CREATE VIEW customer_orders AS
SELECT c.id AS customer_id, c.name, o.id AS order_id, o.total
FROM customers c JOIN orders o ON o.customer_id = c.id;
GO

CREATE TRIGGER trg_customer_orders_delete ON customer_orders
INSTEAD OF DELETE
AS
BEGIN
    DELETE FROM orders WHERE id IN (SELECT order_id FROM deleted);
END;
```

Now `DELETE FROM customer_orders WHERE order_id = 5` deletes the order but keeps the customer.

#### 412: What are the downsides of triggers?

- **Hidden logic**: someone reading the app code doesn't see that an insert also updates three other tables.
- **Performance**: row-level triggers add work to every row, and bulk operations can become very slow.
- **Chains**: triggers that fire other triggers are hard to debug.
- **Harder testing and migrations**.
- **Bulk loads** may skip triggers (some bulk tools don't fire them by default).

Triggers are a good fit for auditing, keeping `updated_at` columns current, and enforcing rules that constraints can't express. For business workflows, application code or queued jobs are usually clearer.

#### 413: What is dynamic SQL, and how do you write it safely?

Dynamic SQL is SQL text built and run at runtime, for example when the table name or the list of columns isn't known in advance. The danger is SQL injection if user input is pasted into the text.

```sql
-- PostgreSQL: format() with %I for identifiers and USING for values
EXECUTE format('SELECT count(*) FROM %I WHERE status = $1', p_table_name)
USING p_status
INTO v_count;

-- SQL Server: QUOTENAME for identifiers, sp_executesql parameters for values
DECLARE @sql NVARCHAR(MAX) =
    N'SELECT COUNT(*) FROM ' + QUOTENAME(@table_name) + N' WHERE status = @status';
EXEC sp_executesql @sql, N'@status VARCHAR(20)', @status = @status;
```

Rules: never concatenate values into the text, pass them as parameters. Quote identifiers with the database's quoting function. Better still, check identifiers against a fixed allow-list.

#### 414: What is a cursor, and why are cursors often discouraged?

A cursor lets you process a query result one row at a time, like a loop.

```sql
-- SQL Server
DECLARE @id INT;
DECLARE c CURSOR LOCAL FAST_FORWARD FOR SELECT id FROM orders WHERE status = 'new';
OPEN c;
FETCH NEXT FROM c INTO @id;
WHILE @@FETCH_STATUS = 0
BEGIN
    EXEC process_order @id;
    FETCH NEXT FROM c INTO @id;
END;
CLOSE c;
DEALLOCATE c;
```

Databases are built for set-based operations. One `UPDATE` touching 100,000 rows is usually much faster than 100,000 single-row updates in a loop. Cursors are fine when you really have to do something per row that can't be done in a set, like calling a procedure per row or batching work. Client-side cursors are also useful for streaming large results to an application without loading everything into memory.

#### 415: How do you handle errors in stored procedures?

```sql
-- SQL Server
BEGIN TRY
    BEGIN TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
    COMMIT;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK;
    THROW;   -- re-raise the original error
END CATCH;

-- PostgreSQL PL/pgSQL
BEGIN
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
EXCEPTION
    WHEN check_violation THEN
        RAISE NOTICE 'Not enough money';
        RAISE;
END;
```

In SQL Server, also use `SET XACT_ABORT ON` so most errors roll back the whole transaction automatically. In PostgreSQL, a block with an `EXCEPTION` clause creates a savepoint, which has some cost, so don't wrap every small step in one inside a hot loop.

#### 416: What is a table-valued function?

A function that returns a set of rows, which you can use in `FROM` like a table.

```sql
-- PostgreSQL
CREATE FUNCTION customer_orders(p_customer_id INT)
RETURNS TABLE (order_id INT, order_date DATE, total NUMERIC)
LANGUAGE sql STABLE
AS $$
    SELECT id, order_date, total FROM orders WHERE customer_id = p_customer_id;
$$;

SELECT * FROM customer_orders(42);

-- SQL Server inline table-valued function
CREATE FUNCTION dbo.customer_orders (@customer_id INT)
RETURNS TABLE
AS RETURN (
    SELECT id AS order_id, order_date, total FROM orders WHERE customer_id = @customer_id
);
```

In SQL Server, inline table-valued functions (a single `SELECT`) are expanded into the calling query like a view and perform well. Multi-statement table-valued functions are much harder for the optimizer and are often slow.

#### 417: What do IMMUTABLE, STABLE and VOLATILE mean for PostgreSQL functions?

They tell the optimizer how the function behaves:

- **IMMUTABLE**: always the same result for the same arguments, never reads the database. Example: `lower(text)`. Can be used in indexes and can be evaluated once at planning time.
- **STABLE**: same result within one statement, can read the database. Example: a lookup function, or `now()`.
- **VOLATILE** (default): can return different results on every call, or have side effects. Example: `random()`, or functions that insert data.

Marking a function wrongly can cause wrong results (an `IMMUTABLE` function that actually reads a table) or slow queries (a `VOLATILE` function that could have been optimized). Other databases have similar ideas, like `DETERMINISTIC` in MySQL and Oracle.

#### 418: What are system-versioned temporal tables?

Temporal tables (from SQL:2011) keep the full history of each row automatically. Every change saves the old version with the time period it was valid, and you can query the table as it was at any past moment.

```sql
-- SQL Server
CREATE TABLE products (
    id         INT PRIMARY KEY,
    price      DECIMAL(10, 2),
    valid_from DATETIME2 GENERATED ALWAYS AS ROW START,
    valid_to   DATETIME2 GENERATED ALWAYS AS ROW END,
    PERIOD FOR SYSTEM_TIME (valid_from, valid_to)
) WITH (SYSTEM_VERSIONING = ON (HISTORY_TABLE = dbo.products_history));

SELECT * FROM products FOR SYSTEM_TIME AS OF '2026-01-01T00:00:00';
```

SQL Server, MariaDB, DB2 and Oracle (Flashback) support this. PostgreSQL doesn't have system versioning built in, but PostgreSQL 18 added application-time temporal constraints: `PRIMARY KEY` and `UNIQUE` with `WITHOUT OVERLAPS`, and foreign keys with `PERIOD`.

### Database Design and Normalization

#### 419: What is normalization and why do it?

Normalization is organizing tables so each fact is stored in one place. It removes duplicate data and prevents update problems:

- **Update anomaly**: a customer's address is stored on every order, and you update some copies but not others.
- **Insert anomaly**: you can't add a product until someone orders it, because products only exist in the orders table.
- **Delete anomaly**: deleting the last order for a customer also deletes everything you knew about that customer.

The normal forms (1NF, 2NF, 3NF, BCNF and higher) are steps toward this. Most OLTP databases aim for 3NF and denormalize only where there's a clear reason.

#### 420: What is First Normal Form (1NF)?

A table is in 1NF when:

- Each column holds a single (atomic) value, with no lists in one cell.
- There are no repeating groups of columns like `phone1`, `phone2`, `phone3`.
- Each row is unique (has a key).

```text
Not 1NF:
| customer_id | phones                 |
| 1           | 555-1111, 555-2222     |

1NF:
| customer_id | phone    |
| 1           | 555-1111 |
| 1           | 555-2222 |
```

Modern types like arrays and JSON blur this line a little. Storing a list in a column is fine if you always treat it as one value. It becomes a problem when you need to search, join or constrain individual items.

#### 421: What is Second Normal Form (2NF)?

A table is in 2NF when it's in 1NF and no non-key column depends on only part of a composite key.

```text
order_items(order_id, product_id, quantity, product_name)
Key: (order_id, product_id)
```

`product_name` depends only on `product_id`, not on the whole key. So the same name repeats on every order line. The fix is to move it to a `products` table. 2NF only matters for tables with composite keys.

#### 422: What is Third Normal Form (3NF)?

A table is in 3NF when it's in 2NF and no non-key column depends on another non-key column (no transitive dependencies).

```text
employees(id, name, department_id, department_name)
```

`department_name` depends on `department_id`, which depends on `id`. If a department is renamed, you have to update many employee rows. Move `department_name` to a `departments` table.

A short way to remember 1NF to 3NF: every non-key column depends on "the key, the whole key, and nothing but the key".

#### 423: What is Boyce-Codd Normal Form (BCNF)?

BCNF is a slightly stricter 3NF: for every dependency `X -> Y`, `X` must be a candidate key. It only differs from 3NF when a table has several overlapping candidate keys.

Example: `(student, course, teacher)`, where each teacher teaches exactly one course and a student takes each course from one teacher. `teacher -> course`, but `teacher` isn't a key. The table is in 3NF but not BCNF. Splitting it into `(teacher, course)` and `(student, teacher)` fixes it, though some rules then become harder to enforce with constraints alone.

#### 424: What are 4NF and 5NF?

- **4NF** deals with multi-valued dependencies. If an employee has several skills and several languages, and these have nothing to do with each other, storing them in one table `(employee, skill, language)` forces you to store every combination. Split into `(employee, skill)` and `(employee, language)`.
- **5NF** (project-join normal form) deals with cases where a table can only be split into three or more tables without losing information, and not into two.

You rarely see these in interviews beyond knowing what they are. In practice, a clean 3NF/BCNF design with sensible many-to-many tables usually covers them.

#### 425: When is it OK to denormalize?

- Reads are far more common than writes and the joins or aggregates are measurably expensive.
- Data warehouses and reporting tables, where star schemas are normal.
- Storing a historical value on purpose. For example, `order_items.unit_price` should keep the price at the time of purchase, even though `products.price` exists. That's not really duplication, since it's a different fact.
- Caching computed values, like a counter, that would be expensive to compute every time.

Always have a plan for keeping copies in sync, and measure before and after.

#### 426: What is the difference between a star schema and a snowflake schema?

Both are used in data warehouses.

- **Star schema**: a central **fact table** (events or transactions with numbers like quantity and amount) surrounded by **dimension tables** (date, customer, product, store). Dimensions are denormalized, so each is one wide table. Queries are simple with one join per dimension.
- **Snowflake schema**: dimensions are normalized into sub-tables, like product to category to department. Less duplication, but more joins.

```sql
SELECT d.year, p.category, SUM(f.amount) AS revenue
FROM fact_sales f
JOIN dim_date d    ON d.date_key = f.date_key
JOIN dim_product p ON p.product_key = f.product_key
GROUP BY d.year, p.category;
```

Star schemas are more common because they're easier to query and columnar engines handle wide tables well.

#### 427: What are slowly changing dimensions (SCD)?

They're ways to handle dimension data that changes over time, like a customer moving to another city.

- **Type 0**: never change the value.
- **Type 1**: overwrite the old value. No history.
- **Type 2**: add a new row for each change, with `valid_from`, `valid_to` and an `is_current` flag. Full history. Facts point to the version that was current when they happened.
- **Type 3**: keep a "previous value" column. Limited history.

```sql
-- Type 2: close the old row and add a new one
UPDATE dim_customer
SET valid_to = CURRENT_DATE, is_current = FALSE
WHERE customer_id = 42 AND is_current;

INSERT INTO dim_customer (customer_id, city, valid_from, valid_to, is_current)
VALUES (42, 'Berlin', CURRENT_DATE, DATE '9999-12-31', TRUE);
```

Type 2 needs a surrogate key (like `customer_key`) because the business key `customer_id` repeats.

#### 428: How do you model a many-to-many relationship?

Use a junction table (also called a link, bridge or associative table) with foreign keys to both sides.

```sql
CREATE TABLE students (id INT PRIMARY KEY, name TEXT);
CREATE TABLE courses  (id INT PRIMARY KEY, title TEXT);

CREATE TABLE enrollments (
    student_id  INT REFERENCES students(id) ON DELETE CASCADE,
    course_id   INT REFERENCES courses(id)  ON DELETE CASCADE,
    enrolled_at DATE NOT NULL DEFAULT CURRENT_DATE,
    grade       CHAR(2),
    PRIMARY KEY (student_id, course_id)
);

CREATE INDEX idx_enrollments_course ON enrollments (course_id);
```

The composite primary key prevents duplicate links and serves lookups by student. The extra index serves lookups by course. The junction table is also the right place for attributes of the relationship, like `grade`.

#### 429: What are the pros and cons of soft deletes?

A soft delete marks a row as deleted (`deleted_at` timestamp or `is_deleted` flag) instead of removing it.

Pros:

- Easy to undo.
- Keeps history and references intact.

Cons:

- Every query must remember `WHERE deleted_at IS NULL`. Forgetting it is a common bug.
- Unique constraints get harder (a deleted user's email blocks a new signup). Use a partial unique index: `CREATE UNIQUE INDEX ... ON users (email) WHERE deleted_at IS NULL`.
- Foreign keys don't know about soft deletes.
- Tables grow forever, and privacy laws like GDPR may require real deletion.

Alternatives include moving deleted rows to an archive table, or using temporal tables to keep history.

#### 430: What is the Entity-Attribute-Value (EAV) pattern and why is it usually avoided?

EAV stores data as rows of `(entity_id, attribute_name, value)` instead of real columns.

```text
| entity_id | attribute | value  |
| 1         | color     | red    |
| 1         | weight    | 2.5    |
| 1         | in_stock  | true   |
```

It looks flexible, but:

- All values are strings, so you lose types and constraints.
- Getting one entity back as a row needs a pivot with many joins or conditional aggregation.
- You can't use `NOT NULL`, `CHECK` or foreign keys on attributes.
- Queries are slow and complicated.

Today a JSON column usually does the same job better: it's flexible, can be indexed and has validation functions. EAV still appears in some systems, like medical records and older e-commerce platforms.

### Security

#### 431: What is SQL injection?

SQL injection happens when user input is put directly into SQL text, so the user can change what the query does.

```python
# Vulnerable
query = "SELECT * FROM users WHERE email = '" + email + "' AND password_hash = '" + pw + "'"
```

If someone enters `' OR '1'='1' --` as the email, the query becomes:

```sql
SELECT * FROM users WHERE email = '' OR '1'='1' --' AND password_hash = '...'
```

The condition is always true and the rest is commented out. Attackers can read data, change it, or sometimes run commands on the server. It's still one of the most common security problems in web applications.

#### 432: How do you prevent SQL injection?

1. **Use parameterized queries** (prepared statements) for every value. The database treats the parameter as data, never as SQL.
   ```python
   cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
   ```
2. **Never build identifiers from user input** without checking them against an allow-list (for example, allowed sort columns).
3. **Use the least privileges**: the app's database user shouldn't be able to drop tables or read tables it doesn't need.
4. **Be careful with dynamic SQL inside stored procedures**: it can be injected too (question 413).
5. ORMs help, but raw-SQL features in ORMs can still be misused.

Escaping input by hand is fragile and shouldn't be your main defense.

#### 433: How do GRANT and REVOKE work?

```sql
GRANT SELECT, INSERT, UPDATE ON orders TO app_user;
GRANT SELECT ON ALL TABLES IN SCHEMA reporting TO analyst;   -- PostgreSQL
GRANT EXECUTE ON FUNCTION order_total(INT) TO app_user;

REVOKE UPDATE ON orders FROM app_user;

-- Column-level permissions
GRANT SELECT (id, name, country) ON customers TO support_team;
```

`WITH GRANT OPTION` lets the user pass the permission on to others. In PostgreSQL, `GRANT ... ON ALL TABLES` only covers existing tables. Use `ALTER DEFAULT PRIVILEGES` for tables created later.

#### 434: What are roles and why use them?

A role is a named group of permissions. You grant permissions to roles and then give roles to users, instead of managing permissions for each user.

```sql
CREATE ROLE readonly;
GRANT CONNECT ON DATABASE shop TO readonly;
GRANT USAGE ON SCHEMA public TO readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;

CREATE ROLE anna LOGIN PASSWORD '...';
GRANT readonly TO anna;
```

When someone changes teams, you change their roles, not dozens of grants. PostgreSQL 14+ has predefined roles like `pg_read_all_data` and `pg_write_all_data`.

#### 435: What is row-level security?

Row-level security (RLS) filters which rows a user can see or change, based on a policy, enforced by the database itself.

```sql
-- PostgreSQL: each tenant only sees its own rows
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON invoices
    USING (tenant_id = current_setting('app.tenant_id')::int);

-- The app sets this per connection or transaction
SET app.tenant_id = '42';
SELECT * FROM invoices;   -- only tenant 42's invoices
```

SQL Server has security policies with predicate functions, and Oracle has Virtual Private Database. RLS is common in multi-tenant SaaS apps. Note that table owners and superusers bypass RLS in PostgreSQL unless you use `FORCE ROW LEVEL SECURITY`.

#### 436: What does the principle of least privilege mean for databases?

Give every user and application only the permissions they need, and nothing more.

- The application user can read and write its tables, but can't create or drop objects. Migrations run with a separate user.
- Reporting users get read-only access, ideally on a replica.
- Nobody uses the superuser account (`postgres`, `root`, `sa`) for daily work.
- Separate accounts per service, so you can track and revoke access.
- Use views or column grants to hide sensitive columns like salaries or personal data.

This limits the damage from a bug, a leaked password or SQL injection.

#### 437: How do you protect sensitive data stored in a database?

- **Encryption in transit**: require TLS for all connections.
- **Encryption at rest**: encrypt the data files and backups (Transparent Data Encryption in SQL Server and Oracle, MySQL InnoDB encryption, or disk-level encryption).
- **Column-level encryption** for very sensitive fields, like SQL Server Always Encrypted or encrypting in the application, so even DBAs can't read the plain values.
- **Hash passwords** with a slow algorithm like bcrypt or Argon2 in the application. Never store them as plain text or reversible encryption.
- **Masking**: show partial values to support staff (SQL Server Dynamic Data Masking, or views).
- **Keep personal data to a minimum** and delete it when no longer needed.
- **Protect backups** as carefully as the live database.

#### 438: How do you audit who changed or read data?

- **Built-in auditing**: SQL Server Audit, Oracle Unified Auditing, MySQL Enterprise Audit, and the `pgaudit` extension for PostgreSQL. These log statements by user, object and type.
- **Triggers** that write changes to audit tables (question 410).
- **Change Data Capture (CDC)**: read changes from the transaction log (SQL Server CDC, Debezium for PostgreSQL and MySQL) and send them to an audit store.
- **Temporal tables** to keep every past version of rows.
- Store audit logs where the audited users can't change them.

Logging every `SELECT` on a busy system produces a lot of data, so audit the sensitive tables and actions that actually matter.

### Practical Query Problems

#### 439: How do you find customers who bought every product in a category?

This is called relational division. Count the distinct products each customer bought in the category and compare with the total number of products in that category.

```sql
SELECT o.customer_id
FROM orders o
JOIN order_items i ON i.order_id = o.id
JOIN products p    ON p.id = i.product_id
WHERE p.category = 'Accessories'
GROUP BY o.customer_id
HAVING COUNT(DISTINCT p.id) = (
    SELECT COUNT(*) FROM products WHERE category = 'Accessories'
);
```

Another way uses double `NOT EXISTS`: "customers for whom there is no product in the category that they haven't bought."

```sql
SELECT c.id
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM products p
    WHERE p.category = 'Accessories'
      AND NOT EXISTS (
          SELECT 1
          FROM orders o
          JOIN order_items i ON i.order_id = o.id
          WHERE o.customer_id = c.id AND i.product_id = p.id
      )
);
```

#### 440: How do you find the department with the highest total salary, including ties?

```sql
WITH dept_totals AS (
    SELECT d.name, SUM(e.salary) AS total_salary
    FROM departments d
    JOIN employees e ON e.department_id = d.id
    GROUP BY d.name
)
SELECT name, total_salary
FROM dept_totals
WHERE total_salary = (SELECT MAX(total_salary) FROM dept_totals);
```

Using `ORDER BY ... FETCH FIRST 1 ROW ONLY` would hide ties, unless you add `WITH TIES`.

#### 441: How do you calculate month-over-month revenue change, including months with no revenue?

```sql
WITH months AS (
    SELECT generate_series(DATE '2026-01-01', DATE '2026-12-01', INTERVAL '1 month')::date AS month
),
revenue AS (
    SELECT DATE_TRUNC('month', order_date)::date AS month, SUM(total) AS revenue
    FROM orders
    WHERE status <> 'cancelled'
    GROUP BY 1
),
filled AS (
    SELECT m.month, COALESCE(r.revenue, 0) AS revenue
    FROM months m
    LEFT JOIN revenue r ON r.month = m.month
)
SELECT month, revenue,
       LAG(revenue) OVER (ORDER BY month) AS prev_month,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
             / NULLIF(LAG(revenue) OVER (ORDER BY month), 0), 1) AS change_pct
FROM filled
ORDER BY month;
```

Without filling in empty months, `LAG` would compare March with January when February had no sales.

#### 442: How do you find overlapping bookings?

Two ranges `[start1, end1)` and `[start2, end2)` overlap when `start1 < end2 AND start2 < end1`.

```sql
SELECT a.id AS booking_a, b.id AS booking_b, a.room_id
FROM bookings a
JOIN bookings b
  ON a.room_id = b.room_id
 AND a.id < b.id                 -- each pair once, and not with itself
 AND a.check_in  < b.check_out
 AND b.check_in  < a.check_out;
```

In PostgreSQL, range types make this shorter (`a.during && b.during`), and an exclusion constraint can stop overlaps from being inserted at all (question 321). PostgreSQL 18 also supports `PRIMARY KEY (room_id, during WITHOUT OVERLAPS)`.

#### 443: How do you merge overlapping time ranges into continuous periods?

Sort the ranges, start a new group when a range starts after the furthest end seen so far, then take the min and max of each group.

```sql
WITH ordered AS (
    SELECT user_id, start_time, end_time,
           MAX(end_time) OVER (
               PARTITION BY user_id ORDER BY start_time, end_time
               ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
           ) AS prev_max_end
    FROM sessions
),
flagged AS (
    SELECT *,
           CASE WHEN prev_max_end IS NULL OR start_time > prev_max_end THEN 1 ELSE 0 END AS new_group
    FROM ordered
),
grouped AS (
    SELECT *,
           SUM(new_group) OVER (PARTITION BY user_id ORDER BY start_time, end_time) AS grp
    FROM flagged
)
SELECT user_id, MIN(start_time) AS period_start, MAX(end_time) AS period_end
FROM grouped
GROUP BY user_id, grp
ORDER BY user_id, period_start;
```

Using the running `MAX(end_time)`, rather than just the previous row's end, handles a long range that covers several shorter ones after it. Use `>=` instead of `>` if ranges that only touch should stay separate.

#### 444: How do you calculate a running account balance?

```sql
SELECT account_id, created_at, type, amount,
       SUM(CASE WHEN type = 'credit' THEN amount ELSE -amount END)
           OVER (PARTITION BY account_id
                 ORDER BY created_at, id
                 ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS balance
FROM transactions
ORDER BY account_id, created_at, id;
```

`id` in the `ORDER BY` breaks ties between transactions with the same timestamp, so the result is the same every time. To find accounts that ever went negative, wrap it and filter on `balance < 0`.

#### 445: How do you find each customer's first order and what they bought in it?

```sql
WITH first_orders AS (
    SELECT *
    FROM (
        SELECT o.*,
               ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date, id) AS rn
        FROM orders o
    ) t
    WHERE rn = 1
)
SELECT f.customer_id, f.id AS first_order_id, f.order_date, p.name AS product, i.quantity
FROM first_orders f
JOIN order_items i ON i.order_id = f.id
JOIN products p    ON p.id = i.product_id
ORDER BY f.customer_id;
```

Filtering to the first order before joining the items keeps the row-numbering step small.

#### 446: How do you get the top 2 products by revenue in each category for the last 30 days?

```sql
WITH revenue AS (
    SELECT p.category, p.id, p.name,
           SUM(i.quantity * i.unit_price) AS revenue
    FROM order_items i
    JOIN orders o   ON o.id = i.order_id
    JOIN products p ON p.id = i.product_id
    WHERE o.order_date >= CURRENT_DATE - INTERVAL '30' DAY
      AND o.status <> 'cancelled'
    GROUP BY p.category, p.id, p.name
),
ranked AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY category ORDER BY revenue DESC) AS rnk
    FROM revenue
)
SELECT category, name, revenue, rnk
FROM ranked
WHERE rnk <= 2
ORDER BY category, rnk;
```

The window function runs on top of the grouped result. Notice the date condition is written so an index on `order_date` can be used.

#### 447: How do you calculate the percentage of late deliveries per month?

```sql
SELECT DATE_TRUNC('month', order_date) AS month,
       COUNT(*) AS delivered,
       COUNT(*) FILTER (WHERE delivered_at > promised_at) AS late,
       ROUND(100.0 * COUNT(*) FILTER (WHERE delivered_at > promised_at) / COUNT(*), 1) AS late_pct
FROM shipments
WHERE delivered_at IS NOT NULL
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;
```

Without `FILTER`, use `SUM(CASE WHEN delivered_at > promised_at THEN 1 ELSE 0 END)`. Note the `100.0`: with `100`, integer division in PostgreSQL or SQL Server would round most percentages down to 0.

#### 448: How do you find duplicate customers whose emails differ only in case or spaces?

```sql
SELECT LOWER(TRIM(email)) AS normalized_email,
       COUNT(*)           AS cnt,
       STRING_AGG(CAST(id AS VARCHAR(20)), ', ') AS customer_ids
FROM customers
GROUP BY LOWER(TRIM(email))
HAVING COUNT(*) > 1;
```

To stop it from happening again, add a unique index on the normalized value:

```sql
CREATE UNIQUE INDEX uq_customers_email_normalized ON customers (LOWER(TRIM(email)));
```

In PostgreSQL you could also use the `citext` type or a case-insensitive collation.

#### 449: How do you find 3 or more consecutive free seats in a row?

```sql
-- seats(row_letter, seat_no, is_free)
WITH free AS (
    SELECT row_letter, seat_no,
           seat_no - ROW_NUMBER() OVER (PARTITION BY row_letter ORDER BY seat_no) AS grp
    FROM seats
    WHERE is_free
)
SELECT row_letter,
       MIN(seat_no) AS first_seat,
       MAX(seat_no) AS last_seat,
       COUNT(*)     AS free_in_block
FROM free
GROUP BY row_letter, grp
HAVING COUNT(*) >= 3
ORDER BY row_letter, first_seat;
```

This is the gaps and islands pattern again (question 353). Consecutive free seats have the same `seat_no - row_number` value, so grouping by it gives each block of free seats.

#### 450: How do you suggest friends based on mutual friends?

Assume `friendships(user_id, friend_id)` stores each friendship in both directions.

```sql
SELECT f2.friend_id     AS suggested_user,
       COUNT(*)         AS mutual_friends
FROM friendships f1
JOIN friendships f2
  ON f2.user_id = f1.friend_id          -- friends of my friends
WHERE f1.user_id = 42
  AND f2.friend_id <> 42                -- not me
  AND NOT EXISTS (                      -- not already my friend
      SELECT 1 FROM friendships x
      WHERE x.user_id = 42 AND x.friend_id = f2.friend_id
  )
GROUP BY f2.friend_id
ORDER BY mutual_friends DESC, suggested_user
FETCH FIRST 10 ROWS ONLY;
```

With a primary key on `(user_id, friend_id)`, every lookup here uses the index. If friendships are stored only once (with `user_id < friend_id`), first build a view with both directions using `UNION ALL`.

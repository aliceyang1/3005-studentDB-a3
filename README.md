# COMP 3005 Assignment 3 - Question 1

### Description

Name: Alice Yang
Student number: 101277355

Created for COMP3005 Assignment 3 Question 1 - Winter 2024

This is a simple Python3 application that manages student records from a PostgreSQL database.

[Video Demo Link](https://youtu.be/jMeabRbVaAY)

### PostgreSQL Database setup

- Open pgAdmin 4
- Create a new database called `school_db` in pgAdmin 4
- Using the query tool for the newly created database, open and run the included `a3setup.sql` file in pgAdmin 4
- This creates the `students` table and inserts the initial data

Run the `SELECT * FROM students` in the query tool to test that database is set up correctly

- Should see 3 students 

### Install Python dependencies

Install [psycopg 3](https://pypi.org/project/psycopg/)


### How to run

1. Update the connection setting variable values in the code to match your PostgreSQL database connection information.

2. Run the following command in the terminal:

```bash
python3 a3q1.py
```

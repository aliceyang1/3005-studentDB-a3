# COMP 3005 Assignment 3 - Question 1

### Description

Name: Alice Yang
Student number: 101277355

This is a simple Python3 application that manages student records from a PostgreSQL database.

[Video Link](https://youtu.be/EO-nJoHwOF8)

### PostgreSQL Database setup

- Open pgAdmin 4
- Create a new database called `school_db` in pgAdmin 4
- Using the query tool for the newly created database, open and run:
- `CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);`

- `INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
`
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

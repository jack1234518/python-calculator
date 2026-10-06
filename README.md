# Python Calculator

A command-line calculator built with Python that performs basic arithmetic operations, validates user input, handles errors, and maintains persistent calculation history.

## Features

* Addition, subtraction, multiplication, and division
* Input validation for invalid numbers
* Operation validation
* Division-by-zero error handling
* Calculation history
* Persistent history stored in a local file
* View calculation history
* Clear calculation history
* Interactive calculator menu
* Continuous calculations until the user chooses to exit

## Technologies Used

* **Python 3**
* **Git**
* **GitHub**
* Python file handling
* Python functions
* Exception handling
* Loops and conditional statements

## Project Structure

```text
python-calculator/
│
├── calculator.py
├── README.md
├── .gitignore
└── learning_tests/
    └── Personal practice files
```

The `learning_tests` folder contains files created while learning and testing individual Python concepts. It is excluded from Git tracking using `.gitignore`.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/jack1234518/python-calculator.git
```

### 2. Open the project folder

```bash
cd python-calculator
```

### 3. Run the calculator

```bash
python calculator.py
```

## Example

```text
Calculator Menu:
1. Continue
2. View Calculation History
3. Clear History
4. Exit

Choose an option (1-4): 1

Enter first number: 43
Enter operation (+, -, *, /): +
Enter second number: 34

Result: 77
```

## Error Handling

The calculator handles common invalid inputs, including:

* Invalid numbers
* Invalid mathematical operations
* Division by zero

For example:

```text
Enter second number: 0

Error: Cannot divide by zero.
Calculation was not saved to history.
```

## What I Learned

This project was built as a practical Python learning project. It helped me practice:

* Variables and data types
* User input
* Conditional statements
* `while` loops
* Functions
* Lists
* String formatting
* Exception handling
* File handling
* Reading and writing files
* Git and GitHub
* Organizing a Python project

## Future Improvements

Possible improvements for future versions include:

* Support for decimal numbers
* More mathematical operations
* A graphical user interface
* Unit tests
* Better project architecture
* Packaging the calculator as an installable application

## Author

**Jack**

IT Student | Aspiring Software Engineer / AI Engineer

---

⭐ This project is part of my journey toward becoming a professional software engineer.

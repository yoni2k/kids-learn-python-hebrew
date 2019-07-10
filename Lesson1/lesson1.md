# High level
In this lesson we'll learn the very basics to write first programs with tests in PyTest.

Unlike following lessons, in order to teach enough basics, this lesson is very large, requires a few hours of frontal explanation, and a few hours of independent work with help.

# Topics
- Python files
- Strings
- Numbers/Integers
- Math operations
- Functions
- Working with tests

## Python files
Files end with ".py"

## Strings
- What is a string, what they are needed for
- Escape character \, needed for example for representing ', or " in the middle of string
- Newline \n
- Different ways to present:  "", '', """""".
  - """""" for multiline
  - having both '', "" helps not to use escape characters when using " in the middle of string for example
- "+" operator

## Numbers/integers, math operations
 - Integer - difference between string and integer
 - Math operators: +, -, *, /
 - () - useful for:
   - Clarity of understanding order of operations
   - When order of operations not according to preset order 

## Functions
- Why use functions:
  - The caller didn't implement
  - Reuse from numerous places
  - Easier to read code
- Declaration
- Use
- Passing parameters (one or many), declaration and use of parameters
- Returning value
- Functions must be defined before used
- Whitespace is important in Python, show by example of methods how something is part of method or not based on whitespace

## Print
print() function, how to use it

## Working with tests
 - Test methods in PyTest start with "test_" prefix, and by convension follow with function name being tested
 - How to run a PyTest tests, see if passed.
 - Compares expected and actual results 
 - If failed, see what was the expected and actual value
 - How to rerun all tests in the lesson
 - How to rerun specific test
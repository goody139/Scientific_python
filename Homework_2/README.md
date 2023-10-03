# Homework 02

The deadline of this homework is on **Tuesday, 19th of April, 23:59:00 UTC+2**.

## Overview

The purpose of this homework is mainly to test the basic python skills such as Data types, methods, loops, etc.

## Cloning the repository

via command line

```bash
git clone <url>
```

or via Github Desktop application

```
File > Clone a Repository
```

In order to complete this assignment, you need to implement the following functions:

### 1. Check if the number is prime

Your task for this exercise is to implement the function `is_prime` in the `prime.py` file.

It is supposed to take any natural number and return a `Boolean` according to if the number is prime or not.

| Input | Output    |
| :---- | :-------- |
| `1`   | **False** |
| `2`   | **True**  |
| `3`   | **True**  |

### 2. Multiply every character with the given number

Your task for this exercise is to implement the function `repeat` in the `repeat.py` file.

It is supposed to take a string and a number, and multiply every character with the given number. The output must be a string and in a correct order.

| Input           | Output                                     |
| :-------------- | :----------------------------------------- |
| `a, 1`          | `a`                                        |
| `now, 2`        | `nnooww`                                   |
| `osnabrueck, 4` | `oooossssnnnnaaaabbbbrrrruuuueeeecccckkkk` |

## Submitting this homework

- Make sure that you test your code before submitting it. You can run the tests either by using Testing in Visual Studio Code or by running `pytest` command.

- After your code passes the tests, push your code by running the following commands or via Github Desktop Application:

```bash
git add .
```

```bash
git commit -m "Commit message"
```

```bash
git push
```

- Congratulations! If you have verified that your commit has passed the online autograde, then you have successfully completed your homework and you will see a green tick on your repo.

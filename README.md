# Nondeterministic finite automata

## Table of contents

- [About](#about)
- [Preview](#preview)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Using git](#using-git)
  - [Downloading sorce code](#downloading-sorce-code)
- [How to use](#how-to-use)
  - [Samples available](#samples-available)
- [Project structure](#project-structure)

## About

This project is a result of praticial work for the Computer Theory class at UFPI. This application is a simple terminal program that consists of converting non-determinist finite automatons with epsilon transition into non-deterministic finite automatons and do the recognition of a word in it.

## Preview

## Installation

### Requirements

[Python](https://www.python.org) - Python is a programming language that lets you work more quickly and integrate your systems more effectively.

### Using Git

Clone this project using command below:

```bash
  git clone https://github.com/CassianoJunior/nondeterministic-finite-automaton
```

Open your terminal inside the created folder and run:

```bash
  python main.py
```

### Downloading sorce code

You can also download zipped source code. After downloading and unzipping, just open your terminal inside the folder and run:

```bash
  python main.py
```

## How to use

You can insert your own NFA instance, just create a txt file and describe your automaton in the following format:

```bash
q0,q1,q2           # all states, comma separated
a,b,c              # alphabet symbols, comma separated
5                  # amount of transition functions
(q0,a):(q1)        # transition function. Format: (state, symbol):(reached states, comma separated)
(q1,epsilon):(q0)
(q1,b):(q2)
(q1,c):(q2)
(q2,epsilon):(q0)
q0                 # initial state
(q0)               # final states in parentheses, each separated by a comma
```

### Samples available

Also, you can try some samples included in the program, they are described below:

1. Words whose third-to-last symbol is 1 | RE: (0+1)*1(0+1)(0+1)
2. Words that starts with 0 and ends with 1 | RE: 0(0+1)*1
3. Words that starts with 001 | RE: 001(0+1)*
4. Words witch contains 110 as substring | RE: (0+1)*110(0+1)*
5. Words that start and end with the same symbol | RE: 0(0+1)*0 | 1(0+1)*1 | 0 | 1
6. Words that contain a or bb or ccc as a suffix | RE: (a+b+c)*a | (a+b+c)*bb | (a+b+c)*ccc
7. Only accepts aa or bb | RE: aa | bb
8. Words where b and c only appear after the occurrence of a | RE: (a(b+c)*)* | e
9. Words that contain a as suffix or ba as prefix | RE: (a+b)*a | ba(a+b)*

## Project structure

```bash
  $PROJECT_ROOT
    ├── examples.py  # All samples
    ├── main.py      # Entry point
    ├── nfa.py       # NFA Class
    └── sample.txt   # Sample in txt format
```

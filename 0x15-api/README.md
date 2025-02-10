# Project: API Data Management with Python

## Overview

In the transition from old-school system administration to the modern SRE role, scripting in Bash, while useful, often falls short in efficiency and manageability compared to more advanced programming languages. This project aims to leverage Python for system administration tasks, specifically focusing on interacting with an API to manage employee data. By accessing employee data through an API, we'll demonstrate how to organize and export this data into various formats, moving beyond the limitations of Bash scripting for complex tasks.

## Background Context

Traditional system administrators primarily relied on Bash scripting for automating tasks. However, as the field evolves, there's a significant shift towards using more versatile programming languages. SREs (Site Reliability Engineers) blend software engineering with system management, employing languages like Python for scripting. This project exemplifies such an approach by using Python to interact with APIs, a common method for accessing and manipulating data in modern web services and microservices.

## Learning Objectives
By the end of this project, learners should be able to explain:

- The limitations of Bash scripting for complex tasks
- The basics of APIs and how they facilitate interaction with applications
- The principles of REST APIs and microservices
- The formats of CSV and JSON for data representation
- Best practices in Python coding style as per PEP8
- The significance of naming conventions in Python for packages, modules, classes, variables, functions, and constants

## Resources

- [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [What is an API?](https://www.webopedia.com/definitions/api/)
- [Understanding REST APIs](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [Introduction to Microservices](https://smartbear.com/learn/api-design/microservices/)
- [PEP8 - Python Style Guide](https://peps.python.org/pep-0008/)

## Requirements

- Use of vi, vim, emacs as editors
- Code should be compatible with Python 3.8.5 on Ubuntu 20.04 LTS
- Adherence to PEP8 styling (version 2.8.*)
- Inclusion of a README.md at the project root
- Organization of imports in alphabetical order
- Documentation for all modules
- Use of __name__ == "__main__" to ensure code does not execute on import
- Use of dict.get() for safe dictionary key access

## Tasks
0. Gather Data from an API: Script to access employee data via API.
1. Export to CSV: Export employee data to a CSV file.
2. Export to JSON: Convert and export employee data to JSON format.
3. Dictionary of List of Dictionaries: Organize employee data into a specific data structure for advanced manipulation.

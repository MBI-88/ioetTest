# Title of the project

This project is an application for ACME payments.

# Requirements

Python 3.11
Additional libraries not required.

# Facility

Clone the repository, keep github instructions.

# Use

Run the main file with .txt file path exmple: 

### python main.py employee_data.txt

### python -m unittest tests/test_acme.py -v

# Description

This project is an application that dynamically calculates the payment that the ACME company has to make to its workers. Through a file with a txt extension, the information is sent to the application and it returns the result in the console.


# Metodologies and algorithms

The project is divided into 3 directories, making it easy to scale, clean, and understand. The acme directory contains the operation logic for payments and the company-supplied structure for making these payments. In the decorators directory, there is the logic for the validation of the type of file that can be supplied to the application. The decorator has the task of validating the entered path and file extension before they are passed to the function that transforms the data into an array. Once they are validated, the information is passed to the ACME class.


# License
This project is licensed under the open source.
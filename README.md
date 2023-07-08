# Football Ticketing System
In this assignment, you will become familiar with file operations, lists, and dictionaries as you implement a real-world Football ticketing system. You will also gain hands-on experience designing data structures to store related data for categories and seats in the Şükrü Saraçoğlu Stadium, and perform operations such as selling or canceling tickets. The seating arrangement for football fans consists of categories, and ticket transactions are made within these categories. There are two types of categories: category-1 (Marathon Tribune) and category-2 (Back-Goal Tribune). Each category can be further divided into subcategories (e.g., category-1A, category-1B, etc.).

You are expected to design and implement a console-based basic Football ticketing system that reads an input file line by line and executes each command with its arguments. The input file name should be "input.txt" and it must be located in the same folder as your Python file. A list of available commands is provided in Section 3. The stadium allows the creation of an arbitrary number of categories with a rectangular layout, where the columns are named with a sequence of 0, 1, 2, 3, ..., and the rows are named with the English alphabet characters (A, B, C, ..., Z). This layout is illustrated in Figure 2. The side of each category facing the football ground corresponds to the columns, while the other side corresponds to the rows. As a result, the number of rows in any category is limited to 26.

In our stadium, there are three types of fares for each seat: student, full pay, and season ticket. The price for student and full pay tickets is $10 and $20, respectively. The price for a season ticket is $250. Your program should output the results of the operations to both the console and a text file. The output file should be named "output.txt" and it should be created in the same folder as your Python file.

# Setup

1-Firstly, download or clone the project to your computer.

2-In the project directory, create an input file named "input.txt". This file will contain the commands and arguments, each on a separate line.

3-In your Python file, create an output file named "output.txt". This file will be used to store the program's operation results.

# Usage

The project is a command-line-based Football ticketing system application. The code reads the "input.txt" file, processes each line, and executes the commands and arguments. Below is a list of available commands:

CREATECATEGORY:This command is used to create a category consisting of rows and columns for football fans.

SELLTICKET:This command is used to sell tickets to football fans from the category.

CANCELTICKET:This command is used to cancel the tickets that football fans have purchased from the category they have determined.

BALANCE:This command shows the number of tickets sold by type of football fans in a certain category and the total revenue in that category.

SHOWCATEGORY:This command is used to visualize the current layout of the specified category with their seats and their actual status.

# Output

The program outputs the results of the operations to both the console and the "output.txt" file. The "output.txt" file is created in the same directory as the Python file. Each operation result is displayed in the "output.txt" file.

# Notes

1-The number of rows in a category is limited to a maximum of 26. Seat numbers are represented using the letters of the English alphabet (A, B, C, ...).

2-The ticket prices are $10 for student tickets, $20 for full pay tickets, and $250 for season tickets.

3-Commands and arguments should be separated by spaces.


[AS_3_FALL_22.pdf](https://github.com/SerhatAkbulut1/Assignment-2/files/11971566/AS_3_FALL_22.pdf)

[output.txt](https://github.com/SerhatAkbulut1/Assignment-2/files/11971576/output.txt)

[input.txt](https://github.com/SerhatAkbulut1/Assignment-2/files/11971574/input.txt)

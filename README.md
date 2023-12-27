# SANTA'S LIST

#### Description: This is a simple Python application that allows you to create Santa's List by entering information about people, including their name, age, gift, and whether they have been naughty or nice. The application uses the tabulate library to display the Santa's List in a formatted table.


### Design Choices

This program is designed with the diligent elf in mind. As an elf, your responsibility includes updating Santa's record-keeping. With this application, you can input the names, ages, gifts, and naughty/nice status of children who send their lists to the North Pole.


### How to Use

Run the program: python santas_list.py
Enter information for each person (name, age, gift, naughty or nice).
Type 'Exit' when you are done entering people.
Choose whether to generate Santa's List.
View the generated Santa's List.

### Dependencies

Python 3
tabulate library (pip install tabulate)

### Code Structure

Person class: Represents a person with attributes like name, age, gift, and naughty/nice status.

List class: Manages the Santa's List and provides methods to add people to the list.

add_to_list function: Adds a list of Person instances to the Santa's List.

is_nice function: Updates the Santa's List for nice people.

is_naughty function: Updates the Santa's List for naughty people.

main function: The main execution of the program, where users input information and generate the Santa's List.
Notes

To exit the program at any point, type 'Exit'.
The application uses emoji ("\U0001F4A9") to represent naughty people in the list.
The tabulate library is used to format the Santa's List table.


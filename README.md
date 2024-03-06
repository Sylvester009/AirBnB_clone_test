# Airbnb Clone Console

## Project Description

This is a project that creates a command-line interface (CLI) for managing Airbnb-like objects, It provides functionalities to create, update, and delete objects, as well as storing and persisting data to a JSON file.

## Command Interpreter Description

The command interpreter allows users to interact with the Airbnb clone application through a command-line interface. Users can execute various commands to perform operations on Airbnb objects, such as creating new listings, updating user information

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the `console.py` file using Python.

### How to Use the Command Interpreter

Once the command interpreter is running, you can use the following commands to interact with the application:

- `create <class>`: Create a new instance of the specified class.
- `show <class> <id>`: Display details of a specific instance.
- `update <class> <id> <attribute> "<value>"`: Update the specified attribute of an instance.
- `destroy <class> <id>`: Delete a specific instance.
- `all <class>`: Display all instances of a given class.
- `quit` or `EOF`: Exit the command interpreter.

### Examples

Here are some examples of how to use the command interpreter:

```bash
$ create User
$ update User 1 name "Samuel Alex"
$ create Listing
$ show Listing 1
$ all User
$ destroy User 1
$ quit


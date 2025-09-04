## About the program

This COBOL program simulates an account management system. This program will involve multiple COBOL source files and perform various operations like crediting, debiting, viewing the balance, and even exiting the program. Here’s how you its structured:

- Main Program (main.cob): The main program will handle the user interface and call subprograms for different operations.
- Operations Program (operations.cob): This program will handle the actual operations like credit, debit, and view balance.
- Data Storage Program (data.cob): This program will manage the storage of the account balance.

## Steps to Compile and Run the Program

- Option 1: Install COBOL compiler on MaC
If you don't already have a COBOL compiler, you'll need to install one. Common COBOL compiler is GnuCOBOL: An open-source COBOL compiler. To Install , use brew:

```bash
brew install gnucobol 
```

- Option 2: Open the terminal in the GitHub codespace or Ubuntu Linux system and run the following command to install the COBOL compiler:

```bash
sudo apt-get update && \
sudo apt-get install gnucobol
```

reference: [gnucobol](https://formulae.brew.sh/formula/gnucobol)

- Compile, link and create executable: Link the object files together to create the final executable:

```bash
cobc -x main.cob operations.cob data.cob -o accountsystem
```

- Run the Program: Run the executable to start the account management system:

```bash
./accountsystem
```

## Program Interaction Example

- Program starts with user input menu

```bash
--------------------------------
Account Management System
1. View Balance
2. Credit Account
3. Debit Account
4. Exit
--------------------------------
Enter your choice (1-4): 
```

- User Chooses to View Balance:

```bash
Current balance: 1000.00
```

- User Chooses to Credit:

```bash
Enter credit amount:
200.00
Amount credited. New balance: 1200.00
```

- User Chooses to Debit:

```bash
Enter debit amount:
300.00
Amount debited. New balance: 900.00
```

- User Chooses to Exit:

```bash
Exiting the program. Goodbye!
```

## Explanation

- main.cob: This is the main interface where users select operations.
- operations.cob: It handles specific operations such as viewing, crediting, and debiting the account balance.
- data.cob: This program acts as a simple data storage, handling reading and writing of the balance.

This multi-file structure introduces modularity, making it easier to manage and extend the program. Each file has a clear responsibility, and the program flow is driven by user interaction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

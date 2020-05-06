# 9GA Command Line Python
This is a command line application for a flash card database that the user can add to, read from, update, and delete

## Getting Started
Repo Github: https://github.com/digitalfences/9GACommandLine-Python

Application wil run with any virtual environment friendly to Python3.
Basic app will run with the argument flash, as well as accepting --start or --create flags with a quantity argument
```
Ex. python3 app.py flash
    python3 app.py flash --create 1
    python3 app.py flash --start 20
```
The app will create a database on your computer for storing flashcards and preload it with a seed file in main.py automatically as long as the main.py file is present on your machine. The main file can be edited and run at any time to quickly re-seed the database.

Both the create and start functions are available in the main app, the tags are just shortcuts that bypass the inital menu. the passed quantity will be the amount of cards you would like to create or be tested on for that session.

The create function will ask you to input a new card to the database by entering front and back text for it.

The session function will present you with the front of the card and ask you for the back. Scoring is manual so exact answers are not required. 

### Prerequisites

A computer, an internet connection, and a dream.

```
Ex. MacBook Pro, Azer laptop, Dell desktop etc.
```

### Installing

Through github repository:

```
1. Clone this repo to your computer
2. Make sure you have python of 3.6 or later and the most recent version of Postgres CLI
3. Go into the lib dir
4. Run `psql < settings.sql`
   - This command will create a postgreSQL database named flashcardapp on your computer
5. Run `pipenv install'
   - This command will install the dependencies packages   
6. Run `pipenv shell` to Start your virtual environment
7. Run `python3 app.py flash` to experience this command line application
```

### Read

Start method will read a quantity of cards from the database. The cards are sorted to present you with cards you have answered correctly the fewest times first. If a quantity greater than the number of cards in the database is provided, it will simply show all cards. 

### Create

Create method adds a quantity of new cards to the database after user enters front and back text for the cards

### Update and Delete

As questions are answered, the number of correct or incorrect answers on a card are recorded in the database. This uses peewee's update functionality. 

Deletion is implemented subtly in the start session method. When a question is being answered, the user can enter 'q' to leave the method or 'd' to delete it. The user will be prompted to confirm their intention on either of these cases. If re-affirmed, the user can delete the card from the database and continue their session. 
## Versioning

1.0

## Authors

* **Galen Emanuel** - *Full Development* - [digitalfences](https://github.com/digitalfences)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Shimin Rao for his example readme https://github.com/life2free/ContactBook_CommandLine
* GA for project guidance and instruction

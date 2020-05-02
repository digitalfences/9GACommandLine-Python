import argparse
from peewee import *

db = PostgresqlDatabase('flashcardapp', user='postgres', password='', host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class FlashCard(BaseModel):
    front_text  = CharField()
    back_text = CharField()
    times_correct = IntegerField()
    times_incorrect = IntegerField()

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

#This function will trigger an addition of a card to the database
def create(args):
    quantity = int(args)
    for i in range(quantity):
        newfront_text = input("Please add cards front text")
        newback_text = input("Please add cards back text")
        db.create_tables([FlashCard])
        newCard = FlashCard(front_text=newfront_text, back_text=newback_text,times_correct=0,times_incorrect=0)
        newCard.save()
        print("Card created")
#This function will bring back a number of cards from the database to test the user
def session(args):
    print(f"beginning practice session with {args} cards")
    cards = FlashCard.select()
    cards = sorted(cards, key=lambda i: i.times_incorrect,reverse=True)
    for i in range(int(args)):
        print(f"CARD {i}:\n")
        print(cards[i].front_text)
        solution = input("TYPE SOLUTION HERE:")
        print(f"YOUR ANSWER WAS: {solution}\n")
        print(f"CARD ANSWER WAS: {cards[i].back_text}")
        endState = ''
        while endState != 'y' and endState != 'n':
            endState = input("WERE YOU CORRECT? (y/n):")
            if endState == 'y':
                print("")
            elif endState != 'y' and endState != 'n':
                print('ERROR. TYPE y OR n WITHOUT ADDITIONAL MARK:')
            else:
                print("")

        
def main(args):
    choice = "-1" 
    if args.start:
        session(args.quantity)
    elif args.create:
        create(args.quantity)
    else:
        while choice != "3":
            print("Welcome to the FlashCard app.\n")
            choice = input("Please pick an option by typing its number.\n[1]CREATE new card\n[2]START new practice\n[3]QUIT\n")
            if choice == "1":
                number = input("How many cards would you like to create: ")
                create(number)
            elif choice =="2":
                number = input("How many prompts would you like to answer: ")
                session(number)
            elif choice == "3":
                print("exiting...")
                break
            else: 
                print("error. please type a number when prompted.")

main_parser = subparsers.add_parser('flash')
main_parser.add_argument('quantity',nargs='?', default='1')
main_parser.add_argument('--start', action='store_true')
main_parser.add_argument('--create', action='store_true')
main_parser.set_defaults(func=main)

if __name__ == '__main__':
    args = parser.parse_args() 
    try:
        func = args.func
    except AttributeError:
        parser.error("too few arguments")
    func(args) # call the default function
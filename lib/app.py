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
    for (range(args.quantity)):
        newfront_text = input("Please add cards front text")
        newback_text = input("Please add cards back text")
        db.create_tables([FlashCard])
        newCard = FlashCard(front_text=newfront_text, back_text=newback_text,times_correct=0,times_incorrect=0)
        newCard.save()
        print("Card created")
#This function will bring back a number of cards from the database to test the user
def session(args):
    print(args.quantity)
def main(args):
    choice = 0 
    if args.start:
        session(args)
    elif args.create:
        create()
    else:
        while choice != "3":
            print("Welcome to the FlashCard app.\n")
            choice = input("Please pick an option by typing its number.\n[1]CREATE new card\n[2]START new practice\n[3]QUIT\n")
            if choice == "1":
                create()
            elif choice =="2":
                session(args)
            elif choice == "3":
                print("exiting...")
                break
            else: 
                print("error. please type a number when prompted.")

main_parser = subparsers.add_parser('flash')
main_parser.add_argument('quantity')
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
import argparse
from main import seedTables 
from peewee import *
#This established database connection
db = PostgresqlDatabase('flashcardapp', user='postgres', password='', host='localhost', port=5432)
db.connect()
#These are the models we use for the flashcards
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
    cards = FlashCard.select()
    cards = sorted(cards, key=lambda i: i.times_correct)
    if int(args) > len (cards):
        args = str(len(cards))
    correct = 0
    print(f"beginning practice session with {args} cards")
    for i in range(int(args)):
        print(f"CARD {i+1}:\n")
        print(cards[i].front_text)
        solution = input("TYPE SOLUTION HERE:")
        print(f"YOUR ANSWER WAS: {solution}\n")
        print(f"CARD ANSWER WAS: {cards[i].back_text}")
        endState = ''
        while endState != 'y' and endState != 'n':
            endState = input("WERE YOU CORRECT? (y/n):")
            if endState == 'y':
                correct += 1
                print("Updating card tally...\n")
                cards[i].times_correct += 1
                cards[i].save()
                print(f"You have gotten this question correct {cards[i].times_correct} times\n")
                print(f"You have gotten this question incorrect {cards[i].times_incorrect} times\n")
            elif endState == 'q':
                choice = input("Are you sure you want to quit this session?(y/n)")
                if choice == 'y':
                    print(f"Session ended. {correct} correct out of {args}")
                    print("exiting...")
                    return
                elif choice == 'n':
                    print("exit not authenticated")
                else:
                    print("error authenticating exit")
                break
            elif endState == 'd':
                choice = input("Are you sure you want to delete this card?(y/n)")
                if choice == 'y':
                    target = FlashCard.get(FlashCard.id == cards[i].id)
                    target.delete_instance
                    print("card deleted")
                elif choice == 'n':
                    print("delete not authenticated")
                else:
                    print("error authenticating delete")
            elif endState != 'y' and endState != 'n':
                print('ERROR. TYPE y OR n WITHOUT ADDITIONAL MARK. You can also type q to leave the session or d to delete the current card:')
            else:
                print("Updating card tally...\n")
                cards[i].times_incorrect += 1
                cards[i].save()
                print(f"You have gotten this question correct {cards[i].times_correct} times\n")
                print(f"You have gotten this question incorrect {cards[i].times_incorrect} times\n")
    print(f"Session ended. {correct} correct out of {args}")
        
def main(args):
    if len(FlashCard.select()) == 0:
        seedTables()
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
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


db.create_tables([FlashCard])
testCard = FlashCard(front_text='Who made you?', back_text='Galen Emanuel',times_correct=0,times_incorrect=0)
testCard.save()
testcard2 = FlashCard.get(FlashCard.front_text == 'Who made you?')
print(testcard2)
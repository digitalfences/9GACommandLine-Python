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


db.drop_tables([FlashCard])
db.create_tables([FlashCard])
testCard1 = FlashCard(front_text='Who created the python language?', back_text='Guido van Rossum',times_correct=0,times_incorrect=0)
testCard1.save()
testcard2 = FlashCard(front_text='What\'s the capital of Brazil?', back_text='Brasilia',times_correct=0,times_incorrect=0)
testcard2.save()
testcard3 = FlashCard(front_text='What speak they in netherlands', back_text='Dutchlish',times_correct=0,times_incorrect=0)
testcard3.save()
testcard4 = FlashCard(front_text='What is the national song of canada?', back_text='O... canada',times_correct=0,times_incorrect=0)
testcard4.save()
testcard5 = FlashCard(front_text='How many acres is the amazon rainforest?', back_text='1.4 billion',times_correct=0,times_incorrect=0)
testcard5.save()
testcard6 = FlashCard(front_text='When was the nation of haiti established?', back_text='1804',times_correct=0,times_incorrect=0)
testcard6.save()
testcard7 = FlashCard(front_text='What is the earths largest continent?', back_text='Asia',times_correct=0,times_incorrect=0)
testcard7.save()
testcard8 = FlashCard(front_text='What river runs through baghdad?', back_text='Tigris',times_correct=0,times_incorrect=0)
testcard8.save()
testcard9 = FlashCard(front_text='What country has hella lakes?', back_text='Canada',times_correct=0,times_incorrect=0)
testcard9.save()
testcard10 = FlashCard(front_text='What percentage of the nile river is located in Egypt?', back_text='22%',times_correct=0,times_incorrect=0)
testcard10.save()
testcard11 = FlashCard(front_text='What is the driest place on earth?', back_text='McMurdo, Antartica',times_correct=0,times_incorrect=0)
testcard11.save()
testcard12 = FlashCard(front_text='What is an indigenous language of peru?', back_text='Quechua',times_correct=0,times_incorrect=0)
testcard12.save()
testcard13 = FlashCard(front_text='Which African nation has the most pyramids?', back_text='Sudan',times_correct=0,times_incorrect=0)
testcard13.save()
testcard14 = FlashCard(front_text='What is the oldest city in the world?', back_text='Damascus',times_correct=0,times_incorrect=0)
testcard14.save()
testcard15 = FlashCard(front_text='What US state has the most active volcanoes?', back_text='Alaska',times_correct=0,times_incorrect=0)
testcard15.save()
testcard16 = FlashCard(front_text='What is the largest country in the Arabian Peninsula?', back_text='Saudi Arabida',times_correct=0,times_incorrect=0)
testcard16.save()
testcard17 = FlashCard(front_text='What country has the most coastline?', back_text='Canada',times_correct=0,times_incorrect=0)
testcard17.save()
testcard18 = FlashCard(front_text='Where is kangaroo island, and its treasure?', back_text='Australia',times_correct=0,times_incorrect=0)
testcard18.save()
testcard19 = FlashCard(front_text='What is the tallest mountain in the world?', back_text='Mount Everest',times_correct=0,times_incorrect=0)
testcard19.save()
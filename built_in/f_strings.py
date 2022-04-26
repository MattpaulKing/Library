from datetime import datetime

first_name = 'matt'
last_name = 'king'

sentence = f'my name is {first_name} {last_name}'
print(sentence)
#prints 'my name is matt king'

person = {'name': 'Jen', 'age': 23}

sentence_2 = f"my name is {person['name']} and i am {person['age']} years old"
print(sentence_2)
# my name is Jen and i am 23 years old

birthday = datetime(1994, 9, 1)

sentence_3 = f"{first_name} {last_name} has a birthday on {birthday: %B %d, %Y}"
print(sentence_3)
# matt king has a birthday on September 01, 1994
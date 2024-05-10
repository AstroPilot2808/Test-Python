import random

def coin_toss():
    return random.choice(["heads","tails"])
    
def random_number():
    return random.randint(1, 10)

cards = ["jack" , "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card) 
    
import itertools
from countpos import countpos
import random

def twentyfour(lst):
    for nums in itertools.permutations(lst):
        for ops in itertools.product('+-*/', repeat=3):
            
            form1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)  
            form2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)  
           
            for form in [form1, form2]: 
                try:
                    if abs(eval(form) - 24.0) < 1e-10:   
                        return form
                except ZeroDivisionError: 
                    continue
    
    return "No answer."
    
all_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]

def show_answer(generated_cards):
    
    stopper = False
    
    cards = ",".join(generated_cards)
    cards_list = cards.split(",")
    cards_list = [i.strip() for i in cards_list]
    
    #sorting numbers from letters
    number_list = [int(i) for i in cards_list if i.isdigit()]
    letter_list = [i for i in cards_list if not i.isdigit()]
    
    while "a" in letter_list:
        letter_list.remove("a")
        number_list.append(1)
    
    possibilities = []
    letters = "".join(letter_list)
    
    if letters:
        possibilities = [i + number_list for i in countpos(letters)]
    
    else:
        possibilities = [number_list]
        
    answers = []
    for possibility in possibilities:
        answers.append(twentyfour(possibility))
    if len(answers)>1 and "No answer." in answers:
        while "No answer." in answers:
            answers.remove("No answer.")
    print("Some possibilities:")
    for answer in answers:
        print(answer)
    print("\n----------\n")
    
while True:
    generated_cards = []
    times = 0
    while times < 4:
        index = random.randint(0, 12)
        generated_cards.append(all_cards[index])
        times += 1

    print("Your cards: ")
    print(generated_cards)
    print("\n")
    
    while True:
        user_answer = input("Your answer: \n")
        print("\n")
        if user_answer == "r":
            show_answer(generated_cards)
            break
        elif abs(eval(user_answer)-24.0) < 1e-10:
            print("Correct!\n")
            break
        else:
            print("Wrong answer. Try again or 'r' to reveal correct answer.\n")


    

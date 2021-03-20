import itertools
from countpos import countpos

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

while True:
    stopper = False
    
    cards = input("Enter cards one by one separated by commas.\n")
    print("\n")
    cards_list = cards.split(",")
    cards_list = [i.strip() for i in cards_list]
    
    for i in cards_list:
        if not i.isdigit() and i.lower() != "j" and i.lower() != "q" and i.lower() != "k" and i.lower() != "a":
            stopper = True
            break
            
    if stopper == True:
        print("Enter numbers only.\n")
        continue
    
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
    print("\n")
    

import random
from capitals import states

def states_quizzz():
    random.shuffle(states)
    answers = {
        "tries": 0,
        "correct": 0,
        "incorrect": 0
    }
    
    for state in states:
        correctAnswer = False
        incorrectAnswer = 0
        while(incorrectAnswer!=3 and not correctAnswer):
            state_name = state['name']
            answer = input(f"Type in capital name for the state of {state_name} or 'quit' for exit")
            if answer=="quit":
                print("Sorry to see you go!")
                return
            elif answer == state['capital']:
                print(state['capital'])
                answers['correct'] +=1
                correctAnswer = True
            else:
                incorrectAnswer +=1
                if incorrectAnswer == 3:
                    print(f"You reached 3 incerrect answers threshold, Let's skipt this question. That was {state['capital']}")
                else:
                    print(f"Sorry incorrect answer. Try number {incorrectAnswer}")
    print(f"You finished the game with following results:\nCorrect answers: {answers['correct']}, \nIncorrect answers: {answers['incorrect']}, \nTotal tries: {answers['tries']} ")




states_quizzz()
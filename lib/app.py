'''
Taken from state capitals lab, need to rework to interface with sql models
replay = "y"
print("Welcome to Flash Card memorization\n")
while replay == "y":
    for state in states:
        question = state["name"]
        solution = state["capital"]
        print(f"Name the capital of {question}. Press type 'h' for hint\n")
        answer = 'h'
        while answer == 'h':
            answer = input("Your answer: ")
            if answer == solution:
                print(f"Correct! Answer was {solution}")
                state['correct'] = state['correct'] + 1
                correct = correct+1
                print(f"{correct} out of 50")
                break    
            elif answer == 'h':
                print (f"{solution[0:3]}\n")
            else:
                print(f"Wrong! Answer was {solution}")
                state['incorrect'] = state['incorrect'] + 1
                print(f"{correct} out of 50")
                break
    replay = input("Play again?(y/n)")
    if replay=='n':
        print("exiting...")
    else:
        states = sorted(states, key=lambda i: i['incorrect'],reverse=True)
        '''

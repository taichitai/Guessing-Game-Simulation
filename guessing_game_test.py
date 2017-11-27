import random


"""
Set the variables here.
Comment out one of the different K generation methods to test different scenarios.
"""

lowerLimit = -1000
upperLimit = 1000
k = random.randint(1, 100) #Random K
# k = (upperLimit - lowerLimit) / 2 + lowerLimit #K = mean of lowerLimit and upperLimit
numberOfRuns = 100
guessesPerRun = 100000

def generateScenario():
    """
    Generates Random pairs of A and B without A == B
    """

    Result = "Draw"
    
    while Result == "Draw":
        A = random.randint(lowerLimit, upperLimit)
        B = random.randint(lowerLimit, upperLimit)
        
        if B > A:
            Result = "B"
            
        elif A > B:
            Result = "A"
        
    return (A, B, Result)

def guessScenario(Scenario, Guess):
    """
    Guesses based on k, if K > A, then guesses A is bigger.
    Random guess if K = A.
    Returns True on coreect guesses
    """
    
    if scenario[0] > Guess:
        Answer = "A"
    elif scenario[0] < Guess:
        Answer = "B"
    else:
        if random.randint(0,1):
            Answer = "A"
        else:
            Answer = "B"

    if Scenario[2] == Answer:
        return True
    else:
        return False


"""
Evaluates guesses and scenarios, prints out accuracy per run
"""
runs = 0
while runs < guessesPerRun:
    i = 0
    correct = 0
    wrong = 0
     
    while i < guessesPerRun:
        scenario = generateScenario()
        evaluation = guessScenario(scenario, k)
     
        if evaluation:
            correct += 1
        else:
            wrong += 1
             
        i += 1
     
    print ("Correct: ", correct, "Wrong: ", wrong, "Accuracy: ", correct/i * 100, "%")
    runs += 1

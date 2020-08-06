# 1 - Perform a task
# 2 - Return a value

def greet(name) :
    print(f'Hi {name}')


def get_greeting(name):
    return (f'Hi {name}')

message = get_greeting("Joe Smith")

file = open("testing.txt", "w")
file.write(message)
#
def save_user (**user):
    print(user)
    print()
    for number in user:
        print(f'{number} of the user is {user[number]}')


save_user( SSN = "245-41-9870", name = " John Smith ", age = 25)
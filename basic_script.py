def add_user(users,user):
    users.append(user)
    print("added user: {}".format(user))
    return users

def print_users(users):
    for item in users:
        print(item)

users =['joe','mary','bob']
print("\n\n")

print("******* add a user")
users = add_user(users,'sara')
print("\n")

print("******* print all users")
print_users(users)
print('\n\n')
input("input enter to exit....")
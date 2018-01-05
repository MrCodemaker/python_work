current_users = ['Eric', 'alex', 'ANDRE', 'Jessica', 'Jason', 'james']

new_users = ['jessica', 'roman', 'Isaac', 'james']

for new_user in new_users:
    if new_user in current_users:
        new_user = new_user.lower()
        print("This name is already taken")
    else:
        print("Name available")

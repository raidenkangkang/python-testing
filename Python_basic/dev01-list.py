user_name = input("your name is: ")
user_hero = input("your hero name is: ")
user_age = int(input("your age is: "))
user_hp = 100

#profile of user, if user_name is null, then default to play_01, otherwise take the name from user input
if user_name: ## not null
    user_profile = [user_name, user_hero, user_age, user_hp]
else:
    user_profile = ["play_01", user_hero, user_age, user_hp]

#print all info of user profile
print()
print("user profile information as below: ")
print("Name: ", user_profile[0])
print("Hero name: ",user_profile[1])
print("Age: ", user_profile[2])
print("Initial HP: ", user_profile[3])
#!/usr/bin/env python3

my_favourite_fruits =["Banana","Mango","apple"]

for fruit in my_favourite_fruits:
    print(fruit)

#len number of elements in the list
print(len(my_favourite_fruits))

friends = ["Mwangi","Jane","Albert","Steph","Anita","Paul"]
print(friends)
friends[4] = "Mary"
print(friends)
print("--------------------")
new_friends = friends.copy()
print(new_friends)

new_friends.sort()
new_friends.pop()
print(new_friends)

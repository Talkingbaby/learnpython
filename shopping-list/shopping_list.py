#create list to hold items
shopping_list = []
#print instructions on how to use the app
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
#ask for new items
    new_item = input("+ ")
    #be able to quite the app
    if new_item == 'DONE':
        break
#add new items to list
    shopping_list.append(new_item)
    
#print out the list
print("My list:")
for item in shopping_list:
    print(item)
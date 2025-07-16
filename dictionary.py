#Task-1

dictionary = {'Navya': 90, 'Nisha': 60, 'Mike': 44, 'Pranav': 78}
name = input("Enter the student's name: ")
if name in dictionary:
    print(f"{name}'s marks:",dictionary.get(name))
else:
    print('Student not found.')

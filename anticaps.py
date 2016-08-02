import re


answer = input("Please enter the number of your selection.\n\t1: ALL CAPS\n\t2: no caps\n\t3: First word. Caps only.\n\t4: Capitalize The First Letter In Every Word")

tochange = input("Please enter your editables.\n")

if answer == '1':
    output = tochange.upper()
elif answer == '2':
    output = tochange.lower()
elif answer == '3':
    output = re.compile(r'(?<=[\.\?!]\s)(\w+))
elif answer == '3': 
    output = tochange.title()
    
#print(len(tochange) + " " + len(output))
print("\n\n" + output)

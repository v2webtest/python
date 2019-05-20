print("Starting programme..")

enType: int = int(input("\n\nEnter  program type.. ").strip())
print(enType)
# Checking of Type and printing message
if enType == 1:
    print("-- Type is First.")
elif enType == 2:
    print("-- Type is Second.")
else:
    print("-- Unknown Type!")

print("End of program.")

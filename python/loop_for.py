for letter in "Python":
    print(f"Current letter: {letter}")

fruits = ["Apple","Banana","Grapes","Guava","Pineapple","Oranges","Grapefruit","Kiwi"]
for fruit in fruits:
    print(f"Current fruit is: {fruit}")

for index in range(len(fruits)):
    print(f"[R] Current fruit is: {fruits[index]}")    

for i in range (3,7+1):
    for j in range(1,10+1):
        print(f"{i} X {j} = {i*j}")
    print("--")

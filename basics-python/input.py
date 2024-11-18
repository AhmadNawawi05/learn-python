name = input("Cheers Mate, Whats your name?: ")

print("Hello " + name)

# while True:
#     try:
#          age  = (int(input("How old are you " + name + " ?")))
#         break
# except ValueError:
#    print("it ok if you dont want to tell")

# while True:
#     try:
#         age = int(input("How old are you " + name + " ?"))
#         break
#     except ValueError:
#         print("please fill the question " + name )

max_attemps = 4

for attempt in range(1, max_attemps + 1):
    try:
        age = int(input("How old are you " + name + " ?: "))
        
        if age == 18 :
            print("Hell yeah, I'm " + str(age) + " years old too!")
        elif age >= 19 :
            print("You're older than me by " + str(age - 18) + " years.")
        elif age <= 17 :
            print("You're younger than me by " + str(18 - age) + " years.")
            break
    except ValueError:
        print("Please answer my question.")

else:
    print("You didn't answer my question {} times. its okay if you didn't  want tell that you are a f#cking old man.".format(max_attemps))
        
        
height = float(input("How tall are you ? Please enter in cm: "))

print("that's good if you are " + str(height) + " cm" )
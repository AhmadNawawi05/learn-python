# if statement = blok code yang akan dieksekusi jika kondisinya terpenuhi 

age = int(input("How old are you? : "))

if age == 18 : 
    print ("we at the same age!")
elif age >= 17 :
    print("you old enough")
elif age <= 0 :
    print("you haven't born yet")
else:
    print("you are a litle kiddo")
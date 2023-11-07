# loop control statements = mengubah eksekusi loop dari urutan normalnya

# break    =  digunakan untuk mengakhiri loop sepenuhnya
# continue =  melompat ke iterasi loop berikutnya.
# pass     = tidak melakukan apa pun, bertindak sebagai pengganti

# Break

# while True:
#     name = input("Enter youre name!: ")
#     if name != "":
#         break
    
    
# Continue

# phone_number = "123-456-789"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")


# Pass

for i in range(1, 21) :
    if i == 13 :
        continue
    print(i)
# logical operator (and, or, not) = digunakan untuk memeriksa apakah dua atau lebih pernyataan bersyarat benar

temp = int(input("Whats the temperature outside?"))

# logical operator menggunakan and & or

if temp >=0 and temp <= 30 :
    print("The temperature is look good")
    print("Go out and tuch some grass!")
elif temp < 0 or temp > 30:
    print("The temperature is bad")
    print("It's freezing cold, stay inside!")
    
# logical operator menggunakan not (di kasus ini logika nya di balik)

# if not(temp >=0 and temp <= 30) :
#     print("The temperature is bad")
#     print("It's freezing cold, stay inside!")
# elif not(temp < 0 or temp > 30):
#     print("The temperature is look good")
#     print("Go out and tuch some grass!")
# tuple = collection yang berurutan dan tidak bisa di ubah
#         digunakan untuk menggabungkan data yang related

student = ("Anne Sinclair", 18, "Male")

# print(student.count("Anne Sinclair"))
# print(student.index("Male"))

for i in student:
    print(i)
    
if "Male" in student:
    print("Anne is Male")
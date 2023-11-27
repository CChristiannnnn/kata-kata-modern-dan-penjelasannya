import random
character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang_kata_sandi = int(input("berapa panjang kata sandi?"))
sandi = ""
for i in range(panjang_kata_sandi):
    sandi += random.choice(character)
print("kata sandi yang dihasilkan", sandi)
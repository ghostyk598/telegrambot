import random

def imagedsa1():

    imagedsa = ["wah.jpeg", "what.png", "what312.jpeg"]

    image = random.choice(imagedsa)

    print(image)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
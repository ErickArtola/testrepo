secret_word = input("Hello, feeble human. Guess the secret word and I'll let you go:")

while True:
    if secret_word == "chupacabra":
        break
    else:
        if secret_word != "chupacabra":
            secret_word = input("Feeble human, your soul is mine. But try again if you want to escape: ")
print ("You got lucky!")
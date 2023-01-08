import base64
import codecs

answer = "y" #starts with answer already set to y in order to start the loop

while answer == "y":

    print("Welcome to the Cyber Challange Assistant! Please select which option you would like! \n \n 1 - Base64 Decode \n \n 2 - ROT13 Decryptor \n ")


    decoder = input("Which option would you like? ") #must type choice exactly as it is printed
    print("\n")

    if decoder == "1": #only checks that it is spelled exactly the same as printed above

        codedString = input("Please put your encoded message here: ")
        print("\n")
        decodedString = base64.b64decode(codedString)
        print("your decoded string:" + " " + codecs.decode(decodedString) + "\n")
        print("would you like to decode something else?\n")
        loopAnswer = input("Please answer with y/n: ")
        print("\n")
        if loopAnswer == "y":
            continue
        else:
                exit()
    elif decoder == "2": #only checks that it is spelled exactly the same as printed above
        text = input("Please put your encrypted ROT13 message here: ")
        print("\n")
        rot13 = codecs.encode(text, 'rot_13')
        print("your decoded string:" + " " + rot13 + "\n")
        text = codecs.decode(rot13, 'rot_13')
        print("would you like to decode something else?\n")
        loopAnswer = input("Please answer with y/n: ")
        print("\n")
        if loopAnswer == "y": #only checks that you used y or n. Anything other than y will close it
            continue
        else:
            exit()
    else:
        print("Sorry, I only have the two options at this time.")
        quit()
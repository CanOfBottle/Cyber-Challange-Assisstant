import base64
import codecs

answer = "y" #starts with answer already set to y in order to start the loop

while answer == "y":

    decoder = input("What would you like to decode?(Base64 or ROT13) ") #must type choice exactly as it is printed

    match decoder:
        case "Base64": #only checks that it is spelled exactly the same as printed above
            codedString = input("What where you looking to decode? ")
            decodedString = base64.b64decode(codedString)
            print("your decoded string:" + " " + codecs.decode(decodedString))
            print("would you like to decode something else? ")
            loopAnswer = input("Please answer with y/n: ")
            if loopAnswer == "y":
                continue
            else:
                exit()
        case "ROT13": #only checks that it is spelled exactly the same as printed above
            text = input("Please put your encrypted message here: ")
            rot13 = codecs.encode(text, 'rot_13')
            print("your decoded string:" + " " + rot13)
            text = codecs.decode(rot13, 'rot_13')
            print("would you like to decode something else? ")
            loopAnswer = input("Please answer with y/n: ")
            if loopAnswer == "y": #only checks that you used y or n. Anything other than y will close it
                continue
            else:
                exit()
        case _:
            print("Sorry, I only have the two options at this time.")
            quit()
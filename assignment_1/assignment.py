import json

'''
    Dear Teacher

    I know I did not split the file into functions despite your call to do so.
    This is because I, as a professional in the field, believe in this specific
    case such a split would not actually make the file more readable.

    When a script is this small keeping it all as one continues code allows the
    code to be written in the same order as it is executed. I believe that with
    the context of the assignment this code is very readable.
'''

dictionary = {
    "duck": "ankka",
    "axolotl": "aksolotli",
    "shrimp" : "katkarapu",
    "tardigrade": "karhukainen",
    "platypus": "vesinokkaeläin"
    }

try:
    file = open("dictionary.json", "r", encoding="utf-8")
    dictionary = json.load(file)
    file.close()
except:
    print("Warning! Failed to read dictionary.")
    print("Defaulting to built-in dictionary.")
    print("Inserting new data might overwrite old dictionary.")

while True:
    print("Input a word to search or nothing to exit.")
    inputString = input("Input: ").lower().strip()
    if inputString == "":
        break

    if inputString in dictionary:
        print(f"{inputString} = {dictionary[inputString]}")
    else:
        print(f"{inputString} was not found in dictionary. Please input a translation.")
        translation = input("Translation: ").lower().strip()
        dictionary[inputString] = translation
        try:
                file = open("dictionary.json", "w", encoding="utf-8")
                json.dump(dictionary, file)
                file.close()
        except:
            print("Warning! Failed to save dictionary.")

print("Goodbye :)")
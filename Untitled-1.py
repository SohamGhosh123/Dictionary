import json
from difflib import get_close_matches
d=json.load(open("C:/Users/dipak/Desktop/Dictionary/dictionary.json"))
def translate(w):
    w=w.lower()
    if w in d:
        return d[w]
    elif len(get_close_matches(w,d.keys()))>0:
        yn=input("Did you mean %s instead? Enter yes or no "%get_close_matches(w,d.keys())[0])
        yn=yn.lower()
        if yn=="yes":
            return d[get_close_matches(w,d.keys())[0]]
        elif yn=="no":
            return "The word does not exist"
        else:
            return "we didnt understand"
    else:
        return "Please double check the word"
word=input("Enter the word")
output=translate(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
input("Press enter to exit")
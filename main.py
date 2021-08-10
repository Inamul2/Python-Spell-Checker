from textblob import TextBlob
a = input("Enter the spell : ")
print(f"Incorrect : {a}")
print(f"Correct : {TextBlob(a).correct()}")

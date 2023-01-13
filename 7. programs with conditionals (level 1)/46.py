s = input("Enter String: ").lower()

vowels = ["a","e","i","o","u"]
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

if len(s) == 0:
    print("Empty string")
else:
    for letter in s:
        if letter not in vowels and letter not in consonants:
            print(f"{letter} is not a letter") 
        elif letter not in vowels:
            print(f"{letter} is a consonant")
        else:
            print(f"{letter} is a vowel")

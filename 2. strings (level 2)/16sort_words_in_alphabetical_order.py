s = "Hello World polina ufsdg asfgduav yuwqfgeuywqgd"

my_list = s.split()

new_list = []

for word in my_list:
    # changing to lower
    word = sorted(word.lower())
    print(word)
    #declaring new word variable
    new_word = ""

    for char in word:
        new_word = "{0}{1}".format(new_word, char)
        #print (new_word)
    new_list.append(new_word)
print(new_list)

# printing list into strings

for word in new_list:
    print(word, end = " ")
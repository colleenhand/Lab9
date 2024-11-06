#the author's names are Colleen, Anna, and Victoria
def count_character(word, ch):
    index = 0
    count = 0
    while index < len(word):
        if word[index] == ch:
            count += 1
        index += 1     
    print(count)

count_character("bonobos", "o")

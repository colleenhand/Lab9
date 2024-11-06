#the author's names are Colleen, Anna, and Victoria
def until_dot(word):
    index = 0
    while index < len(word) and word[index] != ".":
        index += 1
    print(word[:index])

until_dot("This is a sentence. This is another.")
until_dot("192.168.200.2")
until_dot("No dots here")

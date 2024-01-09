def alt_string(input_string):
    transformed_string = ""
    for index, char in enumerate(input_string):
        if index % 2 == 0:
            transformed_string += char.upper()
        else:
            transformed_string += char.lower()
    return transformed_string

my_string = "Hello World"
transformed_string = alt_string(my_string)
print(my_string)
print(transformed_string)

new_string = "I am learning to code"
print(new_string)
words = new_string.split() 
word0 = words[0].lower()
word1 = words[1].upper()
word2 = words[2].lower()
word3 = words[3].upper()
word4 = words[4].lower()

new_sentence = ' '.join([word0, word1, word2, word3, word4])
print(new_sentence) 

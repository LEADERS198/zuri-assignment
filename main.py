# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re 



def read_file_content():
    # [assignment] Add your code here
       
    f = open("story.txt", "r")
    content = f.read()
    f.close
    print(content)
    return f.read()


read_file_content()
    #return "Hello World"     



def count_words():
    # [assignment] Add your code here
    read_file_content = ("system.txt")
    word=input("Enter the word you want to count: ")
    splitted_word = word.rsplit()
    result = {}
    for words in splitted_word:
        list_data = ("she")
        word_count = list_data.count(words)
        result[words] = word_count
    print(result)
count_words()    

    
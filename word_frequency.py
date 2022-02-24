from pickle import STOP
from string import punctuation
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
PUNCTUATION =  string.punctuation 
print(PUNCTUATION)

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        text_string = file.read()
        words = text_string.lower()
        stripped_text = " "
        for char in words:
            if not char in PUNCTUATION:
                stripped_text += char
        line_break = stripped_text.replace('\n','').replace('—', ' ')
        squeaky_clean = line_break.split(" ")
        
        

    working_words = {}
    for words in squeaky_clean:
        if words not in STOP_WORDS:
            if words in working_words:
                working_words[words] += 1
            else:
                working_words[words] = 1
    
    
    working_words = sorted(working_words.items(), key=lambda seq: seq[1], reverse = True)
    for words, count in working_words:
        print(words,count)

    



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)



#remove punctuation
#list_of_words.split(" ")


#everything into lowercase



#remove requently used words 'and' etc --create dictionary
# and in list_of_words  then move to unincluded_list


#keep count of how often each word is used (will be using f-strings)
# for words in list_of_words
#(method dictorary- .keys()) += peyton ~sorted function~

#need to sort then format, once they are counting    sorted(a_list, key=len, reverse=True)
import os
import nltk
import string

def tokenize(file_num):
    script_directory = os.path.dirname(os.path.realpath(__file__))

    text_files_directory = os.path.join(script_directory, '..', 'text_files')

    text_file_path = os.path.join(text_files_directory, f'file{file_num}_1a.txt')
    text_file_path_out = os.path.join(text_files_directory, f'file{file_num}_1b.txt')

    with open(text_file_path, 'r') as file:
        content = file.read()
        words = nltk.word_tokenize(content)
    open(text_file_path_out, 'x')
    with open(text_file_path_out, 'w') as file:
        file.write(" ".join(words))
    if(file_num<=5):
        with open(text_file_path_out, 'r') as file:
            content = file.read()
            print(content)

def main():
    for file_number in range(1, 1000):
        tokenize(file_number)

if __name__ == '__main__':
    main()
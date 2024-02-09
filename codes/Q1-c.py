import os
import nltk
from nltk.corpus import stopwords
import string

nltk.download('stopwords')
nltk.download('punkt')

def remove_stopwords(file_num):
    script_directory = os.path.dirname(os.path.realpath(__file__))

    text_files_directory = os.path.join(script_directory, '..', 'text_files')

    text_file_path = os.path.join(text_files_directory, f'file{file_num}_1b.txt')
    text_file_path_out = os.path.join(text_files_directory, f'file{file_num}_1c.txt')

    stop_words = set(stopwords.words('english'))
    filtered_text=""
    with open(text_file_path, 'r') as file:
        content = file.read()
        words = nltk.word_tokenize(content)
        filtered_words = [word.lower() for word in words if (word.lower() not in stop_words) and (word.lower() not in string.punctuation)]
        filtered_text = ' '.join(filtered_words)

    open(text_file_path_out, 'x')
    with open(text_file_path_out, 'w') as file:
        file.write(filtered_text)

    if(file_num<=5):
        with open(text_file_path_out, 'r') as file:
            content = file.read()
            print(content)

def main():
    for file_number in range(1, 1000):
        remove_stopwords(file_number)

if __name__ == '__main__':
    main()
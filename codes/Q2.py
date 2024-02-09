import os
import nltk
from nltk.corpus import stopwords
import string

nltk.download('stopwords')
nltk.download('punkt')

def process_queries(queries, operation, dict):
    if(len(operation)==0):
        print(dict[queries[0]])
        return dict[queries[0]]
    if queries[0] not in dict:
        final=set()
    else:
        final=dict[queries[0]]
    print(queries[0], end=" ")
    for i in range (len(operation)):
        print(operation[i]+" "+queries[i+1], end="")
        final=evaluate_condition(final, queries[i+1], operation[i], dict)
    print()
    return final

def evaluate_condition(final, word2, operation, dict):
    U=set(list(range(1, 1000)))

    if word2 not in dict:
        s=set()
    else:
        s=dict[word2]

    if operation=="AND":
        return final ^ s
    elif operation=="OR":
        return final.union(s)
    elif operation=="AND NOT":
        return final-(final^s)
    else:
        return (U-s).union(final^s)

def invert_ind(file, dict, num):
    content=""
    with open(text_file_path, 'r') as file:
        content = file.read().split()
    for word in content:
        if word not in dict:
            dict[word]=set([num])
        else:
            dict[word].add(num)

if __name__ == "__main__":

    my_dict = {}
    for file_number in range(1, 1000):
        script_directory = os.path.dirname(os.path.realpath(__file__))
        text_files_directory = os.path.join(script_directory, '..', 'text_files')
        text_file_path = os.path.join(text_files_directory, f'file{file_number}_1e.txt')
        invert_ind(text_file_path, my_dict, file_number) 
    import pickle

    with open('index.pkl', 'wb') as f:
        pickle.dump(my_dict, f)

    with open('index.pkl', 'rb') as f:
        loaded_dict= pickle.load(f)

    for key, val in loaded_dict.items():
        print(f"{key}: {val}")    

    N = int(input("Enter the number of queries (N): "))

    for _ in range(N):
        num=0
        files=""
        query = input("Enter query: ")
        operation= input("Enter operation: ")
        stop_words = set(stopwords.words('english'))
        words = nltk.word_tokenize(query)
        filtered_words = [word.lower() for word in words if (word.lower() not in stop_words) and (word.lower() not in string.punctuation)]
        final_set=process_queries(filtered_words, operation.split(', '), loaded_dict)
        print("Names of the documents retrieved for query "+str(_+1)+":", end=" ")
        final_set=list(final_set)
        j=0
        while j < len(final_set):
            print(f"file{final_set[j]}.txt", end="")
            if j != len(final_set)-1:
                print(", ", end="")
            j += 1
        print()
        print("Number of documents retrieved for query "+str(_+1)+":" +str(len(final_set)))
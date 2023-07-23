# 
import os
#Set the working directory (As written, this program counts the words in subfolders with writing but not the text files in the parent folder)
os.chdir('insert path to working directory')
working_directory = os.getcwd()

# Create a list with the relevant folders
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
folders = get_immediate_subdirectories(working_directory)

#function takes a list of file paths as an input, and outputs an int corresponding to the number of words in the file
def count_words(file_paths):
 word_count = 0
 for x in file_paths:
    file = open(x, "r")
    data = file.read()
    words = data.split()
    word_count += len(words)
 return word_count

folder_word_counts=[]

# loop through folders, enter each one to count the words, store results in list folder_word_counts
for folder in folders:
   os.chdir(os.path.join(working_directory, folder))
   #create a list of text files
   text_files = [x for x in os.listdir() if x.endswith(".txt")]
   #create a list of file paths to text files
   file_paths = [os.getcwd() + "/" + x for x in text_files]
   folder_word_counts.append(count_words(file_paths))

print(folder_word_counts)

sum = 0
for x in folder_word_counts:
   sum += x
result = str(sum)

#return to working directory to record logs
os.chdir(working_directory)
import logging
logging.basicConfig(filename='words_written.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.error('You have written ' + result + ' words')



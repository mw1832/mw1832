import os
# Change the working directory (Intended to be run from a directory which contains folders which contain text files)
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

# loop through folders, list the .txt files
for folder in folders:
   text_files = [x for x in os.listdir(os.path.join(working_directory, folder)) if x.endswith(".txt")]
   #create a list of file paths
   file_paths = [os.path.join(working_directory, folder) + "/" + x for x in text_files]
   #call the function to count the words in the .txt files in the folder, store results in a list
   folder_word_counts.append(count_words(file_paths))

#How many words did we find in each folder?
print(folder_word_counts)

#Sum the list of integers
sum = 0
for x in folder_word_counts:
   sum += x
#Store the result as a string
result = str(sum)

#append to a .log file the total number of words, and the date/time
import logging
logging.basicConfig(filename='words_written.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.error('You have written ' + result + ' words')



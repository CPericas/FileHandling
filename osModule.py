#Task 1: Directory Inspector:
#Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the 
# user for the directory path and then display the contents.
#Code Example:
#import os
#def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
#Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. Handle exceptions for 
# invalid paths or inaccessible directories.

import os
def list_files_and_directories(directory):
    print(f"Contents of the directory: {directory}")
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            print(f"Directory: {filename}")
        else:
            print(f"File: {filename}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ").strip()
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
    else:
        list_files_and_directories(directory_path)


#Task 2: File Size Reporter:
#Problem Statement: Write a Python program that reports the sizes of all files in a specific directory. The program should ask the user 
# for a directory path and then print each file's name and size within that directory.
#Code Example:
#def report_file_sizes(directory):
        # Iterate through files in the directory and print their names and sizes
#Expected Outcome: Your program should display the name and size (in bytes) of each file in the given directory. Ensure that the program
# only reports on files, not directories, and handles any errors gracefully.

import os
def report_file_size(directory):
    try:
        print(f"File size in directory: {directory}")
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                print(f"{filename}: {file_size} bytes")
    except FileNotFoundError:
        print(f"Error: Directory {directory} not found")
    except PermissionError:
        print(f"Error: Permission denied for Directory {directory}.")
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ").strip()
    if not os.path.exists(directory_path):
        print(f"Error: Directory {directory_path} does not exist.")
    else:
        report_file_size(directory_path)




#Task 3: File Extension Counter:
#Problem Statement: Develop a Python script that counts the number of files of each extension type in a directory. For instance, in a 
# directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".
#Code Example:
#def count_file_extensions(directory):
        # Count and print the number of files of each extension type in the directory
#Expected Outcome: The script should accurately count and display the number of files for each extension type in the specified 
# directory. Handle different cases of file extensions (e.g., '.TXT' and '.txt' should be considered the same).

import os
from collections import defaultdict

def count_file_extensions(directory):
    extension_counts = defaultdict(int)

    for root, dirs, files in os.walk(directory):
        for file in files:
            _, extension = os.path.splitext(file)
            extension = extension.lower()
            extension_counts[extension] += 1

    for extension, count in extension_counts.items():
        print(f"{extension.upper()}: {count}")

directory = input("Enter the directory path: ")
count_file_extensions(directory)


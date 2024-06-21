#Task 1: Email Extractor:
#Problem Statement: Write a Python script to extract all email addresses from a given text file (contacts.txt). The file contains a mix 
# of text and email addresses.
#File Example:
#Contact List:
#John Doe - john.doe@example.com
#Jane Smith - jane.smith@gmail.com
#For inquiries, please contact info@example.com
#Code Example:
#import re

#def extract_emails(filename):
        # Read the file and use regex to find and return all email addresses
#Expected Outcome: The script should output a list of all unique email addresses found in the file. Utilize regex to accurately identify
# email addresses amidst other text.

import re
import os

def extract_emails(filename):
    print("Current working directory:", os.getcwd())
    print("Files in the current directory:", os.listdir())
    if not os.path.isfile(filename):
        print(f"Error: The file {filename} does not exist.")
        return []
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_set = set()

    try:
        with open(filename, 'r') as file:
            for line in file:
                matches = re.findall(email_pattern, line)
                for match in matches:
                    email_set.add(match)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []
    return list(email_set)

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), 'contacts.txt')
    email_list = extract_emails(file_path)
    if email_list:
        print("Extracted email addresses:", email_list)
    else:
        print("No email addresses found or an error occurred.")



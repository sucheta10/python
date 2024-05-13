# Email List Cleanup
# You have a file named email_list.txt that contains a list of email addresses, some of which are duplicates. Write a Python program to read the file, remove duplicates, and sort the email addresses in alphabetical order. Then, write the cleaned list back to a new file named cleaned_emails.txt.

def clean_email_list(input_file, output_file):
    # Read emails from the input file
    with open(input_file, 'r') as file:
        emails = file.readlines()

    # Remove duplicates and sort the list
    unique_emails = sorted(set(emails))

    # Write the cleaned list to the output file
    with open(output_file, 'w') as file:
        file.writelines(unique_emails)

# Replace 'email_list.txt' and 'cleaned_emails.txt' with your actual file names
clean_email_list('C:/Users/Sucheta/OneDrive/Desktop/python/email.txt', 'C:/Users/Sucheta/OneDrive/Desktop/python/email_output.txt')

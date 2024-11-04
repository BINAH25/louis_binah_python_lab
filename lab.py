import os
import requests
from datetime import datetime


directory_name = 'louis_binah'
file_name = f'{directory_name}.txt'
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create the directory is it does not exist
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Directory {directory_name} Created")
else:
    print(f"Directory {directory_name} Already exist")

# download the file and write its content to file_name
url = "https://raw.githubusercontent.com/sdg000/pydevops_intro_lab/main/change_me.txt"
try:
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(directory_name, file_name), 'wb') as file:
            file.write(response.content)
            absolute_path = os.path.abspath(os.path.join(directory_name, file_name))
            print(f"File downloaded successfully and save to {absolute_path}")

    else:
        print("Failed to download file.")
except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")

# modified the file content  with the user input 
user_input = input("Describe what you have learned so far in a sentence: ")
with open(os.path.join(directory_name, file_name), "w") as file:
    file.write(user_input + "\n")
    file.write("Current date and time: " + current_time)
    print("File content modified successfully")


# Read and print the modified file content
with open(os.path.join(directory_name, file_name), "r") as file:
    content = file.read()
    print(content)

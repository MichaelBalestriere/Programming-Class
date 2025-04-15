import os

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    else:
        print(f"File {file_path} does not exist.")
        
delete_file("deleteMe.txt") #example file path.

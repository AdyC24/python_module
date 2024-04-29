import os

def rename(dir):
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            new_file = f"SKC - {file}"
            os.rename(os.path.join(dir, file), os.path.join(dir, new_file))

rename("C:/Users/User/Documents/New folder/SKC")
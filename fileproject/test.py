# # Python program to explain shutil.move() method 
	
# # importing os module 
# import os 

# # importing shutil module 
# import shutil 

# # path 
# path = 'C:/Users/Rajnish/Desktop/GeeksforGeeks'

# # List files and directories 
# # in 'C:/Users/Rajnish/Desktop/GeeksforGeeks' 
# print("Before moving file:") 
# print(os.listdir(path)) 


# # Source path 
# source = 'C:/Users/Rajnish/Desktop/GeeksforGeeks/source'

# # Destination path 
# destination = 'C:/Users/Rajnish/Desktop/GeeksforGeeks/destination'

# # Move the content of 
# # source to destination 
# dest = shutil.move(source, destination) 

# # List files and directories 
# # in "C:/Users / Rajnish / Desktop / GeeksforGeeks" 
# print("After moving file:") 
# print(os.listdir(path)) 

# # Print path of newly 
# # created file 
# print("Destination path:", dest) 

import os 
import shutil 
import pathlib

def moving_file_directory(source,destination) :
    path = pathlib.Path.cwd()
    source_src = path / f"{source}"
    destination_dst = path / f"{destination}"
    shutil.move(source_src, destination_dst) 
 
user_input = input()
user_input_1 = input()

moving_file_directory(user_input,user_input_1)
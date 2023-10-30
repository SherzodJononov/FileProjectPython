import pathlib
import os
from functionforproject import *
    
try:
    print("1) Show our directory")
    print("2) Create a new file")
    print("3) Create a new directory")
    print("4) Delete a file")
    print("5) Delete a file directory")
    print("6) Rename a file or directory")
    print("7) Change folder")
    print("8) Search files")
    print("9) Opening files")
    print("10) Read files")
    print("11) Moving files_directory")
except:
    print("Try again ")

line = pathlib.Path.cwd()

while True:
    user_input = (input('Select what action you want to perform :'))
    if user_input == "quit":
        break

    elif user_input == "home":
        new_line = pathlib.Path.cwd()
        line = new_line
        print(line)
    
    elif user_input == "cwd":
        print(os.getcwd())

    elif user_input == '1' :
        catalog()

    elif user_input == '2' :

        user_input_file = input("Enter the name of the file : ")
        makefile(user_input_file)

    elif user_input == '3':

        user_input_file = input("Enter the name of the directory : ")
        makedirectory(user_input_file)

    elif user_input == '4':

        user_input_file = input("Enter the name of the file which you want delete : ")
        deletefile(user_input_file)

    elif user_input == '5':

        user_input_file = input("Enter the name of the directory which you want delete : ")
        deletedirectory(user_input_file)

    elif user_input == '6':

        user_input_file1 = input("Enter the old name of the file : ")
        user_input_file2 = input("Enter the new name of the file : ")
        rename_file_directory(user_input_file1,user_input_file2)

    elif user_input == '7':

        user_input_file = input("Which you want to use : ")
        change(user_input_file)

    # this do sth
    elif user_input == '8' :

        # print("Enter the name of the file which you want to search : ")ашду
        user_input_place = input("Enter the place of file : ")
        user_input_filename = input("Enter the filename of file : ")
        user_input_mode = input("Enter the mode of file : ")
        search(user_input_place,user_input_filename,user_input_mode)

    elif user_input == '9' :
        
        user_input_place = input("Enter the place of file : ")
        user_input_format = input("Enter the filename of file : ")
        user_input_mode = input("Enter the mode of file : ")
        open_file(user_input_filename,user_input_format,user_input_mode)
    
    elif user_input == '10' :

        user_input_place = input("Enter the place of file : ")
        user_input_format = input("Enter the filename of file : ")
        user_input_mode = input("Enter the mode of file : ")
        read_file(user_input_place,user_input_format,user_input_mode)

    elif user_input == '11' : 
        user_source = input("Enter the source file_directory : ")
        user_destination = input("Enter the destination file_directory : ")

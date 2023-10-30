import pathlib
import os
import shutil

line_for_our = pathlib.Path.cwd()
#list_files_folders
def catalog():    
    print("Which other files you want to import :")
    print("1).txt file")
    print("2).py file")
    print("3)catalog")
    user_input = int(input())
    if user_input == 3: 
        try :
            for i in line_for_our.iterdir():
                file = i 
                print(f"{file}  {round(int(os.path.getatime(file))//3600%24,2)}:{round(int(os.path.getatime(file))//60%60,2)}:{round(int(os.path.getatime(file))%60,2)} size :{os.path.getsize(file)}")
        except :
            print("Try again")
    elif user_input == 2:
        try :
            for i in line_for_our.glob("**/*.py"):
                print(i)
        except:
            print("Try again")
    elif user_input == 1:
        try :
            for i in line_for_our.glob("**/*.txt"):
                print(i)
        except:
            print("Try again")
# # makefile

def makefile(filename):
    line_for_our = pathlib.Path.cwd()
    line_for_our = line_for_our / f"{filename}"
    if line_for_our.exists() == True:
        print("This file has in this directory")
        print("Are you sure you want to delete it?")
        user_agree = input("Yes or No\n")
        if user_agree == "Yes":
            line_for_our.touch()
    else :
        line_for_our.touch()
        print(line_for_our)

# makedirectory

def makedirectory(directoryname):
    try :
        line_for_our = pathlib.Path.cwd()
        line_for_our = line_for_our / f"{directoryname}"
        if line_for_our.exists() == True:
            print("This file has in this directory")
            print("if you want change you file you choose 'Yes or No'")
            user_agree = input()
            if user_agree == "Yes":
                deletedirectory(line_for_our)
                # user_file_new = input("Please enter a new name directory : ")
                # line_for_our = line_for_our / f"{user_file_new}"
                # line_for_our.mkdir()
        else :
            line_for_our.mkdir()
            print(line_for_our)
    except:
        print("Try again")

# deletefile

def deletefile(filename):
    try :
        line_for_our = pathlib.Path.cwd()
        line_for_our = line_for_our / f"{filename}"
        if line_for_our.exists() == True:
            print("Are you want to delete this file ? ")
            user_agree = input("Yes or No\n")
            if user_agree == "Yes":
                line_for_our.unlink()
                print(line_for_our)
        else :
            print("This file not existe in this directory ")
    except :
        print("Try again")


# deletedirectory

def deletedirectory(directoryname):
    try :
        line_for_our = pathlib.Path.cwd()
        line_for_our = line_for_our / f"{directoryname}"
        if line_for_our.exists() == True:
            print("this file has in this directory")
            print("if you want change you file you choose 'Yes or No' ")
            user_agree = input()
            if user_agree == "Yes":
                line_for_our.rmdir()
                print(line_for_our)
        else :
            print("This directory not existe in this place ")
    except:
        print("Try again")

#rename file_directory

def rename_file_directory(oldname, newname):
        
        try:
            # print("Which file or folder do you want to change : ")
            line_for_our = pathlib.Path.cwd()
            old_file_directory = line_for_our  / f"{oldname}"
            new_file_directory = line_for_our / f"{newname}"
            if old_file_directory.exists()==True:   
                old_file_directory.rename(new_file_directory)
                print("Name has been changed")
            else :
                print("Try again")
        except :
            print("Try again")

def search(place,filename,mode):
    try:
        line_for_our = pathlib.Path.cwd() / f"{place}"
        file = line_for_our / f"{filename}.{mode}"
        for i in line_for_our.glob(f"*.{mode}"):
            if file == i:
                print(i)
            else :
                continue
    except:
        print("Your entered place or filename or mode mistake ")


def open_file(filename,format,mode):

    try:
        file = open(f"{filename}.{format}", f"{mode}")
        print("If you want to add any thing please choose Yes or No : ")
        user_agree = input()
        if user_agree == "Yes":
            print("Please write if you want any thing : ")
            user_add = input()
            file.write(user_add)
            file.close()
    except:
        print("Try again ")

def change(filename):

    try:
        # print(os.getcwd())
        line_for_our = pathlib.Path.cwd()
        line_for_our = line_for_our / f"{filename}"
        os.chdir(line_for_our)
        print(os.getcwd())
    except:
        print("Try again ")


def read_file(filename,format,mode):

    try:
        print()
        file = open(f"{filename}.{format}", f"{mode}")
        print(file.read())
        print() 
    except:
        print("Try again ")

def moving_file_directory(source,destination) :
    path = pathlib.Path.cwd()
    source_src = path / f"{source}"
    destination_dst = path / f"{destination}"
    shutil.move(source_src, destination_dst) 
 
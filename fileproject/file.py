import pathlib
import os
print("1) Show our directory")
print("2) Create a new file")
print("3) Create a new directory")
print("4) Delete a file")
print("5) Delete a file directory")
print("6) Rename a file or directory")
print("7) Change folder")
user_input = int(input('Select what action you want to perform :'))

if user_input == 1 :

        try :
            home_dir = pathlib.Path.cwd()

            for i in home_dir.iterdir():
                file = i 
                print(f"{file}  {round(int(os.path.getatime(file))//3600%24,2)}:{round(int(os.path.getatime(file))//60%60,2)}:{round(int(os.path.getatime(file))%60,2)} size :{os.path.getsize(file)}")
        except :
            print("Try again")

elif user_input == 2 :

    try :   
        user_file_input = input("Write the name of the file to be created :")
        new_file = user_file_input
        line_file = pathlib.Path.cwd() / f"{new_file}"
        if line_file.exists():
            print("Your file has exeist in this directory")
            print("You want to create a new file with this name instead of this file :")
            input_again = input("Yes or No\n")
            if input_again == 'Yes':
                line_file.touch()
                print(line_file)
            elif input_again == 'No':
                    pass
        else :
            line_file.touch()
            print(line_file)
    except :
         print("Try again")

elif user_input == 3:

    try :
        user_directory_input = input("Write the name of the directory to be created :")
        new_directory = user_directory_input
        line_directory = pathlib.Path.cwd() / f"{new_directory}"
        # line_file.touch()
        if line_directory.exists():
            print("Your directory has exeist in this directory")
            print("You want to create a new directory with this name instead of this file :")
            input_again = input("Yes or No\n")
            if input_again == 'Yes':
                line_directory.mkdir()
                print(line_directory)
            elif input_again == 'No':
                    pass
        else :
            line_directory.mkdir()
            print(line_directory)
    except:
         print("Try again")

elif user_input == 4:

    try :     
        user_file_input = input("Write the name of the file to be delete :")
        new_file = user_file_input
        line_file = pathlib.Path.cwd() / f"{new_file}"
        if line_file.exists() == False:
            print("Your file has not exist in this directory")
        elif line_file.exists() == True:
            print("Are you want delete this file")
            user_delete_input = input("Yes or No\n")
            if user_delete_input == "Yes":  
                line_file.unlink()
            else :
                pass
    except :
        print("Try again")

elif user_input == 5:

    try:
        user_directory_input = input("Write the name of the file to be delete : ")
        new_directory = user_directory_input
        line_directory = pathlib.Path.cwd() / f"{new_directory}"
        if line_directory.exists() == False:
            print("Your file has not exist in this directory")
        elif line_directory.exists() == True:
            print("Are you want delete this file")
            user_delete_input = input("Yes or No\n")
            if user_delete_input == "Yes":  
                line_directory.rmdir()
            else :
                pass
    except:
        print("Try again")

elif user_input == 6:

    try :
        line_file_directory = pathlib.Path.cwd()
        user_file_directory_input = input("Which file or folder do you want to change : ")
        old_file_directory = line_file_directory  / f"{user_file_directory_input}"
        new_file_directory = input("New file name : ")
        new_file_directory = line_file_directory / f"{new_file_directory}"

        if old_file_directory.rename(new_file_directory) == True:
            print("Name has been changed")
    except :
        pass

elif user_input == 7 :

    try :

        line_directory = pathlib.Path.cwd()
        # user_place = input("Enter your old place :")
        # old_place = line_directory / f"{user_place}"
        print(f"Your old place {line_directory}")
        print("Are you sure you want to change your place ")
        user_delete_input = input("Yes or No\n")
        if user_delete_input == "Yes" :
            user_place_new = input("Enter your new place :")
            line_directory = line_directory / f"{user_place_new}"
            print(line_directory)
    except :
        pass
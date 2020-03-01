from datetime import datetime
import subprocess
import os

#-------------------------------------------------------------------------------------------
# READ AND WRITE TEXT TO AND FROM FILE

now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

# WRITE TO A FILE 
fw = open(str(now) + '.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon')
fw.close()

# READ FROM A FILE
fr = open(str(now) + '.txt', 'r')
text = fr.read()
print(text)
fr.close()

#-------------------------------------------------------------------------------------------

# This method converts string to lists.

def str_to_list(word): 
    return [char for char in word]  

a = str_to_list("hello world")

print (a)

#-------------------------------------------------------------------------------------------

# This method converts a list of characters to their corresponding list of ascii numbers.

def list_to_ascii(original_list):

    return [ord(x) for x in original_list]


list1 = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
a = list_to_ascii(list1)
print(a)

#-------------------------------------------------------------------------------------------

# This method converts string to list of each characters corresponding ascii number.

def str_to_ascii(text):

    
    def str_to_list(word): 

        return [char for char in word] 
        
    def list_to_ascii(original_list):
        
        return [ord(x) for x in original_list]
    
    text_list = str_to_list(text)
    text_ascii = list_to_ascii(text_list)

    return text_ascii

print(str_to_ascii("hello world"))

#-------------------------------------------------------------------------------------------

def Powershell_exe(destination_of_script,destination_of_file):

    # This method can execute powershell scripts 
    # located in both .txt and .ps1 files
    # 
    # destination_of_script = where file containing the script is located
    # destination_of_file = in which file to return output 

    script = open(destination_of_script , "r") 
    p1 = subprocess.run(["powershell.exe", script.read()], capture_output=True, text=True)
    return destination_of_file.write(p1.stdout)   

#-------------------------------------------------------------------------------------------

def Script_Runner(script_folder_loction, output_file_location):
    
    # This method iterates through the script folder. 
    # It then uses the Powershell_exe() method to execute each file.

    # script_folder_loction = Location where all powershell scripts are stored.
    # output_file_location = The location of the log file.

    for filename in os.listdir(script_folder_loction):
        if filename.endswith(".txt") or filename.endswith(".ps1"): 
            
            # scrit = path to a script file
            script = os.path.join(script_folder_loction, filename)

            # The Powershell_exe() method is now used to execute te "script" file.
            Powershell_exe(script,output_file_location)

            continue
        else:
            continue

#-------------------------------------------------------------------------------------------

def Maintainer(file_name,num_of_files):

    # This method is used to calculate the amount of files in a folder. 
    # And remove the oldest files if there are to many.

    # file_name = Name of folder containing the files.
    # num_of_files = Number of files allowed in folder.

    while True:

        file_count = sum([len(files) for r, d, files in os.walk(file_name)]) #Counts number of files in folder

        if file_count > num_of_files:
            
            # The following code is used to determin the oldest file in the folder
            path = file_name
            os.chdir(path)
            files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)

            oldest_file = files[0]
            # newest_file = files[-1]

            os.remove(oldest_file) # Removes oldest file

        else:
            break

#-------------------------------------------------------------------------------------------




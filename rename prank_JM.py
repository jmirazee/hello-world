import os
def rename_files():
    file_list = os.listdir(r"C:\Users\mgmirazee\Documents\MATEEN\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Diirectory is " +saved_path)
    os.chdir(r"C:\Users\mgmirazee\Documents\MATEEN\prank")
#for renaming, remove numbers from the name
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "1023456789"))
rename_files()

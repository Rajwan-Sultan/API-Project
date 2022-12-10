import glob
import shutil
import os
import zipfile
from subprocess import call


def call_file(path):
    call(["python", path])


source_path = "../source/*"
destination_path = "../destination/"

postfix = [1, 2, 3]

try:
    while True:
        # if __name__ == "__main__":
        source_object = glob.glob(source_path)
        if len(source_object) > 0:
            # print("Source Object -->", source_object)  # ['../source\\some.txt']

            object_path = source_object[0]
            # print("Object Path -->", object_path)  # ../source\some.txt

            # !copies file from source to server directory
            shutil.copy(object_path, '.')

            object_name = object_path.split("\\")[-1].split('.')
            # print("Object Name -->", object_name)  # ['some', 'txt']

            # call_name = object_path.split("\\")[-1]
            # print("Call Name -->", type(call_name))  # hi.py

            prefix = object_name[0]
            postfix2 = object_name[1]

            if postfix2 != "txt":
                try:
                    call_file(object_path.split("\\")[-1])
                except Exception as e:
                    print("Error in other python file", e)

            for item in postfix:
                filename = prefix+'_'+str(item)+'.'+postfix2
                if postfix2 == 'txt':
                    print(filename)
                # shutil.copy(object_path, f"{destination_path}\{filename}")#! sends the new file to the destination
                # print(myfilename)##../destination/\some_1.txt

                #! creats new file in the server
                shutil.copy(object_path, filename)
                myfilename = filename
                lines = ""
                myfile = open(myfilename, 'r')
                myline = myfile.readlines()  # gives a list of lines
                for i in myline:
                    lines += i
                myfile.close()
                # print(lines)
                with open(filename, 'a') as f:
                    i = myfilename.split("_")
                    j = i[1].split(".")
                    f.write(('\n'+lines)*(int(j[0])*10-1))
                f.close()

                zipO = zipfile.ZipFile("All.zip", "w")
                for i in os.listdir():
                    if i.endswith(".txt") and i != prefix+".txt":
                        zipO.write(i)
                zipO.close()
                shutil.copy(f"../server/All.zip",
                            f"{destination_path}All.zip")
                os.remove("All.zip")

        os.remove(object_path)
        os.remove(object_path.split("\\")[-1])
        for i in os.listdir():
            if i != "main.py":
                os.remove(i)
        os.chdir(destination_path)
        shutil.unpack_archive("All.zip", destination_path)
        os.remove("All.zip")
        os.chdir("../server")

except:
    print("Exiting from command")

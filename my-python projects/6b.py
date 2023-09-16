import zipfile
import os
def zip_folder(folder_path,output_path):
    with zipfile.ZipFile(output_path,'w',zipfile.ZIP_DEFLATED)as zipf:
        for root,_,files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root,file)
                arcname=os.path.relpath(file_path,folder_path)
                zipf.write(file_path,arcname)
folder_path=input("enter the path of the folder to be zipped: ")
output_path=input("enter the output zip file name: ")
try:
    zip_folder(folder_path,output_path)
    print(f"zip archive '{output_path}' created successfully")
except Exception as e:
    print(f"as error occured :{e}")
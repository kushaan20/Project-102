import os 
import shutil 
import dropbox 

path = input("Enter the directory to be sorted : ")

list_of_files = os.listdir(path)

for file in list_of_files:
    name,ext = os.path.splitext(file)
    ext = ext[1:]

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'SLPP25ERLCwAAAAAAAAAAem-7YLAgz-YY8knYiFaIbO02OvkhzSuXe6ebsu7_JCS'
    transferData = TransferData(access_token)

    file_from = path + '/' + ext
    file_to = '/test_dropbox/test.txt'  

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':  
    main()

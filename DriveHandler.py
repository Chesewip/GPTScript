from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from googleapiclient.discovery import build
from oauth2client.client import GoogleCredentials
from google.colab import files
from datetime import datetime
import os
import zipfile
import time

class DriveHandler:

    def __init__(self, folder_id):
        self.folder_id = folder_id
        auth.authenticate_user()
        gauth = GoogleAuth()
        gauth.credentials = GoogleCredentials.get_application_default()
        self.drive = GoogleDrive(gauth)
        self.drive_service = build('drive', 'v3')
        self.now = datetime.now()
        self.timestamp_str = self.now.strftime("%Y-%m-%d_%H-%M-%S")

    def clearFiles(self):
        try:
            file_list = self.drive.ListFile({'q': f"'{self.folder_id}' in parents"}).GetList()

            # Delete files from Colab environment
            for file in file_list:
                if os.path.isfile(file['title']):
                    os.remove(file['title'])

            # Delete files from Google Drive
            for file in file_list:
                print(f'Deleting file {file["title"]}')
                file.Delete()

            # Clear trash
            self.drive_service.files().emptyTrash().execute()
        except Exception as e:
            print(f'An error occurred in clearFiles: {e}')

    def downloadResult(self, script):
        try:
            time.sleep(7)
            file_list = self.drive.ListFile({'q': f"'{self.folder_id}' in parents"}).GetList()
            print(file_list);

            for file in file_list:
                print(f'Downloading file {file["title"]}')
                file.GetContentFile(file['title'])

            with open('script.txt', 'w') as f:
                f.write(script)

            zip_file_name = f'script_{self.timestamp_str}.zip'
            with zipfile.ZipFile(zip_file_name, 'w') as zipf:
                for file in file_list:
                    zipf.write(file['title'])
                zipf.write('script.txt')

            files.download(zip_file_name)
            self.clearFiles();
        except Exception as e:
            print(f'An error occurred in downloadResult: {e}')

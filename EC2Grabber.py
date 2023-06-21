import os
import paramiko
from stat import S_ISDIR

class EC2Grabber:

    def __init__(self, ec2Address, keyFile, remoteDir, outputDir):
        self.pid = None
        self.remoteDir = remoteDir
        self.outputDir = outputDir
        self.ec2Adress = ec2Address
        self.keyFile = keyFile
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ec2Adress, username='ubuntu', key_filename= self.keyFile)
        self.sftp = self.ssh.open_sftp()

    def __del__(self):
        self.closeVoiceCloners()

    def startVoiceCloners(self):
        stdin, stdout, stderr = self.ssh.exec_command('python /home/ubuntu/gptconvo/ai-voice-cloning/start.sh --share')
        self.pid = stdout.read().strip()  # Get the PID
        stdin, stdout, stderr = self.ssh.exec_command('python /home/ubuntu/gptconvo/ai-voice-cloning/start.sh --share')# Start the script and print the PID
        self.pid2 = stdout.read().strip()

    def closeVoiceCloners(self):
        self.ssh.exec_command(f'kill {self.pid}')
        self.ssh.exec_command(f'kill {self.pi2}')

    def _sftp_walk(self, remotepath):
        path = remotepath
        files = []
        folders = []
        for f in self.sftp.listdir_attr(remotepath):
            if S_ISDIR(f.st_mode):
                folders.append(f.filename)
            else:
                files.append(f.filename)

        yield path, folders, files
        for folder in folders:
            new_path = '/'.join([remotepath, folder])
            for x in self._sftp_walk(new_path):
                yield x

    def getVoiceResults(self):
        if not os.path.exists(self.outputDir):
            os.makedirs(self.outputDir)

        for dirpath, dirnames, filenames in self._sftp_walk(self.remoteDir):
            local_dir_path = os.path.join(self.outputDir, os.path.relpath(dirpath, self.remoteDir))
            local_dir_path = local_dir_path.replace('\\', '/')
            if not os.path.exists(local_dir_path):
                os.makedirs(local_dir_path)

            for filename in filenames:
                remote_file_path = '/'.join([dirpath, filename])
                local_file_path = os.path.join(local_dir_path, filename)
                self.sftp.get(remote_file_path, local_file_path)
                self.sftp.remove(remote_file_path)



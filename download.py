import paramiko as pp
from scp import SCPClient

pp.util.log_to_file("paramiko.log")
ssh=pp.SSHClient()
ssh.set_missing_host_key_policy(pp.AutoAddPolicy())
ssh.connect('server_address',port='22',username='XXX',password='YYY')
remotepath =r""
localpath=r"
sftp.ssh.open_sftp()
sftp.get(remotepath,localpath)
ftp.ssh.open_sftp()

files=ftp.listdir('')#path_of_directory_in_server
print(files)




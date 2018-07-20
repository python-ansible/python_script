import paramiko
import sys

class action(object):
    def __init__(self, IP, command):
        self.IP = IP
        self.username = 'root'
        self.password = 'Paic1234'
        self.command = command

    def ssh_connect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=self.IP, username=self.username, password=self.password)
            stdin,stdout,stderr=ssh.exec_command(self.command)
            print "######################> %s <####################" %(self.IP)
            print stderr.read()
            print stdout.read()
            ssh.close()
        except Exception,e:
            print "######################> %s <####################" %(self.IP)
            print "%s" %(e)

def get_values(hostname):
    conf_file=open('scn.conf','r')
    lines = conf_file.readlines()
    for line in lines:
        line = line.strip("\n")
        line = eval(line)
        if hostname == line["hostname"]:
            return(line)
            break
    conf_file.close()

if __name__ == "__main__":
    para=sys.argv
    if len(para) <> 3:
        print "Please input IP and command like: python batch_exe.py 1.1.1.1,2.2.2.2 'command'"
    else:
        host_ip = para[1].split(',')
        command = para[2]
        for i in range(0,len(host_ip)):
            conn = action(host_ip[i],command)
            conn.ssh_connect()


#!/usr/bin/python 
#coding:utf-8
import multiprocessing
import re 
import sys,os
import commands
import datetime
import ConfigParser
import pdb

def pinger(count,ip):
    cmd='ping -c %s %s' % (count,ip)
    ret = commands.getoutput(cmd)
    loss_re=re.compile(r"received, (.*) packet loss")
    packet_loss=loss_re.findall(ret)[0]
    cp = ConfigParser.SafeConfigParser()
    cp.read('./hosts.txt')
    system = cp.get('os','system')
    if system == 'mac':
        rtt_re=re.compile(r"round-trip min/avg/max/stddev = (.*) ")
    else:
        rtt_re=re.compile(r"rtt min/avg/max/mdev = (.*) ")
    rtts=rtt_re.findall(ret)
    if rtts:
        rtt=rtts[0].split('/')
        rtt_min=rtt[0]
        rtt_avg=rtt[1]
        rtt_max=rtt[2]
        print "%s\t\t%s\t\t%s\t\t%s\t\t%s"%(ip,packet_loss,rtt_min,rtt_max,rtt_avg)
    else:
        print "%s\t\t%s\t\tnone\t\tnone\t\tnone"%(ip,packet_loss)

if __name__ == "__main__":
    if not os.path.exists("hosts.txt") :
        print "\033[31mhosts.txt文件不存在，请重试\033[0m"
        sys.exit(1)
    #import pdb
    #pdb.set_trace()
    now=datetime.datetime.now()
    now=now.strftime('%Y-%m-%d %H:%M:%S') 
    file=open('hosts.txt','r')
    cp = ConfigParser.SafeConfigParser()
    cp.read('./hosts.txt')
    ip = cp.get('ip','ip').split(',')
    #线程数，默认2，最好不超过核心数
    pool=multiprocessing.Pool(processes=2)
    result=[]
    print "##############################%s##############################"%now
    print "IPADDRSS\t\tLOSS\t\tMIN\t\tMAX\t\tAVG"
    for i in ip:
    #ping操作的次数，默认3
        result.append(pool.apply_async(pinger,(3,i))) 
    pool.close()           
    pool.join()

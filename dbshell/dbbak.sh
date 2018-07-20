#!/bin/bash
#scripts for dirbakup and upload to ftp server.
#author by wzl
#带日期压缩备份
#FTP异地保存
bakdir=mylog
date=`date +%F`

cd /var
tar zcf ${bakdir}_${date}.tar.gz ${bakdir}
sleep 1

ftp -n <<- EOF
#远程ftp服务器IP
open 192.168.142.129    
user aaa bbb
put mylog_*.tar.gz
bye
EOF

rm -rf  mylog_*.tar.gz


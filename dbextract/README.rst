=======================
PingAn Cloud Automation

CS,PORTAL,NSP 抽取
=======================

0.准备阶段:
    a.创建数据库用户：
    grant all privileges on *.* to backup@'%' Identified by "backup";
    grant all privileges on *.* to extract@'localhost' Identified by "extract";
    b.初始化数据库database:
	CREATE DATABASE IF NOT EXISTS sza_keystone DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
        CREATE DATABASE IF NOT EXISTS sza_neutron DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

1.安装
    a.安装setuptools
    b.安装dbextract
    注：抽取回来的数据库临时文件存放在/root/db_extract目录下，可以在db_init里面修改。
2.配置crontab
    a.编辑/etc/dbextract/config.json
    b.命令：
	crontab -e
	1 1 * * * dbextract -c /etc/dbextract/config.json >> /var/log/dbextract/dbextract.log 2>&1

3.config.json字段解析：
{
    "debug": true,
    "dest_database":{
	"host": "localhost",
	"username": "extract",
        "password": "extract"
    },
    "src_databases": [
	{
	    "host": "10.21.200.48",
	    "username": "alphaops",
   	    "password": "LuckyOps20@",
            "self_db": "cloud",
	    "target_db": "cs_sza"
        }
    ]
}

	    

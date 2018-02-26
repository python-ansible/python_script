# _*_ coding=utf-8 _*_

import os
import threading
import logging

class Config(object):
    config = None
    def __init__(self, config):
	Config.config = config

class DB(object):
    def __init__(self, host, username, password, database, backup_dir='/root/db_backup', suffix='_extract.sql'):
	self.host = host
	self.username= username
	self.password = password
	self.database = database
	self.filename = host + '_' + database + suffix
	self.path = backup_dir + '/' + self.filename
	# create db files for backup
 	cmd = "mkdir -p %s" %backup_dir
	os.system(cmd)

    def load_databases(self):
	para = {"host": self.host,
          	"username": self.username,
		"password": self.password,
		"database": self.database,
		"path": self.path
		}
	cmd = "mysqldump --single-transaction -h%(host)s -u%(username)s -p%(password)s %(database)s > %(path)s" %para
	logging.info("cmd = %s" %cmd)
	os.system(cmd)

    def update_databases(self, host, username, password, database):
   	para = {"host": host,
		"username": username,
		"password": password,
		"database": database,
		"path": self.path
                }
	cmd = "mysql -h%(host)s -u%(username)s -p%(password)s %(database)s < %(path)s" %para
	logging.info("cmd = %s" %cmd)
	os.system(cmd)

class ExtractDB(threading.Thread):
    def __init__(self, dest_database, src_database):
	super(ExtractDB, self).__init__()
	self.target_host = dest_database['host']
	self.target_username = dest_database['username']
        self.target_password = dest_database['password']
	self.target_db = src_database['target_db']
	self.src_host = src_database['host']
	self.db = DB(src_database['host'], src_database['username'], src_database['password'], src_database['self_db'])

    def run(self):
	try:
	    logging.info("%s[%s] exctract starting" %(self.src_host, self.target_db))
	    self.db.load_databases()
	    self.db.update_databases(self.target_host, self.target_username, self.target_password, self.target_db)
	    logging.info("%s[%s] exctract data success" %(self.src_host, self.target_db))
	except Exception as e:
	    logging.error("%s[%s] exctract data failed" %(self.src_host, self.target_db))

class Scheduler(object):
    def __init__(self, config):
	self.dest_database = config['dest_database']
	self.src_databases = config['src_databases']
	self.tasks = []
    def concurrency(self):
   	for src_database in self.src_databases:
	    task = ExtractDB(self.dest_database, src_database)
  	    task.setDaemon(True)
	    task.start()
            self.tasks.append(task)

    def joins(self):
	for task in self.tasks:
 	    task.join()

    def run(self):
	self.concurrency()
	self.joins()

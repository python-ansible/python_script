#!/usr/bin/python
# _*_ coding=utf-8 _*_
#db 数据抽取
#auth: wangzelin
#modify date:2017-12-01
import json
import logging
import time
from optparse import OptionParser
from db import Config
from db import Scheduler

def log_init():
    if Config.config['debug']:
	level=logging.DEBUG
    else:
	level=logging.INFO
    logging.basicConfig(level=level,
		format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
		datefmt='%a, %d %b %Y %H:%M:%S')
def option_parser():
    parser = OptionParser(usage="usage:%prog [optinos] filepath")
    parser.add_option("-c", "--config",
                    action = "store",
                    dest = "config",
		    default = None,
                    help= "Specify the config file path"
                    )
    (options, args) = parser.parse_args()
    return options

def init_config(path):
    config = None
    if path:
	with open(path, 'r') as fp:
	    Config.config = json.load(fp, encoding="ASCII")

def main():
    try:
	options = option_parser()
        init_config(options.config)
        if not Config.config:
	    print("config is None")
	    exit(0)
	log_init()
	scheduler = Scheduler(Config.config)
	scheduler.run()
    except Exception as e:
	print("exception %s" %e)

if __name__ == "__main__":
    main()

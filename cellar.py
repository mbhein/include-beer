#!/usr/bin/env python3

""" Display stats on Beer cellar
    Usage:
        python3 cellar.py

"""
import time
import os, sys
import logging

import modules.config.manager as cfg_mgr
import modules.config.logging as logger

def main():


    config = cfg_mgr.ConfigManager()
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    log_dir = os.path.expanduser(config.defaults.log_dir)
    log_file = os.path.join(log_dir, 'cellar.log')
    #log_this = logger.load_logger('include-beer.cellar', log_file, config.defaults.debug)
    log_this = logger.load_logger('include-beer.cellar')

    log_this.info('Cellar open')
    


    



if __name__ == '__main__':
    main()

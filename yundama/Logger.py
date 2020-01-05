# -*- coding: utf-8 -*-
__author__ = 'twodogegg'

import logging
import coloredlogs
from datetime import datetime
from logging import handlers


class Logger:
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename='', level='debug', dir='.', backCount=3, fmt='(%(levelname)s) %(asctime)s: %(message)s'):
        if not filename:
            filename = str(datetime.now().date())
        filename = filename + '.log'
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        filename = dir + '/' + filename
        th = handlers.TimedRotatingFileHandler(filename=filename, backupCount=backCount, encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)

        coloredlogs.install(level='DEBUG', logger=self.logger)

    def info(self, value):
        self.logger.info(value)

    def error(self, value):
        self.logger.error(value)

    def debug(self, value):
        self.logger.debug(value)

    def warning(self, value):
        self.logger.warning(value)

    def critical(self, value):
        self.logger.critical(value)

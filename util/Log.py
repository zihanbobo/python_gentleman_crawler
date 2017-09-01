# encoding:utf-8
import logging,os

class Logger:
 def __init__(self, path):
  self.logger = logging.getLogger(path)
  fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')
  #设置CMD日志
  sh = logging.StreamHandler()
  sh.setFormatter(fmt)
  #设置文件日志
  fh = logging.FileHandler(path, encoding="utf8")
  fh.setFormatter(fmt)
  #fh.encoding = "utf8"
  #self.logger.addHandler(sh)
  self.logger.addHandler(fh)

 def debug(self,message):
  self.logger.debug(message)

 def info(self,message):
  self.logger.info(message)

 def war(self,message):
  self.logger.warn(message)

 def error(self,message):
  self.logger.error(message)

 def cri(self,message):
  self.logger.critical(message)

if __name__ =='__main__':
 logyyx = Logger('logs/test.log')
 logyyx.debug('一个debug信息')
 logyyx.info('一个info信息')
 logyyx.war('一个warning信息')
 logyyx.error('一个error信息')
 logyyx.cri('一个致命critical信息')
import logging

serviceLog = logging.getLogger('preprocessor')
serviceLog.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()
consoleFormat = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')
consoleHandler.setFormatter(consoleFormat)
consoleHandler.setLevel(logging.DEBUG)

serviceLog.addHandler(consoleHandler)

class serviceLogger():
    def debug(message):
        serviceLog.debug(message)
    
    def info(message):
        serviceLog.info(message)
    
    def warning(message):
        serviceLog.warning(message)
    
    def error(message):
        serviceLog.error(message)
    
    def critical(message):
        serviceLog.critical(message)

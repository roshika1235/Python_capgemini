import logging
logging.basicConfig(level=logging.INFO)
logging.info("App started")
logging.warning("Low memory")
logging.error("no error")

#debug- while dev
#info- app started db connected
#warning-if duplicated features are present  somethin unexdcepted
#error-acception occured
#critical-server down

#basic config:
#level,filename,format,filemode-(a,w)
#logrecord attributes
help("logging.LogRecord")
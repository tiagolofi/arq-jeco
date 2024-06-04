
import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '[%(levelname)s] %(asctime)s: %(pathname)s > %(module)s > %(funcName)s > %(lineno)d: %(message)s'
)

Logger = logging.getLogger(__name__)
Logger.CRITICAL = 50
Logger.FATAL = 50
Logger.ERROR = 40
Logger.WARNING = 30
Logger.WARN = 30
Logger.INFO = 20
Logger.DEBUG = 10
Logger.NOTSET = 0

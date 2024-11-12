# logging_config.py
import logging
import colorlog
import os
from dotenv import load_dotenv

# Logging把等級分為六個等級，NOTSET >= DEBUG >= INFO >= WARNING >= ERROR >= CRITICAL
class LoggerConfigurator:
    def __init__(self, level=logging.DEBUG, file_path='./log/app.log'):
        self.level = level
        self.file_path = file_path
        self.logger = None

        # Load environment variables from .env file
        load_dotenv()

        # Read the LOG_TO_FILE variable from the .env file
        self.log_to_file = os.getenv('LOG_TO_FILE', 'False').lower() == 'true'
        
        self.configure_logging()

    def configure_logging(self):
        LOGFORMAT = "%(log_color)s%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(lineno)d - %(message)s%(reset)s"
        LOGCOLORS = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }

        # Set up formatter with colors
        formatter = colorlog.ColoredFormatter(LOGFORMAT, log_colors=LOGCOLORS)

        # Get the root logger
        self.logger = colorlog.getLogger()

        # Check if handlers already exist to avoid adding duplicates
        if not self.logger.hasHandlers():
            stream_handler = colorlog.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

            # Add FileHandler if log_to_file is True
            if self.log_to_file:
                # Ensure the directory exists
                log_dir = os.path.dirname(self.file_path)
                if not os.path.exists(log_dir):
                    os.makedirs(log_dir)

                # Create file handler with utf-8 encoding
                file_handler = logging.FileHandler(self.file_path, encoding='utf-8')
                file_handler.setFormatter(logging.Formatter(
                    '%(asctime)s - %(name)s - %(module)s - %(lineno)d - %(levelname)s - %(message)s'))
                self.logger.addHandler(file_handler)

            self.logger.setLevel(self.level)

        # Silence less important loggers
        logging.getLogger('PIL').setLevel(logging.WARNING)
        logging.getLogger('matplotlib').setLevel(logging.WARNING)
        logging.getLogger('OpenGL').setLevel(logging.WARNING)

    def get_logger(self, name):
        return self.logger.getChild(name)

# # Example usage:
# configurator = LoggerConfigurator(file_path='./log/my_log_file.log')
# logger = configurator.get_logger('my_logger')
# logger.info("This will be logged to both the console and the file if LOG_TO_FILE is True")
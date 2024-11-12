# __init__.py
from utils.logging_config import LoggerConfigurator

# 初始化並配置日誌系統
log_configurator = LoggerConfigurator()
logger = log_configurator.get_logger(__name__)
from . import logger  # 從同一個包導入 logger

class Model:
    def __init__(self):
        logger.debug("Initializing Model")
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count
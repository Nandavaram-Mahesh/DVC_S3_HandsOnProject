import os
import logging


def setup_logger(name):
        
    # Ensure the "logs" directory exists
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    # logging configuration
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')
    if not logger.handlers:
        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel('DEBUG')
        # File Handler
        log_filename = f'{name}.log'
        log_file_path = os.path.join(log_dir, log_filename)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel('DEBUG')
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s- %(filename)s:%(lineno)d - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        # Add Handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

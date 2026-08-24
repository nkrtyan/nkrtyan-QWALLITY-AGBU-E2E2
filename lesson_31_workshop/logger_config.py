import logging

def setup_logging():
    logging.basicConfig(
    level=logging.INFO,   
    format='%(asctime)s [%(levelname)s] %(message)s',   
    filename= "info.log",
    filemode='w+',
    )
    return logging.getLogger()

logger = setup_logging()
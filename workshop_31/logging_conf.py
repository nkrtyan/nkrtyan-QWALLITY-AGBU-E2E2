import logging


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%m-%d-%Y', 
        filename='logging_file.log', 
        filemode='w',  
	    encoding='utf-8'  
)
    
pass
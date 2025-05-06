import sys
import logging
from src.logger import logger

#custom exception
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        
        _, _, exc_tb = error_detail.exc_info()
        self.error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            exc_tb.tb_frame.f_code.co_filename,
            exc_tb.tb_lineno,
            str(error_message)  
        )

    def __str__(self):
        return self.error_message
    
    
if __name__ == "__main__":
    # Test the CustomException class
    try:
            a=1/0
    except Exception as e:
                logger.info("divided by zero")
                raise CustomException(e, sys)
    

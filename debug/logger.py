""" Log functions
"""
import os
import logging
from datetime import datetime

class Logger:
    def __init__(self) -> None:
        if not hasattr(self, '_logPath') or self._logPath is None:
            # Construct Log file name
            log_dir = os.path.join(os.getcwd(), 'log')
            os.makedirs(log_dir, exist_ok=True)
            self._logPath = os.path.join(
                log_dir,
                #os.getcwd(),
                #"monitor-stock-" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".log"
                "monitor-stock-" + datetime.now().strftime('%Y-%m-%d') + ".log"
            )
            logging.basicConfig(
                filename=self._logPath, 
                level=logging.INFO, 
                format='%(asctime)s - %(levelname)s - %(message)s'
            )
               
    def log(self, *args, **kwargs ):
        line = ' '.join(map(str, args)) + ' ' + ' '.join(f'{key}={value}' for key, value in kwargs.items())    
        # with open(self._logPath, 'w') as file:
        #     file.write( line + '\n' )
        logging.info(line)
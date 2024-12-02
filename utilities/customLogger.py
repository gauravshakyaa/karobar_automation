import logging
import os

# class LogGen:
    # @staticmethod
    # def loggen():
    #     logger = logging.getLogger()
        
    #     # Prevent multiple handlers from being added
    #     if not logger.hasHandlers():
    #         logging.basicConfig(
    #             filename = "C://Users//acer//VisualStudioProjects//Karobar_Revamp_Selenium//Configurations//Logs//revamp_karobar.log",
    #             format="%(asctime)s: %(levelname)s: %(message)s",
    #             datefmt="%m%d%Y %H:%M:%S %p",
    #             level=logging.INFO  # You can set it to DEBUG, INFO, etc.
    #         )
        
    #     return logger
    
def setup_logging(log_file=os.path.join(os.getcwd(), "Configurations", "Logs", "revamp_karobar.log")):
    logging.basicConfig(
        level=logging.INFO,  # Change to DEBUG for more detailed logs
        format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
        handlers=[
            logging.FileHandler(log_file),  # Log to file
            logging.StreamHandler()        # Print logs to console
        ],
        force=True
    )


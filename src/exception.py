import sys
import logging

# Function to capture detailed error information
def error_message_detail(error, error_detail: sys):
    # Extracting traceback information
    _, _, exc_tb = error_detail.exc_info()
    # Getting the filename where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Creating a formatted error message with the filename, line number, and the actual error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    # Returning the formatted error message
    return error_message

# Custom exception class to handle exceptions with detailed information
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Initialize the parent Exception class with the basic error message
        super().__init__(error_message)
        # Use the error_message_detail function to create a detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # Override the __str__ method to return the detailed error message when the exception is printed
    def __str__(self):
        return self.error_message



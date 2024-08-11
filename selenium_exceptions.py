from selenium.common.exceptions import NoSuchElementException, TimeoutException

def handle_exception(exception):
    if isinstance(exception, NoSuchElementException):
        print("Element not found.")
    elif isinstance(exception, TimeoutException):
        print("Element took too long to load.")
    else:
        print(f"An error occurred: {exception}") 
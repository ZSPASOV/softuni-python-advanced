# Sometimes you may need to create custom exceptions that serves your purpose
# In Python, users can define such exceptions by creating a new class

class CustomError(Exception):  # derived from the exception class
    pass
raise CustomError # raising the exception
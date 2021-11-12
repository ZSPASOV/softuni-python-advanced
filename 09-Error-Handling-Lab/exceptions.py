class Error(Exception):
    pass


class InvalidInputError(Error):
    pass


class BadRequestError(Error):
    pass


try: # demo16
    # execute operation
    pass
except Error:
    pass

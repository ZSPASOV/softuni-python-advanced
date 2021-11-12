# An Except clause may name multiple exceptions as a parenthesized tuple, for example
except (RuntimeError, TypeError, NameError):
    pass

# If some of these exceptions occur, the body of the except statement will be executed

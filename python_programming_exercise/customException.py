class MyError(Exception):
    """My own exception class


    Attributes:
        msg  -- explanation of the error
    """
    def __init__(self,msg):
        self.msg=msg
    


# myError=MyError('Something went wrong')


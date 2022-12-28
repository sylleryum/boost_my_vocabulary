class InvalidKeyException(Exception):
    def __init__(self, message):
        super().__init__(message)


class ResourceDuplicatedException(Exception):
    def __init__(self, message):
        super().__init__(message)

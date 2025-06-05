class UserNotFoundException(Exception):
    """Exception raised when a user is not found."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class TaskNotFoundException(Exception):
    """Exception raised when a task is not found."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
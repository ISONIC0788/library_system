import time
import functools

def track_access(func):
    """
    Decorator that logs the method name, arguments, and timestamp.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # args[1:] is used to skip 'self' so we only see relevant arguments
        print(f"[LOG] {timestamp} | Accessed: {func.__name__} | Args: {args[1:]} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def permission_check(required_role):
    """
    Closure that returns a decorator to enforce role-based access.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # We assume 'user' is passed as the second argument (after self)
            # or as a named keyword argument.
            user = kwargs.get('user')
            if not user and len(args) > 1:
                user = args[1]
            
            # Check if user object has a role attribute
            if not user or getattr(user, 'role', None) != required_role:
                user_name = getattr(user, 'name', 'Unknown')
                print(f" Access Denied: User '{user_name}' does not have '{required_role}' privileges.")
                return None
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def borrow_item(item):
    """
    Demonstrates Duck Typing.
    Accepts ANY object as long as it has a .title attribute.
    """
    try:
        # If the object has a title, we treat it like a borrowable item
        print(f" Duck Test: Processing borrowing for '{item.title}'...")
    except AttributeError:
        print("Error: This object is not borrowable (Missing 'title' attribute).")
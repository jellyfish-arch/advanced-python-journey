# 03 - Decorators (Introduction)
# Intermediate Concept: Functions that modify the behavior of other functions

import time
from functools import wraps

# --- Basic decorator ---
def shout(func):
    """Decorator that converts function output to uppercase."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@shout
def greet(name):
    """Return a greeting message."""
    return f"hello, {name}! welcome aboard."


print(greet("Arjun"))
print(f"Function name preserved: {greet.__name__}")


# --- Timer decorator ---
def timer(func):
    """Decorator that measures execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {func.__name__}() took {elapsed:.6f} seconds")
        return result
    return wrapper


@timer
def compute_sum(n):
    """Compute sum of numbers from 1 to n."""
    return sum(range(1, n + 1))


result = compute_sum(1_000_000)
print(f"Sum = {result:,}")


# --- Logger decorator ---
def logger(func):
    """Decorator that logs function calls with arguments."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"[LOG] Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__}() returned {result!r}")
        return result
    return wrapper


@logger
def multiply(a, b):
    """Multiply two numbers."""
    return a * b


multiply(7, 6)


# --- Access control decorator ---
def require_auth(func):
    """Decorator that checks if user is authenticated before executing."""
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("authenticated", False):
            print(f"[DENIED] Access denied for '{user.get('name', 'unknown')}'")
            return None
        print(f"[GRANTED] Access granted for '{user['name']}'")
        return func(user, *args, **kwargs)
    return wrapper


@require_auth
def view_dashboard(user):
    """Return sensitive dashboard data."""
    return f"Dashboard data for {user['name']}: [Revenue: Rs.5.2L | Users: 1,204]"


admin = {"name": "Priya", "authenticated": True}
guest = {"name": "Guest", "authenticated": False}

print(view_dashboard(admin))
print(view_dashboard(guest))


# --- Stacking decorators ---
@logger
@timer
def fibonacci(n):
    """Calculate nth Fibonacci number iteratively."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print()
fib_result = fibonacci(30)
print(f"Fibonacci(30) = {fib_result}")


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print("Decorators demonstrated: @shout, @timer, @logger, @require_auth")
    print("Key concept: Decorators wrap functions to add behavior without modifying them")

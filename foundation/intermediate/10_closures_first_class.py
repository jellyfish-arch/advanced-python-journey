# 10 - Closures & First-Class Functions
# Intermediate Concept: Functions as objects, closures, factories, and higher-order functions

# --- Functions are first-class objects ---
print("=" * 50)
print("FIRST-CLASS FUNCTIONS")
print("=" * 50)


def greet(name):
    return f"Hello, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"


# Assign functions to variables
say = greet
print(say("Arjun"))

# Store functions in a data structure
actions = {"greet": greet, "farewell": farewell}
for action_name, action_func in actions.items():
    print(f"  {action_name}: {action_func('Priya')}")

print()

# --- Higher-order functions (functions that accept/return functions) ---
print("=" * 50)
print("HIGHER-ORDER FUNCTIONS")
print("=" * 50)


def apply_operation(func, data):
    """Apply a function to each element and return results."""
    return [func(item) for item in data]


def double(x):
    return x * 2


def negate(x):
    return -x


numbers = [1, 2, 3, 4, 5]
print(f"Original:  {numbers}")
print(f"Doubled:   {apply_operation(double, numbers)}")
print(f"Negated:   {apply_operation(negate, numbers)}")
print(f"Cubed:     {apply_operation(lambda x: x ** 3, numbers)}")

print()

# --- Closures: Functions that remember their enclosing scope ---
print("=" * 50)
print("CLOSURES")
print("=" * 50)


def make_multiplier(factor):
    """Return a function that multiplies by the given factor.

    The inner function 'closes over' the 'factor' variable.
    """
    def multiplier(x):
        return x * factor
    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)
to_percentage = make_multiplier(100)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")
print(f"to_percentage(0.85) = {to_percentage(0.85)}")

# Verify closure captures the variable
print(f"Closure vars: {double.__closure__[0].cell_contents}")

print()

# --- Closure: Counter factory ---
def make_counter(start=0):
    """Create a counter with its own independent state."""
    count = [start]  # Mutable container to allow modification in closure

    def increment(step=1):
        count[0] += step
        return count[0]

    def decrement(step=1):
        count[0] -= step
        return count[0]

    def get():
        return count[0]

    def reset():
        count[0] = start
        return count[0]

    # Return a dict of operations (like a simple object)
    return {
        "increment": increment,
        "decrement": decrement,
        "get": get,
        "reset": reset,
    }


print("--- Counter Factory ---")
counter_a = make_counter()
counter_b = make_counter(100)

print(f"A: {counter_a['increment']()}")      # 1
print(f"A: {counter_a['increment']()}")      # 2
print(f"A: {counter_a['increment'](5)}")     # 7
print(f"B: {counter_b['decrement'](10)}")    # 90
print(f"A: {counter_a['get']()}")            # 7 (independent state)
print(f"A: {counter_a['reset']()}")          # 0

print()

# --- Closure: Logger factory ---
def make_logger(prefix, level="INFO"):
    """Create a logger with a fixed prefix and level."""
    log_count = [0]

    def log(message):
        log_count[0] += 1
        print(f"[{level}] {prefix} | #{log_count[0]}: {message}")

    def get_count():
        return log_count[0]

    log.get_count = get_count  # Attach function as attribute
    return log


print("--- Logger Factory ---")
db_logger = make_logger("DATABASE", "DEBUG")
api_logger = make_logger("API", "INFO")

db_logger("Connection established")
db_logger("Query executed: SELECT * FROM users")
api_logger("GET /api/users -> 200")
db_logger("Connection closed")
api_logger("POST /api/orders -> 201")

print(f"DB logs: {db_logger.get_count()}, API logs: {api_logger.get_count()}")

print()

# --- Closure: Memoization (caching) ---
def memoize(func):
    """Closure-based memoization for pure functions."""
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
            print(f"  [SAVE] Computed {func.__name__}{args} = {cache[args]}")
        else:
            print(f"  [FAST] Cached   {func.__name__}{args} = {cache[args]}")
        return cache[args]

    wrapper.cache = cache
    return wrapper


print("--- Memoization with Closures ---")

@memoize
def fibonacci(n):
    """Calculate nth Fibonacci number recursively."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(8)
print(f"\nfibonacci(8) = {result}")
print(f"Cache size: {len(fibonacci.cache)} entries")

# Calling again uses cache entirely
print("\nCalling fibonacci(6) again:")
fibonacci(6)

print()

# --- Practical: Function dispatcher ---
print("=" * 50)
print("PRACTICAL: Command Dispatcher")
print("=" * 50)


def make_dispatcher():
    """Create a command dispatcher using closures."""
    registry = {}

    def register(name):
        """Register a function with a command name."""
        def decorator(func):
            registry[name] = func
            return func
        return decorator

    def dispatch(name, *args, **kwargs):
        """Execute a registered command."""
        if name in registry:
            return registry[name](*args, **kwargs)
        return f"[X] Unknown command: '{name}'"

    def list_commands():
        """List all registered commands."""
        return list(registry.keys())

    return register, dispatch, list_commands


register, dispatch, list_commands = make_dispatcher()


@register("add")
def add(a, b):
    return f"{a} + {b} = {a + b}"


@register("multiply")
def multiply(a, b):
    return f"{a} x {b} = {a * b}"


@register("greet")
def greet_user(name):
    return f"Hello, {name}! "


print(f"Available commands: {list_commands()}")
print(dispatch("add", 10, 20))
print(dispatch("multiply", 7, 6))
print(dispatch("greet", "Vikram"))
print(dispatch("unknown_cmd"))


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print("Covered: first-class functions, closures, factories, memoization, dispatchers")
    print("Key insight: Closures encapsulate state without classes")

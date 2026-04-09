# 05 - *args and **kwargs
# Intermediate Concept: Flexible function arguments, unpacking, and forwarding

# --- *args: Variable positional arguments ---
def calculate_average(*scores):
    """Calculate the average of any number of scores."""
    if not scores:
        return 0
    total = sum(scores)
    avg = total / len(scores)
    print(f"Scores: {scores}")
    print(f"Average: {avg:.2f} (from {len(scores)} values)")
    return avg


calculate_average(85, 90, 78, 92, 88)
calculate_average(100)
print()


# --- **kwargs: Variable keyword arguments ---
def build_profile(**details):
    """Build a user profile from keyword arguments."""
    print("--- Profile ---")
    for key, value in details.items():
        formatted_key = key.replace("_", " ").title()
        print(f"  {formatted_key}: {value}")
    print()


build_profile(name="Arjun", age=25, city="Bangalore", role="Backend Developer")
build_profile(name="Sneha", skill="Data Science", experience_years=3)


# --- Combining regular, *args, and **kwargs ---
def create_order(customer, *items, **options):
    """Create an order with flexible item list and options."""
    print(f"[PKG] Order for: {customer}")
    print(f"   Items ({len(items)}):")
    for item in items:
        print(f"     - {item}")

    # Process options with defaults
    delivery = options.get("delivery", "standard")
    gift_wrap = options.get("gift_wrap", False)
    discount = options.get("discount", 0)

    print(f"   Delivery: {delivery}")
    print(f"   Gift Wrap: {'Yes' if gift_wrap else 'No'}")
    if discount > 0:
        print(f"   Discount: {discount}%")
    print()


create_order("Priya", "Laptop", "Mouse", "Keyboard",
             delivery="express", gift_wrap=True, discount=10)
create_order("Rahul", "Headphones")


# --- Unpacking with * and ** ---
def display_score(name, subject, score):
    """Display a formatted score."""
    print(f"  {name} scored {score} in {subject}")


# Unpacking a list into positional args
data_list = ["Meera", "Mathematics", 95]
display_score(*data_list)

# Unpacking a dict into keyword args
data_dict = {"name": "Vikram", "subject": "Physics", "score": 88}
display_score(**data_dict)
print()


# --- Forwarding args and kwargs ---
def log_call(func):
    """A wrapper that forwards all arguments to the original function."""
    def wrapper(*args, **kwargs):
        print(f"[FWD] Forwarding call to {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper


@log_call
def send_notification(user, message, priority="normal"):
    """Send a notification to a user."""
    print(f"[MSG] [{priority.upper()}] To {user}: {message}")


send_notification("Arjun", "Your order has been shipped!", priority="high")
print()


# --- Practical: Flexible config builder ---
def merge_configs(*configs, **overrides):
    """Merge multiple config dictionaries with optional overrides."""
    merged = {}
    for config in configs:
        merged.update(config)
    merged.update(overrides)
    return merged


defaults = {"theme": "dark", "language": "en", "notifications": True}
user_prefs = {"theme": "light", "font_size": 14}
admin_prefs = {"debug": True}

final_config = merge_configs(defaults, user_prefs, admin_prefs, language="hi")
print("Final config:")
for key, value in final_config.items():
    print(f"  {key}: {value}")


# --- Keyword-only arguments (after *) ---
def search(query, *, case_sensitive=False, max_results=10):
    """Search with keyword-only options."""
    print(f"\n[SEARCH] Searching for '{query}'")
    print(f"   Case sensitive: {case_sensitive}")
    print(f"   Max results: {max_results}")


search("python decorators", case_sensitive=True, max_results=5)
search("error handling")


# --- Main ---
if __name__ == "__main__":
    print("\n--- Summary ---")
    print("Covered: *args, **kwargs, unpacking, forwarding, keyword-only args")
    print("Key insight: These tools make functions flexible and reusable")

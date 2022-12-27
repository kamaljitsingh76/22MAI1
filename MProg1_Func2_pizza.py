# Storing a function in a module
# File: MProg1_Func2_pizza.py
def make_pizza(size, *toppings):
 """Make a pizza."""
 print("\nMaking a " + size + " pizza.")
 print("Toppings:")
 for topping in toppings:
  print("- " + topping)

# File:MProg15_Module2.py
# Collecting an arbitrary number of keyword arguments

def build_profile1(first, last, **user_info):
    """Build a user's profile dictionary.
    Build a dict with the required keys."""
    profile = {'first': first, 'last': last}
 # Add any other keys and values.
    for key, value in user_info.items():
        profile[key] = value
    return profile
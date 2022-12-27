# File:MProg15_Module2.py
# Collecting an arbitrary number of keyword arguments

def build_profile(first, last, **user_info):
    """Build a user's profile dictionary.
    Build a dict with the required keys."""
    profile = {'first': first, 'last': last}
 # Add any other keys and values.
    for key, value in user_info.items():
        profile[key] = value
    return profile

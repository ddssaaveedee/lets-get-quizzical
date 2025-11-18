"""
File containing utility methods
"""

import json
import os


def load_secrets(filename="config.json"):
    """
    Loads secret configuration from a local JSON file.
    If the file is missing, it raises an error prompting the user
    to create the file from the example template.
    """
    if not os.path.exists(filename):
        template_name = filename + ".template"
        raise FileNotFoundError(
            f"ERROR: Configuration file '{filename}' not found. "
            f"Please create it by copying and filling out '{template_name}'."
        )

    try:
        with open(filename, "r", encoding="utf-8") as file:
            secrets = json.load(file)
            return secrets
    except json.JSONDecodeError:
        print(f"ERROR: Could not decode JSON from '{filename}'. Check the file syntax.")
        raise
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        raise

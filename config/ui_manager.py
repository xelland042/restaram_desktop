import json
import os
from pathlib import Path
import shutil

# Define current and parent directories
current_directory = Path(__file__).resolve().parent
parent_directory = current_directory.parent

# Specify the config files and directories
config_theme_file = os.path.join(parent_directory, 'config', 'config_theme.json')
theme_file = os.path.join(parent_directory, 'config', 'theme.json')


# Ensure the config files exist in a writable location
def ensure_config_exists():
    try:
        # Check if original files are writable in the config directory
        if os.path.exists(config_theme_file) and os.access(config_theme_file, os.W_OK) and \
                os.path.exists(theme_file) and os.access(theme_file, os.W_OK):
            # If both files exist and are writable, return them directly
            return Path(config_theme_file), Path(theme_file)
        else:
            raise PermissionError
    except PermissionError:
        # Fallback to a user-writable directory, such as /tmp
        fallback_dir = Path('/tmp/my_app_config')
        fallback_dir.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist

        # Fallback paths for config files
        fallback_config_theme_file = fallback_dir / 'config_theme.json'
        fallback_theme_file = fallback_dir / 'theme.json'

        # Copy the original config_theme.json if it doesn't exist in /tmp
        if not fallback_config_theme_file.exists():
            shutil.copy(config_theme_file, fallback_config_theme_file)

        # Copy the original theme.json if it doesn't exist in /tmp
        if not fallback_theme_file.exists():
            shutil.copy(theme_file, fallback_theme_file)

        return fallback_config_theme_file, fallback_theme_file


def get_current_theme():
    user_config_theme_file, _ = ensure_config_exists()
    with open(user_config_theme_file, 'r') as file:
        config_ = json.load(file)
    return config_.get("theme")


def get_color(name: str):
    _, user_theme_file = ensure_config_exists()
    with open(user_theme_file, 'r') as file:
        colors = json.load(file)

    theme = get_current_theme()
    return colors.get(theme, {}).get(name)


def set_theme(new_theme):
    user_config_theme_file, _ = ensure_config_exists()
    # Write the new theme to the config file
    with open(user_config_theme_file, 'w') as file:
        json.dump({'theme': new_theme}, file)

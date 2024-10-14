import json
import os
import shutil
from pathlib import Path
from babel.support import Translations

current_directory = Path(__file__).resolve().parent
parent_directory = current_directory.parent
config_dir = os.path.join(parent_directory, 'config')
config_file = os.path.join(parent_directory, 'config', 'config.json')
locales_dir = os.path.join(parent_directory, 'locales')


def ensure_config_exists():
    try:
        if os.path.exists(config_file) and os.access(config_file, os.W_OK):
            # Use the existing config file if it exists and is writable
            return Path(config_file)
        else:
            raise PermissionError
    except PermissionError:
        # Fallback to a more accessible path, such as /tmp on Linux systems
        fallback_dir = Path('/tmp/my_app_config')
        fallback_dir.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist
        fallback_config_file = fallback_dir / 'config.json'

        if not fallback_config_file.exists():
            # Copy the original config file to the writable fallback location
            shutil.copy(config_file, fallback_config_file)

        return fallback_config_file


def get_translations(language_code: str):
    try:
        translations = Translations.load(locales_dir, [language_code])
        return translations
    except Exception as e:
        print(f"Error loading translations: {e}")
        # Fallback to default language
        return Translations.load(locales_dir, ['uz'])


def translate(text: str):
    language_code = get_current_language()
    translations = get_translations(language_code)
    return translations.gettext(text)


def get_current_language():
    user_config_file = ensure_config_exists()  # Ensure config exists in writable location
    with open(user_config_file, 'r') as file:
        config = json.load(file)
    return config.get('language', 'uz')


def set_language(new_language_code):
    user_config_file = ensure_config_exists()  # Ensure config exists in writable location
    # Write the new language code to the config file
    with open(user_config_file, 'w') as file:
        json.dump({'language': new_language_code}, file)

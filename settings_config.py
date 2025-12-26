test_settings = {
    'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'
}

def add_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()

    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()

    if key in settings.keys():
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, setting):
    key = setting.lower()

    if key in settings.keys():
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings:
        return 'No settings available.'
   
    result = "Current User Settings:\n"

    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
   
    return result

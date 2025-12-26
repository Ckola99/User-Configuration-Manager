# User Configuration Manager

## Overview

This project implements a **User Configuration Manager** that allows users to manage their application settings such as theme, language, notifications, and volume. The system provides a simple interface to add, update, delete, and view user settings stored in a Python dictionary.

---

## Features

- ✅ **Add Settings**: Create new configuration settings
- ✅ **Update Settings**: Modify existing settings
- ✅ **Delete Settings**: Remove unwanted settings
- ✅ **View Settings**: Display all current settings in a formatted view
- ✅ **Case-insensitive**: All keys and values are normalized to lowercase
- ✅ **Validation**: Prevents duplicate additions and invalid updates/deletions

---

## Functions

### `add_setting(settings, setting)`

Adds a new setting to the configuration dictionary.

#### Parameters
- `settings` (dict): The dictionary containing all user settings
- `setting` (tuple): A tuple containing `(key, value)` to be added

#### Returns
- Success message if the setting is added
- Error message if the setting already exists

#### Behavior
- Converts both key and value to lowercase
- Checks if the key already exists in the dictionary
- Adds the setting if it doesn't exist

#### Example
```python
test_settings = {'theme': 'dark'}
result = add_setting(test_settings, ('Language', 'English'))
# Returns: "Setting 'language' added with value 'english' successfully!"
# test_settings is now: {'theme': 'dark', 'language': 'english'}

# Attempting to add duplicate
result = add_setting(test_settings, ('Theme', 'Light'))
# Returns: "Setting 'theme' already exists! Cannot add a new setting with this name."
```

---

### `update_setting(settings, setting)`

Updates an existing setting in the configuration dictionary.

#### Parameters
- `settings` (dict): The dictionary containing all user settings
- `setting` (tuple): A tuple containing `(key, value)` to be updated

#### Returns
- Success message if the setting is updated
- Error message if the setting doesn't exist

#### Behavior
- Converts both key and value to lowercase
- Checks if the key exists in the dictionary
- Updates the value if the key exists

#### Example
```python
test_settings = {'theme': 'dark', 'volume': 'high'}
result = update_setting(test_settings, ('Volume', 'Low'))
# Returns: "Setting 'volume' updated to 'low' successfully!"
# test_settings is now: {'theme': 'dark', 'volume': 'low'}

# Attempting to update non-existing setting
result = update_setting(test_settings, ('Language', 'Spanish'))
# Returns: "Setting 'language' does not exist! Cannot update a non-existing setting."
```

---

### `delete_setting(settings, setting)`

Deletes a setting from the configuration dictionary.

#### Parameters
- `settings` (dict): The dictionary containing all user settings
- `setting` (str): The key of the setting to be deleted

#### Returns
- Success message if the setting is deleted
- Error message if the setting doesn't exist

#### Behavior
- Converts the key to lowercase
- Checks if the key exists in the dictionary
- Removes the setting if it exists

#### Example
```python
test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
result = delete_setting(test_settings, 'Notifications')
# Returns: "Setting 'notifications' deleted successfully!"
# test_settings is now: {'theme': 'dark', 'volume': 'high'}

# Attempting to delete non-existing setting
result = delete_setting(test_settings, 'Language')
# Returns: "Setting not found!"
```

---

### `view_settings(settings)`

Displays all current settings in a formatted string.

#### Parameters
- `settings` (dict): The dictionary containing all user settings

#### Returns
- A formatted string displaying all settings
- "No settings available." if the dictionary is empty

#### Behavior
- Returns a message if no settings exist
- Formats settings with capitalized keys
- Each setting appears on a new line

#### Example
```python
test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
result = view_settings(test_settings)
print(result)
```

**Output:**
```
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high
```

**Empty Settings:**
```python
result = view_settings({})
# Returns: "No settings available."
```

---

## Usage

### Basic Example

```python
# Initialize settings dictionary
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

# View current settings
print(view_settings(test_settings))

# Add a new setting
add_setting(test_settings, ('Language', 'English'))

# Update an existing setting
update_setting(test_settings, ('Theme', 'Light'))

# Delete a setting
delete_setting(test_settings, 'Volume')

# View updated settings
print(view_settings(test_settings))
```

### Complete Workflow Example

```python
# Start with empty settings
user_settings = {}

# Add multiple settings
add_setting(user_settings, ('Theme', 'Dark'))
add_setting(user_settings, ('Language', 'English'))
add_setting(user_settings, ('Notifications', 'Enabled'))
add_setting(user_settings, ('Volume', 'Medium'))

# Display settings
print(view_settings(user_settings))

# Update theme preference
update_setting(user_settings, ('Theme', 'Light'))

# Remove volume setting
delete_setting(user_settings, 'Volume')

# Final settings view
print(view_settings(user_settings))
```

---

## Key Features Explained

### Case Normalization

All keys and values are automatically converted to lowercase for consistency:

```python
add_setting(test_settings, ('THEME', 'DARK'))
# Stored as: {'theme': 'dark'}
```

### Duplicate Prevention

The system prevents adding duplicate settings:

```python
test_settings = {'theme': 'dark'}
add_setting(test_settings, ('Theme', 'Light'))
# Returns error message, setting not added
```

### Safe Updates and Deletions

Operations only succeed on existing settings:

```python
update_setting({}, ('theme', 'dark'))
# Returns error: setting doesn't exist

delete_setting({}, 'theme')
# Returns: "Setting not found!"
```

---

## Testing

### Sample Test Data

```python
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}
```

### Test Scenarios

#### Test 1: Add New Setting
```python
result = add_setting(test_settings, ('Language', 'English'))
assert 'language' in test_settings
assert result == "Setting 'language' added with value 'english' successfully!"
```

#### Test 2: Add Duplicate Setting
```python
result = add_setting(test_settings, ('Theme', 'Light'))
assert result == "Setting 'theme' already exists! Cannot add a new setting with this name."
```

#### Test 3: Update Existing Setting
```python
result = update_setting(test_settings, ('Volume', 'Low'))
assert test_settings['volume'] == 'low'
assert result == "Setting 'volume' updated to 'low' successfully!"
```

#### Test 4: Update Non-existing Setting
```python
result = update_setting(test_settings, ('Brightness', 'High'))
assert result == "Setting 'brightness' does not exist! Cannot update a non-existing setting."
```

#### Test 5: Delete Existing Setting
```python
result = delete_setting(test_settings, 'Notifications')
assert 'notifications' not in test_settings
assert result == "Setting 'notifications' deleted successfully!"
```

#### Test 6: Delete Non-existing Setting
```python
result = delete_setting(test_settings, 'Language')
assert result == "Setting not found!"
```

#### Test 7: View Settings
```python
result = view_settings(test_settings)
assert "Current User Settings:" in result
assert "Theme:" in result
```

#### Test 8: View Empty Settings
```python
result = view_settings({})
assert result == "No settings available."
```

---

## Code Structure

```
.
├── README.md
└── user_config_manager.py
```

### Main Components

1. **`add_setting()`**: Handles adding new configuration settings
2. **`update_setting()`**: Manages updates to existing settings
3. **`delete_setting()`**: Removes settings from the configuration
4. **`view_settings()`**: Displays all current settings in a formatted view
5. **`test_settings`**: Sample dictionary for testing functionality

---

## Design Principles

- 🔒 **Immutability Protection**: Checks existence before modifications
- 📝 **Clear Messaging**: Descriptive success and error messages
- 🔤 **Case Normalization**: Consistent lowercase storage
- ✨ **Simple Interface**: Easy-to-use function signatures
- 🎯 **Single Responsibility**: Each function has one clear purpose

---

## Common Use Cases

### Application Settings
```python
app_settings = {}
add_setting(app_settings, ('Theme', 'Dark'))
add_setting(app_settings, ('Font Size', '14'))
add_setting(app_settings, ('Auto Save', 'Enabled'))
```

### User Preferences
```python
user_prefs = {}
add_setting(user_prefs, ('Language', 'English'))
add_setting(user_prefs, ('Time Zone', 'UTC'))
add_setting(user_prefs, ('Date Format', 'MM/DD/YYYY'))
```

### Notification Settings
```python
notif_settings = {}
add_setting(notif_settings, ('Email', 'Enabled'))
add_setting(notif_settings, ('SMS', 'Disabled'))
add_setting(notif_settings, ('Push', 'Enabled'))
```

---

## Error Handling

The system provides clear error messages for various scenarios:

| Scenario | Error Message |
|----------|---------------|
| Adding duplicate setting | `Setting '[key]' already exists! Cannot add a new setting with this name.` |
| Updating non-existing setting | `Setting '[key]' does not exist! Cannot update a non-existing setting.` |
| Deleting non-existing setting | `Setting not found!` |
| Viewing empty settings | `No settings available.` |

---

## Dependencies

- **Python 3.6+**
- **No external dependencies**: Uses only Python built-in features

---

## Best Practices

1. **Initialize Settings**: Start with a dictionary containing default settings
2. **Validate Input**: The functions handle validation internally
3. **Check Return Messages**: Use return messages to verify operation success
4. **Use Consistent Keys**: Even though case is normalized, use consistent naming
5. **Handle Empty State**: Always check for empty settings before operations

---

## Future Enhancements

Potential improvements for the project:

- [ ] Add setting validation (e.g., specific allowed values)
- [ ] Implement setting categories/groups
- [ ] Add bulk operations (add/update/delete multiple settings)
- [ ] Export/import settings to JSON or YAML
- [ ] Add setting history and undo functionality
- [ ] Implement setting encryption for sensitive data
- [ ] Add type checking for setting values
- [ ] Create a CLI interface

---

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests for new functionality
5. Submit a pull request

---

## License

This project is provided for educational purposes. No license restrictions are applied.

---

## Author

Created as a Python configuration management utility example.

---

## Changelog

### Version 1.0.0
- Initial release
- Basic CRUD operations for settings
- Case-insensitive key handling
- Formatted settings display

---

## Support

If you have questions or encounter issues:
- Open an issue on the project repository
- Check existing documentation
- Review test cases for usage examples

---

## Acknowledgments

Built as part of a programming lab exercise to demonstrate:
- Dictionary manipulation in Python
- Function design and implementation
- Error handling and validation
- User-friendly messaging

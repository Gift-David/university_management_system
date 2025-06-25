import json
import os

# Reads a JSON file and returns the data
def read_json(filepath):
    if not os.path.exists(filepath):
        return []
    
    with open(filepath, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
 
# Writes a python object
def write_json(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

# Appends a new record to a list stored in a JSON file
def append_to_json(filepath, new_record):
    data = read_json(filepath)
    data.append(new_record)
    write_json(filepath, data)
    
# Updates a record in a list of dicts
def update_json_record(filepath, key, value, update_data):
    data = read_json(filepath)
    updated = False
    for record in data:
        if record.get(key) == value:
            record.update(update_data)
            updated = True
            break
    if updated:
        write_json(filepath, data)
    
    return updated

# Deletes a record from a JSON file
def delete_json_record(filepath, key, value):
    data = read_json(filepath)
    new_data = [record for record in data if record.get(key) != value]
    deleted = len(data) != len(new_data)
    if deleted:
        write_json(filepath, new_data)
    return deleted
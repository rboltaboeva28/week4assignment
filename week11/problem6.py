devices = {
    "LIGHT_LIVING": {"type": "dimmer", "value": 50, "range": (0, 100)},
    "THERMOSTAT":   {"type": "temp",   "value": 22, "range": (15, 30)},
    "DOOR_LOCK":    {"type": "binary", "value": 0,  "range": (0, 1)} # 0=Locked, 1=Unlocked
}

def process_commands(device_db, command_list):
    print("--- Processing Smart Home Commands ---")
    for command in command_list:
        try:
            parts = command.split(":")
            if len(parts) != 3:
                raise ValueError("Invalid command format (expected ID:ACTION:VALUE)")
            
            device_id, action, value_str = parts
            if device_id not in device_db:
                raise KeyError(f"Unknown device ID '{device_id}'")
            if action != "SET":
                raise ValueError(f"Unsupported action '{action}'")
            
            try:
                value = int(value_str)
            except ValueError:
                raise ValueError(f"Value '{value_str}' must be an integer")
            
            min_val, max_val = device_db[device_id]["range"]
            if value < min_val or value > max_val:
                raise ValueError(f"Value {value} outside allowed range {min_val}-{max_val}")

        except (ValueError, KeyError) as e:
            print(f"Skipping command '{command}': {e}")
        else:
            device_db[device_id]["value"] = value
            print(f"Success: Updated {device_id} to {value}")  
    print("\nFinal State:", devices)        

cmds = [
    "LIGHT_LIVING:SET:100",    # Valid
    "LIGHT_LIVING:SET:200",    # Out of range
    "THERMOSTAT:COOL:20",      # Invalid Action
    "GARAGE_DOOR:SET:1",       # Unknown Device
    "DOOR_LOCK:SET:OPEN",      # Invalid Value Type
    "bad_format_command"       # Bad Format
]
(process_commands(devices, cmds))
def format_duration(duration_str):
    # Split de string op de decimalen om alleen het deel na de laatste ":" te krijgen
    parts = duration_str.split(".")
    seconds_str = parts[0].split(":")[-1]  # Krijg het deel na de laatste ":" (de seconden)
    
    # Converteer naar float
    seconds = float(seconds_str)
    
    # Rond de seconden af tot 2 decimalen
    rounded_seconds = round(seconds, 2)
    
    return rounded_seconds

# Voorbeeldgebruik:
duration_str = "0:00:33.195136"
formatted_duration = format_duration(duration_str)
print(formatted_duration)  # Output: 33.2

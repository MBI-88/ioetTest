from datetime import datetime

"""
This script is the data struture for validating payments.
"""
payKeys: dict[str, list[tuple[datetime, datetime, int]]] = {
    "Week": [
        (datetime.strptime("00:01", "%H:%M").time(),
         datetime.strptime("09:00", "%H:%M").time(), 25),  
        (datetime.strptime("09:01", "%H:%M").time(),
         datetime.strptime("18:00", "%H:%M").time(), 15),
        (datetime.strptime("18:01", "%H:%M").time(),
         datetime.strptime("23:00", "%H:%M").time(), 20),
    ],
    "Weekend": [
        (datetime.strptime("00:01", "%H:%M").time(),
         datetime.strptime("09:00", "%H:%M").time(), 30),
        (datetime.strptime("09:01", "%H:%M").time(),
         datetime.strptime("18:00", "%H:%M").time(), 20),
        (datetime.strptime("18:01", "%H:%M").time(),
         datetime.strptime("23:00", "%H:%M").time(), 25),
    ]
}
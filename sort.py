import json
import os


PARKING_FILE = "parking_data.json"

# Directions from Main Entry to clusters
cluster_directions = {
    "Cluster 1": "Turn Left",
    "Cluster 2": "Turn Right"
}

# Slot positions (Clockwise, Slot 3 is the Middle)
slot_directions = {
    "Cluster 1": {1: "Left", 2: "Left", 3: "Straight", 4: "Right", 5: "Right"},
    "Cluster 2": {1: "Right", 2: "Right", 3: "Straight", 4: "Left", 5: "Left"}
}

# Function to load parking data from file
def load_parking_data():
    if os.path.exists(PARKING_FILE):
        with open(PARKING_FILE, "r") as file:
            return json.load(file)
    else:
        return {
            "Cluster 1": [0, 0, 0, 0, 0],  # Five slots in Cluster 1
            "Cluster 2": [0, 0, 0, 0, 0]   # Five slots in Cluster 2
        }


def save_parking_data(data):
    with open(PARKING_FILE, "w") as file:
        json.dump(data, file)


parking_slots = load_parking_data()

# Function to display parking slots
def display_parking():
    print("\n Current Parking Status:")
    for cluster, slots in parking_slots.items():
        print(f"{cluster}: {['Occupied' if s else 'Available' for s in slots]}")

# Function to find an available slot
def find_parking_slot(cluster, desired_slot):
    if parking_slots[cluster][desired_slot - 1] == 0:
        return desired_slot
    else:
        print("\n Desired slot is occupied! Finding nearest available slot...")
        for i in range(5):  # Check all slots in the cluster
            if parking_slots[cluster][i] == 0:
                return i + 1  # Slots are 1-based index
        return None  # No available slots


print("\n Welcome to Smart Parking!")
cluster_choice = input("Choose a cluster (1 or 2): ")
cluster_key = f"Cluster {cluster_choice}"

if cluster_key not in parking_slots:
    print(" Invalid cluster! Exiting...")
else:
    #  Shows direction to cluster
    print(f"\n➡ From Main Entry: **{cluster_directions[cluster_key]}** to reach **{cluster_key}**.")

    display_parking()
    
    #  User input: Choose slot
    desired_slot = int(input("Enter desired slot number (1-5): "))
    
    # Check for available slots
    assigned_slot = find_parking_slot(cluster_key, desired_slot)
    
    if assigned_slot:
        parking_slots[cluster_key][assigned_slot - 1] = 1  # Mark slot as occupied
        direction = slot_directions[cluster_key][assigned_slot]  # Get direction
        print(f"\n Park at **{cluster_key}, Slot {assigned_slot}**.")
        print(f" Direction to park: **{direction}**")
        
        # Save updated parking data
        save_parking_data(parking_slots)
    else:
        print("\n No available slots in this cluster!")

    display_parking()  # Show updated parking

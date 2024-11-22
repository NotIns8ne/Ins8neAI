import os
import json
import hashlib
import uuid
import time

# Constants
OWNER_USERNAME = "NotIns8ne"
PAYMENT_FILE = "payments.json"
PARTNER_PROGRAMS_FILE = "partner_programs.json"
STORE_CREATION_FEE = 30  # Fee per store created
BASE_PRICE = 50  # Minimum donation for advanced features

# Function to mark a payment
def mark_payment(username, amount):
    if not os.path.exists(PAYMENT_FILE):
        with open(PAYMENT_FILE, "w") as f:
            json.dump({}, f)

    with open(PAYMENT_FILE, "r") as f:
        payment_data = json.load(f)

    if username not in payment_data:
        payment_data[username] = {"total_paid": 0, "transactions": []}

    payment_data[username]["total_paid"] += amount
    payment_data[username]["transactions"].append({
        "amount": amount,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(PAYMENT_FILE, "w") as f:
        json.dump(payment_data, f)

    print(f"✅ Payment of ${amount} recorded for {username}.")

# Function to create a store
def create_store(store_name):
    mark_payment(OWNER_USERNAME, STORE_CREATION_FEE)
    store_key = str(uuid.uuid4())  # Generate a unique key for the store
    print(f"🛒 Store '{store_name}' created successfully! A fee of ${STORE_CREATION_FEE} has been charged.")
    print(f"🔑 Your store key: {store_key}")
    return store_key

# Function to setup partner programs
def setup_partner_programs():
    if not os.path.exists(PARTNER_PROGRAMS_FILE):
        partner_data = {
            "GoDaddy": {
                "api_key": "",
                "secret": "",
                "account_id": ""
            },
            "Shopify": {
                "api_key": "",
                "secret": "",
                "store_url": ""
            }
        }
        with open(PARTNER_PROGRAMS_FILE, "w") as f:
            json.dump(partner_data, f)
        print("🔧 Partner programs setup file created. Please enter your details.")

# Function to auto-update partner program details
def auto_update_payment_details():
    setup_partner_programs()
    with open(PARTNER_PROGRAMS_FILE, "r") as f:
        partner_data = json.load(f)

    for program, details in partner_data.items():
        if not details["api_key"] or not details["secret"]:
            print(f"⚠️ Please enter your {program} API key and secret.")
            details["api_key"] = input(f"Enter {program} API key: ")
            details["secret"] = input(f"Enter {program} secret: ")

    with open(PARTNER_PROGRAMS_FILE, "w") as f:
        json.dump(partner_data, f)
    print("✅ Partner program details have been updated.")

def main():
    auto_update_payment_details()
    while True:
        command = input("Enter 'create_store <store_name>' to create a store or 'exit' to quit: ")
        if command.lower() == 'exit':
            break
        
        parts = command.split()
        if parts[0] == 'create_store' and len(parts) > 1:
            create_store(parts[1])
        else:
            print("❌ Invalid command. Please try again.")

if __name__ == "__main__":
    main()
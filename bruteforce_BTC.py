import bitcoin
import random
import time

# Function to brute force a private key
def brute_force_private_key(target_address):
    start_time = time.time()
    attempts = 0
    
    while True:
        # Generate a random private key
        private_key = bitcoin.random_key()
        public_key = bitcoin.privtopub(private_key)
        address = bitcoin.pubtoaddr(public_key)
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the generated address matches the target
        if address == target_address:
            end_time = time.time()
            print(f"Private Key Found: {private_key}")
            print(f"Public Address: {address}")
            print(f"Total Attempts: {attempts}")
            print(f"Time Taken: {end_time - start_time} seconds")
            break
        
        # Optional: Limit the number of attempts to avoid infinite loop
        if attempts % 1000000 == 0:
            print(f"Attempts: {attempts}")

# Example usage
target_address = "YOUR_TARGET_ADDRESS_HERE"
brute_force_private_key(target_address)

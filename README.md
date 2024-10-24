# Bitcoin Private Key Brute Forcer

This Python script attempts to **brute force a Bitcoin private key** by generating random keys until it matches a given public Bitcoin address. The process demonstrates the infeasibility of brute-forcing real Bitcoin addresses due to the **astronomical size of the key space**.

---

## 🚨 Disclaimer

This project is for **educational purposes only**. Attempting to brute force private keys of Bitcoin addresses without authorization is **illegal** and unethical. Bitcoin addresses are secure because of their cryptographic strength, and this script serves only to illustrate how improbable it is to guess a valid key.

---

## Features

- **Random Key Generation**: Generates private keys and converts them to public addresses.
- **Brute Force Logic**: Compares the generated address to a target address.
- **Progress Reporting**: Tracks the number of attempts and elapsed time.
- **Performance**: Reports status every 1 million attempts to monitor progress.

---

## Prerequisites

1. **Python 3.x** installed on your machine.
2. Install the required Bitcoin library:
   ```bash
   pip install bitcoin

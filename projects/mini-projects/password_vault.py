import os
import json
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PasswordVault:
    def __init__(self, master_password):
        self.salt = b'fixed_salt_for_demo' # In real app, use a random salt stored securely
        self.key = self._derive_key(master_password)
        self.fernet = Fernet(self.key)
        self.db_file = 'vault.json'
        self.data = self._load_data()

    def _derive_key(self, password):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def _load_data(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_data(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def add_password(self, site, username, password):
        encrypted_pwd = self.fernet.encrypt(password.encode()).decode()
        self.data[site] = {'user': username, 'pass': encrypted_pwd}
        self._save_data()
        print(f"Stored credentials for {site}")

    def get_password(self, site):
        if site in self.data:
            entry = self.data[site]
            decrypted_pwd = self.fernet.decrypt(entry['pass'].encode()).decode()
            return f"User: {entry['user']}\nPass: {decrypted_pwd}"
        return "Not found."

def main():
    print("--- Secure Password Vault ---")
    master = input("Enter Master Password: ")
    vault = PasswordVault(master)

    while True:
        print("\n1. Add Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == '1':
            site = input("Site: ")
            user = input("Username: ")
            pwd = input("Password: ")
            vault.add_password(site, user, pwd)
        elif choice == '2':
            site = input("Site: ")
            print(vault.get_password(site))
        elif choice == '3':
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")

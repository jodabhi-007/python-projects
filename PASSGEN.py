import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."

    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password (or '0' to exit): "))
            if length == 0:
                print("Exiting the password generator. Goodbye!")
                break
            elif length < 1:
                print("Please enter a positive integer for the password length.")
                continue
            
            password = generate_password(length)
            print(f"Generated Password: {password}")
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
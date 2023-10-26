import random

# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# List of exit messages
exit_messages = [
    "Goodbye!",
    "Thanks for using the program. Goodbye!",
    "Have a great day!",
    "See you later!",
]

# Main function
def main():
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print(random.choice(exit_messages))  # Display a random exit message
            restart = input("Enter 's' to start again, or press Enter to exit: ")
            if restart.lower() == 's':
                continue  # Start the program again
            else:
                print("Goodbye!")
                break
        try:
            num = int(user_input)
            result = check_odd_even(num)
            print(f"{num} is {result}.")
        except ValueError:
            print("Please enter a valid number.")

# Entry point of the program
if __name__ == "__main__":
    main()

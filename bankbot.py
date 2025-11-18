# Bank Chatbot
# Helps new customers choose an account type and start sign-up steps

def bank_bot():
    print("Welcome to SwiftBank Virtual Assistant.")
    name = input("May I have your name, please? ")
    print(f"Hello {name}, I'm here to help you open a new account.")

    print("\nHere are the account types we offer:")
    print("1. Checking Account - Best for everyday transactions.")
    print("2. Savings Account - Great for earning interest on your balance.")
    print("3. Business Account - For managing your company finances.")
    
    choice = input("Please enter the number for the account you'd like to open: ")

    if choice == "1":
        print("\nExcellent choice! A Checking Account lets you manage bills and payments easily.")
    elif choice == "2":
        print("\nA Savings Account is perfect if you want to earn interest while saving money.")
    elif choice == "3":
        print("\nOur Business Account helps manage your company finances efficiently.")
    else:
        print("\nI'm sorry, I didn’t understand that. Please restart and choose a valid option.")
        return
    
    deposit = input("\nWould you like to make an initial deposit today? (yes/no): ").lower()
    if deposit == "yes":
        amount = input("Great! How much would you like to deposit? $")
        print(f"Thank you, {name}. We’ve recorded your initial deposit of ${amount}.")
    else:
        print("No problem. You can deposit funds anytime after your account is created.")
    
    print("\nYour application has been started. A representative will contact you shortly to finalize the setup.")
    print("Thank you for choosing SwiftBank!")

bank_bot()

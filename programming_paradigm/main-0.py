# main.py

import argparse
from bank_account import BankAccount

def main():
    """
    Main function to parse command-line arguments and perform banking operations.
    """
    parser = argparse.ArgumentParser(
        description="Perform banking operations on a BankAccount.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Using a single-action approach to handle operations
    parser.add_argument('operation', choices=['deposit', 'withdraw', 'balance'],
                        help="""The operation to perform.
  'deposit' - Adds funds to the account.
  'withdraw' - Removes funds from the account.
  'balance' - Displays the current balance.
""")
    parser.add_argument('--amount', type=float, 
                        help="The amount for 'deposit' or 'withdraw' operations.")

    args = parser.parse_args()

    # Create a BankAccount instance for testing.
    # We'll start with a balance of $100 for demonstration.
    account = BankAccount(100.00)

    print("---------------------------------------")
    print("Welcome to the Python Bank Account CLI.")
    print("Initial Balance: $100.00")
    print("---------------------------------------")

    try:
        if args.operation == 'deposit':
            if args.amount is None:
                parser.error("The '--amount' argument is required for 'deposit'.")
            account.deposit(args.amount)
            print(f"Successfully deposited: ${args.amount:,.2f}")
        
        elif args.operation == 'withdraw':
            if args.amount is None:
                parser.error("The '--amount' argument is required for 'withdraw'.")
            if account.withdraw(args.amount):
                print(f"Successfully withdrew: ${args.amount:,.2f}")
            else:
                print("Transaction failed: Insufficient funds.")
        
        elif args.operation == 'balance':
            account.display_balance()

        # Always show the final balance after an operation (except for balance command itself)
        if args.operation != 'balance':
            print("---------------------------------------")
            account.display_balance()
            print("---------------------------------------")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
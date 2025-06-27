# Section 2: Data Structures & Algorithms
# Q3: Greedy Minimize Coins

def minimize_coins(amount):
    
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = {}  

    remaining = amount
    for coin in denominations:
        count = remaining // coin        
        if count > 0:
            result[coin] = count
            remaining -= coin * count    
    return result

def main():
    
    amt_str = input("Enter amount (integer) to change: ").strip()
    if not amt_str.isdigit():
        print("Invalid input; please enter a positive integer.")
        return

    amt = int(amt_str)
    if amt <= 0:
        print("Amount must be greater than zero.")
        return

    coins_used = minimize_coins(amt)
    print(f"Minimum coins/notes for Rs.{amt}:")
    for coin, cnt in coins_used.items():
        print(f"  Rs.{coin} x {cnt}")

if __name__ == "__main__":
    main()

# Section 1: Python Programming & OOP
# Q1: Functional Movie Booking System

movies = ["Avengers", "Inception", "The Matrix", "Parasite"]
prices = {
    "Avengers": 250,
    "Inception": 200,
    "The Matrix": 180,
    "Parasite": 150
}

def show_movies():
    
    print("Available Movies:")
    for i in range(len(movies)):
        name = movies[i]
        cost = prices[name]
        print(f"  {i+1}. {name} – Rs.{cost}")

def calculate_amount(movie_name, ticket_count):
    price_per_ticket = prices.get(movie_name, 0)
    return price_per_ticket * ticket_count

def book_tickets():
    
    show_movies()
    
    choice = input("Enter the movie number you want to book: ").strip()
    if not choice.isdigit():
        print("Invalid input: please enter a number.")
        return
    choice = int(choice)
    if choice < 1 or choice > len(movies):
        print("Invalid selection: that movie number does not exist.")
        return
    
    selected_movie = movies[choice - 1]
    
    qty = input(f"How many tickets for '{selected_movie}'? ").strip()
    if not qty.isdigit():
        print("Invalid input: please enter a number of tickets.")
        return
    qty = int(qty)
    if qty <= 0:
        print("Invalid quantity: you must book at least one ticket.")
        return
    
    total = calculate_amount(selected_movie, qty)
    print(f"You have booked {qty} ticket(s) for '{selected_movie}'.")
    print(f"Total amount: Rs.{total}")


if __name__ == "__main__":
    book_tickets()


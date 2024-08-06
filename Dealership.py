import random
import string
import json
import os
from colorama import Fore, Style, init

init(autoreset=True)

def format_price(price):
    if price >= 1_000_000:
        return f"${price / 1_000_000:.1f}M"
    elif price >= 1_000:
        return f"${price / 1_000:.1f}K"
    else:
        return f"${price:.2f}"

class CarDealershipSimulator:
    def __init__(self):
        self.luxury_cars = ["Rolls Royce", "Maybach", "Bmw Alphina", "Bentley", "Aston Martin"]
        self.sports_cars = ["Mclaren", "Lamborghini", "Porsche", "Ferrari", "Bugatti"]
        self.economy_cars = ["Alfa Romeo", "Ford", "Toyota", "Mini Cooper", "Honda", "Nissan"]
        self.carmodels = self.luxury_cars + self.sports_cars + self.economy_cars
        self.carvalue = {
            "Rolls Royce": 500_000,
            "Maybach": 200_000,
            "Bmw Alphina": 150_000,
            "Bentley": 250_000,
            "Aston Martin": 180_000,
            "Alfa Romeo": 50_000,
            "Mclaren": 400_000,
            "Lamborghini": 300_000,
            "Ford": 40_000,
            "Toyota": 50_000,
            "Porsche": 150_000,
            "Mini Cooper": 60_000,
            "Ferrari": 350_000,
            "Bugatti": 700_000,
            "Honda": 30_000,
            "Nissan": 35_000
        }
        self.carmileage = {
            "Rolls Royce": 10,
            "Maybach": 15,
            "Bmw Alphina": 20,
            "Bentley": 8,
            "Aston Martin": 12,
            "Alfa Romeo": 25,
            "Mclaren": 5,
            "Lamborghini": 8,
            "Ford": 30,
            "Toyota": 35,
            "Porsche": 18,
            "Mini Cooper": 28,
            "Ferrari": 6,
            "Bugatti": 4,
            "Honda": 40,
            "Nissan": 38
        }
        self.carcondition = {
            "Rolls Royce": "New",
            "Maybach": "New",
            "Bmw Alphina": "New",
            "Bentley": "New",
            "Aston Martin": "New",
            "Alfa Romeo": "Used",
            "Mclaren": "New",
            "Lamborghini": "New",
            "Ford": "Used",
            "Toyota": "Used",
            "Porsche": "New",
            "Mini Cooper": "Used",
            "Ferrari": "New",
            "Bugatti": "New",
            "Honda": "Used",
            "Nissan": "Used"
        }
        self.carage = {
            "Rolls Royce": 0,
            "Maybach": 0,
            "Bmw Alphina": 0,
            "Bentley": 0,
            "Aston Martin": 0,
            "Alfa Romeo": 3,
            "Mclaren": 0,
            "Lamborghini": 0,
            "Ford": 5,
            "Toyota": 4,
            "Porsche": 0,
            "Mini Cooper": 6,
            "Ferrari": 0,
            "Bugatti": 0,
            "Honda": 5,
            "Nissan": 4
        }
        self.money = 1_000_000
        self.total_money = 0
        self.cars_bought = 0
        self.years = 0
        self.current_year = 2023
        self.owned = {}
        self.price_history = {model: [price] for model, price in self.carvalue.items()}
        self.car_history = {model: {"owners": 0, "maintenance": []} for model in self.carmodels}
        self.income_history = []
        self.expense_history = []

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        while True:
            self.clear_console()
            print(Fore.CYAN + Style.BRIGHT + "Welcome to the Advanced Car Dealership Simulator!")
            print(Fore.GREEN + "\nMain Menu:")
            print(Fore.YELLOW + "1. View available cars")
            print("2. Buy a car")
            print("3. View your owned cars")
            print("4. Sell a car")
            print("5. Add your own car")
            print("6. Simulate next year")
            print("7. Save game")
            print("8. Load game")
            print("9. View user guide")
            print("10. Exit")
            choice = input(Fore.MAGENTA + "Enter your choice: ")
            if choice == '1':
                self.view_available_cars()
            elif choice == '2':
                self.buy_car_menu()
            elif choice == '3':
                self.view_owned_cars()
            elif choice == '4':
                self.sell_car()
            elif choice == '5':
                self.add_user_car()
            elif choice == '6':
                self.simulate()
            elif choice == '7':
                self.save_game()
            elif choice == '8':
                self.load_game()
            elif choice == '9':
                self.view_user_guide()
            elif choice == '10':
                print(Fore.CYAN + "Exiting the game. Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")

    def view_available_cars(self):
        self.clear_console()
        print(Fore.GREEN + Style.BRIGHT + "Available Cars:")
        for key in self.carvalue:
            print(f"{Fore.YELLOW}{key}: {format_price(self.carvalue[key])} | Mileage: {self.carmileage[key]}k miles | Condition: {self.carcondition[key]} | Age: {self.carage[key]} years")
        input(Fore.CYAN + "\nPress Enter to return to the main menu...")

    def buy_car_menu(self):
        while True:
            self.clear_console()
            print(Fore.GREEN + "\nBuy a Car Menu:")
            print(Fore.YELLOW + "1. View Luxury Cars")
            print("2. View Sports Cars")
            print("3. View Economy Cars")
            print("4. Return to Main Menu")
            choice = input(Fore.MAGENTA + "Enter your choice: ")
            if choice == '1':
                self.buy_car("Luxury", self.luxury_cars)
            elif choice == '2':
                self.buy_car("Sports", self.sports_cars)
            elif choice == '3':
                self.buy_car("Economy", self.economy_cars)
            elif choice == '4':
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")

    def buy_car(self, category, car_list):
        self.clear_console()
        print(Fore.GREEN + f"\n{category} Cars:")
        for key in car_list:
            print(f"{Fore.YELLOW}{key}: {format_price(self.carvalue[key])} | Mileage: {self.carmileage[key]}k miles | Condition: {self.carcondition[key]} | Age: {self.carage[key]} years")
        carname = string.capwords(input(Fore.MAGENTA + "\nWhich car would you like to buy? (or type 'back' to return): "))
        if carname.lower() == 'back':
            return
        if carname in car_list:
            print(f"{Fore.YELLOW}{carname}: {format_price(self.carvalue[carname])} | Mileage: {self.carmileage[carname]}k miles | Condition: {self.carcondition[carname]} | Age: {self.carage[carname]} years")
            buythiscar = input(Fore.MAGENTA + "Do you want to buy this car? (yes or no): ").lower()
            if buythiscar == "yes":
                negotiation = random.randint(-5000, 5000)
                final_price = max(0, self.carvalue[carname] + negotiation)
                if self.money - final_price >= 0:
                    if carname in self.owned:
                        print(Fore.RED + "You already own this car.")
                    else:
                        self.owned[carname] = 1
                        self.money -= final_price
                        self.car_history[carname]["owners"] += 1
                        self.expense_history.append({"type": "purchase", "amount": final_price, "car": carname, "year": self.current_year})
                        print(f"{Fore.GREEN}You bought a {carname} for {format_price(final_price)}.")
                else:
                    print(Fore.RED + "You don't have enough money.")
            else:
                print(Fore.CYAN + "Purchase cancelled.")
        else:
            print(Fore.RED + "Invalid car model.")
        input(Fore.CYAN + "\nPress Enter to return to the previous menu...")

    def view_owned_cars(self):
        self.clear_console()
        print(Fore.GREEN + Style.BRIGHT + "Your Owned Cars:")
        for key in self.owned:
            print(f"{Fore.YELLOW}{key}: {self.owned[key]} car(s)")
            print(f"    Age: {self.carage[key]} years | Mileage: {self.carmileage[key]}k miles | Condition: {self.carcondition[key]}")
            print(f"    Owners: {self.car_history[key]['owners']} | Maintenance: {self.car_history[key]['maintenance']}")
        input(Fore.CYAN + "\nPress Enter to return to the main menu...")

    def sell_car(self):
        self.clear_console()
        print(Fore.GREEN + Style.BRIGHT + "Sell a Car:")
        carname = string.capwords(input(Fore.MAGENTA + "\nWhich car would you like to sell? --> "))
        if carname in self.owned:
            sellprice = self.carvalue[carname]
            self.money += sellprice
            del self.owned[carname]
            self.income_history.append({"type": "sale", "amount": sellprice, "car": carname, "year": self.current_year})
            print(f"{Fore.GREEN}You sold your {carname} for {format_price(sellprice)}.")
        else:
            print(Fore.RED + "You do not own this car.")
        input(Fore.CYAN + "\nPress Enter to return to the main menu...")

    def add_user_car(self):
        self.clear_console()
        print(Fore.GREEN + Style.BRIGHT + "Add Your Own Car:")
        carname = string.capwords(input(Fore.MAGENTA + "\nEnter the name of the car: "))
        try:
            carprice = int(input(Fore.MAGENTA + "Enter the value of the car: $"))
            carmileage = int(input(Fore.MAGENTA + "Enter the mileage of the car: "))
            carcondition = input(Fore.MAGENTA + "Enter the condition of the car (New/Used): ").capitalize()
            carage = int(input(Fore.MAGENTA + "Enter the age of the car (years): "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter valid numbers.")
            input(Fore.CYAN + "\nPress Enter to return to the main menu...")
            return

        if carcondition not in ["New", "Used"]:
            print(Fore.RED + "Invalid condition. Please enter 'New' or 'Used'.")
            input(Fore.CYAN + "\nPress Enter to return to the main menu...")
            return

        self.carmodels.append(carname)
        self.carvalue[carname] = carprice
        self.carmileage[carname] = carmileage
        self.carcondition[carname] = carcondition
        self.carage[carname] = carage
        self.price_history[carname] = [carprice]
        self.car_history[carname] = {"owners": 0, "maintenance": []}

        print(Fore.GREEN + f"Your car {carname} has been added successfully.")
        input(Fore.CYAN + "\nPress Enter to return to the main menu...")

    def simulate(self):
        self.clear_console()
        print(Fore.CYAN + Style.BRIGHT + "\nSimulating Car Prices for the next year...")
        self.current_year += 1
        self.random_event()
        maintenance_costs = self.calculate_maintenance_costs()
        for model in self.carmodels:
            base_price = self.carvalue[model]
            depreciation = max(5000, base_price * 0.1) if self.carcondition[model] == "New" else max(2000, base_price * 0.2)
            self.carvalue[model] = max(0, base_price - depreciation + random.randint(-20000, 20000))
            self.price_history[model].append(self.carvalue[model])
            self.carage[model] += 1  # Increase the age of each car by 1 year
        print(Fore.GREEN + "\nNew Car Prices:")
        for model, price in self.carvalue.items():
            print(f"{Fore.YELLOW}{model}: {format_price(price)}")
        print(Fore.CYAN + "\nYour owned cars:")
        for key in self.owned:
            print(f"{Fore.YELLOW}{key}: {self.owned[key]} car(s)")

        self.yearly_report(maintenance_costs)
        self.calculate_profit(maintenance_costs)
        input(Fore.CYAN + "\nPress Enter to return to the main menu...")

    def calculate_maintenance_costs(self):
        total_cost = 0
        for car in self.owned:
            age = self.carage[car]
            condition = self.carcondition[car]
            maintenance_cost = (1000 * age) if condition == "New" else (2000 * age)
            total_cost += maintenance_cost
            self.car_history[car]["maintenance"].append({"year": self.current_year, "cost": maintenance_cost})
            self.expense_history.append({"type": "maintenance", "amount": maintenance_cost, "car": car, "year": self.current_year})
        return total_cost

    def calculate_profit(self, maintenance_costs):
        profit = 0
        for car in self.owned:
            profit += self.carvalue[car]
        total_assets = self.money + profit
        print(f"\n{Fore.GREEN}Total value of your assets: {format_price(total_assets)}")
        print(f"{Fore.GREEN}Profit from car sales: {format_price(profit - sum(self.carvalue[car] for car in self.owned) - maintenance_costs)}")

    def random_event(self):
        events = [
            {"event": "economic boom", "description": "An economic boom increases car values significantly.", "impact": lambda value: value + random.randint(10000, 50000)},
            {"event": "recession", "description": "A recession decreases car values significantly.", "impact": lambda value: value - random.randint(10000, 50000)},
            {"event": "new tax law", "description": "A new tax law negatively affects car values.", "impact": lambda value: value - random.randint(5000, 25000)},
            {"event": "high demand", "description": "High demand increases car values moderately.", "impact": lambda value: value + random.randint(5000, 30000)},
            {"event": "low demand", "description": "Low demand decreases car values moderately.", "impact": lambda value: value - random.randint(5000, 30000)},
            {"event": "new technology", "description": "New technology boosts car values.", "impact": lambda value: value + random.randint(5000, 20000)},
            {"event": "market saturation", "description": "Market saturation decreases car values.", "impact": lambda value: value - random.randint(10000, 40000)},
            {"event": "natural disaster", "description": "A natural disaster significantly lowers car values.", "impact": lambda value: value - random.randint(20000, 60000)}
        ]
        event = random.choice(events)
        print(f"{Fore.MAGENTA}Random event this year: {Fore.YELLOW}{event['event']}")
        print(f"{Fore.YELLOW}{event['description']}")
        for model in self.carmodels:
            self.carvalue[model] = max(0, event["impact"](self.carvalue[model]))

    def yearly_report(self, maintenance_costs):
        print(Fore.CYAN + "\nYearly Report:")
        print(f"{Fore.YELLOW}Year: {self.current_year}")
        print(f"{Fore.YELLOW}Money: {format_price(self.money)}")
        print(f"{Fore.YELLOW}Owned Cars: {self.owned}")
        print(Fore.GREEN + "\nPrice History:")
        for model, history in self.price_history.items():
            print(f"{Fore.YELLOW}{model}: {', '.join(map(format_price, history))}")
        print(Fore.GREEN + "\nIncome History:")
        for entry in self.income_history:
            print(f"{Fore.YELLOW}{entry}")
        print(Fore.GREEN + "\nExpense History:")
        for entry in self.expense_history:
            print(f"{Fore.YELLOW}{entry}")
        print(Fore.GREEN + f"\nTotal Maintenance Costs: {format_price(maintenance_costs)}")

    def save_game(self):
        slot = input(Fore.MAGENTA + "Enter save slot number (1-3): ")
        if slot not in ['1', '2', '3']:
            print(Fore.RED + "Invalid slot number. Please choose between 1 and 3.")
            return
        game_state = {
            "money": self.money,
            "owned": self.owned,
            "current_year": self.current_year,
            "carvalue": self.carvalue,
            "price_history": self.price_history,
            "carage": self.carage,
            "car_history": self.car_history,
            "income_history": self.income_history,
            "expense_history": self.expense_history
        }
        with open(f"car_dealership_save_{slot}.json", "w") as save_file:
            json.dump(game_state, save_file)
        print(Fore.GREEN + "Game saved successfully.")
        input(Fore.CYAN + "\nPress Enter to return to the main menu...")

    def load_game(self):
        slot = input(Fore.MAGENTA + "Enter load slot number (1-3): ")
        if slot not in ['1', '2', '3']:
            print(Fore.RED + "Invalid slot number. Please choose between 1 and 3.")
            return
        if os.path.exists(f"car_dealership_save_{slot}.json"):
            with open(f"car_dealership_save_{slot}.json", "r") as save_file:
                game_state = json.load(save_file)
            self.money = game_state["money"]
            self.owned = game_state["owned"]
            self.current_year = game_state["current_year"]
            self.carvalue = game_state["carvalue"]
            self.price_history = game_state["price_history"]
            self.carage = game_state["carage"]
            self.car_history = game_state["car_history"]
            self.income_history = game_state["income_history"]
            self.expense_history = game_state["expense_history"]
            print(Fore.GREEN + "Game loaded successfully.")
        else:
            print(Fore.RED + "No saved game found in this slot. Starting a new game.")
        input(Fore.CYAN + "\nPress Enter to return to the main menu...")

    def view_user_guide(self):
        while True:
            self.clear_console()
            print(Fore.GREEN + Style.BRIGHT + "User Guide:")
            print(Fore.YELLOW + "1. View available cars: Displays the list of cars available for purchase with their details.")
            print("2. Buy a car: Allows you to purchase a car if you have enough money.")
            print("3. View your owned cars: Shows the cars you currently own along with their details.")
            print("4. Sell a car: Enables you to sell one of your owned cars.")
            print("5. Add your own car: Allows you to add a car of your own to the dealership.")
            print("6. Simulate next year: Advances the game by one year, applying random events and updating car prices.")
            print("7. Save game: Saves your current game state in one of three slots.")
            print("8. Load game: Loads a previously saved game from one of three slots.")
            print("9. Exit: Exits the game.")
            print("\n0. Return to Main Menu")
            choice = input(Fore.MAGENTA + "\nEnter your choice: ")
            if choice == '0':
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
                input(Fore.CYAN + "\nPress Enter to return to the user guide...")

if __name__ == "__main__":
    game = CarDealershipSimulator()
    game.main_menu()

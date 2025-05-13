#Jerico Branch
#4/18/2025
#PW5
#Basketball shorties

import random

class BasketballAdventure:
    def __init__(self, player_name):
        """Starting the game with player stats and starting values"""
        self.player_name = player_name  # Store player's name
        self.energy = 100              # Starting energy (0-100)
        self.skill = 50                # Basketball skill level
        self.confidence = 50           # Player confidence level
        self.inventory = ["basketball", "water bottle"]  # Starting items
        self.day = 1                   # Current day counter
        self.location = "neighborhood court"  # Starting location
        self.game_over = False        
    def display_stats(self):
        """Show current player stats and inventory"""
        print(f"\nDay {self.day} - Location: {self.location}")
        print(f"Player: {self.player_name}")
        print(f"Energy: {self.energy} | Skill: {self.skill} | Confidence: {self.confidence}")
        print(f"Inventory: {', '.join(self.inventory)}")

    def random_event(self):
        """Trigger a random in-game event"""
        events = [
            self.find_basketball_camp,
            self.meet_streetball_legend,
            self.find_energy_drink,
            self.get_injured,
            self.find_new_court,
            self.empty_event
        ]
        random.choice(events)()  # Call a random event method

    def find_basketball_camp(self):
        """Event: Discover a basketball training camp"""
        print(f"{self.player_name}, you discover a basketball camp in progress!")
        choice = input("Do you want to (1) Join for training or (2) Challenge the coach? ")

        if choice == "1":
            # Training option
            print(f"{self.player_name} spends the day learning new techniques!")
            self.skill += random.randint(5, 15)
            self.energy -= random.randint(10, 20)
        else:
            # Challenge option
            print(f"{self.player_name} challenges the coach to a 1-on-1 game!")
            win_chance = 0.3 + (self.skill / 200)  # Higher skill = better chance

            if random.random() < win_chance:
                print(f"{self.player_name} wins! The coach is impressed.")
                self.confidence += 15
                self.skill += 10
                if "coach's playbook" not in self.inventory:
                    self.inventory.append("coach's playbook")  # Reward for winning
            else:
                print(f"{self.player_name} loses, but learns valuable lessons.")
                self.confidence -= 5
                self.skill += 5
            self.energy -= 25  # Energy cost for challenge

    def meet_streetball_legend(self):
        """Event: Encounter a skilled streetball player"""
        print(f"{self.player_name}, you meet a streetball legend at the court!")

        if "lucky headband" in self.inventory:
            # Special interaction if player has the headband
            print("He recognizes your headband and offers to teach you!")
            self.skill += 20
            self.confidence += 15
            self.energy -= 15
        else:
            # Normal interaction
            print(f"He challenges {self.player_name} to a game of HORSE.")
            win_chance = 0.4 + (self.skill / 150)  # Skill affects outcome

            if random.random() < win_chance:
                print(f"{self.player_name} wins! He gives you his lucky headband.")
                self.inventory.append("lucky headband")  # New item reward
                self.confidence += 20
            else:
                print(f"{self.player_name} loses, but gains some experience.")
                self.skill += 10
            self.energy -= 20

    def find_energy_drink(self):
        """Event: Find an energy-boosting item"""
        print("You find an unopened energy drink on the bench!")
        self.inventory.append("energy drink")
        print("Added energy drink to your inventory!")

    def get_injured(self):
        """Event: Player gets injured with random severity"""
        injury = random.choice(["sprained ankle", "sore wrist", "tired legs"])
        print(f"Oh snaps! {self.player_name} has developed a {injury} from overtraining!")
        self.energy -= random.randint(15, 30)

        # Check if player can use energy drink to recover
        if "energy drink" in self.inventory:
            use = input("Use energy drink to recover? (y/n) ").lower()
            if use == "y":
                self.inventory.remove("energy drink")
                self.energy += 30
                print("The energy drink helps you recover!")

    def find_new_court(self):
        """Event: Discover a new basketball location"""
        new_location = random.choice([
            "Haymount courts",
            "FTCC gym",
            "Cape Fear court",
            "Space Jam Hoops"
        ])
        print(f"{self.player_name} discovers a new basketball location: {new_location}!")
        self.location = new_location
        self.energy -= 10  # Energy cost for traveling

    def empty_event(self):
        """Default event: Simple practice session"""
        print(f"{self.player_name} practices shots alone today.")
        self.skill += random.randint(1, 10)
        self.energy -= random.randint(5, 15)

    def daily_actions(self):
        """Handle player's daily choice of action"""
        print("What do you want to do today?")
        print("1. Practice shooting")
        print("2. Play a pickup game")
        print("3. Rest and recover")
        print("4. Travel to new location")
        print("5. Check inventory")
        print("6. Quit game")

        # Get and validate player input
        choice = input("Choose an action (1-6): ")
        while choice not in ["1", "2", "3", "4", "5", "6"]:
            choice = input("Invalid choice. Please enter a number from 1 to 6: ")

        # Handle each action choice
        if choice == "1":
            print(f"{self.player_name} spends hours working on your shot.")
            self.skill += random.randint(3, 8)
            self.energy -= random.randint(10, 20)
        elif choice == "2":
            print(f"{self.player_name} joins a pickup game with the homies.")
            if random.random() < 0.5 + (self.skill / 100):  # Skill affects outcome
                print("Your team wins! You gain confidence.")
                self.confidence += random.randint(5, 15)
            else:
                print("Your team loses, but you learn from the experience.")
                self.confidence -= random.randint(1, 5)
            self.skill += random.randint(2, 6)
            self.energy -= random.randint(15, 25)
        elif choice == "3":
            recovery = random.randint(15, 30)
            print(f"{self.player_name} rests and recovers {recovery} energy.")
            self.energy += recovery
        elif choice == "4":
            self.find_new_court()
        elif choice == "5":
            print("Inventory:")
            for item in self.inventory:
                print(f"- {item}")
            input("Press Enter to continue...")
            return
        elif choice == "6":
            self.game_over = True

        # 40% chance of random event after certain actions
        if random.random() < 0.4 and choice in ["1", "2", "4"]:
            self.random_event()

    def check_game_status(self):
        """Check win/lose conditions to end game"""
        if self.energy <= 0:
            print(f"{self.player_name} is too exhausted to continue! Game Over.")
            self.game_over = True
        elif self.confidence <= 0:
            print(f"{self.player_name} has lost all confidence. Time to quit.")
            self.game_over = True
        elif self.skill >= 100:
            print(f"Congratulations {self.player_name}! You've become a Basketball GOD! Sike! You'll never be Michael Jordan!!!")
            self.game_over = True

    def play(self):
        """Main game loop that controls gameplay flow"""
        print(f"\n=== Basketball Adventure ===")
        print(f"Welcome, {self.player_name}!")
        print("Train, compete, and become a basketball legend!")
        print("Manage your energy, skill, and confidence to succeed.\n")

        # Continue playing until game_over is True
        while not self.game_over:
            self.display_stats()
            self.daily_actions()
            self.day += 1
            self.check_game_status()

        # Game over screen
        print(f"Game over after {self.day-1} days, {self.player_name}!")
        print(f"Final Skill Level: {self.skill}")

def main():
    
    print("🏀=== Basketball Shorties ===🏀")
    player_name = input("Enter your Hooper's name: ")
    game = BasketballAdventure(player_name)  # Create game instance
    game.play()  # Start the game

if __name__ == "__main__":
    main()  # Run the game when executed directly
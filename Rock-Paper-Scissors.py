import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("800x600")
        self.root.configure(bg='#1a1a2e')
        self.root.resizable(False, False)
        
        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        
        # Center the window
        self.center_window()
        
        # Create main menu
        self.create_main_menu()
        
    def center_window(self):
        self.root.update_idletasks()
        width = 800
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Main menu frame
        main_frame = tk.Frame(self.root, bg='#1a1a2e')
        main_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="ROCK PAPER SCISSORS",
            font=('Arial', 32, 'bold'),
            fg='#eee2dc',
            bg='#1a1a2e'
        )
        title_label.pack(pady=80)
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="The Ultimate Battle of Choices",
            font=('Arial', 16, 'italic'),
            fg='#ac3931',
            bg='#1a1a2e'
        )
        subtitle_label.pack(pady=10)
        
        # Visual elements
        elements_frame = tk.Frame(main_frame, bg='#1a1a2e')
        elements_frame.pack(pady=40)
        
        # Rock Paper Scissors symbols
        symbols_frame = tk.Frame(elements_frame, bg='#1a1a2e')
        symbols_frame.pack()
        
        symbols = ['ROCK', 'PAPER', 'SCISSORS']
        for i, symbol in enumerate(symbols):
            symbol_label = tk.Label(
                symbols_frame,
                text=symbol,
                font=('Arial', 20, 'bold'),
                fg='#ffffff',
                bg='#1a1a2e'
            )
            symbol_label.pack(side='left', padx=30)
        
        # Play button
        play_button = tk.Button(
            main_frame,
            text="START GAME",
            font=('Arial', 18, 'bold'),
            fg='white',
            bg='#ac3931',
            activebackground='#8b2e26',
            activeforeground='white',
            relief='flat',
            padx=40,
            pady=15,
            cursor='hand2',
            command=self.start_game
        )
        play_button.pack(pady=40)
        
        # Instructions
        instructions = tk.Label(
            main_frame,
            text="Rock crushes Scissors • Scissors cuts Paper • Paper covers Rock",
            font=('Arial', 12),
            fg='#eee2dc',
            bg='#1a1a2e'
        )
        instructions.pack(pady=20)
    
    def start_game(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Game frame
        self.game_frame = tk.Frame(self.root, bg='#0f3460')
        self.game_frame.pack(fill='both', expand=True)
        
        # Header
        header_frame = tk.Frame(self.game_frame, bg='#16537e', height=80)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Game title in header
        game_title = tk.Label(
            header_frame,
            text="ROCK PAPER SCISSORS BATTLE",
            font=('Arial', 20, 'bold'),
            fg='white',
            bg='#16537e'
        )
        game_title.pack(pady=20)
        
        # Score frame
        score_frame = tk.Frame(self.game_frame, bg='#0f3460')
        score_frame.pack(pady=10)
        
        # Player score
        player_score_frame = tk.Frame(score_frame, bg='#1a237e')
        player_score_frame.pack(side='left', padx=20, pady=10)
        
        tk.Label(
            player_score_frame,
            text="PLAYER",
            font=('Arial', 14, 'bold'),
            fg='white',
            bg='#1a237e'
        ).pack(padx=20, pady=5)
        
        self.player_score_label = tk.Label(
            player_score_frame,
            text=str(self.player_score),
            font=('Arial', 24, 'bold'),
            fg='#4fc3f7',
            bg='#1a237e'
        )
        self.player_score_label.pack(padx=20, pady=5)
        
        # VS label
        vs_label = tk.Label(
            score_frame,
            text="VS",
            font=('Arial', 16, 'bold'),
            fg='#ff6b6b',
            bg='#0f3460'
        )
        vs_label.pack(side='left', padx=40)
        
        # Computer score
        computer_score_frame = tk.Frame(score_frame, bg='#b71c1c')
        computer_score_frame.pack(side='left', padx=20, pady=10)
        
        tk.Label(
            computer_score_frame,
            text="COMPUTER",
            font=('Arial', 14, 'bold'),
            fg='white',
            bg='#b71c1c'
        ).pack(padx=20, pady=5)
        
        self.computer_score_label = tk.Label(
            computer_score_frame,
            text=str(self.computer_score),
            font=('Arial', 24, 'bold'),
            fg='#ffab91',
            bg='#b71c1c'
        )
        self.computer_score_label.pack(padx=20, pady=5)
        
        # Game area
        game_area = tk.Frame(self.game_frame, bg='#0f3460')
        game_area.pack(pady=30, expand=True)
        
        # Choice display
        choice_frame = tk.Frame(game_area, bg='#0f3460')
        choice_frame.pack(pady=20)
        
        # Player choice
        player_choice_frame = tk.Frame(choice_frame, bg='#1e88e5')
        player_choice_frame.pack(side='left', padx=30, pady=20)
        
        tk.Label(
            player_choice_frame,
            text="Your Choice",
            font=('Arial', 12, 'bold'),
            fg='white',
            bg='#1e88e5'
        ).pack(padx=30, pady=10)
        
        self.player_choice_label = tk.Label(
            player_choice_frame,
            text="?",
            font=('Arial', 32, 'bold'),
            fg='white',
            bg='#1e88e5'
        )
        self.player_choice_label.pack(padx=30, pady=10)
        
        # Computer choice
        computer_choice_frame = tk.Frame(choice_frame, bg='#e53935')
        computer_choice_frame.pack(side='left', padx=30, pady=20)
        
        tk.Label(
            computer_choice_frame,
            text="Computer Choice",
            font=('Arial', 12, 'bold'),
            fg='white',
            bg='#e53935'
        ).pack(padx=30, pady=10)
        
        self.computer_choice_label = tk.Label(
            computer_choice_frame,
            text="?",
            font=('Arial', 32, 'bold'),
            fg='white',
            bg='#e53935'
        )
        self.computer_choice_label.pack(padx=30, pady=10)
        
        # Result label
        self.result_label = tk.Label(
            game_area,
            text="Make your choice!",
            font=('Arial', 18, 'bold'),
            fg='#ffeb3b',
            bg='#0f3460'
        )
        self.result_label.pack(pady=30)
        
        # Buttons frame
        buttons_frame = tk.Frame(game_area, bg='#0f3460')
        buttons_frame.pack(pady=20)
        
        # Game buttons
        choices = [
            ('ROCK', '#795548'),
            ('PAPER', '#607d8b'),
            ('SCISSORS', '#ff5722')
        ]
        
        for choice, color in choices:
            btn = tk.Button(
                buttons_frame,
                text=choice,
                font=('Arial', 14, 'bold'),
                fg='white',
                bg=color,
                activebackground=color,
                activeforeground='white',
                relief='flat',
                padx=25,
                pady=15,
                cursor='hand2',
                command=lambda c=choice: self.play_round(c)
            )
            btn.pack(side='left', padx=15)
        
        # Control buttons frame
        control_frame = tk.Frame(self.game_frame, bg='#0f3460')
        control_frame.pack(side='bottom', pady=20)
        
        # Reset button
        reset_button = tk.Button(
            control_frame,
            text="Reset Score",
            font=('Arial', 12, 'bold'),
            fg='white',
            bg='#ff9800',
            activebackground='#f57c00',
            activeforeground='white',
            relief='flat',
            padx=20,
            pady=10,
            cursor='hand2',
            command=self.reset_game
        )
        reset_button.pack(side='left', padx=10)
        
        # Back to menu button
        back_button = tk.Button(
            control_frame,
            text="Back to Menu",
            font=('Arial', 12, 'bold'),
            fg='white',
            bg='#37474f',
            activebackground='#263238',
            activeforeground='white',
            relief='flat',
            padx=20,
            pady=10,
            cursor='hand2',
            command=self.back_to_menu
        )
        back_button.pack(side='left', padx=10)
    
    def play_round(self, player_choice):
        choices = ['ROCK', 'PAPER', 'SCISSORS']
        computer_choice = random.choice(choices)
        
        # Update choice displays
        self.player_choice_label.config(text=player_choice)
        self.computer_choice_label.config(text=computer_choice)
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update scores and result message
        if result == "win":
            self.player_score += 1
            self.result_label.config(
                text=f"You Win! {player_choice} beats {computer_choice}",
                fg='#4caf50'
            )
        elif result == "lose":
            self.computer_score += 1
            self.result_label.config(
                text=f"You Lose! {computer_choice} beats {player_choice}",
                fg='#f44336'
            )
        else:
            self.result_label.config(
                text=f"It's a Tie! Both chose {player_choice}",
                fg='#ff9800'
            )
        
        # Update score labels
        self.player_score_label.config(text=str(self.player_score))
        self.computer_score_label.config(text=str(self.computer_score))
        
        self.rounds_played += 1
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "tie"
        elif (player == "ROCK" and computer == "SCISSORS") or \
             (player == "PAPER" and computer == "ROCK") or \
             (player == "SCISSORS" and computer == "PAPER"):
            return "win"
        else:
            return "lose"
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        
        # Reset displays
        self.player_score_label.config(text="0")
        self.computer_score_label.config(text="0")
        self.player_choice_label.config(text="?")
        self.computer_choice_label.config(text="?")
        self.result_label.config(
            text="Make your choice!",
            fg='#ffeb3b'
        )
    
    def back_to_menu(self):
        self.reset_game()
        self.create_main_menu()
    
    def run(self):
        self.root.mainloop()

# Run the game
if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()
# import tkinter as tk
# from tkinter import ttk, messagebox
# import random
# from typing import List
# import threading
# import time

# class DiceSimulator:
#     def __init__(self):
#         self.total_rolls = 0
        
#     def roll_dice(self, num_dice: int) -> List[int]:
#         """Roll the specified number of dice and return results"""
#         results = [random.randint(1, 6) for _ in range(num_dice)]
#         self.total_rolls += 1
#         return results
    
#     def get_total_rolls(self) -> int:
#         return self.total_rolls

# class DiceSimulatorGUI:
#     def __init__(self, root):
#         self.root = root
#         self.simulator = DiceSimulator()
#         self.setup_gui()
        
#     def setup_gui(self):
#         # Configure main window
#         self.root.title("🎲 Dice Rolling Simulator")
#         self.root.geometry("600x500")
#         self.root.configure(bg='#2c3e50')
#         self.root.resizable(False, False)
        
#         # Configure styles
#         style = ttk.Style()
#         style.theme_use('clam')
        
#         # Main container
#         main_frame = tk.Frame(self.root, bg='#2c3e50', padx=20, pady=20)
#         main_frame.pack(fill=tk.BOTH, expand=True)
        
#         # Title
#         title_label = tk.Label(
#             main_frame, 
#             text="🎲 DICE ROLLING SIMULATOR 🎲",
#             font=('Arial', 24, 'bold'),
#             fg='#ecf0f1',
#             bg='#2c3e50'
#         )
#         title_label.pack(pady=(0, 30))
        
#         # Controls frame
#         controls_frame = tk.Frame(main_frame, bg='#2c3e50')
#         controls_frame.pack(pady=10)
        
#         # Number of dice selection
#         dice_label = tk.Label(
#             controls_frame,
#             text="Number of dice to roll:",
#             font=('Arial', 14),
#             fg='#ecf0f1',
#             bg='#2c3e50'
#         )
#         dice_label.pack(pady=5)
        
#         self.dice_var = tk.StringVar(value="2")
#         dice_spinbox = tk.Spinbox(
#             controls_frame,
#             from_=1,
#             to=10,
#             width=5,
#             textvariable=self.dice_var,
#             font=('Arial', 14),
#             justify='center'
#         )
#         dice_spinbox.pack(pady=10)
        
#         # Roll button
#         self.roll_button = tk.Button(
#             controls_frame,
#             text="🎲 ROLL DICE 🎲",
#             command=self.roll_dice_animated,
#             font=('Arial', 16, 'bold'),
#             bg='#e74c3c',
#             fg='white',
#             width=15,
#             height=2,
#             relief='raised',
#             bd=3
#         )
#         self.roll_button.pack(pady=20)
        
#         # Results frame
#         results_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
#         results_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
#         # Results title
#         results_title = tk.Label(
#             results_frame,
#             text="Roll Results",
#             font=('Arial', 16, 'bold'),
#             fg='#ecf0f1',
#             bg='#34495e'
#         )
#         results_title.pack(pady=10)
        
#         # Dice display frame
#         self.dice_display_frame = tk.Frame(results_frame, bg='#34495e')
#         self.dice_display_frame.pack(pady=10)
        
#         # Sum and stats frame
#         stats_frame = tk.Frame(results_frame, bg='#34495e')
#         stats_frame.pack(pady=15)
        
#         self.sum_label = tk.Label(
#             stats_frame,
#             text="Sum: -",
#             font=('Arial', 14, 'bold'),
#             fg='#f39c12',
#             bg='#34495e'
#         )
#         self.sum_label.pack(pady=5)
        
#         self.total_rolls_label = tk.Label(
#             stats_frame,
#             text="Total rolls: 0",
#             font=('Arial', 12),
#             fg='#95a5a6',
#             bg='#34495e'
#         )
#         self.total_rolls_label.pack(pady=5)
        
#         # Clear button
#         clear_button = tk.Button(
#             main_frame,
#             text="Clear Results",
#             command=self.clear_results,
#             font=('Arial', 10),
#             bg='#95a5a6',
#             fg='white',
#             width=12
#         )
#         clear_button.pack(pady=10)
        
#         # Initial display
#         self.display_welcome()
    
#     def display_welcome(self):
#         """Display welcome message"""
#         welcome_label = tk.Label(
#             self.dice_display_frame,
#             text="🎯 Select number of dice and click ROLL! 🎯",
#             font=('Arial', 12),
#             fg='#bdc3c7',
#             bg='#34495e'
#         )
#         welcome_label.pack(pady=20)
    
#     def get_dice_emoji(self, value: int) -> str:
#         """Return dice emoji for given value"""
#         dice_emojis = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}
#         return dice_emojis.get(value, '🎲')
    
#     def clear_dice_display(self):
#         """Clear the dice display frame"""
#         for widget in self.dice_display_frame.winfo_children():
#             widget.destroy()
    
#     def roll_dice_animated(self):
#         """Roll dice with animation effect"""
#         try:
#             num_dice = int(self.dice_var.get())
#         except ValueError:
#             messagebox.showerror("Error", "Please enter a valid number of dice!")
#             return
        
#         if not (1 <= num_dice <= 10):
#             messagebox.showerror("Error", "Number of dice must be between 1 and 10!")
#             return
        
#         # Disable button during animation
#         self.roll_button.config(state='disabled', text='Rolling...')
        
#         # Start animation in separate thread
#         threading.Thread(target=self.animate_roll, args=(num_dice,), daemon=True).start()
    
#     def animate_roll(self, num_dice: int):
#         """Animate the dice rolling"""
#         # Clear previous results
#         self.root.after(0, self.clear_dice_display)
        
#         # Animation frames
#         for frame in range(8):  # 8 animation frames
#             # Generate random values for animation
#             temp_results = [random.randint(1, 6) for _ in range(num_dice)]
#             self.root.after(frame * 100, lambda r=temp_results: self.display_temp_results(r))
        
#         # Final roll
#         final_results = self.simulator.roll_dice(num_dice)
#         self.root.after(800, lambda: self.display_final_results(final_results))
#         self.root.after(800, lambda: self.roll_button.config(state='normal', text='🎲 ROLL DICE 🎲'))
    
#     def display_temp_results(self, results: List[int]):
#         """Display temporary results during animation"""
#         self.clear_dice_display()
        
#         # Create grid for dice
#         rows = 2 if len(results) > 5 else 1
#         cols = min(5, len(results)) if len(results) > 5 else len(results)
        
#         for i, value in enumerate(results):
#             row = i // cols
#             col = i % cols
            
#             dice_frame = tk.Frame(self.dice_display_frame, bg='#34495e')
#             dice_frame.grid(row=row, column=col, padx=10, pady=5)
            
#             dice_label = tk.Label(
#                 dice_frame,
#                 text=self.get_dice_emoji(value),
#                 font=('Arial', 30),
#                 bg='#34495e'
#             )
#             dice_label.pack()
            
#             value_label = tk.Label(
#                 dice_frame,
#                 text=str(value),
#                 font=('Arial', 12, 'bold'),
#                 fg='#ecf0f1',
#                 bg='#34495e'
#             )
#             value_label.pack()
    
#     def display_final_results(self, results: List[int]):
#         """Display final dice results"""
#         self.clear_dice_display()
        
#         # Create grid for dice
#         rows = 2 if len(results) > 5 else 1
#         cols = min(5, len(results)) if len(results) > 5 else len(results)
        
#         for i, value in enumerate(results):
#             row = i // cols
#             col = i % cols
            
#             dice_frame = tk.Frame(
#                 self.dice_display_frame, 
#                 bg='#27ae60', 
#                 relief='raised', 
#                 bd=2,
#                 padx=10,
#                 pady=5
#             )
#             dice_frame.grid(row=row, column=col, padx=10, pady=10)
            
#             dice_label = tk.Label(
#                 dice_frame,
#                 text=self.get_dice_emoji(value),
#                 font=('Arial', 35),
#                 bg='#27ae60'
#             )
#             dice_label.pack()
            
#             value_label = tk.Label(
#                 dice_frame,
#                 text=str(value),
#                 font=('Arial', 14, 'bold'),
#                 fg='white',
#                 bg='#27ae60'
#             )
#             value_label.pack()
        
#         # Update sum and total rolls
#         dice_sum = sum(results)
#         self.sum_label.config(text=f"Sum: {dice_sum}")
#         self.total_rolls_label.config(text=f"Total rolls: {self.simulator.get_total_rolls()}")
        
#         # Show success message for special rolls
#         self.check_special_rolls(results)
    
#     def check_special_rolls(self, results: List[int]):
#         """Check for special roll combinations"""
#         if len(results) >= 2:
#             if all(x == results[0] for x in results):
#                 messagebox.showinfo("🎉 Special Roll!", f"Amazing! All {results[0]}s!")
#             elif sum(results) == len(results):  # All ones
#                 messagebox.showinfo("😅 Snake Eyes!", "All ones! Better luck next time!")
#             elif sum(results) == len(results) * 6:  # All sixes
#                 messagebox.showinfo("🔥 Jackpot!", "All sixes! Incredible roll!")
    
#     def clear_results(self):
#         """Clear all results and reset"""
#         self.clear_dice_display()
#         self.sum_label.config(text="Sum: -")
#         self.simulator.total_rolls = 0
#         self.total_rolls_label.config(text="Total rolls: 0")
#         self.display_welcome()

# def main():
#     root = tk.Tk()
#     app = DiceSimulatorGUI(root)
    
#     #Center window on screen
#     root.update_idletasks()
#     x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
#     y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
#     root.geometry(f"+{x}+{y}")
    
#     root.mainloop()

# if __name__ == "__main__":
#     main()


import tkinter as tk
from tkinter import ttk, messagebox
import random
from typing import List
import threading

class DiceSimulator:
    def __init__(self):
        self.total_rolls = 0
        self.history = []  # store last 5 rolls with sum
        
    def roll_dice(self, num_dice: int) -> List[int]:
        """Roll the specified number of dice and return results"""
        results = [random.randint(1, 6) for _ in range(num_dice)]
        self.total_rolls += 1
        dice_sum = sum(results)
        self.history.insert(0, (results, dice_sum))  # store roll + sum
        if len(self.history) > 5:  # keep last 5 only
            self.history.pop()
        return results
    
    def get_total_rolls(self) -> int:
        return self.total_rolls

class DiceSimulatorGUI:
    def __init__(self, root):
        self.root = root
        self.simulator = DiceSimulator()
        self.setup_gui()
        
    def setup_gui(self):
        # Configure main window
        self.root.title("🎲 Dice Rolling Simulator")
        self.root.geometry("650x600")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(False, False)
        
        # Configure styles
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#2c3e50', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🎲 DICE ROLLING SIMULATOR 🎲",
            font=('Arial', 24, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))
        
        # Controls frame
        controls_frame = tk.Frame(main_frame, bg='#2c3e50')
        controls_frame.pack(pady=10)
        
        dice_label = tk.Label(
            controls_frame,
            text="Number of dice to roll:",
            font=('Arial', 14),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        dice_label.pack(pady=5)
        
        self.dice_var = tk.StringVar(value="2")
        dice_spinbox = tk.Spinbox(
            controls_frame,
            from_=1,
            to=10,
            width=5,
            textvariable=self.dice_var,
            font=('Arial', 14),
            justify='center'
        )
        dice_spinbox.pack(pady=10)
        
        # Roll button
        self.roll_button = tk.Button(
            controls_frame,
            text="🎲 ROLL DICE 🎲",
            command=self.roll_dice_animated,
            font=('Arial', 16, 'bold'),
            bg='#e74c3c',
            fg='white',
            width=15,
            height=2,
            relief='raised',
            bd=3
        )
        self.roll_button.pack(pady=20)
        
        # Results frame
        results_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=15)
        
        results_title = tk.Label(
            results_frame,
            text="Roll Results",
            font=('Arial', 16, 'bold'),
            fg='#ecf0f1',
            bg='#34495e'
        )
        results_title.pack(pady=10)
        
        self.dice_display_frame = tk.Frame(results_frame, bg='#34495e')
        self.dice_display_frame.pack(pady=10)
        
        # Stats frame
        stats_frame = tk.Frame(results_frame, bg='#34495e')
        stats_frame.pack(pady=15)
        
        self.sum_label = tk.Label(
            stats_frame,
            text="Sum: -",
            font=('Arial', 14, 'bold'),
            fg='#f39c12',
            bg='#34495e'
        )
        self.sum_label.pack(pady=5)
        
        self.avg_label = tk.Label(
            stats_frame,
            text="Average: -",
            font=('Arial', 12),
            fg='#1abc9c',
            bg='#34495e'
        )
        self.avg_label.pack(pady=5)
        
        self.total_rolls_label = tk.Label(
            stats_frame,
            text="Total rolls: 0",
            font=('Arial', 12),
            fg='#95a5a6',
            bg='#34495e'
        )
        self.total_rolls_label.pack(pady=5)
        
        # History frame
        self.history_frame = tk.Frame(results_frame, bg='#2c3e50')
        self.history_frame.pack(pady=15, fill=tk.X)
        
        self.history_label = tk.Label(
            self.history_frame,
            text="History (last 5 rolls):\n-",
            font=('Arial', 11),
            fg='#bdc3c7',
            bg='#2c3e50',
            justify="left"
        )
        self.history_label.pack()
        
        # Clear button
        clear_button = tk.Button(
            main_frame,
            text="Clear Results",
            command=self.clear_results,
            font=('Arial', 10),
            bg='#95a5a6',
            fg='white',
            width=12
        )
        clear_button.pack(pady=10)
        
        self.display_welcome()
    
    def display_welcome(self):
        self.clear_dice_display()
        welcome_label = tk.Label(
            self.dice_display_frame,
            text="🎯 Select number of dice and click ROLL! 🎯",
            font=('Arial', 12),
            fg='#bdc3c7',
            bg='#34495e'
        )
        welcome_label.pack(pady=20)
    
    def get_dice_emoji(self, value: int) -> str:
        dice_emojis = {1: '⚀', 2: '⚁', 3: '⚂', 4: '⚃', 5: '⚄', 6: '⚅'}
        return dice_emojis.get(value, '🎲')
    
    def clear_dice_display(self):
        for widget in self.dice_display_frame.winfo_children():
            widget.destroy()
    
    def roll_dice_animated(self):
        try:
            num_dice = int(self.dice_var.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of dice!")
            return
        
        if not (1 <= num_dice <= 10):
            messagebox.showerror("Error", "Number of dice must be between 1 and 10!")
            return
        
        self.roll_button.config(state='disabled', text='Rolling...')
        threading.Thread(target=self.animate_roll, args=(num_dice,), daemon=True).start()
    
    def animate_roll(self, num_dice: int):
        self.root.after(0, self.clear_dice_display)
        
        for frame in range(8):
            temp_results = [random.randint(1, 6) for _ in range(num_dice)]
            self.root.after(frame * 100, lambda r=temp_results: self.display_temp_results(r))
        
        final_results = self.simulator.roll_dice(num_dice)
        self.root.after(800, lambda: self.display_final_results(final_results))
        self.root.after(800, lambda: self.roll_button.config(state='normal', text='🎲 ROLL DICE 🎲'))
    
    def display_temp_results(self, results: List[int]):
        self.clear_dice_display()
        cols = min(5, len(results))
        
        for i, value in enumerate(results):
            row, col = divmod(i, cols)
            dice_frame = tk.Frame(self.dice_display_frame, bg='#34495e')
            dice_frame.grid(row=row, column=col, padx=10, pady=5)
            
            tk.Label(
                dice_frame,
                text=self.get_dice_emoji(value),
                font=('Arial', 30),
                bg='#34495e'
            ).pack()
            tk.Label(
                dice_frame,
                text=str(value),
                font=('Arial', 12, 'bold'),
                fg='#ecf0f1',
                bg='#34495e'
            ).pack()
    
    def display_final_results(self, results: List[int]):
        self.clear_dice_display()
        cols = min(5, len(results))
        
        for i, value in enumerate(results):
            row, col = divmod(i, cols)
            dice_frame = tk.Frame(self.dice_display_frame, bg='#27ae60', relief='raised', bd=2, padx=10, pady=5)
            dice_frame.grid(row=row, column=col, padx=10, pady=10)
            
            tk.Label(
                dice_frame,
                text=self.get_dice_emoji(value),
                font=('Arial', 35),
                bg='#27ae60'
            ).pack()
            tk.Label(
                dice_frame,
                text=str(value),
                font=('Arial', 14, 'bold'),
                fg='white',
                bg='#27ae60'
            ).pack()
        
        dice_sum = sum(results)
        avg = round(dice_sum / len(results), 2)
        
        self.sum_label.config(text=f"Sum: {dice_sum}")
        self.avg_label.config(text=f"Average: {avg}")
        self.total_rolls_label.config(text=f"Total rolls: {self.simulator.get_total_rolls()}")
        
        # Update history
        history_text = "History (last 5 rolls):\n"
        for roll, s in self.simulator.history:
            history_text += f"🎲 {roll} → Sum={s}\n"
        self.history_label.config(text=history_text)
    
    def clear_results(self):
        self.clear_dice_display()
        self.sum_label.config(text="Sum: -")
        self.avg_label.config(text="Average: -")
        self.simulator.total_rolls = 0
        self.simulator.history = []
        self.total_rolls_label.config(text="Total rolls: 0")
        self.history_label.config(text="History (last 5 rolls):\n-")
        self.display_welcome()

def main():
    root = tk.Tk()
    app = DiceSimulatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

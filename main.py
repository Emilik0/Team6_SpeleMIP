## IMPORTS ##
# GUI
import tkinter as tk
from tkinter import messagebox

## CODE ##

class GameUI:
    def interface():

        # WINDOW SETUP
        root = tk.Tk()
        root.title("Multiply!")
        root.configure(bg='#1DA1F2')
        window_width = 800
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        player_scores = [0, 0]
        curr_number = None
        curr_player = 0
        turn = 1

        team_label = tk.Label(root, text="Team 6", bg='#1DA1F2', fg = "gray")
        team_label.pack()

        score_label = tk.Label(root, text=f"Player 1: {player_scores[0]} | Player 2: {player_scores[1]}", font=("Arial", 20, "bold"), bg='#1DA1F2', fg='white')
        score_label.place(relx=0.5, rely=0.95, anchor="center")
        
        # START PAGE
        def start():
            nonlocal curr_player
            header = tk.Label(root, text="Multiply!", font=("Arial", 30, "bold"), bg='#1DA1F2', fg='white')
            header.pack(pady=(70,20))

            player_label = tk.Label(root, text=f"Player {curr_player + 1}'s turn", font=("Arial", 20, "bold"), bg='#1DA1F2', fg='white')
            player_label.pack(pady=(10, 40))

            instruction_label = tk.Label(root, text="Choose starting number:", font=("Arial", 20, "bold"), bg='#1DA1F2', fg='white')
            instruction_label.pack(pady=10)

            num_button_frame = tk.Frame(root, bg='#1DA1F2')
            num_button_array = []
            for i in range(8, 19):
                num_button = tk.Button(num_button_frame, text=str(i), command=lambda n=i: prepare_num(n), font=("Arial", 18), fg='#1DA1F2', bg='white', width=3, height = 1)
                num_button_array.append(num_button)
                num_button.pack(side='left', padx=10)
            num_button_frame.pack(pady=5)

            # TURN FUNCTION
            def prepare_num(num):
                print(turn) # debug
                nonlocal instruction_label, curr_number
                curr_number = num
                instruction_label.pack_forget()
                num_button_frame.pack_forget()

                curr_number_label = tk.Label(root, text=f"Current number: {curr_number}", font=("Arial", 20, "bold"), bg='#1DA1F2', fg='white')
                curr_number_label.pack(pady=10)

                instruction_label.config(text="Choose a multiplier:")
                instruction_label.pack(pady=10)

                multiply_frame = tk.Frame(root, bg='#1DA1F2')
                multiply_array = []
                for i in [2, 3, 4]:
                    multiply_button = tk.Button(multiply_frame, text=str(i), command=lambda m=i: multiply(curr_number, m), font=("Arial", 18), fg='#1DA1F2', bg='white', width=3, height = 1)
                    multiply_array.append(multiply_button)
                    multiply_button.pack(side='left', padx=10)
                multiply_frame.pack(pady=5)

                # GAME LOGIC
                def multiply(number, multi):
                    nonlocal curr_number, curr_player, turn
                    number *= multi

                    if number % 2 == 0:
                        player_scores[1 - curr_player] -= 1
                    else:
                        player_scores[curr_player] += 1

                    if number >= 1200:
                        if player_scores[0] == player_scores[1]:
                            messagebox.showinfo("Game Over", "It's a tie!")
                            root.quit()
                        else:
                            winner = "Player 1" if player_scores[0] > player_scores[1] else "Player 2"
                            messagebox.showinfo("Game Over", f"{winner} wins!")
                            root.quit()
                    else:
                        curr_player = 1 - curr_player
                        player_label.config(text=f"Player {curr_player + 1}'s turn")
                        player_label.pack(pady=(10, 40))
                        turn+=1

                    curr_number_label.config(text=f"Current number: {number}")
                    curr_number_label.pack_forget()
                    score_label.config(text=f"Player 1: {player_scores[0]} | Player 2: {player_scores[1]}")
                    multiply_frame.pack_forget()
                    prepare_num(number)
            
        
        start()
        root.mainloop()

    interface()

  
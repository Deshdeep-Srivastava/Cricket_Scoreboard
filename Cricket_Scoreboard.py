import tkinter as tk

class CricketScoreboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Scoreboard")
        self.score = 0
        self.wicket = 0
        self.team1_score = 0
        self.team2_score = 0
        self.team1_wicket = 0
        self.team2_wicket = 0
        # self.team1_players = []
        # self.team2_players = []
        # self.team1_ballsplayed = 0
        # self.team2_ballsplayed = 0
        self.balls_bowled = 0
        self.total_balls_in_a_match = 24

        self.team_name = tk.Label(root, text = "Team 1 is playing")
        self.team_name.pack()
        
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 24))
        self.score_label.pack()
        
        self.wicket_label = tk.Label(root, text="Wickets fallen: 0", font="Arial 24")
        self.wicket_label.pack()
        
        self.ballsbowled_label = tk.Label(root, text="Balls bowled: 0", font = "Arial 20")
        self.ballsbowled_label.pack()

        self.run_label = tk.Label(root, text="Enter runs:")
        self.run_label.pack()

        self.run_entry = tk.Entry(root)
        self.run_entry.pack()

        self.add_run_button = tk.Button(root, text="Add Run", command=self.add_run)
        self.add_run_button.pack()

    def add_run(self):
        try:
            runs = self.run_entry.get()
            
            if runs == "W":
                self.wicket += 1
                self.wicket_label.config(text=f"Wickets fallen: {self.wicket}")
            else:
                self.score += int(runs)
                self.score_label.config(text=f"Score: {self.score}")
            self.balls_bowled += 1
            self.ballsbowled_label.config(text=f"Balls bowled: {self.balls_bowled}")
            self.run_entry.delete(0, tk.END)
        except ValueError:
            self.run_label.config(text="Invalid input. Please enter a number.")

root = tk.Tk()
root.geometry("800x600")
scoreboard = CricketScoreboard(root)
root.mainloop()
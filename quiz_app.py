import tkinter as tk

QUESTIONS = [
    ("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], 1),
    ("Which language runs in a browser?", ["Python", "Java", "JavaScript", "C++"], 2),
    ("What does CPU stand for?", ["Central Processing Unit", "Computer Personal Unit",
     "Central Program Utility", "Core Processing Utility"], 0),
    ("Which planet is the Red Planet?", ["Venus", "Jupiter", "Mars", "Saturn"], 2),
    ("What is 15 x 4?", ["45", "50", "60", "70"], 2),
    ("Which data type stores True/False?", ["int", "bool", "str", "float"], 1),
    ("Who painted the Mona Lisa?", ["Van Gogh", "Picasso", "Da Vinci", "Monet"], 2),
    ("What is H2O?", ["Oxygen", "Hydrogen", "Water", "Salt"], 2),
    ("Which is the largest ocean?", ["Atlantic", "Indian", "Arctic", "Pacific"], 3),
    ("How many bits in a byte?", ["4", "8", "16", "32"], 1),
]
BG, FG, ACCENT, TIME = "#1e1e2e", "#cdd6f4", "#89b4fa", 15


class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Master")
        self.geometry("560x440")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.show_start()

    def clear(self):
        for w in self.winfo_children():
            w.destroy()

    def label(self, text, size=14, bold=False, fg=FG, **kw):
        return tk.Label(self, text=text, bg=BG, fg=fg,
                        font=("Helvetica", size, "bold" if bold else "normal"), **kw)

    def show_start(self):
        self.clear()
        self.label("Quiz Master", 32, True, ACCENT).pack(pady=(90, 10))
        self.label(f"{len(QUESTIONS)} questions  •  {TIME}s each").pack()
        tk.Button(self, text="Start Quiz", font=("Helvetica", 14, "bold"),
                  bg=ACCENT, fg=BG, width=14, relief="flat",
                  command=self.start_quiz).pack(pady=40)

    def start_quiz(self):
        self.i, self.score, self.time_left = 0, 0, TIME
        self.show_question()

    def show_question(self):
        self.clear()
        q, opts, _ = QUESTIONS[self.i]
        top = tk.Frame(self, bg=BG)
        top.pack(fill="x", padx=20, pady=15)
        self.label(f"Question {self.i + 1}/{len(QUESTIONS)}", 12).pack(
            in_=top, side="left")
        self.timer_lbl = self.label(f"{self.time_left}s", 12, True, "#f9e2af")
        self.timer_lbl.pack(in_=top, side="right")
        self.label(q, 18, True, wraplength=500).pack(pady=(30, 25))
        self.btns = []
        for k, opt in enumerate(opts):
            b = tk.Button(self, text=opt, font=("Helvetica", 13), bg="#313244",
                          fg=FG, relief="flat", width=40, pady=8,
                          command=lambda k=k: self.answer(k))
            b.pack(pady=5)
            self.btns.append(b)
        self.tick()

    def tick(self):
        self.timer_lbl.config(text=f"{self.time_left}s")
        if self.time_left == 0:
            self.answer(-1)
            return
        self.time_left -= 1
        self.after_id = self.after(1000, self.tick)

    def answer(self, idx):
        self.after_cancel(self.after_id)
        correct = QUESTIONS[self.i][2]
        for k, b in enumerate(self.btns):
            b.config(state="disabled",
                     bg="#a6e3a1" if k == correct else
                     "#f38ba8" if k == idx else "#313244",
                     fg=BG if k in (correct, idx) else FG)
        if idx == correct:
            self.score += 1
        self.after(800, self.next_question)

    def next_question(self):
        self.i += 1
        if self.i < len(QUESTIONS):
            self.time_left = TIME
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear()
        pct = self.score * 100 // len(QUESTIONS)
        verdict = ("Excellent!" if pct >= 80 else
                   "Good job!" if pct >= 50 else "Keep practicing!")
        self.label("Quiz Complete!", 30, True, ACCENT).pack(pady=(80, 10))
        self.label(f"Score: {self.score}/{len(QUESTIONS)}  ({pct}%)", 20,
                   True).pack(pady=5)
        self.label(verdict, 14).pack()
        tk.Button(self, text="Play Again", font=("Helvetica", 13, "bold"),
                  bg=ACCENT, fg=BG, width=12, relief="flat",
                  command=self.show_start).pack(pady=40)


QuizApp().mainloop()

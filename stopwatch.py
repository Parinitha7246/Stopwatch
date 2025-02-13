import time
import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("400x300")
        self.root.configure(bg="#2C3E50")  # Dark background

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Time Display
        self.label = tk.Label(root, text="00:00:00", font=("Arial", 40, "bold"), fg="white", bg="#2C3E50")
        self.label.pack(pady=20)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#2C3E50")
        btn_frame.pack()

        self.start_btn = tk.Button(btn_frame, text="Start", font=("Arial", 12, "bold"), command=self.start, bg="#27AE60", fg="white", width=9)
        self.start_btn.grid(row=0, column=0, padx=5, pady=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", font=("Arial", 12, "bold"), command=self.stop, bg="#E67E22", fg="white", width=9)
        self.stop_btn.grid(row=0, column=1, padx=5, pady=5)

        self.resume_btn = tk.Button(btn_frame, text="Resume", font=("Arial", 12, "bold"), command=self.resume, bg="#2980B9", fg="white", width=9)
        self.resume_btn.grid(row=1, column=0, padx=5, pady=5)

        self.restart_btn = tk.Button(btn_frame, text="Restart", font=("Arial", 12, "bold"), command=self.restart, bg="#8E44AD", fg="white", width=9)
        self.restart_btn.grid(row=1, column=1, padx=5, pady=5)

        self.end_btn = tk.Button(root, text="End", font=("Arial", 12, "bold"), command=self.end, bg="#C0392B", fg="white", width=20)
        self.end_btn.pack(pady=10)

        # Start updating the timer display
        self.update_timer()

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_timer()

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def resume(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_timer()

    def restart(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

    def end(self):
        self.root.quit()

    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes = int(self.elapsed_time // 60)
            seconds = int(self.elapsed_time % 60)
            milliseconds = int((self.elapsed_time * 100) % 100)
            self.label.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:02}")

        self.root.after(10, self.update_timer)  # Update every 10ms

# Run the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()

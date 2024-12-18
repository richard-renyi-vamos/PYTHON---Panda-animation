import tkinter as tk
import time

class PandaAnimation:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Draw panda face
        self.face = self.canvas.create_oval(100, 100, 300, 300, fill="white", outline="black")
        self.left_eye = self.canvas.create_oval(140, 150, 180, 190, fill="black")
        self.right_eye = self.canvas.create_oval(220, 150, 260, 190, fill="black")
        self.left_eye_inner = self.canvas.create_oval(155, 160, 165, 170, fill="white")
        self.right_eye_inner = self.canvas.create_oval(235, 160, 245, 170, fill="white")
        self.nose = self.canvas.create_oval(190, 220, 210, 240, fill="black")
        self.mouth = self.canvas.create_arc(180, 230, 220, 270, start=0, extent=180, style=tk.ARC)

        self.is_blinking = False
        self.animate()

    def blink(self):
        if not self.is_blinking:
            self.is_blinking = True
            # Cover eyes
            self.canvas.itemconfig(self.left_eye, fill="white")
            self.canvas.itemconfig(self.right_eye, fill="white")
        else:
            self.is_blinking = False
            # Restore eyes
            self.canvas.itemconfig(self.left_eye, fill="black")
            self.canvas.itemconfig(self.right_eye, fill="black")

    def animate(self):
        self.blink()
        self.canvas.after(500, self.animate)  # Blink every 500ms

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Animated Panda")
    animation = PandaAnimation(root)
    root.mainloop()

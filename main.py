from tkinter import *
from tkinter import messagebox, filedialog
import os

from PIL import ImageGrab


class Draw():
    def __init__(self, root):

        # Defining title and Size of the Tkinter Window GUI
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        self.root.geometry("1000x900")
        self.root.configure(background="navy")
        #         self.root.resizable(0,0)

        # Variable for pointer
        self.pointer = "black"

        # Widgets for Tkinter Window

        # Configure the alignment , font size and color of the text
        text = Text(root)
        text.tag_configure("tag_name", justify='center', font=('arial', 25), background='blue', foreground='white')

        # Insert a Text
        text.insert("1.0", "Tic-Tac-Toe AI")

        # Add the tag for following given text
        text.tag_add("tag_name", "1.0", "end")
        text.pack()

        # Reset Button to clear the entire screen and redraw the board
        self.clear_screen = Button(self.root, text="Reset", bd=4, bg='white', command=self.reset_board,
                                   width=9, relief=RIDGE)
        self.clear_screen.place(x=12, y=45)

        # Submit Button to save the drawing and advance the AI
        self.submit_btn = Button(self.root, text="Submit", bd=4, bg='white', command=self.save_drawing,
                                 width=9, relief=RIDGE)
        self.submit_btn.place(x=12, y=75)

        # Defining a background color for the Canvas
        self.background = Canvas(self.root, bg='white', bd=5, relief=GROOVE, height=800, width=800)
        self.background.place(x=100, y=40)

        # Bind the background Canvas with mouse click
        self.background.bind("<B1-Motion>", self.paint)

        # Draw the Tic-Tac-Toe board
        self.draw_board()

    # Functions are defined here

    # Paint Function for Drawing the lines on Canvas
    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)

        self.background.create_oval(x1, y1, x2, y2, fill=self.pointer, outline=self.pointer,
                                    width=1)

    def draw_board(self):
        # Horizontal lines
        self.background.create_line(100, 300, 700, 300, width=5, fill='black')
        self.background.create_line(100, 500, 700, 500, width=5, fill='black')

        # Vertical lines
        self.background.create_line(300, 100, 300, 700, width=5, fill='black')
        self.background.create_line(500, 100, 500, 700, width=5, fill='black')

    def reset_board(self):
        # Clear the canvas
        self.background.delete('all')

        # Redraw the Tic-Tac-Toe board
        self.draw_board()

    def save_drawing(self):
        try:
            # Specify the file name and extension
            file_name = "positionOneX.jpg"

            # Get the path to the user's downloads folder
            downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

            # Specify the complete file path
            file_path = os.path.join(downloads_folder, file_name)

            # Get the next available file path if the file already exists
            inc = 0
            while os.path.exists(file_path):
                inc += 1
                file_name = f"drawing{inc}.jpg"
                file_path = os.path.join(downloads_folder, file_name)

            # Save the drawing
            x = self.root.winfo_rootx() + self.background.winfo_x()
            y = self.root.winfo_rooty() + self.background.winfo_y()
            x1 = x + self.background.winfo_width()
            y1 = y + self.background.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

        except Exception as e:
            print("Error in saving the drawing:", str(e))


if __name__ == "__main__":
    root = Tk()
    p = Draw(root)
    root.mainloop()

import time
from tkinter import *
import os
import tensorflow as tf
import random
from PIL import ImageGrab, Image
from enum import Enum
from PIL import ImageGrab


# Defining the board state settings
class BoardState(Enum):
    X = "X"
    O = "O"
    EMPTY = "empty"


class Draw:

    def __init__(self, root):

        # Defining title and Size of the Tkinter Window GUI
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        self.root.geometry("1000x900")
        self.root.configure(background="navy")

        # Variable for pointer
        self.pointer = "black"

        # Configure the alignment, font size and color of the text
        text = Text(root)
        text.tag_configure("tag_name", justify='center', font=('arial', 25), background='blue', foreground='white')

        # Insert a Text
        text.insert("1.0", "Tic-Tac-Toe AI")

        # Add the tag for following given text
        text.tag_add("tag_name", "1.0", "end")
        text.pack()

        # Add a label to display the game result
        self.result_label = Label(root, text="", font=("Arial", 20), bg="navy", fg="white")
        self.result_label.pack()

        # Reset Button to clear the entire screen and redraw the board
        self.clear_screen = Button(self.root, text="Reset", bd=4, bg='white', command=self.reset_board,
                                   width=9, relief=RIDGE)
        self.clear_screen.place(x=12, y=45)

        # Submit Button to save the drawing and advance the AI
        self.submit_btn = Button(self.root, text="Submit", bd=4, bg='white', command=self.move_submitted,
                                 width=9, relief=RIDGE)
        self.submit_btn.place(x=12, y=75)

        # Defining a background color for the Canvas
        self.background = Canvas(self.root, bg='white', bd=5, relief=GROOVE, height=800, width=800)
        self.background.place(x=100, y=40)

        # Bind the background Canvas with mouse click
        self.background.bind("<B1-Motion>", self.paint)

        # Draw the Tic-Tac-Toe board
        self.draw_board()

        # Create the board instance variable
        self.board = [
            [BoardState.EMPTY, BoardState.EMPTY, BoardState.EMPTY],
            [BoardState.EMPTY, BoardState.EMPTY, BoardState.EMPTY],
            [BoardState.EMPTY, BoardState.EMPTY, BoardState.EMPTY]
        ]

        self.move_symbol = BoardState.X
        self.first_move = FALSE

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

        # Reset the board
        self.board = [
            [BoardState.EMPTY, BoardState.EMPTY, BoardState.EMPTY],
            [BoardState.EMPTY, BoardState.EMPTY, BoardState.EMPTY],
            [BoardState.EMPTY, BoardState.EMPTY, BoardState.EMPTY]
        ]

        # Reset AI symbol
        self.first_move = FALSE

    def move_submitted(self):
        self.save_board()
        self.update_board_states()
        self.decide_move()

    def save_board(self):
        try:
            # Specify the file name and extension
            file_name = "slot1.jpg"

            # Get the path to the folder where the script is located
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Create the path to the AnalyzePictures folder
            pictures_folder = os.path.join(script_dir, "AnalyzePictures")

            # Create the AnalyzePictures folder if it doesn't exist
            os.makedirs(pictures_folder, exist_ok=True)

            # Specify the complete file path
            file_path = os.path.join(pictures_folder, file_name)

            # Save the screenshot of the entire grid
            x = self.root.winfo_rootx() + self.background.winfo_x()
            y = self.root.winfo_rooty() + self.background.winfo_y()
            x1 = x + self.background.winfo_width()
            y1 = y + self.background.winfo_height()

            # Save slot one picture
            ImageGrab.grab().crop((x + 100, y + 100, x + 290, y + 290)).save(file_path)

            # Reset the file name
            file_name = "slot2.jpg"
            # Specify the complete file path
            file_path = os.path.join(pictures_folder, file_name)

            # Save the screenshot of correct square
            ImageGrab.grab().crop((x + 305, y + 100, x + 495, y + 290)).save(file_path)

            # Reset the file name
            file_name = "slot3.jpg"
            # Specify the complete file path
            file_path = os.path.join(pictures_folder, file_name)

            # Save the screenshot of correct square
            ImageGrab.grab().crop((x + 505, y + 100, x + 695, y + 290)).save(file_path)

            # Reset the file name
            file_name = "slot4.jpg"
            # Specify the complete file path
            file_path = os.path.join(pictures_folder, file_name)

            # Save the screenshot of the entire grid
            ImageGrab.grab().crop((x + 100, y + 305, x + 290, y + 495)).save(file_path)

            # Reset the file name
            file_name = "slot5.jpg"
            # Specify the complete file path
            file_path = os.path.join(pictures_folder, file_name)

            # Save the screenshot of correct square
            ImageGrab.grab().crop((x + 305, y + 305, x + 495, y + 495)).save(file_path)

            # Reset the file name
            file_name = "slot6.jpg"
            # Specify the complete file path
            file_path = os.path.join(pictures_folder, file_name)

            # Save the screenshot of correct square
            ImageGrab.grab().crop((x + 505, y + 305, x + 695, y + 495)).save(file_path)

            # Reset the file name
            file_name = "slot7.jpg"
            # Specify the complete file path
            file_path = os.path.join(pictures_folder, file_name)

            # Save the screenshot of the entire grid
            ImageGrab.grab().crop((x + 100, y + 505, x + 290, y + 695)).save(file_path)

            # Reset the file name
            file_name = "slot8.jpg"
            # Specify the complete file path
            file_path = os.path.join(pictures_folder, file_name)

            # Save the screenshot of correct square
            ImageGrab.grab().crop((x + 305, y + 505, x + 495, y + 695)).save(file_path)

            # Reset the file name
            file_name = "slot9.jpg"
            # Specify the complete file path
            file_path = os.path.join(pictures_folder, file_name)

            # Save the screenshot of correct square
            ImageGrab.grab().crop((x + 505, y + 505, x + 695, y + 695)).save(file_path)

        except Exception as e:
            print("Error in saving the drawing:", str(e))


    def update_board_states(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == BoardState.EMPTY:
                    image_path = os.path.join("AnalyzePictures", f"slot{(i * 3) + (j + 1)}.jpg")
                    if self.has_drawing_in_square(image_path):
                        if self.is_x(image_path):
                            self.board[i][j] = BoardState.X
                            if not self.first_move:
                                self.move_symbol = BoardState.O
                        else:
                            self.board[i][j] = BoardState.O
                            if not self.first_move:
                                self.move_symbol = BoardState.X
                        self.first_move = TRUE
        print(self.board)

    def has_drawing_in_square(self, image_path):
        # Load the image
        image = Image.open(image_path)

        # Convert the image to grayscale
        image = image.convert("L")

        # Get the image dimensions
        width, height = image.size

        # Count the number of black pixels
        black_pixel_count = 0
        total_pixels = width * height

        # Iterate over each pixel and count the black pixels
        for x in range(width):
            for y in range(height):
                pixel_value = image.getpixel((x, y))
                if pixel_value == 0:
                    black_pixel_count += 1

        # Calculate the percentage of black pixels
        black_pixel_percentage = (black_pixel_count / total_pixels) * 100

        print("Black percentage: " + str(black_pixel_percentage))

        # Determine if the image is mostly white
        if black_pixel_percentage > 1:
            return True
        else:
            return False

    def is_x(self, file_path):
        # Load the square
        img = Image.open(file_path)
        img = img.resize((64, 64))  # Resize the image to match the input size of the model
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = img / 255.0  # Normalize the image

        # Reshape the image to match the input shape expected by the model (batch size, height, width, channels)
        img = img.reshape(1, 64, 64, 3)

        # Load the trained model
        model = tf.keras.models.load_model("tic_tac_toe_model.h5")

        # Predict the class of the image using the loaded model
        prediction = model.predict(img)
        if prediction > 0.5:
            print("The image is classified as an X.")
            return True
        else:
            print("The image is classified as an O.")
            return False

    def decide_move(self):
        empty_squares = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == BoardState.EMPTY:
                    empty_squares.append((i, j))

        if empty_squares:
            # Randomly select an empty square
            random_square = random.choice(empty_squares)
            row, col = random_square

            # Add the move_symbol to the selected square
            self.board[row][col] = self.move_symbol

            # Draw the move_symbol on the board
            self.draw_move_symbol(row, col)

        # Check for a winner
        winner = self.find_winner()
        if winner is None and len(empty_squares) == 0:
            # All squares are filled, and no winner, so it's a tie
            self.end_game(None)

    def draw_move_symbol(self, row, col):
        x = 200 + col * 200
        y = 200 + row * 200

        if self.move_symbol == BoardState.X:
            self.background.create_line(x - 50, y - 50, x + 50, y + 50, width=5, fill='red')
            self.background.create_line(x + 50, y - 50, x - 50, y + 50, width=5, fill='red')
        else:
            self.background.create_oval(x - 50, y - 50, x + 50, y + 50, width=5, outline='red')

    def find_winner(self):
        # Check rows
        for row in self.board:
            if row[0] != BoardState.EMPTY and row[0] == row[1] == row[2]:
                self.end_game(row[0])
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] != BoardState.EMPTY:
                if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                    self.end_game(self.board[0][col])
                    return self.board[0][col]

        # Check diagonals
        if self.board[0][0] != BoardState.EMPTY and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.end_game(self.board[0][0])
            return self.board[0][0]
        if self.board[0][2] != BoardState.EMPTY and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.end_game(self.board[0][2])
            return self.board[0][2]

        # No winner
        return None

    def end_game(self, winning_symbol):
        if winning_symbol is None:
            self.result_label.config(text="It's a tie!")
            print("It's a tie!")
        elif winning_symbol != self.move_symbol:
            self.result_label.config(text="You win!")
            print("You win!")
        else:
            self.result_label.config(text="You lose!")
            print("You lose!")
        print("Resetting board...")
        time.sleep(3)
        self.reset_board()


if __name__ == "__main__":
    root = Tk()
    p = Draw(root)
    root.mainloop()

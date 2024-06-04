import tkinter as tk
from tkinter import ttk
from notebot_ai import GPTResponder
from notebot_commands.basic_commands import CommandHandler
from notebot_ui.NoteBotUI import NoteBotUI


def main():
    # Create the main window
    root = tk.Tk()
    root.title("NoteBot Notepad")
    root.geometry("800x600")
    root.configure(bg='gray')

    # Initialize the AI responder and command handler
    ai_responder = GPTResponder()
    command_handler = CommandHandler()

    # Initialize and start the UI
    app = NoteBotUI(root, ai_responder, command_handler)
    app.run()


if __name__ == "__main__":
    main()

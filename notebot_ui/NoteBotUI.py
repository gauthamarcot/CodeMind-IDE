import tkinter as tk
from tkinter import ttk

class NoteBotUI:
    def __init__(self, root, ai_responder, command_handler):
        self.root = root
        self.ai_responder = ai_responder
        self.command_handler = command_handler
        self.current_ascii_index = 0
        self.ascii_art_list = [
            """
              _____
             /     \\
            | () () |
             \\  ^  /
              |||||
              |||||
            """,
            """
              _____
             /     \\
            | >   < |
             \\  ^  /
              |||||
              |||||
            """,
            """
              _____
             /     \\
            |  O O  |
             \\  ^  /
              |||||
              |||||
            """
        ]

        self.setup_ui()

    def setup_ui(self):
        # Create tabs
        tab_control = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(tab_control)
        self.tab2 = ttk.Frame(tab_control)
        tab_control.add(self.tab1, text='Tab 1')
        tab_control.add(self.tab2, text='Tab 2')
        tab_control.pack(expand=1, fill='both')

        # ASCII AI figure
        self.ai_label = tk.Label(self.tab1, text=self.ascii_art_list[self.current_ascii_index], bg="gray", fg="red", font=("Courier", 12))
        self.ai_label.place(relx=0.75, rely=0.1, relwidth=0.2, relheight=0.2)

        # Text area for main interaction
        self.text_area = tk.Text(self.tab1, wrap='word', bg="white", fg="black")
        self.text_area.place(relx=0.05, rely=0.35, relwidth=0.9, relheight=0.5)

        # Specific question area
        self.specific_question_area = tk.Entry(self.tab1, bg="white", fg="black")
        self.specific_question_area.place(relx=0.05, rely=0.9, relwidth=0.8, relheight=0.05)

        # Submit button
        submit_button = tk.Button(self.tab1, text="Submit", command=self.on_submit, bg="red", fg="white")
        submit_button.place(relx=0.86, rely=0.9, relwidth=0.09, relheight=0.05)

    def update_ascii_art(self):
        self.current_ascii_index = (self.current_ascii_index + 1) % len(self.ascii_art_list)
        self.ai_label.config(text=self.ascii_art_list[self.current_ascii_index])

    def on_submit(self):
        try:
            user_query = self.text_area.get("1.0", tk.END).strip()
            specific_query = self.specific_question_area.get().strip()

            if user_query.startswith('/'):
                command = user_query.split()[0]
                data = self.text_area.get("1.0", tk.END).split(command, 1)[-1]
                response = self.command_handler.handle_command(command, data)
                self.text_area.insert(tk.END, f"\n{response}\n")
            elif specific_query:
                response = self.ai_responder.generate_response(specific_query)
                self.text_area.insert(tk.END, f"\nAI: {response}\n")
            else:
                response = self.ai_responder.generate_response(user_query)
                self.text_area.insert(tk.END, f"\nAI: {response}\n")

            self.specific_question_area.delete(0, tk.END)
            self.update_ascii_art()
        except Exception as e:
            logging.error(f"Error on submit: {e}")

    def run(self):
        self.root.mainloop()

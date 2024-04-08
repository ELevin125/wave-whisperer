import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox

from app.Embedder import Embedder
from app.Extractor import Extractor

class WaveWhispererApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Wave Whisperer")

        self.selected_path = "./assets/audioSample.wav"

        self.embed_option = tk.IntVar(value=1)
        self.output_message = tk.StringVar(value=" ")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Select an option:").grid(row=0, column=0, sticky="w")

        # Change modes
        embed_radio = tk.Radiobutton(self.master, text="Embed Message", variable=self.embed_option, value=1, command=self.show_message_input)
        embed_radio.grid(row=1, column=0, sticky="w")

        extract_radio = tk.Radiobutton(self.master, text="Extract Message", variable=self.embed_option, value=2, command=self.show_output)
        extract_radio.grid(row=2, column=0, sticky="w")

        # GUI for embedding
        self.message_label = tk.Label(self.master, text="Insert Message:")
        self.message_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.message_entry = tk.Text(self.master, height=1, width=50, wrap=tk.WORD)
        self.message_entry.grid(row=4, column=0, padx=10, pady=5, columnspan=2, sticky="w")

        # GUI for extraction
        self.output_label = tk.Label(self.master, text="Message in provided file:")
        self.output_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.output_text = tk.Text(self.master, height=1, width=50, state=tk.DISABLED, wrap=tk.WORD)
        self.output_text.grid(row=4, column=0, padx=10, pady=5, columnspan=2, sticky="w")
        
        # other GUI elements
        self.browse_button = tk.Button(self.master, text="Browse File", command=self.browse_file)
        self.browse_button.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.file_path_label = tk.Label(self.master, text="Selected File Path: " + self.selected_path)
        self.file_path_label.grid(row=5, column=1, columnspan=1, pady=5, sticky="w")

        self.process_button = tk.Button(self.master, text="Process", command=self.process)
        self.process_button.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        # set app into Embed mode by default
        self.output_text.grid_remove()
        self.output_label.grid_remove()
        self.message_entry.grid()
        self.message_label.grid()

    def _set_output_text(self, str):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, str)
        self.output_text.config(state=tk.DISABLED)

    def show_message_input(self):
        self.output_text.grid_remove()
        self.output_label.grid_remove()
        self.message_entry.grid()
        self.message_label.grid()

    def show_output(self):
        self.message_entry.grid_remove()
        self.message_label.grid_remove()
        self.output_text.grid()
        self.output_label.grid()

    def browse_file(self):
        self.selected_path = filedialog.askopenfilename()
        self.file_path_label.config(text="Selected File Path: " + self.selected_path)

    def process(self):
        if self.embed_option.get() == 1:
            # Embed Message
            embedder = Embedder(self.selected_path)
            message_to_embed = str(self.message_entry.get("1.0", "end"))

            embedder.embed_message(message_to_embed, self.selected_path[:-4] + "_embedded.wav")

            messagebox.showinfo("Embedding Done", "Embedding process completed successfully!")
        elif self.embed_option.get() == 2:
            # Extract Message
            extractor = Extractor(self.selected_path)
            extracted_message = extractor.extract_message()
            self._set_output_text(extracted_message)

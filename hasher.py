import tkinter as tk
from tkinter import filedialog
import hashlib

class HashGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hash Generator")
        self.root.geometry("700x500")  # Set a fixed window size

        self.file_path = ""
        
        self.file_label = tk.Label(root, text="Selected File:")
        self.file_label.pack()

        self.selected_file_label = tk.Label(root, text="")
        self.selected_file_label.pack()

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.result_text = tk.Text(root, wrap=tk.WORD, height=40)  # Wrap text and set height
        self.result_text.pack()

    def browse_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.selected_file_label.config(text=f"File: {self.file_path}")
            self.calculate_hashes()

    def calculate_hashes(self):
        if self.file_path:
            hash_algorithms = ['md5', 'sha1', 'sha256', 'sha3_256', 'sha3_512', 'blake2b', 'blake2s']
            hash_results = {}

            with open(self.file_path, 'rb') as file:
                data = file.read()
                for algorithm in hash_algorithms:
                    hash_obj = hashlib.new(algorithm)
                    hash_obj.update(data)
                    hash_results[algorithm] = hash_obj.hexdigest()

            self.display_results(hash_results)
        else:
            self.result_text.delete("1.0", tk.END)  # Clear the text widget
            self.result_text.insert(tk.END, "Please select a file first.")

    def display_results(self, results):
        self.result_text.delete("1.0", tk.END)  # Clear the text widget
        self.result_text.insert(tk.END, "Hashes:\n\n")
        for algorithm, hash_value in results.items():
            hash_text = f"{algorithm.upper()}: {hash_value}\n"
            self.result_text.insert(tk.END, hash_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = HashGeneratorApp(root)
    root.mainloop()

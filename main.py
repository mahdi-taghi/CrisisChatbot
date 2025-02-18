import tkinter as tk
from tkinter import scrolledtext
import ollama

SYSTEM_PROMPT = """
You are a Crisis Management AI Expert.
Your job is to provide professional guidance on crisis management, risk assessment, disaster response, and emergency planning.
You should give clear, structured, and practical advice.
If a user’s question lacks clarity, politely ask for more details.
"""

def generate_response(query):
    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query}
        ]
    )
    return response["message"]["content"]

class CrisisChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot")

        self.chat_box = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
        self.chat_box.pack(pady=10)
        self.chat_box.config(state=tk.DISABLED)

        self.input_box = tk.Entry(master, width=50, font=("Arial", 14))
        self.input_box.pack(pady=5)
        self.input_box.bind("<Return>", self.process_query)

        self.send_btn = tk.Button(master, text="Ask", command=self.process_query, font=("Arial", 12))
        self.send_btn.pack()

    def process_query(self, event=None):
        user_text = self.input_box.get().strip()
        if user_text:
            self.update_chat(f"You: {user_text}")
            self.input_box.delete(0, tk.END)
            response_text = generate_response(user_text)
            self.update_chat(f"Bot: {response_text}")

    def update_chat(self, message):
        self.chat_box.config(state=tk.NORMAL)
        self.chat_box.insert(tk.END, message + "\n\n")
        self.chat_box.config(state=tk.DISABLED)
        self.chat_box.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    while True:
        try:
            app = CrisisChatApp(root)
            root.mainloop()
        except Exception:
            pass

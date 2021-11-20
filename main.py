import requests
from tkinter import *


def get_stats(call):
    r = requests.get(call)
    return r.json()


def show_tq():
    user_key = key.get()
    url_boxes = f"https://api.hypixel.net/key?key={user_key}"
    data = get_stats(url_boxes)
    queries = int(data["player"]["stats"]["Bedwars"]["bedwars_boxes"])

    Label(root, text=f"Queries: {queries + 1}").grid(row=3, column=1)


root = Tk()
root.title("Bw Loot Boxes")

Label(root, text="Enter your API Key here:").grid(row=1, column=1)
Label(root, text="Enter your UUID here:  ").grid(row=2, column=1)

key = StringVar()
Entry(root, textvariable=key).grid(row=1, column=2, padx=(0, 5))

Button(root, text="Count Loot Boxes", command=show_tq).grid(row=3, column=2)

root.mainloop()


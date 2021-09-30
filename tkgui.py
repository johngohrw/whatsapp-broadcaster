
import tkinter as tk
import math

phones = ''
message = '' 
interval = ''

def runGUI():        
    # variables
    width = 800
    height = 550
    scrollbarWidth = 20
    # variables end

    window = tk.Tk()
    window.geometry('{}x{}'.format(width, height))
    window.resizable(False, False) 
    window.title("whatsapp broadcaster")

    def handle_click(evt):
        global phones
        global message
        global interval

        phones = phonesEntry.get("1.0",tk.END)
        message = msgEntry.get("1.0",tk.END)
        interval = intervalEntry.get()

        window.destroy()

    # greeting
    greeting = tk.Label(window, text="whatsapp broadcaster", font=("Arial", "16", "bold"))
    greeting.place(x=0, y=8, width=width, height=50)

    leftWidth = math.floor(width * 0.36)
    rightWidth = math.floor(width * 0.64)

    # instructions
    instruction1 = tk.Label(window, text="enter one phone number per-line", font=("Arial", "10"))
    instruction1.place(x=0, y=62, width=leftWidth, height=15)
    instruction2 = tk.Label(window, text="(numbers only, no space, no symbols)", font=("Arial", "10"))
    instruction2.place(x=0, y=77, width=leftWidth, height=15)

    # phone entry
    entry = {"margin": 12, "height": 312, "y": 92}

    scroll = tk.Scrollbar(window)
    scroll.place(x=leftWidth-scrollbarWidth-entry["margin"], y=entry["y"]+entry["margin"], width=scrollbarWidth, height=entry["height"])

    phonesEntry = tk.Text(yscrollcommand=scroll.set, fg="black", bg="#ededed", width=50, font=("Arial", "10"))
    phonesEntry.place(x=entry["margin"], y=entry["y"]+entry["margin"], width=leftWidth-scrollbarWidth-(entry["margin"] * 2), height=entry["height"])

    scroll.config(command=phonesEntry.yview)

    # instructions2
    instruction3 = tk.Label(window, text="enter the message to broadcast below", font=("Arial", "10"))
    instruction3.place(x=leftWidth, y=62, width=rightWidth, height=30)

    # message to broadcast
    entry2 = {"margin": 12, "height": 270, "y": 92}

    scroll2 = tk.Scrollbar(window)
    scroll2.place(x=leftWidth+rightWidth-scrollbarWidth-entry2["margin"], y=entry2["y"]+entry2["margin"], width=scrollbarWidth, height=entry2["height"])

    msgEntry = tk.Text(yscrollcommand=scroll2.set, fg="black", bg="#ededed", width=50, font=("Arial", "10"))
    msgEntry.place(x=leftWidth + entry2["margin"], y=entry2["y"]+entry2["margin"], width=rightWidth-scrollbarWidth-(entry2["margin"] * 2), height=entry2["height"])

    scroll2.config(command=msgEntry.yview)

    # instructions2
    instruction3 = tk.Label(window, text="enter the message to broadcast below", font=("Arial", "10"))
    instruction3.place(x=leftWidth, y=62, width=rightWidth, height=30)

    # interval between messages
    entry3 = {"margin": 12, "height": 30, "y": 386}

    intervalLabel = tk.Label(window, text="interval between messages (seconds):", font=("Arial", "10"))
    intervalLabel.place(x=leftWidth + entry3["margin"], y=entry3["y"], width=260, height=entry3["height"])

    intervalEntry = tk.Entry(fg="black", bg="#ededed", width=50, font=("Arial", "14"))
    intervalEntry.place(x=leftWidth + entry3["margin"] + 260, y=entry3["y"], width=rightWidth-(entry3["margin"] * 2) - 260, height=entry3["height"])
    intervalEntry.insert(-1, "60") # Default value

    # info
    infoLabel = tk.Label(window, text="make sure everything is correct. a Chrome window will open after clicking the button", font=("Arial", "10"))
    infoLabel.place(x=0, y=420, width=width, height=80)

    # button
    button = tk.Button(text="start broadcasting", bg="#010101",fg="white")
    button.place(x=12, y=500, width=width - 24, height=40)
    button.bind("<Button-1>", handle_click)

    window.mainloop()

    if (len(phones) == 0 or len(message) == 0):
        quit()

    return {"phones": phones, "message": message, "interval": interval}


    

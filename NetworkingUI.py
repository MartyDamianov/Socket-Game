import tkinter as tk

network = []
def NetworkUI():
    global network
    window = tk.Tk()
    window.title("Networking demo")
    window.geometry("400x400")

    def client():
        global network
        Client.destroy()
        Server.destroy()
        
        port = tk.StringVar()
        user = tk.StringVar()
        username = tk.StringVar()

        entry = tk.Entry(window, textvariable = port).place(x = 140, y = 0)
        entry2 = tk.Entry(window, textvariable = user).place(x = 140, y = 40)
        entry3 = tk.Entry(window, textvariable = username).place(x = 140, y = 80)

        def Enter():
            global network
            Port = port.get()
            User = user.get()
            Username = username.get()
            network = [Port, User, Username]

            window.destroy()
            
        enter = tk.Button(window, text = "Enter", command = Enter).place(x = 180, y = 110)

        label = tk.Label(window, text = "Port : ").place(x = 100, y = 0)
        label2 = tk.Label(window, text = "Host : ").place(x = 100, y = 40)
        label3 = tk.Label(window, text = "Username : ").place(x = 70, y = 80)

    def server():
        global network
        Client.destroy()
        Server.destroy()
        
        username = tk.StringVar()
        entry = tk.Entry(window, textvariable = username).place(x = 140, y = 0)

        def Enter():
            global network
            Username = username.get()
            network = [Username]
            window.destroy()

        enter = tk.Button(window, text = "Enter", command = Enter).place(x = 180, y = 30)
        label = tk.Label(window, text = "Username : ").place(x = 70, y = 0)

    Client = tk.Button(window, text = "Join game", command = client)
    Client.pack()
    Server = tk.Button(window, text = "Host game", command = server)
    Server.pack()

    tk.mainloop()
    return network


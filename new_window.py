import tkinter as tk

root = tk.Tk()
root.withdraw()

current_window = None

def  replace_window(root):
    """Destroy current window, create new window"""
    global current_window
    if current_window is not None:
        current_window.destroy()
    current_window = tk.Toplevel(root)

    # if the user kills the window via the window manager,
    # exit the application. 
    current_window.wm_protocol("WM_DELETE_WINDOW", root.destroy)

    return current_window

counter = 0
def new_window():
    global counter
    counter += 1

    window = replace_window(root)
    label = tk.Label(window, text="This is window %s" % counter)
    button = tk.Button(window, text="Create a new window", command=new_window)
    label.pack(fill="both", expand=True, padx=20, pady=20)
    button.pack(padx=10, pady=10)

window = new_window()

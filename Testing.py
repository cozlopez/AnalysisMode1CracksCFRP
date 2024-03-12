import tkinter as tk
import os

# Create the root window
root = tk.Tk()

# Set the title of the window
root.title("Folder Selection")

# Set the size of the window
root.geometry("400x200")

# Get the list of subfolders in the directory
base_dir = os.path.join(os.getcwd(), "Images")
subfolders = [f.name for f in os.scandir(base_dir) if f.is_dir()]

# Create a StringVar to store the selected folder
selected_folder = tk.StringVar()

# Function to handle the folder selection
def select_folder(evt):
    selected_folder.set(listbox.get(listbox.curselection()))
    print("Selected Folder:", selected_folder.get())
    root.after(1000, root.destroy)  # Close the window after 1000 milliseconds

# Create a Label to display a message
label = tk.Label(root, text="Please select a folder:")
label.pack(pady=10)

# Create a Listbox to display the subfolders
listbox = tk.Listbox(root)
listbox.pack(pady=20)

# Add the subfolders to the Listbox
for folder in subfolders:
    listbox.insert(tk.END, folder)

# Bind the select_folder function to the Listbox selection event
listbox.bind('<<ListboxSelect>>', select_folder)

# Run the main event loop
root.mainloop()

# After the window is closed, the selected folder can be retrieved from the StringVar
print("Selected Folder (after window closed):", selected_folder.get())
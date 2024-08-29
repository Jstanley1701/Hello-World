#Backup Script
import os
import shutil
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def backup_files(source_dir, dest_dir):
    if not os.path.isdir(source_dir):
        messagebox.showerror("Error", f"Source directory '{source_dir}' does not exist.")
        return
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_dir = os.path.join(dest_dir, f"backup_{timestamp}")
    os.makedirs(backup_dir, exist_ok=True)
    
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(backup_dir, item)
        
        if os.path.isdir(source_path):
            shutil.copytree(source_path, dest_path)
        else:
            shutil.copy2(source_path, dest_path)
    
    messagebox.showinfo("Success", f"Backup completed successfully to '{backup_dir}'.")

def select_source_directory():
    source_dir = filedialog.askdirectory(title="Select Source Directory")
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_dir)

def select_destination_directory():
    dest_dir = filedialog.askdirectory(title="Select Destination Directory")
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, dest_dir)

def start_backup():
    source_dir = source_entry.get()
    dest_dir = dest_entry.get()
    if not source_dir or not dest_dir:
        messagebox.showwarning("Input Error", "Please select both source and destination directories.")
        return
    backup_files(source_dir, dest_dir)

# Create the main application window
root = tk.Tk()
root.title("Backup Utility")

# Create and place the widgets
tk.Label(root, text="Source Directory:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_source_directory).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Destination Directory:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
dest_entry = tk.Entry(root, width=50)
dest_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_destination_directory).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Start Backup", command=start_backup).grid(row=2, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()

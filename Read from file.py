import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os

class LabelInput:
    """
    This class represents a single input field for a label.
    """
    def __init__(self, master, label_text, row, default_text):
        """
        Constructor for the LabelInput class.

        Parameters:
            - master (tkinter.Tk): the parent window
            - label_text (str): the text to display as the label for the input field
            - row (int): the row in which to place the input field
            - default_text (str): the default text to display in the input field
        """
        self.label = tk.Label(master, text=label_text, font=("Arial", 12))
        self.label.grid(row=row, column=0, padx=10, pady=10, sticky=tk.W)
        self.entry = tk.Entry(master, font=("Arial", 12), width=40)
        self.entry.grid(row=row, column=1, padx=10, pady=10)
        self.entry.insert(0, default_text)

class LabelEditor:
    """
    This class represents the main window for the label editor.
    """
    def __init__(self, master):
        """
        Constructor for the LabelEditor class.

        Parameters:
            - master (tkinter.Tk): the parent window
        """
        self.master = master
        self.master.title("Label Editor - Telefónica/Movistar")
        self.label_inputs = []

        self.label_list_button = tk.Button(master, text="Lista de Etiquetas", font=("Arial", 12), command=self.open_label_list_window)
        self.label_list_button.grid(row=0, column=0, padx=10, pady=10)

        self.create_new_label_button = tk.Button(master, text="Crear nueva Etiqueta", font=("Arial", 12), command=self.create_new_label)
        self.create_new_label_button.grid(row=0, column=2, padx=10, pady=10)

        # Try to open the label data file
        try:
            with open("label_data.json", "r") as f:
                label_data = json.load(f)
        except FileNotFoundError:
            label_data = {"Nombre Etiqueta (interno):" : "" , "Pedido/Derivada:": "", "Código:": "", "Descripción:": "", "Peso individual de cada cable:": "", "Cables por caja:": "", "Cajas por pallet:": ""}

        # Center the window on the screen
        self.master.geometry("+%d+%d" % ((self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 3, (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3))

        # Create the labels + input fields for each value inside the "label_data.json" file
        self.label_inputs = []
        for i, label_text in enumerate(label_data.keys()):
            label_input = LabelInput(master, label_text, i, label_data[label_text])
            label_input.entry.configure(state="disabled", disabledforeground="black")
            self.label_inputs.append(label_input)

        # This places the label list and create new label buttons on top of the main GUI
        for i, label_input in enumerate(self.label_inputs):
            label_input.label.grid(row=i + 1, column=0, padx=10, pady=10, sticky=tk.W)
            label_input.entry.grid(row=i + 1, column=1, padx=10, pady=10, sticky=tk.W)

        # Create the "Pallets a preparar" input field
        self.pallets_label = tk.Label(master, text="Pallets a preparar:", font=("Arial", 12))
        self.pallets_label.grid(row=len(label_data) + 1, column=0, padx=10, pady=10, sticky=tk.W)
        self.pallets_entry = tk.Entry(master, font=("Arial", 12), width=40)
        self.pallets_entry.grid(row=len(label_data) + 1, column=1, padx=10, pady=10)
        self.pallets_entry.insert(0, "")
        self.pallets_entry.bind("<KeyRelease>", self.validate_pallets_entry)

        # Create a spacer between the "Pallets a preparar" field and the save button
        #spacer = tk.Frame(master)
        #spacer.grid(row=len(label_data) + 2, column=0)

        # Create the "Modify" button
        self.modify_button = tk.Button(master, text="Modificar", font=("Arial", 12), command=self.modify, state=tk.DISABLED)
        self.modify_button.grid(row=len(label_data) + 3, column=0, padx=10, pady=10)

        # Create the "Save" button
        self.save_button = tk.Button(master, text="Guardar", font=("Arial", 12), command=self.save, state=tk.DISABLED)
        self.save_button.grid(row=len(label_data) + 3, column=1, padx=10, pady=10)

        # Create the "Generate files" button
        self.generate_files_button = tk.Button(master, text="Generar archivos", font=("Arial", 12), state=tk.DISABLED)
        self.generate_files_button.grid(row=len(label_data) + 3, column=2, padx=10, pady=10)

    def modify(self):
        """
        Enables all the input fields and the save button.
        """
        for label_input in self.label_inputs:
            label_input.entry.configure(state="normal")
        self.save_button.configure(state="normal")
        self.modify_button.configure(state="disabled")
        self.generate_files_button.configure(state="disabled")

    def save(self):
        """
        Saves the input data to the label data file and disables all the input fields and the save button.
        """
        label_data = {}
        for label_input in self.label_inputs:
            label_data[label_input.label.cget("text")] = label_input.entry.get()
            label_input.entry.configure(state="disabled")
        with open("label_data.json", "w") as f:
            json.dump(label_data, f)
        self.save_button.configure(state="disabled")
        self.modify_button.configure(state="normal")
        self.generate_files_button.configure(state="normal")
        #validate pallets entry
        self.validate_pallets_entry(None)

    def validate_pallets_entry(self, event):
        pallets_value = self.pallets_entry.get()
        if pallets_value.isnumeric() and int(pallets_value) > 0 and int(pallets_value) < 100:
            self.generate_files_button.configure(state="normal")
        else:
            self.generate_files_button.configure(state="disabled")

    # New code

    def open_label_list_window(self):
        label_list_window = tk.Toplevel(self.master)
        label_list_window.title("Label List")

        label_list_window.grab_set()  # Set modal state

        label_files = [filename for filename in os.listdir("Telefónica Labels") if filename.endswith(".json")]
        label_listbox = tk.Listbox(label_list_window, selectmode=tk.SINGLE)

        scrollbar = tk.Scrollbar(label_list_window, orient=tk.VERTICAL)
        label_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=label_listbox.yview)

        for label_file in label_files:
            label_listbox.insert(tk.END, label_file)

        label_listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        scrollbar.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ns")

        label_list_window.rowconfigure(0, weight=1)
        label_list_window.columnconfigure(0, weight=1)

        label_list_window.minsize(width=400, height=450)  # Adjust the minimum size as needed

        def open_selected_label():
            selected_item = label_listbox.curselection()
            if selected_item:
                selected_label = label_listbox.get(selected_item)
                with open(os.path.join("Telefónica Labels", selected_label), "r") as f:
                    label_data = json.load(f)
                    for label_input in self.label_inputs:
                        label_input.entry.configure(state="normal")
                        label_input.entry.delete(0, tk.END)
                        label_input.entry.insert(0, label_data.get(label_input.label.cget("text"), ""))
                        label_input.entry.configure(state="disabled")
                label_list_window.destroy()
                # enable modify button

        def delete_selected_label():
            selected_item = label_listbox.curselection()
            if selected_item:
                selected_label = label_listbox.get(selected_item)
                confirmation = messagebox.askyesno("Confirm Deletion",
                                                   f"Are you sure you want to delete '{selected_label}'?")
                if confirmation:
                    os.remove(os.path.join("Telefónica Labels", selected_label))
                    label_listbox.delete(selected_item)
                    label_listbox.selection_clear(0, tk.END)

        open_button = tk.Button(label_list_window, text="Open", command=open_selected_label)
        delete_button = tk.Button(label_list_window, text="Delete", command=delete_selected_label)

        label_listbox.grid(row=0, column=0, padx=10, pady=10)
        open_button.grid(row=1, column=0, padx=10, pady=10)
        delete_button.grid(row=2, column=0, padx=10, pady=10)

    def create_new_label(self):
        for label_input in self.label_inputs:
            label_input.entry.configure(state="normal")
            label_input.entry.delete(0, tk.END)
        #self.save_button.configure(state="normal")


root = tk.Tk()
label_editor = LabelEditor(root)

root.mainloop()
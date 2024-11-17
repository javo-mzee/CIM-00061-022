import tkinter as tk
from tkinter import ttk

def create_employee_management_system():
    # Initialize the main window
    root = tk.Tk()
    root.title("Employee Management System")
    root.geometry("800x600")

    # Create a notebook for tabs
    notebook = ttk.Notebook(root)

    # Create tabs
    tabs = {
        "Registration": tk.Frame(notebook),
        "Login": tk.Frame(notebook),
        "Finance": tk.Frame(notebook),
        "Departments": tk.Frame(notebook),
        "Procurement": tk.Frame(notebook),
        "Leave": tk.Frame(notebook),
    }

    for name, frame in tabs.items():
        notebook.add(frame, text=name)

    notebook.pack(expand=1, fill="both")

    # Add content to each tab
    def populate_registration_tab():
        tk.Label(tabs["Registration"], text="Employee Registration", font=("Arial", 16)).pack(pady=10)
        tk.Label(tabs["Registration"], text="Name:").pack(anchor="w", padx=20)
        tk.Entry(tabs["Registration"]).pack(fill="x", padx=20, pady=5)
        tk.Label(tabs["Registration"], text="Email:").pack(anchor="w", padx=20)
        tk.Entry(tabs["Registration"]).pack(fill="x", padx=20, pady=5)
        tk.Label(tabs["Registration"], text="Position:").pack(anchor="w", padx=20)
        tk.Entry(tabs["Registration"]).pack(fill="x", padx=20, pady=5)
        tk.Button(tabs["Registration"], text="Submit", command=lambda: print("Registration Submitted")).pack(pady=10)

    def populate_login_tab():
        tk.Label(tabs["Login"], text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(tabs["Login"], text="Username:").pack(anchor="w", padx=20)
        tk.Entry(tabs["Login"]).pack(fill="x", padx=20, pady=5)
        tk.Label(tabs["Login"], text="Password:").pack(anchor="w", padx=20)
        tk.Entry(tabs["Login"], show="*").pack(fill="x", padx=20, pady=5)
        tk.Button(tabs["Login"], text="Login", command=lambda: print("Login Attempt")).pack(pady=10)

    def populate_finance_tab():
        tk.Label(tabs["Finance"], text="Finance Module", font=("Arial", 16)).pack(pady=10)
        tk.Label(tabs["Finance"], text="View salary details or update records here.").pack(pady=20)

    def populate_departments_tab():
        tk.Label(tabs["Departments"], text="Departments Module", font=("Arial", 16)).pack(pady=10)
        tk.Label(tabs["Departments"], text="Manage or view departments here.").pack(pady=20)

    def populate_procurement_tab():
        tk.Label(tabs["Procurement"], text="Procurement Module", font=("Arial", 16)).pack(pady=10)
        tk.Label(tabs["Procurement"], text="Track or request resources here.").pack(pady=20)

    def populate_leave_tab():
        tk.Label(tabs["Leave"], text="Leave Management", font=("Arial", 16)).pack(pady=10)
        tk.Label(tabs["Leave"], text="Apply for leave or check leave status.").pack(pady=20)

    # Populate each tab
    populate_registration_tab()
    populate_login_tab()
    populate_finance_tab()
    populate_departments_tab()
    populate_procurement_tab()
    populate_leave_tab()

    # Run the application
    root.mainloop()

# Run the employee management system
create_employee_management_system()

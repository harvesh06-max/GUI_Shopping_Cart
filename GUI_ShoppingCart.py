from tkinter import *
from tkinter import messagebox

# ---Product prices map---
item_prices = {
    "Bread": 40, "Milk": 30, "Eggs": 50, "Dal": 90, "Rice": 70, "Oil": 100, "Sugar": 40, "Salt": 25, "Spices": 60, "Lays": 20,
    "Pen": 10, "Notebook": 50, "Eraser": 5, "Sharpener": 5, "Ruler": 15, "Marker": 20, "Highlighter": 25, "Stapler": 40, "Tape": 30, "Glue": 30,
    "T-Shirt": 250, "Jeans": 900, "Jacket": 1200, "Dress": 1100, "Kurta": 800, "Shorts": 400, "Skirt": 500, "Sweater": 700, "Blazer": 1500, "Cardigan": 650,
    "Smartphone": 12000, "Laptop": 50000, "Tablet": 18000, "Headphones": 2000, "Smartwatch": 4000, "Camera": 35000, "Speaker": 3000, "Monitor": 8000, "Keyboard": 900, "Mouse": 500,
    "Watch": 1500, "Sunglasses": 800, "Belt": 400, "Wallet": 700, "Bag": 1000, "Hat": 300, "Scarf": 350, "Gloves": 250, "Jewelry": 5000, "Tie": 200,
}

# --- Cart dictionary: stores added items and quantities ---
cart = {}

def add_to_cart(item_name, price):
    if item_name in cart:
        cart[item_name]["quantity"] += 1
    else:
        cart[item_name] = {"price": price, "quantity": 1}
    print(f"Added {item_name} to cart.")

def show_category_items(category):
    for widget in items_frame.winfo_children():
        widget.destroy()

    category_items = {
        "Grocery": [
            {"name": "Bread", "image": "bread.png"},
            {"name": "Milk", "image": "milk.png"},
            {"name": "Eggs", "image": "eggs.png"},
            {"name": "Dal", "image": "dal.png"},
            {"name": "Rice", "image": "rice.png"},
            {"name": "Oil", "image": "oil.png"},
            {"name": "Sugar", "image": "sugar.png"},
            {"name": "Salt", "image": "salt.png"},
            {"name": "Spices", "image": "spices.png"},
            {"name": "Lays", "image": "lays.png"},
        ],
        "Stationery": [
            {"name": "Pen", "image": "pen.png"},
            {"name": "Notebook", "image": "notebook.png"},
            {"name": "Eraser", "image": "eraser.png"},
            {"name": "Sharpener", "image": "sharpener.png"},
            {"name": "Ruler", "image": "ruler.png"},
            {"name": "Marker", "image": "marker.png"},
            {"name": "Highlighter", "image": "highlighter.png"},
            {"name": "Stapler", "image": "stapler.png"},
            {"name": "Tape", "image": "tape.png"},
            {"name": "Glue", "image": "glue.png"},
        ],
        "Clothing": [
            {"name": "T-Shirt", "image": "tshirt.png"},
            {"name": "Jeans", "image": "jeans.png"},
            {"name": "Jacket", "image": "jacket.png"},
            {"name": "Dress", "image": "dress.png"},
            {"name": "Kurta", "image": "kurta.png"},
            {"name": "Shorts", "image": "shorts.png"},
            {"name": "Skirt", "image": "skirt.png"},
            {"name": "Sweater", "image": "sweater.png"},
            {"name": "Blazer", "image": "blazer.png"},
            {"name": "Cardigan", "image": "cardigan.png"},
        ],
        "Electronics": [
            {"name": "Smartphone", "image": "smartphone.png"},
            {"name": "Laptop", "image": "laptop.png"},
            {"name": "Tablet", "image": "tablet.png"},
            {"name": "Headphones", "image": "headphones.png"},
            {"name": "Smartwatch", "image": "smartwatch.png"},
            {"name": "Camera", "image": "camera.png"},
            {"name": "Speaker", "image": "speaker.png"},
            {"name": "Monitor", "image": "monitor.png"},
            {"name": "Keyboard", "image": "keyboard.png"},
            {"name": "Mouse", "image": "mouse.png"},
        ],
        "Accessories": [
            {"name": "Watch", "image": "watch.png"},
            {"name": "Sunglasses", "image": "sunglasses.png"},
            {"name": "Belt", "image": "belt.png"},
            {"name": "Wallet", "image": "wallet.png"},
            {"name": "Bag", "image": "bag.png"},
            {"name": "Hat", "image": "hat.png"},
            {"name": "Scarf", "image": "scarf.png"},
            {"name": "Gloves", "image": "gloves.png"},
            {"name": "Jewelry", "image": "jewelry.png"},
            {"name": "Tie", "image": "tie.png"},
        ]
    }

    items = category_items.get(category, [])

    max_columns = 5
    row = 0
    col = 0

    for item in items:
        # Try to load image, skip if not found
        try:
            img = PhotoImage(file=item["image"])
        except:
            img = None

        # Use lambda to pass name and price into add_to_cart
        btn = Button(items_frame,
                     text=f"{item['name']}\n₹{item_prices.get(item['name'], 0)}",
                     command=lambda n=item["name"], p=item_prices.get(item["name"], 0): add_to_cart(n, p),
                     image=img,
                     compound='top',
                     font=("Arial", 14),
                     bg="#328f87",
                     fg="#032b28",
                     activebackground="#328f87",
                     activeforeground="#032b28")
        btn.image = img
        btn.grid(row=row, column=col, padx=10, pady=10)

        col += 1
        if col >= max_columns:
            col = 0
            row += 1

def checkout():
    if not cart:
        messagebox.showinfo("Checkout", "Cart is empty!")
        return
    total = 0
    summary = ""
    for item_name, details in cart.items():
        item_total = details["price"] * details["quantity"]
        total += item_total
        summary += f'{item_name} x {details["quantity"]} = ₹{item_total}\n'
    summary += f'\nTotal: ₹{total}\n\nThank you for shopping!'
    messagebox.showinfo("Checkout", summary)
    cart.clear()

window = Tk()
window.geometry("700x550")
window.title("Online Ordering")
window.config(background="#abd6cf")

categories = Menu(window)
window.config(menu=categories)

Categories = Menu(categories, tearoff=0)
categories.add_cascade(label="Categories", menu=Categories)
Categories.add_command(label="Stationery", command=lambda: show_category_items("Stationery"))
Categories.add_command(label="Clothing", command=lambda: show_category_items("Clothing"))
Categories.add_command(label="Electronics", command=lambda: show_category_items("Electronics"))
Categories.add_command(label="Accessories", command=lambda: show_category_items("Accessories"))
Categories.add_command(label="Grocery", command=lambda: show_category_items("Grocery"))

label = Label(window,
              text="MAIN MENU",
              font=('Arial', 25, 'bold'),
              fg="#000d0b", bg="#3d7a70",
              relief="ridge", bd=10,
              padx=10, pady=10)
label.pack(side="top", fill="x")

items_frame = Frame(window, bg="#abd6cf")
items_frame.pack(fill="both", expand=True)

# Checkout button at the bottom
checkout_btn = Button(window, text="Checkout", font=("Arial", 16, "bold"), bg="#3d7a70", fg="white", command=checkout)
checkout_btn.pack(pady=10)

show_category_items("Stationery")

window.mainloop()


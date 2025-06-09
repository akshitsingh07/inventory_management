# Inventory Management 🛒

A Python-based inventory management system for tracking products, suppliers, and sales. Features a Tkinter-powered GUI and persists data using SQLite.

---

## 🚀 Features

- **Product Management**: Add, edit, delete products with name, quantity, price, etc.
- **Supplier & Category Management**: Manage associated suppliers and product categories.
- **Sales & Billing Module**: Record sales, generate bills, and update inventory automatically.
- **Dashboard**: Navigate between modules and view basic stats.
- **SQLite Backend**: Lightweight, file-based database via `sqlite3`.

---

## 🧰 Prerequisites

- Python 3.7+
- Required Python libraries:
  ```bash
  pip install tkinter sqlite3 pandas
  ```
- Optional: Pillow for handling images in GUI (if applicable).

---

## 📥 Installation & Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/akshitsingh07/inventory_management.git
    cd inventory_management
    ```

2. (Optional) Create virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate   # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```bash
    python create_db.py
    ```

---

## ▶️ Running the Application

Launch the main application:
```bash
python dashboard.py
```

---

## 🗂️ Code Structure

| File              | Description                                             |
|-------------------|---------------------------------------------------------|
| `create_db.py`    | Initializes SQLite database schema                      |
| `dashboard.py`    | Main GUI dashboard for navigation                       |
| `product.py`      | Product CRUD operations                                |
| `supplier.py`     | Supplier CRUD operations                               |
| `category.py`     | Category CRUD operations                               |
| `sales.py`        | Manage and view sales records                          |
| `billing.py`      | Billing operations with invoice generation             |

---

## ✅ Usage Workflow

1. Run `create_db.py` to prepare the database.
2. Launch `dashboard.py` which will open the GUI window.
3. Use navigation buttons to access different modules:
   - Add/edit/delete products, suppliers, categories
   - Create invoices via billing module (automatically updates inventory)
   - View past sales and stock levels

---

## 🛠️ Configuration

- **Database file**: `inventory.db` (default SQLite name)
- **GUI images/invoices**: Create `images/` and `bills/` folders if used by the app.
- **Default Settings**: Modify file paths or defaults directly in corresponding modules.

---

## 💡 Future Enhancements

- Add user authentication (e.g. admin vs staff roles)
- Export reports to CSV/PDF or integrate with Excel
- Incorporate barcode scanning and low-stock alerts
- Transition to client-server model with Flask or Django web interface

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Improve GUI layout and UX
- Add new features (e.g. reporting, analytics)
- Write tests and improve error handling

Open an issue or submit a pull request—happy to collaborate!

---

## 📄 License

Specify your license here (e.g., MIT, Apache 2.0).

---

### 📚 References

Based on common inventory app templates and inspired by similar open-source Python projects.

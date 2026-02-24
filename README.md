

# Smart Library System

A robust, "Pythonic" library management system designed to demonstrate advanced Python concepts including Object-Oriented Programming, Magic Methods (Dunder methods), Decorators, Closures, and Package Structure.

## 📂 Project Structure

```text
library_system/
├── __init__.py      # Package initialization & exposure
├── core.py          # Core OOP logic (Book & Library classes)
├── utils.py         # Advanced logic (Decorators, Closures, Duck Typing)
└── __main__.py      # Entry point for the demonstration

```

## 🚀 How to Run

1. **Clone the repository** (or navigate to the project folder):
```bash
cd /path/to/project_root

```


2. **Run the package as a module**:
*Important: You must run this from the parent directory, not inside the `library_system` folder.*
```bash
python3 -m library_system

```



## 🧠 Technical Analysis

### 1. Method Resolution Order (MRO) Analysis

*Requirement: Analyze the MRO for a hypothetical `DigitalBook` class inheriting from `Book` and `Software`.*

If we define a class structure as follows:

```python
class Software:
    pass

class DigitalBook(Book, Software):
    pass

```

Python uses the **C3 Linearization Algorithm** to determine the order in which methods are resolved.

**The Algorithm Steps:**

1. **Linearization of DigitalBook:** `L(DigitalBook) = [DigitalBook] + merge(L(Book), L(Software), [Book, Software])`
2. **Parents:**
* `L(Book) = [Book, object]`
* `L(Software) = [Software, object]`


3. **Merge Process:**
* Python looks at the head of the first list (`Book`). It is not in the tail of any other list. -> **Select `Book**`.
* Remaining Merge: `merge([object], [Software, object], [Software])`
* Next, `Software` is the head of its list and not in any tail. -> **Select `Software**`.
* Remaining Merge: `merge([object], [object])` -> **Select `object**`.



**Final MRO Result:**
`DigitalBook` ➝ `Book` ➝ `Software` ➝ `object`

**Implication:**
If both `Book` and `Software` have a method with the same name (e.g., `deploy()`), Python will execute the version in **`Book`** first because it appears earlier in the MRO list.

### 2. The "Duck Test" (Duck Typing)

The system implements Python's "Duck Typing" philosophy ("If it looks like a duck and quacks like a duck, it's a duck").

The `borrow_item(item)` function in `utils.py` does **not** check if the object is an instance of the `Book` class. Instead, it follows the **EAFP** (Easier to Ask for Forgiveness than Permission) principle:

```python
def borrow_item(item):
    try:
        print(f"Processing '{item.title}'...")
    except AttributeError:
        print("Error: Object is not borrowable...")

```

This allows the function to accept **any** object (e.g., a `Magazine`, a `DVD`, or a `Download`) as long as it possesses a `.title` attribute.

## ✨ Features

* **Magic Methods:** Implements `__str__`, `__len__`, `__eq__`, and `__getitem__` for intuitive object interaction.
* **Decorators:** `@track_access` logs function calls with timestamps.
* **Closures:** `permission_check` enforces Role-Based Access Control (RBAC).
* **PEP 8 Compliance:** Code follows standard Python style guidelines.

```

```
# Create our Checklist
checklist = list()

# Define Functions
def create(item):
    """Add item to the checklist."""
    checklist.append(item)

def read(index):
    """Read item from the checklist."""
    if 0 <= index < len(checklist):
        print(checklist[index])
        return checklist[index]
    else:
        print("Error: Index out of range.")
        return None


def update(index, item):
    """Update item in the checklist."""
    if 0 <= index < len(checklist):
        checklist[index] = item
    else:
        print("Error: Index out of range.")

def destroy(index):
    """Remove item from the checklist."""
    if 0 <= index < len(checklist):
        checklist.pop(index)
    else:
        print("Error: Index out of range.")

def list_all_items():
    """Print all items in the checklist."""
    if not checklist:
        print("List is empty.")
    else:
        for index, item in enumerate(checklist):
            print(f"{index}: {item}")

def mark_completed(index):
    """Mark an item as completed."""
    if 0 <= index < len(checklist):
        checklist[index] = f"✔ {checklist[index]}"
    else:
        print("Error: Index out of range.")

def user_input(prompt):
    """Get user input."""
    return input(prompt)

def select(function_code):
    """Execute function based on the user's selection."""
    function_code = function_code.upper()

    if function_code == "C":
        item = user_input("Input item: ")
        create(item)
    elif function_code == "R":
        index = int(user_input("Index Number? "))
        read(index)
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")
    return True

def test():
    """Test functions."""
    create("Apples")
    create("Bananas")
    assert read(0) == "Apples"
    assert read(1) == "Bananas"

    update(0, "Grapes")
    assert read(0) == "Grapes"

    destroy(1)
    assert len(checklist) == 1

    mark_completed(0)
    assert checklist[0] == "✔ Grapes"

    print("All tests passed.")

# Run Tests
test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit: ")
    running = select(selection)

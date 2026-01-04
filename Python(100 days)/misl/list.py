import time

# 1. The "Database" (Just a simple empty list)
# This is where we store the data in memory.
my_checklist = []

def show_menu():
    print("\n" + "="*30)
    print(" 📝  MASTER CHECKLIST v1.0")
    print("="*30)
    print("1. [View] Show all items")
    print("2. [Add] Add new item")
    print("3. [Remove] Check off an item")
    print("4. [Exit] Close App")
    print("-" * 30)

# 2. The "Game Loop" (Keeps the app running forever until we quit)
while True:
    show_menu()
    choice = input("👉 Select an option (1-4): ")

    # OPTION 1: VIEW ITEMS
    if choice == '1':
        print("\n📂 CURRENT LIST:")
        if len(my_checklist) == 0:
            print("   (The list is empty! Add something first.)")
        else:
            # 'enumerate' gives us both the index (0,1,2) and the item
            for index, item in enumerate(my_checklist):
                print(f"   [{index + 1}] {item}")

    # OPTION 2: ADD ITEMS
    elif choice == '2':
        new_item = input("\n✍️  What do you want to add?: ")
        my_checklist.append(new_item)  # .append adds to the end
        print(f"✅ Added: '{new_item}'")
        time.sleep(0.5)

    # OPTION 3: REMOVE ITEMS
    elif choice == '3':
        print("\n🗑️  WHICH ITEM TO REMOVE?")
        # Show the list again so they know the numbers
        for index, item in enumerate(my_checklist):
            print(f"   [{index + 1}] {item}")
        
        try:
            item_number = int(input("Enter number to remove: "))
            # We subtract 1 because computers start counting at 0, humans start at 1
            removed_item = my_checklist.pop(item_number - 1) 
            print(f"❌ Removed: '{removed_item}'")
        except:
            print("⚠️  Error: Invalid number!")

    # OPTION 4: EXIT
    elif choice == '4':
        print("👋 Saving (not really)... Goodbye!")
        break

    else:
        print("🛑 Invalid choice, try again.")
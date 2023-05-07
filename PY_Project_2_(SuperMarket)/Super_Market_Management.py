# -----------------SUPERMARKET MANAGEMENT SYSTEM--------------------
items = []
while True:

    display = input("Press [ ENTER ] to continue.")

    print("------------------Welcome to the supermarket------------------")

    print("""
            1. Add items for sale \n
            2. View items \n 
            3. Purchase items \n 
            4. Search items \n 
            5. Edit items \n 
            6. Exit
            """)

    choice = input("Enter the number of your choice : ")

    if choice == "1":
        print("------------------Add items------------------")

        print("To Add an item fill in the form")

        item = {}

        item["name"] = input("Item Name : ")
        while True:
            try:
                item["quantity"] = int(input("Item Quantity : "))
                break
            except ValueError:
                print("Quantity should only be in digits")
        while True:
            try:
                item["price"] = int(input("Price ₹ : "))
                break
            except ValueError:
                print("Price should only be in digits")

        print("Item has been successfully added.")
        items.append(item)

    elif choice == "2":
        print("------------------View Items------------------")

        print("The number of items in the inventory are : ", len(items))

        while len(items) != 0:
            print("Here are all the items available in the supermarket.")

            for item in items:
                for key, value in item.items():
                    print(key, ":", value)
            break

    elif choice == "3":
        print("------------------purchase items------------------")

        print(items)

        purchase_item = input("which item do you want to purchase? Enter name : ")
        for item in items:
            if purchase_item.lower() == item["name"].lower():
                if item["quantity"] != 0:
                    print("Pay ", item["price"], "at checkout counter.")
                    item["quantity"] -= 1
                else:
                    print("item out of stock.")

    elif choice == "4":
        print("------------------search items------------------")

        find_item = input("Enter the item \"s name to search in inventory : ")
        for item in items:
            if item["name"].lower() == find_item.lower():
                print("The item named " + find_item +" is displayed below with its details")
                print(item)

    elif choice == "5":
        print("------------------edit items------------------")
        item_name = input(
            "Enter the name of the item that you want to edit : ")

        for item in items:
            if item_name.lower() == item["name"].lower():
                print("Here are the current details of " + item_name)
                print(item)
                item["name"] = input("Change Item name : ")
                while True:
                    try:
                        item["quantity"] = int(
                            input("Change Item quantity : "))
                        break
                    except ValueError:
                        print("Quantity should only be in digits")
                while True:
                    try:
                        item["price"] = int(input("Change Price $ : "))
                        break
                    except ValueError:
                        print("Price should only be in digits")

                print("Item has been successfully updated.")

                print(item)
            else:
                print("Item not found")

    elif choice == "6":
        print("------------------exited------------------")
        break

    else:
        print("You entered an invalid option")
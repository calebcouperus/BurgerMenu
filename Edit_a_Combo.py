import easygui

combos = {
    'value': {'beef burger': '5.69', 'fries': '1.00', 'fizzy drink': '1.00'},
    'cheezy': {'cheeseburger': '6.69', 'fries': '1.00', 'fizzy drink': '1.00'},
    'super': {'cheeseburger': '6.69', 'large fries': '2.00', 'smoothie': '2.00'}
}


def search_combo(search_name):
    for combo_name, combo_info in combos.items():
        if search_name.lower() in combo_name.lower():
            return combo_name, combo_info
    return None, None


def edit_combo():
    search_term = easygui.enterbox(
        "Enter the name of the combo you want to edit:", title='Enter Search')
    combo_name, combo_info = search_combo(search_term)
    if combo_info:
        new_combo_info = combo_info.copy()
        easygui.msgbox(
            f"Editing Combo: {combo_name}\nCurrent Items and Prices:\n"
            f"{combo_info}",
            title='Edit Combo')

        while True:
            action = easygui.choicebox("Select an action:", "Edit Combo",
                                       ["Add Item", "Remove Item",
                                        "Change Price", "Finish Editing"])

            if action == "Add Item":
                new_item_name = easygui.enterbox(
                    "Enter the name of the new item:")
                new_item_price = easygui.enterbox(
                    f"Enter the price for {new_item_name}:")
                new_combo_info[new_item_name] = new_item_price
                easygui.msgbox(f"Added {new_item_name} to the combo.",
                               title='Edit Successful')

            elif action == "Remove Item":
                item_to_remove = easygui.choicebox("Select an item to remove:",
                                                   "Remove Item",
                                                   list(new_combo_info.keys()))
                del new_combo_info[item_to_remove]
                easygui.msgbox(f"Removed {item_to_remove} from the combo.",
                               title='Edit Successful')

            elif action == "Change Price":
                item_to_change = easygui.choicebox(
                    "Select an item to change the price:", "Change Price",
                    list(new_combo_info.keys()))
                new_price = easygui.enterbox(
                    f"Enter the new price for {item_to_change} (current price: "
                    f"{new_combo_info[item_to_change]}):")
                new_combo_info[item_to_change] = new_price
                easygui.msgbox(
                    f"Changed the price of {item_to_change} to {new_price}.",
                    title='Edit Successful')

            elif action == "Finish Editing":
                combos[combo_name] = new_combo_info
                easygui.msgbox(
                    f"Combo '{combo_name}' has been updated with the following "
                    f"items and prices:\n{new_combo_info}",
                    title='Edit Successful')
                break

    else:
        easygui.msgbox("The combo is not in the menu.", title='Error Message')


def search():
    search_term = easygui.enterbox(
        "Enter the name of the combo or item you want to search for:",
        title='Enter Search')
    result = search_combo(search_term)
    if result[1]:
        if len(result[1]) == 1:  # Single item found
            item_name, item_price = list(result[1].items())[0]
            easygui.msgbox(f"{item_name}: ${item_price}", title='Search Result')
        else:  # Combo found
            contact_details = f"Combo Details for {result[0]}:\n"
            for key, value in result[1].items():
                contact_details += f"{key}: {value}\n"
            easygui.msgbox(contact_details, title='Search Result')
    else:
        easygui.msgbox("The combo or item is not in the menu.",
                       title='Error Message')


edit_combo()

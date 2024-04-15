import easygui

combos = {'value': {'beef burger': '5.69', 'fries': '1.00', 'fizzy drink':
          '1.00'},
          'cheesy': {'cheeseburger': '6.69', 'fries': '1.00', 'fizzy '
                                                              'drink':
                                                              '1.00'},
          'super': {'cheeseburger': '6.69', 'large fries': '2.00',
                    'smoothie': '2.00'}}


def add_combo():
    combo_name = easygui.enterbox("Enter the combo name:", title='Enter Combo '
                                                                 'Name')
    burger = easygui.enterbox(
        "Enter the burger in the combo:",
        title='Enter Burger')
    burger_price = easygui.enterbox(
        "Enter the price of the burger in the combo:",
        title='Enter Burger Price')
    drink = easygui.enterbox("Enter the drink in the new combo:",
                             title='Enter Drink')
    drink_price = easygui.enterbox("Enter the price of the drink in the new "
                                   "combo:",
                                   title='Enter Drink Price')
    side = easygui.enterbox("Enter the side you want to add to the combo:",
                            title='Enter Side')
    side_price = easygui.enterbox("Enter the price of the new side:",
                                  title='Enter Side Price')
    new_combo = {
        burger: burger_price,
        drink: drink_price,
        side: side_price,
    }
    combos[f"{combo_name}"] = new_combo


def search_combo(search_name):
    for combo_name, combo_info in combos.items():
        if search_name.lower() in combo_name.lower():
            return combo_info
        for item_name, item_price in combo_info.items():
            if search_name.lower() in item_name.lower():
                return {item_name: item_price}
    return None


def search():
    search_term = easygui.enterbox("Enter the name of the combo or item you "
                                   "want to search for:", title='Enter Search')
    result = search_combo(search_term)
    if result:
        if len(result) == 1:  # Single item found
            item_name, item_price = list(result.items())[0]
            easygui.msgbox(f"{item_name}: ${item_price}", title='Search Result')
        else:  # Combo found
            combo_name = list(result.keys())[0]
            contact_details = f"Combo Details for {combo_name}:\n"
            for key, value in result.items():
                contact_details += f"{key}: {value}\n"
            easygui.msgbox(contact_details, title='Search Result')
    else:
        easygui.msgbox("The combo or item is not in the menu.", title='Error '
                                                                      'Message')


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


def delete_combo():
    search_term = easygui.enterbox("Enter the name of the combo you want to "
                                   "delete:", title='Enter Search')
    combo_name, _ = search_combo(search_term)
    if combo_name:
        confirm = easygui.boolbox(f"Are you sure you want to delete the combo '"
                                  f"{combo_name}'?", title='Confirmation',
                                  choices=("Yes", "No"))
        if confirm:
            del combos[combo_name]
            easygui.msgbox(f"Combo '{combo_name}' has been deleted.",
                           title='Deletion Successful')
        else:
            easygui.msgbox("Deletion canceled.", title='Cancellation')
    else:
        easygui.msgbox("The combo is not in the menu.", title='Error Message')


def list_combos():
    combo_details = "List of Combos:\n\n"
    for combo_name, combo_info in combos.items():
        combo_details += f"Combo: {combo_name}\n"
        for item, price in combo_info.items():
            combo_details += f" - {item}: ${price}\n"
        combo_details += "\n"

    easygui.msgbox(combo_details, title='Combo List')


def main_menu():
    while True:
        user_choice = easygui.choicebox("Select an action:", "Burger Menu",
                                        ["Add Combo", "Search", "Edit Combo",
                                         "Delete Combo", "Output All Combos",
                                         "Exit"])

        if user_choice == "Add Combo":
            add_combo()
        elif user_choice == "Search":
            search()
        elif user_choice == "Edit Combo":
            edit_combo()
        elif user_choice == "Delete Combo":
            delete_combo()
        elif user_choice == "Output All Combos":
            list_combos()
        elif user_choice == "Exit":
            break


if __name__ == "__main__":
    main_menu()

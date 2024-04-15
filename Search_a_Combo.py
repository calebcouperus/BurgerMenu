import easygui

combos = {
    'value': {'beef burger': '5.69', 'fries': '1.00', 'fizzy drink': '1.00'},
    'cheezy': {'cheeseburger': '6.69', 'fries': '1.00', 'fizzy drink': '1.00'},
    'super': {'cheeseburger': '6.69', 'large fries': '2.00', 'smoothie': '2.00'}
}


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


search()

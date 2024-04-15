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


delete_combo()

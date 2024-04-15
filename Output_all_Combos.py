import easygui

combos = {
    'value': {'beef burger': '5.69', 'fries': '1.00', 'fizzy drink': '1.00'},
    'cheezy': {'cheeseburger': '6.69', 'fries': '1.00', 'fizzy drink': '1.00'},
    'super': {'cheeseburger': '6.69', 'large fries': '2.00', 'smoothie': '2.00'}
}


def list_combos():
    combo_details = "List of Combos:\n\n"
    for combo_name, combo_info in combos.items():
        combo_details += f"Combo: {combo_name}\n"
        for item, price in combo_info.items():
            combo_details += f" - {item}: ${price}\n"
        combo_details += "\n"

    easygui.msgbox(combo_details, title='Combo List')


list_combos()

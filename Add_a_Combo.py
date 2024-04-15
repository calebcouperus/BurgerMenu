import easygui

combos = {'value': {'beef burger': '5.69', 'fries': '1.00', 'fizzy drink':
    '1.00'},
          'cheezy': {'cheeseburger': '6.69', 'fries': '1.00', 'fizzy '
                                                              'drink':
              '1.00'},
          'super': {'cheeseburger': '6.69', 'large fries': '2.00',
                    'smoothie': '2.00'}}


def add():
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


add()
print(combos)

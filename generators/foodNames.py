__all__ = ['foodNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                if (var.get('i')<Js(2.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('names', ((((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names3').get(var.get('rnd3'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                        var.put('names', ((((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names4').get(var.get('rnd3'))))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                        var.put('names', ((((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names5').get(var.get('rnd3'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                if (var.get('i')<Js(8.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    while PyJsStrictEq(var.get('rnd3'),var.get('rnd')):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('names', ((((var.get('names6').get(var.get('rnd'))+Js(' and '))+var.get('names6').get(var.get('rnd3')))+Js(' '))+var.get('names7').get(var.get('rnd2'))))
                else:
                    var.put('names', ((var.get('names6').get(var.get('rnd'))+Js(' '))+var.get('names7').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Baked'), Js('Barbecued'), Js('Basted'), Js('Blanched'), Js('Braised'), Js('Breaded'), Js('Brined'), Js('Broasted'), Js('Cooked'), Js('Cured'), Js('Deep-Fried'), Js('Dried'), Js('Dry-Roasted'), Js('Engine-Cooked'), Js('Fire-Grilled'), Js('Fire-Roasted'), Js('Fried'), Js('Gentle-Fried'), Js('Grilled'), Js('Infused'), Js('Marinated'), Js('Oven-Baked'), Js('Oven-Grilled'), Js('Pan-Fried'), Js('Pickled'), Js('Poached'), Js('Pressure-Cooked'), Js('Pressure-Fried'), Js('Roasted'), Js('Sautéed'), Js('Seared'), Js('Shallow-Fried'), Js('Simmered'), Js('Slow-Cooked'), Js('Smoked'), Js('Steamed'), Js('Stewed'), Js('Stir-Fried'), Js('Stuffed'), Js('Tea-Smoked'), Js('Tenderized'), Js('Thermal-Cooked')]))
var.put('names2', Js([Js('Almonds & Avocado'), Js('Apple & Lavender'), Js('Apples & Mustard'), Js('Apples & Walnut'), Js('Apricot & Basil'), Js('Apricots & Honey'), Js('Asparagus'), Js('Basil & Cinnamon'), Js('Basil & Clove'), Js('Basil & Lime'), Js('Basil & Mint'), Js('Beets & Lemon'), Js('Beets & Orange'), Js('Bittersweet'), Js('Black Pepper'), Js('Blackberry & Ginger'), Js('Blueberry'), Js('Blueberry & Mushroom'), Js('Butter'), Js('Carrot & Coriander'), Js('Carrot & Violet'), Js('Potatoes &'), Js('Rice &'), Js('Pasta & '), Js('Carrots & Ginger'), Js('Casserole of'), Js('Cheese &'), Js('Chestnuts &'), Js('Chili'), Js('Cinnamon'), Js('Cinnamon & Thyme'), Js('Cocoa & Mushroom'), Js('Coconut'), Js('Coconut & Ginger'), Js('Confit of'), Js('Coriander & Lemon'), Js('Cranberry'), Js('Creamy'), Js('Cucumber &'), Js('Cucumber & Lime'), Js('Curry of'), Js('Dark Ale'), Js('Dark Beer'), Js('Easter-Style'), Js('Egg & Beans'), Js('Egg & Beet'), Js('Egg & Coconut'), Js('Fennel'), Js('Fennel & Garlic'), Js('Fennel & Lemon'), Js('Fennel & Lime'), Js('Fennel & Orange'), Js('Figs & Olive'), Js('Forest'), Js('Garlic'), Js('Garlic & Ginger'), Js('Garlic & Lime'), Js('Garlic & Onion'), Js('Garlic & Rosemary'), Js('Garlic & Tomato'), Js('Ginger'), Js('Ginger & Honey'), Js('Hazelnut'), Js('Herbs &'), Js('Honey'), Js('Honey & Almond'), Js('Honey & Nuts'), Js('Honey & Thyme'), Js('Honey-Coated'), Js('Hot & Spicy'), Js('Hot & Sweet'), Js('Jasmine'), Js('Juniper'), Js('Lemon'), Js('Lemongrass'), Js('Light Ale'), Js('Light Beer'), Js('Lime'), Js('Lime & Ginger'), Js('Lime-Coated'), Js('Mango & Pine'), Js('Mint'), Js('Mint & Berry'), Js('Mint & Mustard'), Js('Mint & Orange'), Js('Mountain'), Js('Mushroom'), Js('Mushroom & Apricot'), Js('Mushroom & Garlic'), Js('Mushroom & Rosemary'), Js('Mustard'), Js('Mustard & Garlic'), Js('Mustard & Rosemary'), Js('Mustard & Thyme'), Js('Northern-Style'), Js('Nuts &'), Js('Olive'), Js('Olives & Mustard'), Js('Onions & Cream'), Js('Onions & Tomato'), Js('Orange'), Js('Orange & Mustard'), Js('Orange & Olive'), Js('Oregano'), Js('Paprika'), Js('Parmesan'), Js('Parsnip & Pear'), Js('Peach & Vinegar'), Js('Peanuts &'), Js('Peas & Mushroom'), Js('Pepper'), Js('Pepper & Garlic'), Js('Pepper & Lime'), Js('Pepper & Mango'), Js('Peppermint'), Js('Pine'), Js('Pineapple'), Js('Raspberry & Peanut'), Js('Red Whine'), Js('Rhubarb'), Js('Rosemary'), Js('Rosemary & Onion'), Js('Saffron'), Js('Saffron & Shallot'), Js('Salt & Pepper'), Js('Salt & Savory'), Js('Salted'), Js('Salty & Sour'), Js('Savory'), Js('Sour'), Js('Sour & Cream'), Js('Souther-Style'), Js('Soy'), Js('Stew of'), Js('Sugar'), Js('Sweet & Fresh'), Js('Sweet & Savory'), Js('Sweet & Spicy'), Js("Sweet 'n Sour"), Js('Thyme & Parsley'), Js('Tomatoes &'), Js('Truffles &'), Js('Vanilla'), Js('Vanilla & Mint'), Js('Vegetables &'), Js('Vinegar'), Js('Walnuts &'), Js('Wasabi'), Js('Watercress'), Js('Western-Style'), Js('White Wine'), Js('Yogurt')]))
var.put('names3', Js([Js('Bear'), Js('Beef'), Js('Boar'), Js('Chicken'), Js('Duck'), Js('Horse'), Js('Lamb'), Js('Mammoth'), Js('Mutton'), Js('Ostrich'), Js('Pheasant'), Js('Pigeon'), Js('Pork'), Js('Quail'), Js('Rabbit'), Js('Turkey'), Js('Venison'), Js('Yak')]))
var.put('names4', Js([Js('Clams'), Js('Cockles'), Js('Cod'), Js('Crab'), Js('Crocodile'), Js('Alligator'), Js('Fish'), Js('Frog'), Js('Herring'), Js('Lobster'), Js('Mussels'), Js('Oysters'), Js('Prawns'), Js('Salmon'), Js('Scallops'), Js('Shrimps'), Js('Snapper'), Js('Trout'), Js('Tuna')]))
var.put('names5', Js([Js('Bake'), Js('Bread'), Js('Bruschetta'), Js('Buns'), Js('Calzone'), Js('Chestnuts'), Js('Chutney'), Js('Flatbread'), Js('Forest Mushrooms'), Js('Gratin'), Js('Kebabs'), Js('Lasagna'), Js('Linguine'), Js('Moussaka'), Js('Minestrone'), Js('Stracciatella'), Js('Goulash'), Js('Bisque'), Js('Nut Mix'), Js('Omelet'), Js('Pasta'), Js('Pie'), Js('Pizza'), Js('Potato Wedges'), Js('Potatoes'), Js('Rice'), Js('Risotto'), Js('Roll'), Js('Salad'), Js('Sandwich'), Js('Scrambled Egg'), Js('Soup'), Js('Spring Greens'), Js('Spring Vegetables'), Js('Stuffed Bread'), Js('Taco'), Js('Tart'), Js('Tofu'), Js('Tortilla'), Js('Vegetable Mix'), Js('Vegetables'), Js('Walnuts'), Js('Winter Greens'), Js('Winter Vegetables')]))
var.put('names6', Js([Js('Almond'), Js('Apple'), Js('Avocado'), Js('Banana'), Js('Blueberry'), Js('Caramel'), Js('Cardamom'), Js('Cashew'), Js('Cherry'), Js('Chestnut'), Js('Chocolate'), Js('Cinnamon'), Js('Cocoa'), Js('Coconut'), Js('Coffee'), Js('Cranberry'), Js('Dark Chocolate'), Js('Date'), Js('Elderberry'), Js('Ginger'), Js('Gooseberry'), Js('Grape'), Js('Grapefruit'), Js('Guava'), Js('Hazelnut'), Js('Honey'), Js('Kiwi'), Js('Lemon'), Js('Licorice'), Js('Lime'), Js('Mandarin'), Js('Mango'), Js('Melon'), Js('Milk Chocolate'), Js('Mint'), Js('Nutmeg'), Js('Orange'), Js('Papaya'), Js('Passion Fruit'), Js('Peach'), Js('Peanut'), Js('Pecan'), Js('Pineapple'), Js('Pistachio'), Js('Plum'), Js('Praline'), Js('Raspberry'), Js('Red Wine'), Js('Rum'), Js('Saffron'), Js('Strawberry'), Js('Vanilla'), Js('Walnut'), Js('White Chocolate'), Js('White Wine')]))
var.put('names7', Js([Js('Bombe'), Js('Bonbons'), Js('Bread'), Js('Buns'), Js('Cake'), Js('Candy'), Js('Cheesecake'), Js('Cobbler'), Js('Cone'), Js('Cookies'), Js('Crispies'), Js('Crumble'), Js('Custard'), Js('Delight'), Js('Doughnut'), Js('Fruit Salad'), Js('Fruitcake'), Js('Fudge'), Js('Genoise'), Js('Gingerbread'), Js('Ice Cream'), Js('Ice Lollies'), Js('Jam'), Js('Jelly'), Js('Milk'), Js('Molten Cake'), Js('Mooncake'), Js('Pancakes'), Js('Pastry'), Js('Pavlova'), Js('Pie'), Js('Pound Cake'), Js('Pud'), Js('Pudding'), Js('Roll'), Js('Snacks'), Js('Sorbet'), Js('Soufflé'), Js('Split'), Js('Steamed Pudding'), Js('Strudel'), Js('Sundae'), Js('Surprise'), Js('Tart'), Js('Tarte Tatin'), Js('Toast'), Js('Toffee'), Js('Trifle'), Js('Wafer'), Js('Waffles'), Js('Whip'), Js('Yogurt')]))
pass
pass


# Add lib to the module scope
foodNames = var.to_python()
__all__ = ['pizzeriaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('The All Around'), Js("The Bake 'n Take"), Js('The Balance of Flour'), Js("The Basil 'n Peel"), Js('The Belle Pepper'), Js('The Bits and Pizzas'), Js('The Black Olive'), Js('Chateau Dough'), Js('The Cheese Base'), Js('The Cheese Connection'), Js('Cheese Louise'), Js('The Cheese Piece'), Js('Cheese and Kisses'), Js('Cheesus'), Js('Cheesus Crust'), Js('The Clay Oven'), Js('The Commandough'), Js('The Conversation Pizza'), Js('The Corner Grill'), Js('Cravings'), Js('Crazy Dough'), Js('The Crispy Crust'), Js('Crust Lust'), Js('Cut the Cheese'), Js('The Deep Dish'), Js('The Dough Bro'), Js('Dough Business'), Js('The Dough Must Go On'), Js('Dough Nuts'), Js('Dough Oh'), Js('Dough Re Mi'), Js('Dough of Hands'), Js('The Doughbie Brothers'), Js('The Doughfather'), Js('The Doughfellas'), Js('Doughy Delights'), Js('Feeling Saucy'), Js("The Flippin'"), Js('Flour Girl'), Js('Flour Power'), Js('Flour Up'), Js('Flour to You'), Js("For Pizza's Sake"), Js('From Top to Dough'), Js('From Topping to Dough'), Js('The Full Moon'), Js('The Funky Anchovy'), Js('Get to the Toppings'), Js('The Gluteus Maximus'), Js('The Gluteus Minimus'), Js('The Happy Flour'), Js('The Home Slice'), Js('The Hot Oven'), Js('The Hot Spot'), Js('The Hot Stone'), Js('Il Tricolore'), Js('In One Pizza'), Js('Knead Pizza'), Js('Knead to Know'), Js('Luscious Layers'), Js('The Lust for Crust'), Js('Master Pieces'), Js('The Meadough'), Js('Molten Delights'), Js('Napoli'), Js('Oh Cheese'), Js('The Olive'), Js('The Olive Branch'), Js('On Toppings'), Js('Onomotopizza'), Js('Oven Baked'), Js('The Oven and Shaker'), Js('Over the Toppings'), Js('Papa Pizza'), Js("Pepperoni's"), Js('Pi Pie'), Js('Pieology'), Js('The Pizza Bro'), Js('Pizza Cake'), Js('The Pizza Connection'), Js('Pizza Me'), Js('Pizza Mind'), Js('Pizza My Heart'), Js('Pizza Pals'), Js('Pizza Pan'), Js('Pizza Paradise'), Js('Pizza Squared'), Js('Pizza Together'), Js('Pizza Work'), Js('The Pizza de Resistance'), Js('Pizza di Mama'), Js('Pizza the Action'), Js('The Pizzageddon'), Js('The Pizzasmith'), Js('Pizzazz'), Js('Pizzazza'), Js('The Pizzone'), Js('The Prime'), Js('The Prime Dough'), Js("Rest 'n Pizza"), Js('Rise to the Toppings'), Js('Rolling in Dough'), Js('The Round Table'), Js('Rounded Down'), Js('The Sassy Sauce'), Js('Say Cheese'), Js('Slice of Heaven'), Js('Slice of Italy'), Js('Slice of Life'), Js('The Stone Hot'), Js('Stuffed'), Js('Sweet Sensations'), Js('That Cheese Dough'), Js("That's Amore"), Js('The Tomato Base'), Js('The Tomato Pie'), Js('The Top Slice'), Js('The Topspin'), Js('The Tri-Slice'), Js('The Upper Crust'), Js('We Knead'), Js('The Pizzazy'), Js('The Pizzander'), Js('The Pizzaffar'), Js('The Pizzamarra'), Js('The Pizzaga'), Js('The Pizza Saga'), Js("Pizz'ahoy"), Js('The Pizzamba'), Js('The Pizzanity'), Js('The Pizzavant'), Js('The Scampizza'), Js('The Octopizza'), Js('The Papizza'), Js('The Tipizza')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+Js(' Pizzeria')))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
pizzeriaNames = var.to_python()
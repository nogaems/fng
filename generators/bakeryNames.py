__all__ = ['bakeryNames']

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
    var.put('nm1', Js([Js('Ahead of Bread'), Js('Awake & Bake'), Js('Babycakes'), Js('Bake Awake'), Js('Baked'), Js('Baked Bites'), Js('Bakers Delight'), Js('Balance of Flour'), Js('Batter Spatter'), Js('Best Thing Since Sliced Bread'), Js('Blends of Flour'), Js('Blissful Bites'), Js('Born and Bread'), Js('Bottom of the Flour'), Js('Bread & Butter'), Js('Bread Ahead'), Js('Bread and Batter'), Js('Bread and Custards'), Js('Bread and Peanut Butter'), Js('Breadline'), Js('Breadsmith'), Js('Break Bread'), Js('Budding Tastes'), Js('Bun Boutique'), Js('Buns in the Oven'), Js('Buns of Steel'), Js('Cake Bakes'), Js('Cake Break'), Js('Cake Couture'), Js('Cake Outbreak'), Js('Cake Zone'), Js('Cake a Diem'), Js("Cake's Sake"), Js("Cake's at Stake"), Js('Cake-A-Licious'), Js('Cakes and Ale'), Js('Cakewalk'), Js('Cakewalkers'), Js('Cakey Bakey'), Js('Chateau Dough'), Js('Cocoa Nutter'), Js("Coffee Break 'n Cake"), Js('Commandough'), Js('Common Scents'), Js('Cookie-Clutter'), Js('Cookie-Cutter'), Js('Cookoo for Cookies'), Js('Creamy Creations'), Js('Creative Treats'), Js('Crumbs'), Js('Crumbs and Bites'), Js('Crunchy Crumbles'), Js('Cups and Cakes'), Js('Cut the Cake'), Js('Dough Business'), Js('Dough Re Mi'), Js('Dough must go on'), Js('Dough of Hands'), Js('Doughing Pains'), Js('Doughy Delights'), Js('Dripping Drizzles'), Js('Emergency Cake'), Js('Finest Flour'), Js('Flour Down'), Js('Flour Girl'), Js('Flour Leaves'), Js('Flour Meadough'), Js('Flour Play'), Js('Flour Power'), Js('Flour Up'), Js('Flours for Hours'), Js("Fondante's Inferno"), Js('For Flours on End'), Js('For Goodness Cakes'), Js('Fresh from the Oven'), Js('Ginger Snapped'), Js('Give and Cake'), Js('Glazed and Glorious'), Js('Gluteus Maximus'), Js('Gluteus Minimus'), Js('Glutton for Punishment'), Js('Grains of Scents'), Js('Great Buns'), Js('Happy Flour'), Js('Have Your Cake & Eat It'), Js('Hearts and Flours'), Js('Hot Buns'), Js('Hour of the Bread'), Js('Icing on the Cake'), Js('Irresistible Indulgence'), Js('Ivory Flour'), Js('Knead Bread?'), Js('Knead for Sweets'), Js('Knead to Know'), Js('Let Them Eat Cake'), Js('Loaf Oaf'), Js('Love Flour'), Js('Love of Loaves'), Js('Luscious Layers'), Js('Lush & Luscious'), Js('Lust for Flour'), Js('Mad Batters'), Js('Makes Scents'), Js('Mayflour'), Js('Monster Cookies'), Js('More Flour to You'), Js('Muffin Top'), Js('Naturally Delicious'), Js('One-Man Dough'), Js("Oven Lovin'"), Js('Path of Crumbs'), Js('Piece of Cake'), Js('Piece of the Pie'), Js('Premier Cakes'), Js('Prime Dough'), Js('Quakey Cakeys'), Js('Raisin Dough'), Js('Rise of the Buns'), Js('Risk it for a Biscuit'), Js('Rolling Scones'), Js('Scents Time Immemorial'), Js('Scents of Humor'), Js('Sensational Goodies'), Js('Sifted Gifts'), Js('Sinful Temptations'), Js('Sixth Scents'), Js('Slow Dough'), Js('Smell the Flours'), Js('Snack Rack'), Js('Snack Shack'), Js('Snackamuffins'), Js('Sprinkles of Joy'), Js('Status Dough'), Js('Steal the Dough'), Js('Sugar Beat'), Js('Sugar Bliss'), Js('Sweet Beat'), Js('Sweet Cakes'), Js('Sweet Cheeks'), Js('Sweet Dreams'), Js('Sweet Sensations'), Js('Sweetie Pies'), Js('Sweets and Such'), Js('Swirls and Pearls'), Js('Take the Cake'), Js('Takes the Cake'), Js('Taste of Heaven'), Js('The Cake is a Pie'), Js('The Confection Connection'), Js('The Cookie Cook'), Js('The Cookie Rookie'), Js('The Cooling Rack'), Js('The Dough Below'), Js('The Dough Flow'), Js('The Flour Tower'), Js('The Fruitcake'), Js('The Glaze Maze'), Js('The Glaze Phase'), Js('The Grateful Bread'), Js('The Mistledough'), Js('The Pastry Corner'), Js('The Pastry Sheet'), Js('The Secret Ingredient'), Js('The Shadough'), Js('The Sweet Spot'), Js('The Torpedough'), Js("There's Nothing Batter"), Js('Those Buns Dough'), Js('Tiers of Delight'), Js('Tiers of Joy'), Js('Tokens of my Confection'), Js('Top of the Flour'), Js('Top of the Muffin'), Js('Torte Reform'), Js('Tough Cookies'), Js('Tout de Sweet'), Js('Up the Cakes'), Js('Wakey Bakey'), Js('Wallflour'), Js('We Knead Dough'), Js('We Take the Cake'), Js('Wee Flours'), Js('Whisk it for a Biscuit'), Js('Whoopie Cakes'), Js('Witching Flours'), Js('You Take the Cake')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
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
bakeryNames = var.to_python()
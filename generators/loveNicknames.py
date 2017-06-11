__all__ = ['loveNicknames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Angel'), Js('Angel Eyes'), Js('Angelface'), Js('Babe'), Js('Babes'), Js('Baboo'), Js('Baby'), Js('Baby Bear'), Js('Baby Bird'), Js('Baby Boo'), Js('Baby Cakes'), Js('Baby Girl'), Js('Babydoll'), Js('Big Kitty'), Js('Biscuit'), Js('Blossom'), Js('Bonbon'), Js('Boo Bear'), Js('Booboo'), Js('Bright Eyes'), Js('Bubba'), Js('Bubbies'), Js('Bubbles'), Js('Bunbun'), Js('Bunny'), Js('Buttercup'), Js('Buttons'), Js('Cacao'), Js('Cakes'), Js('Candy'), Js('Cheesecake'), Js('Cherry Blossom'), Js('Cherry Pie'), Js('Chipmunk'), Js('Chocolate'), Js('Cinnamon'), Js('Cocoa'), Js('Cookie'), Js('Cuddle Bear'), Js('Cuddle Muffin'), Js('Cuddlebug'), Js('Cuddles'), Js('Cupcake'), Js('Cupid'), Js('Cuppy Cake'), Js('Cuteness'), Js('Cutie'), Js('Cutie Patootie'), Js('Cutie Pie'), Js("Darlin'"), Js('Darling'), Js('Darlington'), Js('Dashing'), Js('Dear'), Js('Dearheart'), Js('Deary'), Js('Dewdrop'), Js('Dimples'), Js('Donut'), Js('Doodle'), Js('Dove'), Js('Dreambuns'), Js('Dreamlove'), Js('Duckling'), Js('Ducky'), Js('Dummy'), Js('Dumpling'), Js('Everything'), Js('Flower'), Js('Fluffkin'), Js('Flufs'), Js('Fruit Cake'), Js('Fruit Loop'), Js('Funny Bunny'), Js('Giggles'), Js('Goofball'), Js('Gorgeous'), Js('Gumdrop'), Js('Handsome'), Js('Happiness'), Js('Hon'), Js("Hon' Bun"), Js('Honey'), Js('Honey Bear'), Js('Honey Bee'), Js('Honey Bunny'), Js('Honey Buns'), Js('Honey Pie'), Js('Honey Pot'), Js('Hot Cakes'), Js('Hot Honey'), Js('Hot Stuff'), Js('Hottie'), Js('Hubby Wubby'), Js('Huggy Bear'), Js('Jelly Bean'), Js('Joy'), Js('Kissy Face'), Js('Kit Kat'), Js('Kitten'), Js('Kittycat'), Js('Lemon Drop'), Js('Lemonpie'), Js('Little Dove'), Js('Love'), Js('Love Bug'), Js('Love Nugget'), Js('Lovebird'), Js('Loveylove'), Js('Lovie'), Js('Lucky Charm'), Js('Magic'), Js('Marshmallow'), Js('Melody'), Js('Mooky'), Js('Muffin'), Js('Muggles'), Js('Munchkin'), Js('Muppet'), Js('My Dear'), Js('My Everything'), Js('My World'), Js('Nugget'), Js('Numnums'), Js('Pancake'), Js('Pandabear'), Js('Paradise'), Js('Passion Fruit'), Js('Peach'), Js('Peach Blossom'), Js('Peachy Pie'), Js('Peanut'), Js('Petal'), Js('Pookums'), Js('Porkchop'), Js('Precious'), Js("Puddin'"), Js("Pumpkin'"), Js('Puppy'), Js('Pussycat'), Js('Rubber Ducky'), Js('Schmooky'), Js('Scrumptious'), Js('Shmoops'), Js('Short Cake'), Js('Silly Goose'), Js('Smiles'), Js('Smooch'), Js('Smoochie'), Js('Smoochie Poo'), Js('Snickerdoodle'), Js('Snoogypuss'), Js('Snookie'), Js('Snookums'), Js('Snow Pea'), Js('Snowflake'), Js('Snuggems'), Js('Snuggle Bear'), Js('Snuggle Bunny'), Js('Snuggles'), Js('Snuggly'), Js('Soda Pop'), Js('Songbird'), Js('Sparkles'), Js('Sparky'), Js('Spring'), Js('Sprinkles'), Js('Star'), Js('Starlight'), Js('Starshine'), Js('Steambuns'), Js('Stud Muffin'), Js('Sugar'), Js('Sugar Bear'), Js('Sugar Biscuit'), Js('Sugar Britches'), Js('Sugar Buns'), Js('Sugar Lips'), Js('Sugar Puff'), Js('Sugarplum'), Js('Summer'), Js('Summerpie'), Js('Sunshine'), Js('Sweet Baby'), Js('Sweet Cheeks'), Js('Sweet Pea'), Js('Sweet Peach'), Js('Sweet Potato'), Js('Sweetheart'), Js('Sweetie'), Js('Sweetie Bird'), Js('Sweetkins'), Js('Sweetness'), Js('Sweets'), Js('Sweetstuff'), Js('Sweetums'), Js('Sweety Cakes'), Js('Tator-tot'), Js('Teddy Bear'), Js('Toots'), Js('Tootsie'), Js('Tumtums'), Js('Twinkie'), Js('Twinkle Toes'), Js('Waffles'), Js('Wiggles'), Js('Wookie'), Js('Wookums'), Js('Yummy'), Js('Yumyum')]))
pass
pass


# Add lib to the module scope
loveNicknames = var.to_python()
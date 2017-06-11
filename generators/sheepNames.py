__all__ = ['sheepNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ace'), Js('Babbit'), Js('Badger'), Js('Bambam'), Js('Basil'), Js('Biggs'), Js('Boomboom'), Js('Boomer'), Js('Bud'), Js('Buddy'), Js('Bullet'), Js('Buster'), Js('Butters'), Js('Capricorn'), Js('Chopper'), Js('Chops'), Js('Cloud'), Js('Coal'), Js('Cobalt'), Js('Coffee'), Js('Comet'), Js('Cosmo'), Js('Cotton'), Js('Cuddles'), Js('Dash'), Js('Dawson'), Js('Dillon'), Js('Dodge'), Js('Dodger'), Js('Duke'), Js('Fire'), Js('Fluff'), Js('Gunther'), Js('Hammer'), Js('Impact'), Js('Jax'), Js('Kramer'), Js('Lancelot'), Js('Lightning'), Js('Lucky'), Js('Maverick'), Js('McCloud'), Js('Mercury'), Js('Midnight'), Js('Monty'), Js('Mort'), Js('Murky'), Js('Mush'), Js('Nebula'), Js('Nibbler'), Js('Nibbles'), Js('Nibler'), Js('Ogre'), Js('Onyx'), Js('Orion'), Js('Owen'), Js('Patches'), Js('Patton'), Js('Phineas'), Js('Pillo'), Js('Pitch'), Js('Popcorn'), Js('Pound'), Js('Puff'), Js('Rack'), Js('Ragget'), Js('Rambo'), Js('Ramone'), Js('Ripple'), Js('Rock'), Js('Rowan'), Js('Rowdy'), Js('Ruff'), Js('Rufus'), Js('Saber'), Js('Salt'), Js('Satin'), Js('Sawyer'), Js('Scruffy'), Js('Scuddle'), Js('Sean'), Js('Shawn'), Js('Shelby'), Js('Silver'), Js('Skooter'), Js('Slam'), Js('Smokey'), Js('Smooch'), Js('Snow'), Js('Snowflake'), Js('Soots'), Js('Spark'), Js('Spartan'), Js('Spice'), Js('Sponge'), Js('Spot'), Js('Storm'), Js('Striker'), Js('Taz'), Js('Thunder'), Js('Tickles'), Js('Truffle'), Js('Tumnus'), Js('Tweedle'), Js('Twinkle'), Js('Vanilla'), Js('Walnut'), Js('Wellington'), Js('Woolsley')]))
var.put('nm2', Js([Js('Agnes'), Js('Angel'), Js('Aria'), Js('Baarbara'), Js('Beetle'), Js('Bella'), Js('Bitsy'), Js('Blue'), Js('Bonnie'), Js('Buffy'), Js('Bugsie'), Js('Bumble'), Js('Bunny'), Js('Buttercup'), Js('Button'), Js('Buttons'), Js('Candy'), Js('Capri'), Js('Chewe'), Js('Cloude'), Js('Clover'), Js('Coco'), Js('Cosmo'), Js('Cotton'), Js('Cream'), Js('Creme'), Js('Crystal'), Js('Cuddle'), Js('Cuddles'), Js('Cushion'), Js('Daahling'), Js('Daffodil'), Js('Daisy'), Js('Darling'), Js('Dixie'), Js('Dolly'), Js('Dora'), Js('Dottie'), Js('Ebony'), Js('Ewey'), Js('Fern'), Js('Flower'), Js('Fluffy'), Js('Flufkins'), Js('Flurry'), Js('Gigi'), Js('Ginger'), Js('Gloria'), Js('Goldilocks'), Js('Gorgeous'), Js('Honey'), Js('Iris'), Js('Ivory'), Js('Ivy'), Js('Jasmin'), Js('Jazzy'), Js('Lane'), Js('Lavender'), Js('Libby'), Js('Lilly'), Js('Linsey'), Js('Lucy'), Js('Luna'), Js('Lyric'), Js('Maggie'), Js('Maple'), Js('Marigold'), Js('Midge'), Js('Midnight'), Js('Minty'), Js('Misty'), Js('Molly'), Js('Momma'), Js('Muffin'), Js('Nell'), Js('Nibble'), Js('Nova'), Js('Nutmeg'), Js('Oreo'), Js('Pearl'), Js('Pepper'), Js('Petunia'), Js('Pickle'), Js('Puffle'), Js('Puffles'), Js('Raine'), Js('Raspberry'), Js('Rosemary'), Js('Ruth'), Js('Sage'), Js('Serenity'), Js('Shaggy'), Js('Shelly'), Js('Sierra'), Js('Silver'), Js('Smiley'), Js('Smooch'), Js('Smooches'), Js('Snowflake'), Js('Snuggle'), Js('Snuggles'), Js('Snugs'), Js('Socks'), Js('Speckle'), Js('Speckles'), Js('Spice'), Js('Strawberry'), Js('Sugar'), Js('Sweetie'), Js('Sweetpea'), Js('Teeny'), Js('Tinkerbell'), Js('Tiny'), Js('Tulip'), Js('Twinkie'), Js('Twinkle'), Js('Vanilla'), Js('Velvet'), Js('Venus')]))
pass
pass


# Add lib to the module scope
sheepNames = var.to_python()
__all__ = ['christmasElfNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', (((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Alabaster'), Js('Angel'), Js('Berry'), Js('Bing'), Js('Bling'), Js('Blitz'), Js('Blue'), Js('Bluebell'), Js('Brandysnap'), Js('Brownie'), Js('Buddy'), Js('Bushy'), Js('Buster'), Js('Butters'), Js('Button'), Js('Buttons'), Js('Candycane'), Js('Cedar'), Js('Chestnut'), Js('Choco'), Js('Cinnamon'), Js('Coco'), Js('Cocoa'), Js('Cookie'), Js('Dash'), Js('Elm'), Js('Evergreen'), Js('Fig'), Js('Figgy'), Js('Fir'), Js('Fizzy'), Js('Flake'), Js('Fluffy'), Js('Frost'), Js('Frosty'), Js('Fruity'), Js('Fudge'), Js('Fuzzle'), Js('Garland'), Js('Ginger'), Js('Gingernuts'), Js('Gingersnap'), Js('Glitter'), Js('Glory'), Js('Hazelnut'), Js('Ice'), Js('Jangle'), Js('Jingle'), Js('Jolly'), Js('Marzipan'), Js('Merry'), Js('Mince'), Js('Mint'), Js('Mistle'), Js('Mistletoe'), Js('Noel'), Js('Nutmeg'), Js('Pepper'), Js('Peppetmint'), Js('Perky'), Js('Pine'), Js('Pinecone'), Js('Pudding'), Js('Rusty'), Js('Shimmer'), Js('Skittle'), Js('Snappy'), Js('Snow'), Js('Snowball'), Js('Snowdrop'), Js('Snowflake'), Js('Sparkle'), Js('Sprinkle'), Js('Sprinkles'), Js('Starlight'), Js('Stripes'), Js('Sugar'), Js('Sugarplum'), Js('Tinkles'), Js('Tinsel'), Js('Tiny'), Js('Topper'), Js('Trinket'), Js('Twinkle'), Js('Twinkletoes'), Js('Wink'), Js('Winter'), Js('Yule')]))
var.put('nm2', Js([Js('Angel'), Js('Berry'), Js('Bing'), Js('Bling'), Js('Blitz'), Js('Blue'), Js('Bluebell'), Js('Brownie'), Js('Button'), Js('Buttons'), Js('Candycane'), Js('Choco'), Js('Cinnamon'), Js('Coco'), Js('Cocoa'), Js('Cookie'), Js('Dash'), Js('Fig'), Js('Figgy'), Js('Fizzy'), Js('Flake'), Js('Fluffy'), Js('Fruity'), Js('Fudge'), Js('Fuzzle'), Js('Garland'), Js('Ginger'), Js('Gingernuts'), Js('Gingersnap'), Js('Glitter'), Js('Glory'), Js('Ice'), Js('Jangle'), Js('Jingle'), Js('Jolly'), Js('Merry'), Js('Mince'), Js('Mint'), Js('Mistle'), Js('Mistletoe'), Js('Nutmeg'), Js('Pepper'), Js('Peppetmint'), Js('Perky'), Js('Pine'), Js('Pudding'), Js('Skittle'), Js('Snappy'), Js('Snow'), Js('Snowball'), Js('Snowdrop'), Js('Snowflake'), Js('Sparkle'), Js('Sprinkle'), Js('Sprinkles'), Js('Starlight'), Js('Stripes'), Js('Sugar'), Js('Sugarplum'), Js('Tinkles'), Js('Tinsel'), Js('Tiny'), Js('Topper'), Js('Trinket'), Js('Twinkle'), Js('Twinkletoes'), Js('Wink'), Js('Winter'), Js('Yule')]))
var.put('nm3', Js([Js('Angel'), Js('Belle'), Js('Berry'), Js('Bing'), Js('Bling'), Js('Blitz'), Js('Blue'), Js('Bluebell'), Js('Brandy'), Js('Brownie'), Js('Bubbles'), Js('Button'), Js('Buttons'), Js('Candy'), Js('Candycane'), Js('Carol'), Js('Cherry'), Js('Choco'), Js('Cinnamon'), Js('Clove'), Js('Coco'), Js('Cocoa'), Js('Cookie'), Js('Cupcake'), Js('Dandy'), Js('Dash'), Js('Ember'), Js('Emerald'), Js('Eve'), Js('Evie'), Js('Faith'), Js('Fig'), Js('Figgy'), Js('Fizzy'), Js('Flake'), Js('Fluffy'), Js('Fruity'), Js('Fudge'), Js('Fuzzle'), Js('Garland'), Js('Ginger'), Js('Gingernuts'), Js('Gingersnap'), Js('Glitter'), Js('Gloria'), Js('Glory'), Js('Hazel'), Js('Holly'), Js('Honey'), Js('Honeycomb'), Js('Hope'), Js('Ice'), Js('Ivy'), Js('Jangle'), Js('Jewel'), Js('Jingle'), Js('Jolly'), Js('Joy'), Js('Juniper'), Js('Merry'), Js('Mince'), Js('Mint'), Js('Mistle'), Js('Mistletoe'), Js('Noelle'), Js('Nutmeg'), Js('Pepper'), Js('Peppetmint'), Js('Perky'), Js('Pine'), Js('Pudding'), Js('Ruby'), Js('Scarlet'), Js('Skittle'), Js('Snappy'), Js('Snow'), Js('Snowball'), Js('Snowdrop'), Js('Snowflake'), Js('Sparkle'), Js('Sprinkle'), Js('Sprinkles'), Js('Starlight'), Js('Stripes'), Js('Sugar'), Js('Sugarplum'), Js('Tinkles'), Js('Tinsel'), Js('Tiny'), Js('Topper'), Js('Trinket'), Js('Trixie'), Js('Twinkle'), Js('Twinkletoes'), Js('Wink'), Js('Winter'), Js('Yule')]))
var.put('nm4', Js([Js('Angel'), Js('Bustle'), Js('Busy'), Js('Candle'), Js('Candy'), Js('Carol'), Js('Chill'), Js('Chilly'), Js('Chimney'), Js('Chocolate'), Js('Cider'), Js('Cookie'), Js('Crackle'), Js('Cuddle'), Js('Dream'), Js('Ever'), Js('Fire'), Js('Flippy'), Js('Frost'), Js('Frosty'), Js('Fruit'), Js('Gift'), Js('Good'), Js('Goody'), Js('Grotto'), Js('Happy'), Js('Holi'), Js('Holly'), Js('Hot'), Js('Hustle'), Js('Ivy'), Js('Jiggle'), Js('Jingle'), Js('Jolly'), Js('Magic'), Js('Milk'), Js('Milky'), Js('Miracle'), Js('Mistle'), Js('Mitten'), Js('Morning'), Js('Muffin'), Js('Nibble'), Js('Night'), Js('Nippy'), Js('Party'), Js('Pickle'), Js('Plum'), Js('Poem'), Js('Pudding'), Js('Rhyme'), Js('Ribbon'), Js('Sleepy'), Js('Snow'), Js('Sparkle'), Js('Sugar'), Js('Sweet'), Js('Toffee'), Js('Twinkle'), Js('Wiggle')]))
var.put('nm5', Js([Js('ball'), Js('beard'), Js('bell'), Js('bow'), Js('box'), Js('cake'), Js('cane'), Js('card'), Js('carol'), Js('cheer'), Js('dance'), Js('dancer'), Js('dash'), Js('feast'), Js('flake'), Js('foot'), Js('friend'), Js('frost'), Js('fun'), Js('game'), Js('gift'), Js('glitter'), Js('glove'), Js('guest'), Js('hat'), Js('hope'), Js('hug'), Js('icicle'), Js('ivy'), Js('joke'), Js('joy'), Js('jump'), Js('kiss'), Js('laugh'), Js('light'), Js('love'), Js('milk'), Js('mitten'), Js('moon'), Js('myrrh'), Js('night'), Js('pie'), Js('plum'), Js('scarf'), Js('sledge'), Js('sleigh'), Js('song'), Js('spirit'), Js('star'), Js('toy'), Js('tree'), Js('warmth'), Js('wine'), Js('wish'), Js('wrap')]))
pass
pass


# Add lib to the module scope
christmasElfNames = var.to_python()
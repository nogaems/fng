__all__ = ['deerNames']

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
var.put('nm1', Js([Js('Angel'), Js('Asp'), Js('Ghost'), Js('Aspen'), Js('Avalon'), Js('Ayalon'), Js('Bay'), Js('Birr'), Js('Blitz'), Js('Blitzen'), Js('Bolt'), Js('Boomerang'), Js('Bou'), Js('Brake'), Js('Browne'), Js('Brutus'), Js('Buck'), Js('Buckeye'), Js('Buckley'), Js('Bucky'), Js('Buff'), Js('Buttons'), Js('Champion'), Js('Chantler'), Js('Charger'), Js('Chase'), Js('Chestnut'), Js('Colt'), Js('Comet'), Js('Covert'), Js('Cupid'), Js('Dancer'), Js('Dapper'), Js('Darby'), Js('Dart'), Js('Darton'), Js('Dash'), Js('Dearborn'), Js('Derland'), Js('Devin'), Js('Doc'), Js('Doe'), Js('Donner'), Js('Dot'), Js('Drummer'), Js('Edge'), Js('Elk'), Js('Elwood'), Js('Fable'), Js('Forest'), Js('Forester'), Js('Freckles'), Js('Gallop'), Js('Giggle'), Js('Grayson'), Js('Grove'), Js('Grover'), Js('Hersh'), Js('Hershel'), Js('Indy'), Js('Ivor'), Js('Jingle'), Js('John Doe'), Js('Jumbo'), Js('Juno'), Js('Knob'), Js('Knobs'), Js('Legacy'), Js('Lightning'), Js('Lockhart'), Js('Lucky'), Js('Magnum'), Js('Mahony'), Js('Midnight'), Js('Mohawk'), Js('Prancer'), Js('Quest'), Js('Ray'), Js('Rocky'), Js('Roe'), Js('Rohan'), Js('Romulus'), Js('Roscoe'), Js('Rowan'), Js('Rush'), Js('Russet'), Js('Scooter'), Js('Shade'), Js('Shadow'), Js('Silver'), Js('Sky'), Js('Snow'), Js('Solace'), Js('Spike'), Js('Spot'), Js('Springer'), Js('Sprinter'), Js('Sprite'), Js('Spruce'), Js('Spurt'), Js('Starbuck'), Js('Storm'), Js('Stormy'), Js('Sunny'), Js('Tawn'), Js('Thicket'), Js('Thunder'), Js('Timber'), Js('Titan'), Js('Umber'), Js('Ward'), Js('Weald'), Js('Willow'), Js('Wonder'), Js('Woods'), Js('Woody'), Js('Yogi')]))
var.put('nm2', Js([Js('Aphra'), Js('Afra'), Js('Hymn'), Js('Ayala'), Js('Bambi'), Js('Fawn'), Js('Fawne'), Js('Doe'), Js('Raleigh'), Js('Hinda'), Js('Hynd'), Js('Hynda'), Js('Hynde'), Js('Luna'), Js('Willow'), Js('Lyric'), Js('Dash'), Js('Milo'), Js('Fern'), Js('Melrose'), Js('Ficus'), Js('Spryte'), Js('Lucky'), Js('Dance'), Js('Ayala'), Js('Summer'), Js('Spring'), Js('Autumn'), Js('Winter'), Js('Elain'), Js('Tabby'), Js('Tibby'), Js('Ivory'), Js('Pearl'), Js('Snow'), Js('Snowflake'), Js('Hazel'), Js('Bay'), Js('Umber'), Js('Amber'), Js('Cinnamon'), Js('Coco'), Js('Tawny'), Js('Cookie'), Js('Muffin'), Js('Beauty'), Js('Buttercup'), Js('Freckles'), Js('Spot'), Js('Speckle'), Js('Speckles'), Js('Grace'), Js('Ivy'), Js('Promise'), Js('Raidrop'), Js('Serenity'), Js('Speckles'), Js('Zoe'), Js('Dyani'), Js('Hinda'), Js('Jane Doe'), Js('Daisy'), Js('Dear'), Js('Pepper'), Js('Princess'), Js('Queen'), Js('Elli'), Js('Elkee'), Js('Vixen'), Js('Dash'), Js('Silka'), Js('Boubou'), Js('Harmony'), Js('Flower'), Js('Furball'), Js('Buttercup'), Js('Nutmeg'), Js('Aurora'), Js('Aura'), Js('Heiress'), Js('Liberty'), Js('Jasmine'), Js('Ashley'), Js('Jewel'), Js('Enigma'), Js('Toffee'), Js('Patches'), Js('Shye'), Js('Huntress'), Js('Cotton'), Js('Luna'), Js('Breeze'), Js('Breezy'), Js('Dashful'), Js('Whiskers'), Js('Nighte'), Js('Brooke'), Js('Moone'), Js('Winde'), Js('Windy'), Js('Enya'), Js('Cloude'), Js('Hope'), Js('Lace'), Js('Silk'), Js('Orchid'), Js('Lullaby'), Js('Pebbles'), Js('River'), Js('Cupcake'), Js('Mystique'), Js('Ginger'), Js('Destiny')]))
pass
pass


# Add lib to the module scope
deerNames = var.to_python()
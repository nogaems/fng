__all__ = ['rocNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Acid'), Js('Anger'), Js('Angry'), Js('Beam'), Js('Bitter'), Js('Black'), Js('Blade'), Js('Bleak'), Js('Blood'), Js('Bold'), Js('Bone'), Js('Brass'), Js('Bright'), Js('Broad'), Js('Bronze'), Js('Chaos'), Js('Cloud'), Js('Crazy'), Js('Crimson'), Js('Crown'), Js('Dark'), Js('Dawn'), Js('Dead'), Js('Death'), Js('Demon'), Js('Devil'), Js('Doom'), Js('Draft'), Js('Dread'), Js('Dream'), Js('Dusk'), Js('Dust'), Js('Ebon'), Js('Ember'), Js('Fire'), Js('Flame'), Js('Fog'), Js('Foul'), Js('Frost'), Js('Fume'), Js('Fury'), Js('Ghost'), Js('Giant'), Js('Glass'), Js('Gloom'), Js('Gold'), Js('Grave'), Js('Great'), Js('Grey'), Js('Grim'), Js('Grin'), Js('Half'), Js('Hate'), Js('Hell'), Js('Hollow'), Js('Ice'), Js('Iron'), Js('Jade'), Js('Kill'), Js('Kite'), Js('Light'), Js('Lightning'), Js('Lone'), Js('Lunar'), Js('Mad'), Js('Marsh'), Js('Metal'), Js('Mist'), Js('Moon'), Js('Night'), Js('Onyx'), Js('Phantom'), Js('Primal'), Js('Prime'), Js('Putrid'), Js('Quill'), Js('Rabid'), Js('Rage'), Js('Rain'), Js('Rapid'), Js('Rash'), Js('Razor'), Js('Red'), Js('River'), Js('Shadow'), Js('Silent'), Js('Smoke'), Js('Solar'), Js('Spark'), Js('Spite'), Js('Star'), Js('Stark'), Js('Steel'), Js('Stitch'), Js('Storm'), Js('Sun'), Js('Swift'), Js('Terror'), Js('Thorn'), Js('Thrill'), Js('Thunder'), Js('Twilight'), Js('Venom'), Js('Warp'), Js('Whip')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('beak'), Js('belly'), Js('bill'), Js('breast'), Js('claw'), Js('crest'), Js('crown'), Js('eye'), Js('eyes'), Js('feather'), Js('head'), Js('mantle'), Js('plume'), Js('tail'), Js('talon'), Js('wing'), Js('wings')]))
pass
pass


# Add lib to the module scope
rocNames = var.to_python()
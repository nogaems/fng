__all__ = ['mgtFaeries']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                if (var.get('i')<Js(2.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd6'))):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(4.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                    else:
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    while PyJsStrictEq(var.get('nm6').get(var.get('rnd')),var.get('nm7').get(var.get('rnd2'))):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+Js(' '))+var.get('nm8').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((var.get('nm9').get(var.get('rnd'))+Js(' '))+var.get('nm10').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('f'), Js('h'), Js('l'), Js('n'), Js('r'), Js('s'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('oo'), Js('ia'), Js('ea'), Js('ee')]))
var.put('nm3', Js([Js('b'), Js('d'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('v'), Js('b'), Js('d'), Js('dw'), Js('l'), Js('ll'), Js('lw'), Js('lr'), Js('lm'), Js('ln'), Js('m'), Js('mr'), Js('mm'), Js('n'), Js('nm'), Js('nr'), Js('nv'), Js('r'), Js('rl'), Js('rn'), Js('rm'), Js('sh'), Js('sn'), Js('sr'), Js('vl'), Js('vr')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('l'), Js('n'), Js('r'), Js('s'), Js('th'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n'), Js('ph'), Js('s'), Js('th')]))
var.put('nm6', Js([Js('acorn'), Js('alder'), Js('alpen'), Js('amber'), Js('autumn'), Js('barely'), Js('beech'), Js('birch'), Js('briar'), Js('bright'), Js('cedar'), Js('cherry'), Js('cinder'), Js('cloud'), Js('crystal'), Js('dawn'), Js('dew'), Js('dream'), Js('dusk'), Js('elm'), Js('ember'), Js('feather'), Js('fern'), Js('fog'), Js('forest'), Js('free'), Js('frost'), Js('gentle'), Js('grand'), Js('grass'), Js('great'), Js('green'), Js('haven'), Js('hazel'), Js('heart'), Js('holly'), Js('humble'), Js('keen'), Js('kind'), Js('leaf'), Js('light'), Js('lone'), Js('maple'), Js('marble'), Js('marsh'), Js('mellow'), Js('mist'), Js('moon'), Js('moss'), Js('nettle'), Js('night'), Js('oaken'), Js('orb'), Js('peach'), Js('pine'), Js('plain'), Js('pride'), Js('proud'), Js('rain'), Js('rapid'), Js('ring'), Js('river'), Js('rock'), Js('rose'), Js('rune'), Js('silent'), Js('silk'), Js('silver'), Js('sky'), Js('snow'), Js('spell'), Js('spring'), Js('spruce'), Js('star'), Js('stern'), Js('stout'), Js('sun'), Js('swift'), Js('thorn'), Js('vine'), Js('water'), Js('weather'), Js('willow'), Js('wood'), Js('yew')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('bash'), Js('beam'), Js('belly'), Js('bend'), Js('berry'), Js('bind'), Js('blossom'), Js('blow'), Js('bough'), Js('brace'), Js('braid'), Js('bramble'), Js('branch'), Js('brand'), Js('breath'), Js('breeze'), Js('brook'), Js('brooke'), Js('bush'), Js('cloud'), Js('copse'), Js('covert'), Js('crest'), Js('crown'), Js('dance'), Js('dancer'), Js('dew'), Js('down'), Js('draft'), Js('dream'), Js('drift'), Js('drop'), Js('dust'), Js('fall'), Js('fern'), Js('fir'), Js('flow'), Js('gaze'), Js('gem'), Js('glade'), Js('gleam'), Js('glide'), Js('glow'), Js('grove'), Js('gust'), Js('heart'), Js('husk'), Js('larch'), Js('leaf'), Js('lock'), Js('ridge'), Js('river'), Js('rock'), Js('run'), Js('seed'), Js('shade'), Js('shine'), Js('shrub'), Js('skipper'), Js('snow'), Js('soar'), Js('song'), Js('spell'), Js('spirit'), Js('sprout'), Js('spur'), Js('stand'), Js('star'), Js('stone'), Js('stride'), Js('stutter'), Js('sun'), Js('thorn'), Js('track'), Js('trap'), Js('twig'), Js('ward'), Js('water'), Js('wind'), Js('wing'), Js('wings')]))
var.put('nm8', Js([Js('Dancer'), Js('Faerie'), Js('Flitter'), Js('Leprechaun'), Js('Pixie'), Js('Prankster'), Js('Schemer'), Js('Spinner'), Js('Sprite'), Js('Swarm')]))
var.put('nm9', Js([Js('Autumn'), Js('Blizzard'), Js('Brush'), Js('Bush'), Js('Cloud'), Js('Dew'), Js('Dewdrop'), Js('Dirt'), Js('Dream'), Js('Dust'), Js('Fan'), Js('Feather'), Js('Fire'), Js('Flight'), Js('Flock'), Js('Flower'), Js('Fog'), Js('Forest'), Js('Frost'), Js('Garden'), Js('Glen'), Js('Gust'), Js('Honey'), Js('Ice'), Js('Icicle'), Js('Jewel'), Js('Kite'), Js('Leaf'), Js('Lift'), Js('Light'), Js('Lunar'), Js('Marble'), Js('Marsh'), Js('Meadow'), Js('Mist'), Js('Moon'), Js('Mountain'), Js('Nectar'), Js('Night'), Js('Nightshade'), Js('Ocean'), Js('Plane'), Js('Rain'), Js('Riddle'), Js('River'), Js('Sand'), Js('Sea'), Js('Shade'), Js('Shadow'), Js('Shore'), Js('Shrub'), Js('Silk'), Js('Snow'), Js('Solar'), Js('Spring'), Js('Storm'), Js('Stream'), Js('Summer'), Js('Sun'), Js('Thorn'), Js('Thunder'), Js('Water'), Js('Wind'), Js('Winter'), Js('Zephyr')]))
var.put('nm10', Js([Js('Archmage'), Js('Blackguard'), Js('Caretaker'), Js('Clique'), Js('Cohort'), Js('Dancer'), Js('Dewdancer'), Js('Disciple'), Js('Faerie'), Js('Flitter'), Js('Gatewarden'), Js('Guard'), Js('Guardian'), Js('Harbinger'), Js('Invader'), Js('Keeper'), Js('Lancer'), Js('Leprechaun'), Js('Mage'), Js('Mechanist'), Js('Noble'), Js('Overseer'), Js('Pixie'), Js('Prankster'), Js('Priestess'), Js('Prowler'), Js('Ranger'), Js('Rascal'), Js('Rover'), Js('Sage'), Js('Schemer'), Js('Scout'), Js('Seer'), Js('Singer'), Js('Skipper'), Js('Soulsinger'), Js('Spinner'), Js('Sprite'), Js('Spy'), Js('Squadron'), Js('Swarm'), Js('Thief'), Js('Trickster'), Js('Wanderer'), Js('Warden'), Js('Witch')]))
pass
pass


# Add lib to the module scope
mgtFaeries = var.to_python()
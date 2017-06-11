__all__ = ['plantationNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Allen'), Js('Alt'), Js('Ash'), Js('Asp'), Js('Aspen'), Js('Autumn'), Js('Banner'), Js('Barley'), Js('Beaver'), Js('Bee'), Js('Beech'), Js('Belle'), Js('Bird'), Js('Birds'), Js('Black'), Js('Bleak'), Js('Bog'), Js('Boulder'), Js('Brier'), Js('Broad'), Js('Brown'), Js('Buck'), Js('Castle'), Js('Cedar'), Js('Cherry'), Js('Cinnamon'), Js('Clare'), Js('Clay'), Js('Clear'), Js('Clover'), Js('Cold'), Js('Cole'), Js('Cool'), Js('Craw'), Js('Creek'), Js('Crescent'), Js('Crimson'), Js('Crow'), Js('Dawn'), Js('Dusk'), Js('East'), Js('Edge'), Js('Elk'), Js('Elm'), Js('Ever'), Js('Fair'), Js('Far'), Js('Farm'), Js('Forest'), Js('Fox'), Js('Free'), Js('Frog'), Js('Frost'), Js('Glen'), Js('Good'), Js('Grace'), Js('Grass'), Js('Gray'), Js('Green'), Js('Grime'), Js('Hare'), Js('Haw'), Js('Hazel'), Js('High'), Js('Hill'), Js('Holly'), Js('Home'), Js('Honey'), Js('Hope'), Js('Humble'), Js('Idle'), Js('Ivy'), Js('Jade'), Js('King'), Js('Kings'), Js('Lake'), Js('Lang'), Js('Lily'), Js('Locust'), Js('Log'), Js('Long'), Js('Low'), Js('Marsh'), Js('Mel'), Js('Mid'), Js('Middle'), Js('Mill'), Js('Moon'), Js('Moss'), Js('Mud'), Js('Myrtle'), Js('Narrow'), Js('Nettle'), Js('New'), Js('Noble'), Js('North'), Js('Oak'), Js('Oat'), Js('Peace'), Js('Pine'), Js('Pleasant'), Js('Raven'), Js('Red'), Js('Rich'), Js('Ridge'), Js('Rivers'), Js('Rock'), Js('Rose'), Js('Rosen'), Js('Rust'), Js('Salt'), Js('Sand'), Js('Sea'), Js('Shade'), Js('Shadow'), Js('Short'), Js('Snow'), Js('South'), Js('Spring'), Js('Stag'), Js('Star'), Js('Stone'), Js('Summer'), Js('Swan'), Js('Tangle'), Js('Thorn'), Js('Under'), Js('West'), Js('Wheat'), Js('Whit'), Js('White'), Js('Wild'), Js('Willow'), Js('Wind'), Js('Winter'), Js('Wood'), Js('Worm')]))
var.put('nm2', Js([Js('bald'), Js('bay'), Js('bend'), Js('berry'), Js('bloom'), Js('blossom'), Js('bluff'), Js('borough'), Js('bourne'), Js('branch'), Js('bridge'), Js('brook'), Js('burg'), Js('burgh'), Js('burn'), Js('bury'), Js('cairn'), Js('cove'), Js('creek'), Js('dale'), Js('dam'), Js('dew'), Js('down'), Js('field'), Js('fields'), Js('font'), Js('ford'), Js('green'), Js('ground'), Js('grove'), Js('hall'), Js('haven'), Js('hill'), Js('hope'), Js('isle'), Js('land'), Js('lands'), Js('lane'), Js('lawn'), Js('meadow'), Js('mond'), Js('mont'), Js('more'), Js('moss'), Js('mount'), Js('mountain'), Js('mourne'), Js('mouth'), Js('pebble'), Js('plains'), Js('point'), Js('pond'), Js('pool'), Js('port'), Js('rest'), Js('ridge'), Js('river'), Js('rock'), Js('side'), Js('song'), Js('sor'), Js('spring'), Js('springs'), Js('stead'), Js('stone'), Js('stones'), Js('thorne'), Js('ton'), Js('town'), Js('vale'), Js('valley'), Js('view'), Js('ville'), Js('wall'), Js('way'), Js('well'), Js('wild'), Js('will'), Js('wood'), Js('woods'), Js('worth'), Js('worthy')]))
var.put('nm3', Js([Js('Plantation'), Js('Plantation House'), Js('Manor'), Js('Home'), Js('Mansion'), Js('Hall'), Js('Plantation')]))
pass
pass


# Add lib to the module scope
plantationNames = var.to_python()
__all__ = ['snowlands']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', (((Js('The ')+var.get('names1').get(var.get('rnd')))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                var.put('names', (((((((Js('The ')+var.get('names3').get(var.get('rnd')))+var.get('names4').get(var.get('rnd2')))+var.get('names5').get(var.get('rnd3')))+var.get('names6').get(var.get('rnd4')))+var.get('names7').get(var.get('rnd5')))+Js(' '))+var.get('names8').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Aquamarine'), Js('Arctic'), Js('Avalanche'), Js('Azure'), Js('Blasting'), Js('Bleak'), Js('Blizzard'), Js('Bone-Chilling'), Js('Boreal'), Js('Brilliant'), Js('Chillbreath'), Js('Chillwind'), Js('Coldwind'), Js('Cracking'), Js('Crisp'), Js('Crystal'), Js('Crystalline'), Js('Diamond'), Js('Flurry'), Js('Freezing'), Js('Frigid'), Js('Frost'), Js('Frostbite'), Js('Frostbreath'), Js('Frosted'), Js('Frostfever'), Js('Frostfinger'), Js('Frostfire'), Js('Frozen'), Js('Ghostly'), Js('Glacial'), Js('Glacier'), Js('Glazed'), Js('Glimmering'), Js('Ice Crystal'), Js('Ice Floe'), Js('Ice Needle'), Js('Iceberg'), Js('Icebound'), Js('Icecap'), Js('Iced'), Js('Iceshelf'), Js('Icicle'), Js('Icy'), Js('Igloo'), Js('Ivory'), Js('Meltwater'), Js('Milky'), Js('Mirror'), Js('Mute'), Js('Muted'), Js('Nevermelting'), Js('Northbound'), Js('Northern'), Js('Numb'), Js('Pale'), Js('Pearly'), Js('Penguin'), Js('Permafrost'), Js('Petrified'), Js('Polar'), Js('Powder'), Js('Quiet'), Js('Quivering'), Js('Raw'), Js('Reflecting'), Js('Shattering'), Js('Shimmering'), Js('Shivering'), Js('Shuddering'), Js('Silent'), Js('Silver'), Js('Silvery'), Js('Sleeted'), Js('Sliding'), Js('Slippery'), Js('Snow Angel'), Js('Snow Crystal'), Js('Snow Owl'), Js('Snow Pack'), Js('Snow Storm'), Js('Snowbank'), Js('Snowcap'), Js('Snowdrift'), Js('Snowfall'), Js('Snowflake'), Js('Snowman'), Js('Snowslide'), Js('Snowy'), Js('Solid'), Js('Soundless'), Js('Sparkling'), Js('Thundersnow'), Js('Twinkling'), Js('Wailing'), Js('Weeping'), Js('Whimpering'), Js('Whispering'), Js('White'), Js('Winter'), Js('Yowling')]))
var.put('names2', Js([Js('Desert'), Js('Tundra'), Js('Taiga'), Js('Forests'), Js('Expanse'), Js('Fields'), Js('Flatlands'), Js('Plains')]))
var.put('names3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z')]))
var.put('names6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
var.put('names8', Js([Js('Tundra'), Js('Taiga'), Js('Expanse'), Js('Snow Fields'), Js('Snowlands'), Js('Snow Plains'), Js('Ice Fields'), Js('Icelands'), Js('Ice Plains')]))
pass
pass


# Add lib to the module scope
snowlands = var.to_python()
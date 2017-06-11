__all__ = ['firelandNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', (((((((Js('The ')+var.get('nm3').get(var.get('rnd')))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+Js(' '))+var.get('nm8').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Agni'), Js('Ash'), Js('Ashen'), Js('Barrage'), Js('Berserk'), Js('Blazing'), Js('Blister'), Js('Blistering'), Js('Blustering'), Js('Boiling'), Js('Branded'), Js('Brimstone'), Js('Broiling'), Js('Burning'), Js('Caustic'), Js('Charcoal'), Js('Charred'), Js('Charring'), Js('Cherufe'), Js('Combustion'), Js('Conflagration'), Js('Crimson'), Js('Dragon'), Js('Dragonfire'), Js('Ebon'), Js('Efreet'), Js('Ember'), Js('Fiery'), Js('Firewhirl'), Js('Flaming'), Js('Flaring'), Js('Frenzied'), Js('Frenzy'), Js('Fume'), Js('Fuming'), Js('Furious'), Js('Furnace'), Js('Glowing'), Js('Grime'), Js('Hell'), Js('Inferno'), Js('Kindle'), Js('Lampad'), Js('Lava'), Js('Mad'), Js('Magma'), Js('Nether'), Js('Nightmare'), Js('Obsidian'), Js('Onyx'), Js('Parching'), Js('Phoenix'), Js('Pitch'), Js('Pyre'), Js('Pyro'), Js('Rabid'), Js('Raging'), Js('Raving'), Js('Roasting'), Js('Ruined'), Js('Sanguine'), Js('Scalding'), Js('Scaled'), Js('Scarlet'), Js('Scorching'), Js('Searing'), Js('Singed'), Js('Sizzling'), Js('Smoking'), Js('Smouldering'), Js('Smudge'), Js('Solar'), Js('Soot'), Js('Spark'), Js('Steaming'), Js('Sultry'), Js('Tempest'), Js('Thermo'), Js('Torch'), Js('Torment'), Js('Torrid'), Js('Turbulent'), Js('Violent'), Js('Volcanic'), Js('Volcano'), Js('Wicked'), Js('Wild')]))
var.put('nm2', Js([Js('Badlands'), Js('Barrens'), Js('Desert'), Js('Domain'), Js('Dominion'), Js('Expanse'), Js('Field'), Js('Fields'), Js('Land'), Js('Lands'), Js('Plains'), Js('Range'), Js('Terrain'), Js('Territory'), Js('Wastes'), Js('Wilderness'), Js('Wilds')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
var.put('nm8', Js([Js('Badlands'), Js('Barrens'), Js('Desert'), Js('Domain'), Js('Dominion'), Js('Expanse'), Js('Field'), Js('Fields'), Js('Land'), Js('Lands'), Js('Plains'), Js('Range'), Js('Terrain'), Js('Territory'), Js('Wastes'), Js('Wilderness'), Js('Wilds'), Js('Fireland'), Js('Firelands'), Js('Fire Fields'), Js('Flamelands'), Js('Flame Fields'), Js('Ashlands'), Js('Ash Fields'), Js('Emberlands'), Js('Ember Lands')]))
pass
pass


# Add lib to the module scope
firelandNames = var.to_python()
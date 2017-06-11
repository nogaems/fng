__all__ = ['mgtDryads']

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
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('i')<Js(2.0)):
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd5'))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(4.0)):
                        var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6'))))
                    else:
                        var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                while PyJsStrictEq(var.get('nm6').get(var.get('rnd')),var.get('nm7').get(var.get('rnd2'))):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+Js(' '))+var.get('nm8').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('th'), Js('w')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ya'), Js('ae'), Js('ea'), Js('ia'), Js('ye'), Js('ie')]))
var.put('nm3', Js([Js('h'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('v')]))
var.put('nm4', Js([Js('fn'), Js('fr'), Js('hn'), Js('ln'), Js('lm'), Js('ls'), Js('mn'), Js('mr'), Js('nm'), Js('n'), Js('nn'), Js('nr'), Js('ns'), Js('nph'), Js('ph'), Js('r'), Js('rr'), Js('sn'), Js('st'), Js('sh'), Js('th'), Js('thr')]))
var.put('nm5', Js([Js('fn'), Js('fr'), Js('h'), Js('hn'), Js('l'), Js('ll'), Js('lm'), Js('ln'), Js('ls'), Js('m'), Js('mn'), Js('mr'), Js('n'), Js('nn'), Js('nr'), Js('r'), Js('rr'), Js('s'), Js('sn'), Js('sh'), Js('ss'), Js('thr')]))
var.put('nm6', Js([Js('acorn'), Js('alder'), Js('ash'), Js('beech'), Js('birch'), Js('cedar'), Js('cherry'), Js('cypress'), Js('elm'), Js('fir'), Js('juniper'), Js('larch'), Js('locust'), Js('maple'), Js('oak'), Js('peach'), Js('pine'), Js('poplar'), Js('spruce'), Js('walnut'), Js('willow'), Js('yew'), Js('tree'), Js('hazel'), Js('thistle'), Js('autumn'), Js('bare'), Js('bark'), Js('bitter'), Js('blade'), Js('blossom'), Js('bramble'), Js('brow'), Js('bush'), Js('copse'), Js('covert'), Js('dawn'), Js('deep'), Js('fall'), Js('fern'), Js('gentle'), Js('gnarl'), Js('grove'), Js('hard'), Js('heart'), Js('husk'), Js('leaf'), Js('limb'), Js('mild'), Js('nettle'), Js('oak'), Js('pad'), Js('root'), Js('scrub'), Js('shadow'), Js('silver'), Js('snow'), Js('somber'), Js('splinter'), Js('spring'), Js('sprout'), Js('summer'), Js('tangle'), Js('tendril'), Js('thorn'), Js('trunk'), Js('twig'), Js('vine'), Js('wild'), Js('winter'), Js('wise'), Js('worm')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('bark'), Js('bellow'), Js('blade'), Js('blossom'), Js('bramble'), Js('brow'), Js('copse'), Js('covert'), Js('crown'), Js('fern'), Js('fir'), Js('flower'), Js('glade'), Js('grove'), Js('heart'), Js('husk'), Js('leaf'), Js('limb'), Js('limbs'), Js('root'), Js('scrub'), Js('shade'), Js('shrub'), Js('spine'), Js('sprout'), Js('stalk'), Js('stand'), Js('strider'), Js('stump'), Js('tendril'), Js('thorn'), Js('trunk'), Js('twig'), Js('wald'), Js('walker'), Js('wood')]))
var.put('nm8', Js([Js('Chorus'), Js('Dancer'), Js('Dryad'), Js('Dryad'), Js('Dryad'), Js('Dryad'), Js('Dryad'), Js('Dryad'), Js('Elder'), Js('Emissary'), Js('Enchantress'), Js('Guardian'), Js('Legate'), Js('Mage'), Js('Militant'), Js('Naturalist'), Js('Outrider'), Js('Pathfinder'), Js('Ranger'), Js('Scout'), Js('Sentinel'), Js('Sophisticate'), Js('Stalker'), Js('Trickster'), Js('Vanguard'), Js('Walker')]))
pass
pass


# Add lib to the module scope
mgtDryads = var.to_python()
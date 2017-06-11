__all__ = ['mgtTreefolk']

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
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm5').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                if (var.get('i')<Js(2.0)):
                    while ((var.get('rnd3')<Js(6.0)) or PyJsStrictEq(var.get('nm5').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd')))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                else:
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm5').get(var.get('rnd3')),var.get('nm3').get(var.get('rnd4'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(4.0)):
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd3'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm5').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd6'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm6').get(var.get('rnd')),var.get('nm7').get(var.get('rnd2'))):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('names', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+Js(' '))+var.get('nm8').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm10').get(var.get('rnd'))+Js(' '))+var.get('nm9').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('d'), Js('g'), Js('j'), Js('n'), Js('m'), Js('r'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('fr'), Js('g'), Js('gr'), Js('gd'), Js('l'), Js('lg'), Js('ld'), Js('lm'), Js('m'), Js('mn'), Js('ml'), Js('n'), Js('ng'), Js('nd'), Js('nl'), Js('nr'), Js('nz'), Js('r'), Js('rg'), Js('rv'), Js('rd'), Js('rl'), Js('v'), Js('vr'), Js('vl'), Js('z'), Js('zr'), Js('zl')]))
var.put('nm4', Js([Js('d'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('l'), Js('ld'), Js('m'), Js('n'), Js('nd'), Js('nt'), Js('s'), Js('sk'), Js('t'), Js('th')]))
var.put('nm6', Js([Js('alpen'), Js('amber'), Js('autumn'), Js('bark'), Js('blade'), Js('blanch'), Js('bog'), Js('branch'), Js('bristle'), Js('broad'), Js('cloud'), Js('copse'), Js('coven'), Js('crag'), Js('dawn'), Js('dead'), Js('dew'), Js('dun'), Js('dusk'), Js('ever'), Js('far'), Js('fern'), Js('forest'), Js('grand'), Js('grass'), Js('grim'), Js('heart'), Js('husk'), Js('iron'), Js('jade'), Js('leaf'), Js('lumber'), Js('marsh'), Js('meadow'), Js('mirror'), Js('mist'), Js('moss'), Js('needle'), Js('noble'), Js('orb'), Js('petal'), Js('pulp'), Js('root'), Js('rough'), Js('seed'), Js('shade'), Js('shadow'), Js('shrub'), Js('silent'), Js('splinter'), Js('sprig'), Js('stalk'), Js('tall'), Js('thorn'), Js('timber'), Js('weald'), Js('weather'), Js('wicker'), Js('wild'), Js('wood'), Js('young')]))
var.put('nm7', Js([Js('bark'), Js('beard'), Js('blade'), Js('bloom'), Js('blossom'), Js('bough'), Js('bramble'), Js('branch'), Js('breeze'), Js('copse'), Js('covert'), Js('crest'), Js('crown'), Js('dew'), Js('fern'), Js('fir'), Js('glade'), Js('glow'), Js('gnarl'), Js('grove'), Js('knot'), Js('limb'), Js('root'), Js('seed'), Js('shade'), Js('shadow'), Js('shrub'), Js('splint'), Js('splinter'), Js('sprout'), Js('spruce'), Js('stalk'), Js('stand'), Js('trunk'), Js('twig'), Js('ward'), Js('wood')]))
var.put('nm8', Js([Js('Abomination'), Js('Agent'), Js('Ambassador'), Js('Ancient'), Js('Cerberus'), Js('Champion'), Js('Chaperone'), Js('Cohort'), Js('Consul'), Js('Custodian'), Js('Delegate'), Js('Elder'), Js('Emissary'), Js('Envoy'), Js('Forerunner'), Js('Guard'), Js('Guardian'), Js('Harbinger'), Js('Healer'), Js('Keeper'), Js('Mystic'), Js('Oak'), Js('Oberserver'), Js('Oracle'), Js('Patrol'), Js('Prime'), Js('Protector'), Js('Safeguard'), Js('Sage'), Js('Scion'), Js('Seer'), Js('Sentinel'), Js('Shaman'), Js('Shepherd'), Js('Summoner'), Js('Tower'), Js('Treefolk'), Js('Warden'), Js('Warrior'), Js('Watcher'), Js('Acacia'), Js('Alder'), Js('Ash'), Js('Aspen'), Js('Azalea'), Js('Balsa'), Js('Bamboo'), Js('Baobab'), Js('Bayonet'), Js('Beech'), Js('Birch'), Js('Box'), Js('Buckeye'), Js('Buckthorn'), Js('Bunya'), Js('Bush'), Js('Cassava'), Js('Catalpa'), Js('Cedar'), Js('Conifer'), Js('Cycad'), Js('Cypress'), Js('Elder'), Js('Elm'), Js('Eucalyptus'), Js('Fir'), Js('Hawthorn'), Js('Hazel'), Js('Hemlock'), Js('Hickory'), Js('Holly'), Js('Hornbeam'), Js('Juniper'), Js('Larch'), Js('Leaf'), Js('Locust'), Js('Magnolia'), Js('Mahogany'), Js('Mangrove'), Js('Maple'), Js('Medlar'), Js('Milkbark'), Js('Oak'), Js('Oleander'), Js('Palm'), Js('Palmetto'), Js('Persimmon'), Js('Pine'), Js('Poplar'), Js('Privet'), Js('Rhododendron'), Js('Rowan'), Js('Sequoia'), Js('Spruce'), Js('Strongbark'), Js('Sumac'), Js('Sycamore'), Js('Tree'), Js('Viburnum'), Js('Willow'), Js('Wood'), Js('Yew'), Js('Yucca')]))
var.put('nm9', Js([Js('Abomination'), Js('Agent'), Js('Ambassador'), Js('Ancient'), Js('Cerberus'), Js('Champion'), Js('Chaperone'), Js('Cohort'), Js('Consul'), Js('Custodian'), Js('Delegate'), Js('Elder'), Js('Emissary'), Js('Envoy'), Js('Forerunner'), Js('Guard'), Js('Guardian'), Js('Harbinger'), Js('Healer'), Js('Keeper'), Js('Mystic'), Js('Oak'), Js('Oberserver'), Js('Oracle'), Js('Patrol'), Js('Prime'), Js('Protector'), Js('Safeguard'), Js('Sage'), Js('Scion'), Js('Seer'), Js('Sentinel'), Js('Shaman'), Js('Shepherd'), Js('Summoner'), Js('Tower'), Js('Treefolk'), Js('Warden'), Js('Warrior'), Js('Watcher')]))
var.put('nm10', Js([Js('Acacia'), Js('Alder'), Js('Ash'), Js('Aspen'), Js('Azalea'), Js('Balsa'), Js('Bamboo'), Js('Baobab'), Js('Bayonet'), Js('Beech'), Js('Birch'), Js('Box'), Js('Buckeye'), Js('Buckthorn'), Js('Bunya'), Js('Bush'), Js('Cassava'), Js('Catalpa'), Js('Cedar'), Js('Conifer'), Js('Cycad'), Js('Cypress'), Js('Elder'), Js('Elm'), Js('Eucalyptus'), Js('Fir'), Js('Hawthorn'), Js('Hazel'), Js('Hemlock'), Js('Hickory'), Js('Holly'), Js('Hornbeam'), Js('Juniper'), Js('Larch'), Js('Leaf'), Js('Locust'), Js('Magnolia'), Js('Mahogany'), Js('Mangrove'), Js('Maple'), Js('Medlar'), Js('Milkbark'), Js('Oak'), Js('Oleander'), Js('Palm'), Js('Palmetto'), Js('Persimmon'), Js('Pine'), Js('Poplar'), Js('Privet'), Js('Rhododendron'), Js('Rowan'), Js('Sequoia'), Js('Spruce'), Js('Strongbark'), Js('Sumac'), Js('Sycamore'), Js('Tree'), Js('Viburnum'), Js('Willow'), Js('Wood'), Js('Yew'), Js('Yucca')]))
pass
pass


# Add lib to the module scope
mgtTreefolk = var.to_python()
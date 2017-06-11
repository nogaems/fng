__all__ = ['dragonNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            var.put('rnd16', ((var.get('Math').callprop('random')*var.get('nm16').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm6').get(var.get('rnd')),var.get('nm8').get(var.get('rnd3'))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm10').get(var.get('rnd5')),var.get('nm8').get(var.get('rnd3'))):
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                if (var.get('i')<Js(7.0)):
                    var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+Js(', '))+var.get('nm16').get(var.get('rnd16'))))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm8').get(var.get('rnd3'))):
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('names', ((((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd5')))+Js(', '))+var.get('nm16').get(var.get('rnd16'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm11').get(var.get('rnd')),var.get('nm13').get(var.get('rnd3'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm15').get(var.get('rnd5')),var.get('nm13').get(var.get('rnd3'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd5')))+Js(', '))+var.get('nm16').get(var.get('rnd16'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm13').get(var.get('rnd3'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                        var.put('names', ((((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm15').get(var.get('rnd5')))+Js(', '))+var.get('nm16').get(var.get('rnd16'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm5').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('nm16').get(var.get('rnd16'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('nm16').get(var.get('rnd16'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('fr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('t'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('u'), Js('u'), Js('u'), Js('u'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('ai'), Js('ay'), Js('ei'), Js('eo'), Js('ia'), Js('ie'), Js('oi')]))
var.put('nm3', Js([Js('d'), Js('ddr'), Js('dr'), Js('g'), Js('gh'), Js('k'), Js('lb'), Js('ldr'), Js('lr'), Js('lzr'), Js('m'), Js('mb'), Js('mm'), Js('mr'), Js('n'), Js('nd'), Js('ndr'), Js('nn'), Js('r'), Js('rd'), Js('rg'), Js('rr'), Js('rs'), Js('rv'), Js('s'), Js('t'), Js('th'), Js('v'), Js('vr'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js('cr'), Js('d'), Js('n'), Js('nt'), Js('r'), Js('rr'), Js('sd')]))
var.put('nm5', Js([Js(''), Js(''), Js('d'), Js('g'), Js('m'), Js('n'), Js('nth'), Js('r'), Js('rth'), Js('s'), Js('ss'), Js('t')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('f'), Js('fr'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('v'), Js('z')]))
var.put('nm7', Js([Js('u'), Js('u'), Js('u'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('ae'), Js('ai'), Js('ay'), Js('ei'), Js('eo'), Js('ie'), Js('io'), Js('oa')]))
var.put('nm8', Js([Js('d'), Js('dh'), Js('g'), Js('gh'), Js('k'), Js('ldr'), Js('ll'), Js('m'), Js('mm'), Js('mr'), Js('n'), Js('nd'), Js('ndr'), Js('nn'), Js('p'), Js('ph'), Js('r'), Js('rg'), Js('rl'), Js('rm'), Js('rr'), Js('rs'), Js('rv'), Js('s'), Js('ss'), Js('t'), Js('th'), Js('v'), Js('vn'), Js('z'), Js('zz')]))
var.put('nm9', Js([Js('d'), Js('l'), Js('n'), Js('nt'), Js('ph'), Js('r'), Js('rr'), Js('ss')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('l'), Js('lth'), Js('n'), Js('nth'), Js('r'), Js('rth'), Js('s'), Js('ss'), Js('t'), Js('th')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('fr'), Js('g'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('z')]))
var.put('nm12', Js([Js('u'), Js('u'), Js('u'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('ae'), Js('ai'), Js('ay'), Js('ei'), Js('eo'), Js('ia'), Js('ie'), Js('io'), Js('oa'), Js('oi')]))
var.put('nm13', Js([Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gh'), Js('k'), Js('l'), Js('ldr'), Js('ll'), Js('lr'), Js('m'), Js('mm'), Js('mr'), Js('n'), Js('nd'), Js('ndr'), Js('nn'), Js('p'), Js('ph'), Js('r'), Js('rl'), Js('rm'), Js('rr'), Js('rs'), Js('rv'), Js('s'), Js('ss'), Js('t'), Js('th'), Js('v'), Js('vn'), Js('vr'), Js('z'), Js('zz')]))
var.put('nm14', Js([Js('d'), Js('l'), Js('n'), Js('nt'), Js('ph'), Js('r'), Js('rr'), Js('ss')]))
var.put('nm15', Js([Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('l'), Js('lth'), Js('n'), Js('nth'), Js('r'), Js('rth'), Js('s'), Js('ss'), Js('t'), Js('th')]))
var.put('nm16', Js([Js('the Nocturnal'), Js('the Protective'), Js('the Clever'), Js('the Bright'), Js('the Dark'), Js('the Dark One'), Js('the Dark'), Js('the Eternal'), Js('the Firestarter'), Js('the Eternal One'), Js('the Calm'), Js('the Gentle'), Js('the Redeemer'), Js('the Champion'), Js('the Evil One'), Js('the Chosen'), Js('the Great'), Js('the Kind'), Js('the Fierce'), Js('the Strong'), Js('the Tiran'), Js('the Dragonlord'), Js('the Warrior'), Js('the Barbarian'), Js('the Tall'), Js('the Magnificent'), Js('the Clean'), Js('the Adorable'), Js('the Gifted'), Js('the Tender'), Js('the Powerful One'), Js('the Gifted One'), Js('the Powerful'), Js('the Black'), Js('the White'), Js('the White One'), Js('the Careful'), Js('the Clumsy One'), Js('the Grumpy'), Js('the Jealous One'), Js('the Mysterious'), Js('the Mysterious One'), Js('the Scary'), Js('the Scary One'), Js('the Brave'), Js('the Victorious'), Js('the Skinny One'), Js('the Mammoth'), Js('the Puny'), Js('the Quiet'), Js('the Voiceless'), Js('the Loud'), Js('the Voiceless One'), Js('the Fast One'), Js('the Swift'), Js('the Young One'), Js('the Youngling'), Js('the Slow'), Js('the Creep'), Js('the Warm'), Js('Warmheart'), Js('Braveheart'), Js('Gentleheart'), Js('the Strong Minded'), Js('the Stubborn'), Js('Firebreath'), Js('Icebreath'), Js('the Squeeler'), Js('Champion of Dragons'), Js('Eternal Fire'), Js('Gentle Mind'), Js('Longtail'), Js('Redeemer of Men'), Js('Protector of the Weak'), Js('Protector of the Forest'), Js('Protector of the Sky'), Js('Lord of the Skies'), Js('Champion of the Skies'), Js('Champion of Men'), Js('Lord of Fire'), Js('Lord of Ice'), Js('Lord of the Red'), Js('Lord of the Black'), Js('Lord of the White'), Js('Lord of the Blue'), Js('Lord of the Green'), Js('Lord of the Yellow'), Js('Lord of the Brown'), Js('Champion of the Red'), Js('Champion of the White'), Js('Champion of the Black'), Js('Champion of the Blue'), Js('Champion of the Yellow'), Js('Champion of the Brown'), Js('Champion of the Green'), Js('Protector of Creatures'), Js('Protector of Life'), Js('Giver of Life'), Js('Bringer of Death'), Js('the Deathlord'), Js('the Dead'), Js('Destroyer of Life'), Js('Destroyer of Men'), Js('Eater of Sheep'), Js('Eater of All'), Js('the Hungry'), Js('Eater of Bunnies'), Js('the Bunny Killer'), Js('the Rabbit Slayer'), Js('the Taker of Life'), Js('the Insane'), Js('the Life Giver')]))
pass
pass


# Add lib to the module scope
dragonNames = var.to_python()
__all__ = ['witcherElfs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7'))))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    if (var.get('rnd4')<Js(20.0)):
                        var.put('rnd5', Js(0.0))
                        var.put('rnd6', Js(0.0))
                    else:
                        while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7'))))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('rnd4')<Js(30.0)):
                        var.put('rnd5', Js(0.0))
                        var.put('rnd6', Js(0.0))
                    else:
                        while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('cr'), Js('d'), Js('f'), Js('g'), Js('h'), Js('m'), Js('r'), Js('s'), Js('t'), Js('v'), Js('vr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('oi'), Js('au'), Js('ai'), Js('ei'), Js('ae'), Js('ea'), Js('io')]))
var.put('nm3', Js([Js('b'), Js('bh'), Js('ch'), Js('d'), Js('dr'), Js('h'), Js('l'), Js('m'), Js('md'), Js('ml'), Js('mm'), Js('n'), Js('nd'), Js('ndr'), Js('ng'), Js('ngr'), Js('nl'), Js('nn'), Js('r'), Js('rbr'), Js('rd'), Js('rl'), Js('rn'), Js('rrd'), Js('rv'), Js('s'), Js('v')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('oi'), Js('au'), Js('ai'), Js('ei'), Js('ae'), Js('ea'), Js('io')]))
var.put('nm5', Js([Js(''), Js('b'), Js('bh'), Js('ch'), Js('d'), Js('dr'), Js('h'), Js('l'), Js('m'), Js('md'), Js('ml'), Js('mm'), Js('n'), Js('nd'), Js('ndr'), Js('ng'), Js('ngr'), Js('nl'), Js('nn'), Js('r'), Js('rbr'), Js('rd'), Js('rl'), Js('rn'), Js('rrd'), Js('rv'), Js('s'), Js('v')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js('d'), Js('r'), Js('s'), Js('n'), Js('c'), Js('ch'), Js('l'), Js('rr'), Js('th'), Js('m'), Js('nn')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sr'), Js('sh'), Js('t'), Js('th'), Js('v')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ie'), Js('ee'), Js('io'), Js('ua'), Js('ia')]))
var.put('nm10', Js([Js('d'), Js('dh'), Js('fr'), Js('f'), Js('ff'), Js('gl'), Js('gh'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('nn'), Js('nr'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('th'), Js('thl'), Js('tt'), Js('t'), Js('tl'), Js('v')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ie'), Js('ee'), Js('io'), Js('ua'), Js('ia')]))
var.put('nm12', Js([Js(''), Js('d'), Js('dh'), Js('fr'), Js('f'), Js('ff'), Js('gl'), Js('gh'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('nn'), Js('nr'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('th'), Js('thl'), Js('tt'), Js('t'), Js('tl'), Js('v')]))
var.put('nm14', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('nn'), Js('n'), Js('l'), Js('s'), Js('sh')]))
pass
pass


# Add lib to the module scope
witcherElfs = var.to_python()
__all__ = ['swOrtolanNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm8').get(var.get('rnd3')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(2.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd3')<Js(3.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd3')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js('b'), Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('t'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('ee'), Js('oo')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('br'), Js('bn'), Js('d'), Js('dn'), Js('dr'), Js('dd'), Js('j'), Js('l'), Js('lb'), Js('lbr'), Js('ldr'), Js('lr'), Js('lm'), Js('ln'), Js('ld'), Js('md'), Js('ml'), Js('mdr'), Js('md'), Js('mr'), Js('mm'), Js('mn'), Js('ndr'), Js('n'), Js('nn'), Js('nl'), Js('nd'), Js('nb'), Js('r'), Js('rl'), Js('rn'), Js('rm'), Js('rd'), Js('rb')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('b'), Js('g'), Js('gh'), Js('j'), Js('k'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('t'), Js('tz'), Js('x')]))
var.put('nm5', Js([Js(''), Js(''), Js('b'), Js('bh'), Js('bl'), Js('f'), Js('fl'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sl'), Js('w')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o')]))
var.put('nm7', Js([Js('bk'), Js('b'), Js('bb'), Js('bn'), Js('bl'), Js('bs'), Js('bh'), Js('d'), Js('dd'), Js('dn'), Js('dl'), Js('f'), Js('ff'), Js('fl'), Js('fr'), Js('h'), Js('hh'), Js('l'), Js('ll'), Js('lm'), Js('lr'), Js('ln'), Js('ld'), Js('m'), Js('mm'), Js('ml'), Js('md'), Js('mn'), Js('ms'), Js('n'), Js('nn'), Js('nl'), Js('ns'), Js('nm'), Js('ph'), Js('phl'), Js('phn'), Js('t'), Js('th'), Js('tl'), Js('tn'), Js('ts')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('n'), Js('m'), Js('s'), Js('ss'), Js('th')]))
var.put('nm9', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sr'), Js('t'), Js('v')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('ee'), Js('oo'), Js('ai')]))
var.put('nm11', Js([Js('b'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('t'), Js('v')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('x')]))
pass
pass


# Add lib to the module scope
swOrtolanNames = var.to_python()
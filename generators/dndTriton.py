__all__ = ['dndTriton']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nameFem', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nameMas', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameFem_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
    while PyJsStrictEq(var.get('nm6').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd'))):
        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
    if (var.get('i')<Js(5.0)):
        var.put('nFm', ((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm8').get(var.get('rnd4')))+Js('n')))
    else:
        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
        while PyJsStrictEq(var.get('nm7').get(var.get('rnd6')),var.get('nm6').get(var.get('rnd3'))):
            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
        var.put('nFm', ((((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd4')))+Js('n')))
    var.get('testSwear')(var.get('nFm'))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('nMs', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd2')))+Js('s')))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameMas_.func_name = 'nameMas'
var.put('nameMas', PyJsHoisted_nameMas_)
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
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
            while (PyJsStrictEq(var.get('nm11').get(var.get('rnd3')),var.get('nm9').get(var.get('rnd'))) or (var.get('nm11').get(var.get('rnd3'))==var.get('nm13').get(var.get('rnd5')))):
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
            var.put('nSr', (((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd5')))+Js('ath')))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.get('nameFem')()
                while PyJsStrictEq(var.get('nFm'),Js('')):
                    var.get('nameFem')()
                var.put('names', ((var.get('nFm')+Js(' '))+var.get('nSr')))
            else:
                var.get('nameMas')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameMas')()
                var.put('names', ((var.get('nMs')+Js(' '))+var.get('nSr')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('d'), Js('dh'), Js('j'), Js('jh'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('dd'), Js('g'), Js('gl'), Js('hn'), Js('hl'), Js('hr'), Js('l'), Js('lg'), Js('lm'), Js('ld'), Js('ln'), Js('lz'), Js('m'), Js('mn'), Js('mr'), Js('n'), Js('nn'), Js('nd'), Js('nl'), Js('nr'), Js('nv'), Js('r'), Js('rl'), Js('rn'), Js('rv'), Js('rz'), Js('v'), Js('vn'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('d'), Js('dh'), Js('f'), Js('fl'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('vl'), Js('w'), Js('wh'), Js('y')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('i')]))
var.put('nm6', Js([Js('d'), Js('dd'), Js('dr'), Js('gr'), Js('gl'), Js('hl'), Js('hn'), Js('l'), Js('lr'), Js('lt'), Js('lth'), Js('ml'), Js('nl'), Js('nth'), Js('nr'), Js('r'), Js('rn'), Js('rl'), Js('rr'), Js('s'), Js('sh'), Js('st'), Js('sl'), Js('sn'), Js('t'), Js('th'), Js('tr'), Js('thr'), Js('tl'), Js('thl')]))
var.put('nm7', Js([Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r')]))
var.put('nm8', Js([Js('e'), Js('y'), Js('y'), Js('y'), Js('y'), Js('y'), Js('y')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('d'), Js('dh'), Js('j'), Js('g'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('v'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('u'), Js('a'), Js('u'), Js('a'), Js('u'), Js('e'), Js('o')]))
var.put('nm11', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('hl'), Js('hn'), Js('hm'), Js('hr'), Js('l'), Js('n'), Js('m'), Js('r'), Js('v')]))
var.put('nm12', Js([Js('a'), Js('o'), Js('a'), Js('o'), Js('e'), Js('u')]))
var.put('nm13', Js([Js('d'), Js('g'), Js('l'), Js('ll'), Js('ln'), Js('lm'), Js('lv'), Js('m'), Js('mn'), Js('n'), Js('ns'), Js('nz'), Js('r'), Js('rs'), Js('s'), Js('sn'), Js('x'), Js('z')]))
pass
pass
pass
pass


# Add lib to the module scope
dndTriton = var.to_python()
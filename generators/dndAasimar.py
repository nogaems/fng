__all__ = ['dndAasimar']

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
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
    if (var.get('i')<Js(6.0)):
        while (PyJsStrictEq(var.get('nm9').get(var.get('rnd3')),var.get('nm7').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm9').get(var.get('rnd3')),var.get('nm13').get(var.get('rnd5')))):
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
        var.put('nMs', ((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd5'))))
    else:
        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
        while (PyJsStrictEq(var.get('nm11').get(var.get('rnd6')),var.get('nm9').get(var.get('rnd3'))) or PyJsStrictEq(var.get('nm11').get(var.get('rnd6')),var.get('nm13').get(var.get('rnd5')))):
            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
        var.put('nMs', ((((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm13').get(var.get('rnd5'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
    if (var.get('i')<Js(6.0)):
        while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd5')))):
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
        var.put('nMs', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
    else:
        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        while (PyJsStrictEq(var.get('nm5').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))) or PyJsStrictEq(var.get('nm5').get(var.get('rnd6')),var.get('nm6').get(var.get('rnd5')))):
            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
        var.put('nMs', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd5'))))
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.get('nameFem')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameFem')()
            else:
                var.get('nameMas')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameMas')()
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('cr'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('au'), Js('ai'), Js('ea'), Js('ei')]))
var.put('nm3', Js([Js('d'), Js('dr'), Js('g'), Js('gg'), Js('gr'), Js('gw'), Js('k'), Js('kr'), Js('kl'), Js('l'), Js('ld'), Js('lg'), Js('lw'), Js('lr'), Js('lt'), Js('n'), Js('nr'), Js('nw'), Js('nl'), Js('r'), Js('rn'), Js('rr'), Js('rw'), Js('rl'), Js('v'), Js('vr'), Js('w')]))
var.put('nm4', Js([Js('a'), Js('i'), Js('a'), Js('i'), Js('a'), Js('i'), Js('a'), Js('i'), Js('a'), Js('i'), Js('a'), Js('i'), Js('e'), Js('a'), Js('i'), Js('e'), Js('a'), Js('i'), Js('e'), Js('o'), Js('o'), Js('u'), Js('u'), Js('ee'), Js('ia'), Js('ie'), Js('ai'), Js('ei')]))
var.put('nm5', Js([Js('d'), Js('l'), Js('m'), Js('n'), Js('t'), Js('v')]))
var.put('nm6', Js([Js('l'), Js('m'), Js('n'), Js('nt'), Js('r')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('br'), Js('d'), Js('dr'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('rh'), Js('th'), Js('v'), Js('w'), Js('z')]))
var.put('nm8', Js([Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('e'), Js('e'), Js('ia'), Js('io'), Js('ea'), Js('eo')]))
var.put('nm9', Js([Js('d'), Js('j'), Js('l'), Js('ld'), Js('ldr'), Js('lv'), Js('ll'), Js('lt'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('nr'), Js('nv'), Js('nl'), Js('ndr'), Js('nm'), Js('r'), Js('rd'), Js('rk'), Js('rs'), Js('s'), Js('sr'), Js('sl'), Js('v')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ea'), Js('ia'), Js('ie')]))
var.put('nm11', Js([Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('z')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('au'), Js('ou'), Js('oe')]))
var.put('nm13', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('m'), Js('n'), Js('r')]))
pass
pass
pass
pass


# Add lib to the module scope
dndAasimar = var.to_python()
__all__ = ['starTrekRomulans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                if PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                    var.put('rnd6', Js(0.0))
                var.put('names', (((((var.get('nm7').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                    var.put('rnd6', Js(0.0))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('ch'), Js('c'), Js('d'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('vr'), Js('x'), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('chr'), Js('j'), Js('k'), Js('l'), Js('j'), Js('k'), Js('l'), Js('lm'), Js('ld'), Js('m'), Js('m'), Js('ns'), Js('nd'), Js('ncl'), Js('r'), Js('r'), Js('rr'), Js('t'), Js('t'), Js('v')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('ee'), Js('iu')]))
var.put('nm5', Js([Js(''), Js('b'), Js('hk'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th'), Js('x')]))
var.put('nm6', Js([Js(''), Js('a'), Js('e'), Js('o'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js('b'), Js('c'), Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v')]))
var.put('nm8', Js([Js('h'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('rr'), Js('t'), Js('tr'), Js('th'), Js('v')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ee')]))
var.put('nm10', Js([Js(''), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('th')]))
var.put('nm11', Js([Js(''), Js('a'), Js('a')]))
pass
pass


# Add lib to the module scope
starTrekRomulans = var.to_python()
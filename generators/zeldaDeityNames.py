__all__ = ['zeldaDeityNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('rnd2')>Js(4.0)):
                    while (var.get('rnd4')>Js(4.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if ((var.get('rnd2')>Js(4.0)) or (var.get('rnd4')>Js(4.0))):
                        while (var.get('rnd6')>Js(4.0)):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('cl'), Js('d'), Js('g'), Js('gr'), Js('gn'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('ld'), Js('ll'), Js('ln'), Js('lm'), Js('m'), Js('mn'), Js('n'), Js('ph'), Js('r'), Js('v'), Js('vr'), Js('z'), Js('zr'), Js('b'), Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z'), Js('b'), Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm4', Js([Js('u'), Js('oo'), Js('ia'), Js('a'), Js('e'), Js('ai'), Js('i'), Js('o')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('n'), Js('m'), Js('r'), Js('s')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('h'), Js('l'), Js('n'), Js('m'), Js('ph'), Js('s'), Js('sh'), Js('t'), Js('v')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('y'), Js('ay'), Js('ie'), Js('ia'), Js('ea')]))
var.put('nm8', Js([Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('rd'), Js('s'), Js('th'), Js('v'), Js('r')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('n'), Js('h')]))
pass
pass


# Add lib to the module scope
zeldaDeityNames = var.to_python()
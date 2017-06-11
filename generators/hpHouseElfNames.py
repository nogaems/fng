__all__ = ['hpHouseElfNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if PyJsStrictEq(var.get('rnd2'),Js(0.0)):
                    var.put('rnd3', Js(0.0))
                else:
                    while PyJsStrictEq(var.get('rnd3'),Js(0.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                if PyJsStrictEq(var.get('rnd2'),Js(0.0)):
                    var.put('rnd3', Js(0.0))
                else:
                    while PyJsStrictEq(var.get('rnd3'),Js(0.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('C'), Js('D'), Js('F'), Js('G'), Js('H'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('P'), Js('R'), Js('S'), Js('T'), Js('V'), Js('W'), Js('Z')]))
var.put('nm2', Js([Js('oo'), Js('a'), Js('o')]))
var.put('nm3', Js([Js(''), Js('d'), Js('n'), Js('r'), Js('l'), Js('b'), Js('k')]))
var.put('nm4', Js([Js('b'), Js('d'), Js('k'), Js('p'), Js('r')]))
var.put('nm5', Js([Js('y'), Js('ey')]))
var.put('nm6', Js([Js('ee'), Js('i'), Js('o')]))
var.put('nm7', Js([Js(''), Js('n'), Js('s'), Js('l'), Js('b'), Js('m'), Js('p')]))
var.put('nm8', Js([Js('k'), Js('n'), Js('s'), Js('l'), Js('m'), Js('p')]))
pass
pass


# Add lib to the module scope
hpHouseElfNames = var.to_python()
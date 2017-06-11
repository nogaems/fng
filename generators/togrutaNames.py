__all__ = ['togrutaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm0', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                var.put('lName', ((((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd3')))+var.get('nm15').get(var.get('rnd4')))+var.get('nm16').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                var.put('lName', ((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+var.get('nm16').get(var.get('rnd5'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('names', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd6')))+Js(' '))+var.get('lName')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm0').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', (((((((var.get('nm0').get(var.get('rnd'))+var.get('nm1').get(var.get('rnd1')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm0', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('o'), Js('u')]))
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('h'), Js('k'), Js('m'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('d'), Js('k'), Js('kr'), Js('ky'), Js('l'), Js('n'), Js('nz'), Js('r'), Js('rh'), Js('s'), Js('sht'), Js('t'), Js('vr'), Js('z')]))
var.put('nm4', Js([Js('a'), Js('aa'), Js('ee'), Js('i'), Js('o'), Js('y')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('hd'), Js('k'), Js('n'), Js('m'), Js('r'), Js('s'), Js('sh')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js('a'), Js('a'), Js('o'), Js('a')]))
var.put('nm7', Js([Js('b'), Js('c'), Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('z')]))
var.put('nm8', Js([Js('a'), Js('aa'), Js('e'), Js('o')]))
var.put('nm9', Js([Js('d'), Js('hn'), Js('hl'), Js('hs'), Js('k'), Js('l'), Js('m'), Js('mn'), Js('n'), Js('r'), Js('rl'), Js('rsh'), Js('rn'), Js('s'), Js('ss'), Js('sh'), Js('shl'), Js('t'), Js('th'), Js('tt')]))
var.put('nm10', Js([Js('a'), Js('aa'), Js('a'), Js('a'), Js('o')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('n'), Js('m'), Js('h'), Js('s'), Js('sh')]))
var.put('nm12', Js([Js('b'), Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm13', Js([Js('a'), Js('y'), Js('aa'), Js('i'), Js('e')]))
var.put('nm14', Js([Js('br'), Js('d'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('r'), Js('rn'), Js('rl'), Js('s'), Js('ss'), Js('sh'), Js('shr'), Js('vr'), Js('w'), Js('z')]))
var.put('nm15', Js([Js('a'), Js('aa'), Js('e'), Js('u'), Js('y'), Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('o'), Js('ii'), Js('ua'), Js('ee')]))
var.put('nm16', Js([Js(''), Js(''), Js(''), Js(''), Js('ks'), Js('l'), Js('n'), Js('m'), Js('r'), Js('s'), Js('sh')]))
pass
pass


# Add lib to the module scope
togrutaNames = var.to_python()
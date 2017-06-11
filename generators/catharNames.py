__all__ = ['catharNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rn', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rn2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                var.put('rn3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rn4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('rn5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rn6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                var.put('lName', (((((var.get('nm10').get(var.get('rn'))+var.get('nm14').get(var.get('rn2')))+var.get('nm11').get(var.get('rn3')))+var.get('nm12').get(var.get('rn4')))+var.get('nm11').get(var.get('rn5')))+var.get('nm13').get(var.get('rn6'))))
            else:
                var.put('rn', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rn2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                var.put('rn5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rn6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                var.put('lName', (((var.get('nm10').get(var.get('rn'))+var.get('nm14').get(var.get('rn2')))+var.get('nm11').get(var.get('rn5')))+var.get('nm13').get(var.get('rn6'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('names', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+Js(' '))+var.get('lName')))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((((var.get('nm2').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+Js(' '))+var.get('lName')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js('a'), Js('u'), Js('y'), Js('i')]))
var.put('nm2', Js([Js('c'), Js('cr'), Js('h'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('x')]))
var.put('nm3', Js([Js('a'), Js('i'), Js('o'), Js('y'), Js('u')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('k'), Js('m'), Js('n'), Js('nd'), Js('r'), Js('rb'), Js('s')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('h'), Js('hr'), Js('k'), Js('m'), Js('n'), Js('rr'), Js('x')]))
var.put('nm6', Js([Js('c'), Js('ch'), Js('d'), Js('j'), Js('m'), Js('n'), Js('r'), Js('s'), Js('th'), Js('x')]))
var.put('nm7', Js([Js('h'), Js('l'), Js('lv'), Js('m'), Js('n'), Js('r'), Js('s'), Js('th'), Js('v'), Js('sh'), Js('w')]))
var.put('nm8', Js([Js('r'), Js('h'), Js('s'), Js('n'), Js('hr'), Js('x'), Js('sh'), Js('z')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js('a'), Js('i'), Js('y')]))
var.put('nm10', Js([Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t')]))
var.put('nm11', Js([Js('i'), Js('o'), Js('a'), Js('u')]))
var.put('nm12', Js([Js('d'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('rg'), Js('z')]))
var.put('nm13', Js([Js(''), Js(''), Js(''), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm14', Js([Js(''), Js(''), Js(''), Js('h')]))
pass
pass


# Add lib to the module scope
catharNames = var.to_python()
__all__ = ['miralukaNames']

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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd2b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', ((((((var.get('nm7').get(var.get('rnd1'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd2b')))+var.get('nm8').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6'))))
            else:
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd1'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd2b')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js('B'), Js('Ch'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('i'), Js('a'), Js('o'), Js('e'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('i'), Js('a'), Js('o'), Js('e'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('c'), Js('d'), Js('f'), Js('h'), Js('hr'), Js('hk'), Js('hl'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('rr'), Js('rth'), Js('s'), Js('t'), Js('th'), Js('y')]))
var.put('nm7', Js([Js('A'), Js('B'), Js('Ch'), Js('D'), Js('E'), Js('F'), Js('Fl'), Js('G'), Js('Gl'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('R'), Js('S'), Js('Sh'), Js('Sl'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z')]))
var.put('nm8', Js([Js('i'), Js('a'), Js('o'), Js('e'), Js('u'), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
miralukaNames = var.to_python()
__all__ = ['swDugNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd2b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd2d', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd2e', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('namelast', (((((var.get('nm3').get(var.get('rnd5'))+var.get('nm2').get(var.get('rnd2d')))+var.get('nm3').get(var.get('rnd3c')))+var.get('nm2').get(var.get('rnd2e')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd6'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd2b')))+var.get('nm4').get(var.get('rnd4')))+Js(' '))+var.get('namelast')))
            else:
                var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2c', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd2b')))+var.get('nm3').get(var.get('rnd3b')))+var.get('nm2').get(var.get('rnd2c')))+Js(' '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('d'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ei'), Js('ou'), Js('aa'), Js('ai')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bh'), Js('d'), Js('dd'), Js('dw'), Js('g'), Js('gn'), Js('gr'), Js('gw'), Js('gg'), Js('k'), Js('kw'), Js('kh'), Js('ln'), Js('lw'), Js('lg'), Js('lb'), Js('lt'), Js('nr'), Js('nb'), Js('nd'), Js('ng'), Js('ns'), Js('rd'), Js('r'), Js('rg'), Js('rn'), Js('s'), Js('sw'), Js('ss'), Js('w')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('d'), Js('hx'), Js('n'), Js('s'), Js('x')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v')]))
var.put('nm6', Js([Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm7', Js([Js('d'), Js('n'), Js('r'), Js('s')]))
pass
pass


# Add lib to the module scope
swDugNames = var.to_python()
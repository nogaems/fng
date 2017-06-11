__all__ = ['swBithNames']

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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            if (var.get('i')<Js(5.0)):
                while (var.get('rnd10')<Js(4.0)):
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('namelast', (((var.get('nm8').get(var.get('rnd6'))+var.get('nm9').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm12').get(var.get('rnd11'))))
            else:
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('namelast', ((((var.get('nm8').get(var.get('rnd6'))+var.get('nm9').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd8')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(8.0)):
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd2b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd3b')))+var.get('nm2').get(var.get('rnd2b')))+var.get('nm7').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(8.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd2b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd3b')))+var.get('nm2').get(var.get('rnd2b')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('d'), Js("d'r"), Js('f'), Js("f't"), Js('g'), Js("g'h"), Js('h'), Js('j'), Js('k'), Js('ph'), Js("ph't"), Js('r'), Js('th')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oo'), Js('eu'), Js('ia'), Js('aa')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('c'), Js('cr'), Js('d'), Js('dd'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('lk'), Js('ll'), Js('mk'), Js('m'), Js('n'), Js('nk'), Js('p'), Js('pp'), Js('r'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('l'), Js('m'), Js('n'), Js('ns'), Js('r'), Js('s'), Js('ss'), Js('w')]))
var.put('nm5', Js([Js('d'), Js("d'h"), Js('f'), Js("f'h"), Js('g'), Js("g'h"), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('rh'), Js("r'h"), Js('th')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('dh'), Js('g'), Js('gr'), Js('h'), Js('l'), Js('lm'), Js('ln'), Js('ls'), Js('m'), Js('mn'), Js('ml'), Js('md'), Js('mm'), Js('n'), Js('nn'), Js('nr'), Js('nl'), Js('nd'), Js('r'), Js('s'), Js('sh'), Js('th'), Js('v'), Js('z')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('ss')]))
var.put('nm8', Js([Js('d'), Js("d'"), Js('f'), Js('g'), Js("g'h"), Js('h'), Js('j'), Js('k'), Js("k's"), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('rh'), Js("r'h"), Js('th')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm10', Js([Js('b'), Js('d'), Js('dh'), Js('g'), Js('gr'), Js('h'), Js('l'), Js('lr'), Js('lm'), Js('m'), Js('mn'), Js('md'), Js('mm'), Js('n'), Js('nn'), Js('nr'), Js('nd'), Js('nt'), Js('r'), Js('rt'), Js('rl'), Js('rd'), Js('s'), Js('sh'), Js('th'), Js('v'), Js('z')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js('l'), Js('m'), Js('n'), Js('r'), Js('rn'), Js('s'), Js('ss')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
pass
pass


# Add lib to the module scope
swBithNames = var.to_python()
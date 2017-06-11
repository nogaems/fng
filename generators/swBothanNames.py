__all__ = ['swBothanNames']

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
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            var.put('namelast', (((((var.get('nm8').get(var.get('rnd6'))+var.get('nm9').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd8')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm12').get(var.get('rnd11'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(7.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(7.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('n'), Js('r'), Js('tr'), Js('v'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('aa'), Js('ee'), Js('ai'), Js('ia')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('c'), Js('ct'), Js('d'), Js('dr'), Js('g'), Js('h'), Js('kr'), Js('k'), Js('m'), Js('nt'), Js('r'), Js('ry'), Js('tr'), Js('v')]))
var.put('nm4', Js([Js('c'), Js('g'), Js('gt'), Js('k'), Js('m'), Js('n'), Js('r'), Js('rc'), Js('rd'), Js('rsk'), Js('sc'), Js('sk'), Js('st'), Js('th')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('dh'), Js('g'), Js('gn'), Js('gl'), Js('h'), Js('k'), Js('kn'), Js('l'), Js('m'), Js('n'), Js('s'), Js('th'), Js('v'), Js('y')]))
var.put('nm6', Js([Js('c'), Js('g'), Js('h'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('nt'), Js('nd'), Js('q'), Js('qh'), Js('r'), Js('rr'), Js('s'), Js('t'), Js('th'), Js('tr'), Js('v')]))
var.put('nm7', Js([Js('h'), Js('l'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('t'), Js('th')]))
var.put('nm8', Js([Js('bw'), Js('d'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('s'), Js('tr'), Js('v')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('aa'), Js('ee'), Js('ai'), Js('ia'), Js('ua'), Js('ea')]))
var.put('nm10', Js([Js('d'), Js("d'h"), Js("f'l"), Js("'f"), Js("h'r"), Js('h'), Js("'h"), Js('k'), Js("'k"), Js('l'), Js("'l"), Js('n'), Js("n'd"), Js('nr'), Js("n'q"), Js('nd'), Js("n'n"), Js('q'), Js('r'), Js('rr'), Js("'r"), Js('s'), Js("s'"), Js("'t"), Js('t'), Js('th'), Js("v'"), Js("y'l")]))
var.put('nm11', Js([Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
pass
pass


# Add lib to the module scope
swBothanNames = var.to_python()
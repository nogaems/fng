__all__ = ['zeldaGerudoNames']

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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('C'), Js('D'), Js('G'), Js('H'), Js('K'), Js('M'), Js('R'), Js('T')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z'), Js('b'), Js('d'), Js('f'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z'), Js('b'), Js('d'), Js('f'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z'), Js('b'), Js('d'), Js('f'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z'), Js('b'), Js('d'), Js('f'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z'), Js('br'), Js('bl'), Js('dr'), Js('dl'), Js('fl'), Js('fn'), Js('fm'), Js('fr'), Js('gr'), Js('gn'), Js('gm'), Js('lb'), Js('ld'), Js('lg'), Js('lm'), Js('ln'), Js('lr'), Js('lt'), Js('lz'), Js('mb'), Js('md'), Js('ml'), Js('mn'), Js('mr'), Js('nb'), Js('nd'), Js('ng'), Js('nl'), Js('nm'), Js('nr'), Js('nz'), Js('rb'), Js('rd'), Js('rg'), Js('rl'), Js('rm'), Js('rn'), Js('rt'), Js('rs'), Js('tl'), Js('tm'), Js('tn'), Js('tr'), Js('vl'), Js('vm'), Js('zl')]))
var.put('nm4', Js([Js('g'), Js('l'), Js('lm'), Js('ln'), Js('m'), Js('n'), Js('r'), Js('rf'), Js('rg'), Js('rn'), Js('rm'), Js('rt'), Js('ng')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('k'), Js('n'), Js('m'), Js('l'), Js('t'), Js('s'), Js('f'), Js('g'), Js('h'), Js('r')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ei'), Js('ea'), Js('eo'), Js('oa'), Js('ou'), Js('oo'), Js('ae'), Js('ai'), Js('au')]))
var.put('nm7', Js([Js('v'), Js('m'), Js('k'), Js('b'), Js('r'), Js('f'), Js('g'), Js('l'), Js('n'), Js('s'), Js('t')]))
var.put('nm8', Js([Js('m'), Js('k'), Js('r'), Js('f'), Js('g'), Js('l'), Js('n'), Js('s'), Js('t')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
zeldaGerudoNames = var.to_python()
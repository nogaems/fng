__all__ = ['sithNames']

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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm13').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('â'), Js('û'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('ch'), Js('d'), Js('dz'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kh'), Js('m'), Js('n'), Js('l'), Js('q'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('sr'), Js('t'), Js('ts'), Js('w'), Js('wr'), Js('wh'), Js('y'), Js('z'), Js('zh'), Js('zr'), Js('ch'), Js('d'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('l'), Js('q'), Js('r'), Js('s'), Js('t'), Js('w'), Js('y'), Js('z')]))
var.put('nm3', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('oi'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('â'), Js('û')]))
var.put('nm4', Js([Js('d'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('sh'), Js('q'), Js('r'), Js('s'), Js('t'), Js('ts'), Js('w'), Js('y'), Js('z')]))
var.put('nm5', Js([Js('d'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('sh'), Js('q'), Js('r'), Js('s'), Js('t'), Js('ts'), Js('w'), Js('y'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('a'), Js('û'), Js('â'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('oi')]))
var.put('nm7', Js([Js('r'), Js('t'), Js('s'), Js('sh'), Js('z'), Js('n'), Js('m'), Js('ts'), Js('l'), Js('w'), Js(''), Js(''), Js(''), Js('')]))
var.put('nm8', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm9', Js([Js('b'), Js('bh'), Js('br'), Js('c'), Js('ch'), Js('cl'), Js('d'), Js('dr'), Js('dh'), Js('g'), Js('gr'), Js('gh'), Js('j'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('q'), Js('r'), Js('rh'), Js('s'), Js('sl'), Js('sh'), Js('t'), Js('tr'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('wh'), Js('x'), Js('y'), Js('z'), Js('zh'), Js('zr'), Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ea'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm11', Js([Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x')]))
var.put('nm12', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm13', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('iu'), Js('ae'), Js('ia'), Js('ua'), Js('uo'), Js('ea'), Js('iu'), Js('ae'), Js('ia'), Js('ua')]))
var.put('nm14', Js([Js('th'), Js('s'), Js('sh'), Js('n'), Js('m'), Js('x'), Js('l'), Js('wr'), Js('sy'), Js('ty'), Js('tiur'), Js('tiuth'), Js('siuth'), Js('ny'), Js('nyr'), Js('lyr'), Js('rius'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
sithNames = var.to_python()
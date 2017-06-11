__all__ = ['forswornNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd8a', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('nameLast', (((((var.get('nm10').get(var.get('rnd8a'))+var.get('nm6').get(var.get('rnd8')))+var.get('nm3').get(var.get('rnd9')))+var.get('nm6').get(var.get('rnd10')))+var.get('nm8').get(var.get('rnd11')))+var.get('nm9').get(var.get('rnd12'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+Js('  '))+var.get('nameLast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('nameLast')))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', ((((var.get('nm7').get(var.get('rnd2'))+var.get('nm8').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd')))+Js(' '))+var.get('nameLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('nameLast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('w')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ey'), Js('ay'), Js('ai'), Js('ua'), Js('uu'), Js('uo'), Js('au')]))
var.put('nm3', Js([Js('br'), Js('bb'), Js('cc'), Js('cr'), Js('cd'), Js('d'), Js('dv'), Js('dr'), Js('dl'), Js('gv'), Js('gl'), Js('gm'), Js('gn'), Js('gr'), Js('l'), Js('lr'), Js('lm'), Js('ln'), Js('lk'), Js('lv'), Js('ld'), Js('lc'), Js('mr'), Js('ml'), Js('mm'), Js('mv'), Js('md'), Js('n'), Js('nn'), Js('nd'), Js('nb'), Js('nv'), Js('nr'), Js('ng'), Js('r'), Js('rk'), Js('rv'), Js('rg'), Js('rd'), Js('rb'), Js('rt'), Js('st'), Js('sl'), Js('sr'), Js('v'), Js('vv'), Js('vr'), Js('vl')]))
var.put('nm4', Js([Js('c'), Js('ch'), Js('d'), Js('g'), Js('l'), Js('n'), Js('r'), Js('s')]))
var.put('nm5', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o')]))
var.put('nm7', Js([Js('uai'), Js('aie'), Js('eia'), Js('uae'), Js('iae'), Js('iea'), Js('ai'), Js('ua'), Js('ea'), Js('ia'), Js('ei')]))
var.put('nm8', Js([Js('d'), Js('f'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('w')]))
pass
pass


# Add lib to the module scope
forswornNames = var.to_python()
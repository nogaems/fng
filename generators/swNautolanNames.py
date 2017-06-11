__all__ = ['swNautolanNames']

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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if (PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)) and ((var.get('i')%Js(2.0))!=Js(0.0))):
                while (var.get('rnd7')<Js(3.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
                else:
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('namelast', ((((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd12')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(7.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd5b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5b')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(5.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('d'), Js('f'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('kn'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('rh'), Js('rr'), Js('s'), Js('sh'), Js('shr'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oo'), Js('ey'), Js('ei'), Js('ea'), Js('ee'), Js('aa')]))
var.put('nm3', Js([Js('ch'), Js('d'), Js('dd'), Js('f'), Js('fr'), Js('k'), Js('kt'), Js('kx'), Js('l'), Js('m'), Js('mr'), Js('md'), Js('mt'), Js('n'), Js('nd'), Js('ng'), Js('nn'), Js('nt'), Js('ntv'), Js('nr'), Js('ny'), Js('pr'), Js('r'), Js('rk'), Js('rr'), Js('s'), Js('shn'), Js('sn'), Js('sp'), Js('spr'), Js('th'), Js('tr'), Js('tv'), Js('v'), Js('w'), Js('x'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('t'), Js('x')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('dr'), Js('dh'), Js('f'), Js('fr'), Js('g'), Js('gh'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('th'), Js('w'), Js('y'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('ea'), Js('ee'), Js('ai'), Js('ie'), Js('ia'), Js('oo')]))
var.put('nm7', Js([Js('b'), Js('c'), Js('ch'), Js('f'), Js('ff'), Js('h'), Js('hl'), Js('l'), Js('ll'), Js('lm'), Js('ln'), Js('lr'), Js('m'), Js('ml'), Js('mm'), Js('my'), Js('n'), Js('nn'), Js('nl'), Js('nd'), Js('ny'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('shn'), Js('t'), Js('th'), Js('w'), Js('y')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('n'), Js('s'), Js('t')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('rh'), Js('s'), Js('st'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oa'), Js('ai'), Js('ia'), Js('ii'), Js('ie'), Js('ee'), Js('oo')]))
var.put('nm11', Js([Js('ch'), Js('chm'), Js('d'), Js('dd'), Js('dr'), Js('dj'), Js('g'), Js('gg'), Js('gr'), Js('gd'), Js('gn'), Js('j'), Js('k'), Js('kt'), Js('kk'), Js('l'), Js('m'), Js('mm'), Js('md'), Js('mp'), Js('n'), Js('nd'), Js('nn'), Js('ng'), Js('nr'), Js('nt'), Js('r'), Js('rr'), Js('rd'), Js('rg'), Js('rj'), Js('rt'), Js('rv'), Js('st'), Js('t'), Js('tr'), Js('wch'), Js('z')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('mt'), Js('n'), Js('ng'), Js('nd'), Js('nt'), Js('r'), Js('rk'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('ts'), Js('z'), Js('zz')]))
pass
pass


# Add lib to the module scope
swNautolanNames = var.to_python()
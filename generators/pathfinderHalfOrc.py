__all__ = ['pathfinderHalfOrc']

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
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if (PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)) and ((var.get('i')%Js(2.0))!=Js(0.0))):
                var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('nameLast', ((((((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd14')))+var.get('nm11').get(var.get('rnd15')))+var.get('nm10').get(var.get('rnd16')))+var.get('nm12').get(var.get('rnd12'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    while (var.get('rnd10')<Js(5.0)):
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    while (var.get('rnd12')<Js(5.0)):
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('nameLast', ((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm12').get(var.get('rnd12'))))
                else:
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('nameLast', ((((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd14')))+var.get('nm12').get(var.get('rnd12'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(8.0)):
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(3.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(3.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('nameLast')))
                else:
                    if (var.get('i')<Js(9.0)):
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('cr'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('h'), Js('hr'), Js('k'), Js('m'), Js('n'), Js('p'), Js('t'), Js('th'), Js('ts'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('o'), Js('aa'), Js('au'), Js('oa'), Js('ia'), Js('ai'), Js('uu')]))
var.put('nm3', Js([Js('br'), Js('b'), Js('d'), Js('dh'), Js('dr'), Js('dz'), Js('g'), Js('gr'), Js('gd'), Js('gh'), Js('k'), Js('kh'), Js('kt'), Js('kd'), Js('kr'), Js('lgr'), Js('ltr'), Js('ldr'), Js('lr'), Js('lkr'), Js('nd'), Js('ng'), Js('ngr'), Js('ndr'), Js('nv'), Js('r'), Js('rv'), Js('rg'), Js('rdr'), Js('st'), Js('sd'), Js('str'), Js('tr'), Js('v'), Js('zr'), Js('zz'), Js('zv'), Js('zvr')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('ch'), Js('d'), Js('g'), Js('k'), Js('l'), Js('lm'), Js('n'), Js('r'), Js('rg'), Js('rm'), Js('rv'), Js('s'), Js('sk'), Js('t'), Js('x'), Js('zhg')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('d'), Js('dr'), Js('g'), Js('h'), Js('k'), Js('m'), Js('n'), Js('r'), Js('rz'), Js('s'), Js('sh'), Js('str'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('o'), Js('ay'), Js('ou'), Js('ai'), Js('uo')]))
var.put('nm7', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dl'), Js('dr'), Js('g'), Js('gh'), Js('gr'), Js('gl'), Js('hg'), Js('hk'), Js('hr'), Js('jk'), Js('l'), Js('ljk'), Js('ll'), Js('ln'), Js('lr'), Js('lt'), Js('m'), Js('mr'), Js('mg'), Js('ml'), Js('n'), Js('ng'), Js('nl'), Js('nc'), Js('r'), Js('rg'), Js('rl'), Js('rd'), Js('s'), Js('sl'), Js('sr'), Js('t'), Js('tt'), Js('tr'), Js('v'), Js('vr'), Js('z'), Js('zr')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('n'), Js('sh'), Js('th'), Js('x')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('g'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('w'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm11', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('dk'), Js('g'), Js('gr'), Js('gh'), Js('gl'), Js('k'), Js('kr'), Js('l'), Js('lk'), Js('lgr'), Js('ln'), Js('lr'), Js('lr'), Js('m'), Js('mk'), Js('n'), Js('nr'), Js('nk'), Js('nd'), Js('ndr'), Js('ng'), Js('rg'), Js('rv'), Js('rk'), Js('r'), Js('rr'), Js('rsh'), Js('shk'), Js('st'), Js('sk'), Js('sr'), Js('sv'), Js('svr'), Js('tsk'), Js('tk'), Js('tr'), Js('v'), Js('xl'), Js('xn'), Js('z'), Js('zr'), Js('zk')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('d'), Js('k'), Js('ld'), Js('lm'), Js('m'), Js('n'), Js('r'), Js('shky'), Js('tsky'), Js('v'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
pathfinderHalfOrc = var.to_python()
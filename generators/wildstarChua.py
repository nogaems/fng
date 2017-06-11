__all__ = ['wildstarChua']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                while (var.get('rnd3')<Js(7.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('lname', ((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3'))))
            else:
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('lname', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd3'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                while (var.get('rnd5')<Js(7.0)):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('name', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('name', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('j'), Js('m'), Js('n'), Js('r'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ao'), Js('oa'), Js('ia'), Js('ee'), Js('ua')]))
var.put('nm3', Js([Js('br'), Js('bn'), Js('dr'), Js('dh'), Js('dg'), Js('dz'), Js('fr'), Js('ff'), Js('g'), Js('gn'), Js('gg'), Js('gz'), Js('gh'), Js('j'), Js('k'), Js('kn'), Js('kv'), Js('kt'), Js('kv'), Js('kz'), Js('lk'), Js('lv'), Js('lg'), Js('ll'), Js('n'), Js('nn'), Js('nk'), Js('np'), Js('nt'), Js('nv'), Js('m'), Js('mm'), Js('mk'), Js('pp'), Js('rr'), Js('rg'), Js('rsr'), Js('rs'), Js('rt'), Js('rv'), Js('rk'), Js('sk'), Js('ss'), Js('sz'), Js('sn'), Js('sm'), Js('t'), Js('tt'), Js('tk'), Js('v'), Js('vn')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('h'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('t'), Js('th'), Js('w'), Js('x'), Js('zz')]))
var.put('nm5', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('g'), Js('gn'), Js('gr'), Js('j'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('vr'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('f'), Js('h'), Js('l'), Js('ll'), Js('m'), Js('ms'), Js('n'), Js('ns'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('t'), Js('th'), Js('x'), Js('zz')]))
pass
pass


# Add lib to the module scope
wildstarChua = var.to_python()
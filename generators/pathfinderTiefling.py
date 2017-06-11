__all__ = ['pathfinderTiefling']

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
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('lastName', ((((var.get('nm9').get(var.get('rnd8'))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm10').get(var.get('rnd11')))+var.get('nm12').get(var.get('rnd12'))))
            else:
                var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('lastName', ((((((var.get('nm9').get(var.get('rnd8'))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd14')))+var.get('nm12').get(var.get('rnd12'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('lastName')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('lastName')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lastName')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lastName')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('cr'), Js('d'), Js('g'), Js('h'), Js('k'), Js('kr'), Js('m'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ia'), Js('io')]))
var.put('nm3', Js([Js('c'), Js('cr'), Js('cn'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('gg'), Js('k'), Js('kr'), Js('l'), Js('ldr'), Js('lv'), Js('ll'), Js('m'), Js('nst'), Js('nv'), Js('nr'), Js('r'), Js('rn'), Js('rd'), Js('rk'), Js('rrd'), Js('rt'), Js('rv'), Js('s'), Js('sr'), Js('sk'), Js('t'), Js('tr'), Js('v'), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('c'), Js('k'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th')]))
var.put('nm5', Js([Js('d'), Js('f'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('str'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('a'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('a'), Js('e'), Js('a'), Js('o'), Js('e'), Js('a'), Js('o'), Js('e'), Js('i'), Js('i'), Js('ei'), Js('ia'), Js('ea'), Js('ai')]))
var.put('nm7', Js([Js('d'), Js('dr'), Js('f'), Js('fr'), Js('ff'), Js('l'), Js('ll'), Js('ld'), Js('ldr'), Js('lr'), Js('ln'), Js('ls'), Js('m'), Js('mr'), Js('mdr'), Js('ms'), Js('nd'), Js('ndr'), Js('nn'), Js('n'), Js('nz'), Js('r'), Js('rdr'), Js('rr'), Js('rs'), Js('rz'), Js('s'), Js('sh'), Js('sz'), Js('sr'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('y'), Js('zs'), Js('d'), Js('f'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y')]))
var.put('nm8', Js([Js('h'), Js('l'), Js('n'), Js('s'), Js('th')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('v'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('a'), Js('e'), Js('e'), Js('i'), Js('aa'), Js('ae'), Js('ia'), Js('ea')]))
var.put('nm11', Js([Js('b'), Js('br'), Js('c'), Js('d'), Js('dr'), Js('fr'), Js('g'), Js('gg'), Js('gr'), Js('gv'), Js('k'), Js('l'), Js('ll'), Js('lr'), Js('lv'), Js('ldr'), Js('m'), Js('mm'), Js('mr'), Js('mdr'), Js('n'), Js('nd'), Js('ng'), Js('ndr'), Js('nst'), Js('nv'), Js('nr'), Js('r'), Js('rh'), Js('rv'), Js('rr'), Js('rz'), Js('rd'), Js('rdr'), Js('s'), Js('ss'), Js('sr'), Js('sh'), Js('st'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('ld'), Js('lt'), Js('m'), Js('n'), Js('nd'), Js('r'), Js('rd'), Js('s'), Js('t'), Js('th')]))
pass
pass


# Add lib to the module scope
pathfinderTiefling = var.to_python()
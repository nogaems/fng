__all__ = ['swAnzatiNames']

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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js('  '))+var.get('nm8').get(var.get('rnd6')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd8')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd10'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                def PyJs_LONG_0_(var=var):
                    return var.put('names', ((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('nm8').get(var.get('rnd6')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd8')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd10'))))
                PyJs_LONG_0_()
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('h'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('ct'), Js('cn'), Js('cm'), Js('gr'), Js('kk'), Js('kr'), Js('kt'), Js('ll'), Js('lf'), Js('lg'), Js('lr'), Js('ld'), Js('nn'), Js('nt'), Js('nr'), Js('mr'), Js('mm'), Js('md'), Js('rr'), Js('rk'), Js('rt'), Js('st'), Js('sn'), Js('sm'), Js('th'), Js('sh'), Js('tt'), Js('tr'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('c'), Js('h'), Js('k'), Js('l'), Js('n'), Js('nt'), Js('r'), Js('s'), Js('th')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ia')]))
var.put('nm7', Js([Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('sh'), Js('th'), Js('mm'), Js('nn'), Js('ll'), Js('dh'), Js('mh'), Js('nh'), Js('kr'), Js('dr'), Js('gr'), Js('ml'), Js('kl')]))
var.put('nm8', Js([Js('b'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ou'), Js('ei'), Js('ea'), Js('ia')]))
var.put('nm10', Js([Js('ct'), Js('cn'), Js('cm'), Js('gr'), Js('kk'), Js('kr'), Js('kt'), Js('ll'), Js('lg'), Js('lf'), Js('ld'), Js('lr'), Js('lkk'), Js('k'), Js('mm'), Js('mr'), Js('md'), Js('nn'), Js('nr'), Js('nd'), Js('nt'), Js('nn'), Js('r'), Js('rr'), Js('rt'), Js('rkk'), Js('sh'), Js('st'), Js('sn'), Js('sm'), Js('th'), Js('sh'), Js('tt'), Js('tr'), Js('zz')]))
pass
pass


# Add lib to the module scope
swAnzatiNames = var.to_python()
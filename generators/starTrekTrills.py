__all__ = ['starTrekTrills']

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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                while (var.get('rnd7')<Js(2.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                if (var.get('rnd8')<Js(4.0)):
                    while (var.get('rnd9')>Js(1.0)):
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                else:
                    while (var.get('rnd9')<Js(2.0)):
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                def PyJs_LONG_0_(var=var):
                    return var.put('names', ((((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nm9').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd8')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
                PyJs_LONG_0_()
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('rnd2')<Js(2.0)):
                    while (var.get('rnd4')<Js(2.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                while (var.get('rnd7')<Js(2.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                if (var.get('rnd8')<Js(4.0)):
                    while (var.get('rnd9')>Js(1.0)):
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                else:
                    while (var.get('rnd9')<Js(2.0)):
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                def PyJs_LONG_1_(var=var):
                    return var.put('names', ((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nm9').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd8')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
                PyJs_LONG_1_()
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js('b'), Js('c'), Js('d'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('vr'), Js('y')]))
var.put('nm2', Js([Js('ia'), Js('aa'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('d'), Js('dr'), Js('g'), Js('hj'), Js('j'), Js('l'), Js('m'), Js('mbl'), Js('n'), Js('r'), Js('rv'), Js('rz'), Js('rj')]))
var.put('nm4', Js([Js(''), Js('d'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('ss')]))
var.put('nm5', Js([Js(''), Js('b'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('r'), Js('v'), Js('y')]))
var.put('nm6', Js([Js('au'), Js('ia'), Js('ee'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm7', Js([Js('b'), Js('dr'), Js('dz'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nh'), Js('r'), Js('s'), Js('ss'), Js('sr'), Js('z'), Js('zr')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('h'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('s')]))
var.put('nm9', Js([Js('b'), Js('d'), Js('gr'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('t'), Js('v')]))
var.put('nm10', Js([Js(''), Js(''), Js('ee'), Js('ia'), Js('au'), Js('aa'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('gr'), Js('gn'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('rr'), Js('r'), Js('s'), Js('tn'), Js('v'), Js('z')]))
var.put('nm12', Js([Js('d'), Js('g'), Js('hn'), Js('hl'), Js('l'), Js('m'), Js('n'), Js('r'), Js('rs'), Js('s'), Js('x')]))
pass
pass


# Add lib to the module scope
starTrekTrills = var.to_python()
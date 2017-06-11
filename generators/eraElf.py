__all__ = ['eraElf']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                if (var.get('i')<Js(6.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    if (var.get('rnd')<Js(4.0)):
                        while (var.get('rnd4')<Js(5.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4'))))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('c'), Js('cl'), Js('d'), Js('f'), Js('g'), Js('gl'), Js('gn'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('t'), Js('th'), Js('v'), Js('vr'), Js('w')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('í'), Js('ö'), Js('ä'), Js('äo'), Js('á'), Js('ae'), Js('ia'), Js('ie'), Js('io'), Js('au'), Js('ae')]))
var.put('nm3', Js([Js('c'), Js('d'), Js('dhg'), Js('dg'), Js('dr'), Js('dh'), Js('f'), Js('g'), Js('gh'), Js('l'), Js('lm'), Js('ln'), Js('ld'), Js('ldth'), Js('ll'), Js('lr'), Js('mn'), Js('m'), Js('mh'), Js('n'), Js('nd'), Js('nr'), Js('nth'), Js('nw'), Js('r'), Js('rd'), Js('rv'), Js('rz'), Js('rth'), Js('s'), Js('sd'), Js('th'), Js('tr'), Js('v')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('dr'), Js('l'), Js('ldr'), Js('lr'), Js('mh'), Js('n'), Js('ng'), Js('r'), Js('rm'), Js('s')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('bh'), Js('cl'), Js('d'), Js('f'), Js('gl'), Js('gh'), Js('h'), Js('l'), Js('m'), Js('n'), Js('rh'), Js('s'), Js('t'), Js('th'), Js('v'), Js('w'), Js('y')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('í'), Js('ë'), Js('ö'), Js('á'), Js('ëa'), Js('ia'), Js('io'), Js('au'), Js('ue'), Js('ua'), Js('ía'), Js('ae')]))
var.put('nm7', Js([Js('d'), Js('dr'), Js('fr'), Js('l'), Js('ll'), Js('lr'), Js('ln'), Js('lm'), Js('ldr'), Js('ld'), Js('ly'), Js('m'), Js('mv'), Js('my'), Js('mm'), Js('ny'), Js('n'), Js('nn'), Js('nv'), Js('nz'), Js('r'), Js('rm'), Js('ry'), Js('rh'), Js('sn'), Js('sl'), Js('t'), Js('th'), Js('y')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('n'), Js('r'), Js('s'), Js('th')]))
pass
pass


# Add lib to the module scope
eraElf = var.to_python()
__all__ = ['satyrNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(5.0)):
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    while (var.get('rnd')<Js(3.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7'))))
            else:
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(3.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('br'), Js('c'), Js('ch'), Js('cr'), Js('cl'), Js('d'), Js('dr'), Js('dh'), Js('f'), Js('g'), Js('gr'), Js('gh'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kn'), Js('m'), Js('n'), Js('pr'), Js('p'), Js('q'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('st'), Js('str'), Js('sn'), Js('sm'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('wr'), Js('x'), Js('xh'), Js('z'), Js('zr'), Js('zh'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('j'), Js('k'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('ai'), Js('ae'), Js('au'), Js('aa'), Js('ea'), Js('eo'), Js('ee'), Js('ia'), Js('ie'), Js('io')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('w'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('ck'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('x'), Js('z')]))
var.put('nm6', Js([Js('e'), Js('i'), Js('u'), Js('a'), Js('o'), Js('y'), Js('ia'), Js('ea'), Js('ae')]))
pass
pass


# Add lib to the module scope
satyrNames = var.to_python()
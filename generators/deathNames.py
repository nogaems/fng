__all__ = ['deathNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            if (var.get('i')<Js(3.0)):
                while (var.get('rnd')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                while (var.get('rnd5')<Js(12.0)):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('br'), Js('c'), Js('ch'), Js('ct'), Js('cth'), Js('d'), Js('dr'), Js('dh'), Js('dy'), Js('dz'), Js('f'), Js('fr'), Js('g'), Js('gh'), Js('gn'), Js('h'), Js('hw'), Js('k'), Js('kh'), Js('kn'), Js('kr'), Js('l'), Js('m'), Js('m'), Js('mn'), Js('mh'), Js('m'), Js('n'), Js('ng'), Js('p'), Js('ph'), Js('pr'), Js('q'), Js('qh'), Js('s'), Js('sh'), Js('st'), Js('sr'), Js('t'), Js('th'), Js('v'), Js('vr'), Js('vh'), Js('w'), Js('wr'), Js('x'), Js('y')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ae'), Js('ai'), Js('aa'), Js('eo'), Js('ea'), Js('ei'), Js('io'), Js('iu'), Js('ia'), Js('oo'), Js('ou'), Js('uu'), Js('ua'), Js('ue')]))
var.put('nm3', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('g'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('z')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('th'), Js('tr'), Js('w')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('cs'), Js('c'), Js('d'), Js('d'), Js('h'), Js('h'), Js('k'), Js('k'), Js('ks'), Js('l'), Js('ls'), Js('l'), Js('n'), Js('n'), Js('ng'), Js('nth'), Js('q'), Js('q'), Js('r'), Js('r'), Js('rs'), Js('s'), Js('s'), Js('t'), Js('t'), Js('th'), Js('v'), Js('x')]))
pass
pass


# Add lib to the module scope
deathNames = var.to_python()
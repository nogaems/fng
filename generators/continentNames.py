__all__ = ['continentNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                if (var.get('rnd')>Js(20.0)):
                    while (var.get('rnd3')>Js(17.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('names', (((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names5').get(var.get('rnd6'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('names', (((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names5').get(var.get('rnd6'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    if (var.get('rnd')>Js(20.0)):
                        while (var.get('rnd3')>Js(17.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    if (var.get('rnd2')>Js(4.0)):
                        while (var.get('rnd4')>Js(4.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    if ((var.get('rnd')>Js(17.0)) or (var.get('rnd')>Js(20.0))):
                        while (var.get('rnd5')>Js(19.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('names', (((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names2').get(var.get('rnd4')))+var.get('names4').get(var.get('rnd5')))+var.get('names5').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('pr'), Js('tr'), Js('vr'), Js('wr'), Js('str'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('vl'), Js('ch'), Js('ph'), Js('sh'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('eu'), Js('eo'), Js('ea'), Js('ei'), Js('ai'), Js('au'), Js('ae'), Js('io'), Js('ia'), Js('iu'), Js('ua')]))
var.put('names3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('w'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('tr'), Js('vr'), Js('wr'), Js('str'), Js('bl'), Js('cl'), Js('pl'), Js('sl'), Js('ch'), Js('ph'), Js('sh')]))
var.put('names4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('pr'), Js('tr'), Js('str'), Js('ph'), Js('sh')]))
var.put('names5', Js([Js('aes'), Js('ai'), Js('all'), Js('an'), Js('and'), Js('ane'), Js('ari'), Js('as'), Js('ath'), Js('ax'), Js('ea'), Js('ela'), Js('en'), Js('end'), Js('eon'), Js('era'), Js('eron'), Js('es'), Js('esh'), Js('eth'), Js('ia'), Js('ias'), Js('ica'), Js('in'), Js('ios'), Js('ira'), Js('is'), Js('ish'), Js('ith'), Js('ix'), Js('oa'), Js('on'), Js('one'), Js('or'), Js('ora'), Js('oris'), Js('os'), Js('oth'), Js('ox'), Js('oya'), Js('uan'), Js('uin'), Js('ul'), Js('un'), Js('une'), Js('ura'), Js('us'), Js('ush'), Js('uth'), Js('ux')]))
var.put('names6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
pass
pass


# Add lib to the module scope
continentNames = var.to_python()
__all__ = ['swGranNames']

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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('rnd6')<Js(5.0)):
                while (var.get('rnd8')<Js(5.0)):
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('namelast', ((var.get('nm1').get(var.get('rnd6'))+var.get('nm5').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd8'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('namelast', ((((var.get('nm1').get(var.get('rnd6'))+var.get('nm5').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd11')))+var.get('nm4').get(var.get('rnd8'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(5.0)):
                if (var.get('rnd')<Js(5.0)):
                    while (var.get('rnd4')<Js(5.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('shm'), Js('t'), Js('th'), Js('tw'), Js('v'), Js('y'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('aa'), Js('oe'), Js('ie'), Js('ia'), Js('ea')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('gg'), Js('gh'), Js('k'), Js('kg'), Js('kk'), Js('ks'), Js('l'), Js('ll'), Js('lv'), Js('m'), Js('mm'), Js('n'), Js('nch'), Js('nl'), Js('nn'), Js('ns'), Js('p'), Js('ph'), Js('r'), Js('rb'), Js('rg'), Js('rh'), Js('rl'), Js('rr'), Js('rv'), Js('s'), Js('sk'), Js('ss'), Js('t'), Js('th'), Js('tt'), Js('w'), Js('wh'), Js('y'), Js('yc')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('ff'), Js('g'), Js('gh'), Js('j'), Js('k'), Js('ks'), Js('kz'), Js('l'), Js('ls'), Js('m'), Js('n'), Js('nd'), Js('ps'), Js('r'), Js('rch'), Js('rg'), Js('s'), Js('sk'), Js('ss'), Js('th'), Js('wz'), Js('x'), Js('yk'), Js('z')]))
var.put('nm5', Js([Js('ee'), Js('aa'), Js('oe'), Js('ie'), Js('ia'), Js('ea'), Js('ei')]))
pass
pass


# Add lib to the module scope
swGranNames = var.to_python()
__all__ = ['destinyFallenNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((((var.get('nm2').get(var.get('rnd6'))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('g'), Js('gr'), Js('k'), Js('kr'), Js('n'), Js('p'), Js('ph'), Js('pr'), Js('r'), Js('s'), Js('sk'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('y')]))
var.put('nm3', Js([Js('g'), Js('gr'), Js('k'), Js('kl'), Js('kn'), Js('kr'), Js('ks'), Js('l'), Js('ld'), Js('lkr'), Js('ltr'), Js('lv'), Js('lz'), Js('p'), Js('r'), Js('rk'), Js('rl'), Js('rrh'), Js('sg'), Js('sgr'), Js('sk'), Js('skr'), Js('str'), Js('thr'), Js('tk'), Js('tr'), Js('v'), Js('vg'), Js('vk'), Js('vr')]))
var.put('nm4', Js([Js('k'), Js('ks'), Js('ks'), Js('ks'), Js('n'), Js('r'), Js('rk'), Js('s'), Js('s'), Js('s'), Js('sk')]))
pass
pass


# Add lib to the module scope
destinyFallenNames = var.to_python()
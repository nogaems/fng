__all__ = ['golemNames']

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
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(5.0)):
                while (var.get('rnd3')<Js(4.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
            else:
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('bh'), Js('d'), Js('dr'), Js('dh'), Js('g'), Js('gr'), Js('gh'), Js('kh'), Js('r'), Js('rh'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('aa'), Js('au')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('br'), Js('d'), Js('dd'), Js('dl'), Js('dr'), Js('fl'), Js('g'), Js('gg'), Js('gn'), Js('gm'), Js('gl'), Js('ggl'), Js('gv'), Js('gz'), Js('k'), Js('kk'), Js('kl'), Js('kv'), Js('l'), Js('ll'), Js('lg'), Js('lgr'), Js('lv'), Js('lb'), Js('ld'), Js('ldr'), Js('ng'), Js('nk'), Js('rb'), Js('rd'), Js('rg'), Js('zg'), Js('zzg'), Js('zzl'), Js('zl')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('hm'), Js('hk'), Js('hn'), Js('k'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('r')]))
pass
pass


# Add lib to the module scope
golemNames = var.to_python()
__all__ = ['dndKobolds']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm3', 'nameMas', 'nm2'])
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
    if (var.get('i')<Js(4.0)):
        while (var.get('rnd')<Js(4.0)):
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
        while ((var.get('rnd4')<Js(5.0)) or PyJsStrictEq(var.get('nm4').get(var.get('rnd4')),var.get('nm1').get(var.get('rnd')))):
            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        var.put('nMs', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4'))))
    else:
        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
        if (var.get('rnd')<Js(4.0)):
            while (var.get('rnd4')<Js(5.0)):
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd4')))):
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
        var.put('nMs', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd2'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameMas_.func_name = 'nameMas'
var.put('nameMas', PyJsHoisted_nameMas_)
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.get('nameMas')()
            while PyJsStrictEq(var.get('nMs'),Js('')):
                var.get('nameMas')()
            var.put('names', var.get('nMs'))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('h'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sn'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('bl'), Js('d'), Js('dr'), Js('g'), Js('gg'), Js('gl'), Js('gn'), Js('gr'), Js('hz'), Js('hr'), Js('hl'), Js('hs'), Js('k'), Js('kk'), Js('kr'), Js('kl'), Js('kb'), Js('kd'), Js('l'), Js('ld'), Js('lb'), Js('lt'), Js('ll'), Js('lp'), Js('lg'), Js('p'), Js('pl'), Js('pp'), Js('r'), Js('rt'), Js('rp'), Js('rb'), Js('rk'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vn')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('gs'), Js('k'), Js('ks'), Js('m'), Js('n'), Js('r'), Js('rn'), Js('s'), Js('ss'), Js('tt'), Js('v'), Js('x')]))
pass
pass
pass


# Add lib to the module scope
dndKobolds = var.to_python()
__all__ = ['dndAarakocra']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nameMas', 'nm2'])
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
    if (var.get('i')<Js(5.0)):
        while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
        var.put('nMs', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
    else:
        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        var.put('nMs', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd3'))))
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
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kh'), Js('kl'), Js('kr'), Js('q'), Js('qh'), Js('ql'), Js('qr'), Js('r'), Js('rh'), Js('s'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('ae'), Js('aia'), Js('ee'), Js('oo'), Js('ou'), Js('ua'), Js('uie')]))
var.put('nm3', Js([Js('c'), Js('cc'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('q'), Js('r'), Js('rr')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('aa'), Js('ea'), Js('ee'), Js('ia'), Js('ie')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ck'), Js('d'), Js('f'), Js('g'), Js('hk'), Js('k'), Js('l'), Js('r'), Js('rr'), Js('rc'), Js('rk'), Js('rrk'), Js('s'), Js('ss')]))
pass
pass
pass


# Add lib to the module scope
dndAarakocra = var.to_python()
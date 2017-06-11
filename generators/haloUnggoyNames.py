__all__ = ['haloUnggoyNames']

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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((var.get('nm2').get(var.get('rnd'))+var.get('nm1').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3')))+var.get('nm1').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd4'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    if (var.get('rnd')<Js(6.0)):
                        while (var.get('rnd3')<Js(6.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((var.get('nm3').get(var.get('rnd'))+var.get('nm1').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd1')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm1').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((var.get('nm4').get(var.get('rnd'))+var.get('nm1').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('i'), Js('u')]))
var.put('nm2', Js([Js('d'), Js('f'), Js('k'), Js('l'), Js('m'), Js('s'), Js('w'), Js('p'), Js('y'), Js('z')]))
var.put('nm3', Js([Js('fl'), Js('kl'), Js('sl'), Js('sm'), Js('pl'), Js('zl'), Js('d'), Js('f'), Js('k'), Js('l'), Js('m'), Js('s'), Js('w'), Js('p'), Js('y'), Js('z')]))
var.put('nm4', Js([Js('fl'), Js('kl'), Js('sl'), Js('sm'), Js('pl'), Js('zl')]))
pass
pass


# Add lib to the module scope
haloUnggoyNames = var.to_python()
__all__ = ['drWhoIceWarriorNames']

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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm1').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm1').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('h'), Js('gr'), Js('g'), Js('gl'), Js('k'), Js('kr'), Js('kl'), Js('r'), Js('sk'), Js('sl'), Js('ss'), Js('sr'), Js('sz'), Js('v'), Js('vr'), Js('xz'), Js('x'), Js('xr'), Js('xzn'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('o'), Js('e'), Js('aa'), Js('a'), Js('u'), Js('a'), Js('y'), Js('a')]))
var.put('nm3', Js([Js('d'), Js('dr'), Js('kss'), Js('ld'), Js('m'), Js('nt'), Js('r'), Js('rt'), Js('rd'), Js('rn'), Js('rg'), Js('sb'), Js('sr'), Js('sz'), Js('szr'), Js('zr'), Js('ssb'), Js('x'), Js('xl'), Js('z'), Js('zd')]))
var.put('nm4', Js([Js('d'), Js('dz'), Js('k'), Js('kz'), Js('l'), Js('lk'), Js('n'), Js('r'), Js('rd'), Js('rzz'), Js('rz'), Js('rs'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('a'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
drWhoIceWarriorNames = var.to_python()
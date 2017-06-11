__all__ = ['warhammerOrcs']

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
            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('cr'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('m'), Js('n'), Js('r'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('dg'), Js('dz'), Js('dr'), Js('g'), Js('gd'), Js('gg'), Js('gh'), Js('gk'), Js('gr'), Js('gz'), Js('hg'), Js('hz'), Js('hzr'), Js('hrz'), Js('hr'), Js('k'), Js('kd'), Js('kg'), Js('kz'), Js('kr'), Js('l'), Js('ld'), Js('lz'), Js('lr'), Js('ldr'), Js('lgr'), Js('m'), Js('mg'), Js('mh'), Js('mgr'), Js('mz'), Js('mzr'), Js('mdr'), Js('md'), Js('nd'), Js('ndr'), Js('nz'), Js('nzr'), Js('ng'), Js('r'), Js('rb'), Js('rrz'), Js('rg'), Js('rgh'), Js('rz'), Js('rzr'), Js('rk'), Js('rl'), Js('t'), Js('tg'), Js('tk'), Js('tr'), Js('tgr'), Js('tz'), Js('tzr'), Js('z'), Js('zh'), Js('zn')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('r'), Js('t'), Js('z')]))
pass
pass


# Add lib to the module scope
warhammerOrcs = var.to_python()
__all__ = ['drWhoZygonNames']

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
var.put('nm1', Js([Js('B'), Js('Br'), Js('Cr'), Js('D'), Js('Dr'), Js('G'), Js('Gr'), Js('K'), Js('Kr'), Js('R'), Js('S'), Js('Sr'), Js('Str'), Js('St'), Js('T'), Js('Tr'), Js('V'), Js('Vr')]))
var.put('nm2', Js([Js('e'), Js('a'), Js('o')]))
var.put('nm3', Js([Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm4', Js([Js('l'), Js('m'), Js('n'), Js('r'), Js('rm'), Js('rn'), Js('s'), Js('st')]))
pass
pass


# Add lib to the module scope
drWhoZygonNames = var.to_python()
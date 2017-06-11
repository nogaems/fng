__all__ = ['narniaMice']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js('eepi'))+var.get('nm2').get(var.get('rnd2')))+Js('ee'))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('ch'), Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('p'), Js('t'), Js('s'), Js('z')]))
var.put('nm2', Js([Js('c'), Js('ch'), Js('d'), Js('j'), Js('k'), Js('m'), Js('n'), Js('t')]))
var.put('nm3', Js([Js('k'), Js('p'), Js('t')]))
pass
pass


# Add lib to the module scope
narniaMice = var.to_python()
__all__ = ['drWhoDalekNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result', 'ext'])
    var.put('result', Js([]))
    var.put('ext', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(150.0))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('ext'),Js(1.0)):
                var.put('names', Js('Exterminate! Exterminate! Exterminate!'))
                if PyJsStrictEq(var.get('i'),Js(9.0)):
                    var.put('names', Js('Just kidding. :) Enjoy this Easter egg.'))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('C'), Js('Ch'), Js('D'), Js('Dh'), Js('G'), Js('Gh'), Js('K'), Js('Kh'), Js('R'), Js('S'), Js('Th'), Js('V')]))
var.put('nm2', Js([Js('a'), Js('aa'), Js('e'), Js('a'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm3', Js([Js('c'), Js('d'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('ss'), Js('st'), Js('t'), Js('th'), Js('y')]))
pass
pass


# Add lib to the module scope
drWhoDalekNames = var.to_python()
__all__ = ['destinyCabalNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm2b', 'nm3', 'nm2'])
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
            if (var.get('i')<Js(5.0)):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2b').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2b').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
                else:
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2b').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2b').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2b').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2b').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('d'), Js('dh'), Js('g'), Js('gh'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('sh'), Js('t'), Js('th'), Js('tl'), Js('v'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js("a'au"), Js("au'ua"), Js("o'ou"), Js("u'u"), Js("u'ua"), Js("u'uo"), Js("ua'au")]))
var.put('nm2b', Js([Js('a'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm4', Js([Js('c'), Js('ch'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('d'), Js('k'), Js('l'), Js('lk'), Js('ll'), Js('m'), Js('n'), Js('rc'), Js('rd'), Js('rg'), Js('rk'), Js('rn')]))
pass
pass


# Add lib to the module scope
destinyCabalNames = var.to_python()
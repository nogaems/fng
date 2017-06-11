__all__ = ['nephilimNames']

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
            if PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(4.0)):
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                if (var.get('rnd3')<Js(21.0)):
                    while (var.get('rnd6')<Js(21.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('a'), Js('e'), Js('a'), Js('e'), Js('a'), Js('e'), Js('a'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ya'), Js('yu'), Js('ee'), Js('ie'), Js('ue'), Js('ia')]))
var.put('nm3', Js([Js('dr'), Js('dj'), Js('gr'), Js('gn'), Js('kb'), Js('kn'), Js('mj'), Js('mr'), Js('mz'), Js('nz'), Js('nq'), Js('rq'), Js('rm'), Js('rj'), Js('rz'), Js('sb'), Js('sz'), Js('st'), Js('tr'), Js('tn'), Js('tz'), Js('b'), Js('d'), Js('g'), Js('j'), Js('k'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('z'), Js('b'), Js('d'), Js('g'), Js('j'), Js('k'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('z'), Js('b'), Js('d'), Js('g'), Js('j'), Js('k'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm4', Js([Js('l'), Js('n'), Js('s'), Js('th'), Js('z'), Js('l'), Js('l'), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
nephilimNames = var.to_python()
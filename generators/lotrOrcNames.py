__all__ = ['lotrOrcNames']

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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('c'), Js('cr'), Js('d'), Js('dr'), Js('g'), Js('gh'), Js('gr'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('r'), Js('s'), Js('sh'), Js('sr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au')]))
var.put('nm3', Js([Js('cb'), Js('cd'), Js('cr'), Js('db'), Js('dd'), Js('fd'), Js('fth'), Js('g'), Js('gb'), Js('gd'), Js('gg'), Js('gl'), Js('gr'), Js('gz'), Js('h'), Js('lcm'), Js('ld'), Js('lf'), Js('lg'), Js('rb'), Js('rc'), Js('rd'), Js('rg'), Js('rz'), Js('shn'), Js('thr'), Js('z'), Js('zb'), Js('zg'), Js('zr'), Js('zz')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('dh'), Js('f'), Js('g'), Js('gh'), Js('kh'), Js('l'), Js('r'), Js('rg'), Js('sh'), Js('t'), Js('th'), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('a'), Js('o'), Js('u'), Js('au')]))
pass
pass


# Add lib to the module scope
lotrOrcNames = var.to_python()
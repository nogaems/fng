__all__ = ['diabloKhazra']

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
            if (var.get('i')<Js(5.0)):
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('ch'), Js('cr'), Js('d'), Js('dr'), Js('gh'), Js('gr'), Js('h'), Js('hr'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('mw'), Js('n'), Js('r'), Js('sh'), Js('sk'), Js('sn'), Js('t'), Js('th'), Js('tr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oa'), Js('ao'), Js('au')]))
var.put('nm3', Js([Js('br'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('ggr'), Js('gl'), Js('hg'), Js('hl'), Js('hgr'), Js('lg'), Js('lgh'), Js('ld'), Js('lz'), Js('lb'), Js('lghb'), Js('ll'), Js('lm'), Js('ndr'), Js('nd'), Js('nz'), Js('nr'), Js('r'), Js('rb'), Js('rg'), Js('rd'), Js('rgr'), Js('rt'), Js('rth'), Js('rz'), Js('t'), Js('wd')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('ch'), Js('d'), Js('g'), Js('gg'), Js('k'), Js('l'), Js('lm'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('rg'), Js('s'), Js('sh'), Js('t'), Js('tch'), Js('th'), Js('wl')]))
pass
pass


# Add lib to the module scope
diabloKhazra = var.to_python()
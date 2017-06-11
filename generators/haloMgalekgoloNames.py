__all__ = ['haloMgalekgoloNames']

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
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            def PyJs_LONG_0_(var=var):
                return ((((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+Js(' '))+var.get('nm3').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm3').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+Js(' '))+var.get('nm3').get(var.get('rnd11')))
            var.put('names', (((PyJs_LONG_0_()+var.get('nm2').get(var.get('rnd12')))+var.get('nm4').get(var.get('rnd13')))+var.get('nm2').get(var.get('rnd14'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('w'), Js('x'), Js('y'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o')]))
var.put('nm3', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('w'), Js('x'), Js('y')]))
var.put('nm4', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('w'), Js('x'), Js('y'), Js('b'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('w'), Js('x'), Js('y'), Js('bn'), Js('dn'), Js('fn'), Js('gn'), Js('kn'), Js('pn'), Js('sn'), Js('tn'), Js('bm'), Js('dm'), Js('fm'), Js('gm'), Js('km'), Js('pm'), Js('sm'), Js('tm'), Js('bk'), Js('dk'), Js('lk'), Js('mk'), Js('nk'), Js('pk'), Js('sk'), Js('tk'), Js('bl'), Js('fl'), Js('gl'), Js('pl'), Js('tl'), Js('xl'), Js('sl'), Js('bd'), Js('gd'), Js('fd'), Js('ld'), Js('pd'), Js('sd'), Js('xd'), Js('bb'), Js('dd'), Js('ff'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt'), Js('ww'), Js('br'), Js('dr'), Js('gr'), Js('fr'), Js('kr'), Js('pr'), Js('tr'), Js('xr')]))
pass
pass


# Add lib to the module scope
haloMgalekgoloNames = var.to_python()
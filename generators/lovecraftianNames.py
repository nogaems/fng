__all__ = ['lovecraftianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('names', (((((var.get('nm2').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6'))))
            else:
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd1'))+var.get('nm2').get(var.get('rnd')))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('e'), Js('i'), Js('u'), Js('o'), Js('a'), Js('ai'), Js('aiu'), Js('aiue'), Js('e'), Js('i'), Js('ia'), Js('iau'), Js('iu'), Js('o'), Js('u'), Js('y'), Js('ya'), Js('yi'), Js('yo')]))
var.put('nm2', Js([Js('bh'), Js('br'), Js("c'th"), Js('cn'), Js('ct'), Js('cth'), Js('cx'), Js('d'), Js("d'"), Js('g'), Js('gh'), Js('ghr'), Js('gr'), Js('h'), Js('k'), Js('kh'), Js('kth'), Js('mh'), Js("mh'"), Js('ml'), Js('n'), Js('ng'), Js('sh'), Js('t'), Js('th'), Js('tr'), Js('v'), Js("v'"), Js('vh'), Js("vh'"), Js('vr'), Js('x'), Js('z'), Js("z'"), Js('zh')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('u'), Js('o'), Js('a'), Js('e'), Js('i'), Js('u'), Js('o'), Js('ao'), Js('aio'), Js('ui'), Js('aa'), Js('io'), Js('ou'), Js('y')]))
var.put('nm4', Js([Js('bb'), Js('bh'), Js('br'), Js('cn'), Js('ct'), Js('dh'), Js('dhr'), Js('dr'), Js('drr'), Js('g'), Js('gd'), Js('gg'), Js('ggd'), Js('gh'), Js('gn'), Js('gnn'), Js('gr'), Js('jh'), Js('kl'), Js('l'), Js('ld'), Js('lk'), Js('ll'), Js('lp'), Js('lth'), Js('mbr'), Js('nd'), Js('p'), Js('r'), Js('rr'), Js('rv'), Js('th'), Js('thl'), Js('thr'), Js('thrh'), Js('tl'), Js('vh'), Js('x'), Js('xh'), Js('z'), Js('zh'), Js('zt')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js("'dhr"), Js("'dr"), Js("'end"), Js("'gn"), Js("'ith"), Js("'itr"), Js("'k"), Js("'kr"), Js("'l"), Js("'m"), Js("'r"), Js("'th"), Js("'vh"), Js("'x"), Js("'zh")]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('u'), Js('o')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('h'), Js('l'), Js('lb'), Js('lbh'), Js('n'), Js('r'), Js('rc'), Js('rh'), Js('s'), Js('sh'), Js('ss'), Js('st'), Js('sz'), Js('th'), Js('tl'), Js('x'), Js('xr'), Js('xz')]))
pass
pass


# Add lib to the module scope
lovecraftianNames = var.to_python()
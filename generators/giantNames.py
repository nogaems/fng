__all__ = ['giantNames']

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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('a'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('ar'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('sr'), Js('tr'), Js('vr'), Js('wr'), Js('al'), Js('bl'), Js('cl'), Js('dl'), Js('fl'), Js('gl'), Js('kl'), Js('sl'), Js('vl'), Js('zl'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('e'), Js('i'), Js('u'), Js('o'), Js('a')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('ag'), Js('am'), Js('as'), Js('bar'), Js('barg'), Js('bog'), Js('bor'), Js('bos'), Js('brog'), Js('der'), Js('dhor'), Js('dius'), Js('dor'), Js('dus'), Js('fius'), Js('fum'), Js('fur'), Js('gan'), Js('gant'), Js('gar'), Js('gi'), Js('gir'), Js('grog'), Js('kaos'), Js('karos'), Js('kos'), Js('krus'), Js('las'), Js('lith'), Js('log'), Js('lor'), Js('los'), Js('malog'), Js('mir'), Js('mohr'), Js('nar'), Js('nas'), Js('nir'), Js('nus'), Js('og'), Js('om'), Js('os'), Js('rion'), Js('roch'), Js('rog'), Js('rus'), Js('rym'), Js('sag'), Js('sal'), Js('sar'), Js('sius'), Js('sog'), Js('sor'), Js('tag'), Js('tius'), Js('theus'), Js('thor'), Js('thos'), Js('to'), Js('tor'), Js('vag'), Js('ver'), Js('var'), Js('vir'), Js('vog'), Js('war'), Js('wor'), Js('zar'), Js('ziar'), Js('zus')]))
pass
pass


# Add lib to the module scope
giantNames = var.to_python()
__all__ = ['chissNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
            var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
            def PyJs_LONG_0_(var=var):
                return ((((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+Js("'"))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+Js("'"))+var.get('nm9').get(var.get('rnd9')))+var.get('nm10').get(var.get('rnd10')))+var.get('nm11').get(var.get('rnd11')))
            var.put('names', (((PyJs_LONG_0_()+var.get('nm12').get(var.get('rnd12')))+var.get('nm13').get(var.get('rnd13')))+var.get('nm14').get(var.get('rnd14'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('C'), Js('D'), Js('G'), Js('H'), Js('J'), Js('K'), Js('M'), Js('N'), Js('P'), Js('R'), Js('S'), Js('T'), Js('V'), Js('W'), Js('Z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('ra'), Js('re'), Js('ru'), Js('ri'), Js('ro'), Js('la'), Js('le'), Js('lu'), Js('li'), Js('lo')]))
var.put('nm3', Js([Js('th'), Js('tth'), Js('tt'), Js('s'), Js('ss'), Js('sh'), Js('st'), Js('sd'), Js('g'), Js('gh'), Js('w'), Js('q'), Js('qh'), Js('r'), Js('rr'), Js('rs'), Js('rt'), Js('rd'), Js('rg'), Js('rk'), Js('rm'), Js('rn'), Js('c'), Js('rc'), Js('sk'), Js('z'), Js('zz'), Js('m'), Js('mm'), Js('n'), Js('ng')]))
var.put('nm4', Js([Js('i'), Js('a'), Js('o'), Js('e'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('m'), Js('n'), Js('l'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('m'), Js('n'), Js('l'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z'), Js('ab'), Js('ac'), Js('ad'), Js('ag'), Js('ah'), Js('am'), Js('an'), Js('al'), Js('ap'), Js('ar'), Js('as'), Js('at'), Js('av'), Js('aw'), Js('az'), Js('ob'), Js('oc'), Js('od'), Js('og'), Js('oh'), Js('om'), Js('on'), Js('ol'), Js('op'), Js('or'), Js('os'), Js('ot'), Js('ov'), Js('ow'), Js('oz'), Js('ib'), Js('ic'), Js('id'), Js('ig'), Js('ih'), Js('im'), Js('in'), Js('il'), Js('ip'), Js('ir'), Js('is'), Js('it'), Js('iv'), Js('iw'), Js('iz'), Js('eb'), Js('ec'), Js('ed'), Js('eg'), Js('eh'), Js('em'), Js('en'), Js('el'), Js('ep'), Js('er'), Js('es'), Js('et'), Js('ev'), Js('ew'), Js('ez')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('ae'), Js('ea'), Js('au'), Js('ua'), Js('ao'), Js('oa'), Js('ou'), Js('uo'), Js('ia'), Js('ai')]))
var.put('nm7', Js([Js('n'), Js('t'), Js('th'), Js('w'), Js('l'), Js('m'), Js('sh'), Js('s'), Js('k'), Js('w'), Js('z'), Js('r')]))
var.put('nm8', Js([Js('i'), Js('a'), Js('o'), Js('e'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm9', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('ra'), Js('re'), Js('ru'), Js('ri'), Js('ro'), Js('la'), Js('le'), Js('lu'), Js('li'), Js('lo'), Js('ae'), Js('ea'), Js('au'), Js('ua'), Js('ao'), Js('oa'), Js('ou'), Js('uo'), Js('ia'), Js('ai')]))
var.put('nm11', Js([Js('th'), Js('tth'), Js('tt'), Js('s'), Js('s'), Js('s'), Js('g'), Js('g'), Js('r'), Js('r'), Js('c'), Js('c'), Js('m'), Js('m'), Js('n'), Js('n'), Js('z'), Js('z'), Js('ss'), Js('sh'), Js('st'), Js('sd'), Js('g'), Js('gh'), Js('w'), Js('q'), Js('qh'), Js('r'), Js('rr'), Js('rs'), Js('rt'), Js('rd'), Js('rg'), Js('rk'), Js('rm'), Js('rn'), Js('c'), Js('rc'), Js('sk'), Js('z'), Js('zz'), Js('m'), Js('mm'), Js('n'), Js('ng')]))
var.put('nm12', Js([Js('i'), Js('a'), Js('o'), Js('e'), Js('u')]))
var.put('nm13', Js([Js('th'), Js('tth'), Js('tt'), Js('s'), Js('s'), Js('s'), Js('g'), Js('g'), Js('r'), Js('r'), Js('c'), Js('c'), Js('m'), Js('m'), Js('n'), Js('n'), Js('z'), Js('z'), Js('ss'), Js('sh'), Js('st'), Js('sd'), Js('g'), Js('gh'), Js('w'), Js('q'), Js('qh'), Js('r'), Js('rr'), Js('rs'), Js('rt'), Js('rd'), Js('rg'), Js('rk'), Js('rm'), Js('rn'), Js('c'), Js('rc'), Js('sk'), Js('z'), Js('zz'), Js('m'), Js('mm'), Js('n'), Js('ng'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm14', Js([Js('i'), Js('a'), Js('o'), Js('e'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
chissNames = var.to_python()
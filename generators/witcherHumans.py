__all__ = ['witcherHumans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7'))))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    if (var.get('rnd4')<Js(20.0)):
                        var.put('rnd5', Js(0.0))
                        var.put('rnd6', Js(0.0))
                    else:
                        while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7'))))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('rnd4')<Js(40.0)):
                        var.put('rnd5', Js(0.0))
                        var.put('rnd6', Js(0.0))
                    else:
                        while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('f'), Js('gr'), Js('g'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('st'), Js('str'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ui'), Js('ea'), Js('ei'), Js('ie'), Js('ai'), Js('ua'), Js('ei'), Js('eo'), Js('ia'), Js('aa'), Js('ee')]))
var.put('nm3', Js([Js('b'), Js('b'), Js('br'), Js('bl'), Js('cl'), Js('c'), Js('c'), Js('cr'), Js('d'), Js('d'), Js('dl'), Js('dr'), Js('g'), Js('g'), Js('gr'), Js('gn'), Js('k'), Js('k'), Js('kr'), Js('kn'), Js('l'), Js('l'), Js('lc'), Js('ll'), Js('lm'), Js('lt'), Js('lw'), Js('m'), Js('m'), Js('mn'), Js('mr'), Js('n'), Js('n'), Js('nc'), Js('ndl'), Js('nh'), Js('nn'), Js('ns'), Js('nz'), Js('r'), Js('r'), Js('rd'), Js('rk'), Js('rn'), Js('rs'), Js('rv'), Js('ry'), Js('s'), Js('s'), Js('st'), Js('sk'), Js('sr'), Js('str'), Js('t'), Js('th'), Js('tr'), Js('tn'), Js('t'), Js('thm'), Js('v'), Js('v'), Js('z'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ui'), Js('ea'), Js('ei'), Js('ie'), Js('ai'), Js('ua'), Js('ei'), Js('eo'), Js('ia'), Js('aa'), Js('ee')]))
var.put('nm5', Js([Js(''), Js('b'), Js('b'), Js('br'), Js('bl'), Js('cl'), Js('c'), Js('c'), Js('cr'), Js('d'), Js('d'), Js('dl'), Js('dr'), Js('g'), Js('g'), Js('gr'), Js('gn'), Js('k'), Js('k'), Js('kr'), Js('kn'), Js('l'), Js('l'), Js('lc'), Js('ll'), Js('lm'), Js('lt'), Js('lw'), Js('m'), Js('m'), Js('mn'), Js('mr'), Js('n'), Js('n'), Js('nc'), Js('ndl'), Js('nh'), Js('nn'), Js('ns'), Js('nz'), Js('r'), Js('r'), Js('rd'), Js('rk'), Js('rn'), Js('rs'), Js('rv'), Js('ry'), Js('s'), Js('s'), Js('st'), Js('sk'), Js('sr'), Js('str'), Js('t'), Js('th'), Js('tr'), Js('tn'), Js('t'), Js('thm'), Js('v'), Js('v'), Js('z'), Js('z')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ck'), Js('d'), Js('k'), Js('l'), Js('ld'), Js('ll'), Js('lt'), Js('n'), Js('nd'), Js('r'), Js('s'), Js('st'), Js('y')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('br'), Js('c'), Js('d'), Js('dh'), Js('f'), Js('gl'), Js('gr'), Js('gw'), Js('k'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('y')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('io'), Js('ei'), Js('ea'), Js('ae'), Js('ia'), Js('ue'), Js('ua')]))
var.put('nm10', Js([Js('br'), Js('b'), Js('dh'), Js('d'), Js('dd'), Js('f'), Js('ff'), Js('fr'), Js('g'), Js('gh'), Js('gg'), Js('k'), Js('l'), Js('ll'), Js('lm'), Js('ln'), Js('lv'), Js('n'), Js('nc'), Js('nfr'), Js('nn'), Js('pp'), Js('ph'), Js('pr'), Js('r'), Js('rg'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('tt'), Js('th'), Js('v'), Js('zk'), Js('z')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('io'), Js('ei'), Js('ea'), Js('ae'), Js('ia'), Js('ue'), Js('ua')]))
var.put('nm12', Js([Js(''), Js('br'), Js('b'), Js('dh'), Js('d'), Js('dd'), Js('f'), Js('ff'), Js('fr'), Js('g'), Js('gh'), Js('gg'), Js('k'), Js('l'), Js('ll'), Js('lm'), Js('ln'), Js('lv'), Js('n'), Js('nc'), Js('nfr'), Js('nn'), Js('pp'), Js('ph'), Js('pr'), Js('r'), Js('rg'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('tt'), Js('th'), Js('v'), Js('zk'), Js('z')]))
var.put('nm14', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('s'), Js('n'), Js('h'), Js('l'), Js('th')]))
pass
pass


# Add lib to the module scope
witcherHumans = var.to_python()
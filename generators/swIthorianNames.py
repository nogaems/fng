__all__ = ['swIthorianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if (PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)) and ((var.get('i')%Js(2.0))!=Js(0.0))):
                while (var.get('rnd7')<Js(3.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                while (var.get('rnd10')<Js(4.0)):
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
                else:
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('namelast', ((((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd12')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd5b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5b')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5b')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('ch'), Js('cl'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('jh'), Js('jw'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('pl'), Js('pw'), Js('q'), Js('r'), Js('s'), Js('sn'), Js('spr'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('vl'), Js('w'), Js('wh'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('oo'), Js('ea'), Js('ua'), Js('eo'), Js('ou'), Js('ee'), Js('ao'), Js('ii'), Js('aa'), Js('ui'), Js('au'), Js('uu'), Js('ie')]))
var.put('nm3', Js([Js("'kl"), Js("'tr"), Js('b'), Js('bb'), Js('c'), Js('d'), Js('dl'), Js('ff'), Js('g'), Js('gg'), Js('ggj'), Js('h'), Js('k'), Js('kk'), Js('kl'), Js('kn'), Js('l'), Js('ld'), Js('lj'), Js('ll'), Js('lln'), Js('lm'), Js('ln'), Js('lr'), Js('lt'), Js('m'), Js('mf'), Js('ml'), Js('mw'), Js('n'), Js('nc'), Js('nd'), Js('nf'), Js('ngt'), Js('nst'), Js('nt'), Js('nw'), Js('pl'), Js('r'), Js('rf'), Js('rgl'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('rt'), Js('rth'), Js('s'), Js('sh'), Js("sh't"), Js('sm'), Js('ss'), Js('sthm'), Js('t'), Js('th'), Js('thw'), Js('tr'), Js('tt'), Js('v'), Js('vv'), Js('w'), Js('wb'), Js('x'), Js('xx'), Js('z'), Js('zl'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bb'), Js('bs'), Js('c'), Js('cl'), Js('d'), Js('g'), Js('gg'), Js('hp'), Js('j'), Js('k'), Js('l'), Js('ls'), Js('m'), Js('mm'), Js('n'), Js('nk'), Js('ph'), Js('r'), Js('rd'), Js('rg'), Js('rl'), Js('rn'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('th'), Js('v'), Js('w'), Js('wl'), Js('x'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('ch'), Js('cw'), Js('d'), Js('dh'), Js('f'), Js('fr'), Js('gh'), Js('gw'), Js('h'), Js('kh'), Js('kl'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('pl'), Js('pw'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('sw'), Js('sl'), Js('t'), Js('th'), Js('tw'), Js('v'), Js('vl'), Js('vh'), Js('w'), Js('wh'), Js('y')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ee'), Js('oo'), Js('uu'), Js('ii')]))
var.put('nm7', Js([Js("'sh"), Js("'th"), Js('bl'), Js('ch'), Js('dh'), Js('dw'), Js('f'), Js('ff'), Js('gh'), Js('gw'), Js('h'), Js('hh'), Js('kh'), Js('kw'), Js('ks'), Js('l'), Js('ls'), Js('ll'), Js('ln'), Js('lm'), Js('lth'), Js('lsh'), Js('lw'), Js('m'), Js('mm'), Js('mf'), Js('mw'), Js('mn'), Js('ml'), Js('mw'), Js('n'), Js('nd'), Js('ndr'), Js('nf'), Js('nw'), Js('nsh'), Js('ph'), Js('rsh'), Js('rs'), Js('rf'), Js('rl'), Js('rh'), Js('r'), Js('rw'), Js('rn'), Js('rm'), Js('rth'), Js('sh'), Js('sf'), Js('sv'), Js('sw'), Js('shw'), Js('ss'), Js('sn'), Js('sm'), Js('th'), Js('thw'), Js('thl'), Js('v'), Js('w'), Js('wh'), Js('wl'), Js('ws'), Js('wsh')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('f'), Js('g'), Js('h'), Js('l'), Js('m'), Js('mm'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('ss'), Js('th'), Js('w')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('cr'), Js('d'), Js('fl'), Js('fr'), Js('h'), Js('l'), Js('m'), Js('n'), Js('nh'), Js('p'), Js('pw'), Js('r'), Js('s'), Js('sl'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('oo'), Js('ea'), Js('ee'), Js('au'), Js('ua')]))
var.put('nm11', Js([Js('b'), Js('bb'), Js('bbl'), Js('bl'), Js('d'), Js('dd'), Js('f'), Js('fl'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('ll'), Js('lt'), Js('m'), Js('mfl'), Js('n'), Js('nd'), Js('nt'), Js('pr'), Js('q'), Js('r'), Js('rk'), Js('rt'), Js('rtk'), Js('s'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('w'), Js('wm'), Js('wr'), Js('xl'), Js('z')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bb'), Js('d'), Js('g'), Js('hl'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('ngs'), Js('nd'), Js('nn'), Js('r'), Js('rlq'), Js('s'), Js('t'), Js('th'), Js('thh'), Js('ts'), Js('w')]))
pass
pass


# Add lib to the module scope
swIthorianNames = var.to_python()
__all__ = ['swRodianNames']

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
                while (var.get('rnd7')<Js(10.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
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
                    while (var.get('rnd')<Js(10.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(8.0)):
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
                    while (var.get('rnd')<Js(10.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(40.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('c'), Js('ch'), Js('chr'), Js('cl'), Js('cr'), Js('d'), Js('dh'), Js('dr'), Js('dw'), Js('f'), Js('fr'), Js('g'), Js('gl'), Js('gr'), Js('gw'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('kn'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('pr'), Js('prw'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('sk'), Js('sl'), Js('sn'), Js('sp'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('ts'), Js('tw'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('aa'), Js('ei'), Js('oi'), Js('oo'), Js('ii'), Js('iu'), Js('ae'), Js('ea'), Js('ou'), Js('uu'), Js('ya'), Js('ye'), Js('yi'), Js('ua'), Js('ae'), Js('ay'), Js('ey'), Js('ei')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('bd'), Js('bl'), Js('bn'), Js('c'), Js('ch'), Js('d'), Js('dd'), Js('dj'), Js('dl'), Js('dr'), Js('f'), Js('ff'), Js('g'), Js('gr'), Js('gv'), Js('gw'), Js('h'), Js('hd'), Js('hm'), Js('j'), Js('k'), Js('kd'), Js('kk'), Js('kl'), Js('ks'), Js('ksl'), Js('ksr'), Js('kw'), Js('l'), Js('lb'), Js('lg'), Js('lk'), Js('lks'), Js('ll'), Js('llk'), Js('lr'), Js('ls'), Js('lt'), Js('lv'), Js('m'), Js('mb'), Js('mtr'), Js('n'), Js('nc'), Js('nd'), Js('ndr'), Js('ng'), Js('nk'), Js('nm'), Js('nn'), Js('nnd'), Js('nnt'), Js('nq'), Js('ns'), Js('nt'), Js('nw'), Js('p'), Js('pd'), Js('ph'), Js('pl'), Js('pp'), Js('q'), Js('r'), Js('rb'), Js('rd'), Js('rg'), Js('rgr'), Js('rh'), Js('rm'), Js('rn'), Js('rr'), Js('rrt'), Js('rsh'), Js('rss'), Js('rth'), Js('rv'), Js('rz'), Js('s'), Js('sd'), Js('sh'), Js('sk'), Js('ss'), Js('st'), Js('t'), Js('th'), Js('ts'), Js('v'), Js('vl'), Js('vv'), Js('w'), Js('x'), Js('z'), Js('zn'), Js('zw'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('bb'), Js('c'), Js('ch'), Js('ck'), Js('d'), Js('dd'), Js('f'), Js('g'), Js('gg'), Js('gn'), Js('h'), Js('k'), Js('kk'), Js('l'), Js('ld'), Js('ll'), Js('m'), Js('n'), Js('ng'), Js('nn'), Js('ns'), Js('nst'), Js('nt'), Js('p'), Js('pp'), Js('q'), Js('r'), Js('rk'), Js('rl'), Js('rm'), Js('rmm'), Js('rn'), Js('rtt'), Js('s'), Js('sh'), Js('sk'), Js('ss'), Js('ssk'), Js('t'), Js('tch'), Js('tz'), Js('v'), Js('w'), Js('x'), Js('xl'), Js('z'), Js('zz')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('bh'), Js('c'), Js('ch'), Js('cl'), Js('d'), Js('dh'), Js('dr'), Js('f'), Js('fl'), Js('g'), Js('gl'), Js('gh'), Js('gr'), Js('h'), Js('hr'), Js('j'), Js('k'), Js('kh'), Js('kl'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('phr'), Js('r'), Js('s'), Js('sh'), Js('sl'), Js('sn'), Js('sm'), Js('t'), Js('th'), Js('thr'), Js('tr'), Js('tw'), Js('v'), Js('vl'), Js('vr'), Js('vh'), Js('w'), Js('wr'), Js('wh'), Js('z'), Js('zh'), Js('zn'), Js('zm'), Js('zl')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('e'), Js('i'), Js('ee'), Js('ee'), Js('ee'), Js('ii'), Js('ii'), Js('ii'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ii'), Js('ii'), Js('ii'), Js('ii'), Js('ee'), Js('ii'), Js('oo'), Js('ea'), Js('ee'), Js('ei'), Js('eea'), Js('ii'), Js('oa'), Js('uu'), Js('ia')]))
var.put('nm7', Js([Js('b'), Js('bb'), Js('bl'), Js('bs'), Js('bn'), Js('bm'), Js('c'), Js('cn'), Js('cm'), Js('d'), Js('dh'), Js('dl'), Js('dn'), Js('dm'), Js('f'), Js('ff'), Js('fl'), Js('fn'), Js('fm'), Js('fr'), Js('g'), Js('gg'), Js('ht'), Js('hn'), Js('k'), Js('l'), Js('ll'), Js('ls'), Js('ln'), Js('lm'), Js('lb'), Js('lk'), Js('lk'), Js('ll'), Js('lv'), Js('lw'), Js('lr'), Js('m'), Js('mn'), Js('mm'), Js('md'), Js('ms'), Js('mz'), Js('n'), Js('nz'), Js('nr'), Js('nb'), Js('nd'), Js('ndr'), Js('nnr'), Js('nt'), Js('nm'), Js('nh'), Js('ns'), Js('ph'), Js('phl'), Js('phr'), Js('phn'), Js('r'), Js('rs'), Js('rz'), Js('rl'), Js('rd'), Js('rf'), Js('rm'), Js('rn'), Js('rp'), Js('rr'), Js('s'), Js('sh'), Js('ss'), Js('t'), Js('thm'), Js('th'), Js('thn'), Js('thl'), Js('ths'), Js('tz'), Js('ts'), Js('tt'), Js('v'), Js('w'), Js('z'), Js('zl')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('ss'), Js('th'), Js('w'), Js('z')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gh'), Js('gr'), Js('h'), Js('j'), Js('jc'), Js('k'), Js('khz'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('pr'), Js('r'), Js('s'), Js('sh'), Js('sw'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('vl'), Js('w'), Js('x'), Js('xr'), Js('z'), Js('zs'), Js('zt')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('e'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ee'), Js('ai'), Js('ee'), Js('oo'), Js('iee'), Js('eaa'), Js('ia'), Js('io'), Js('aa'), Js('uo'), Js('y'), Js('ii'), Js('oa'), Js('yo'), Js('yi'), Js('ye')]))
var.put('nm11', Js([Js('b'), Js('c'), Js('ch'), Js('d'), Js('fr'), Js('g'), Js('gg'), Js('j'), Js('k'), Js('kc'), Js('kk'), Js('ks'), Js('l'), Js('ld'), Js('lk'), Js('ln'), Js('lz'), Js('m'), Js('ml'), Js('n'), Js('nc'), Js('nck'), Js('nd'), Js('ng'), Js('nk'), Js('nn'), Js('np'), Js('nt'), Js('nw'), Js('p'), Js('pk'), Js('pp'), Js('r'), Js('rm'), Js('rr'), Js('rt'), Js('s'), Js('sk'), Js('sm'), Js('ss'), Js('st'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('y'), Js('z')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('d'), Js('ff'), Js('gg'), Js('ggs'), Js('gs'), Js('h'), Js('hn'), Js('hnt'), Js('ht'), Js('k'), Js('l'), Js('lb'), Js('ll'), Js('ls'), Js('m'), Js('n'), Js('ng'), Js('nk'), Js('nn'), Js('ntt'), Js('nx'), Js('p'), Js('q'), Js('r'), Js('rk'), Js('rn'), Js('ro'), Js('rr'), Js('rs'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('w'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
swRodianNames = var.to_python()
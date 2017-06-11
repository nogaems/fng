__all__ = ['civilizationNames']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            if (var.get('i')<Js(3.0)):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('names', ((((var.get('nm5').get(var.get('rnd2'))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6'))))
                    else:
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        while (var.get('rnd5')<Js(8.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('sr'), Js('tr'), Js('vr'), Js('wr'), Js('str'), Js('st'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('kl'), Js('sl'), Js('vl'), Js('ch'), Js('ph'), Js('sh'), Js('sch'), Js('gn'), Js('kn'), Js('sn'), Js('sm'), Js('sw'), Js('tw'), Js('sc'), Js('wh'), Js('th'), Js('thr'), Js('sph'), Js('spr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('eu'), Js('eo'), Js('ea'), Js('ei'), Js('aa'), Js('ai'), Js('au'), Js('ae'), Js('io'), Js('ia'), Js('iu'), Js('ie'), Js('oo'), Js('oa'), Js('ou'), Js('oe'), Js('oi'), Js('uu'), Js('ua'), Js('ue'), Js('ui'), Js('uo')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('w'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('w'), Js('z')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('w'), Js('z'), Js('bb'), Js('cc'), Js('ch'), Js('ck'), Js('cq'), Js('cr'), Js('cs'), Js('ct'), Js('cth'), Js('cz'), Js('dd'), Js('dg'), Js('dh'), Js('dn'), Js('dr'), Js('fd'), Js('ff'), Js('fk'), Js('fl'), Js('fn'), Js('fr'), Js('gb'), Js('gg'), Js('gh'), Js('gm'), Js('gn'), Js('gr'), Js('hg'), Js('hh'), Js('hk'), Js('hm'), Js('hn'), Js('hq'), Js('hr'), Js('kd'), Js('kh'), Js('kk'), Js('kl'), Js('kn'), Js('kr'), Js('ks'), Js('ksh'), Js('kt'), Js('kth'), Js('kz'), Js('lb'), Js('lc'), Js('ld'), Js('lf'), Js('lg'), Js('lh'), Js('lk'), Js('ll'), Js('lm'), Js('ln'), Js('lp'), Js('lph'), Js('lq'), Js('lr'), Js('ls'), Js('lsh'), Js('lst'), Js('lt'), Js('lth'), Js('lw'), Js('lz'), Js('mb'), Js('md'), Js('mh'), Js('mk'), Js('ml'), Js('mm'), Js('mn'), Js('mp'), Js('mph'), Js('mq'), Js('mr'), Js('ms'), Js('msh'), Js('mt'), Js('mth'), Js('mst'), Js('mz'), Js('nb'), Js('nc'), Js('nd'), Js('nf'), Js('ng'), Js('nh'), Js('nk'), Js('nl'), Js('nm'), Js('nn'), Js('np'), Js('nph'), Js('nq'), Js('nr'), Js('ns'), Js('nsh'), Js('nst'), Js('nt'), Js('nth'), Js('nw'), Js('nz'), Js('ph'), Js('pm'), Js('pn'), Js('pp'), Js('pq'), Js('pr'), Js('phr'), Js('phl'), Js('phm'), Js('phn'), Js('pth'), Js('pt'), Js('ps'), Js('pz'), Js('rb'), Js('rc'), Js('rd'), Js('rf'), Js('rg'), Js('rh'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rp'), Js('rph'), Js('rq'), Js('rr'), Js('rs'), Js('rsh'), Js('rst'), Js('rt'), Js('rth'), Js('rw'), Js('rz'), Js('sb'), Js('sc'), Js('sd'), Js('sh'), Js('sk'), Js('sl'), Js('sm'), Js('sn'), Js('sp'), Js('sph'), Js('sr'), Js('ss'), Js('st'), Js('str'), Js('sth'), Js('sz'), Js('th'), Js('tl'), Js('tm'), Js('tn'), Js('tr'), Js('thr'), Js('thn'), Js('thm'), Js('tch')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('g'), Js('h'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nd'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('x')]))
pass
pass


# Add lib to the module scope
civilizationNames = var.to_python()
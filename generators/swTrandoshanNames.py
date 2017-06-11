__all__ = ['swTrandoshanNames']

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
            if ((var.get('i')%Js(2.0))!=Js(0.0)):
                while (var.get('rnd10')<Js(7.0)):
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(10.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd5')<Js(10.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('bl'), Js('br'), Js('c'), Js('ch'), Js('cl'), Js('cr'), Js('d'), Js('dh'), Js('dr'), Js('fr'), Js('g'), Js('gh'), Js('gr'), Js('grr'), Js('gwh'), Js('h'), Js('hr'), Js('hss'), Js('j'), Js('k'), Js('khr'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('mr'), Js('n'), Js('nr'), Js('nrr'), Js('p'), Js('pr'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('sk'), Js('sl'), Js('ss'), Js('ssk'), Js('sstr'), Js('st'), Js('thr'), Js('t'), Js('tr'), Js('tsh'), Js('tss'), Js('v'), Js('vr'), Js('w'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('y'), Js('uu'), Js('ee'), Js('aa'), Js('oo'), Js('ai'), Js('ui'), Js('ey')]))
var.put('nm3', Js([Js('ch'), Js('cr'), Js('d'), Js('dfr'), Js('dg'), Js('g'), Js('gg'), Js('gr'), Js('hhm'), Js('hs'), Js('k'), Js('khss'), Js('kk'), Js('kr'), Js('ks'), Js('kt'), Js('l'), Js('ld'), Js('lf'), Js('ll'), Js('lt'), Js('m'), Js('mr'), Js('n'), Js('nd'), Js('ng'), Js('nk'), Js('nn'), Js('nt'), Js('nv'), Js('ph'), Js('qz'), Js('r'), Js('rd'), Js('rk'), Js('rn'), Js('rr'), Js('rth'), Js('rtsn'), Js('s'), Js('sd'), Js('sh'), Js('sn'), Js('ss'), Js('sskr'), Js('t'), Js('tl'), Js('tt'), Js('v'), Js('vr'), Js('z'), Js('zzm')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('ff'), Js('g'), Js('gg'), Js('h'), Js('hk'), Js('hssk'), Js('k'), Js('kk'), Js('kss'), Js('kt'), Js('l'), Js('ll'), Js('mx'), Js('n'), Js('nk'), Js('pp'), Js('q'), Js('r'), Js('rg'), Js('rj'), Js('rk'), Js('rkh'), Js('rq'), Js('rr'), Js('rrng'), Js('rrsk'), Js('rsk'), Js('rssk'), Js('rst'), Js('rt'), Js('rth'), Js('s'), Js('sh'), Js('shk'), Js('sk'), Js('ss'), Js('ssc'), Js('ssh'), Js('ssk'), Js('sskk'), Js('sst'), Js('t'), Js('tch'), Js('tt'), Js('v'), Js('w'), Js('x'), Js('xx'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('bl'), Js('cl'), Js('ch'), Js('cr'), Js('dh'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gh'), Js('gr'), Js('h'), Js('hs'), Js('k'), Js('kh'), Js('kl'), Js('kn'), Js('km'), Js('l'), Js('m'), Js('ms'), Js('mss'), Js('mh'), Js('n'), Js('ns'), Js('nh'), Js('p'), Js('pr'), Js('q'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('ss'), Js('sl'), Js('sm'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('ts'), Js('v'), Js('w'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('y'), Js('uu'), Js('ee'), Js('aa'), Js('oo'), Js('ai')]))
var.put('nm7', Js([Js('ch'), Js('d'), Js('dw'), Js('f'), Js('ff'), Js('g'), Js('gg'), Js('gl'), Js('h'), Js('hh'), Js('hr'), Js('hs'), Js('hss'), Js('k'), Js('ks'), Js('khs'), Js('l'), Js('ls'), Js('lss'), Js('ll'), Js('lf'), Js('lm'), Js('ln'), Js('ld'), Js('m'), Js('ml'), Js('n'), Js('nl'), Js('nd'), Js('nc'), Js('ph'), Js('r'), Js('rs'), Js('rl'), Js('rt'), Js('rth'), Js('rg'), Js('sl'), Js('ss'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('tt'), Js('tl'), Js('v'), Js('z')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('ff'), Js('h'), Js('k'), Js('kss'), Js('l'), Js('m'), Js('n'), Js('nn'), Js('rkh'), Js('s'), Js('ss'), Js('sh'), Js('ssh'), Js('t'), Js('th')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('hs'), Js('hss'), Js('hsk'), Js('j'), Js('jh'), Js('jhc'), Js('k'), Js('kl'), Js('m'), Js('n'), Js('r'), Js('s'), Js('ss'), Js('sm'), Js('st'), Js('sv'), Js('t'), Js('tr'), Js('ts'), Js('v'), Js('vl'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('y'), Js('ea'), Js('aa'), Js('oo'), Js('eo'), Js('ee'), Js('au')]))
var.put('nm11', Js([Js('br'), Js('b'), Js('cr'), Js('cd'), Js('d'), Js('dg'), Js('dm'), Js('dr'), Js('dr'), Js('g'), Js('gg'), Js('gr'), Js('gs'), Js('gl'), Js('k'), Js('kk'), Js('kr'), Js('ks'), Js('kl'), Js('l'), Js('ll'), Js('ls'), Js('m'), Js('mm'), Js('mr'), Js('ms'), Js('n'), Js('nn'), Js('ns'), Js('nl'), Js('ng'), Js('q'), Js('r'), Js('rs'), Js('rz'), Js('rd'), Js('rr'), Js('s'), Js('ss'), Js('sd'), Js('sl'), Js('sg'), Js('tn'), Js('v'), Js('vv')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('gg'), Js('gh'), Js('hk'), Js('k'), Js('kt'), Js('l'), Js('n'), Js('r'), Js('rn'), Js('rs'), Js('s'), Js('sss'), Js('st'), Js('ssk'), Js('sch'), Js('ss'), Js('t'), Js('tch'), Js('z')]))
pass
pass


# Add lib to the module scope
swTrandoshanNames = var.to_python()
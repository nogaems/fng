__all__ = ['swWookieNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(4.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd5'))))
                    else:
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd9')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(2.0)):
                    while (var.get('rnd')<Js(15.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(15.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(5.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd5'))))
                        else:
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('c'), Js('ch'), Js('chr'), Js('d'), Js('drrl'), Js('dr'), Js('drl'), Js('f'), Js('fr'), Js('g'), Js('gr'), Js('grr'), Js('grrw'), Js('gw'), Js('h'), Js('hr'), Js('j'), Js('k'), Js('kh'), Js('kk'), Js('kr'), Js('krr'), Js('krrs'), Js('l'), Js('m'), Js('mr'), Js('n'), Js('q'), Js('r'), Js('rh'), Js('rr'), Js('s'), Js('sh'), Js('sn'), Js('snr'), Js('snrr'), Js('snrl'), Js('sp'), Js('st'), Js('t'), Js('tr'), Js('tvr'), Js('tvrr'), Js('trr'), Js('v'), Js('vr'), Js('w'), Js('wh'), Js('wr'), Js('wrh'), Js('wrrl'), Js('wrr'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('aaa'), Js('ae'), Js('ai'), Js('ao'), Js('aoa'), Js('au'), Js('ay'), Js('ayy'), Js('ee'), Js('eee'), Js('eeo'), Js('eo'), Js('eu'), Js('ia'), Js('iaa'), Js('ie'), Js('ii'), Js('ioe'), Js('iya'), Js('iyy'), Js('oa'), Js('oo'), Js('ooa'), Js('ooo'), Js('ou'), Js('oua'), Js('ua'), Js('uaa'), Js('uu'), Js('uy'), Js('y'), Js('ya'), Js('yi'), Js('yy'), Js('yyy')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('br'), Js('c'), Js('cc'), Js('ch'), Js('d'), Js('dd'), Js('f'), Js('ff'), Js('fr'), Js('g'), Js('gg'), Js('ggl'), Js('gh'), Js('ghr'), Js('gr'), Js('h'), Js('hnch'), Js('hr'), Js('j'), Js('jj'), Js('k'), Js('kch'), Js('kk'), Js('kt'), Js('l'), Js('lb'), Js('lgh'), Js('lghr'), Js('ll'), Js('llffw'), Js('lm'), Js('ln'), Js('lp'), Js('lrr'), Js('lw'), Js('m'), Js('mb'), Js('mc'), Js('mgr'), Js('mm'), Js('mn'), Js('mp'), Js('n'), Js('nch'), Js('nd'), Js('ng'), Js('nh'), Js('nl'), Js('nn'), Js('nnk'), Js('ns'), Js('nt'), Js('p'), Js('pp'), Js('r'), Js('rb'), Js('rc'), Js('rch'), Js('rd'), Js('rdr'), Js('rf'), Js('rff'), Js('rfh'), Js('rg'), Js('rk'), Js('rkk'), Js('rl'), Js('rr'), Js('rrf'), Js('rrfh'), Js('rrr'), Js('rrw'), Js('rt'), Js('rv'), Js('rw'), Js('rww'), Js('s'), Js('sch'), Js('sh'), Js('sht'), Js('sn'), Js('ssh'), Js('st'), Js('t'), Js('tb'), Js('tc'), Js('tch'), Js('th'), Js('thk'), Js('thr'), Js('thrr'), Js('thrrr'), Js('tt'), Js('tw'), Js('v'), Js('vg'), Js('vv'), Js('w'), Js('wb'), Js('wd'), Js('whhr'), Js('whr'), Js('wk'), Js('wr'), Js('wrr'), Js('wrrh'), Js('ww'), Js('y'), Js('zn'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('ck'), Js('drr'), Js('drrl'), Js('h'), Js('hn'), Js('hr'), Js('hrr'), Js('k'), Js('kk'), Js('kk'), Js('kkk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nch'), Js('nk'), Js('r'), Js('rd'), Js('rk'), Js('rl'), Js('rm'), Js('rph'), Js('rr'), Js('rrr'), Js('s'), Js('sch'), Js('sh'), Js('shk'), Js('ss'), Js('st'), Js('t'), Js('v'), Js('vv'), Js('w'), Js('wk'), Js('wl'), Js('wn'), Js('wr')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('bh'), Js('c'), Js('d'), Js('dr'), Js('dh'), Js('dhr'), Js('f'), Js('fr'), Js('g'), Js('gch'), Js('ghr'), Js('gr'), Js('gw'), Js('h'), Js('hw'), Js('hwr'), Js('j'), Js('k'), Js('kr'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('rr'), Js('rh'), Js('rhr'), Js('s'), Js('shr'), Js('t'), Js('w'), Js('wh'), Js('wr'), Js('whr')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ie'), Js('ia'), Js('oe'), Js('ay'), Js('ayy'), Js('ua'), Js('aaa'), Js('aa'), Js('y'), Js('ay'), Js('yo'), Js('ae'), Js('aa'), Js('yy'), Js('eu'), Js('oo')]))
var.put('nm7', Js([Js('b'), Js('bb'), Js('bh'), Js('c'), Js('cc'), Js('ch'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('gh'), Js('ghr'), Js('h'), Js('hl'), Js('hb'), Js('hlb'), Js('ht'), Js('k'), Js('kk'), Js('kh'), Js('kl'), Js('l'), Js('lr'), Js('lg'), Js('ld'), Js('ll'), Js('lm'), Js('ln'), Js('m'), Js('mb'), Js('mc'), Js('mm'), Js('mn'), Js('n'), Js('nch'), Js('ng'), Js('ngl'), Js('nb'), Js('nm'), Js('nn'), Js('p'), Js('pr'), Js('r'), Js('rc'), Js('rgl'), Js('rr'), Js('rrl'), Js('rrr'), Js('rrs'), Js('s'), Js('sst'), Js('st'), Js('t'), Js('thn'), Js('tm'), Js('tt'), Js('v'), Js('vv'), Js('w'), Js('wl'), Js('wr')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('ck'), Js('gn'), Js('gnh'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nh'), Js('r'), Js('rl'), Js('rr'), Js('rrl'), Js('s'), Js('sh'), Js('shk'), Js('w')]))
pass
pass


# Add lib to the module scope
swWookieNames = var.to_python()
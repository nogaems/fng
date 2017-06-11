__all__ = ['barbarianNames']

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
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        if (var.get('rnd2')<Js(5.0)):
                            while (var.get('rnd4')<Js(5.0)):
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        if (var.get('rnd2')<Js(5.0)):
                            while (var.get('rnd4')<Js(5.0)):
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        if ((var.get('rnd2')<Js(5.0)) or (var.get('rnd4')<Js(5.0))):
                            while (var.get('rnd6')<Js(5.0)):
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((var.get('nm2').get(var.get('rnd'))+var.get('nm1').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        if (var.get('rnd')<Js(3.0)):
                            while (var.get('rnd4')<Js(3.0)):
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', ((((var.get('nm2').get(var.get('rnd'))+var.get('nm1').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm1').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        if (var.get('rnd')<Js(3.0)):
                            while (var.get('rnd4')<Js(3.0)):
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        if ((var.get('rnd')<Js(3.0)) or (var.get('rnd4')<Js(3.0))):
                            while (var.get('rnd6')<Js(3.0)):
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', ((((((var.get('nm2').get(var.get('rnd'))+var.get('nm1').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm1').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm1').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('ae'), Js('au'), Js('ei'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm2', Js([Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('bh'), Js('d'), Js('dr'), Js('dh'), Js('f'), Js('fr'), Js('g'), Js('gh'), Js('gr'), Js('gl'), Js('h'), Js('hy'), Js('hr'), Js('j'), Js('k'), Js('kh'), Js('kr'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('rh'), Js('s'), Js('sk'), Js('sg'), Js('sm'), Js('sn'), Js('st'), Js('t'), Js('th'), Js('thr'), Js('ty'), Js('v'), Js('y')]))
var.put('nm3', Js([Js('bl'), Js('br'), Js('d'), Js('db'), Js('dbr'), Js('dd'), Js('ddg'), Js('dg'), Js('dl'), Js('dm'), Js('dr'), Js('dv'), Js('f'), Js('fd'), Js('fgr'), Js('fk'), Js('fl'), Js('fn'), Js('fr'), Js('fst'), Js('fv'), Js('g'), Js('gb'), Js('gd'), Js('gf'), Js('gg'), Js('ggv'), Js('gl'), Js('gn'), Js('gr'), Js('gss'), Js('gv'), Js('k'), Js('kk'), Js('l'), Js('lb'), Js('lc'), Js('ld'), Js('ldr'), Js('lf'), Js('lfr'), Js('lg'), Js('lgr'), Js('lk'), Js('ll'), Js('llg'), Js('llk'), Js('llv'), Js('lm'), Js('ln'), Js('lp'), Js('lr'), Js('ls'), Js('lsk'), Js('lsn'), Js('lst'), Js('lsv'), Js('lt'), Js('lv'), Js('m'), Js('md'), Js('mk'), Js('ml'), Js('mm'), Js('ms'), Js('n'), Js('nb'), Js('nd'), Js('ndr'), Js('ng'), Js('nl'), Js('nn'), Js('nng'), Js('nr'), Js('nsk'), Js('nt'), Js('nv'), Js('nw'), Js('p'), Js('pl'), Js('pp'), Js('pr'), Js('r'), Js('rb'), Js('rd'), Js('rdg'), Js('rf'), Js('rg'), Js('rgr'), Js('rk'), Js('rkm'), Js('rl'), Js('rls'), Js('rm'), Js('rn'), Js('rng'), Js('rngr'), Js('rnh'), Js('rnk'), Js('rns'), Js('rnv'), Js('rr'), Js('rst'), Js('rt'), Js('rth'), Js('rtm'), Js('rv'), Js('s'), Js('sb'), Js('sbr'), Js('sg'), Js('sgr'), Js('sk'), Js('sl'), Js('sm'), Js('sn'), Js('sr'), Js('ssk'), Js('st'), Js('stm'), Js('str'), Js('sv'), Js('t'), Js('tg'), Js('th'), Js('thg'), Js('thn'), Js('thr'), Js('thv'), Js('tm'), Js('tr'), Js('tt'), Js('ttf'), Js('tv'), Js('v'), Js('yv'), Js('z'), Js('zg'), Js('zl'), Js('zn')]))
var.put('nm4', Js([Js('d'), Js('dr'), Js('f'), Js('g'), Js('kr'), Js('k'), Js('l'), Js('ld'), Js('lf'), Js('lk'), Js('ll'), Js('lr'), Js('m'), Js('mm'), Js('n'), Js('nd'), Js('nn'), Js('r'), Js('rd'), Js('rn'), Js('rr'), Js('s'), Js('th'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('bh'), Js('ch'), Js('d'), Js('dh'), Js('f'), Js('fr'), Js('g'), Js('gh'), Js('gr'), Js('gw'), Js('gl'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('st'), Js('sv'), Js('t'), Js('th'), Js('thr'), Js('tr'), Js('v'), Js('w')]))
var.put('nm6', Js([Js('ae'), Js('ea'), Js('ie'), Js('ei'), Js('io'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm7', Js([Js('bj'), Js('c'), Js('d'), Js('dd'), Js('df'), Js('dl'), Js('dr'), Js('f'), Js('ff'), Js('fl'), Js('fn'), Js('fr'), Js('fth'), Js('g'), Js('gd'), Js('gm'), Js('gn'), Js('gnh'), Js('gr'), Js('h'), Js('hh'), Js('k'), Js('l'), Js('ld'), Js('lf'), Js('lfh'), Js('lg'), Js('lgr'), Js('lh'), Js('lk'), Js('ll'), Js('lm'), Js('lr'), Js('ls'), Js('lv'), Js('m'), Js('mm'), Js('n'), Js('nd'), Js('ndr'), Js('ng'), Js('ngr'), Js('ngv'), Js('nh'), Js('nl'), Js('nn'), Js('nnh'), Js('nr'), Js('ns'), Js('nt'), Js('nv'), Js('r'), Js('rd'), Js('rf'), Js('rg'), Js('rgh'), Js('rgr'), Js('rh'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rnd'), Js('rng'), Js('rr'), Js('rst'), Js('rt'), Js('rth'), Js('rtr'), Js('rv'), Js('s'), Js('sb'), Js('sd'), Js('sg'), Js('sh'), Js('sl'), Js('st'), Js('stn'), Js('str'), Js('sv'), Js('t'), Js('thr'), Js('tk'), Js('tr'), Js('tt'), Js('tth'), Js('v'), Js('y'), Js('yj'), Js('ym'), Js('yn')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js('f'), Js('g'), Js('h'), Js('l'), Js('n'), Js('nn'), Js('s'), Js('sh'), Js('th'), Js('y')]))
pass
pass


# Add lib to the module scope
barbarianNames = var.to_python()
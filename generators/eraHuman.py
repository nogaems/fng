__all__ = ['eraHuman']

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
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('rnd5')<Js(5.0)):
                    var.put('rnd4', Js(0.0))
                if (var.get('i')<Js(6.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    if (var.get('rnd')<Js(4.0)):
                        while (var.get('rnd4')<Js(5.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4'))))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fl'), Js('fr'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kn'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sl'), Js('sv'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('w'), Js('y')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ie'), Js('ae'), Js('oo'), Js('ai'), Js('ea'), Js('aa'), Js('ei'), Js('ui'), Js('uo'), Js('oa')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('ch'), Js('d'), Js('db'), Js('dg'), Js('dl'), Js('dr'), Js('fr'), Js('ft'), Js('g'), Js('gl'), Js('gm'), Js('h'), Js('hw'), Js('j'), Js('k'), Js('l'), Js('lb'), Js('lbr'), Js('lc'), Js('ld'), Js('lf'), Js('lh'), Js('lk'), Js('ll'), Js('lm'), Js('lr'), Js('lst'), Js('lt'), Js('lw'), Js('m'), Js('mb'), Js('mbl'), Js('mpt'), Js('n'), Js('nbr'), Js('nc'), Js('nd'), Js('nds'), Js('ng'), Js('ngr'), Js('ngv'), Js('ngw'), Js('nn'), Js('ns'), Js('r'), Js('rc'), Js('rd'), Js('rdl'), Js('rdr'), Js('rds'), Js('rgr'), Js('rk'), Js('rm'), Js('rmm'), Js('rmn'), Js('rn'), Js('rr'), Js('rs'), Js('rsh'), Js('rt'), Js('rth'), Js('rtl'), Js('rtr'), Js('rv'), Js('rw'), Js('rz'), Js('s'), Js('sb'), Js('sl'), Js('sth'), Js('str'), Js('stv'), Js('t'), Js('tch'), Js('th'), Js('thlb'), Js('thm'), Js('v'), Js('vr'), Js('w'), Js('wl'), Js('yn')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('ck'), Js('d'), Js('f'), Js('g'), Js('gh'), Js('l'), Js('ld'), Js('lf'), Js('ll'), Js('lt'), Js('m'), Js('mb'), Js('n'), Js('nd'), Js('ng'), Js('nt'), Js('r'), Js('rd'), Js('rn'), Js('rr'), Js('rst'), Js('rt'), Js('rth'), Js('s'), Js('sk'), Js('st'), Js('t'), Js('th'), Js('w'), Js('y')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('g'), Js('gr'), Js('gl'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('pr'), Js('ph'), Js('s'), Js('sl'), Js('sh'), Js('sr'), Js('t'), Js('th'), Js('tr'), Js('w'), Js('y')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('ia'), Js('ua'), Js('ae'), Js('ee'), Js('ie'), Js('ea')]))
var.put('nm7', Js([Js('bb'), Js('br'), Js('c'), Js('d'), Js('dd'), Js('dn'), Js('f'), Js('ff'), Js('fr'), Js('fn'), Js('gn'), Js('g'), Js('gg'), Js('hr'), Js('hn'), Js('nl'), Js('l'), Js('ld'), Js('ll'), Js('lm'), Js('ln'), Js('lb'), Js('ls'), Js('lv'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('ng'), Js('nn'), Js('nm'), Js('nd'), Js('nw'), Js('ns'), Js('p'), Js('ph'), Js('r'), Js('rd'), Js('rn'), Js('rl'), Js('rm'), Js('rr'), Js('rs'), Js('rw'), Js('rg'), Js('rtr'), Js('s'), Js('sn'), Js('sl'), Js('sh'), Js('sm'), Js('ss'), Js('t'), Js('th'), Js('tr'), Js('tn'), Js('v'), Js('w')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('l'), Js('ld'), Js('n'), Js('s'), Js('t')]))
pass
pass


# Add lib to the module scope
eraHuman = var.to_python()
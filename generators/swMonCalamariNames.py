__all__ = ['swMonCalamariNames']

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
                while (var.get('rnd7')<Js(4.0)):
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
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('namelast')))
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
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(5.0)):
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gh'), Js('gr'), Js('h'), Js('j'), Js('jh'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('mx'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('tr'), Js('v'), Js('vc'), Js('vr'), Js('y')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('oo'), Js('ee'), Js('oe'), Js('io'), Js('ua'), Js('ae'), Js('oa'), Js('ie'), Js('ai'), Js('uu'), Js('ea')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('c'), Js('ck'), Js('ckd'), Js('ckl'), Js('ckr'), Js('dr'), Js('fw'), Js('g'), Js('ggr'), Js('h'), Js('hd'), Js('j'), Js('k'), Js('kb'), Js('kk'), Js('kl'), Js('km'), Js('l'), Js('lb'), Js('lbr'), Js('ld'), Js('lk'), Js('lkph'), Js('ll'), Js('lm'), Js('lp'), Js('lsp'), Js('lt'), Js('ly'), Js('m'), Js('mb'), Js('mbr'), Js('mck'), Js('mm'), Js('n'), Js('nd'), Js('ndl'), Js('ng'), Js('nk'), Js('nl'), Js('nq'), Js('ns'), Js('ph'), Js('r'), Js('rb'), Js('rch'), Js('rg'), Js('rl'), Js('rn'), Js('rpf'), Js('rr'), Js('rsh'), Js('rt'), Js('s'), Js('sf'), Js('shn'), Js('ss'), Js('t'), Js('th'), Js('tr'), Js('tt'), Js('vr'), Js('x'), Js('xl'), Js('yg'), Js('z'), Js('zl')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ck'), Js('ff'), Js('h'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('ln'), Js('m'), Js('n'), Js('ns'), Js('nt'), Js('r'), Js('rl'), Js('rn'), Js('rt'), Js('rth'), Js('rx'), Js('s'), Js('sh'), Js('ss'), Js('ss'), Js('sz'), Js('t'), Js('th'), Js('x'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('f'), Js('h'), Js('j'), Js('jh'), Js('k'), Js('kl'), Js('l'), Js('m'), Js('mh'), Js('n'), Js('nh'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('vr'), Js('y')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ie'), Js('ue'), Js('ee'), Js('ia'), Js('ae')]))
var.put('nm7', Js([Js('b'), Js('bt'), Js('d'), Js('dh'), Js('dn'), Js('f'), Js('fw'), Js('fn'), Js('fl'), Js('hl'), Js('hh'), Js('hn'), Js('hm'), Js('hl'), Js('k'), Js('kh'), Js('ky'), Js('kl'), Js('km'), Js('kn'), Js('l'), Js('lb'), Js('lh'), Js('lm'), Js('ln'), Js('ll'), Js('m'), Js('mb'), Js('mn'), Js('md'), Js('n'), Js('nd'), Js('nl'), Js('nh'), Js('nk'), Js('nky'), Js('nm'), Js('nn'), Js('r'), Js('rd'), Js('rg'), Js('rh'), Js('s'), Js('sh'), Js('sm'), Js('so'), Js('w'), Js('y'), Js('z')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('m'), Js('n'), Js('nt'), Js('r'), Js('s')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('g'), Js('gh'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('vr'), Js('w')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ou'), Js('ia'), Js('ua'), Js('ai'), Js('oo'), Js('aa'), Js('ee')]))
var.put('nm11', Js([Js('b'), Js('bb'), Js('br'), Js('ch'), Js('ckb'), Js('ckd'), Js('d'), Js('dd'), Js('dl'), Js('dr'), Js('g'), Js('gr'), Js('gb'), Js('h'), Js('hd'), Js('k'), Js('kb'), Js('l'), Js('lb'), Js('lk'), Js('lg'), Js('lgr'), Js('lw'), Js('ld'), Js('m'), Js('mg'), Js('md'), Js('mb'), Js('n'), Js('md'), Js('mb'), Js('ng'), Js('p'), Js('pt'), Js('r'), Js('rc'), Js('rr'), Js('rt'), Js('rg'), Js('rb'), Js('rgr'), Js('s'), Js('spl'), Js('sc'), Js('shc'), Js('sr'), Js('th'), Js('thr'), Js('tr'), Js('tt'), Js('vn'), Js('y')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bb'), Js('c'), Js('hb'), Js('hd'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('ls'), Js('n'), Js('r'), Js('s'), Js('sch'), Js('ss'), Js('x'), Js('xx'), Js('xz')]))
pass
pass


# Add lib to the module scope
swMonCalamariNames = var.to_python()
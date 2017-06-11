__all__ = ['swMandalorianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                while (var.get('rnd7')<Js(5.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                while (var.get('rnd10')<Js(5.0)):
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(10.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(7.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('g'), Js('gh'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nj'), Js('p'), Js('r'), Js('rh'), Js('s'), Js('t'), Js('tr'), Js('th'), Js('thr'), Js('v'), Js('vr'), Js('w'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('o'), Js('o'), Js('o'), Js('u'), Js('u'), Js('u'), Js('a'), Js('o'), Js('u'), Js('ae'), Js('uu'), Js('ii'), Js('aa'), Js('ea'), Js('ai'), Js('ee'), Js('io'), Js('oe')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('j'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('p'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('v'), Js('y'), Js('b'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('b'), Js('bb'), Js('br'), Js('bz'), Js('d'), Js('dd'), Js('dz'), Js('dr'), Js('g'), Js('gg'), Js('gb'), Js('gd'), Js('ht'), Js('j'), Js('k'), Js('kk'), Js('kb'), Js('kd'), Js('kr'), Js('ksh'), Js('l'), Js('ll'), Js('lm'), Js('lr'), Js('m'), Js('mz'), Js('n'), Js('nd'), Js('ng'), Js('nn'), Js('nt'), Js('nz'), Js('p'), Js('ps'), Js('r'), Js('rbr'), Js('rd'), Js('rg'), Js('rk'), Js('rr'), Js('rst'), Js('rt'), Js('rth'), Js('s'), Js('sc'), Js('ss'), Js('t'), Js('ty'), Js('v'), Js('y'), Js('zd')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ck'), Js('d'), Js('dth'), Js('g'), Js('gg'), Js('gr'), Js('j'), Js('k'), Js('l'), Js('ld'), Js('m'), Js('n'), Js('ng'), Js('nk'), Js('nn'), Js('nx'), Js('r'), Js('rk'), Js('rr'), Js('rt'), Js('s'), Js('t'), Js('th'), Js('ts'), Js('x'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('d'), Js('f'), Js('h'), Js('j'), Js('jh'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('vh'), Js('w'), Js('wh'), Js('x'), Js('z'), Js('zh')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('aa'), Js('ao'), Js('ay'), Js('oo'), Js('ae'), Js('ai'), Js('ia')]))
var.put('nm7', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('j'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('p'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('v'), Js('y'), Js('b'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('b'), Js('c'), Js('g'), Js('k'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('b'), Js('c'), Js('g'), Js('k'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('b'), Js('c'), Js('g'), Js('k'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('b'), Js('bb'), Js('c'), Js('ch'), Js('d'), Js('dh'), Js('f'), Js('ff'), Js('g'), Js('h'), Js('hh'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('mn'), Js('mr'), Js('ms'), Js('n'), Js('nr'), Js('nm'), Js('nt'), Js('ph'), Js('r'), Js('rr'), Js('rs'), Js('rt'), Js('rn'), Js('rm'), Js('rl'), Js('s'), Js('ss'), Js('sh'), Js('st'), Js('sth'), Js('sm'), Js('sn'), Js('sl'), Js('sk'), Js('t'), Js('th'), Js('v'), Js('vl')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('h'), Js('k'), Js('l'), Js('lk'), Js('m'), Js('n'), Js('rn'), Js('s'), Js('sh'), Js('th')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('c'), Js('ch'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('sk'), Js('sp'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('w'), Js('wr'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('y'), Js('oo'), Js('ou'), Js('ai'), Js('ua'), Js('au'), Js('uu')]))
var.put('nm11', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('j'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('p'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('v'), Js('y'), Js('b'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('b'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('gg'), Js('gr'), Js('h'), Js('k'), Js('kk'), Js('l'), Js('lb'), Js('lg'), Js('lk'), Js('ll'), Js('m'), Js('n'), Js('nk'), Js('pm'), Js('r'), Js('rh'), Js('rk'), Js('rm'), Js('rn'), Js('rr'), Js('rv'), Js('rvh'), Js('s'), Js('t'), Js('v'), Js('vh'), Js('x'), Js('zl')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('gg'), Js('gh'), Js('hl'), Js('k'), Js('l'), Js('ll'), Js('n'), Js('ng'), Js('ngh'), Js('nch'), Js('r'), Js('rd'), Js('rr'), Js('rs'), Js('rn'), Js('rt'), Js('s'), Js('ss'), Js('st'), Js('t'), Js('tt'), Js('wr')]))
var.put('nm13', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('j'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('p'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('v'), Js('b'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v')]))
pass
pass


# Add lib to the module scope
swMandalorianNames = var.to_python()
__all__ = ['diabloDemon']

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
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('c'), Js('cr'), Js('ch'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('sl'), Js('str'), Js('sthr'), Js('sth'), Js('sr'), Js('t'), Js('th'), Js('tr'), Js('thr'), Js('v'), Js('vr'), Js('wr'), Js('x'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('io'), Js('oi'), Js('aa'), Js('iu'), Js('ia'), Js('ou'), Js('ea'), Js('uu'), Js('au'), Js('ao')]))
var.put('nm3', Js([Js('b'), Js('bl'), Js('br'), Js('c'), Js('d'), Js('dd'), Js('dr'), Js('g'), Js('gg'), Js('gh'), Js('gn'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('kr'), Js('kk'), Js('kn'), Js('lf'), Js('lth'), Js('lt'), Js('lm'), Js('lr'), Js('ld'), Js('m'), Js('mm'), Js('n'), Js('ng'), Js('nth'), Js('nd'), Js('nr'), Js('nt'), Js('ph'), Js('phr'), Js('r'), Js('rch'), Js('rp'), Js('rr'), Js('rt'), Js('rzh'), Js('rs'), Js('rz'), Js('rd'), Js('rk'), Js('s'), Js('sh'), Js('ss'), Js('sz'), Js('str'), Js('t'), Js('th'), Js('tr'), Js('thr'), Js('x'), Js('xtr'), Js('xx'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('hr'), Js('k'), Js('l'), Js('n'), Js('r'), Js('rm'), Js('rr'), Js('rth'), Js('s'), Js('ss'), Js('th'), Js('tt'), Js('w'), Js('x'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('bl'), Js('c'), Js('ch'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gl'), Js('gr'), Js('gh'), Js('fr'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('pr'), Js('phr'), Js('pl'), Js('r'), Js('s'), Js('sh'), Js('shr'), Js('st'), Js('sth'), Js('sthr'), Js('sl'), Js('t'), Js('th'), Js('thr'), Js('v'), Js('w'), Js('wr'), Js('x'), Js('y'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('io'), Js('oi'), Js('aa'), Js('iu'), Js('ia'), Js('ou'), Js('ea'), Js('uu'), Js('au'), Js('ao')]))
var.put('nm7', Js([Js('b'), Js('bb'), Js('br'), Js('bh'), Js('c'), Js('ch'), Js('d'), Js('dh'), Js('dd'), Js('dr'), Js('g'), Js('gn'), Js('gr'), Js('h'), Js('hr'), Js('hl'), Js('k'), Js('kh'), Js('kr'), Js('l'), Js('lf'), Js('lph'), Js('lth'), Js('lm'), Js('ln'), Js('ld'), Js('ll'), Js('lr'), Js('m'), Js('mm'), Js('ml'), Js('mf'), Js('n'), Js('nn'), Js('ng'), Js('nth'), Js('ns'), Js('nt'), Js('ndr'), Js('ph'), Js('phr'), Js('r'), Js('rr'), Js('rph'), Js('rl'), Js('rs'), Js('rn'), Js('s'), Js('sh'), Js('ss'), Js('sz'), Js('sth'), Js('str'), Js('t'), Js('th'), Js('tr'), Js('tt'), Js('thr'), Js('x'), Js('xx'), Js('xh'), Js('z'), Js('zz')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n'), Js('s'), Js('th'), Js('z')]))
pass
pass


# Add lib to the module scope
diabloDemon = var.to_python()
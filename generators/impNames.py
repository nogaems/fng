__all__ = ['impNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd')<Js(7.0)):
                    while (var.get('rnd5')<Js(5.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.put('tyr', ((var.get('Math').callprop('random')*Js(300.0))|Js(0.0)))
            if PyJsStrictEq(var.get('tyr'),Js(10.0)):
                var.put('names', Js('Tyrion Lannister (just kidding)'))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('cr'), Js('cy'), Js('d'), Js('dr'), Js('g'), Js('gn'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('ky'), Js('l'), Js('n'), Js('p'), Js('q'), Js('qr'), Js('r'), Js('sh'), Js('t'), Js('tr'), Js('ty'), Js('v'), Js('x'), Js('y'), Js('z'), Js('zr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('ia'), Js('iu'), Js('ai'), Js('aa')]))
var.put('nm3', Js([Js('bb'), Js('bh'), Js('bj'), Js('bk'), Js('bl'), Js('bq'), Js('br'), Js('gb'), Js('gf'), Js('gh'), Js('gl'), Js('gm'), Js('gn'), Js('gr'), Js('kb'), Js('kh'), Js('kj'), Js('kk'), Js('kl'), Js('km'), Js('kn'), Js('kr'), Js('lb'), Js('lj'), Js('ll'), Js('ln'), Js('lp'), Js('lr'), Js('lt'), Js('ph'), Js('pk'), Js('pn'), Js('pp'), Js('pq'), Js('pr'), Js('rb'), Js('rj'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rp'), Js('rq'), Js('rr'), Js('rt'), Js('zb'), Js('zl'), Js('zm'), Js('zn'), Js('zp'), Js('zr'), Js('zt'), Js('cb'), Js('cl'), Js('cn'), Js('cq'), Js('cr'), Js('ct'), Js('cx'), Js('cz'), Js('dj'), Js('dr'), Js('dv'), Js('dz'), Js('fn'), Js('fr'), Js('nc'), Js('nd'), Js('ng'), Js('nj'), Js('nl'), Js('nt'), Js('qb'), Js('ql'), Js('qn'), Js('qq'), Js('qr'), Js('sc'), Js('sh'), Js('sk'), Js('sl'), Js('sm'), Js('sn'), Js('sq'), Js('sr'), Js('ss'), Js('st'), Js('str'), Js('sz'), Js('tc'), Js('th'), Js('tj'), Js('tn'), Js('xh'), Js('xn')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('ch'), Js('cr'), Js('cy'), Js('d'), Js('dr'), Js('gn'), Js('gr'), Js('kr'), Js('ky'), Js('qr'), Js('r'), Js('sz'), Js('t'), Js('tr'), Js('ty'), Js('v'), Js('x'), Js('y'), Js('z'), Js('zr')]))
var.put('nm6', Js([Js('c'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('t'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
impNames = var.to_python()
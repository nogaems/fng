__all__ = ['swHuttNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('namelast', ((((var.get('nm1').get(var.get('rnd8'))+var.get('nm2').get(var.get('rnd9')))+var.get('nm3').get(var.get('rnd10')))+var.get('nm2').get(var.get('rnd11')))+var.get('nm4').get(var.get('rnd12'))))
            else:
                while (var.get('rnd8')<Js(5.0)):
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                while (var.get('rnd12')<Js(9.0)):
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('namelast', ((var.get('nm1').get(var.get('rnd8'))+var.get('nm2').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd12'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(7.0)):
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('bw'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gl'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('pr'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('sk'), Js('sm'), Js('sp'), Js('sz'), Js('t'), Js('tr'), Js('v'), Js('w'), Js('wh'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('uu'), Js('ee'), Js('io'), Js('oo'), Js('eu'), Js('ua'), Js('ai'), Js('oa'), Js('oe'), Js('ae')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('bd'), Js('bs'), Js('ch'), Js('chr'), Js('d'), Js('dd'), Js('ddl'), Js('ff'), Js('ffr'), Js('g'), Js('gg'), Js('gh'), Js('gr'), Js('j'), Js('jj'), Js('k'), Js('kk'), Js('l'), Js('lb'), Js('ld'), Js('lg'), Js('ll'), Js('ln'), Js('lr'), Js('lt'), Js('m'), Js('mb'), Js('mdr'), Js('mr'), Js('n'), Js('nd'), Js('ng'), Js('ngr'), Js('nj'), Js('nn'), Js('nt'), Js('nv'), Js('ny'), Js('pp'), Js('q'), Js('r'), Js('rb'), Js('rbl'), Js('rchr'), Js('rd'), Js('rdr'), Js('rg'), Js('rgr'), Js('rk'), Js('rl'), Js('rp'), Js('rph'), Js('rr'), Js('rrb'), Js('rrg'), Js('rs'), Js('rt'), Js('rv'), Js('rz'), Js('s'), Js('sh'), Js('sk'), Js('skh'), Js('ss'), Js('st'), Js('t'), Js('th'), Js('tj'), Js('tt'), Js('v'), Js('w'), Js('wn'), Js('x'), Js('yb')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('g'), Js('gg'), Js('h'), Js('hl'), Js('k'), Js('l'), Js('lb'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('rd'), Js('rg'), Js('rgg'), Js('rm'), Js('s'), Js('sch'), Js('sh'), Js('sk'), Js('ss'), Js('th'), Js('x'), Js('z'), Js('zz')]))
pass
pass


# Add lib to the module scope
swHuttNames = var.to_python()
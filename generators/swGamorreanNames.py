__all__ = ['swGamorreanNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('namelast', ((var.get('nm1').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd8'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('namelast', ((((var.get('nm1').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd11')))+var.get('nm9').get(var.get('rnd8'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('bn'), Js('br'), Js('c'), Js('d'), Js('dr'), Js('g'), Js('gh'), Js('gl'), Js('gr'), Js('grr'), Js('grt'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('sc'), Js('sh'), Js('sl'), Js('sn'), Js('sq'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('eu'), Js('au'), Js('ee'), Js('oo'), Js('uu'), Js('ou'), Js('ua')]))
var.put('nm3', Js([Js('b'), Js('bn'), Js('br'), Js('d'), Js('dbr'), Js('fn'), Js('g'), Js('gb'), Js('ggt'), Js('gh'), Js('gl'), Js('gn'), Js('gr'), Js('gt'), Js('gz'), Js('kt'), Js('l'), Js('lg'), Js('ll'), Js('lr'), Js('m'), Js('mb'), Js('mm'), Js('mr'), Js('n'), Js('nf'), Js('ngf'), Js('nt'), Js('nth'), Js('r'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rt'), Js('sh'), Js('ss'), Js('t'), Js('th'), Js('thm'), Js('v'), Js('zz')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('ck'), Js('ckt'), Js('f'), Js('ff'), Js('g'), Js('gg'), Js('gh'), Js('k'), Js('kk'), Js('l'), Js('lk'), Js('m'), Js('n'), Js('ng'), Js('nn'), Js('nt'), Js('r'), Js('rc'), Js('rg'), Js('rk'), Js('rn'), Js('rp'), Js('rrp'), Js('rrt'), Js('rt'), Js('rth'), Js('s'), Js('ss'), Js('t'), Js('th'), Js('tt'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('bn'), Js('br'), Js('c'), Js('d'), Js('dr'), Js('g'), Js('gh'), Js('gl'), Js('gr'), Js('grr'), Js('grt'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('sc'), Js('sh'), Js('sl'), Js('sn'), Js('sq'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('x'), Js('z')]))
var.put('nm6', Js([Js('b'), Js('bn'), Js('br'), Js('d'), Js('dv'), Js('fbr'), Js('fn'), Js('g'), Js('gb'), Js('gg'), Js('gh'), Js('gl'), Js('gm'), Js('gn'), Js('gr'), Js('gsh'), Js('gv'), Js('km'), Js('l'), Js('ll'), Js('lly'), Js('ln'), Js('lr'), Js('m'), Js('mm'), Js('mr'), Js('mv'), Js('n'), Js('ndr'), Js('nf'), Js('ng'), Js('nr'), Js('nth'), Js('r'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('shr'), Js('sn'), Js('sr'), Js('t'), Js('th'), Js('thn'), Js('tr'), Js('vn'), Js('zs')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('cz'), Js('cs'), Js('f'), Js('ff'), Js('g'), Js('gg'), Js('gh'), Js('k'), Js('ks'), Js('l'), Js('ms'), Js('m'), Js('n'), Js('ns'), Js('nn'), Js('ng'), Js('r'), Js('rc'), Js('rf'), Js('rn'), Js('rq'), Js('rs'), Js('rr'), Js('rm'), Js('rth'), Js('s'), Js('ss'), Js('t'), Js('th'), Js('sh'), Js('sz'), Js('z')]))
var.put('nm8', Js([Js('b'), Js('bn'), Js('br'), Js('d'), Js('dbr'), Js('dv'), Js('fbr'), Js('fn'), Js('g'), Js('gb'), Js('gg'), Js('ggt'), Js('gh'), Js('gl'), Js('gm'), Js('gn'), Js('gr'), Js('gsh'), Js('gt'), Js('gv'), Js('gz'), Js('km'), Js('kt'), Js('l'), Js('lg'), Js('ll'), Js('lly'), Js('ln'), Js('lr'), Js('m'), Js('mb'), Js('mm'), Js('mr'), Js('mv'), Js('n'), Js('ndr'), Js('nf'), Js('ng'), Js('ngf'), Js('nr'), Js('nt'), Js('nth'), Js('r'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('rt'), Js('sh'), Js('shr'), Js('sn'), Js('sr'), Js('ss'), Js('t'), Js('th'), Js('thm'), Js('thn'), Js('tr'), Js('v'), Js('vn'), Js('zs'), Js('zz')]))
var.put('nm9', Js([Js('b'), Js('c'), Js('ck'), Js('ckt'), Js('cs'), Js('cz'), Js('f'), Js('ff'), Js('g'), Js('gg'), Js('gh'), Js('k'), Js('kk'), Js('ks'), Js('l'), Js('lk'), Js('m'), Js('ms'), Js('n'), Js('ng'), Js('nn'), Js('ns'), Js('nt'), Js('r'), Js('rc'), Js('rf'), Js('rg'), Js('rk'), Js('rm'), Js('rn'), Js('rp'), Js('rq'), Js('rr'), Js('rrp'), Js('rrt'), Js('rs'), Js('rt'), Js('rth'), Js('s'), Js('sh'), Js('ss'), Js('sz'), Js('t'), Js('th'), Js('tt'), Js('z')]))
pass
pass


# Add lib to the module scope
swGamorreanNames = var.to_python()
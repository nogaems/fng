__all__ = ['goblinNormal']

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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd2b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((var.get('nm5').get(var.get('rnd5'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((var.get('nm5').get(var.get('rnd5'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd2b')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            else:
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((var.get('nm1').get(var.get('rnd5'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd7'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd5'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd2b')))+var.get('nm4').get(var.get('rnd7'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('p'), Js('r'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('br'), Js('bl'), Js('cr'), Js('cl'), Js('ch'), Js('dr'), Js('fr'), Js('gr'), Js('gl'), Js('gn'), Js('kr'), Js('kl'), Js('pr'), Js('pl'), Js('str'), Js('st'), Js('sr'), Js('sl'), Js('tr'), Js('vr'), Js('wr'), Js('zr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ia'), Js('io'), Js('ee'), Js('aa'), Js('ui'), Js('ie'), Js('ea'), Js('oi')]))
var.put('nm3', Js([Js('b'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z'), Js('b'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z'), Js('b'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z'), Js('b'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z'), Js('bb'), Js('bd'), Js('bh'), Js('bl'), Js('bk'), Js('bn'), Js('br'), Js('bs'), Js('bt'), Js('bz'), Js('db'), Js('dd'), Js('df'), Js('dh'), Js('dl'), Js('dn'), Js('dr'), Js('ds'), Js('dv'), Js('dz'), Js(''), Js('gg'), Js('gb'), Js('gd'), Js('gh'), Js('gk'), Js('gl'), Js('gm'), Js('gn'), Js('gr'), Js('gs'), Js('gt'), Js('gz'), Js('hd'), Js('hb'), Js('hk'), Js('hn'), Js('hz'), Js('kl'), Js('kn'), Js('kz'), Js('kv'), Js('kk'), Js('lb'), Js('ld'), Js('lg'), Js('lk'), Js('ll'), Js('lr'), Js('ls'), Js('lt'), Js('lv'), Js('lz'), Js('mr'), Js('mv'), Js('mz'), Js('mt'), Js('nr'), Js('nv'), Js('nz'), Js('nt'), Js('rb'), Js('rd'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('rs'), Js('rt'), Js('rv'), Js('rz'), Js('sb'), Js('sd'), Js('sh'), Js('sk'), Js('sm'), Js('sn'), Js('sr'), Js('str'), Js('st'), Js('sv'), Js('sz'), Js('ss'), Js('tb'), Js('tl'), Js('tm'), Js('tn'), Js('tr'), Js('tv'), Js('tz'), Js('tt'), Js('vl'), Js('vn'), Js('vr'), Js('vz'), Js('zb'), Js('zd'), Js('zg'), Js('zl'), Js('zm'), Js('zn'), Js('zt')]))
var.put('nm4', Js([Js('c'), Js('g'), Js('k'), Js('l'), Js('q'), Js('r'), Js('t'), Js('x'), Js('z'), Js('nk'), Js('ld'), Js('rd'), Js('s'), Js('sz'), Js('zz'), Js('ng'), Js('kz'), Js('lb'), Js('rm'), Js('sb'), Js('bs'), Js('ts'), Js('cs'), Js('ct'), Js('gs'), Js('gz'), Js('kt'), Js('kx'), Js('lk'), Js('lx'), Js('rk'), Js('rt'), Js('rd'), Js('rx')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('bh'), Js('br'), Js('bl'), Js('cr'), Js('cl'), Js('ch'), Js('fr'), Js('fl'), Js('gr'), Js('gl'), Js('gn'), Js('kh'), Js('kl'), Js('ph'), Js('pr'), Js('sh'), Js('st'), Js('sr'), Js('sl'), Js('sw'), Js('th'), Js('thr'), Js('tr'), Js('vr'), Js('wr')]))
var.put('nm6', Js([Js('b'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('b'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('b'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('b'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('bb'), Js('bd'), Js('bh'), Js('bl'), Js('bk'), Js('bn'), Js('br'), Js('bs'), Js('bt'), Js('bz'), Js('fb'), Js('fl'), Js('fm'), Js('fn'), Js('fs'), Js('ft'), Js('gg'), Js('gb'), Js('gd'), Js('gh'), Js('gk'), Js('gl'), Js('gm'), Js('gn'), Js('gr'), Js('gs'), Js('gt'), Js('gz'), Js('hd'), Js('hb'), Js('hk'), Js('hn'), Js('hz'), Js('kl'), Js('kn'), Js('kz'), Js('kv'), Js('kk'), Js('lb'), Js('ld'), Js('lg'), Js('lk'), Js('ll'), Js('lr'), Js('ls'), Js('lt'), Js('lv'), Js('lz'), Js('mr'), Js('mv'), Js('mz'), Js('mt'), Js('nr'), Js('nv'), Js('nz'), Js('nt'), Js('ph'), Js('pf'), Js('pl'), Js('pn'), Js('pm'), Js('pr'), Js('ps'), Js('pt'), Js('pv'), Js('rb'), Js('rd'), Js('rg'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('rs'), Js('rt'), Js('rv'), Js('rz'), Js('sb'), Js('sd'), Js('sh'), Js('sk'), Js('sm'), Js('sn'), Js('sr'), Js('str'), Js('st'), Js('sv'), Js('sz'), Js('ss'), Js('tb'), Js('tl'), Js('tm'), Js('tn'), Js('tr'), Js('tv'), Js('tz'), Js('tt'), Js('vl'), Js('vn'), Js('vr'), Js('vz')]))
var.put('nm7', Js([Js('h'), Js('f'), Js('g'), Js('l'), Js('n'), Js('q'), Js('s'), Js('x'), Js('z'), Js('ls'), Js('nk'), Js('zz'), Js('ld'), Js('sh'), Js('sz'), Js('ss'), Js('gs'), Js('sx'), Js('lx'), Js('hx'), Js('th'), Js('rx'), Js('rt'), Js('ft'), Js('fs'), Js('fz'), Js('lm'), Js('lk'), Js('lt'), Js('ng'), Js('nx'), Js('ns'), Js('nq')]))
var.put('nm8', Js([Js('e'), Js('i'), Js('ee'), Js('ia'), Js('ea'), Js('a'), Js('ai'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
goblinNormal = var.to_python()
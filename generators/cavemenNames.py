__all__ = ['cavemenNames']

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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('names', ((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(5.0)):
                        while (var.get('rnd')<Js(3.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        while (var.get('rnd5')<Js(2.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('br'), Js('bh'), Js('cr'), Js('d'), Js('dr'), Js('dh'), Js('fr'), Js('g'), Js('gr'), Js('gn'), Js('gh'), Js('j'), Js('kr'), Js('kh'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('o'), Js('o'), Js('o'), Js('ou'), Js('oo'), Js('aa'), Js('oe'), Js('ua'), Js('uu'), Js('ia')]))
var.put('nm3', Js([Js('cr'), Js('cc'), Js('ch'), Js('d'), Js('dd'), Js('dr'), Js('dh'), Js('dv'), Js('g'), Js('gg'), Js('gr'), Js('gn'), Js('gv'), Js('gz'), Js('k'), Js('kn'), Js('kz'), Js('kv'), Js('kk'), Js('l'), Js('ll'), Js('lr'), Js('lk'), Js('mg'), Js('mk'), Js('n'), Js('ng'), Js('nk'), Js('nd'), Js('nr'), Js('rg'), Js('rd'), Js('rb'), Js('rl'), Js('rr'), Js('rz'), Js('rv'), Js('rk'), Js('sk'), Js('sg'), Js('sv'), Js('t'), Js('tk'), Js('tz'), Js('tt'), Js('v'), Js('vv'), Js('vr'), Js('vk'), Js('vd'), Js('z'), Js('zz'), Js('zk'), Js('zd'), Js('zc'), Js('zg')]))
var.put('nm4', Js([Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('kk'), Js('lk'), Js('ll'), Js('n'), Js('r'), Js('rc'), Js('rk'), Js('rv'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('c'), Js('ch'), Js('d'), Js('dh'), Js('f'), Js('fl'), Js('gh'), Js('gn'), Js('h'), Js('j'), Js('jh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sc'), Js('sk'), Js('sn'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('ts'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('o'), Js('aa'), Js('ae'), Js('ai'), Js('ee'), Js('oe'), Js('ua')]))
var.put('nm7', Js([Js('b'), Js('b'), Js('d'), Js('d'), Js('g'), Js('g'), Js('k'), Js('k'), Js('l'), Js('l'), Js('n'), Js('n'), Js('r'), Js('r'), Js('s'), Js('s'), Js('t'), Js('t'), Js('z'), Js('z'), Js('b'), Js('b'), Js('d'), Js('d'), Js('g'), Js('g'), Js('k'), Js('k'), Js('l'), Js('l'), Js('n'), Js('n'), Js('r'), Js('r'), Js('s'), Js('s'), Js('t'), Js('t'), Js('z'), Js('z'), Js('b'), Js('br'), Js('bh'), Js('bn'), Js('bb'), Js('ch'), Js('cn'), Js('cl'), Js('cr'), Js('d'), Js('dd'), Js('dn'), Js('dl'), Js('fr'), Js('fn'), Js('fl'), Js('g'), Js('gg'), Js('gl'), Js('gn'), Js('gr'), Js('gy'), Js('k'), Js('kk'), Js('ky'), Js('kl'), Js('kn'), Js('km'), Js('l'), Js('ll'), Js('lg'), Js('ly'), Js('ln'), Js('lm'), Js('lv'), Js('mg'), Js('ml'), Js('n'), Js('nn'), Js('ng'), Js('nk'), Js('nd'), Js('nz'), Js('r'), Js('rr'), Js('rb'), Js('rl'), Js('rt'), Js('rth'), Js('s'), Js('sz'), Js('sr'), Js('st'), Js('sh'), Js('ss'), Js('t'), Js('ty'), Js('yl'), Js('yr'), Js('yn'), Js('yg'), Js('yr'), Js('vr'), Js('vn'), Js('vl'), Js('vk'), Js('z'), Js('zh'), Js('zn')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n'), Js('s')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js('br'), Js('bh'), Js('cr'), Js('d'), Js('dr'), Js('dh'), Js('fr'), Js('g'), Js('gr'), Js('gn'), Js('gh'), Js('j'), Js('kr'), Js('kh'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('c'), Js('ch'), Js('d'), Js('dh'), Js('f'), Js('fl'), Js('gh'), Js('gn'), Js('h'), Js('j'), Js('jh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sc'), Js('sk'), Js('sn'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('ts'), Js('v'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('o'), Js('o'), Js('o'), Js('ou'), Js('oo'), Js('aa'), Js('oe'), Js('ua'), Js('uu'), Js('ia'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('o'), Js('aa'), Js('ae'), Js('ai'), Js('ee'), Js('oe'), Js('ua')]))
var.put('nm11', Js([Js('b'), Js('b'), Js('d'), Js('d'), Js('g'), Js('g'), Js('k'), Js('k'), Js('l'), Js('l'), Js('n'), Js('n'), Js('r'), Js('r'), Js('s'), Js('s'), Js('t'), Js('t'), Js('z'), Js('z'), Js('b'), Js('br'), Js('bh'), Js('bn'), Js('bb'), Js('ch'), Js('cn'), Js('cl'), Js('cr'), Js('d'), Js('dd'), Js('dn'), Js('dl'), Js('fr'), Js('fn'), Js('fl'), Js('g'), Js('gg'), Js('gl'), Js('gn'), Js('gr'), Js('gy'), Js('k'), Js('kk'), Js('ky'), Js('kl'), Js('kn'), Js('km'), Js('l'), Js('ll'), Js('lg'), Js('ly'), Js('ln'), Js('lm'), Js('lv'), Js('mg'), Js('ml'), Js('n'), Js('nn'), Js('ng'), Js('nk'), Js('nd'), Js('nz'), Js('r'), Js('rr'), Js('rb'), Js('rl'), Js('rt'), Js('rth'), Js('s'), Js('sz'), Js('sr'), Js('st'), Js('sh'), Js('ss'), Js('t'), Js('ty'), Js('yl'), Js('yr'), Js('yn'), Js('yg'), Js('yr'), Js('vr'), Js('vn'), Js('vl'), Js('vk'), Js('z'), Js('zh'), Js('zn'), Js('cr'), Js('cc'), Js('ch'), Js('d'), Js('dd'), Js('dr'), Js('dh'), Js('dv'), Js('g'), Js('gg'), Js('gr'), Js('gn'), Js('gv'), Js('gz'), Js('k'), Js('kn'), Js('kz'), Js('kv'), Js('kk'), Js('l'), Js('ll'), Js('lr'), Js('lk'), Js('mg'), Js('mk'), Js('n'), Js('ng'), Js('nk'), Js('nd'), Js('nr'), Js('rg'), Js('rd'), Js('rb'), Js('rl'), Js('rr'), Js('rz'), Js('rv'), Js('rk'), Js('sk'), Js('sg'), Js('sv'), Js('t'), Js('tk'), Js('tz'), Js('tt'), Js('v'), Js('vv'), Js('vr'), Js('vk'), Js('vd'), Js('z'), Js('zz'), Js('zk'), Js('zd'), Js('zc'), Js('zg')]))
var.put('nm12', Js([Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('kk'), Js('lk'), Js('ll'), Js('n'), Js('r'), Js('t'), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n'), Js('s')]))
pass
pass


# Add lib to the module scope
cavemenNames = var.to_python()
__all__ = ['pathfinderOrc']

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
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                while (var.get('rnd8')<Js(5.0)):
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('nameLast', ((var.get('nm9').get(var.get('rnd8'))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd12'))))
            else:
                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('nameLast', ((((var.get('nm9').get(var.get('rnd8'))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm10').get(var.get('rnd11')))+var.get('nm12').get(var.get('rnd12'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(2.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    while (var.get('rnd5')<Js(10.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(3.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                else:
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('cr'), Js('dr'), Js('f'), Js('gr'), Js('h'), Js('kr'), Js('kz'), Js('m'), Js('n'), Js('pr'), Js('r'), Js('t'), Js('tr'), Js('v'), Js('vr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bd'), Js('bz'), Js('d'), Js('dd'), Js('dr'), Js('dz'), Js('g'), Js('gh'), Js('gr'), Js('gn'), Js('gz'), Js('k'), Js('kk'), Js('kd'), Js('kz'), Js('kn'), Js('l'), Js('ld'), Js('lkz'), Js('ll'), Js('lz'), Js('lr'), Js('lg'), Js('lk'), Js('m'), Js('mg'), Js('mz'), Js('mr'), Js('n'), Js('ng'), Js('nr'), Js('nk'), Js('r'), Js('rd'), Js('rk'), Js('rn'), Js('rr'), Js('rg'), Js('rz'), Js('rv'), Js('s'), Js('sr'), Js('sk'), Js('sg'), Js('sc'), Js('v'), Js('vr'), Js('vk'), Js('vz'), Js('z'), Js('zr'), Js('zk'), Js('zn'), Js('zm'), Js('zc')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('ch'), Js('g'), Js('hn'), Js('hk'), Js('hm'), Js('hd'), Js('k'), Js('kk'), Js('lk'), Js('lkk'), Js('lt'), Js('ld'), Js('m'), Js('n'), Js('r'), Js('rd'), Js('rk'), Js('rg'), Js('rn'), Js('sh'), Js('sk'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('g'), Js('gr'), Js('f'), Js('g'), Js('gr'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('tr'), Js('v'), Js('vr')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ya'), Js('oa'), Js('ia'), Js('ua')]))
var.put('nm7', Js([Js('b'), Js('bb'), Js('bg'), Js('d'), Js('dd'), Js('dg'), Js('dj'), Js('dr'), Js('ff'), Js('gg'), Js('gj'), Js('gd'), Js('gr'), Js('gn'), Js('gm'), Js('hj'), Js('hm'), Js('hn'), Js('hr'), Js('k'), Js('kd'), Js('kb'), Js('kr'), Js('kk'), Js('l'), Js('lb'), Js('lg'), Js('llg'), Js('ld'), Js('lld'), Js('lk'), Js('lr'), Js('llr'), Js('m'), Js('mr'), Js('mj'), Js('mg'), Js('mk'), Js('ng'), Js('nj'), Js('n'), Js('nn'), Js('nr'), Js('r'), Js('rg'), Js('rj'), Js('rr'), Js('rv'), Js('sgr'), Js('sg'), Js('sh'), Js('sk'), Js('z'), Js('zn')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('ng'), Js('s'), Js('ss'), Js('t')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('ch'), Js('cr'), Js('d'), Js('dh'), Js('f'), Js('g'), Js('gh'), Js('gr'), Js('k'), Js('kr'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('t'), Js('th'), Js('v'), Js('vh'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('uu'), Js('aa'), Js('ua')]))
var.put('nm11', Js([Js('d'), Js('dd'), Js('dr'), Js('fr'), Js('fn'), Js('g'), Js('gg'), Js('gd'), Js('gn'), Js('gm'), Js('gz'), Js('hm'), Js('hj'), Js('hm'), Js('k'), Js('kk'), Js('kd'), Js('kn'), Js('ld'), Js('lb'), Js('lk'), Js('lz'), Js('lg'), Js('lk'), Js('ll'), Js('lr'), Js('m'), Js('mg'), Js('mk'), Js('n'), Js('nn'), Js('ng'), Js('nr'), Js('nk'), Js('r'), Js('rr'), Js('rg'), Js('rk'), Js('rn'), Js('rm'), Js('rv'), Js('sg'), Js('ss'), Js('s'), Js('sr'), Js('sk'), Js('sn'), Js('v'), Js('vr'), Js('vn'), Js('vk'), Js('z'), Js('zk'), Js('zn'), Js('zm')]))
var.put('nm12', Js([Js('d'), Js('hn'), Js('hd'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th')]))
pass
pass


# Add lib to the module scope
pathfinderOrc = var.to_python()
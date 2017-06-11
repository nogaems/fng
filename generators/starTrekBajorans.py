__all__ = ['starTrekBajorans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm11').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm13').get(var.get('rnd8')))+var.get('nm14').get(var.get('rnd9'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                    def PyJs_LONG_0_(var=var):
                        return (((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm11').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm13').get(var.get('rnd8')))+var.get('nm14').get(var.get('rnd9')))+var.get('nm15').get(var.get('rnd10')))+var.get('nm16').get(var.get('rnd11')))
                    var.put('names', PyJs_LONG_0_())
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+var.get('nm10').get(var.get('rnd9'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    def PyJs_LONG_1_(var=var):
                        return (((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+var.get('nm4').get(var.get('rnd9')))+var.get('nm9').get(var.get('rnd10')))+var.get('nm10').get(var.get('rnd11')))
                    var.put('names', PyJs_LONG_1_())
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('ch'), Js('sh'), Js('br'), Js('pr'), Js('tr'), Js('dr'), Js('kr'), Js('vr'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('ee')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('nj'), Js('mj'), Js('nt'), Js('mt'), Js('ct'), Js('kt'), Js('ny'), Js('cy'), Js('gy'), Js('ky'), Js('my'), Js('py'), Js('sy'), Js('ty'), Js('ry'), Js('rm'), Js('rb'), Js('rc'), Js('rd'), Js('rj'), Js('rk'), Js('rm'), Js('rn'), Js('rp'), Js('rs'), Js('rt'), Js('rv'), Js('rw'), Js('rz'), Js('sh'), Js('ch'), Js('th'), Js('ll'), Js('dd'), Js('gg'), Js('kk'), Js('rr'), Js('zk'), Js('sk'), Js('lk'), Js('tk'), Js('tr'), Js('dr')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm5', Js([Js('n'), Js('ld'), Js('k'), Js('s'), Js('r'), Js('sh'), Js('t'), Js('m'), Js('lb'), Js('hl'), Js('l'), Js('d'), Js('ld'), Js('g'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('b'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('kr'), Js('tr'), Js('rh'), Js('sh'), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('aie'), Js('ue'), Js('oa'), Js('aa'), Js('ee')]))
var.put('nm8', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('ln'), Js('lb'), Js('lz'), Js('lg'), Js('lk'), Js('ltr'), Js('zk'), Js('zd'), Js('rk'), Js('rd'), Js('rg'), Js('rn'), Js('rt'), Js('yr'), Js('yd'), Js('mm'), Js('rr'), Js('ss'), Js('nn'), Js('tt'), Js('br'), Js('kr'), Js('gd'), Js('nd'), Js('nt')]))
var.put('nm9', Js([Js('m'), Js('s'), Js('r'), Js('n'), Js('g'), Js('l'), Js('th'), Js('rn'), Js('c')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm11', Js([Js('b'), Js('bl'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('w'), Js('x'), Js('y'), Js('z'), Js('gr'), Js('gl'), Js('sh'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('o'), Js('u'), Js('ee'), Js('ai'), Js('oa')]))
var.put('nm13', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('w'), Js('x'), Js('y'), Js('z'), Js('sh'), Js('pr'), Js('rd'), Js('lr'), Js('gh'), Js('rj'), Js('lk')]))
var.put('nm14', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ia'), Js('ea')]))
var.put('nm15', Js([Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('w'), Js('y'), Js('z')]))
var.put('nm16', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ia'), Js('ea'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
starTrekBajorans = var.to_python()
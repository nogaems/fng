__all__ = ['warhammerGoblins']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                if (var.get('i')<Js(4.0)):
                    var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd5')<Js(4.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('ch'), Js('cr'), Js('g'), Js('gh'), Js('gr'), Js('gn'), Js('k'), Js('kr'), Js('kn'), Js('r'), Js('sk'), Js('sc'), Js('sm'), Js('sn'), Js('st'), Js('str'), Js('skr'), Js('t'), Js('tr'), Js('z'), Js('zr')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('e'), Js('u')]))
var.put('nm3', Js([Js('c'), Js('cc'), Js('cl'), Js('cr'), Js('cn'), Js('gl'), Js('gr'), Js('gn'), Js('gg'), Js('g'), Js('gd'), Js('gdr'), Js('gs'), Js('gt'), Js('gtr'), Js('k'), Js('kk'), Js('kt'), Js('kr'), Js('ktr'), Js('ks'), Js('kz'), Js('kv'), Js('ng'), Js('nz'), Js('nr'), Js('nk'), Js('nkz'), Js('nks'), Js('rc'), Js('rk'), Js('rg'), Js('rgr'), Js('rkr'), Js('rs'), Js('rsn'), Js('rsm'), Js('rz'), Js('rt'), Js('rtr'), Js('rsl'), Js('sn'), Js('str'), Js('sk'), Js('sc'), Js('str'), Js('skr'), Js('sz'), Js('tr'), Js('tkr'), Js('tn'), Js('tv'), Js('vr'), Js('vl')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('k'), Js('n'), Js('m'), Js('mm'), Js('r'), Js('rr'), Js('rk'), Js('s'), Js('sk'), Js('sz'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('ch'), Js('d'), Js('g'), Js('gh'), Js('k'), Js('kh'), Js('r'), Js('sr'), Js('sc'), Js('sk'), Js('sn'), Js('sl'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('x'), Js('z')]))
var.put('nm6', Js([Js('i'), Js('a'), Js('i'), Js('a'), Js('i'), Js('a'), Js('i'), Js('a'), Js('e'), Js('e'), Js('e'), Js('o'), Js('u')]))
var.put('nm7', Js([Js('c'), Js('ch'), Js('cc'), Js('g'), Js('gg'), Js('gr'), Js('gtr'), Js('gn'), Js('gz'), Js('k'), Js('kr'), Js('kz'), Js('kt'), Js('l'), Js('ll'), Js('lc'), Js('lk'), Js('lz'), Js('lg'), Js('n'), Js('nn'), Js('nr'), Js('nt'), Js('nk'), Js('r'), Js('rr'), Js('rl'), Js('rk'), Js('rn'), Js('rm'), Js('t'), Js('tt'), Js('th'), Js('tr'), Js('tz'), Js('tzr'), Js('tsr'), Js('tg'), Js('v'), Js('vr'), Js('z'), Js('zr'), Js('zz'), Js('zg'), Js('zk'), Js('zn')]))
pass
pass


# Add lib to the module scope
warhammerGoblins = var.to_python()
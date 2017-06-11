__all__ = ['dragonkinNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                while (PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm10').get(var.get('rnd5')))):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    while (PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm9').get(var.get('rnd6'))) or PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm10').get(var.get('rnd5')))):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    if (var.get('i')<Js(8.0)):
                        var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd5'))))
                    else:
                        var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    while (PyJsStrictEq(var.get('nm13').get(var.get('rnd3')),var.get('nm11').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm13').get(var.get('rnd3')),var.get('nm15').get(var.get('rnd5')))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    if (var.get('i')<Js(6.0)):
                        var.put('names', ((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        while (PyJsStrictEq(var.get('nm13').get(var.get('rnd3')),var.get('nm14').get(var.get('rnd6'))) or PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm15').get(var.get('rnd5')))):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm15').get(var.get('rnd5'))))
                        else:
                            var.put('names', ((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5')))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    if (var.get('i')<Js(6.0)):
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd6'))) or PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm5').get(var.get('rnd5')))):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                        else:
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('dr'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sr'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('ae'), Js('ia'), Js('iu'), Js('io'), Js('eo')]))
var.put('nm3', Js([Js('cr'), Js('cg'), Js('cn'), Js('csh'), Js('cd'), Js('cdr'), Js('dr'), Js('dg'), Js('dgr'), Js('dk'), Js('dkr'), Js('k'), Js('kr'), Js('kt'), Js('kth'), Js('ksh'), Js('l'), Js('lk'), Js('lt'), Js('ldr'), Js('lg'), Js('lgr'), Js('lsh'), Js('lz'), Js('n'), Js('nd'), Js('ndr'), Js('nsh'), Js('nsk'), Js('r'), Js('rc'), Js('rph'), Js('rsh'), Js('rth'), Js('rd'), Js('rdr'), Js('rgr'), Js('rg'), Js('rz'), Js('rzr'), Js('rsh'), Js('s'), Js('sth'), Js('shk'), Js('sk'), Js('sg'), Js('skr'), Js('th'), Js('tr'), Js('tr'), Js('tg'), Js('z'), Js('zz'), Js('zg'), Js('zk')]))
var.put('nm4', Js([Js('b'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('gg'), Js('k'), Js('ks'), Js('n'), Js('nd'), Js('ph'), Js('s'), Js('th'), Js('x'), Js('z')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('c'), Js('ch'), Js('d'), Js('g'), Js('h'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('phr'), Js('r'), Js('s'), Js('shr'), Js('str'), Js('sth'), Js('t'), Js('th'), Js('tr'), Js('z'), Js('zh')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('ae'), Js('ia'), Js('ea'), Js('ie'), Js('ei')]))
var.put('nm8', Js([Js('dr'), Js('dh'), Js('dn'), Js('dhr'), Js('gn'), Js('gr'), Js('ghr'), Js('gtr'), Js('gt'), Js('k'), Js('kk'), Js('kh'), Js('kt'), Js('kth'), Js('l'), Js('lk'), Js('ll'), Js('lg'), Js('ld'), Js('ldr'), Js('lgr'), Js('ln'), Js('lm'), Js('lkh'), Js('ls'), Js('lz'), Js('n'), Js('nd'), Js('ndh'), Js('ndr'), Js('ns'), Js('nsh'), Js('nz'), Js('nh'), Js('nhr'), Js('ng'), Js('ngh'), Js('r'), Js('rc'), Js('rph'), Js('rsh'), Js('rz'), Js('rl'), Js('s'), Js('sh'), Js('ss'), Js('sth'), Js('sht'), Js('shl'), Js('sn'), Js('sg'), Js('sk'), Js('th'), Js('thr'), Js('thn'), Js('tr'), Js('z'), Js('zh')]))
var.put('nm9', Js([Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('x'), Js('z')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('s'), Js('sh'), Js('th'), Js('x'), Js('z')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('d'), Js('g'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sr'), Js('str'), Js('sth'), Js('t'), Js('tr'), Js('th'), Js('z')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('ae'), Js('ia'), Js('ea'), Js('io'), Js('ie')]))
var.put('nm13', Js([Js('cr'), Js('cn'), Js('cd'), Js('dr'), Js('dh'), Js('dg'), Js('dhr'), Js('gn'), Js('gr'), Js('ghr'), Js('k'), Js('kk'), Js('kt'), Js('kth'), Js('l'), Js('lk'), Js('ll'), Js('lg'), Js('ld'), Js('ldr'), Js('lgr'), Js('lz'), Js('n'), Js('nd'), Js('ndr'), Js('ns'), Js('nsh'), Js('nz'), Js('ng'), Js('r'), Js('rc'), Js('rph'), Js('rsh'), Js('rz'), Js('rd'), Js('rdr'), Js('rgr'), Js('rg'), Js('s'), Js('sh'), Js('ss'), Js('sth'), Js('sht'), Js('sth'), Js('sn'), Js('sg'), Js('sk'), Js('th'), Js('thr'), Js('tr'), Js('z'), Js('zg'), Js('zh')]))
var.put('nm14', Js([Js('b'), Js('d'), Js('g'), Js('l'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('z')]))
var.put('nm15', Js([Js(''), Js(''), Js(''), Js('h'), Js('n'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
dragonkinNames = var.to_python()
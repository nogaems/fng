__all__ = ['orcTowns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(2.0)):
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd')<Js(5.0)):
                    while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('nm1').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd8'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        if (var.get('rnd')<Js(5.0)):
                            while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd8')))+Js('  '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('bh'), Js('ch'), Js('d'), Js('dr'), Js('dh'), Js('g'), Js('gr'), Js('gh'), Js('k'), Js('kr'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('v'), Js('z'), Js('vr'), Js('zr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('cc'), Js('d'), Js('dd'), Js('gg'), Js('g'), Js('r'), Js('rr'), Js('z'), Js('zz'), Js('b'), Js('cc'), Js('d'), Js('dd'), Js('gg'), Js('g'), Js('r'), Js('rr'), Js('z'), Js('zz'), Js('br'), Js('cr'), Js('dr'), Js('dg'), Js('dz'), Js('dgr'), Js('dk'), Js('gr'), Js('gh'), Js('gk'), Js('gz'), Js('gm'), Js('gn'), Js('gv'), Js('lb'), Js('lg'), Js('lgr'), Js('ldr'), Js('lbr'), Js('lk'), Js('lz'), Js('mm'), Js('rg'), Js('rm'), Js('rdr'), Js('rbr'), Js('rd'), Js('rk'), Js('rkr'), Js('rgr'), Js('rz'), Js('shb'), Js('shn'), Js('zg'), Js('zgr'), Js('zd'), Js('zr'), Js('zdr')]))
var.put('nm4', Js([Js(''), Js('kh'), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('l'), Js('n'), Js('r'), Js('rd'), Js('z')]))
pass
pass


# Add lib to the module scope
orcTowns = var.to_python()
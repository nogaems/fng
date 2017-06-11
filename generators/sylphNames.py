__all__ = ['sylphNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        while (var.get('rnd5')<Js(4.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm2').get(var.get('rnd2'))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6'))))
                        while (var.get('names').get('length')>Js(10.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                        while (var.get('names').get('length')>Js(10.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                        while (var.get('names').get('length')>Js(10.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('ch'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('th'), Js('v'), Js('w'), Js('y')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('ea'), Js('ei'), Js('ia'), Js('ie'), Js('ue'), Js('ua'), Js('aei'), Js('aea'), Js('eae')]))
var.put('nm3', Js([Js('bh'), Js('c'), Js('ch'), Js('h'), Js('y'), Js('hl'), Js('hm'), Js('hy'), Js('l'), Js('lm'), Js('ln'), Js('ls'), Js('lt'), Js('lth'), Js('lv'), Js('ll'), Js('m'), Js('mm'), Js('mn'), Js('mh'), Js('ms'), Js('mth'), Js('n'), Js('nh'), Js('nn'), Js('nl'), Js('nt'), Js('ns'), Js('nth'), Js('nv'), Js('nf'), Js('nm'), Js('nh'), Js('nhr'), Js('ph'), Js('phr'), Js('r'), Js('rd'), Js('rph'), Js('rs'), Js('rth'), Js('rh'), Js('rn'), Js('rm'), Js('rv'), Js('ss'), Js('sn'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('thr'), Js('v'), Js('w')]))
var.put('nm4', Js([Js('f'), Js('l'), Js('m'), Js('n'), Js('s'), Js('th'), Js('f'), Js('ff'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('th'), Js('y')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('dh'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('th'), Js('w'), Js('y')]))
var.put('nm6', Js([Js('c'), Js('h'), Js('y'), Js('hl'), Js('hn'), Js('hm'), Js('hsh'), Js('hph'), Js('hy'), Js('hth'), Js('ht'), Js('l'), Js('ll'), Js('lsh'), Js('lf'), Js('ln'), Js('lph'), Js('ls'), Js('lth'), Js('m'), Js('mn'), Js('mh'), Js('ms'), Js('n'), Js('nh'), Js('nl'), Js('nsh'), Js('nt'), Js('ns'), Js('nth'), Js('nph'), Js('nf'), Js('nm'), Js('nh'), Js('nhr'), Js('ph'), Js('phn'), Js('phl'), Js('r'), Js('rd'), Js('rph'), Js('rsh'), Js('rs'), Js('rth'), Js('rh'), Js('rn'), Js('rm'), Js('ss'), Js('sn'), Js('shn'), Js('sh'), Js('st'), Js('sht'), Js('t'), Js('th'), Js('thr'), Js('v'), Js('w')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js('f'), Js('ff'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('y'), Js('f'), Js('ff'), Js('h'), Js('ph'), Js('s'), Js('sh'), Js('y')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('dh'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('th'), Js('v'), Js('w'), Js('y')]))
var.put('nm9', Js([Js('ch'), Js('h'), Js('hl'), Js('hn'), Js('hm'), Js('hsh'), Js('hph'), Js('ht'), Js('hth'), Js('l'), Js('lsh'), Js('lf'), Js('lm'), Js('ln'), Js('lph'), Js('ls'), Js('lt'), Js('lth'), Js('lv'), Js('m'), Js('mm'), Js('mn'), Js('mh'), Js('ms'), Js('msh'), Js('mth'), Js('mf'), Js('n'), Js('nh'), Js('nl'), Js('nsh'), Js('nt'), Js('ns'), Js('nth'), Js('nph'), Js('nv'), Js('nf'), Js('nm'), Js('nh'), Js('nhr'), Js('ph'), Js('phr'), Js('phn'), Js('phl'), Js('r'), Js('rd'), Js('rph'), Js('rsh'), Js('rs'), Js('rth'), Js('rh'), Js('rn'), Js('rm'), Js('ss'), Js('sn'), Js('shn'), Js('sh'), Js('st'), Js('sht'), Js('t'), Js('th'), Js('thr'), Js('v'), Js('w'), Js('y')]))
var.put('nm10', Js([Js('f'), Js('ff'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('th'), Js('y')]))
pass
pass


# Add lib to the module scope
sylphNames = var.to_python()
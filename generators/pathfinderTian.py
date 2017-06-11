__all__ = ['pathfinderTian']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm24', 'nm29', 'nm56', 'nm16', 'nm47', 'nm49', 'nm23', 'nm31', 'nm3', 'nm33', 'nm34', 'nm41', 'nm44', 'nm48', 'nm51', 'nm2', 'nm27', 'nm26', 'nm54', 'nm30', 'nm36', 'nm39', 'nm22', 'nm14', 'nm7', 'nm10', 'nm21', 'nm25', 'nm40', 'nm42', 'nm45', 'nm15', 'nm20', 'nm43', 'nm55', 'nm12', 'nm32', 'nm5', 'nm6', 'nm35', 'nm46', 'nm4', 'nameGen', 'nm8', 'nm28', 'nm18', 'nm37', 'nm17', 'nm13', 'nm9', 'nm38', 'nm50', 'nm57', 'nm52', 'nm53'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(14.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    if (var.get('rnd')<Js(3.0)):
                        while (var.get('rnd3')<Js(3.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('names', ((((((var.get('nm7').get(var.get('rnd4'))+var.get('nm8').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+Js('  '))+var.get('nm4').get(var.get('rnd')))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                        var.put('names', ((((((((var.get('nm17').get(var.get('rnd6'))+var.get('nm18').get(var.get('rnd7')))+var.get('nm19').get(var.get('rnd8')))+Js('  '))+var.get('nm14').get(var.get('rnd')))+var.get('nm11').get(var.get('rnd2')))+var.get('nm15').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm16').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('names', (((((var.get('nm26').get(var.get('rnd4'))+Js('  '))+var.get('nm23').get(var.get('rnd')))+var.get('nm24').get(var.get('rnd2')))+Js('  '))+var.get('nm25').get(var.get('rnd3'))))
                        else:
                            if (var.get('i')<Js(8.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm32').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm33').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm32').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm34').get('length'))))
                                if (var.get('rnd')<Js(3.0)):
                                    while (var.get('rnd5')<Js(3.0)):
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm34').get('length'))))
                                var.put('names', ((((var.get('nm31').get(var.get('rnd'))+var.get('nm32').get(var.get('rnd2')))+var.get('nm33').get(var.get('rnd3')))+var.get('nm32').get(var.get('rnd4')))+var.get('nm34').get(var.get('rnd5'))))
                            else:
                                if (var.get('i')<Js(10.0)):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm37').get('length'))))
                                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm38').get('length'))))
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm39').get('length'))))
                                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm40').get('length'))))
                                    var.put('names', ((((var.get('nm39').get(var.get('rnd3'))+var.get('nm40').get(var.get('rnd4')))+Js('  '))+var.get('nm37').get(var.get('rnd')))+var.get('nm38').get(var.get('rnd2'))))
                                else:
                                    if (var.get('i')<Js(12.0)):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm45').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm46').get('length'))))
                                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm47').get('length'))))
                                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm46').get('length'))))
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm44').get('length'))))
                                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm48').get('length'))))
                                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm49').get('length'))))
                                        var.put('names', (((((((var.get('nm48').get(var.get('rnd6'))+var.get('nm49').get(var.get('rnd7')))+Js('  '))+var.get('nm45').get(var.get('rnd')))+var.get('nm46').get(var.get('rnd2')))+var.get('nm47').get(var.get('rnd3')))+var.get('nm46').get(var.get('rnd4')))+var.get('nm44').get(var.get('rnd5'))))
                                    else:
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm54').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm55').get('length'))))
                                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm56').get('length'))))
                                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm55').get('length'))))
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm57').get('length'))))
                                        var.put('names', ((((var.get('nm54').get(var.get('rnd'))+var.get('nm55').get(var.get('rnd2')))+var.get('nm56').get(var.get('rnd3')))+var.get('nm55').get(var.get('rnd4')))+var.get('nm57').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    if (var.get('rnd')<Js(3.0)):
                        while PyJsStrictEq(var.get('rnd3'),Js(0.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('names', ((((((var.get('nm7').get(var.get('rnd4'))+var.get('nm8').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+Js('  '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                        var.put('names', ((((((((var.get('nm17').get(var.get('rnd6'))+var.get('nm18').get(var.get('rnd7')))+var.get('nm19').get(var.get('rnd8')))+Js('  '))+var.get('nm10').get(var.get('rnd')))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('names', (((((var.get('nm26').get(var.get('rnd4'))+Js('  '))+var.get('nm20').get(var.get('rnd')))+var.get('nm21').get(var.get('rnd2')))+Js('  '))+var.get('nm22').get(var.get('rnd3'))))
                        else:
                            if (var.get('i')<Js(8.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm29').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm30').get('length'))))
                                if (var.get('rnd')<Js(3.0)):
                                    while (var.get('rnd5')<Js(3.0)):
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm30').get('length'))))
                                var.put('names', ((((var.get('nm27').get(var.get('rnd'))+var.get('nm28').get(var.get('rnd2')))+var.get('nm29').get(var.get('rnd3')))+var.get('nm28').get(var.get('rnd4')))+var.get('nm30').get(var.get('rnd5'))))
                            else:
                                if (var.get('i')<Js(10.0)):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm35').get('length'))))
                                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm36').get('length'))))
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm39').get('length'))))
                                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm40').get('length'))))
                                    var.put('names', ((((var.get('nm39').get(var.get('rnd3'))+var.get('nm40').get(var.get('rnd4')))+Js('  '))+var.get('nm35').get(var.get('rnd')))+var.get('nm36').get(var.get('rnd2'))))
                                else:
                                    if (var.get('i')<Js(12.0)):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm41').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm42').get('length'))))
                                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm43').get('length'))))
                                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm42').get('length'))))
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm44').get('length'))))
                                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm48').get('length'))))
                                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm49').get('length'))))
                                        var.put('names', (((((((var.get('nm48').get(var.get('rnd6'))+var.get('nm49').get(var.get('rnd7')))+Js('  '))+var.get('nm41').get(var.get('rnd')))+var.get('nm42').get(var.get('rnd2')))+var.get('nm43').get(var.get('rnd3')))+var.get('nm42').get(var.get('rnd4')))+var.get('nm44').get(var.get('rnd5'))))
                                    else:
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm50').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm51').get('length'))))
                                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm52').get('length'))))
                                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm51').get('length'))))
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm53').get('length'))))
                                        var.put('names', ((((var.get('nm50').get(var.get('rnd'))+var.get('nm51').get(var.get('rnd2')))+var.get('nm52').get(var.get('rnd3')))+var.get('nm51').get(var.get('rnd4')))+var.get('nm53').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('g'), Js('h'), Js('kh'), Js('l'), Js('m'), Js('ng'), Js('nh'), Js('ph'), Js('q'), Js('s'), Js('th'), Js('t'), Js('tr'), Js('v'), Js('x')]))
var.put('nm2', Js([Js('a'), Js('ai'), Js('ao'), Js('i'), Js('ia'), Js('ie'), Js('ieu'), Js('o'), Js('oa'), Js('oai'), Js('u'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('uu')]))
var.put('nm3', Js([Js(''), Js('c'), Js('n'), Js('ng'), Js('nh'), Js('t'), Js('y')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('g'), Js('h'), Js('hy'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('nh'), Js('ph'), Js('q'), Js('s'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('x'), Js('y')]))
var.put('nm5', Js([Js('a'), Js('ai'), Js('ao'), Js('au'), Js('e'), Js('h'), Js('i'), Js('ia'), Js('ie'), Js('ieu'), Js('iu'), Js('o'), Js('oa'), Js('u'), Js('ua'), Js('ue'), Js('uo')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('m'), Js('n'), Js('ng'), Js('nh'), Js('p'), Js('t'), Js('y')]))
var.put('nm7', Js([Js('b'), Js('c'), Js('ch'), Js('d'), Js('g'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('ng'), Js('nh'), Js('nz'), Js('ph'), Js('q'), Js('s'), Js('t'), Js('th'), Js('tr'), Js('v')]))
var.put('nm8', Js([Js('a'), Js('ai'), Js('ao'), Js('au'), Js('i'), Js('ia'), Js('ie'), Js('ieu'), Js('o'), Js('oa'), Js('oi'), Js('oo'), Js('ou'), Js('u'), Js('ua'), Js('ue'), Js('ui'), Js('uo'), Js('uu'), Js('uy'), Js('uye')]))
var.put('nm9', Js([Js(''), Js(''), Js('c'), Js('ch'), Js('m'), Js('n'), Js('ng'), Js('nh'), Js('p'), Js('y')]))
var.put('nm10', Js([Js('b'), Js('ch'), Js('chh'), Js('d'), Js('h'), Js('kh'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('sr'), Js('th'), Js('v')]))
var.put('nm11', Js([Js('oeu'), Js('ou'), Js('ea'), Js('ei'), Js('ia'), Js('ao'), Js('au'), Js('ai'), Js('uo'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm12', Js([Js('b'), Js('ch'), Js('d'), Js('h'), Js('k'), Js('kb'), Js('kd'), Js('kh'), Js('kng'), Js('kr'), Js('ks'), Js('ksm'), Js('ktr'), Js('l'), Js('m'), Js('mb'), Js('ml'), Js('mn'), Js('mph'), Js('mr'), Js('n'), Js('nch'), Js('ngh'), Js('ngs'), Js('nkr'), Js('nl'), Js('nm'), Js('nn'), Js('nr'), Js('ns'), Js('nth'), Js('ntr'), Js('nv'), Js('ny'), Js('p'), Js('ph'), Js('r'), Js('rk'), Js('ry'), Js('s'), Js('sm'), Js('sn'), Js('t'), Js('td'), Js('th'), Js('tt'), Js('v'), Js('y')]))
var.put('nm13', Js([Js('k'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('nn'), Js('p'), Js('r'), Js('s'), Js('th'), Js('y')]))
var.put('nm14', Js([Js('b'), Js('ch'), Js('d'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('p'), Js('r'), Js('s'), Js('sr'), Js('t'), Js('th'), Js('v')]))
var.put('nm15', Js([Js('b'), Js('ch'), Js('d'), Js('k'), Js('kd'), Js('kh'), Js('kkl'), Js('kr'), Js('kry'), Js('ksm'), Js('l'), Js('ll'), Js('lth'), Js('m'), Js('mb'), Js('md'), Js('mj'), Js('mp'), Js('mph'), Js('mr'), Js('n'), Js('nch'), Js('nd'), Js('ngs'), Js('nkr'), Js('nl'), Js('nm'), Js('nn'), Js('nnl'), Js('nt'), Js('nth'), Js('ntr'), Js('nv'), Js('ny'), Js('p'), Js('ph'), Js('r'), Js('rk'), Js('rph'), Js('rsd'), Js('rt'), Js('rv'), Js('ry'), Js('s'), Js('sm'), Js('sn'), Js('sn'), Js('t'), Js('td'), Js('th'), Js('tr'), Js('tt'), Js('v'), Js('vy'), Js('w'), Js('y'), Js('yh'), Js('ym'), Js('yn'), Js('yp')]))
var.put('nm16', Js([Js('ch'), Js('k'), Js('kry'), Js('l'), Js('lly'), Js('ly'), Js('m'), Js('mphy'), Js('n'), Js('ng'), Js('nn'), Js('nny'), Js('ny'), Js('ry'), Js('s'), Js('ss'), Js('th'), Js('vy'), Js('y')]))
var.put('nm17', Js([Js('b'), Js('ch'), Js('chh'), Js('d'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('khl'), Js('l'), Js('m'), Js('nh'), Js('n'), Js('p'), Js('ph'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('y')]))
var.put('nm18', Js([Js('a'), Js('aa'), Js('ae'), Js('ao'), Js('e'), Js('ea'), Js('eo'), Js('i'), Js('ia'), Js('ie'), Js('o'), Js('oe'), Js('ou'), Js('u'), Js('uo')]))
var.put('nm19', Js([Js('ch'), Js('k'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('r'), Js('rn'), Js('s'), Js('t'), Js('th'), Js('v'), Js('y')]))
var.put('nm20', Js([Js('b'), Js('by'), Js('ch'), Js('d'), Js('g'), Js('h'), Js('hy'), Js('j'), Js('k'), Js('kw'), Js('ky'), Js('m'), Js('my'), Js('n'), Js('p'), Js('py'), Js('s'), Js('sh'), Js('t'), Js('w'), Js('y')]))
var.put('nm21', Js([Js('a'), Js('ae'), Js('am'), Js('an'), Js('ang'), Js('e'), Js('ee'), Js('ejun'), Js('eo'), Js('eon'), Js('eong'), Js('eung'), Js('i'), Js('ihu'), Js('ihun'), Js('in'), Js('injae'), Js('injun'), Js('o'), Js('ochun'), Js('ohyon'), Js('on'), Js('ong'), Js('onghyon'), Js('ongmin'), Js('onjun'), Js('onu'), Js('oo'), Js('oon'), Js('oung'), Js('u'), Js('uck'), Js('uk'), Js('ul'), Js('un'), Js('ung'), Js('unghyon'), Js('unho'), Js('unso'), Js('unyong'), Js('uwon')]))
var.put('nm22', Js([Js('bok'), Js('bong'), Js('cheol'), Js('chol'), Js('chuk'), Js('chul'), Js('dae'), Js('eun'), Js('gi'), Js('gu'), Js('gun'), Js('gyu'), Js('hae'), Js('han'), Js('hee'), Js('heon'), Js('ho'), Js('hoo'), Js('hoon'), Js('hu'), Js('hui'), Js('hun'), Js('hwa'), Js('hwan'), Js('hyeon'), Js('hyok'), Js('hyon'), Js('hyuk'), Js('hyun'), Js('il'), Js('ja'), Js('jae'), Js('jin'), Js('jo'), Js('joon'), Js('jun'), Js('jung'), Js('ki'), Js('kyu'), Js('kyung'), Js('min'), Js('mo'), Js('mun'), Js('nam'), Js('sam'), Js('sang'), Js('seo'), Js('seok'), Js('seon'), Js('seong'), Js('shik'), Js('sik'), Js('song'), Js('soo'), Js('sook'), Js('su'), Js('sun'), Js('sung'), Js('tae'), Js('u'), Js('won'), Js('woo'), Js('wook'), Js('woong'), Js('yeol'), Js('yeon'), Js('yeong'), Js('yol'), Js('yong'), Js('yoon'), Js('young'), Js('yul')]))
var.put('nm23', Js([Js('b'), Js('ch'), Js('d'), Js('g'), Js('gr'), Js('h'), Js('hy'), Js('j'), Js('k'), Js('ky'), Js('l'), Js('m'), Js('my'), Js('n'), Js('r'), Js('ry'), Js('s'), Js('sh'), Js('t'), Js('w'), Js('y')]))
var.put('nm24', Js([Js('a'), Js('ae'), Js('am'), Js('an'), Js('ang'), Js('ara'), Js('e'), Js('ee'), Js('eh'), Js('eo'), Js('eon'), Js('eong'), Js('eul'), Js('eum'), Js('eun'), Js('eung'), Js('i'), Js('ihye'), Js('ihyon'), Js('im'), Js('imin'), Js('in'), Js('inji'), Js('inso'), Js('it'), Js('iyeon'), Js('iyong'), Js('iyun'), Js('o'), Js('ohyon'), Js('on'), Js('ong'), Js('oo'), Js('ook'), Js('oon'), Js('oung'), Js('oyon'), Js('oyun'), Js('u'), Js('ubin'), Js('uk'), Js('un'), Js('ung'), Js('unji'), Js('unso')]))
var.put('nm25', Js([Js('ae'), Js('ah'), Js('ahn'), Js('bi'), Js('bin'), Js('bon'), Js('byul'), Js('chae'), Js('dong'), Js('eum'), Js('eun'), Js('gyo'), Js('gyong'), Js('gyung'), Js('ha'), Js('hae'), Js('hee'), Js('ho'), Js('hui'), Js('hwa'), Js('hyang'), Js('hye'), Js('hyo'), Js('hyun'), Js('hyung'), Js('in'), Js('ja'), Js('jeong'), Js('ji'), Js('jin'), Js('jong'), Js('joo'), Js('joong'), Js('ju'), Js('jung'), Js('kyeong'), Js('kyung'), Js('min'), Js('na'), Js('neul'), Js('ok'), Js('ra'), Js('rae'), Js('rang'), Js('ri'), Js('rim'), Js('rin'), Js('ryung'), Js('seo'), Js('seon'), Js('shil'), Js('so'), Js('song'), Js('soo'), Js('sook'), Js('soon'), Js('su'), Js('suk'), Js('sun'), Js('u'), Js('un'), Js('won'), Js('woo'), Js('woon'), Js('yeon'), Js('yon'), Js('yong'), Js('yoon'), Js('young'), Js('yun'), Js('yung')]))
var.put('nm26', Js([Js('Ae'), Js('Ah'), Js('An'), Js("Ch'a"), Js("Ch'ae"), Js("Ch'ang"), Js("Ch'o"), Js("Ch'oe"), Js("Ch'on"), Js("Ch'u"), Js('Cha'), Js('Chang'), Js('Changgok'), Js('Che'), Js('Chegal'), Js('Chi'), Js('Chin'), Js('Cho'), Js('Chom'), Js('Chon'), Js('Chong'), Js('Chu'), Js('Chun'), Js('Chung'), Js('Chup'), Js('Chwa'), Js('Eoh'), Js('Ha'), Js('Hae'), Js('Hak'), Js('Ham'), Js('Han'), Js('Ho'), Js('Hong'), Js('Hu'), Js('Hung'), Js('Hwa'), Js('Hwan'), Js('Hwang'), Js('Hwangbo'), Js('Hyon'), Js('Hyong'), Js('Im'), Js('In'), Js('Ka'), Js('Kae'), Js('Kal'), Js('Kam'), Js('Kan'), Js('Kang'), Js('Kangjon'), Js('Ki'), Js('Kil'), Js('Kim'), Js('Ko'), Js('Kok'), Js('Kong'), Js('Ku'), Js('Kuk'), Js('Kum'), Js('Kun'), Js('Kung'), Js('Kwak'), Js('Kwok'), Js('Kwon'), Js('Kye'), Js('Kyo'), Js('Kyon'), Js('Kyong'), Js('Ma'), Js('Mae'), Js('Maeng'), Js('Man'), Js('Mangjol'), Js('Mi'), Js('Min'), Js('Mo'), Js('Mok'), Js('Muk'), Js('Mun'), Js('Myo'), Js('Myong'), Js('Na'), Js('Nae'), Js('Nam'), Js('Namgung'), Js('Nan'), Js('Nang'), Js('No'), Js('Noe'), Js('Nu'), Js('Ogum'), Js('Oh'), Js('Ok'), Js('Om'), Js('On'), Js('Ong'), Js("P'aeng"), Js("P'an"), Js("P'i"), Js("P'il"), Js("P'o"), Js("P'ung"), Js("P'yo"), Js("P'yon"), Js("P'yong"), Js('Pae'), Js('Paek'), Js('Pak'), Js('Pan'), Js('Pang'), Js('Pi'), Js('Pin'), Js('Ping'), Js('Pok'), Js('Pom'), Js('Pong'), Js('Pu'), Js('Pyon'), Js('Ra'), Js('Ran'), Js('Rang'), Js('Ri'), Js('Rim'), Js('Ro'), Js('Roe'), Js('Ru'), Js('Ryang'), Js('Ryo'), Js('Ryom'), Js('Ryon'), Js('Ryong'), Js('Ryu'), Js('Ryuk'), Js('Sa'), Js('Sagong'), Js('Sam'), Js('Sang'), Js('Si'), Js('Sim'), Js('Sin'), Js('Sip'), Js('So'), Js('Sobong'), Js('Sok'), Js('Sol'), Js('Somun'), Js('Son'), Js('Song'), Js('Sonu'), Js('Sop'), Js('Su'), Js('Sun'), Js('Sung'), Js("T'ae"), Js("T'ak"), Js("T'an"), Js('Tae'), Js('Tam'), Js('Tan'), Js('Tang'), Js('To'), Js('Tokko'), Js('Ton'), Js('Tong'), Js('Tongbang'), Js('Tu'), Js('Uh'), Js('Um'), Js('Un'), Js('Wang'), Js('Wi'), Js('Won'), Js('Wu'), Js('Ya'), Js('Yang'), Js('Ye'), Js('Yi'), Js('Yo'), Js('Yom'), Js('Yon'), Js('Yong'), Js('Yop'), Js('Yu'), Js('Yuk'), Js('Yun')]))
var.put('nm27', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('q'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('ts'), Js('x'), Js('y'), Js('z'), Js('zh')]))
var.put('nm28', Js([Js('aie'), Js('aa'), Js('ei'), Js('aiu'), Js('ua'), Js('uu'), Js('eio'), Js('oi'), Js('ai'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm29', Js([Js('b'), Js('cch'), Js('ch'), Js('d'), Js('dk'), Js('dy'), Js('g'), Js('gh'), Js('ght'), Js('gm'), Js('gs'), Js('j'), Js('k'), Js('kh'), Js('khg'), Js('khj'), Js('kt'), Js('l'), Js('lb'), Js('lch'), Js('ld'), Js('lg'), Js('lgh'), Js('lj'), Js('lt'), Js('lz'), Js('m'), Js('mb'), Js('ml'), Js('n'), Js('nb'), Js('ndj'), Js('ng'), Js('ngg'), Js('ngs'), Js('nksh'), Js('nt'), Js('nz'), Js('q'), Js('r'), Js('rch'), Js('rd'), Js('rg'), Js('rgh'), Js('rk'), Js('rkh'), Js('rt'), Js('s'), Js('sg'), Js('sh'), Js('sl'), Js('t'), Js('tb'), Js('tg'), Js('tl'), Js('ts'), Js('y'), Js('z'), Js('zb'), Js('zh')]))
var.put('nm30', Js([Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('gh'), Js('gt'), Js('l'), Js('ld'), Js('m'), Js('n'), Js('nt'), Js('r'), Js('t'), Js('y')]))
var.put('nm31', Js([Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('c'), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('ts'), Js('y'), Js('z'), Js('zh')]))
var.put('nm32', Js([Js('aa'), Js('ui'), Js('ei'), Js('oa'), Js('ui'), Js('ai'), Js('uu'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm33', Js([Js('b'), Js('ch'), Js('d'), Js('dts'), Js('dv'), Js('g'), Js('gch'), Js('gh'), Js('gm'), Js('gtb'), Js('j'), Js('k'), Js('kh'), Js('khg'), Js('khts'), Js('l'), Js('lj'), Js('lm'), Js('lt'), Js('m'), Js('mb'), Js('n'), Js('nb'), Js('nch'), Js('ng'), Js('nkhh'), Js('nkht'), Js('nkhts'), Js('nts'), Js('nts'), Js('nz'), Js('q'), Js('r'), Js('rb'), Js('rd'), Js('rdz'), Js('rg'), Js('rgh'), Js('rm'), Js('rt'), Js('rz'), Js('s'), Js('t'), Js('ts'), Js('tts'), Js('y'), Js('z')]))
var.put('nm34', Js([Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('gh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('sh')]))
var.put('nm35', Js([Js('a'), Js('ba'), Js('bai'), Js('be'), Js('bo'), Js('bu'), Js('chi'), Js('da'), Js('dai'), Js('ei'), Js('fu'), Js('ga'), Js('ge'), Js('gi'), Js('go'), Js('ha'), Js('hei'), Js('hi'), Js('ho'), Js('hyo'), Js('i'), Js('ie'), Js('jo'), Js('ju'), Js('ka'), Js('ke'), Js('kei'), Js('ki'), Js('ko'), Js('ku'), Js('kyu'), Js('ma'), Js('mi'), Js('mo'), Js('mu'), Js('na'), Js('nao'), Js('ni'), Js('no'), Js('o'), Js('ri'), Js('ro'), Js('ryo'), Js('ryu'), Js('sa'), Js('se'), Js('sei'), Js('shi'), Js('sho'), Js('shu'), Js('so'), Js('su'), Js('ta'), Js('te'), Js('tei'), Js('to'), Js('tsu'), Js('u'), Js('wa'), Js('ya'), Js('yo'), Js('yu')]))
var.put('nm36', Js([Js('bumi'), Js('buro'), Js('buru'), Js('chemon'), Js('chi'), Js('chiro'), Js('chiyo'), Js('chizo'), Js('dayu'), Js('deki'), Js('do'), Js('fu'), Js('fumi'), Js('gobei'), Js('goro'), Js('hari'), Js('haru'), Js('hide'), Js('hiko'), Js('hira'), Js('hiro'), Js('hisa'), Js('hito'), Js('ji'), Js('jio'), Js('jiro'), Js('juro'), Js('kado'), Js('kan'), Js('kao'), Js('karu'), Js('kazu'), Js('kei'), Js('ki'), Js('kichi'), Js('kin'), Js('kio'), Js('kira'), Js('ko'), Js('koto'), Js('kuchu'), Js('kudo'), Js('kumi'), Js('kuni'), Js('kusai'), Js('kushi'), Js('kusho'), Js('kuzo'), Js('mane'), Js('maro'), Js('masu'), Js('matsu'), Js('mei'), Js('miaki'), Js('michi'), Js('mio'), Js('mitsu'), Js('mon'), Js('mori'), Js('moru'), Js('moto'), Js('mune'), Js('nabu'), Js('naga'), Js('nari'), Js('nji'), Js('njiro'), Js('nkei'), Js('nko'), Js('nobu'), Js('nori'), Js('noru'), Js('noto'), Js('noye'), Js('npaku'), Js('nshiro'), Js('ntaro'), Js('nzo'), Js('rata'), Js('rei'), Js('ro'), Js('roji'), Js('roshi'), Js('ru'), Js('sada'), Js('sake'), Js('saku'), Js('sami'), Js('samu'), Js('sashi'), Js('sato'), Js('seki'), Js('setsu'), Js('shashi'), Js('shi'), Js('shige'), Js('shiko'), Js('shiro'), Js('sho'), Js('shushu'), Js('soshi'), Js('su'), Js('suke'), Js('suki'), Js('ta'), Js('tada'), Js('taka'), Js('tane'), Js('tari'), Js('taro'), Js('taru'), Js('toki'), Js('toku'), Js('tomo'), Js('tora'), Js('toshi'), Js('tsu'), Js('tsugu'), Js('tsumi'), Js('tsuna'), Js('tsune'), Js('tsuta'), Js('tsuyo'), Js('tzumi'), Js('wane'), Js('yaki'), Js('yasu'), Js('yori'), Js('yoshi'), Js('yuki'), Js('zane'), Js('zo'), Js('zuka'), Js('zuki'), Js('zuko'), Js('zuma'), Js('zumi'), Js('zumo'), Js('zushi')]))
var.put('nm37', Js([Js('a'), Js('ai'), Js('ba'), Js('be'), Js('chi'), Js('e'), Js('ei'), Js('fu'), Js('ge'), Js('ha'), Js('hai'), Js('hi'), Js('ho'), Js('i'), Js('jo'), Js('ka'), Js('kae'), Js('ki'), Js('ko'), Js('ku'), Js('ma'), Js('mae'), Js('me'), Js('mi'), Js('mo'), Js('mu'), Js('na'), Js('nao'), Js('ni'), Js('no'), Js('o'), Js('rai'), Js('rei'), Js('ri'), Js('ro'), Js('ru'), Js('sa'), Js('sai'), Js('se'), Js('shi'), Js('su'), Js('ta'), Js('te'), Js('to'), Js('tsu'), Js('u'), Js('wa'), Js('ya'), Js('yae'), Js('yo'), Js('yu')]))
var.put('nm38', Js([Js('bari'), Js('chi'), Js('chiha'), Js('chiho'), Js('chiko'), Js('cho'), Js('deko'), Js('doka'), Js('fumi'), Js('fuyu'), Js('gino'), Js('gusa'), Js('haru'), Js('hiro'), Js('ho'), Js('hoko'), Js('homi'), Js('hori'), Js('jiko'), Js('ka'), Js('kage'), Js('kako'), Js('kami'), Js('kane'), Js('kari'), Js('karu'), Js('kaze'), Js('ki'), Js('kichi'), Js('kiko'), Js('kina'), Js('kio'), Js('kira'), Js('ko'), Js('koto'), Js('kuko'), Js('kuma'), Js('kuro'), Js('kyo'), Js('maki'), Js('mako'), Js('mari'), Js('maya'), Js('meka'), Js('meko'), Js('mi'), Js('miho'), Js('mika'), Js('miki'), Js('miko'), Js('mina'), Js('miri'), Js('miya'), Js('mugi'), Js('na'), Js('nae'), Js('nai'), Js('nako'), Js('nami'), Js('natsu'), Js('neka'), Js('neko'), Js('niko'), Js('no'), Js('noka'), Js('nomi'), Js('noue'), Js('nu'), Js('nuko'), Js('nuye'), Js('nuyo'), Js('ra'), Js('rako'), Js('rante'), Js('rari'), Js('rea'), Js('ri'), Js('rika'), Js('riko'), Js('rime'), Js('rimi'), Js('rino'), Js('risa'), Js('risu'), Js('rize'), Js('ro'), Js('roe'), Js('roko'), Js('romi'), Js('roshi'), Js('ru'), Js('rui'), Js('ruka'), Js('ruko'), Js('rumi'), Js('sa'), Js('sae'), Js('sahi'), Js('saji'), Js('saki'), Js('sako'), Js('sami'), Js('samu'), Js('sano'), Js('sato'), Js('se'), Js('shi'), Js('shiko'), Js('shiyo'), Js('soko'), Js('sono'), Js('suka'), Js('suki'), Js('sumi'), Js('suzu'), Js('taba'), Js('tako'), Js('taru'), Js('to'), Js('tomi'), Js('tomo'), Js('tose'), Js('toshi'), Js('tsu'), Js('tsue'), Js('tsuka'), Js('tsuko'), Js('tsumi'), Js('tsune'), Js('tsuyo'), Js('yaka'), Js('yako'), Js('yame'), Js('yano'), Js('yeko'), Js('yo'), Js('yu'), Js('yuka'), Js('yuki'), Js('yuko'), Js('yume'), Js('yumi'), Js('yuri'), Js('zami'), Js('zu'), Js('zue'), Js('zuki'), Js('zuko'), Js('zumi'), Js('zuru'), Js('zusa')]))
var.put('nm39', Js([Js('a'), Js('aka'), Js('ama'), Js('ao'), Js('ara'), Js('asa'), Js('ashi'), Js('azu'), Js('chi'), Js('e'), Js('fu'), Js('fuji'), Js('fuku'), Js('furu'), Js('go'), Js('ha'), Js('hagi'), Js('hama'), Js('hara'), Js('hata'), Js('haya'), Js('hi'), Js('hira'), Js('hiro'), Js('ho'), Js('i'), Js('ichi'), Js('iga'), Js('ike'), Js('ima'), Js('ina'), Js('ise'), Js('ishi'), Js('iwa'), Js('ka'), Js('kaga'), Js('kane'), Js('kawa'), Js('ki'), Js('kishi'), Js('kita'), Js('ko'), Js('koya'), Js('ku'), Js('kura'), Js('kuri'), Js('kuro'), Js('kusu'), Js('ma'), Js('mae'), Js('masu'), Js('matsu'), Js('mi'), Js('mika'), Js('miya'), Js('mo'), Js('mori'), Js('mu'), Js('mura'), Js('na'), Js('naga'), Js('naka'), Js('ni'), Js('nishi'), Js('no'), Js('nomu'), Js('nona'), Js('o'), Js('oga'), Js('oka'), Js('oku'), Js('osa'), Js('sa'), Js('saka'), Js('saku'), Js('sawa'), Js('saza'), Js('se'), Js('shi'), Js('shiba'), Js('shima'), Js('shimi'), Js('shimo'), Js('shino'), Js('so'), Js('su'), Js('suga'), Js('sugi'), Js('sumi'), Js('ta'), Js('taba'), Js('tachi'), Js('taga'), Js('taha'), Js('taka'), Js('tama'), Js('tana'), Js('tani'), Js('te'), Js('tera'), Js('to'), Js('toku'), Js('tsu'), Js('u'), Js('ue'), Js('uye'), Js('wa'), Js('waka'), Js('wata'), Js('ya'), Js('yama'), Js('yoko'), Js('yoshi')]))
var.put('nm40', Js([Js('ba'), Js('bara'), Js('bashi'), Js('bata'), Js('be'), Js('bota'), Js('chi'), Js('chida'), Js('da'), Js('dama'), Js('gai'), Js('gamine'), Js('gano'), Js('gashi'), Js('gata'), Js('gawa'), Js('gi'), Js('guchi'), Js('hara'), Js('hira'), Js('hita'), Js('jima'), Js('jino'), Js('kada'), Js('kaga'), Js('kai'), Js('kaki'), Js('kama'), Js('kami'), Js('kawa'), Js('ki'), Js('kino'), Js('kuchi'), Js('kuda'), Js('kui'), Js('ma'), Js('mada'), Js('magai'), Js('mano'), Js('mari'), Js('matsu'), Js('maya'), Js('mei'), Js('mine'), Js('miya'), Js('mori'), Js('moto'), Js('mura'), Js('naga'), Js('nagi'), Js('nai'), Js('naka'), Js('name'), Js('nda'), Js('ndo'), Js('neko'), Js('nishi'), Js('nno'), Js('no'), Js('ra'), Js('rada'), Js('rai'), Js('rano'), Js('rashi'), Js('rata'), Js('raya'), Js('ri'), Js('rine'), Js('rino'), Js('rita'), Js('roda'), Js('rose'), Js('rota'), Js('ruta'), Js('ruya'), Js('sai'), Js('saki'), Js('sano'), Js('sato'), Js('sawa'), Js('se'), Js('shi'), Js('shida'), Js('shigawa'), Js('shige'), Js('shima'), Js('shino'), Js('shiro'), Js('shita'), Js('suda'), Js('ta'), Js('tani'), Js('to'), Js('tori'), Js('tsuda'), Js('tsuno'), Js('wa'), Js('wano'), Js('wara'), Js('wata'), Js('ya'), Js('yabu'), Js('yake'), Js('yama'), Js('yashi'), Js('yata'), Js('yeda'), Js('yoshi'), Js('zaki'), Js('zuki'), Js('zuma'), Js('zumi')]))
var.put('nm41', Js([Js('b'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('p'), Js('q'), Js('r'), Js('sh'), Js('s'), Js('t'), Js('ts'), Js('w'), Js('x'), Js('y'), Js('z'), Js('zh')]))
var.put('nm42', Js([Js('ai'), Js('uo'), Js('ao'), Js('eu'), Js('ia'), Js('ua'), Js('uo'), Js('ei'), Js('ui'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm43', Js([Js('ch'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('nch'), Js('nf'), Js('ng'), Js('ngb'), Js('ngf'), Js('ngg'), Js('ngh'), Js('ngk'), Js('ngl'), Js('ngm'), Js('ngp'), Js('ngq'), Js('ngsh'), Js('ngw'), Js('ngx'), Js('ngzh'), Js('nh'), Js('nj'), Js('nl'), Js('nm'), Js('nsh'), Js('ny'), Js('nz'), Js('q'), Js('r'), Js('sh'), Js('t'), Js('w'), Js('x'), Js('y'), Js('z'), Js('zh')]))
var.put('nm44', Js([Js(''), Js(''), Js(''), Js('n'), Js('ng')]))
var.put('nm45', Js([Js('b'), Js('ch'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('kw'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('sh'), Js('s'), Js('t'), Js('w'), Js('x'), Js('y'), Js('zh'), Js('z')]))
var.put('nm46', Js([Js('ao'), Js('ua'), Js('ai'), Js('ui'), Js('ia'), Js('ei'), Js('ue'), Js('iu'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm47', Js([Js('b'), Js('c'), Js('ch'), Js('d'), Js('f'), Js('h'), Js('hw'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('nd'), Js('nf'), Js('ng'), Js('ngch'), Js('ngg'), Js('ngh'), Js('ngj'), Js('ngl'), Js('ngm'), Js('ngt'), Js('ngx'), Js('ngy'), Js('ngzh'), Js('nh'), Js('nl'), Js('nm'), Js('nq'), Js('nr'), Js('nt'), Js('nx'), Js('ny'), Js('nzh'), Js('q'), Js('r'), Js('sh'), Js('t'), Js('w'), Js('x'), Js('y'), Js('zh')]))
var.put('nm48', Js([Js('b'), Js('c'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('h'), Js('hs'), Js('hw'), Js('j'), Js('k'), Js('kh'), Js('kw'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('sz'), Js('t'), Js('ts'), Js('w'), Js('x'), Js('y'), Js('zh'), Js('z')]))
var.put('nm49', Js([Js('ai'), Js('ao'), Js('au'), Js('ee'), Js('ea'), Js('eo'), Js('eu'), Js('ia'), Js('iao'), Js('ie'), Js('io'), Js('ua'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm50', Js([Js('b'), Js('c'), Js('d'), Js('dj'), Js('dw'), Js('g'), Js('h'), Js('j'), Js('kr'), Js('k'), Js('p'), Js('r'), Js('s'), Js('sl'), Js('t'), Js('tr'), Js('w'), Js('y')]))
var.put('nm51', Js([Js('ua'), Js('ia'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm52', Js([Js('b'), Js('d'), Js('dd'), Js('dw'), Js('g'), Js('h'), Js('hy'), Js('j'), Js('k'), Js('l'), Js('m'), Js('mb'), Js('md'), Js('n'), Js('nd'), Js('ndr'), Js('ngk'), Js('nn'), Js('nt'), Js('o'), Js('r'), Js('rj'), Js('rm'), Js('rn'), Js('rt'), Js('rw'), Js('ry'), Js('s'), Js('sk'), Js('sn'), Js('t'), Js('tr'), Js('v'), Js('w'), Js('y')]))
var.put('nm53', Js([Js(''), Js(''), Js(''), Js('h'), Js('n'), Js('ng'), Js('r'), Js('s'), Js('t')]))
var.put('nm54', Js([Js('b'), Js('c'), Js('d'), Js('dw'), Js('f'), Js('gl'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('sr'), Js('tr'), Js('v'), Js('w'), Js('y')]))
var.put('nm55', Js([Js('ia'), Js('eo'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm56', Js([Js('c'), Js('d'), Js('dy'), Js('g'), Js('h'), Js('hy'), Js('k'), Js('l'), Js('m'), Js('nn'), Js('nt'), Js('nd'), Js('ng'), Js('nn'), Js('nt'), Js('r'), Js('rj'), Js('rl'), Js('rm'), Js('rt'), Js('s'), Js('sk'), Js('st'), Js('t'), Js('th'), Js('tn'), Js('tr'), Js('v'), Js('w'), Js('y')]))
var.put('nm57', Js([Js(''), Js(''), Js(''), Js('h'), Js('n'), Js('r')]))
pass
pass


# Add lib to the module scope
pathfinderTian = var.to_python()
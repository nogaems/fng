__all__ = ['mgtHumans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm29', 'nm16', 'nm23', 'nm3', 'nm2', 'nm27', 'nm26', 'nm22', 'nm7', 'nm10', 'nm21', 'nm25', 'nm15', 'nm20', 'nm12', 'nm5', 'nm6', 'nm4', 'nameGen', 'nm8', 'nm28', 'nm18', 'nm17', 'nm13', 'nm9'])
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
            if PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                var.put('lName', ((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('lName', ((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                    while PyJsStrictEq(var.get('nm15').get(var.get('rnd')),var.get('nm16').get(var.get('rnd2'))):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                    var.put('lName', (var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    while PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    if (var.get('i')<Js(2.0)):
                        var.put('names', (((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('names', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6')))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                        if (var.get('i')<Js(5.0)):
                            var.put('names', ((((((((var.get('nm21').get(var.get('rnd'))+var.get('nm22').get(var.get('rnd2')))+var.get('nm20').get(var.get('rnd3')))+Js(' '))+var.get('nm21').get(var.get('rnd4')))+var.get('nm22').get(var.get('rnd5')))+var.get('nm23').get(var.get('rnd6')))+var.get('nm22').get(var.get('rnd7')))+var.get('nm20').get(var.get('rnd8'))))
                        else:
                            var.put('names', ((((((((var.get('nm21').get(var.get('rnd4'))+var.get('nm22').get(var.get('rnd5')))+var.get('nm23').get(var.get('rnd6')))+var.get('nm22').get(var.get('rnd7')))+var.get('nm20').get(var.get('rnd8')))+Js(' '))+var.get('nm21').get(var.get('rnd')))+var.get('nm22').get(var.get('rnd2')))+var.get('nm20').get(var.get('rnd3'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length'))))
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            if (var.get('i')<Js(7.0)):
                                def PyJs_LONG_0_(var=var):
                                    return var.put('names', ((((((((((var.get('nm25').get(var.get('rnd'))+var.get('nm26').get(var.get('rnd2')))+var.get('nm27').get(var.get('rnd3')))+var.get('nm26').get(var.get('rnd4')))+var.get('nm27').get(var.get('rnd5')))+var.get('nm26').get(var.get('rnd6')))+Js(' '))+var.get('nm25').get(var.get('rnd7')))+var.get('nm26').get(var.get('rnd8')))+var.get('nm27').get(var.get('rnd9')))+var.get('nm26').get(var.get('rnd10'))))
                                PyJs_LONG_0_()
                            else:
                                def PyJs_LONG_1_(var=var):
                                    return var.put('names', ((((((((((var.get('nm25').get(var.get('rnd7'))+var.get('nm26').get(var.get('rnd8')))+var.get('nm27').get(var.get('rnd9')))+var.get('nm26').get(var.get('rnd10')))+Js(' '))+var.get('nm25').get(var.get('rnd')))+var.get('nm26').get(var.get('rnd2')))+var.get('nm27').get(var.get('rnd3')))+var.get('nm26').get(var.get('rnd4')))+var.get('nm27').get(var.get('rnd5')))+var.get('nm26').get(var.get('rnd6'))))
                                PyJs_LONG_1_()
                        else:
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm29').get('length'))))
                            var.put('names', ((var.get('nm28').get(var.get('rnd'))+Js(' '))+var.get('nm29').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    if (var.get('rnd')<Js(3.0)):
                        while (var.get('rnd5')<Js(3.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('i')<Js(2.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                        if (var.get('i')<Js(5.0)):
                            var.put('names', ((((((((var.get('nm17').get(var.get('rnd'))+var.get('nm18').get(var.get('rnd2')))+var.get('nm20').get(var.get('rnd3')))+Js(' '))+var.get('nm17').get(var.get('rnd4')))+var.get('nm18').get(var.get('rnd5')))+var.get('nm19').get(var.get('rnd6')))+var.get('nm18').get(var.get('rnd7')))+var.get('nm20').get(var.get('rnd8'))))
                        else:
                            var.put('names', ((((((((var.get('nm17').get(var.get('rnd4'))+var.get('nm18').get(var.get('rnd5')))+var.get('nm19').get(var.get('rnd6')))+var.get('nm18').get(var.get('rnd7')))+var.get('nm20').get(var.get('rnd8')))+Js(' '))+var.get('nm17').get(var.get('rnd')))+var.get('nm18').get(var.get('rnd2')))+var.get('nm20').get(var.get('rnd3'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length'))))
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                            if (var.get('i')<Js(7.0)):
                                def PyJs_LONG_2_(var=var):
                                    return var.put('names', ((((((((((var.get('nm25').get(var.get('rnd'))+var.get('nm26').get(var.get('rnd2')))+var.get('nm27').get(var.get('rnd3')))+var.get('nm26').get(var.get('rnd4')))+var.get('nm27').get(var.get('rnd5')))+var.get('nm26').get(var.get('rnd6')))+Js(' '))+var.get('nm25').get(var.get('rnd7')))+var.get('nm26').get(var.get('rnd8')))+var.get('nm27').get(var.get('rnd9')))+var.get('nm26').get(var.get('rnd10'))))
                                PyJs_LONG_2_()
                            else:
                                def PyJs_LONG_3_(var=var):
                                    return var.put('names', ((((((((((var.get('nm25').get(var.get('rnd7'))+var.get('nm26').get(var.get('rnd8')))+var.get('nm27').get(var.get('rnd9')))+var.get('nm26').get(var.get('rnd10')))+Js(' '))+var.get('nm25').get(var.get('rnd')))+var.get('nm26').get(var.get('rnd2')))+var.get('nm27').get(var.get('rnd3')))+var.get('nm26').get(var.get('rnd4')))+var.get('nm27').get(var.get('rnd5')))+var.get('nm26').get(var.get('rnd6'))))
                                PyJs_LONG_3_()
                        else:
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm29').get('length'))))
                            var.put('names', ((var.get('nm28').get(var.get('rnd'))+Js(' '))+var.get('nm29').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('cr'), Js('d'), Js('dr'), Js('g'), Js('l'), Js('n'), Js('r'), Js('t'), Js('tr'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('ie'), Js('ea'), Js('ia')]))
var.put('nm3', Js([Js('d'), Js('dr'), Js('dd'), Js('g'), Js('gr'), Js('gn'), Js('kn'), Js('kk'), Js('kr'), Js('l'), Js('ll'), Js('lr'), Js('lb'), Js('lv'), Js('ng'), Js('nd'), Js('nv'), Js('r'), Js('rc'), Js('rr'), Js('rk'), Js('rt'), Js('sr'), Js('v'), Js('vr'), Js('x')]))
var.put('nm4', Js([Js('d'), Js('m'), Js('n'), Js('r'), Js('t'), Js('y'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('l'), Js('n'), Js('r'), Js('s'), Js('x')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('f'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('th'), Js('v'), Js('y')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ou'), Js('ia'), Js('ea'), Js('ae'), Js('ei'), Js('ie')]))
var.put('nm8', Js([Js('d'), Js('dr'), Js('l'), Js('ll'), Js('lm'), Js('ln'), Js('lv'), Js('m'), Js('mm'), Js('n'), Js('ndr'), Js('nr'), Js('nl'), Js('ng'), Js('nth'), Js('r'), Js('rr'), Js('rl'), Js('sm'), Js('s'), Js('st'), Js('sh'), Js('t'), Js('th'), Js('x'), Js('y'), Js('z')]))
var.put('nm9', Js([Js('l'), Js('ll'), Js('ly'), Js('m'), Js('n'), Js('nt'), Js('nz'), Js('r'), Js('rr'), Js('s'), Js('sh'), Js('v'), Js('x')]))
var.put('nm10', Js([Js('b'), Js('br'), Js('c'), Js('d'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('l'), Js('m'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm11', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm12', Js([Js('ct'), Js('cn'), Js('cc'), Js('ddl'), Js('dr'), Js('dk'), Js('dl'), Js('gss'), Js('gz'), Js('gs'), Js('kk'), Js('kt'), Js('ks'), Js('ll'), Js('ld'), Js('lld'), Js('lv'), Js('ltr'), Js('nc'), Js('ntr'), Js('nd'), Js('nk'), Js('nz'), Js('rc'), Js('rtr'), Js('rk'), Js('rs'), Js('rn'), Js('st'), Js('sc'), Js('shc'), Js('ts'), Js('tk'), Js('zc'), Js('ztr')]))
var.put('nm13', Js([Js('c'), Js('n'), Js('ns'), Js('nd'), Js('r'), Js('rd'), Js('s'), Js('ss')]))
var.put('nm15', Js([Js('alpen'), Js('amber'), Js('ash'), Js('autumn'), Js('axe'), Js('barley'), Js('battle'), Js('bear'), Js('black'), Js('blade'), Js('blaze'), Js('blood'), Js('blue'), Js('bone'), Js('boulder'), Js('bright'), Js('bronze'), Js('burning'), Js('cask'), Js('chest'), Js('cinder'), Js('clan'), Js('claw'), Js('clear'), Js('cliff'), Js('cloud'), Js('cold'), Js('common'), Js('coven'), Js('crag'), Js('crest'), Js('crow'), Js('crystal'), Js('dark'), Js('dawn'), Js('day'), Js('dead'), Js('death'), Js('deep'), Js('dew'), Js('dirge'), Js('distant'), Js('doom'), Js('down'), Js('dragon'), Js('dream'), Js('dusk'), Js('dust'), Js('eagle'), Js('earth'), Js('elf'), Js('ember'), Js('even'), Js('fallen'), Js('far'), Js('farrow'), Js('feather'), Js('fern'), Js('fire'), Js('fist'), Js('flame'), Js('flat'), Js('flint'), Js('fog'), Js('fore'), Js('forest'), Js('four'), Js('free'), Js('frost'), Js('frozen'), Js('full'), Js('fuse'), Js('gloom'), Js('glory'), Js('glow'), Js('gold'), Js('gore'), Js('grand'), Js('grass'), Js('gray'), Js('great'), Js('green'), Js('grizzly'), Js('hallow'), Js('hallowed'), Js('hammer'), Js('hard'), Js('haven'), Js('hawk'), Js('haze'), Js('heart'), Js('heavy'), Js('hell'), Js('high'), Js('hill'), Js('holy'), Js('honor'), Js('horse'), Js('humble'), Js('hydra'), Js('ice'), Js('iron'), Js('keen'), Js('laughing'), Js('leaf'), Js('light'), Js('lightning'), Js('lion'), Js('lone'), Js('long'), Js('low'), Js('luna'), Js('marble'), Js('marsh'), Js('master'), Js('meadow'), Js('mild'), Js('mirth'), Js('mist'), Js('molten'), Js('monster'), Js('moon'), Js('morning'), Js('moss'), Js('mountain'), Js('mourn'), Js('mourning'), Js('nether'), Js('nickle'), Js('night'), Js('noble'), Js('nose'), Js('oat'), Js('ocean'), Js('orb'), Js('pale'), Js('peace'), Js('phoenix'), Js('pine'), Js('plain'), Js('pride'), Js('proud'), Js('pyre'), Js('rage'), Js('rain'), Js('rapid'), Js('raven'), Js('red'), Js('regal'), Js('rich'), Js('river'), Js('rock'), Js('rose'), Js('rough'), Js('rumble'), Js('rune'), Js('sacred'), Js('sage'), Js('saur'), Js('sea'), Js('serpent'), Js('shade'), Js('shadow'), Js('sharp'), Js('shield'), Js('silent'), Js('silver'), Js('simple'), Js('single'), Js('skull'), Js('sky'), Js('slate'), Js('smart'), Js('snake'), Js('snow'), Js('soft'), Js('solid'), Js('spider'), Js('spirit'), Js('spring'), Js('stag'), Js('star'), Js('steel'), Js('stern'), Js('still'), Js('stone'), Js('storm'), Js('stout'), Js('strong'), Js('summer'), Js('sun'), Js('swift'), Js('tall'), Js('tarren'), Js('terra'), Js('three'), Js('thunder'), Js('titan'), Js('tree'), Js('true'), Js('truth'), Js('tusk'), Js('twilight'), Js('two'), Js('void'), Js('war'), Js('water'), Js('wheat'), Js('whisper'), Js('whit'), Js('white'), Js('wild'), Js('willow'), Js('wind'), Js('winter'), Js('wise'), Js('wolf'), Js('wood'), Js('wooden'), Js('wyvern'), Js('young')]))
var.put('nm16', Js([Js('arm'), Js('arrow'), Js('ash'), Js('axe'), Js('bane'), Js('bash'), Js('basher'), Js('beam'), Js('beard'), Js('belly'), Js('bend'), Js('bender'), Js('binder'), Js('blade'), Js('blaze'), Js('bleeder'), Js('blight'), Js('blood'), Js('bloom'), Js('blossom'), Js('blower'), Js('bluff'), Js('bone'), Js('bough'), Js('bow'), Js('brace'), Js('braid'), Js('branch'), Js('brand'), Js('breaker'), Js('breath'), Js('breeze'), Js('brew'), Js('bringer'), Js('brook'), Js('brooke'), Js('brow'), Js('caller'), Js('chaser'), Js('chewer'), Js('claw'), Js('cleaver'), Js('cloud'), Js('crag'), Js('creek'), Js('crest'), Js('crusher'), Js('cut'), Js('cutter'), Js('dancer'), Js('dane'), Js('dew'), Js('doom'), Js('down'), Js('draft'), Js('dream'), Js('dreamer'), Js('drifter'), Js('dust'), Js('eye'), Js('eyes'), Js('fall'), Js('fallow'), Js('fang'), Js('feather'), Js('fire'), Js('fist'), Js('flame'), Js('flare'), Js('flaw'), Js('flayer'), Js('flow'), Js('flower'), Js('follower'), Js('force'), Js('forest'), Js('forge'), Js('fury'), Js('gaze'), Js('gazer'), Js('gem'), Js('glade'), Js('gleam'), Js('glide'), Js('gloom'), Js('glory'), Js('glow'), Js('grain'), Js('grip'), Js('grove'), Js('guard'), Js('gust'), Js('hair'), Js('hammer'), Js('hand'), Js('heart'), Js('hell'), Js('helm'), Js('hide'), Js('horn'), Js('hunter'), Js('jumper'), Js('keep'), Js('keeper'), Js('killer'), Js('lance'), Js('lash'), Js('leaf'), Js('less'), Js('light'), Js('mane'), Js('mantle'), Js('mark'), Js('maul'), Js('maw'), Js('might'), Js('moon'), Js('more'), Js('mourn'), Js('oak'), Js('orb'), Js('ore'), Js('peak'), Js('pelt'), Js('pike'), Js('punch'), Js('rage'), Js('reaper'), Js('reaver'), Js('rider'), Js('ridge'), Js('ripper'), Js('river'), Js('roar'), Js('rock'), Js('root'), Js('run'), Js('runner'), Js('scar'), Js('scream'), Js('scribe'), Js('seeker'), Js('shade'), Js('shadow'), Js('shaper'), Js('shard'), Js('shield'), Js('shine'), Js('shot'), Js('shout'), Js('singer'), Js('sky'), Js('slayer'), Js('snarl'), Js('snout'), Js('snow'), Js('soar'), Js('song'), Js('sorrow'), Js('spark'), Js('spear'), Js('spell'), Js('spire'), Js('spirit'), Js('splitter'), Js('sprinter'), Js('stalker'), Js('star'), Js('steam'), Js('steel'), Js('stone'), Js('stream'), Js('strength'), Js('stride'), Js('strider'), Js('strike'), Js('striker'), Js('sun'), Js('surge'), Js('swallow'), Js('swift'), Js('sword'), Js('sworn'), Js('tail'), Js('taker'), Js('talon'), Js('thorn'), Js('thorne'), Js('tide'), Js('toe'), Js('track'), Js('trap'), Js('trapper'), Js('tree'), Js('vale'), Js('valor'), Js('vigor'), Js('walker'), Js('ward'), Js('watcher'), Js('water'), Js('weaver'), Js('whirl'), Js('whisk'), Js('whisper'), Js('willow'), Js('wind'), Js('winds'), Js('wing'), Js('wolf'), Js('wood'), Js('woods'), Js('wound')]))
var.put('nm17', Js([Js('b'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('l'), Js('m'), Js('q'), Js('sh'), Js('t'), Js('x'), Js('y'), Js('z'), Js('zh')]))
var.put('nm18', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('ua'), Js('oa'), Js('ai'), Js('uo'), Js('iu'), Js('iao')]))
var.put('nm19', Js([Js('b'), Js('ch'), Js('h'), Js('j'), Js('l'), Js('m'), Js('nch'), Js('nf'), Js('ng'), Js('ngf'), Js('ngg'), Js('ngh'), Js('ngp'), Js('ngw'), Js('ngsh'), Js('ngz'), Js('ngzh'), Js('nh'), Js('nj'), Js('nl'), Js('nm'), Js('nsh'), Js('ny'), Js('q'), Js('sh'), Js('t'), Js('w'), Js('x')]))
var.put('nm20', Js([Js(''), Js(''), Js(''), Js(''), Js('n'), Js('ng')]))
var.put('nm21', Js([Js('b'), Js('ch'), Js('d'), Js('f'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('sh'), Js('x'), Js('y'), Js('z')]))
var.put('nm22', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('eu'), Js('iao'), Js('iu'), Js('ei'), Js('uia'), Js('ia'), Js('ao'), Js('ui'), Js('ua')]))
var.put('nm23', Js([Js('d'), Js('f'), Js('h'), Js('j'), Js('l'), Js('nd'), Js('nf'), Js('ng'), Js('ngch'), Js('ngj'), Js('ngm'), Js('ngzh'), Js('nh'), Js('nm'), Js('nr'), Js('nt'), Js('nx'), Js('ny'), Js('nzh'), Js('q'), Js('sh'), Js('t'), Js('w'), Js('zh')]))
var.put('nm25', Js([Js('b'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('ry'), Js('s'), Js('sh'), Js('t'), Js('ts'), Js('w'), Js('y')]))
var.put('nm26', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm27', Js([Js('b'), Js('ch'), Js('d'), Js('g'), Js('j'), Js('k'), Js('m'), Js('n'), Js('nj'), Js('nn'), Js('np'), Js('nt'), Js('nz'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('ts'), Js('w'), Js('y'), Js('z')]))
var.put('nm28', Js([Js('Aberrant'), Js('Abyssal'), Js('Academy'), Js('Accursed'), Js('Advanced'), Js('Aerie'), Js('Afflicted'), Js('Agile'), Js('Alabaster'), Js('Ancestral'), Js('Ancient'), Js('Angelic'), Js('Arcane'), Js('Bandit'), Js('Battle'), Js('Bold'), Js('Brilliant'), Js('Bruised'), Js('Defiant'), Js('Delirious'), Js('Deserted'), Js('Devoted'), Js('Dutiful'), Js('Exalted'), Js('Fearless'), Js('Focused'), Js('Forsaken'), Js('Fury'), Js('Gifted'), Js('Grand'), Js('Grim'), Js('Hidden'), Js('Honorable'), Js('Humble'), Js('Lone'), Js('Lost'), Js('Loyal'), Js('Minor'), Js('Mysterious'), Js('Nervous'), Js('Nimble'), Js('Obedient'), Js('Old'), Js('Powerful'), Js('Prime'), Js('Proud'), Js('Reckless'), Js('Remorseful'), Js('Royal'), Js('Shady'), Js('Silent'), Js('Stark'), Js('Suspicious'), Js('Swift'), Js('Venerated'), Js('Vengeful'), Js('Vigilant'), Js('Violent'), Js('Wicked'), Js('Wild'), Js('Worn'), Js('Wretched'), Js('Zephyr')]))
var.put('nm29', Js([Js('Adept'), Js('Arcanist'), Js('Archer'), Js('Artisan'), Js('Bard'), Js('Bladeweaver'), Js('Champion'), Js('Cleric'), Js('Conjurer'), Js('Dancer'), Js('Escort'), Js('Explorer'), Js('Guard'), Js('Guardian'), Js('Gunslinger'), Js('Hero'), Js('Hunter'), Js('Illusionist'), Js('Infiltrator'), Js('Inquisitor'), Js('Journeyman'), Js('Keeper'), Js('Knight'), Js('Legionnaire'), Js('Lookout'), Js('Mage'), Js('Marine'), Js('Mechanic'), Js('Mercenary'), Js('Minion'), Js('Navigator'), Js('Outrider'), Js('Paratrooper'), Js('Patrol'), Js('Pilot'), Js('Ranger'), Js('Recruit'), Js('Recruiter'), Js('Rider'), Js('Rogue'), Js('Runner'), Js('Sage'), Js('Scavenger'), Js('Scout'), Js('Seer'), Js('Sentinel'), Js('Shepherd'), Js('Shieldguard'), Js('Soldier'), Js('Specialist'), Js('Spellweaver'), Js('Spy'), Js('Stormsinger'), Js('Technician'), Js('Tender'), Js('Trooper'), Js('Vanguard'), Js('Veteran'), Js('Warden'), Js('Warmonger'), Js('Warrior'), Js('Watch'), Js('Watcher'), Js('Weaver')]))
pass
pass


# Add lib to the module scope
mgtHumans = var.to_python()
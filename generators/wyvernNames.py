__all__ = ['wyvernNames']

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
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm6').get(var.get('rnd')),var.get('nm8').get(var.get('rnd3'))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm10').get(var.get('rnd5')),var.get('nm8').get(var.get('rnd3'))):
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                if (var.get('i')<Js(7.0)):
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm8').get(var.get('rnd3'))):
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd5'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm11').get(var.get('rnd')),var.get('nm13').get(var.get('rnd3'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm15').get(var.get('rnd5')),var.get('nm13').get(var.get('rnd3'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm13').get(var.get('rnd3'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                        var.put('names', ((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm15').get(var.get('rnd5'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm5').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('br'), Js('c'), Js('cr'), Js('ch'), Js('dr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('n'), Js('q'), Js('r'), Js('t'), Js('tr'), Js('x'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('au'), Js('ei'), Js('ia'), Js('ua'), Js('uu'), Js('aa'), Js('ui')]))
var.put('nm3', Js([Js('dj'), Js('dg'), Js('dr'), Js('gr'), Js('gz'), Js('j'), Js('k'), Js('kk'), Js('kt'), Js('kg'), Js('kz'), Js('ndr'), Js('nz'), Js('ng'), Js('ngr'), Js('nn'), Js('q'), Js('qq'), Js('qr'), Js('r'), Js('rd'), Js('rg'), Js('rr'), Js('rq'), Js('rv'), Js('rch'), Js('sq'), Js('t'), Js('tr'), Js('tz'), Js('v'), Js('vr'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js('c'), Js('cc'), Js('cr'), Js('d'), Js('g'), Js('gr'), Js('k'), Js('kk'), Js('kr'), Js('n'), Js('nd'), Js('ndr'), Js('q'), Js('r'), Js('rr'), Js('sq'), Js('t'), Js('z'), Js('zz')]))
var.put('nm5', Js([Js(''), Js('c'), Js('d'), Js('g'), Js('k'), Js('n'), Js('q'), Js('t'), Js('x'), Js('z')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js('bh'), Js('c'), Js('ch'), Js('dr'), Js('g'), Js('gn'), Js('gh'), Js('h'), Js('k'), Js('kn'), Js('kh'), Js('khr'), Js('n'), Js('q'), Js('r'), Js('rh'), Js('t'), Js('th'), Js('thr'), Js('x'), Js('v'), Js('z')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('ao'), Js('ei'), Js('ia'), Js('ue'), Js('ua'), Js('aa'), Js('ae')]))
var.put('nm8', Js([Js('dd'), Js('dt'), Js('dr'), Js('g'), Js('gn'), Js('hr'), Js('hn'), Js('k'), Js('kk'), Js('kn'), Js('kr'), Js('kh'), Js('nd'), Js('nz'), Js('ng'), Js('nn'), Js('nq'), Js('q'), Js('qq'), Js('qh'), Js('qr'), Js('r'), Js('rz'), Js('rg'), Js('rr'), Js('rq'), Js('rv'), Js('rch'), Js('rh'), Js('sq'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('vr'), Js('z'), Js('zz')]))
var.put('nm9', Js([Js('c'), Js('cc'), Js('ch'), Js('d'), Js('dh'), Js('g'), Js('k'), Js('kk'), Js('kh'), Js('n'), Js('nd'), Js('nz'), Js('q'), Js('r'), Js('rr'), Js('sh'), Js('t'), Js('z'), Js('zz')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('h'), Js('n'), Js('q'), Js('s'), Js('t'), Js('th')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('dr'), Js('g'), Js('gn'), Js('gr'), Js('k'), Js('kr'), Js('n'), Js('q'), Js('r'), Js('t'), Js('tr'), Js('x'), Js('v'), Js('z')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('ao'), Js('ei'), Js('ia'), Js('ue'), Js('ua'), Js('aa'), Js('ui')]))
var.put('nm13', Js([Js('d'), Js('dd'), Js('dr'), Js('g'), Js('k'), Js('kk'), Js('kr'), Js('kg'), Js('nd'), Js('ndr'), Js('nz'), Js('ng'), Js('nn'), Js('q'), Js('qq'), Js('qr'), Js('r'), Js('rh'), Js('rq'), Js('rr'), Js('rz'), Js('rv'), Js('sq'), Js('t'), Js('tr'), Js('th'), Js('v'), Js('vr'), Js('z'), Js('zz')]))
var.put('nm14', Js([Js('c'), Js('cc'), Js('ch'), Js('d'), Js('g'), Js('k'), Js('kk'), Js('kh'), Js('n'), Js('nd'), Js('q'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('z'), Js('z')]))
var.put('nm15', Js([Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('k'), Js('n'), Js('s'), Js('q'), Js('t')]))
pass
pass


# Add lib to the module scope
wyvernNames = var.to_python()
__all__ = ['eraDwarf']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                if (var.get('rnd5')<Js(5.0)):
                    var.put('rnd4', Js(0.0))
                if (var.get('i')<Js(6.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    if (var.get('rnd')<Js(4.0)):
                        while (var.get('rnd4')<Js(5.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4'))))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('bl'), Js('d'), Js('dr'), Js('f'), Js('fl'), Js('fr'), Js('g'), Js('gr'), Js('h'), Js('ht'), Js('hv'), Js('k'), Js('kr'), Js('kv'), Js('m'), Js('n'), Js('r'), Js('sk'), Js('sv'), Js('th'), Js('thr'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('û'), Js('ó'), Js('é'), Js('á'), Js('î'), Js('â'), Js('ei'), Js('ie'), Js('eo')]))
var.put('nm3', Js([Js('d'), Js('dg'), Js('dr'), Js('fn'), Js('g'), Js('gn'), Js('gd'), Js('gm'), Js('k'), Js('kr'), Js('kksv'), Js('kn'), Js('km'), Js('ldh'), Js('ldhr'), Js('lm'), Js('m'), Js('mm'), Js('mn'), Js('nd'), Js('ndf'), Js('nn'), Js('nndr'), Js('r'), Js('rd'), Js('rg'), Js('rgh'), Js('rh'), Js('rm'), Js('rr'), Js('s'), Js('st'), Js('th'), Js('thg'), Js('thm'), Js('v'), Js('w')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('fk'), Js('g'), Js('k'), Js('kk'), Js('l'), Js('ldn'), Js('m'), Js('n'), Js('nd'), Js('r'), Js('rd'), Js('rk'), Js('rm'), Js('rn'), Js('rst'), Js('rv'), Js('s'), Js('st'), Js('th')]))
var.put('nm5', Js([Js('bh'), Js('d'), Js('dh'), Js('f'), Js('fl'), Js('fr'), Js('fn'), Js('g'), Js('gl'), Js('gh'), Js('gl'), Js('h'), Js('hn'), Js('hr'), Js('hl'), Js('hv'), Js('m'), Js('n'), Js('mh'), Js('s'), Js('th'), Js('v')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('û'), Js('í'), Js('á'), Js('ûi'), Js('io'), Js('îo')]))
var.put('nm7', Js([Js('d'), Js('df'), Js('dr'), Js('fn'), Js('fl'), Js('fr'), Js('gn'), Js('gm'), Js('gh'), Js('l'), Js('ln'), Js('lm'), Js('lr'), Js('ld'), Js('ll'), Js('m'), Js('mr'), Js('mn'), Js('mh'), Js('md'), Js('mm'), Js('nd'), Js('nr'), Js('nh'), Js('nn'), Js('n'), Js('ngl'), Js('nh'), Js('r'), Js('rd'), Js('rdr'), Js('rn'), Js('rh'), Js('s'), Js('ss'), Js('th'), Js('v'), Js('w')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('n'), Js('nn'), Js('s')]))
pass
pass


# Add lib to the module scope
eraDwarf = var.to_python()
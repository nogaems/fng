__all__ = ['swShistavanenNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if ((var.get('i')%Js(2.0))!=Js(0.0)):
                while PyJsStrictEq(var.get('rnd10'),Js(0.0)):
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(6.0)):
                    while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('bl'), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('phl'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('u'), Js('o'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('u'), Js('o'), Js('a'), Js('oo'), Js('aa'), Js('uu')]))
var.put('nm3', Js([Js('cv'), Js('cd'), Js('dv'), Js('dr'), Js('d'), Js('dd'), Js('gv'), Js('gr'), Js('gg'), Js('g'), Js('gn'), Js('k'), Js('kk'), Js('kv'), Js('kl'), Js('kr'), Js('kt'), Js('kd'), Js('lv'), Js('lr'), Js('mr'), Js('mv'), Js('nv'), Js('nr'), Js('nd'), Js('ndr'), Js('nst'), Js('r'), Js('rd'), Js('rt'), Js('vr'), Js('v'), Js('vr'), Js('vg'), Js('vgr'), Js('vd')]))
var.put('nm4', Js([Js(''), Js('c'), Js('d'), Js('f'), Js('gg'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('tt'), Js('v'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('ae'), Js('ea'), Js('ie')]))
var.put('nm8', Js([Js('c'), Js('f'), Js('ft'), Js('l'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('v'), Js('z')]))
var.put('nm9', Js([Js('b'), Js('br'), Js('c'), Js('cr'), Js('d'), Js('dr'), Js('dh'), Js('f'), Js('g'), Js('gr'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('shr'), Js('s'), Js('v'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('ie'), Js('oa'), Js('ae'), Js('oo'), Js('aa')]))
var.put('nm11', Js([Js('c'), Js('d'), Js('dr'), Js('dv'), Js('h'), Js('hr'), Js('hx'), Js('hv'), Js('kv'), Js('kr'), Js('kd'), Js('n'), Js('r'), Js('rr'), Js('v'), Js('vr'), Js('vg'), Js('x'), Js('z')]))
var.put('nm12', Js([Js(''), Js('c'), Js('d'), Js('ft'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('nn'), Js('p'), Js('q'), Js('r'), Js('rr'), Js('t'), Js('v'), Js('vl')]))
pass
pass


# Add lib to the module scope
swShistavanenNames = var.to_python()
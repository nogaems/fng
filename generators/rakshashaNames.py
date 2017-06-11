__all__ = ['rakshashaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameFem', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nameMas', 'nm7', 'nm9', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameFem_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
    if (var.get('i')<Js(4.0)):
        var.put('nMs', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4'))))
    else:
        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
        while PyJsStrictEq(var.get('nm9').get(var.get('rnd7')),var.get('nm8').get(var.get('rnd3'))):
            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
        if (var.get('i')<Js(8.0)):
            var.put('nMs', (((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd6'))))
        else:
            var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
            var.put('rnd9', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('nm4').get(var.get('rnd7')),var.get('nm4').get(var.get('rnd9'))):
                var.put('rnd9', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
            var.put('nMs', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm7').get(var.get('rnd8'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
    while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5')))):
        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    if (var.get('i')<Js(4.0)):
        var.put('nMs', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
    else:
        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        while (PyJsStrictEq(var.get('nm4').get(var.get('rnd7')),var.get('nm3').get(var.get('rnd3'))) or PyJsStrictEq(var.get('nm4').get(var.get('rnd7')),var.get('nm5').get(var.get('rnd5')))):
            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        if (var.get('i')<Js(8.0)):
            var.put('nMs', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd5'))))
        else:
            var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd9', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
            while (PyJsStrictEq(var.get('nm4').get(var.get('rnd7')),var.get('nm4').get(var.get('rnd9'))) or PyJsStrictEq(var.get('nm4').get(var.get('rnd9')),var.get('nm5').get(var.get('rnd5')))):
                var.put('rnd9', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
            var.put('nMs', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm5').get(var.get('rnd5'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameMas_.func_name = 'nameMas'
var.put('nameMas', PyJsHoisted_nameMas_)
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
                var.get('nameFem')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameFem')()
            else:
                var.get('nameMas')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameMas')()
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bg'), Js('br'), Js('c'), Js('d'), Js('dh'), Js('g'), Js('h'), Js('j'), Js('k'), Js('ks'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('v'), Js('y')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('e'), Js('o'), Js('u'), Js('a'), Js('a'), Js('a'), Js('u'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('bh'), Js('bhr'), Js('c'), Js('dr'), Js('gn'), Js('h'), Js('hm'), Js('j'), Js('jn'), Js('k'), Js('kr'), Js('l'), Js('lg'), Js('lm'), Js('m'), Js('n'), Js('nd'), Js('r'), Js('rg'), Js('rm'), Js('rp'), Js('s'), Js('shm'), Js('sk'), Js('sv'), Js('t'), Js('th'), Js('tt'), Js('v')]))
var.put('nm4', Js([Js('b'), Js('bh'), Js('d'), Js('g'), Js('h'), Js('k'), Js('n'), Js('ng'), Js('ngh'), Js('pt'), Js('rh'), Js('rm'), Js('rt'), Js('sh'), Js('shr'), Js('sth'), Js('sv'), Js('t'), Js('thy'), Js('ty'), Js('v'), Js('vy'), Js('y')]))
var.put('nm5', Js([Js(''), Js(''), Js('d'), Js('n'), Js('nt'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('y')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('c'), Js('d'), Js('dh'), Js('g'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('sh'), Js('v'), Js('y')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('a'), Js('a'), Js('a'), Js('i'), Js('i')]))
var.put('nm8', Js([Js('b'), Js('bh'), Js('bj'), Js('d'), Js('dh'), Js('dhr'), Js('dr'), Js('dv'), Js('h'), Js('j'), Js('ks'), Js('l'), Js('ly'), Js('m'), Js('mr'), Js('n'), Js('nd'), Js('ng'), Js('nt'), Js('p'), Js('pt'), Js('rg'), Js('rk'), Js('rm'), Js('ry'), Js('s'), Js('sh'), Js('sm'), Js('t'), Js('th'), Js('tr'), Js('tt'), Js('v'), Js('vh')]))
var.put('nm9', Js([Js('bh'), Js('c'), Js('cy'), Js('d'), Js('dh'), Js('dr'), Js('dv'), Js('j'), Js('k'), Js('ks'), Js('l'), Js('ly'), Js('m'), Js('mb'), Js('n'), Js('nd'), Js('ndh'), Js('ng'), Js('nt'), Js('p'), Js('pt'), Js('r'), Js('rg'), Js('rm'), Js('s'), Js('sh'), Js('sm'), Js('sn'), Js('t'), Js('th'), Js('tr'), Js('ts'), Js('tt'), Js('v'), Js('y')]))
pass
pass
pass
pass


# Add lib to the module scope
rakshashaNames = var.to_python()
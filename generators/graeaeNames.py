__all__ = ['graeaeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nameMas', 'nm2'])
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
    if (var.get('i')<Js(6.0)):
        var.put('nMs', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4'))))
    else:
        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        while PyJsStrictEq(var.get('nm4').get(var.get('rnd7')),var.get('nm3').get(var.get('rnd3'))):
            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        if (var.get('i')<Js(8.0)):
            var.put('nMs', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd4'))))
        else:
            var.put('nMs', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4'))))
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
            var.get('nameMas')()
            while PyJsStrictEq(var.get('nMs'),Js('')):
                var.get('nameMas')()
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js('c'), Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('s'), Js('t'), Js('th'), Js('v'), Js('w')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('ei'), Js('ae'), Js('ea')]))
var.put('nm3', Js([Js('d'), Js('f'), Js('ff'), Js('h'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('ny'), Js('r'), Js('rr'), Js('t'), Js('th'), Js('v'), Js('y')]))
var.put('nm4', Js([Js('lph'), Js('lphr'), Js('lr'), Js('lm'), Js('ln'), Js('mphr'), Js('mn'), Js('mph'), Js('nh'), Js('nr'), Js('nph'), Js('phr'), Js('sh'), Js('sn'), Js('sl'), Js('sph'), Js('sphr'), Js('thr')]))
var.put('nm5', Js([Js('o'), Js('o'), Js('o'), Js('o'), Js('o'), Js('o'), Js('ei'), Js('i'), Js('ae')]))
pass
pass
pass


# Add lib to the module scope
graeaeNames = var.to_python()
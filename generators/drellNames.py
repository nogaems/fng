__all__ = ['drellNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('nm1', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
    else:
        var.put('nm1', Js([Js('')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm2').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('')]))
var.put('nm2', Js([Js('ka'), Js('ki'), Js('ku'), Js('ke'), Js('ko'), Js('sa'), Js('si'), Js('su'), Js('se'), Js('so'), Js('sha'), Js('shi'), Js('shu'), Js('she'), Js('sho'), Js('ta'), Js('ti'), Js('tu'), Js('te'), Js('to'), Js('tha'), Js('thi'), Js('thu'), Js('the'), Js('tho'), Js('dra'), Js('dri'), Js('dru'), Js('dre'), Js('dro'), Js('ma'), Js('mi'), Js('mu'), Js('me'), Js('mo'), Js('na'), Js('ni'), Js('nu'), Js('ne'), Js('no'), Js('ha'), Js('hi'), Js('hu'), Js('he'), Js('ho'), Js('fa'), Js('fi'), Js('fu'), Js('fe'), Js('fo'), Js('ra'), Js('ri'), Js('ru'), Js('re'), Js('ro'), Js('la'), Js('li'), Js('lu'), Js('le'), Js('lo'), Js('ya'), Js('yi'), Js('yu'), Js('ye'), Js('yo')]))
var.put('nm3', Js([Js('n'), Js('l'), Js('t'), Js('k'), Js('s'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('ka'), Js('ki'), Js('ku'), Js('ke'), Js('ko'), Js('sa'), Js('si'), Js('su'), Js('se'), Js('so'), Js('ta'), Js('ti'), Js('tu'), Js('te'), Js('to'), Js('ma'), Js('mi'), Js('mu'), Js('me'), Js('mo'), Js('na'), Js('ni'), Js('nu'), Js('ne'), Js('no'), Js('ha'), Js('hi'), Js('hu'), Js('he'), Js('ho'), Js('fa'), Js('fi'), Js('fu'), Js('fe'), Js('fo'), Js('ra'), Js('ri'), Js('ru'), Js('re'), Js('ro'), Js('la'), Js('li'), Js('lu'), Js('le'), Js('lo'), Js('ya'), Js('yi'), Js('yu'), Js('ye'), Js('yo')]))
var.put('nm5', Js([Js('n'), Js('l'), Js('t'), Js('k'), Js('s'), Js('h'), Js('m'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm7', Js([Js('n'), Js('l'), Js('t'), Js('k'), Js('s')]))
pass
pass


# Add lib to the module scope
drellNames = var.to_python()
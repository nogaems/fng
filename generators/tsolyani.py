__all__ = ['tsolyani']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1c', 'nm1', 'nm4', 'nameGen', 'nm5', 'nm2c', 'nm3', 'nm2'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd17', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd18', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd19', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('lName', ((((((var.get('nm5').get(var.get('rnd19'))+var.get('nm1c').get(var.get('rnd10')))+var.get('nm2').get(var.get('rnd11')))+var.get('nm1').get(var.get('rnd12')))+var.get('nm3').get(var.get('rnd13')))+var.get('nm2').get(var.get('rnd14')))+var.get('nm4').get(var.get('rnd18'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)):
                    var.put('lName', (((((var.get('nm5').get(var.get('rnd19'))+var.get('nm1c').get(var.get('rnd10')))+var.get('nm2').get(var.get('rnd11')))+var.get('nm1').get(var.get('rnd12')))+var.get('nm3').get(var.get('rnd13')))+var.get('nm2').get(var.get('rnd14'))))
                else:
                    var.put('lName', (((((var.get('nm5').get(var.get('rnd19'))+var.get('nm2c').get(var.get('rnd11')))+var.get('nm1').get(var.get('rnd12')))+var.get('nm3').get(var.get('rnd13')))+var.get('nm2').get(var.get('rnd14')))+var.get('nm4').get(var.get('rnd18'))))
            if (var.get('i')<Js(2.0)):
                var.put('names', (((((var.get('nm2c').get(var.get('rnd2'))+var.get('nm1').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('names', ((((((var.get('nm2c').get(var.get('rnd2'))+var.get('nm1').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd9')))+Js(' '))+var.get('lName')))
                else:
                    if PyJsStrictEq(var.get('i'),Js(4.0)):
                        var.put('names', ((((((((var.get('nm2c').get(var.get('rnd2'))+var.get('nm1').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm1').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+Js(' '))+var.get('lName')))
                    else:
                        if PyJsStrictEq(var.get('i'),Js(5.0)):
                            var.put('names', ((((var.get('nm1c').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd9')))+Js(' '))+var.get('lName')))
                        else:
                            if PyJsStrictEq(var.get('i'),Js(6.0)):
                                var.put('names', ((((((var.get('nm1c').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm1').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                            else:
                                if PyJsStrictEq(var.get('i'),Js(7.0)):
                                    var.put('names', (((((((var.get('nm1c').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm1').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd9')))+Js(' '))+var.get('lName')))
                                else:
                                    if PyJsStrictEq(var.get('i'),Js(8.0)):
                                        var.put('names', (((((((((var.get('nm1c').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm1').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm1').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+Js(' '))+var.get('lName')))
                                    else:
                                        if PyJsStrictEq(var.get('i'),Js(9.0)):
                                            var.put('names', ((((((((((var.get('nm1c').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm1').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm1').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm4').get(var.get('rnd9')))+Js(' '))+var.get('lName')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js("'"), Js("'"), Js("'"), Js("'"), Js("'"), Js("'"), Js("'"), Js('b'), Js('ch'), Js('d'), Js('dh'), Js('f'), Js('g'), Js('gh'), Js('h'), Js('hl'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('ss'), Js('t'), Js('th'), Js('tl'), Js('ts'), Js('v'), Js('w'), Js('y'), Js('z'), Js('zh')]))
var.put('nm1c', Js([Js("'"), Js("'"), Js("'"), Js("'"), Js("'"), Js("'"), Js("'"), Js('B'), Js('Ch'), Js('D'), Js('Dh'), Js('F'), Js('G'), Js('Gh'), Js('H'), Js('Hl'), Js('K'), Js('Kh'), Js('L'), Js('M'), Js('N'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('Sh'), Js('Ss'), Js('T'), Js('Th'), Js('Tl'), Js('Ts'), Js('V'), Js('W'), Js('Y'), Js('Z'), Js('Zh')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('au'), Js('ai'), Js('ua'), Js('ue'), Js('ae'), Js('ai'), Js('oi')]))
var.put('nm2c', Js([Js('A'), Js('E'), Js('I'), Js('O'), Js('U'), Js('A'), Js('E'), Js('I'), Js('O'), Js('U'), Js('A'), Js('E'), Js('I'), Js('O'), Js('U'), Js('A'), Js('E'), Js('I'), Js('O'), Js('U'), Js('Y'), Js('A'), Js('E'), Js('I'), Js('O'), Js('U'), Js('A'), Js('E'), Js('I'), Js('O'), Js('U'), Js('A'), Js('E'), Js('O'), Js('I'), Js('U'), Js('Au'), Js('Ai'), Js('Ua'), Js('Ue'), Js('Ae'), Js('Ai'), Js('Oi')]))
var.put('nm3', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('l'), Js('m'), Js('n'), Js('ng'), Js('r'), Js('s'), Js('sh'), Js('ss'), Js('y')]))
var.put('nm4', Js([Js('hl'), Js('k'), Js('kh'), Js('l'), Js('l'), Js('l'), Js('l'), Js('l'), Js('l'), Js('l'), Js('m'), Js('n'), Js('m'), Js('n'), Js('m'), Js('n'), Js('m'), Js('n'), Js('ng'), Js('r'), Js('r'), Js('r'), Js('s'), Js('sh'), Js('tl')]))
var.put('nm5', Js([Js('hi'), Js('hi'), Js('hi'), Js('hi'), Js('hi'), Js('hi'), Js('hi'), Js('hi'), Js('dhu'), Js('vu')]))
pass
pass


# Add lib to the module scope
tsolyani = var.to_python()
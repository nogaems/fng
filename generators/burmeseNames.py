__all__ = ['burmeseNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm2').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm2').get(var.get('rnd3')))+Js(' '))+var.get('nm2').get(var.get('rnd4'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm1').get(var.get('rnd2'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm1').get(var.get('rnd2')))+Js(' '))+var.get('nm1').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm1').get(var.get('rnd2')))+Js(' '))+var.get('nm1').get(var.get('rnd3')))+Js(' '))+var.get('nm1').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('Aeindra'), Js('Ag'), Js('Aung'), Js('Aye'), Js('Cho'), Js('Ei'), Js('Eindra'), Js('Eka'), Js('Hayma'), Js('Haymar'), Js('Hlaing'), Js('Hline'), Js('Hnin'), Js('Hsu'), Js('Htay'), Js('Htet'), Js('Htun'), Js('Inzali'), Js('Kay'), Js('Khaing'), Js('Khin'), Js('Khine'), Js('Kyaw'), Js('Le'), Js('Marlar'), Js('May'), Js('Mon'), Js('Myat'), Js('Myint'), Js('Myitzu'), Js('Naing'), Js('Nanda'), Js('Nandar'), Js('New'), Js('Nhin'), Js('Nila'), Js('Nilar'), Js('Nine'), Js('Nway'), Js('Nwe'), Js('Ohmar'), Js('Ommar'), Js('Phone'), Js('Phyo'), Js('Phyu'), Js('Pwint'), Js('San'), Js('Sanda'), Js('Sandar'), Js('Su'), Js('Thanda'), Js('Thandar'), Js('Thawda'), Js('Thawdar'), Js('Thawka'), Js('Theingi'), Js('Thet'), Js('Thi'), Js('Thida'), Js('Thidar'), Js('Thin'), Js('Thinza'), Js('Thinzar'), Js('Thiri'), Js('Thu'), Js('Thuzar'), Js('Tun'), Js('U'), Js('Win'), Js('Yadana'), Js('Yadanar'), Js('Yati'), Js('Yee'), Js('Yi'), Js('Yin'), Js('Yu'), Js('Yuzana'), Js('Zar'), Js('Zaw'), Js('Zin')]))
var.put('nm1', Js([Js('Ag'), Js('Arkar'), Js('Aung'), Js('Bo'), Js('Hein'), Js('Htet'), Js('Htun'), Js('Htut'), Js('Kan'), Js('Kaung'), Js('Khaing'), Js('Khant'), Js('Khine'), Js('Ko'), Js('Kyaw'), Js('Lin'), Js('Linn'), Js('Maung'), Js('Mg'), Js('Min'), Js('Myat'), Js('Myint'), Js('Myo'), Js('Naing'), Js('Nyan'), Js('Phone'), Js('Phyo'), Js('Phyoe'), Js('Pyae'), Js('Pyay'), Js('Sein'), Js('Soe'), Js('Thant'), Js('Thawda'), Js('Thet'), Js('Thiha'), Js('Thu'), Js('Thura'), Js('Thurein'), Js('Thuta'), Js('Tun'), Js('U'), Js('Wai'), Js('Win'), Js('Wunna'), Js('Yarzar'), Js('Yaza'), Js('Ye'), Js('Zarni'), Js('Zaw'), Js('Zeya'), Js('Zeyar'), Js('Zin')]))
pass
pass


# Add lib to the module scope
burmeseNames = var.to_python()
__all__ = ['djinnNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                while PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd'))):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+Js(' the '))+var.get('nm16').get(var.get('rnd16'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm8').get(var.get('rnd3'))):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    if (var.get('i')<Js(8.0)):
                        var.put('names', ((((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd5')))+Js(' the '))+var.get('nm16').get(var.get('rnd16'))))
                    else:
                        var.put('names', ((((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+Js(' the '))+var.get('nm16').get(var.get('rnd16'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    while PyJsStrictEq(var.get('nm13').get(var.get('rnd3')),var.get('nm11').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    if (var.get('i')<Js(6.0)):
                        var.put('names', ((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd5')))+Js(' the '))+var.get('nm16').get(var.get('rnd16'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        while PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm13').get(var.get('rnd3'))):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm15').get(var.get('rnd5')))+Js(' the '))+var.get('nm16').get(var.get('rnd16'))))
                        else:
                            var.put('names', ((((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd5')))+Js(' the '))+var.get('nm16').get(var.get('rnd16'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    if (var.get('i')<Js(6.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' the '))+var.get('nm16').get(var.get('rnd16'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js(' the '))+var.get('nm16').get(var.get('rnd16'))))
                        else:
                            var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' the '))+var.get('nm16').get(var.get('rnd16'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('ee'), Js('ua'), Js('ai'), Js('oo')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('br'), Js('d'), Js('h'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('nq'), Js('q'), Js('s'), Js('sh'), Js('sm'), Js('ss'), Js('sf'), Js('st'), Js('t'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js('b'), Js('bb'), Js('d'), Js('h'), Js('k'), Js('m'), Js('n'), Js('r'), Js('rr'), Js('rh'), Js('s'), Js('sh'), Js('ss'), Js('z'), Js('zz')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('d'), Js('f'), Js('l'), Js('m'), Js('n'), Js('sh'), Js('z')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('g'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('w'), Js('y'), Js('z')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('i'), Js('aa'), Js('ee'), Js('ai'), Js('ia')]))
var.put('nm8', Js([Js('b'), Js('d'), Js('dh'), Js('dr'), Js('f'), Js('ff'), Js('l'), Js('ll'), Js('m'), Js('mn'), Js('r'), Js('s'), Js('sh'), Js('ss'), Js('t'), Js('th'), Js('w'), Js('y'), Js('z')]))
var.put('nm9', Js([Js('d'), Js('f'), Js('ff'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('s'), Js('ss'), Js('t'), Js('w'), Js('y'), Js('z')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('bh'), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('y'), Js('z')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('i'), Js('aa'), Js('ee'), Js('ai')]))
var.put('nm13', Js([Js('b'), Js('bb'), Js('d'), Js('h'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('rr'), Js('s'), Js('sh'), Js('ss'), Js('t'), Js('th'), Js('z'), Js('zz')]))
var.put('nm14', Js([Js('b'), Js('d'), Js('h'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('y'), Js('z'), Js('zz')]))
var.put('nm15', Js([Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('z')]))
var.put('nm16', Js([Js('Accomplished'), Js('Adored'), Js('Adventurous'), Js('Amazing'), Js('Ancient'), Js('Austere'), Js('Beloved'), Js('Better'), Js('Bold'), Js('Bountiful'), Js('Brilliant'), Js('Carefree'), Js('Courageous'), Js('Creative'), Js('Cruel'), Js('Daring'), Js('Devoted'), Js('Dreamy'), Js('Elegant'), Js('Enchanted'), Js('Enlightened'), Js('Exalted'), Js('Extravagant'), Js('Fair'), Js('Fantastic'), Js('Fearless'), Js('Fesity'), Js('First'), Js('Flawless'), Js('Fortunate'), Js('Friendly'), Js('Generous'), Js('Gentle'), Js('Gifted'), Js('Giving'), Js('Glamorous'), Js('Glorious'), Js('Gorgeous'), Js('Graceful'), Js('Gracious'), Js('Grand'), Js('Grandiose'), Js('Great'), Js('Handsome'), Js('Happy'), Js('Harmonious'), Js('Heavenly'), Js('Honest'), Js('Honored'), Js('Humble'), Js('Idolized'), Js('Illustrious'), Js('Impeccable'), Js('Incredible'), Js('Intrepid'), Js('Jolly'), Js('Joyful'), Js('Joyous'), Js('Kind'), Js('Kindhearted'), Js('Light'), Js('Lovable'), Js('Loyal'), Js('Lucky'), Js('Luminous'), Js('Lustrous'), Js('Luxurious'), Js('Magnificent'), Js('Majestic'), Js('Marvelous'), Js('Mighty'), Js('Mysterious'), Js('Original'), Js('Pleasant'), Js('Pleasing'), Js('Powerful'), Js('Precious'), Js('Proud'), Js('Pure'), Js('Radiant'), Js('Rewarding'), Js('Rich'), Js('Royal'), Js('Sane'), Js('Scented'), Js('Serene'), Js('Silent'), Js('Simple'), Js('Spectacular'), Js('Stunning'), Js('Superior'), Js('Swift'), Js('Tender'), Js('Terrific'), Js('Treasured'), Js('Tremendous'), Js('Trustworthy'), Js('Truthful'), Js('Unequaled'), Js('Venerated'), Js('Vibrant'), Js('Victorious'), Js('Virtuous'), Js('Wealthy'), Js('Wise'), Js('Wonderful')]))
pass
pass


# Add lib to the module scope
djinnNames = var.to_python()
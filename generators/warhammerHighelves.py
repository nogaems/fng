__all__ = ['warhammerHighelves']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('nameL', var.get('nm8').get(var.get('rnd')))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+Js(' the '))+var.get('nameL')))
                else:
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd8')))+Js(' the '))+var.get('nameL')))
            else:
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm').get('length'))))
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((((((var.get('nm').get(var.get('rnd0'))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' the '))+var.get('nameL')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((((((var.get('nm').get(var.get('rnd0'))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd5')))+Js(' the '))+var.get('nameL')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm', Js([Js('Bel-'), Js(''), Js(''), Js(''), Js('')]))
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('g'), Js('gh'), Js('h'), Js('k'), Js('m'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('e'), Js('e'), Js('o'), Js('o'), Js('ye'), Js('ae'), Js('io'), Js('ya'), Js('aa')]))
var.put('nm3', Js([Js('b'), Js('d'), Js('l'), Js('n'), Js('r'), Js('z'), Js('b'), Js('d'), Js('l'), Js('n'), Js('r'), Js('z'), Js('b'), Js('br'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('dh'), Js('gr'), Js('l'), Js('lv'), Js('lr'), Js('ln'), Js('ld'), Js('n'), Js('nd'), Js('nn'), Js('nt'), Js('nth'), Js('ntr'), Js('r'), Js('rh'), Js('rv'), Js('rt'), Js('rth'), Js('rd'), Js('rh'), Js('th'), Js('thl'), Js('z'), Js('zr')]))
var.put('nm4', Js([Js('c'), Js('l'), Js('n'), Js('r'), Js('s')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('d'), Js('f'), Js('h'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('o'), Js('o'), Js('ie'), Js('ia'), Js('ae'), Js('ye'), Js('ei')]))
var.put('nm7', Js([Js('c'), Js('d'), Js('f'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z'), Js('c'), Js('d'), Js('dh'), Js('dd'), Js('f'), Js('ff'), Js('fn'), Js('gh'), Js('h'), Js('hh'), Js('k'), Js('kh'), Js('l'), Js('ll'), Js('lr'), Js('lv'), Js('lm'), Js('ln'), Js('lf'), Js('lg'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('nn'), Js('nr'), Js('nv'), Js('r'), Js('rr'), Js('rh'), Js('rn'), Js('rl'), Js('s'), Js('sh'), Js('ss'), Js('t'), Js('tt'), Js('th'), Js('v'), Js('z'), Js('zz')]))
var.put('nm8', Js([Js('Academic'), Js('Acclaimed'), Js('Admired'), Js('Agile'), Js('Ancient'), Js('Angel'), Js('Angelic'), Js('Artist'), Js('Austere'), Js('Beast'), Js('Beautiful'), Js('Blessed'), Js('Bold'), Js('Brave'), Js('Brilliant'), Js('Celebrated'), Js('Clever'), Js('Composed'), Js('Conqueror'), Js('Defender'), Js('Defiant'), Js('Devoted'), Js('Diligent'), Js('Discrete'), Js('Earnest'), Js('Educated'), Js('Elegant'), Js('Enchanted'), Js('Enchanting'), Js('Enforcer'), Js('Enlightened'), Js('Exalted'), Js('Executioner'), Js('Expert'), Js('Explorer'), Js('Fearless'), Js('Flamboyant'), Js('Flawless'), Js('Generous'), Js('Gentle'), Js('Gifted'), Js('Giving'), Js('Glorious'), Js('Graceful'), Js('Grand'), Js('Great'), Js('Grim'), Js('Guardian'), Js('Honest'), Js('Honorable'), Js('Honored'), Js('Humble'), Js('Illustrious'), Js('Immortal'), Js('Impetuous'), Js('Incredible'), Js('Just'), Js('Learned'), Js('Light'), Js('Loremaster'), Js('Loyal'), Js('Magnificent'), Js('Majestic'), Js('Marvelous'), Js('Merciful'), Js('Mighty'), Js('Oracle'), Js('Paragon'), Js('Patient'), Js('Peacemaker'), Js('Pious'), Js('Pleasant'), Js('Poet'), Js('Powerful'), Js('Prime'), Js('Proud'), Js('Radiant'), Js('Sage'), Js('Seafarer'), Js('Serene'), Js('Silent'), Js('Slayer'), Js('Specialist'), Js('Stark'), Js('Stout'), Js('Strict'), Js('Swift'), Js('Valiant'), Js('Vengeful'), Js('Warrior'), Js('Wild'), Js('Wise')]))
pass
pass


# Add lib to the module scope
warhammerHighelves = var.to_python()
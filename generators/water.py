__all__ = ['water']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abysmal'), Js('Arching'), Js('Red'), Js('Black'), Js('White'), Js('Cursed'), Js('Frozen'), Js('Arctic'), Js('Barren'), Js('Billowy'), Js('Bland'), Js('Blue'), Js('Boiling'), Js('Boisterous'), Js('Bottomless'), Js('Boundless'), Js('Brilliant'), Js('Bursting'), Js('Calm'), Js('Calmest'), Js('Charmed'), Js('Cheerless'), Js('Choral'), Js('Circumfluous'), Js('Climbing'), Js('Cobalt'), Js('Cold'), Js('Coral'), Js('Crystal'), Js('Dancing'), Js('Dread'), Js('Dreaded'), Js('Dark'), Js('Darkest'), Js('Dead'), Js('Deep'), Js('Deepest'), Js('Delicious'), Js('Dense'), Js('Depraved'), Js('Distant'), Js('Eastern'), Js('Emerald'), Js('Empty'), Js('Enchanted'), Js('Ethereal'), Js('Ever Reaching'), Js('Fair'), Js('Farthest'), Js('Flat'), Js('Forbidden'), Js('Quiet'), Js('Flowing'), Js('Foaming'), Js('Frothy'), Js('Glassy'), Js('Gleaming'), Js('Glistening'), Js('Grave'), Js('Gray'), Js('Green'), Js('Harmonious'), Js('Heartless'), Js('Heaving'), Js('Homeless'), Js('Hungry'), Js('Infernal'), Js('Infinite'), Js('Invisible'), Js('Isolated'), Js('Jade'), Js('Laughing'), Js('Lifeless'), Js('Living'), Js('Lonely'), Js('Lucent'), Js('Majestic'), Js('Mesmerizing'), Js('Mighty'), Js('Misty'), Js('Moaning'), Js('Molten'), Js('Moon-lit'), Js('Motionless'), Js('Narrow'), Js('Neglected'), Js('Northern'), Js('Orient'), Js('Peaceful'), Js('Perfumed'), Js('Pleasant'), Js('Primeval'), Js('Raging'), Js('Rainy'), Js('Rippling'), Js('Rocking'), Js('Rolling'), Js('Rough'), Js('Rushing'), Js('Sandy'), Js('Sanguine'), Js('Savage'), Js('Serene'), Js('Shimmering'), Js('Shoaling'), Js('Shoreless'), Js('Sleeping'), Js('Slumbrous'), Js('Soundless'), Js('Southern'), Js('Spacious'), Js('Sparkling'), Js('Sterile'), Js('Stern'), Js('Straitened'), Js('Sunny'), Js('Surging'), Js('Teal'), Js('Terrestrial'), Js('Throbbing'), Js('Thundering'), Js('Tideless'), Js('Tinted'), Js('Tossing'), Js('Tranquil'), Js('Treacherous'), Js('Triumphant'), Js('Mirrored'), Js('Restless'), Js('Tropic'), Js('Troubled'), Js('Turbulent'), Js('Turquoise'), Js('Ugly'), Js('Ultramarine'), Js('Uncanny'), Js('Unfathomed'), Js('Unknown'), Js('Unresting'), Js('Unruffled'), Js('Unstable'), Js('Vast'), Js('Violent'), Js('Walled'), Js('Wasted'), Js('Wasteful'), Js('Wasting'), Js('Waveless'), Js('Western'), Js('Whelming'), Js('Whispering'), Js('Wild'), Js('Windy'), Js('Wondering'), Js('Wrinkled'), Js('Yearning')]))
var.put('nm2', Js([Js('Abyss'), Js('Tides'), Js('Waves'), Js('Bay'), Js('Deep'), Js('Depths'), Js('Domain'), Js('Expanse'), Js('Gulf'), Js('Ocean'), Js('Sea'), Js('Waters')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z'), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
water = var.to_python()
__all__ = ['swampNames']

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
            if (var.get('i')<Js(2.0)):
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd1')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd1'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd7')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abysmal'), Js('Alligator'), Js('Amazon'), Js('Ancient'), Js('Arching'), Js('Arrowhead'), Js('Bamboo'), Js('Barren'), Js('Billowy'), Js('Black'), Js('Bland'), Js('Blue'), Js('Bogbeast'), Js('Boiling'), Js('Boundless'), Js('Brown'), Js('Bursting'), Js('Calm'), Js('Calmest'), Js('Charmed'), Js('Cheerless'), Js('Clouded'), Js('Cobalt'), Js('Cold'), Js('Coral'), Js('Crocodile'), Js('Crystal'), Js('Cursed'), Js('Dancing'), Js('Dark'), Js('Darkest'), Js('Dead'), Js('Deep'), Js('Deepest'), Js('Dense'), Js('Depraved'), Js('Distant'), Js('Dragonfly'), Js('Dread'), Js('Dreaded'), Js('Drowning'), Js('Dying'), Js('Eastern'), Js('Emerald'), Js('Empty'), Js('Enchanted'), Js('Ethereal'), Js('Ever Reaching'), Js('Flat'), Js('Flowing'), Js('Foaming'), Js('Foggy'), Js('Forbidden'), Js('Frog'), Js('Frozen'), Js('Furthest'), Js('Gleaming'), Js('Glistening'), Js('Grave'), Js('Gray'), Js('Green'), Js('Harmonious'), Js('Harmony'), Js('Heartless'), Js('Heaving'), Js('Hidden'), Js('Homeless'), Js('Hungry'), Js('Infernal'), Js('Infested'), Js('Infinite'), Js('Invisible'), Js('Isolated'), Js('Jade'), Js('Laughing'), Js('Lifeless'), Js('Lilypad'), Js('Living'), Js('Lonely'), Js('Lotus'), Js('Lucent'), Js('Majestic'), Js('Mesmerizing'), Js('Mighty'), Js('Mirrored'), Js('Misty'), Js('Moaning'), Js('Molten'), Js('Moon-lit'), Js('Mosquito'), Js('Motionless'), Js('Moving'), Js('Mushy'), Js('Narrow'), Js('Neglected'), Js('New'), Js('Northern'), Js('Peaceful'), Js('Perfumed'), Js('Piranha'), Js('Pleasant'), Js('Primeval'), Js('Quiet'), Js('Raging'), Js('Rainy'), Js('Red'), Js('Restless'), Js('Rippling'), Js('Rocking'), Js('Rolling'), Js('Rough'), Js('Rushing'), Js('Sandy'), Js('Sanguine'), Js('Savage'), Js('Serene'), Js('Serpent'), Js('Shimmering'), Js('Silent'), Js('Sleeping'), Js('Slumbrous'), Js('Soundless'), Js('Southern'), Js('Spacious'), Js('Sparkling'), Js('Sterile'), Js('Sunny'), Js('Surging'), Js('Thundering'), Js('Tinted'), Js('Toad'), Js('Tortoise'), Js('Tossing'), Js('Toxic'), Js('Tranquil'), Js('Treacherous'), Js('Tropic'), Js('Troubled'), Js('Turbulent'), Js('Turquoise'), Js('Turtle'), Js('Uncanny'), Js('Unfathomed'), Js('Unknown'), Js('Unstable'), Js('Vast'), Js('Venom'), Js('Violent'), Js('Walled'), Js('Wasted'), Js('Wasteful'), Js('Western'), Js('Whispering'), Js('White'), Js('Wild'), Js('Willow'), Js('Windy'), Js('Wondering'), Js('Wrinkled'), Js('Yearning')]))
var.put('nm2', Js([Js('Abyss'), Js('Basin'), Js('Bog'), Js('Bowels'), Js('Cove'), Js('Glades'), Js('Labyrinth'), Js('Mangrove'), Js('Marsh'), Js('Mire'), Js('Morass'), Js('Polder'), Js('Quag'), Js('Quagmire'), Js('Slough'), Js('Swamp'), Js('Waters'), Js('Wetlands')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
swampNames = var.to_python()
__all__ = ['mgtKor']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    while PyJsStrictEq(var.get('nm7').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', (((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(', '))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nm9').get(var.get('rnd6'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', ((var.get('nm8').get(var.get('rnd'))+Js(' '))+var.get('nm9').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        while PyJsStrictEq(var.get('nm10').get(var.get('rnd')),var.get('nm11').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', (((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+Js(' '))+var.get('nm9').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd1')))+Js(', '))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nm9').get(var.get('rnd6'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', ((var.get('nm8').get(var.get('rnd'))+Js(' '))+var.get('nm9').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        while PyJsStrictEq(var.get('nm10').get(var.get('rnd')),var.get('nm11').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', (((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+Js(' '))+var.get('nm9').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('t'), Js('d'), Js('y'), Js('b'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('bh'), Js('d'), Js('dd'), Js('dh'), Js('lb'), Js('ld'), Js('lg'), Js('ln'), Js('md'), Js('ml'), Js('m'), Js('mm'), Js('n'), Js('nd'), Js('nn'), Js('ng'), Js('nk'), Js('nl'), Js('nm')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('l'), Js('n'), Js('r'), Js('y')]))
var.put('nm5', Js([Js('f'), Js('h'), Js('l'), Js('n'), Js('t'), Js('v'), Js('y')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i')]))
var.put('nm7', Js([Js('hn'), Js('hl'), Js('hm'), Js('l'), Js('lm'), Js('ln'), Js('ly'), Js('lf'), Js('ll'), Js('mn'), Js('m'), Js('mm'), Js('mh'), Js('my'), Js('mw'), Js('n'), Js('ny'), Js('nm'), Js('nh'), Js('nw'), Js('ph'), Js('phr'), Js('phl'), Js('sh'), Js('sl'), Js('sn'), Js('sm'), Js('st'), Js('th'), Js('thn'), Js('thl'), Js('thy'), Js('yl'), Js('yn')]))
var.put('nm8', Js([Js('Aged'), Js('Ambush'), Js('Ancient'), Js('Armament'), Js('Austere'), Js('Bold'), Js('Brilliant'), Js('Cruel'), Js('Defiant'), Js('Dependent'), Js('Devoted'), Js('Devout'), Js('Diligent'), Js('Discrete'), Js('Dutiful'), Js('Eager'), Js('Eternal'), Js('Exalted'), Js('Fearless'), Js('Feline'), Js('Forsaken'), Js('Ghostly'), Js('Gifted'), Js('Glorious'), Js('Grand'), Js('Great'), Js('Grim'), Js('Hollow'), Js('Honored'), Js('Illustrious'), Js('Intrepid'), Js('Juvenile'), Js('Kor'), Js('Lone'), Js('Lost'), Js('Loyal'), Js('Mellow'), Js('Minor'), Js('Monstrous'), Js('Nocturnal'), Js('Obedient'), Js('Outlandish'), Js('Powerful'), Js('Prime'), Js('Rapid'), Js('Reckless'), Js('Relief'), Js('Rigid'), Js('Selfish'), Js('Shadow'), Js('Shadowy'), Js('Shady'), Js('Silent'), Js('Sneaky'), Js('Sniveling'), Js('Somber'), Js('Spirited'), Js('Swift'), Js('Vengeful'), Js('Vicious'), Js('Vigilant'), Js('Violent'), Js('Wicked'), Js('Wild'), Js('Wrathful'), Js('Wretched')]))
var.put('nm9', Js([Js('Aeronaut'), Js('Apprentice'), Js('Artisan'), Js('Augur'), Js('Blademaster'), Js('Brawler'), Js('Bruiser'), Js('Burglar'), Js('Captain'), Js('Champion'), Js('Cleric'), Js('Commander'), Js('Dancer'), Js('Diviner'), Js('Duelist'), Js('Enchanter'), Js('Explorer'), Js('Fighter'), Js('Firewalker'), Js('Glider'), Js('Guard'), Js('Guardian'), Js('Guide'), Js('Harbinger'), Js('Herald'), Js('Hero'), Js('Hookmaster'), Js('Infiltrator'), Js('Leader'), Js('Lookout'), Js('Medic'), Js('Mercenary'), Js('Missionary'), Js('Mole'), Js('Mystic'), Js('Navigator'), Js('Neophyte'), Js('Oracle'), Js('Outfitter'), Js('Pilgrim'), Js('Protector'), Js('Prowler'), Js('Ringleader'), Js('Sage'), Js('Sanctifier'), Js('Scout'), Js('Scythemaster'), Js('Sear'), Js('Seer'), Js('Sentinel'), Js('Shieldmate'), Js('Soothsayer'), Js('Specialist'), Js('Spiritdancer'), Js('Spy'), Js('Tender'), Js('Thief'), Js('Vanguard'), Js('Wanderer'), Js('Warrior'), Js('Watcher'), Js('Wildcat')]))
var.put('nm10', Js([Js('alder'), Js('amber'), Js('barren'), Js('bitter'), Js('boulder'), Js('cinder'), Js('coven'), Js('crest'), Js('dark'), Js('dawn'), Js('deep'), Js('dew'), Js('down'), Js('dream'), Js('dusk'), Js('elm'), Js('ember'), Js('fall'), Js('farrow'), Js('fist'), Js('flame'), Js('flint'), Js('fore'), Js('free'), Js('frost'), Js('gloom'), Js('grand'), Js('gray'), Js('great'), Js('hard'), Js('haven'), Js('high'), Js('keen'), Js('kind'), Js('light'), Js('lone'), Js('long'), Js('meadow'), Js('mirth'), Js('mist'), Js('moon'), Js('mourn'), Js('night'), Js('plain'), Js('pride'), Js('proud'), Js('rapid'), Js('regal'), Js('river'), Js('rough'), Js('shade'), Js('shadow'), Js('silent'), Js('silken'), Js('silver'), Js('simple'), Js('single'), Js('solid'), Js('soul'), Js('spring'), Js('stern'), Js('stone'), Js('storm'), Js('tall'), Js('thunder'), Js('vine'), Js('water'), Js('whit'), Js('wild')]))
var.put('nm11', Js([Js('bane'), Js('beam'), Js('bend'), Js('blaze'), Js('bluff'), Js('bough'), Js('bound'), Js('brace'), Js('branch'), Js('brand'), Js('breeze'), Js('brook'), Js('brooke'), Js('brow'), Js('call'), Js('copse'), Js('crag'), Js('crest'), Js('dane'), Js('down'), Js('fall'), Js('fist'), Js('flaw'), Js('flow'), Js('force'), Js('forge'), Js('fury'), Js('gaze'), Js('glade'), Js('glare'), Js('grove'), Js('guard'), Js('heart'), Js('helm'), Js('husk'), Js('keep'), Js('lance'), Js('lash'), Js('lock'), Js('mane'), Js('mantle'), Js('mark'), Js('more'), Js('mourne'), Js('ridge'), Js('root'), Js('run'), Js('shade'), Js('shard'), Js('shot'), Js('soar'), Js('song'), Js('spine'), Js('spire'), Js('stalk'), Js('stand'), Js('stride'), Js('surge'), Js('sworn'), Js('thorn'), Js('thorne'), Js('track'), Js('vale')]))
pass
pass


# Add lib to the module scope
mgtKor = var.to_python()
__all__ = ['mgtMerfolk']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('lName', ((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd3'))))
            else:
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('lName', ((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+var.get('nm12').get(var.get('rnd3'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('lName')))
                    else:
                        while PyJsStrictEq(var.get('nm7').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd'))):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', (((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        while PyJsStrictEq(var.get('nm13').get(var.get('rnd')),var.get('nm14').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('names', (((var.get('nm13').get(var.get('rnd'))+var.get('nm14').get(var.get('rnd2')))+Js(' '))+var.get('nm15').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                        var.put('names', ((var.get('nm15').get(var.get('rnd'))+Js(' '))+var.get('nm16').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        while PyJsStrictEq(var.get('nm3').get(var.get('rnd4')),var.get('nm1').get(var.get('rnd'))):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd3')))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        while PyJsStrictEq(var.get('nm13').get(var.get('rnd')),var.get('nm14').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('names', (((var.get('nm13').get(var.get('rnd'))+var.get('nm14').get(var.get('rnd2')))+Js(' '))+var.get('nm15').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                        var.put('names', ((var.get('nm15').get(var.get('rnd'))+Js(' '))+var.get('nm16').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('d'), Js('g'), Js('j'), Js('n'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('dd'), Js('dr'), Js('fr'), Js('fl'), Js('l'), Js('ll'), Js('lr'), Js('ln'), Js('n'), Js('nn'), Js('nd'), Js('r'), Js('rd'), Js('rz'), Js('rs'), Js('rv'), Js('t'), Js('tt'), Js('tr'), Js('y'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js('d'), Js('g'), Js('gg'), Js('l'), Js('n'), Js('nd'), Js('ng'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('t'), Js('th')]))
var.put('nm6', Js([Js('a'), Js('a'), Js('i'), Js('o'), Js('o'), Js('u')]))
var.put('nm7', Js([Js('d'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm8', Js([Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('y')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('a'), Js('e'), Js('a'), Js('e'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u')]))
var.put('nm11', Js([Js('d'), Js('dd'), Js('g'), Js('gg'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('t'), Js('tt'), Js('z'), Js('zz')]))
var.put('nm12', Js([Js('c'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r')]))
var.put('nm13', Js([Js('azure'), Js('blue'), Js('bright'), Js('clear'), Js('cloud'), Js('coral'), Js('coven'), Js('crystal'), Js('deep'), Js('depth'), Js('down'), Js('dream'), Js('fallow'), Js('fore'), Js('grand'), Js('gravel'), Js('haze'), Js('ink'), Js('keen'), Js('light'), Js('low'), Js('mellow'), Js('mer'), Js('mild'), Js('moon'), Js('night'), Js('ocean'), Js('orb'), Js('pale'), Js('prism'), Js('pure'), Js('razor'), Js('rip '), Js('root'), Js('rough'), Js('sand'), Js('sea'), Js('shadow'), Js('shore'), Js('silver'), Js('soft'), Js('star'), Js('storm'), Js('strong'), Js('surge'), Js('swift'), Js('tidal'), Js('tide'), Js('void'), Js('wake'), Js('wander'), Js('water'), Js('wave'), Js('well'), Js('whit'), Js('wild'), Js('wind')]))
var.put('nm14', Js([Js('bar'), Js('bend'), Js('bender'), Js('bind'), Js('binder'), Js('bough'), Js('bow'), Js('brand'), Js('breath'), Js('breeze'), Js('brine'), Js('brook'), Js('brooke'), Js('brow'), Js('caller'), Js('channel'), Js('crag'), Js('crash'), Js('creek'), Js('crest'), Js('dancer'), Js('dew'), Js('dream'), Js('dreamer'), Js('fallow'), Js('fathom'), Js('fin'), Js('flow'), Js('front'), Js('gabber'), Js('gill'), Js('glade'), Js('glide'), Js('helm'), Js('line'), Js('might'), Js('more'), Js('rider'), Js('ridge'), Js('river'), Js('sage'), Js('scape'), Js('seeker'), Js('shaper'), Js('shard'), Js('shine'), Js('sigh'), Js('singer'), Js('soar'), Js('spanner'), Js('spout'), Js('stand'), Js('stream'), Js('surge'), Js('sworn'), Js('tail'), Js('tide'), Js('trapper'), Js('tread'), Js('vigor'), Js('wake'), Js('ward'), Js('water'), Js('weaver'), Js('wine')]))
var.put('nm15', Js([Js('Adept'), Js('Ambassador'), Js('Angler'), Js('Apothecary'), Js('Assassin'), Js('Bouncer'), Js('Commander'), Js('Disciple'), Js('Diver'), Js('Douser'), Js('Drowner'), Js('Elite'), Js('Entangler'), Js('Explorer'), Js('Fighter'), Js('Fluxmage'), Js('Guard'), Js('Guardian'), Js('Guide'), Js('Harbinger'), Js('Hero'), Js('Hunter'), Js('Hypnotist'), Js('Illusionist'), Js('Infiltrator'), Js('Knight'), Js('Legate'), Js('Mage'), Js('Mentor'), Js('Merchant'), Js('Merfolk'), Js('Mesmerist'), Js('Mystic'), Js('Patrol'), Js('Pilferer'), Js('Priest'), Js('Prophet'), Js('Raider'), Js('Rider'), Js('Sage'), Js('Scout'), Js('Scryer'), Js('Seer'), Js('Selkie'), Js('Sentinel'), Js('Shaman'), Js('Spy'), Js('Stalker'), Js('Summoner'), Js('Thief'), Js('Tracker'), Js('Trader'), Js('Trapper'), Js('Trasher'), Js('Triton'), Js('Visionary'), Js('Warrior'), Js('Watch'), Js('Weaver')]))
var.put('nm16', Js([Js('Abyss'), Js('Abyssal'), Js('Agile'), Js('Arctic'), Js('Atoll'), Js('Azure'), Js('Barrier'), Js('Basin'), Js('Bay'), Js('Brave'), Js('Buoyant'), Js('Cape'), Js('Careful'), Js('Careless'), Js('Coral'), Js('Coven'), Js('Darting'), Js('Defiant'), Js('Depth'), Js('Diligent'), Js('Diving'), Js('Enclave'), Js('Energetic'), Js('Esteemed'), Js('Exalted'), Js('Expanse'), Js('Experienced'), Js('Fearless'), Js('Gifted'), Js('Glorious'), Js('Grand'), Js('Gulf'), Js('Harbor'), Js('Hasty'), Js('Intrepid'), Js('Jolting'), Js('Juvenile'), Js('Keen'), Js('Lagoon'), Js('Marine'), Js('Maritime'), Js('Nautical'), Js('Nimble'), Js('Oceanic'), Js('Prime'), Js('Prism'), Js('Radiant'), Js('Reckless'), Js('Reef'), Js('Salty'), Js('Shore'), Js('Slippery'), Js('Stark'), Js('Storm'), Js('Surf'), Js('Surfing'), Js('Surge'), Js('Swift'), Js('Tidal'), Js('Tide'), Js('Turbulent'), Js('Vicious'), Js('Vigilant'), Js('Void'), Js('Wake'), Js('Wave'), Js('Webbed'), Js('Wharf'), Js('Whirlpool'), Js('Wild'), Js('Zealous')]))
pass
pass


# Add lib to the module scope
mgtMerfolk = var.to_python()
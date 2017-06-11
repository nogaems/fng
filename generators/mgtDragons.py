__all__ = ['mgtDragons']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm10').get(var.get('rnd')),var.get('nm11').get(var.get('rnd2'))):
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                var.put('lName', (((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+Js(' '))+var.get('nm12').get(var.get('rnd3'))))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                var.put('lName', ((var.get('nm13').get(var.get('rnd'))+Js(' '))+var.get('nm12').get(var.get('rnd2'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd'))):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', (((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+Js(', '))+var.get('lName')))
                    else:
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd5')),var.get('nm8').get(var.get('rnd3'))):
                            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        var.put('names', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6')))+Js(', '))+var.get('lName')))
                else:
                    var.put('names', var.get('lName'))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm5').get(var.get('rnd5'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
                else:
                    var.put('names', var.get('lName'))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('cr'), Js('d'), Js('dr'), Js('j'), Js('k'), Js('kr'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('sk'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('uu'), Js('ae'), Js('au')]))
var.put('nm3', Js([Js('c'), Js('g'), Js('k'), Js('l'), Js('ll'), Js('lt'), Js('ld'), Js('m'), Js('mn'), Js('n'), Js('nn'), Js('nd'), Js('nt'), Js('r'), Js('rt'), Js('rk'), Js('rd'), Js('th'), Js('s'), Js('sh'), Js('v'), Js('z')]))
var.put('nm4', Js([Js('ct'), Js('d'), Js('dr'), Js('dg'), Js('g'), Js('gr'), Js('gd'), Js('gh'), Js('kt'), Js('kd'), Js('ld'), Js('lg'), Js('lt'), Js('lgr'), Js('lk'), Js('mg'), Js('mk'), Js('r'), Js('rg'), Js('rk'), Js('rd'), Js('sk'), Js('sg')]))
var.put('nm5', Js([Js('b'), Js('n'), Js('r'), Js('s'), Js('ss'), Js('ssh'), Js('t'), Js('th'), Js('x'), Js('z')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('dr'), Js('g'), Js('k'), Js('kh'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th'), Js('tr'), Js('y')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ei'), Js('ai'), Js('ae')]))
var.put('nm8', Js([Js('d'), Js('g'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm9', Js([Js('c'), Js('d'), Js('dr'), Js('g'), Js('gn'), Js('gr'), Js('k'), Js('kl'), Js('kr'), Js('r'), Js('rr'), Js('rk'), Js('rt'), Js('s'), Js('ss'), Js('sh'), Js('t'), Js('th')]))
var.put('nm10', Js([Js('amber'), Js('arcane'), Js('ash'), Js('ashen'), Js('bale'), Js('battle'), Js('bell'), Js('blade'), Js('blaze'), Js('bolt'), Js('breeze'), Js('bright'), Js('burning'), Js('cinder'), Js('crystal'), Js('dark'), Js('dawn'), Js('death'), Js('doom'), Js('dream'), Js('ember'), Js('ever'), Js('fire'), Js('flame'), Js('forge'), Js('fury'), Js('fuse'), Js('gore'), Js('grand'), Js('haze'), Js('hell'), Js('high'), Js('hollow'), Js('ice'), Js('light'), Js('lightning'), Js('lone'), Js('molten'), Js('mourn'), Js('necro'), Js('night'), Js('prey'), Js('pyre'), Js('rage'), Js('rime'), Js('rune'), Js('saur'), Js('shadow'), Js('shield'), Js('shock'), Js('silent'), Js('storm'), Js('sun'), Js('thunder'), Js('titan'), Js('twilight'), Js('vent'), Js('void'), Js('war'), Js('ward'), Js('wild')]))
var.put('nm11', Js([Js('bane'), Js('bellow'), Js('belly'), Js('bend'), Js('binder'), Js('blaze'), Js('blight'), Js('born'), Js('bough'), Js('brand'), Js('break'), Js('breaker'), Js('breath'), Js('bringer'), Js('brow'), Js('burn'), Js('burner'), Js('chewer'), Js('claw'), Js('crest'), Js('crown'), Js('crusher'), Js('dancer'), Js('draft'), Js('drift'), Js('drifter'), Js('fall'), Js('fang'), Js('fire'), Js('flame'), Js('flare'), Js('flow'), Js('force'), Js('forge'), Js('fury'), Js('glade'), Js('glide'), Js('grip'), Js('heart'), Js('hide'), Js('horn'), Js('kite'), Js('lash'), Js('mane'), Js('master'), Js('maw'), Js('more'), Js('mourn'), Js('rage'), Js('reaver'), Js('roar'), Js('scale'), Js('scales'), Js('scar'), Js('scorch'), Js('seizer'), Js('shadow'), Js('shard'), Js('shield'), Js('slayer'), Js('soar'), Js('spark'), Js('spine'), Js('spire'), Js('stalk'), Js('steel'), Js('stoker'), Js('storm'), Js('surge'), Js('sworn'), Js('talon'), Js('toll'), Js('ward'), Js('wing')]))
var.put('nm12', Js([Js('Behemoth'), Js('Brood'), Js('Charger'), Js('Despot'), Js('Dragon'), Js('Dragon'), Js('Dragon'), Js('Dragon'), Js('Dragon'), Js('Dragon'), Js('Dragon'), Js('Dragonlord'), Js('Dragonlord'), Js('Dragonlord'), Js('Dragonlord'), Js('Guardian'), Js('Heir'), Js('Hunter'), Js('Igniter'), Js('Marauder'), Js('Oppressor'), Js('Pillager'), Js('Predator'), Js('Raider'), Js('Ravager'), Js('Regent'), Js('Scion'), Js('Scourge'), Js('Sentinel'), Js('Sentry'), Js('Skyraider'), Js('Sovereign'), Js('Stalker'), Js('Titan'), Js('Tormentor'), Js('Tyrant'), Js('Warmonger'), Js('Worldgorger')]))
var.put('nm13', Js([Js('Aged'), Js('Agile'), Js('Alabaster'), Js('Anchored'), Js('Ancient'), Js('Belated'), Js('Bitter'), Js('Blight'), Js('Blind'), Js('Bold'), Js('Brimstone'), Js('Broken'), Js('Bronze'), Js('Bruised'), Js('Canopy'), Js('Careless'), Js('Catacomb'), Js('Clockwork'), Js('Cloud'), Js('Colossal'), Js('Corrupt'), Js('Corrupted'), Js('Covetous'), Js('Crimson'), Js('Crooked'), Js('Cruel'), Js('Crypt'), Js('Crystal'), Js('Cunning'), Js('Deafening'), Js('Defiant'), Js('Delirious'), Js('Diligent'), Js('Dream'), Js('Dreary'), Js('Drifting'), Js('Elated'), Js('Elder'), Js('Enchanted'), Js('Enduring'), Js('Enraged'), Js('Eternal'), Js('Exalted'), Js('Fearless'), Js('Fickle'), Js('Fire'), Js('Flame'), Js('Fog'), Js('Forge'), Js('Forsaken'), Js('Furnace'), Js('Fury'), Js('Gargantuan'), Js('Giant'), Js('Gigantic'), Js('Glorious'), Js('Grand'), Js('Grave'), Js('Grim'), Js('Grounded'), Js('Grumpy'), Js('Hateful'), Js('Heavenly'), Js('Hell'), Js('Hollow'), Js('Honored'), Js('Humongous'), Js('Hypersonic'), Js('Infernal'), Js('Inferno'), Js('Infinity'), Js('Iron'), Js('Juvenile'), Js('Light'), Js('Lightning'), Js('Lone'), Js('Lost'), Js('Lunar'), Js('Mad'), Js('Majestic'), Js('Mist'), Js('Moon'), Js('Mysterious'), Js('Nocturnal'), Js('Obedient'), Js('Phantasmal'), Js('Powerful'), Js('Predator'), Js('Primal'), Js('Prime'), Js('Pristine'), Js('Proud'), Js('Quick'), Js('Quicksilver'), Js('Radiant'), Js('Rapid'), Js('Reckless'), Js('Ruthless'), Js('Sadistic'), Js('Sanguine'), Js('Savage'), Js('Scornful'), Js('Selfish'), Js('Shady'), Js('Siege'), Js('Silent'), Js('Silver'), Js('Snarling'), Js('Solar'), Js('Spellbound'), Js('Spiteful'), Js('Stark'), Js('Steel'), Js('Storm'), Js('Sun'), Js('Supersonic'), Js('Swift'), Js('Thunder'), Js('Thunderous'), Js('Tomb'), Js('Turbulent'), Js('Twin'), Js('Vain'), Js('Venerated'), Js('Vengeful'), Js('Vicious'), Js('Villainous'), Js('Violent'), Js('Volcanic'), Js('Whirlwind'), Js('Wicked'), Js('Wild'), Js('Wrathful')]))
pass
pass


# Add lib to the module scope
mgtDragons = var.to_python()
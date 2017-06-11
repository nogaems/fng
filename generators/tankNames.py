__all__ = ['tankNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm5', 'nameGen', 'nm3', 'nm4', 'nm6'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Achilles'), Js('Aegis'), Js('Alaric'), Js('Ancestor'), Js('Anteater'), Js('Apache'), Js('Arbiter'), Js('Arist'), Js('Aristodemus'), Js('Armadillo'), Js('Arminius'), Js('Attila'), Js('Aurora'), Js('Authority'), Js('Awe'), Js('Badger'), Js('Bandit'), Js('Bane'), Js('Barrage'), Js('Basil'), Js('Basilisk'), Js('Basin'), Js('Battlemaster'), Js('Beast'), Js('Beelzebub'), Js('Beetle'), Js('Behemoth'), Js('Bigwig'), Js('Bison'), Js('Black Knight'), Js('Blitz'), Js('Blizzard'), Js('Bloodlust'), Js('Brass'), Js('Brass Knuckle'), Js('Buffalo'), Js('Bull'), Js('Bulldozer'), Js('Bulwark'), Js('Buster'), Js('Butcher'), Js('Buttress'), Js('Caesar'), Js('Centaur'), Js('Centurion'), Js('Challenger'), Js('Chaos'), Js('Chaperon'), Js('Citadel'), Js('Colossus'), Js('Comanche'), Js('Comet'), Js('Commander'), Js('Commando'), Js('Courage'), Js('Covenant'), Js('Coyote'), Js('Creator'), Js('Creature'), Js('Cruiser'), Js('Crusher'), Js('Crux'), Js('Cthulu'), Js('Curator'), Js('Custodian'), Js('Cyclone'), Js('Cyclops'), Js('Czar'), Js('Daemon'), Js('Dawn'), Js('Deluge'), Js('Demon'), Js('Deputy'), Js('Devil'), Js('Diablo'), Js('Djinn'), Js('Dragon'), Js('Dragoon'), Js('Drake'), Js('Dread'), Js('Duster'), Js('Ecstasy'), Js('Elephant'), Js('Emperor'), Js('Eternal'), Js('Fortress'), Js('Furor'), Js('Fury'), Js('Gargantua'), Js('Gargoyle'), Js('Genesis'), Js('Genghis'), Js('Gladiator'), Js('Glutton'), Js('Goliath'), Js('Governor'), Js('Guardian'), Js('Gurkha'), Js('Hades'), Js('Hammerhead'), Js('Hannibal'), Js('Harvester'), Js('Hellhound'), Js('Hellion'), Js('Herald'), Js('Hippo'), Js('Hog'), Js('Horatius'), Js('Hydra'), Js('Immortal'), Js('Impaler'), Js('Impulse'), Js('Infernal'), Js('Inferno'), Js('Infidel'), Js('Judge'), Js('Judgement'), Js('Julius'), Js('Justice'), Js('Kaiser'), Js('Khan'), Js('Legion'), Js('Leonidas'), Js('Leopard'), Js('Liberty'), Js('Lionheart'), Js('Lucifer'), Js('Lurker'), Js('Lynx'), Js('Maharajah'), Js('Mamluk'), Js('Mammoth'), Js('Maori'), Js('Mastadon'), Js('Matador'), Js('Matriarch'), Js('Maverick'), Js('Meteor'), Js('Miltiades'), Js('Minotaur'), Js('Misery'), Js('Miyamoto'), Js('Mogul'), Js('Monarch'), Js('Mongrel'), Js('Musashi'), Js('Myriad'), Js('Napoleon'), Js('Nightmare'), Js('Overlord'), Js('Overseer'), Js('Paladin'), Js('Panther'), Js('Paragon'), Js('Patriarch'), Js('Patriot'), Js('Perseverance'), Js('Phantom'), Js('Primal'), Js('Prime'), Js('Primus'), Js('Pyrrhus'), Js('Quake'), Js('Reaper'), Js('Requiem'), Js('Rhino'), Js('Samurai'), Js('Savage'), Js('Scipio'), Js('Scorpion'), Js('Scoundrel'), Js('Scourge'), Js('Scythe'), Js('Seism'), Js('Sentinel'), Js('Shepherd'), Js('Shockwave'), Js('Slayer'), Js('Spartacus'), Js('Spartan'), Js('Spirit'), Js('Spitfire'), Js('Stallion'), Js('Stark'), Js('Steward'), Js('Storm'), Js('Sultan'), Js('Sun Tzu'), Js('Sundry'), Js('Tarragon'), Js('Tempest'), Js('Templar'), Js('Terror'), Js('Thor'), Js('Thunder'), Js('Thunderclap'), Js('Thunderstrike'), Js('Titan'), Js('Titanium'), Js('Torment'), Js('Tornado'), Js('Tremor'), Js('Trooper'), Js('Tusker'), Js('Typhoon'), Js('Vercingetorix'), Js('Viking'), Js('Viper'), Js('Visigoth'), Js('Volcano'), Js('Wallace'), Js('Warden'), Js('White Knight'), Js('Widowmaker'), Js('Wyvern'), Js('Xiahou'), Js('Zephyr')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('rnd4')<Js(10.0)):
                while (var.get('rnd5')<Js(10.0)):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', ((((((var.get('nm4').get(var.get('rnd3'))+var.get('nm3').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+Js(' '))+var.get('nm1').get(var.get('rnd'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm3', Js([Js('-'), Js('-'), Js('-'), Js('-'), Js('-'), Js('-'), Js('-'), Js('-'), Js('-'), Js('-'), Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js('0')]))
var.put('nm4', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z')]))
var.put('nm5', Js([Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js('0')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js('0')]))
pass
pass


# Add lib to the module scope
tankNames = var.to_python()
__all__ = ['militaryVehicles']

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
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Aegis'), Js('Amazon'), Js('Arachnid'), Js('Arbiter'), Js('Armadillo'), Js('Atilla'), Js('Augury'), Js('Aurora'), Js('Badger'), Js('Bane'), Js('Bargaining Chip'), Js('Barrage'), Js('Basilisk'), Js('Bayonet'), Js('Beast'), Js('Behemoth'), Js('Bigwig'), Js('Bison'), Js('Black Knight'), Js('Blitz'), Js('Blizzard'), Js('Boar'), Js('Bolide'), Js('Bolt'), Js('Bouncer'), Js('Bronco'), Js('Buffalo'), Js('Buffer'), Js('Bulldozer'), Js('Bulwark'), Js('Buttress'), Js('Canine'), Js('Cavalier'), Js('Centurion'), Js('Cerberus'), Js('Challenger'), Js('Chaperon'), Js('Chelonian'), Js('Chief'), Js('Chieftain'), Js('Citadel'), Js('Cobra'), Js('Colossus'), Js('Colt'), Js('Comet'), Js('Commander'), Js('Commando'), Js('Cooter'), Js('Covenant'), Js('Coyote'), Js('Croc'), Js('Cruiser'), Js('Cthulu'), Js('Curator'), Js('Custodian'), Js('Cyclone'), Js('Cyclops'), Js('Czar'), Js('Dawn'), Js('Deputy'), Js('Devil'), Js('Diablo'), Js('Dire'), Js('Dire Wolf'), Js('Dirge'), Js('Djinn'), Js('Doom'), Js('Dragon'), Js('Drake'), Js('Dread'), Js('Duster'), Js('Edge'), Js('Elephant'), Js('Emperor'), Js('Enigma'), Js('Feline'), Js('Fiend'), Js('Fortress'), Js('Fox'), Js('Furor'), Js('Fury'), Js('Gargantua'), Js('Gargoyle'), Js('Gauntlet'), Js('Genesis'), Js('Genghis'), Js('Gloom'), Js('Glutton'), Js('Goliath'), Js('Gopher'), Js('Governor'), Js('Grimace'), Js('Grizzly'), Js('Guardian'), Js('Guerilla'), Js('Hades'), Js('Harmattan'), Js('Harvester'), Js('Hedgehog'), Js('Heimlich'), Js('Hellhound'), Js('Hellion'), Js('Herald'), Js('Hercules'), Js('Honcho'), Js('Honey Badger'), Js('Horror'), Js('Horus'), Js('Hun'), Js('Hurricane'), Js('Hydra'), Js('Hyena'), Js('Hymn'), Js('Ibis'), Js('Imp'), Js('Inferno'), Js('Jackal'), Js('Jaguar'), Js('Judge'), Js('Judgement'), Js('Kaiser'), Js('Khamsin'), Js('Khan'), Js('King Crab'), Js('Knave'), Js('Knight'), Js('Lament'), Js('Leatherback'), Js('Leonidas'), Js('Leopard'), Js('Leviathan'), Js('Lightning Bolt'), Js('Lucifer'), Js('Magister'), Js('Maharajah'), Js('Mammoth'), Js('Marshal'), Js('Mastodon'), Js('Matador'), Js('Maverick'), Js('Meteor'), Js('Minion'), Js('Mogul'), Js('Mollusk'), Js('Monarch'), Js('Mongrel'), Js('Mug'), Js('Mule'), Js('Mutt'), Js('Ogre'), Js('Oracle'), Js('Outcast'), Js('Overlord'), Js('Overseer'), Js('Paladin'), Js('Pangolin'), Js('Panther'), Js('Paradox'), Js('Paragon'), Js('Parapet'), Js('Patron'), Js('Porcupine'), Js('Prime'), Js('Primus'), Js('Pulse'), Js('Purgatory'), Js('Rajah'), Js('Rampart'), Js('Rascal'), Js('Rattlesnake'), Js('Requiem'), Js('Rex'), Js('Rhino'), Js('Rogue'), Js('Ruffian'), Js('Samaritan'), Js('Samson'), Js('Samurai'), Js('Savage'), Js('Scalawag'), Js('Scallion'), Js('Scimitar'), Js('Scorpion'), Js('Scoundrel'), Js('Scourge'), Js('Scythe'), Js('Sentinel'), Js('Serpent'), Js('Shaitan'), Js('Shepherd'), Js('Sherpa'), Js('Shooting Star'), Js('Sickle'), Js('Siren'), Js('Sirocco'), Js('Skunk'), Js('Smirk'), Js('Snapper'), Js('Spartan'), Js('Sphinx'), Js('Spitfire'), Js('Stallion'), Js('Stark'), Js('Steward'), Js('Storm'), Js('Striker'), Js('Sultan'), Js('Swine'), Js('Tarantula'), Js('Tarragon'), Js('Tempest'), Js('Templar'), Js('Terror'), Js('Thor'), Js('Thunder'), Js('Tigress'), Js('Titan'), Js('Torment'), Js('Tormentor'), Js('Tornado'), Js('Tortoise'), Js('Trooper'), Js('Tusker'), Js('Tycoon'), Js('Typhoon'), Js('Tyrant'), Js('Valkyrie'), Js('Vallation'), Js('Varlet'), Js('Viking'), Js('Viper'), Js('Virago'), Js('Visage'), Js('Vixen'), Js('Vulture'), Js('Warden'), Js('White Knight'), Js('Wolfhound'), Js('Wyvern')]))
    var.put('nm2', Js([Js('Amphibious Vehicle'), Js('Anti-Tank Vehicle'), Js('Armored Car'), Js('Armored Personal Carrier'), Js('Armored Security Vehicle'), Js('Armored Utility Vehicle'), Js('Armored Vehicle'), Js('Artillery Command Vehicle'), Js('Artillery Tractor'), Js('Bridging Vehicle'), Js('Cargo Carrier'), Js('Carrier'), Js('Command Vehicle'), Js('Engineering Vehicle'), Js('Fire Support Vehicle'), Js('Infantry Fighting Vehicle'), Js('Launcher'), Js('Maintenance and Recovery Vehicle'), Js('Mine Clearing Vehicle'), Js('Personal Carrier'), Js('Reconnaissance Vehicle'), Js('Recovery Vehicle'), Js('Repair Vehicle'), Js('Self-Propelled Anti-Tank Vehicle'), Js('Self-Propelled Gun'), Js('Self-Propelled Mortar'), Js('Supply Vehicle'), Js('Tank Destroyer'), Js('Transport'), Js('Utility Vehicle')]))
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', ((((((((var.get('nm4').get(var.get('rnd3'))+var.get('nm3').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+Js(' '))+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
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
militaryVehicles = var.to_python()
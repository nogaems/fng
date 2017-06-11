__all__ = ['mechaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm3', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Action'), Js('Advanced'), Js('Aerial'), Js('All Terrain'), Js('Amplified'), Js('Anarchy'), Js('Apex'), Js('Aquatic'), Js('Arachnid'), Js('Arctic'), Js('Armageddon'), Js('Armed'), Js('Armored'), Js('Artillery'), Js('Assault'), Js('Assembly'), Js('Augmented'), Js('Avatar'), Js('Avian'), Js('Ballistic'), Js('Barrage'), Js('Battle'), Js('Battleground'), Js('Beast'), Js('Bio'), Js('Bio-Armored'), Js('Bionic'), Js('Blitz'), Js('Broad'), Js('Buccaneer'), Js('Cardinal'), Js('Cataclysm'), Js('Cavalry'), Js('Central Command'), Js('Champion'), Js('Chaos'), Js('Charge'), Js('Chrome'), Js('Chrono'), Js('Cloud'), Js('Cobra'), Js('Combat'), Js('Compact'), Js('Core'), Js('Cosmic'), Js('Covert'), Js('Cruel'), Js('Crusader'), Js('Cryo'), Js('Cyclone'), Js('Daemon'), Js('Dark'), Js('Death'), Js('Defensive'), Js('Deployment'), Js('Destruction'), Js('Dimensional'), Js('Divine'), Js('Domination'), Js('Doom'), Js('Dragon'), Js('Dragoon'), Js('Dread'), Js('Drill'), Js('Dynamic'), Js('Elemental'), Js('Elite'), Js('First Assault'), Js('Flock'), Js('Flood'), Js('Frenzy'), Js('Front Line'), Js('Fury'), Js('Galactic'), Js('God'), Js('Goddess'), Js('Golem'), Js('Goliath'), Js('Grand'), Js('Grave'), Js('Great'), Js('Grim'), Js('Hallowed'), Js('Havoc'), Js('Hazard'), Js('Heavy'), Js('Hercules'), Js('Hero'), Js('High Agility'), Js('High Terrain'), Js('Horde'), Js('Hulking'), Js('Hurricane'), Js('Hysteria'), Js('Immortal'), Js('Imperial'), Js('Infernal'), Js('Infinity'), Js('Intervention'), Js('Intrusion'), Js('Invasion'), Js('Iron'), Js('Judgment'), Js('Jumbo'), Js('Jungle'), Js('Legion'), Js('Light'), Js('Mammoth'), Js('Maneuver'), Js('Martial'), Js('Master'), Js('Mayhem'), Js('Mega'), Js('Metal'), Js('Miracle'), Js('Mist'), Js('Mobile'), Js('Multi'), Js('Myriad'), Js('Naval'), Js('Nexus'), Js('Night'), Js('Nuclear'), Js('Offensive'), Js('Ominous'), Js('Orbital'), Js('Panzer'), Js('Paragon'), Js('Peril'), Js('Phantom'), Js('Phoenix'), Js('Pioneer'), Js('Plane'), Js('Planet'), Js('Portable'), Js('Power'), Js('Powered'), Js('Preparation'), Js('Primary'), Js('Prime'), Js('Proto'), Js('Psychic'), Js('Psycho'), Js('Pygmy'), Js('Pyro'), Js('Raid'), Js('Ravage'), Js('Regal'), Js('Rescue'), Js('Revered'), Js('Roaming'), Js('Robust'), Js('Round'), Js('Royal'), Js('Salvage'), Js('Savage'), Js('Science'), Js('Scorpion'), Js('Service'), Js('Shade'), Js('Shadow'), Js('Shock'), Js('Silent'), Js('Silver'), Js('Sinister'), Js('Skirmish'), Js('Solid'), Js('Sonic'), Js('Spider'), Js('Spirit'), Js('Stalker'), Js('Storm'), Js('Storming'), Js('Strategic'), Js('Strike'), Js('Swarm'), Js('Tactical'), Js('Tactical Raid'), Js('Tactile'), Js('Tempest'), Js('Thunder'), Js('Titan'), Js('Titanic'), Js('Transforming'), Js('Trauma'), Js('Typhoon'), Js('Unarmed'), Js('Urban'), Js('Vanguard'), Js('Variable'), Js('Versatile'), Js('Viking'), Js('Vile'), Js('Viper'), Js('Vital'), Js('Vitality'), Js('Void'), Js('Wandering'), Js('War'), Js('Warfare'), Js('Wicked'), Js('Wolverine'), Js('Wrath')]))
    var.put('nm3', Js([Js('Achilles'), Js('Actium'), Js('Agememnon'), Js('Albatross'), Js('Anarchy'), Js('Andromeda'), Js('Antioch'), Js('Apollo'), Js('Aquila'), Js('Archangel'), Js('Archmage'), Js('Argo'), Js('Aries'), Js('Arizone'), Js('Armada'), Js('Armageddon'), Js('Artemis'), Js('Arthas'), Js('Athens'), Js('Atlas'), Js('Aura'), Js('Aurora'), Js('Avalanche'), Js('Avalaon'), Js('Babylon'), Js('Badger'), Js('Bandit'), Js('Basilisk'), Js('Bastion'), Js('Bear'), Js('Behemoth'), Js('Berserker'), Js('Big Boy'), Js('Big Daddy'), Js('Big Girl'), Js('Big Momma'), Js('Black Widow'), Js('Blade'), Js('Blitz'), Js('Blossom'), Js('Boa'), Js('Boar'), Js('Buccaneer'), Js('Buzzard'), Js('Caelestis'), Js('Calamity'), Js('Calypso'), Js('Carnage'), Js('Carthage'), Js('Centipede'), Js('Centurion'), Js('Challenger'), Js('Chimera'), Js('Chronos'), Js('Claymore'), Js('Cobra'), Js('Colossus'), Js('Comet'), Js('Condor'), Js('Conquistador'), Js('Corsair'), Js('Covenant'), Js('Coyote'), Js('Crow'), Js('Curator'), Js('Cyclops'), Js('Dagger'), Js('Death'), Js('Destiny'), Js('Diplomat'), Js('Discovery'), Js('Divine Intervention'), Js('Dragon'), Js('Dreadnought'), Js('Elysium'), Js('Emperor'), Js('Empress'), Js('Endeavor'), Js('Enigma'), Js('Eternity'), Js('Euphoria'), Js('Exarch'), Js('Executioner'), Js('Fade'), Js('Faith'), Js('Falcon'), Js('Fate'), Js('Fortuna'), Js('Freedom'), Js('Frontier'), Js('Galactica'), Js('Gauntlet'), Js('Genesis'), Js('Gladiator'), Js('Glory'), Js('Goblin'), Js('Golem'), Js('Gremlin'), Js('Grim'), Js('Grim Reaper'), Js('Grim Reaver'), Js('Guardian'), Js('Halo'), Js('Hammer'), Js('Hammerhead'), Js('Hannibal'), Js('Harlequin'), Js('Harmony'), Js('Harpy'), Js('Hawk'), Js('Hercules'), Js('Hog'), Js('Hummingbird'), Js('Hunter'), Js('Huntress'), Js('Hurricane'), Js('Icarus'), Js('Impulse'), Js('Independence'), Js('Inferno'), Js('Infinity'), Js('Innuendo'), Js('Invictus'), Js('Invincible'), Js('Jaeger'), Js('Javelin'), Js('Judgment'), Js('Juggernaut'), Js('Karma'), Js('Khan'), Js('Kingfisher'), Js('Kraken'), Js('Legacy'), Js('Legionnaire'), Js('Leviathan'), Js('Liberty'), Js('Loki'), Js('Lupus'), Js('Lust'), Js('Mace'), Js('Manticore'), Js('Matador'), Js('Minotaur'), Js('Myrmidon'), Js('Nebechadnezzar'), Js('Nemesis'), Js('Nemo'), Js('Neptune'), Js('Nero'), Js('Nexus'), Js('Nightingale'), Js('Nightmare'), Js('Nirvana'), Js('Nomad'), Js('Nostradamus'), Js('Nova'), Js('Oberon'), Js('Oblivion'), Js('Oracle'), Js('Orion'), Js('Pandora'), Js('Pathfinder'), Js('Patience'), Js('Peacock'), Js('Pegasus'), Js('Pelican'), Js('Phantom'), Js('Phoenix'), Js('Pilgrim'), Js('Polaris'), Js('Poseidon'), Js('Prometheus'), Js('Promise'), Js('Proximo'), Js('Rascal'), Js('Ravager'), Js('Raven'), Js('Reaper'), Js('Reaver'), Js('Retribution'), Js('Revenant'), Js('Rhino'), Js('Ripper'), Js('Saber'), Js('Sage'), Js('Samurai'), Js('Scavenger'), Js('Scimitar'), Js('Scorpio'), Js('Scythe'), Js('Serenity'), Js('Shade'), Js('Siren'), Js('Slayer'), Js('Sparrow'), Js('Spartacus'), Js('Spectator'), Js('Storm'), Js('Super Nova'), Js('Templar'), Js('Termite'), Js('Thanos'), Js('Thor'), Js('Thunder'), Js('Thunderbolt'), Js('Thunderstorm'), Js('Tomahawk'), Js('Torment'), Js('Tortoise'), Js('Tranquility'), Js('Trident'), Js('Triumph'), Js('Unicorn'), Js('Unity'), Js('Vagabond'), Js('Valhalla'), Js('Valiant'), Js('Valkyrie'), Js('Vanguard'), Js('Vengeance'), Js('Vice'), Js('Viper'), Js('Voyager'), Js('Vulture'), Js('Warlock'), Js('Warrior'), Js('Watcher'), Js('Widow Maker'), Js('Wisdom'), Js('Wolf'), Js('Wolverine'), Js('Woodpecker'), Js('Wrath'), Js('Wyvern'), Js('Zephyr'), Js('Zero'), Js('Zeus'), Js('Zion')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', var.get('nm3').get(var.get('rnd')))
                var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('Angel'), Js('Armor'), Js('Armor Suit'), Js('Battler'), Js('Buster'), Js('Colossus'), Js('Combatant'), Js('Command Suit'), Js('Command Unit'), Js('Decimator'), Js('Leviathan'), Js('Dreadnought'), Js('Drone'), Js('Engine'), Js('Fighter'), Js('Fortress'), Js('Gear'), Js('Guardian'), Js('Gun System'), Js('Jaeger'), Js('Juggernaut'), Js('Machine'), Js('Master'), Js('Master Suit'), Js('Mech'), Js('Panzer'), Js('Runner'), Js('Scouter'), Js('Sentinel'), Js('Stalker'), Js('Strider'), Js('Suit'), Js('Transport'), Js('Trooper'), Js('Unit'), Js('Valkyrie'), Js('Walker'), Js('Warmech')]))
pass
pass


# Add lib to the module scope
mechaNames = var.to_python()
__all__ = ['superTeams']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'nm3', 'result'])
    var.put('nm1', Js([Js('Aberration'), Js('Alpha'), Js('Amendment'), Js('Angel'), Js('Anomaly'), Js('Apex'), Js('Arachnid'), Js('Arcane'), Js('Assault'), Js('Augmented'), Js('Aura'), Js('Aurora'), Js('Banshee'), Js('Barrage'), Js('Behemoth'), Js('Blitz'), Js('Blood'), Js('Cardinal'), Js('Carnage'), Js('Castaway'), Js('Challenger'), Js('Chaperon'), Js('Chief'), Js('Cobra'), Js('Cosmos'), Js('Covert'), Js('Crimson'), Js('Crisis'), Js('Crux'), Js('Curator'), Js('Custodian'), Js('Daemon'), Js('Defiance'), Js('Demon'), Js('Destiny'), Js('Devil'), Js('Divine'), Js('Eerie'), Js('Enigma'), Js('Epitome'), Js('Eternity'), Js('Ethereal'), Js('Exile'), Js('Extreme'), Js('Feral'), Js('Figment'), Js('Flux'), Js('Freak'), Js('Fugitive'), Js('Future'), Js('Galaxy'), Js('Global'), Js('Golden'), Js('Grim'), Js('Guardian'), Js('Hazard'), Js('Illusion'), Js('Impact'), Js('Infernal'), Js('Inferno'), Js('Infinity'), Js('Inhuman'), Js('Insurgence'), Js('Invasion'), Js('Ironclad'), Js('Jackal'), Js('Justice'), Js('Juvenile'), Js('Light'), Js('Maestro'), Js('Maraud'), Js('Maroon'), Js('Memento'), Js('Miracle'), Js('Mirage'), Js('Monster'), Js('Mutant'), Js('Myriad'), Js('Mystery'), Js('Mythic'), Js('Nebula'), Js('Nemesis'), Js('New'), Js('New Law'), Js('New Vision'), Js('Nightmare'), Js('Nova'), Js('Omega'), Js('Oracle'), Js('Parable'), Js('Paradox'), Js('Paragon'), Js('Paramount'), Js('Phantom'), Js('Phenomenon'), Js('Phoenix'), Js('Pinnacle'), Js('Power'), Js('Primal'), Js('Prime'), Js('Prodigy'), Js('Prototype'), Js('Quantum'), Js('Rascal'), Js('Reformation'), Js('Remedy'), Js('Revelation'), Js('Revenent'), Js('Riot'), Js('Rogue'), Js('Ruthless'), Js('Sanction'), Js('Sanguine'), Js('Savage'), Js('Sentence'), Js('Sentinel'), Js('Seraph'), Js('Shadow'), Js('Shepherd'), Js('Silent'), Js('Silver'), Js('Singular'), Js('Singularity'), Js('Skirmish'), Js('Sovereign'), Js('Spectral'), Js('Storm'), Js('Super'), Js('Supreme'), Js('Terra'), Js('Thunder'), Js('Time'), Js('Transcendent'), Js('Triad'), Js('Trinity'), Js('Universe'), Js('Vagrant'), Js('Vertex'), Js('Vigilante'), Js('Viper'), Js('Visionary'), Js('Vitality'), Js('Void'), Js('Watchdog'), Js('Whisper'), Js('Wonder'), Js('Zealot')]))
    var.put('nm2', Js([Js('Alliance'), Js('Allies'), Js('Battalion'), Js('Brawlers'), Js('Centurions'), Js('Champions'), Js('Clan'), Js('Crew'), Js('Crusaders'), Js('Custodians'), Js('Defenders'), Js('Fighters'), Js('Flight'), Js('Force'), Js('Guardians'), Js('Guards'), Js('Heroes'), Js('Knights'), Js('League'), Js('Legion'), Js('Marvels'), Js('Masters'), Js('Oracles'), Js('Outcasts'), Js('Pack'), Js('Patrol'), Js('Rangers'), Js('Rebels'), Js('Sentinels'), Js('Soldiers'), Js('Squad'), Js('Squadron'), Js('Syndicate'), Js('Titans'), Js('Troopers'), Js('Unit'), Js('Warriors'), Js('Watch'), Js('Wings')]))
    var.put('nm3', Js([Js('Aberrations'), Js('Allies'), Js('Ancestors'), Js('Angels'), Js('Animals'), Js('Anomalies'), Js('Arachnids'), Js('Archetypes'), Js('Auras'), Js('Banshees'), Js('Battalion'), Js('Behemoths'), Js('Berserkers'), Js('Bionics'), Js('Brawlers'), Js('Cardinals'), Js('Castaways'), Js('Centurions'), Js('Champions'), Js('Chosen'), Js('Cobras'), Js('Colossals'), Js('Coverts'), Js('Crackerjacks'), Js('Crazed'), Js('Crusaders'), Js('Curators'), Js('Cursed'), Js('Custodians'), Js('Daemons'), Js('Defenders'), Js('Demons'), Js('Deranged'), Js('Designs'), Js('Deviations'), Js('Devils'), Js('Divine'), Js('Divines'), Js('Elite'), Js('Enigmas'), Js('Epitomes'), Js('Eternals'), Js('Ethereals'), Js('Exclusives'), Js('Exiles'), Js('Fanatics'), Js('Ferals'), Js('Fiends'), Js('Figments'), Js('Flight'), Js('Freaks'), Js('Freaks of Nature'), Js('Fruitcakes'), Js('Fugitives'), Js('Gimmicks'), Js('Gizos'), Js('Golems'), Js('Goliaths'), Js('Guardians'), Js('Heralds'), Js('Hounds'), Js('Hunters'), Js('Illusionists'), Js('Illusions'), Js('Immortals'), Js('Imps'), Js('Infernals'), Js('Infinities'), Js('Inventions'), Js('Ironclad'), Js('Jackals'), Js('Juveniles'), Js('Keepers'), Js('Legion'), Js('Lunatics'), Js('Mad Dogs'), Js('Maestros'), Js('Malevolents'), Js('Maniacs'), Js('Marauders'), Js('Maroons'), Js('Marvels'), Js('Masters'), Js('Miracles'), Js('Mirages'), Js('Miscreants'), Js('Monsters'), Js('Myriad'), Js('Nebulas'), Js('Nemeses'), Js('Nightmares'), Js('Novae'), Js('Novas'), Js('Omegas'), Js('Omens'), Js('Oracles'), Js('Originals'), Js('Outcasts'), Js('Parable'), Js('Paradoxes'), Js('Paragons'), Js('Paramounts'), Js('Phoenixes'), Js('Pioneers'), Js('Predator'), Js('Primals'), Js('Primitives'), Js('Primordials'), Js('Pristines'), Js('Prophecies'), Js('Prototypes'), Js('Quirks'), Js('Rangers'), Js('Raptors'), Js('Rascals'), Js('Renegades'), Js('Sanguines'), Js('Savages'), Js('Selected'), Js('Sentinels'), Js('Seraphs'), Js('Silent Ones'), Js('Singularities'), Js('Spectrals'), Js('Superiors'), Js('Thunders'), Js('Titans'), Js('Tricksters'), Js('Trinities'), Js('Undying'), Js('Untamed'), Js('Vagabonds'), Js('Vagrants'), Js('Vigilantes'), Js('Vindicators'), Js('Vipers'), Js('Visionaries'), Js('Watchdogs'), Js('Whispers'), Js('Wildlings'), Js('Wings'), Js('Wonders'), Js('Wretched')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (Js('The ')+var.get('nm3').get(var.get('rnd'))))
                var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
superTeams = var.to_python()
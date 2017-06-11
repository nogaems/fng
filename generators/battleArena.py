__all__ = ['battleArena']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aberration'), Js('Abyss'), Js('Acid'), Js('Afterlife'), Js('Amnesia'), Js('Anarchy'), Js('Angel of death'), Js('Annihilation'), Js('Anthrax'), Js('Archdemon'), Js('Armada'), Js('Armageddon'), Js('Armagedome'), Js('Ash and Dust'), Js('Assassination'), Js('Ataxia'), Js('Autopsy'), Js('Babylon'), Js('Battleborn'), Js('Behemoth'), Js('Berzerker'), Js('Birdfeed'), Js('Black Angel'), Js('Black Bird'), Js('Black Blade'), Js('Black Rainbow'), Js('Blackheart'), Js('Blacksoul'), Js('Blacksun'), Js('Blade Fury'), Js('Bladefist'), Js('Blitz'), Js('Blood and Gore'), Js('Bloodbath'), Js('Bloodblitz'), Js('Bloodlake'), Js('Bloodlust'), Js('Bloodstain'), Js('Broken Hell'), Js('Bullettooth'), Js('Burning Wing'), Js('Cadaver'), Js('Cannibal'), Js('Carcass'), Js('Carnage'), Js('Carnival'), Js('Cataclysm'), Js('Cemetery'), Js('Chaos'), Js('Claymore'), Js('Crimson'), Js('Daggertip'), Js('Dark Ages'), Js('Dead Horse'), Js("Death's"), Js('Deathbound'), Js('Delirium'), Js('Demigod'), Js('Demise'), Js('Demondome'), Js('Desecration'), Js('Diablo'), Js('Dismember'), Js('Dominion'), Js('Doomhammer'), Js('Double Trouble'), Js('Dragontooth'), Js('Dread'), Js('Dynomite'), Js('Eclipse'), Js('Elysium'), Js('Eradication'), Js('Eternity'), Js('Euthanasia'), Js('Exodus'), Js('Exposition'), Js('Extinction'), Js('Extravaganza'), Js('Fallen Saint'), Js('Fatality'), Js('Fear Factory'), Js('Femme Fatale'), Js('Fireworks'), Js('Forsaken'), Js('Four Hoursemen'), Js('Fracas'), Js('Freakville'), Js('Free For All'), Js('Freefall'), Js('Frenzy'), Js('Funeral'), Js('Fury'), Js('Garotte'), Js('Gladiator'), Js('Gore'), Js('Gorefest'), Js('Grim'), Js('Grim Reaper'), Js('Haemorrhage'), Js('Hallowed'), Js('Havoc'), Js('Hazard'), Js('Hell Incarnate'), Js("Hell's Gate"), Js('Hellbound'), Js('Hellion'), Js('Hellraised'), Js('Hellraiser'), Js('Heresy'), Js('Hibernation'), Js('Hollow'), Js('Holy Grail'), Js('Horror'), Js('Hurricane'), Js('Hysteria'), Js('Icarus'), Js('Immolation'), Js('Inferno'), Js('Infinity'), Js('Insomnia'), Js('Iron Maiden'), Js('Ironbound'), Js('Ironwing'), Js('Judgment'), Js('Jungle'), Js('Karma'), Js('King Cobra'), Js('Kriskras'), Js('Labyrinth'), Js('Lawbreaker'), Js('Limbo'), Js('Lost Soul'), Js('Lunacy'), Js('Macabre'), Js('Madness'), Js('Malevolence'), Js('Maneater'), Js('Mania'), Js('Manslayer'), Js('Martyr'), Js('Massacre'), Js('Mayhem'), Js('Menimals'), Js('Misery'), Js('Mistress of Pain'), Js('Molotov'), Js('Napalm'), Js('Necro'), Js('Necrodome'), Js('Necrosis'), Js('Nefarious'), Js('Nephilim'), Js('Nemo'), Js('Nero'), Js('Nether'), Js('Netherdome'), Js('Netherworld'), Js('Nightfall'), Js('Nirvana'), Js('Noxidome'), Js('Noxious'), Js('Obituary'), Js('Obliteration'), Js('Oblivion'), Js('Overkill'), Js('Painkiller'), Js('Paradise'), Js('Paradox'), Js('Paranoia'), Js('Phantom'), Js('Phenomenon'), Js('Phobia'), Js('Psycho'), Js('Puppetmaster'), Js('Reaper'), Js('Red Lamb'), Js('Revolution'), Js('Riot'), Js('Sabertooth'), Js('Salvation'), Js('Sanctuary'), Js('Sandman'), Js('Sandstorm'), Js('Sanguine'), Js('Scimitar'), Js('Scourge'), Js('Scythe'), Js('Search and Destoy'), Js('Septic'), Js('Shadow'), Js('Shadowfall'), Js('Sharktank'), Js('Sinister'), Js('Skeleton'), Js('Slaughter and Laughter'), Js('Slice and Dice'), Js('Solstice'), Js('Spectacle'), Js('Starfall'), Js('Stormfury'), Js('Suffocation'), Js('Suicide'), Js('Sundown'), Js('Surgery'), Js('Switchblade'), Js('Symphony'), Js('Symptomium'), Js('Termination'), Js('Terminus'), Js('Terror'), Js('Terrordome'), Js('Thorne'), Js('Thunder'), Js('Tyranny'), Js('Titan'), Js('Torture Squad'), Js('Tragedy'), Js('Tranquility'), Js('Transcendence'), Js('Twilight'), Js('Underdome'), Js('Underworld'), Js('Vermin'), Js('Void'), Js('Warpath'), Js('White Witch'), Js('Wrath'), Js('Xenomorph'), Js('Zero')]))
var.put('nm2', Js([Js('Arena'), Js('Stadium'), Js('Coliseum'), Js('Amphitheater'), Js('Arena')]))
pass
pass


# Add lib to the module scope
battleArena = var.to_python()
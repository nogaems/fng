__all__ = ['vampireClans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(8.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', var.get('nm3').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abyss'), Js('Annihilation'), Js('Banished'), Js('Bite'), Js('Black'), Js('Blood'), Js("Blood's"), Js("Crypt's"), Js('Dark'), Js('Death'), Js("Death's"), Js("Demise's"), Js('Demon'), Js('Demonic'), Js('Devil'), Js("Devil's"), Js('Dishonored'), Js('Downfall'), Js("Dusk's"), Js("End's"), Js('Enigma'), Js('Eternal'), Js('Fanged'), Js('Ghoul'), Js('Grave'), Js("Heaven's"), Js("Hell's"), Js('Immortal'), Js("Limbo's"), Js("Lucifer's"), Js('Midnight'), Js("Misery's"), Js('Moonlight'), Js('Necrosis'), Js('Nether'), Js('Night'), Js("Night's"), Js('Nightmare'), Js('Nightshade'), Js('Onyx'), Js('Perpetual'), Js('Phantom'), Js("Purgatory's"), Js('Sanguine'), Js('Shadow'), Js("Shadow's"), Js('Tempest'), Js('Tomb'), Js('Tormented'), Js('Undying'), Js('Unending'), Js('Wicked')]))
var.put('nm2', Js([Js('Ancestors'), Js('Ancestry'), Js('Army'), Js('Birth'), Js('Brigade'), Js('Castaways'), Js('Company'), Js('Coven'), Js('Covet'), Js('Craving'), Js('Crawlers'), Js('Defilers'), Js('Descendants'), Js('Descent'), Js('Desire'), Js('Division'), Js('Dragons'), Js('Eclipe'), Js('Exiles'), Js('Fiends'), Js('Flight'), Js('Flyers'), Js('Gaze'), Js('Gift'), Js('Hearts'), Js('Horde'), Js('Hunger'), Js('Insomniacs'), Js('Leeches'), Js('Legion'), Js('Longing'), Js('Lurkers'), Js('Lust'), Js('Marauders'), Js('Mark'), Js('Marks'), Js('Myriad'), Js('Nomads'), Js('Oblivion'), Js('Origin'), Js('Outcasts'), Js('Outlaws'), Js('Phalanx'), Js('Posse'), Js('Quenchers'), Js('Raiders'), Js('Refugees'), Js('Rejects'), Js('Restless'), Js('Rogues'), Js('Runners'), Js('Seekers'), Js('Shadow'), Js('Shadows'), Js('Shroud'), Js('Sundry'), Js('Swarm'), Js('Teeth'), Js('Thirst'), Js('Torment'), Js('Void'), Js('Wanderers'), Js('Watch'), Js('Wings')]))
var.put('nm3', Js([Js('Bite Mark'), Js('Black Knights'), Js('Blood Bankers'), Js('Blood Infusion'), Js('Bloodbound'), Js('Bloodworth'), Js('Carpe Noctem'), Js('Children of the Night'), Js('Citizens of Darkness'), Js('Dark Heaven'), Js('Dark Omen'), Js('Demonix'), Js('Denizens of Darkness'), Js('Diluculum'), Js('Fighters of the Fang'), Js('House of the Bat'), Js('House of the Night'), Js('House of the Phoenix'), Js('Insomniacs'), Js('Lamia'), Js('Masquerade'), Js('Mediis Tenebris'), Js('Midnight Terror'), Js('Neck Romancers'), Js('Night Dwellers'), Js('Night Spawns'), Js("Night's Harmony"), Js('Nightmare Association'), Js('Nightshades'), Js('Nightworth'), Js('Noctis'), Js('Nox'), Js('Purebloods'), Js('Red Night'), Js('Sanguine Ligurio'), Js('Sanguinity'), Js('Sanguinoso'), Js('Silver Coven'), Js('Solar Eclipse'), Js('Tantibus'), Js('The Ashes'), Js('The Brood'), Js('The Flock'), Js('The Gauntlet'), Js('The Mist'), Js('The Sabbat'), Js('The Scarlet Kiss'), Js('The Unaligned'), Js('The Will'), Js('Total Eclipse'), Js('Visio Aeternae'), Js('Youngbloods')]))
pass
pass


# Add lib to the module scope
vampireClans = var.to_python()
__all__ = ['nightclubNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('names', var.get('names1').get(var.get('rnd')))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('names', (Js('Club ')+var.get('names1').get(var.get('rnd'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('names', (Js('The ')+var.get('names2').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Adonis'), Js('Alcazar'), Js('Alibi'), Js('All Star'), Js('Altitude'), Js('Apex'), Js('Apollo'), Js('Aqua'), Js('Arcane'), Js('Archangel'), Js('Arctic'), Js('Aspect'), Js('Attitude'), Js('Aura'), Js('Aurora'), Js('Azure'), Js('Balthazar'), Js('Barbarian'), Js('Barrage'), Js('Bazaar'), Js('Blaze'), Js('Bliss'), Js('Bloom'), Js('Blossom'), Js('Borealis'), Js('Bounce'), Js('Boundary'), Js('Bullet'), Js('Bullseye'), Js('Burlesque'), Js('Cacao'), Js('Cameo'), Js('Cargo'), Js("Cat's Eye"), Js('Century'), Js('Chaos'), Js('Cinnamon'), Js('Cipher'), Js('Circus'), Js('Climax'), Js('Cloud'), Js('Cobalt'), Js('Cocoa'), Js('Code'), Js('Colosseum'), Js('Comedy'), Js('Compass'), Js('Cosmos'), Js('Creed'), Js('Crimson'), Js('Crystal'), Js('Cube'), Js('Debut'), Js('Delight'), Js('Delirium'), Js('Destiny'), Js('Detective'), Js('Deviant'), Js('Diamond'), Js('Diva'), Js('Drama'), Js('Duo'), Js('Echo'), Js('Eclipse'), Js('Ecstasy'), Js('Electric'), Js('Elegance'), Js('Element'), Js('Elysium'), Js('Embargo'), Js('Embassy'), Js('Ember'), Js('Emperor'), Js('Empire'), Js('Enchant'), Js('Enigma'), Js('Entity'), Js('Envy'), Js('Escape'), Js('Essence'), Js('Etcetera'), Js('Eternity'), Js('Euphoria'), Js('Fabric'), Js('Fantasia'), Js('Fantasy'), Js('Fate'), Js('Felicity'), Js('Fever'), Js('Fiber'), Js('Fiction'), Js('Fire'), Js('Flower'), Js('Fortune'), Js('Forum'), Js('Frenzy'), Js('Frontier'), Js('Galaxy'), Js('Gallery'), Js('Glacier'), Js('Glee'), Js('Grace'), Js('H20'), Js('Harmony'), Js('Heaven'), Js('Horizon'), Js('Hysteria'), Js('Icecube'), Js('Illusion'), Js('Indigo'), Js('Inferno'), Js('Infinity'), Js('Insanity'), Js('Irony'), Js('Ivory'), Js('Ivy'), Js('Jade'), Js('Justice'), Js('Karma'), Js('Knockout'), Js('Lavender'), Js('Lily'), Js('Lime'), Js('Liquid'), Js('Loop'), Js('Loophole'), Js('Lost'), Js('Lucifer'), Js('Luck'), Js('Luna'), Js('Magenta'), Js('Magic'), Js('Mahogany'), Js('Majesty'), Js('Matter'), Js('Meltdown'), Js('Memo'), Js('Metropolis'), Js('Mint'), Js('Miracle'), Js('Mirage'), Js('Mirth'), Js('Monarch'), Js('Myriad'), Js('Mystery'), Js('Mystic'), Js('Myth'), Js('Nebula'), Js('Nemesis'), Js('Nightingale'), Js('Nightshade'), Js('Nine Lives'), Js('Nirvana'), Js('Nova'), Js('Obelisk'), Js('Obsidian'), Js('Ocean'), Js('Opal'), Js('Oracle'), Js('Orchid'), Js('Oxygen'), Js('Palace'), Js('Paradise'), Js('Paragon'), Js('Parallel'), Js('Paramount'), Js('Particle'), Js('Passion'), Js('Penthuose'), Js('Petal'), Js('Phantom'), Js('Phobia'), Js('Phoenix'), Js('Pinnacle'), Js('Priority'), Js('Prodigy'), Js('Profile'), Js('Prophecy'), Js('Pulse'), Js('Pyre'), Js('Quicksilver'), Js('Ragdoll'), Js('Rapture'), Js('Realm'), Js('Record'), Js('Reflex'), Js('Reincarnation'), Js('Reply'), Js('Republic'), Js('Resilience'), Js('Revolution'), Js('Riddle'), Js('Rogue'), Js('Rose'), Js('Rouge'), Js('Royale'), Js('Ruby'), Js('Sanction'), Js('Sanguine'), Js('Sanity'), Js('Sapphire'), Js('Sarcasm'), Js('Satire'), Js('Scarlet'), Js('Scent'), Js('Secret'), Js('Sepia'), Js('Serenity'), Js('Shadow'), Js('Silver'), Js('Sin'), Js('Sketch'), Js('Snowflake'), Js('Solo'), Js('Sphinx'), Js('Spice'), Js('Spirit'), Js('Storm'), Js('Studio'), Js('Summit'), Js('Supernova'), Js('Syndrome'), Js('Telepathy'), Js('Tempest'), Js('Temple'), Js('Temptation'), Js('Thunder'), Js('Tranquility'), Js('Trinity'), Js('Trinket'), Js('Triumph'), Js('Troy'), Js('Twilight'), Js('Typhoon'), Js('Universe'), Js('Utopia'), Js('Vampire'), Js('Vanish'), Js('Vapor'), Js('Veil'), Js('Venue'), Js('Venus'), Js('Vertex'), Js('Vigor'), Js('Vision'), Js('Volts'), Js('Vortex'), Js('Werewolf'), Js('Whisper'), Js('Zion')]))
var.put('names2', Js([Js('Adventure'), Js('Agenda'), Js('Album'), Js('Angel'), Js('Answer'), Js('Aquarium'), Js('Arrow'), Js('Attitude'), Js('Aura'), Js('Aurora'), Js('Avenue'), Js('Barbarian'), Js('Beach'), Js('Blossom'), Js('Bolt'), Js('Brew'), Js('Bridge'), Js('Bullet'), Js('Cameo'), Js('Capital'), Js('Castle'), Js('Century'), Js('Champion'), Js('Cherry'), Js('Circus'), Js('Coach'), Js('Code'), Js('Codename'), Js('Core'), Js('Court'), Js('Crobar'), Js('Crown'), Js('Crypt'), Js('Demon'), Js('Den'), Js('Deviant'), Js('Devil'), Js('Dove'), Js('Dream'), Js('Eclipse'), Js('Element'), Js('Emperor'), Js('Empire'), Js('Escape'), Js('Essence'), Js('Finale'), Js('Fire'), Js('Floor'), Js('Flux'), Js('Focus'), Js('Fortress'), Js('Forum'), Js('Foundation'), Js('Fragment'), Js('Galaxy'), Js('Gallery'), Js('Garage'), Js('Garden'), Js('Garrison'), Js('Gate'), Js('Grind'), Js('Groove'), Js('Harp'), Js('Heart'), Js('Heat'), Js('Hour'), Js('Hub'), Js('Hunt'), Js('Illusion'), Js('Incubus'), Js('Inferno'), Js('Ivy'), Js('Jive'), Js('Jungle'), Js('King'), Js('Lagoon'), Js('Legacy'), Js('Lily'), Js('Lion'), Js('Lodge'), Js('Loop'), Js('Loophole'), Js('Manor'), Js('Match'), Js('Millenium'), Js('Ministry'), Js('Mist'), Js('Monarch'), Js('Moon'), Js('Myth'), Js('Needle'), Js('Nest'), Js('Night'), Js('Nomad'), Js('Origin'), Js('Original'), Js('Parlour'), Js('Pavilion'), Js('Petal'), Js('Phantom'), Js('Place'), Js('Plan'), Js('Pride'), Js('Prince'), Js('Profile'), Js('Project'), Js('Propaganda'), Js('Punch'), Js('Punchline'), Js('Qube'), Js('Queen'), Js('Question'), Js('Raffle'), Js('Release'), Js('Resistance'), Js('Rhythm'), Js('Rogue'), Js('Rule'), Js('Shadow'), Js('Ship'), Js('Shore'), Js('Shout'), Js('Silver Spoon'), Js('Sin'), Js('Sketch'), Js('Sliver'), Js('Solstice'), Js('Spy'), Js('Station'), Js('Storm'), Js('Studio'), Js('Succubus'), Js('Summit'), Js('Sun'), Js('Supernova'), Js('Swan'), Js('Temptation'), Js('Theatre'), Js('Thirst'), Js('Thorn'), Js('Thunder'), Js('Titan'), Js('Tomb'), Js('Trinity'), Js('Tunnel'), Js('Underground'), Js('Underworld'), Js('Union'), Js('Universe'), Js('Vault'), Js('Veil'), Js('Venue'), Js('Vibe'), Js('View'), Js('Vine'), Js('Vision'), Js('Vortex'), Js('Whisper')]))
pass
pass


# Add lib to the module scope
nightclubNames = var.to_python()
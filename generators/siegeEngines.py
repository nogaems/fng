__all__ = ['siegeEngines']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Aberration'), Js('Aegis'), Js('Allegiance'), Js('Anarchy'), Js('Angel Wing'), Js('Arachnid'), Js('Armageddon'), Js('Asteroid'), Js('Banshee'), Js('Barrage'), Js('Basilisk'), Js('Battlewolf'), Js('Behemoth'), Js('Black Talon'), Js('Blizzard'), Js('Blood Moon'), Js('Bloodlord'), Js('Bloodspiller'), Js('Bone Warden'), Js('Brimstone'), Js('Buzzard'), Js('Caretaker'), Js('Cascade'), Js('Catastrophe'), Js('Cerberus'), Js('Chimera'), Js('Cobra'), Js('Comet'), Js('Constrictor'), Js('Cosmos'), Js('Cauldron'), Js('Curator'), Js("Curtain's Fall"), Js('Cyclops'), Js('Degenerate'), Js('Demon Horns'), Js('Demon Owl'), Js('Demon Quake'), Js("Devil's Grimace"), Js("Devil's Punch"), Js('Divine Favor'), Js('Divine Vow'), Js('Dragon Spine'), Js('Dragon Visage'), Js('Dragonbreath'), Js('Dragonfire'), Js('Dragonsoul'), Js('Dragoon'), Js('Dreadnaught'), Js('Ebon Herald'), Js('Ebon Shadow'), Js('Echo'), Js('Eclipse'), Js('Electric Guardian'), Js('Emerald Flame'), Js('Enigma'), Js('Eruption'), Js('Eulogy'), Js('Eventide'), Js('Face of Death'), Js('Feral Beast'), Js('Fiend'), Js('Fire Rain'), Js('Flame Wall'), Js('Frankenstein'), Js('Freak Show'), Js('Freak of Nature'), Js('Gargantuan'), Js("Giant's Fist"), Js("Grace's Grace"), Js('Grave Digger'), Js('Grease Monkey'), Js('Grim Reaper'), Js('Hades'), Js('Harbinger'), Js('Harvester'), Js('Hell Bringer'), Js('Hellbird'), Js('Hellbrand'), Js('Hellion'), Js('Hellish Scream'), Js('Hercules'), Js('Hippogriff'), Js('Homage'), Js('Hornet'), Js('Horseman'), Js('Hydra'), Js('Icicle'), Js('Inferno'), Js('Intimidator'), Js('Iron Golem'), Js('Iron Warden'), Js('Ivory Sentinel'), Js('Ivory Stinger'), Js('Jaeger'), Js('Javelin'), Js('Juggernaut'), Js("King's Legacy"), Js('Knockout'), Js('Leech'), Js("Lion's Roar"), Js('Lockjaw'), Js('Lone Rider'), Js('Mammoth'), Js('Man Hunter'), Js('Maneater'), Js('Medusa'), Js('Messenger'), Js('Minotaur'), Js('Mongrel'), Js('Mosquito'), Js('Necro'), Js('Nether Fiend'), Js('Night Terror'), Js('Night Watcher'), Js('Nightfall'), Js('Nightmare'), Js('Oathbreaker'), Js('Oathkeeper'), Js('Oblivion'), Js('Obsidian Blitz'), Js('Obsidian Grip'), Js('Obsidian Maw'), Js('Oddysey'), Js('Omega'), Js('Omen'), Js('Onyx Grasp'), Js('Onyx Javelin'), Js('Oracle'), Js('Overture'), Js('Pandemonium'), Js('Perforator'), Js('Phantom'), Js('Phoenix'), Js('Pilgrim'), Js('Plague Bringer'), Js('Rabid Dog'), Js('Rain of Terror'), Js('Rampage'), Js('Raptor'), Js('Rattlesnake'), Js('Reaper'), Js('Requiem'), Js('Rhinoceros'), Js('Rigor Mortis'), Js('Sabertooth'), Js('Sasquatch'), Js('Savage'), Js('Scorpio'), Js('Seism'), Js('Serpent'), Js('Serpent Sling'), Js('Shepherd'), Js('Shooting Star'), Js('Silence'), Js('Siren'), Js('Skeletal Horse'), Js('Souleater'), Js('Specter'), Js('Sphinx'), Js('Stalker'), Js('Stardust'), Js('Steel Knuckles'), Js('Steelskin'), Js('Storm Cloud'), Js('Sunset'), Js('Super Nova'), Js('Supremacy'), Js('Swan Dive'), Js('Swan Song'), Js('Tempest'), Js('Tenderizer'), Js('Thunder'), Js('Thunder Herald'), Js('Thunderstorm'), Js('Tidal Wave'), Js('Tigress'), Js("Titan's Wrath"), Js('Toboggan'), Js('Tortoise'), Js('Tremor'), Js('Tribute'), Js('Trinity'), Js('Trojan'), Js('Tsunami'), Js('Twister'), Js('Typhoon'), Js('Tyrant'), Js('Valkyrie'), Js('Vampire'), Js('Void'), Js('Volcano'), Js('Wall of Death'), Js('Warbear'), Js('Warden'), Js('Warmonger'), Js('Whirlwind'), Js('Wicker Man'), Js('Widow Maker'), Js('Wyvern')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', (Js('The ')+var.get('nm1').get(var.get('rnd'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
siegeEngines = var.to_python()
__all__ = ['fantasyRaces']

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
    var.registers(['nm1', 'nm2', 'result', 'type'])
    var.put('nm1', Js([Js('Abyss'), Js('Abyssal'), Js('Acid'), Js('Aerial'), Js('Aerie'), Js('Air'), Js('Anchored'), Js('Ancient'), Js('Aquatic'), Js('Arachnid'), Js('Arcane'), Js('Arctic'), Js('Argent'), Js('Ashen'), Js('Astral'), Js('Aurelian'), Js('Aurora'), Js('Austere'), Js('Austral'), Js('Autumn'), Js('Awoken'), Js('Azure'), Js('Barren'), Js('Beast'), Js('Berserk'), Js('Berserker'), Js('Blessed'), Js('Blight'), Js('Blind'), Js('Blood'), Js('Bog'), Js('Bone'), Js('Boreal'), Js('Boulder'), Js('Brass'), Js('Broken'), Js('Bronze'), Js('Brood'), Js('Canopy'), Js('Canyon'), Js('Cave'), Js('Cavern'), Js('Celestial'), Js('Chaos'), Js('Chasm'), Js('Chromatic'), Js('Clockwork'), Js('Cloud'), Js('Common'), Js('Copper'), Js('Core'), Js('Corrupt'), Js('Corrupted'), Js('Crimson'), Js('Cursed'), Js('Dark'), Js('Dawn'), Js('Deaf'), Js('Death'), Js('Deep'), Js('Demi'), Js('Demon'), Js('Demonic'), Js('Desert'), Js('Dew'), Js('Dim'), Js('Dire'), Js('Dirt'), Js('Divine'), Js('Doom'), Js('Dread'), Js('Dream'), Js('Dusk'), Js('Earthen'), Js('Eastern'), Js('Ebon'), Js('Ebony'), Js('Edge'), Js('Eerie'), Js('Elated'), Js('Elder'), Js('Elemental'), Js('Elite'), Js('Ember'), Js('Empyrean'), Js('Enchanted'), Js('Eternal'), Js('Ethereal'), Js('Exalted'), Js('Exo'), Js('Faerie'), Js('Fair'), Js('Fallen'), Js('False'), Js('Fel'), Js('Feral'), Js('Fey'), Js('Fire'), Js('First'), Js('Flame'), Js('Fog'), Js('Forest'), Js('Forged'), Js('Forgotten'), Js('Forlorn'), Js('Forsaken'), Js('Free'), Js('Frost'), Js('Frozen'), Js('Fury'), Js('Gear'), Js('Ghastly'), Js('Ghost'), Js('Giant'), Js('Gilded'), Js('Glacial'), Js('Glass'), Js('Gold'), Js('Grand'), Js('Grave'), Js('Gray'), Js('Great'), Js('Green'), Js('Grey'), Js('Grim'), Js('Grizzled'), Js('Grizzly'), Js('Grotto'), Js('Half'), Js('Hallowed'), Js('Harmony'), Js('Haunted'), Js('Haunting'), Js('Hell'), Js('Hellish'), Js('High'), Js('Highborn'), Js('Hill'), Js('Hive'), Js('Hollow'), Js('Humble'), Js('Ice'), Js('Immortal'), Js('Impure'), Js('Infernal'), Js('Inferno'), Js('Infinite'), Js('Infinity'), Js('Iron'), Js('Island'), Js('Ivory'), Js('Jade'), Js('Jungle'), Js('Juvenile'), Js('Lake'), Js('Lava'), Js('Light'), Js('Lone'), Js('Lost'), Js('Low'), Js('Lucent'), Js('Lunar'), Js('Mad'), Js('Magma'), Js('Major'), Js('Marked'), Js('Marsh'), Js('Masked'), Js('Metal'), Js('Mimic'), Js('Minor'), Js('Mist'), Js('Moon'), Js('Morass'), Js('Moss'), Js('Mountain'), Js('Mud'), Js('Mute'), Js('Mystic'), Js('Nebula'), Js('Nether'), Js('New'), Js('Night'), Js('Nightmare'), Js('Nimbus'), Js('Noble'), Js('Nocturnal'), Js('Nomad'), Js('Northern'), Js('Numb'), Js('Oblivion'), Js('Obsidian'), Js('Occult'), Js('Ocean'), Js('Oceanic'), Js('Onyx'), Js('Painted'), Js('Pale'), Js('Paragon'), Js('Phantom'), Js('Phase'), Js('Pinnacle'), Js('Planar'), Js('Plane'), Js('Poison'), Js('Primal'), Js('Prime'), Js('Primeval'), Js('Primordial'), Js('Proto'), Js('Pure'), Js('Putrid'), Js('Pygmy'), Js('Rabid'), Js('Radiant'), Js('Regal'), Js('Reserve'), Js('River'), Js('Rock'), Js('Royal'), Js('Sable'), Js('Sabre'), Js('Sacred'), Js('Salt'), Js('Sand'), Js('Sanguine'), Js('Savage'), Js('Scaled'), Js('Scourge'), Js('Sea'), Js('Serpent'), Js('Shadow'), Js('Shard'), Js('Shore'), Js('Silent'), Js('Silver'), Js('Skeletal'), Js('Sky'), Js('Smog'), Js('Smoke'), Js('Snow'), Js('Solar'), Js('Sorrow'), Js('Southern'), Js('Spectral'), Js('Spirit'), Js('Spring'), Js('Star'), Js('Stark'), Js('Stone'), Js('Storm'), Js('Subterranean'), Js('Summer'), Js('Sun'), Js('Supreme'), Js('Surface'), Js('Swamp'), Js('Tempest'), Js('Thunder'), Js('Timber'), Js('Timeless'), Js('Titan'), Js('Tomb'), Js('Torment'), Js('Torn'), Js('Tundra'), Js('Twilight'), Js('Urban'), Js('Valley'), Js('Veil'), Js('Veiled'), Js('Velvet'), Js('Venom'), Js('Vile'), Js('Violet'), Js('Void'), Js('Volcano'), Js('Warped'), Js('Waste'), Js('Western'), Js('Wicked'), Js('Wild'), Js('Winter'), Js('Wood'), Js('World'), Js('Wrath'), Js('Wretched'), Js('Zephyr')]))
    var.put('nm2', Js([Js('Angels'), Js('Beasts'), Js('Boggart'), Js('Centaurs'), Js('Demons'), Js('Dragonborn'), Js('Dryads'), Js('Dwarves'), Js('Elementals'), Js('Elves'), Js('Ents'), Js('Fairies'), Js('Faun'), Js('Fiends'), Js('Folk'), Js('Giants'), Js('Gnolls'), Js('Gnomes'), Js('Goblins'), Js('Golems'), Js('Goliaths'), Js('Gorgons'), Js('Gremlins'), Js('Hagravens'), Js('Hags'), Js('Halflings'), Js('Harpies'), Js('Hobbits'), Js('Hobgoblins'), Js('Humans'), Js('Imps'), Js('Kobolds'), Js('Lamia'), Js('Merfolk'), Js('Minotaurs'), Js('Naga'), Js('Nymphs'), Js('Oceanids'), Js('Ogres'), Js('Lich'), Js('Gargoyles'), Js('Grendels'), Js('Draugr'), Js('Kappa'), Js('Oni'), Js('Wendigo'), Js('Drake'), Js('Dragonborn'), Js('Ghouls'), Js('Grell'), Js('Hydra'), Js('Trogg'), Js('Orcs'), Js('People'), Js('Satyr'), Js('Siren'), Js('Spriggan'), Js('Sylphs'), Js('Trolls'), Js('Undine'), Js('Valkyrie'), Js('Vampires'), Js('Werewolves')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if var.get('$')(Js('#firChange')).callprop('is', Js(':checked')):
                var.put('val', var.get('$')(Js('.firChange')).callprop('val'))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('val')+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if var.get('$')(Js('#secChange')).callprop('is', Js(':checked')):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('val', var.get('$')(Js('.secChange')).callprop('val'))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('val')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
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
fantasyRaces = var.to_python()
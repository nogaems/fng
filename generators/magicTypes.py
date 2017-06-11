__all__ = ['magicTypes']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('names', var.get('names1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Aberrant Conjuring'), Js('Aberrant Magic'), Js('Aberrant Sorcery'), Js('Absorption Magic'), Js('Absorption Sorcery'), Js('Acid Bending'), Js('Acid Sorcery'), Js('Acid Conjuring'), Js('Acid Magic'), Js('Affliction Conjuring'), Js('Affliction Magic'), Js('Affliction Sorcery'), Js('Air Bending'), Js('Air Conjuring'), Js('Air Magic'), Js('Air Sorcery'), Js('Air Ritual'), Js('Ancestral Conjuring'), Js('Ancestral Magic'), Js('Ancestral Sorcery'), Js('Ancestral Ritual'), Js('Ancient Magic'), Js('Ancient Sorcery'), Js('Ancient Ritual'), Js('Angel Magic'), Js('Angel Ritual'), Js('Anger Bending'), Js('Anger Conjuring'), Js('Anger Magic'), Js('Anger Ritual'), Js('Anger Sorcery'), Js('Animalistic Conjuring'), Js('Animalistic Magic'), Js('Animalistic Sorcery'), Js('Animalistic Ritual'), Js('Arcane Sorcery'), Js('Arcane Ritual'), Js('Arcane Bending'), Js('Arcane Conjuring'), Js('Arcane Magic'), Js('Astral Bending'), Js('Astral Conjuring'), Js('Astral Ritual'), Js('Astral Sorcery'), Js('Astral Magic'), Js('Binding Magic'), Js('Black Conjuring'), Js('Black Ritual'), Js('Black Sorcery'), Js('Black Magic'), Js('Blood Bending'), Js('Blood Magic'), Js('Blood Sorcery'), Js('Blood Ritual'), Js('Body Bending'), Js('Body Ritual'), Js('Body Sorcery'), Js('Body Magic'), Js('Bullet Magic'), Js('Bullet Sorcery'), Js('Chain Bending'), Js('Chain Ritual'), Js('Chain Sorcery'), Js('Chain Conjuring'), Js('Chain Magic'), Js('Chaos Magic'), Js('Chaos Ritual'), Js('Chaos Sorcery'), Js('Chaotic Conjuring'), Js('Chi Bending'), Js('Chi Sorcery'), Js('Chi Ritual'), Js('Chi Magic'), Js('Clairvoyance Magic'), Js('Clone Conjuring'), Js('Clone Ritual'), Js('Clone Sorcery'), Js('Clone Magic'), Js('Companion Conjuring'), Js('Companion Magic'), Js('Companion Ritual'), Js('Companion Sorcery'), Js('Concealment Conjuring'), Js('Concealment Magic'), Js('Concealment Sorcery'), Js('Confusion Bending'), Js('Confusion Ritual'), Js('Confusion Sorcery'), Js('Confusion Conjuring'), Js('Confusion Magic'), Js('Curse Magic'), Js('Curse Ritual'), Js('Curse Sorcery'), Js('Dark Magic'), Js('Dark Ritual'), Js('Dark Sorcery'), Js('Dawn Magic'), Js('Dawn Sorcery'), Js('Dawn Ritual'), Js('Day Magic'), Js('Day Ritual'), Js('Day Sorcery'), Js('Death Ritual'), Js('Death Sorcery'), Js('Death Bending'), Js('Death Conjuring'), Js('Death Magic'), Js('Defense Conjuring'), Js('Defense Sorcery'), Js('Defense Magic'), Js('Demonic Bending'), Js('Demonic Conjuring'), Js('Demonic Sorcery'), Js('Demonic Ritual'), Js('Destruction Magic'), Js('Destruction Sorcery'), Js("Devil's Sorcery"), Js("Devil's Ritual"), Js('Dispelling Magic'), Js('Dragon Sorcery'), Js('Dragon Ritual'), Js('Dragon Magic'), Js('Draining Magic'), Js('Draining Sorcery'), Js('Dream Bending'), Js('Dream Sorcery'), Js('Dream Ritual'), Js('Dream Conjuring'), Js('Dream Magic'), Js('Druidic Magic'), Js('Druidic Ritual'), Js('Druidic Sorcery'), Js('Dusk Magic'), Js('Dusk Sorcery'), Js('Earth Bending'), Js('Earth Conjuring'), Js('Earth Ritual'), Js('Earth Sorcery'), Js('Earth Magic'), Js('Eclipse Magic'), Js('Eclipse Ritual'), Js('Eclipse Sorcery'), Js('Electric Bending'), Js('Electric Conjuring'), Js('Electric Magic'), Js('Electric Sorcery'), Js('Element Bending'), Js('Elemental Sorcery'), Js('Elemental Ritual'), Js('Elemental Conjuring'), Js('Elemental Magic'), Js('Elvish Magic'), Js('Elvish Sorcery'), Js('Elvish Ritual'), Js('Emotion Sorcery'), Js('Emotion Ritual'), Js('Emotion Bending'), Js('Emotion Conjuring'), Js('Emotion Magic'), Js('Emotional Bending'), Js('Emotional Conjuring'), Js('Emotional Magic'), Js('Emotional Sorcery'), Js('Emotional Ritual'), Js('Energy Sorcery'), Js('Energy Ritual'), Js('Energy Bending'), Js('Energy Conjuring'), Js('Energy Magic'), Js('Extreme Magic'), Js('Extreme Sorcery'), Js('Fairy Sorcery'), Js('Fairy Magic'), Js('Fear Ritual'), Js('Fear Sorcery'), Js('Fear Bending'), Js('Fear Conjuring'), Js('Fear Magic'), Js('Fire Bending'), Js('Fire Conjuring'), Js('Fire Magic'), Js('Fire Sorcery'), Js('Fire Ritual'), Js('Fluid Ritual'), Js('Fluid Sorcery'), Js('Fluid Bending'), Js('Fluid Conjuring'), Js('Fluid Magic'), Js('Gravity Bending'), Js('Gravity Magic'), Js('Gravity Sorcery'), Js('Haunt Sorcery'), Js('Haunt Ritual'), Js('Haunt Conjuring'), Js('Haunt Magic'), Js('Healing Magic'), Js('Healing Sorcery'), Js('Healing Ritual'), Js("Heaven's Magic"), Js("Heaven's Ritual"), Js("Hell's Ritual"), Js("Hell's Sorcery"), Js('High Magic'), Js('High Sorcery'), Js('Holy Ritual'), Js('Holy Bending'), Js('Holy Conjuring'), Js('Holy Magic'), Js('Ice Bending'), Js('Ice Conjuring'), Js('Ice Magic'), Js('Ice Ritual'), Js('Ice Sorcery'), Js('Illusion Sorcery'), Js('Illusion Ritual'), Js('Illusion Conjuring'), Js('Illusion Magic'), Js('Jinx Magic'), Js('Jinx Sorcery'), Js('Lava Ritual'), Js('Lava Sorcery'), Js('Lava Bending'), Js('Lava Conjuring'), Js('Left Hand Magic'), Js('Left Hand Sorcery'), Js('Life Sorcery'), Js('Life Ritual'), Js('Life Bending'), Js('Life Conjuring'), Js('Life Magic'), Js('Light Magic'), Js('Light Sorcery'), Js('Light Ritual'), Js('Lightning Ritual'), Js('Lightning Sorcery'), Js('Lightning Bending'), Js('Lightning Conjuring'), Js('Lightning Magic'), Js('Lost Ritual'), Js('Lost Sorcery'), Js('Lost Magic'), Js('Low Ritual'), Js('Low Sorcery'), Js('Low Magic'), Js('Lunar Conjuring'), Js('Lunar Magic'), Js('Lunar Ritual'), Js('Lunar Sorcery'), Js('Magnetic Bending'), Js('Magnetic Magic'), Js('Magnetic Ritual'), Js('Magnetic Sorcery'), Js('Metal Sorcery'), Js('Metal Bending'), Js('Metal Conjuring'), Js('Mimicry'), Js('Mind Bending'), Js('Mind Conjuring'), Js('Mind Control'), Js('Mind Magic'), Js('Mind Ritual'), Js('Mind Sorcery'), Js('Mirror Ritual'), Js('Mirror Sorcery'), Js('Mirror Magic'), Js('Musical Magic'), Js('Musical Ritual'), Js('Musical Sorcery'), Js('Nature Ritual'), Js('Nature Sorcery'), Js('Nature Bending'), Js('Nature Conjuring'), Js('Nature Magic'), Js('Necromancy'), Js('Necrotic Ritual'), Js('Necrotic Sorcery'), Js('Necrotic Conjuring'), Js('Necrotic Magic'), Js('Nether Magic'), Js('Nether Ritual'), Js('Nether Sorcery'), Js('Night Ritual'), Js('Night Sorcery'), Js('Night Magic'), Js('Noise Magic'), Js('Noise Sorcery'), Js('Ocean Ritual'), Js('Ocean Sorcery'), Js('Ocean Bending'), Js('Ocean Magic'), Js('Organic Magic'), Js('Organic Sorcery'), Js('Organic Ritual'), Js('Phantom Sorcery'), Js('Phantom Ritual'), Js('Phantom Conjuring'), Js('Phantom Magic'), Js('Plague Bending'), Js('Plague Conjuring'), Js('Plague Magic'), Js('Plague Ritual'), Js('Plague Sorcery'), Js('Possession Sorcery'), Js('Possession Ritual'), Js('Possession Magic'), Js('Projection Conjuring'), Js('Projection Magic'), Js('Projection Ritual'), Js('Projection Sorcery'), Js('Rainbow Magic'), Js('Rainbow Sorcery'), Js('Rainbow Ritual'), Js('Restriction Ritual'), Js('Restriction Sorcery'), Js('Restriction Conjuring'), Js('Restriction Magic'), Js('Revival Magic'), Js('Revival Sorcery'), Js('Revival Ritual'), Js('Right Hand Sorcery'), Js('Right Hand Magic'), Js('Scroll Magic'), Js('Scroll Ritual'), Js('Scroll Sorcery'), Js('Seasonal Sorcery'), Js('Seasonal Conjuring'), Js('Seasonal Magic'), Js('Sensory Magic'), Js('Sensory Sorcery'), Js('Shadow Ritual'), Js('Shadow Sorcery'), Js('Shadow Conjuring'), Js('Shadow Magic'), Js('Sleep Bending'), Js('Sleep Ritual'), Js('Sleep Sorcery'), Js('Sleep Magic'), Js('Solar Conjuring'), Js('Solar Magic'), Js('Solar Ritual'), Js('Solar Sorcery'), Js('Soul Ritual'), Js('Soul Sorcery'), Js('Soul Bending'), Js('Soul Conjuring'), Js('Soul Magic'), Js('Sound Magic'), Js('Sound Ritual'), Js('Sound Sorcery'), Js('Speed Sorcery'), Js('Speed Bending'), Js('Speed Magic'), Js('Spirit Bending'), Js('Spirit Conjuring'), Js('Spirit Magic'), Js('Spirit Ritual'), Js('Spirit Sorcery'), Js('Star Sorcery'), Js('Star Ritual'), Js('Star Magic'), Js('Storm Conjuring'), Js('Storm Ritual'), Js('Storm Sorcery'), Js('Subordination Sorcery'), Js('Subordination Magic'), Js('Telepathy'), Js('Teleportation Magic'), Js('Teleportation Sorcery'), Js('Teleportation Ritual'), Js('Tempest Ritual'), Js('Tempest Sorcery'), Js('Tempest Bending'), Js('Tempest Magic'), Js('Time Bending'), Js('Torment Conjuring'), Js('Torment Ritual'), Js('Torment Sorcery'), Js('Transformation Sorcery'), Js('Transformation Ritual'), Js('Transformation Bending'), Js('Transformation Magic'), Js('Twilight Magic'), Js('Twilight Sorcery'), Js('Twilight Ritual'), Js('Unholy Ritual'), Js('Unholy Bending'), Js('Unholy Conjuring'), Js('Unholy Sorcery'), Js('Vibration Sorcery'), Js('Vibration Bending'), Js('Vibration Conjuring'), Js('Vibration Magic'), Js('Voodoo'), Js('Water Bending'), Js('Water Ritual'), Js('Water Sorcery'), Js('Water Conjuring'), Js('Water Magic'), Js('Weather Bending'), Js('Weather Conjuring'), Js('Weather Magic'), Js('Weather Sorcery'), Js('Weather Ritual'), Js('White Ritual'), Js('White Magic'), Js('Witchcraft'), Js('Wizardry'), Js('Sky Magic'), Js('Sky Sorcery'), Js('Sky Ritual'), Js('Summoning Magic'), Js('Summoning Sorcery'), Js('Summoning Ritual')]))
pass
pass


# Add lib to the module scope
magicTypes = var.to_python()
__all__ = ['potionNames']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' of '))+var.get('names2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Potion'), Js('Elixir'), Js('Flask'), Js('Draught'), Js('Philter'), Js('Tonic'), Js('Brew'), Js('Vial'), Js('Phial'), Js('Potion'), Js('Elixir'), Js('Flask'), Js('Draught'), Js('Philter')]))
var.put('names2', Js([Js('Accuracy'), Js('Agility'), Js('Agitation'), Js('Agony'), Js('Altered Minds'), Js('Amnesia'), Js('Ancestry'), Js('Ancient Secrets'), Js('Ancient Wisdom'), Js('Anger'), Js('Arachnid Venom'), Js('Arcane Protection'), Js('Auras'), Js('Awakening'), Js('Bad Fortune'), Js('Balance'), Js('Beginnings'), Js('Berserking'), Js('Blank Minds'), Js('Blessed Water'), Js('Blinding Light'), Js('Blood'), Js('Bloodlust'), Js('Blossoms'), Js('Bribery'), Js('Broken Locks'), Js('Broken Minds'), Js('Brute Force'), Js('Brutes'), Js('Camouflage'), Js('Caution'), Js('Chaos'), Js('Clairvoyance'), Js('Clean Deaths'), Js('Cloud Walking'), Js('Comfort'), Js('Concentration'), Js('Conflicts'), Js('Control'), Js('Corruption'), Js('Cure Disease'), Js('Curing'), Js('Dark Waters'), Js('Dawn'), Js('Death'), Js('Defense'), Js('Delays'), Js('Deliriousness'), Js('Delusion'), Js('Demons'), Js('Depression'), Js('Depressions'), Js('Desires'), Js('Destruction'), Js('Disabling'), Js('Discretion'), Js('Disease'), Js('Disruption'), Js('Distractions'), Js('Domination'), Js('Doubt'), Js('Dream Inducement'), Js('Dream Vision'), Js('Dreamless Sleeps'), Js('Dreams'), Js('Dusk'), Js('Earth'), Js('Ecstasy'), Js('Efficiency'), Js('Empowerment'), Js('Endings'), Js('Endless Time'), Js('Energy'), Js('Enhanced Luck'), Js('Enhanced Reflexes'), Js('Enhanced Senses'), Js('Enhanced Sight'), Js('Enhanced Sleep'), Js('Escapes'), Js('Eternal Rage'), Js('Eternal Sleep'), Js('Excitement'), Js('Explosions'), Js('Failure'), Js('Farsight'), Js('Feather Weight'), Js('Fevers'), Js('Fire'), Js('Fire Protection'), Js('Fire Resistance'), Js('Firepower'), Js('Fireworks'), Js('Fixation'), Js('Flight'), Js('Focus'), Js('Foresight'), Js('Forgetfulness'), Js('Fortitude'), Js('Free Will'), Js('Freedom'), Js('Frozen Blood'), Js('Fury'), Js('Ghostly Essence'), Js('Ghosts'), Js('Giant Growth'), Js('Giants'), Js('Gills'), Js('Godly Powers'), Js('Good Fortune'), Js('Greed'), Js('Growth'), Js('Guilt'), Js('Hallucination'), Js('Happiness'), Js('Harmony'), Js('Haste'), Js('Hatred'), Js('Healing'), Js('Health'), Js('Hidden Talents'), Js('Holy Protection'), Js('Honesty'), Js('Hunger'), Js('Hysteria'), Js('Idle Minds'), Js('Ignorance'), Js('Illusions'), Js('Immobilizing'), Js('Immolation'), Js('Immortality'), Js('Imperfection'), Js('Impotence'), Js('Incapacitate'), Js('Influence'), Js('Insanity'), Js('Insight'), Js('Insomnia'), Js('Instincts'), Js('Intellect'), Js('Intuition'), Js('Invisibility'), Js('Invulnerability'), Js('Iron Skin'), Js('Jealousy'), Js('Joy'), Js('Justice'), Js('Knowledge'), Js('Lies'), Js('Light Feet'), Js('Lightning'), Js('Lightning Speed'), Js("Lion's Roar"), Js("Lion's Strength"), Js('Lockpicking'), Js('Love'), Js('Lucid Dreams'), Js('Luck'), Js('Lunacy'), Js('Lust'), Js('Madness'), Js('Mageblood'), Js('Might'), Js('Mind Control'), Js('Mindbending'), Js('Mirrors'), Js('Misery'), Js('Moonlight'), Js('Mortality'), Js('Nature'), Js('Neglect'), Js('Night Vision'), Js('Nightmares'), Js('Nightvision'), Js('Nimble Feet'), Js('Oblivion'), Js('Open Minds'), Js('Pain'), Js('Pain Relief'), Js('Paralyzed Minds'), Js('Paralyzing'), Js('Patience'), Js('Peace of Mind'), Js('Perception'), Js('Perfection'), Js('Petrification'), Js('Phantoms'), Js('Pheromones'), Js('Pleasure'), Js('Poisons'), Js('Potency'), Js('Precision'), Js('Predictions'), Js('Premonition'), Js('Protection'), Js('Pure Deaths'), Js('Purification'), Js('Putrefication'), Js('Rage'), Js('Reality'), Js('Redemption'), Js('Reflexes'), Js('Rejuvenation'), Js('Remembrance'), Js('Repair'), Js('Resist Fire'), Js('Restriction'), Js('Revelations'), Js('Reversed Growth'), Js('Reversed Time'), Js('Rose Petals'), Js('Scrutiny'), Js('Secrets'), Js('Seduction'), Js('Serenity'), Js('Serpent Venom'), Js('Shielding'), Js('Shrinking'), Js('Silence'), Js('Sleep Inducement'), Js('Slowing'), Js('Smoke'), Js('Solutions'), Js('Soothe Mind'), Js('Sorrow'), Js('Souls'), Js('Speed'), Js('Spellpower'), Js('Steelskin'), Js('Storms'), Js('Strength'), Js('Strong Impulses'), Js('Stunning'), Js('Stupidity'), Js('Sunlight'), Js('Swiftness'), Js('Thirst'), Js('Thunder'), Js('Time'), Js('Titanic Strength'), Js('Tranquillity'), Js('Transcendence'), Js('Truth'), Js('Twilight'), Js('Unconsciousness'), Js('Vampire Blood'), Js('Vampiric Blood'), Js('Victory'), Js('Vigor'), Js('Virtues'), Js('Vision Inducement'), Js('Visions'), Js('Vitality'), Js('War'), Js('Warmth'), Js('Water Breathing'), Js('Water Walking'), Js('Weakness'), Js('Wealth'), Js('Wind'), Js('Wisdom'), Js('the Alchemist'), Js('the Ancestors'), Js('the Arcane'), Js('the Archer'), Js('the Archmage'), Js('the Bear'), Js('the Beginning'), Js('the Berserker'), Js('the Blind'), Js('the Crown'), Js('the Deaf'), Js('the Eclipse'), Js('the Elements'), Js('the End'), Js('the Enhanced Mind'), Js('the Enigma'), Js('the Forest'), Js('the Giant'), Js('the Guru'), Js('the Healer'), Js('the High Mage'), Js('the King'), Js('the Knight'), Js('the Lion'), Js('the Master'), Js('the Mind'), Js('the Moon'), Js('the Mountain'), Js('the Mute'), Js('the Oracle'), Js('the Paragon'), Js('the Phoenix'), Js('the Sages'), Js('the Seer'), Js('the Senses'), Js('the Shadows'), Js('the Sloth'), Js('the Spirit'), Js('the Storm'), Js('the Subconscious'), Js('the Sun'), Js('the Titans'), Js('the Undead'), Js('the Unknown'), Js('the Void'), Js('the Volcano'), Js('the Wolf')]))
pass
pass


# Add lib to the module scope
potionNames = var.to_python()
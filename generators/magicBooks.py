__all__ = ['magicBooks']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            if (var.get('i')<Js(3.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*Js(3.0))|Js(0.0)))
                if PyJsStrictEq(var.get('rnd3'),Js(0.0)):
                    var.put('nmL', var.get('nm1').get(((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0))))
                else:
                    if PyJsStrictEq(var.get('rnd3'),Js(1.0)):
                        var.put('nmL', var.get('nm2').get(((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0))))
                    else:
                        var.put('nmL', var.get('nm3').get(((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0))))
                var.put('names', ((var.get('nm7').get(var.get('rnd2'))+Js(' '))+var.get('nmL')))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+Js(' '))+var.get('nm7').get(var.get('rnd2')))+Js(' '))+var.get('nm8').get(var.get('rnd3')))+Js(' '))+var.get('nm4').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        var.put('names', ((((var.get('nm4').get(var.get('rnd'))+Js(' of '))+var.get('nm8').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                        var.put('rnd3', ((var.get('Math').callprop('random')*Js(3.0))|Js(0.0)))
                        if PyJsStrictEq(var.get('rnd3'),Js(0.0)):
                            var.put('nmL', var.get('nm1').get(((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0))))
                        else:
                            if PyJsStrictEq(var.get('rnd3'),Js(1.0)):
                                var.put('nmL', var.get('nm2').get(((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0))))
                            else:
                                var.put('nmL', var.get('nm3').get(((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0))))
                        var.put('names', ((var.get('nm8').get(var.get('rnd'))+Js(' '))+var.get('nmL')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Dragons'), Js('Fae'), Js('Fairies'), Js('Alicorns'), Js('Unicorns'), Js('Griffins'), Js('Pixies'), Js('Hippogriffs'), Js('Jackalopes'), Js('Kelpies'), Js('Vampires'), Js('Vampiric Creatures'), Js('Phoenixes'), Js('Roc'), Js('Cockatrice'), Js('Sirin'), Js('Tengu'), Js('Harpies'), Js('Minotaurs'), Js('Centaurs'), Js('Hellhounds'), Js('Demons'), Js('Minor Demons'), Js('Lesser Demons'), Js('Werewolves'), Js('Satyrs'), Js('Fauns'), Js('Pegasi'), Js('Chimeras'), Js('Manticores'), Js('Hippocamps'), Js('Sirens'), Js('Nature Spirits'), Js('Nymphs'), Js('Goblins'), Js('Bunyips'), Js('Wolpertingers'), Js('Moon Rabbits'), Js('Basilisks'), Js('Wyverns'), Js('Drakes'), Js('Gorgons'), Js('Hydras'), Js('Naga'), Js('Lamia'), Js('Kappa'), Js('Cyclopses'), Js('Giants'), Js('Brownies'), Js('Banshees'), Js('Gnomes'), Js('Golems'), Js('Gnolls'), Js('Gargoyles'), Js('Ents'), Js('Elementals'), Js('Dryads'), Js('Dragonkin'), Js('Lizardfolk'), Js('Merfolk'), Js('Kobolds'), Js('Imps'), Js('Ogres'), Js('Trolls')]))
var.put('nm2', Js([Js('Fungi'), Js('Herbs'), Js('Trees'), Js('Flowers'), Js('Plants'), Js('Shrubs'), Js('Roots'), Js('Petals'), Js('Blossoms'), Js('Aquatic Plants'), Js('Aquatic Flora'), Js('Flora'), Js('Crystals'), Js('Cave Crystals')]))
var.put('nm3', Js([Js('Alchemy'), Js('Arcane Familiars'), Js('Arithmancy'), Js('Astral Projection'), Js('Astronomy'), Js('Blood Magic'), Js('Charms'), Js('Chi'), Js('Chi Bending'), Js('Chronomancy'), Js('Clairvoyance'), Js('Conjuration'), Js('Counter-Curses'), Js('Cryomancy'), Js('Curse Protection'), Js('Curses'), Js('Dark Arts'), Js('Defensive Arts'), Js('Dispelling'), Js('Divination'), Js('Dreams'), Js('Elemental Magic'), Js('Emotional Sorcery'), Js('Healing Rituals'), Js('Illusions'), Js('Jinxes'), Js('Lucid Dreams'), Js('Lunar Magic'), Js('Magical Companions'), Js('Medimagic'), Js('Mutations'), Js('Necromancy'), Js('Omens'), Js('Permutations'), Js('Portals'), Js('Potions'), Js('Projections'), Js('Pyromancy'), Js('Rituals'), Js('Runes'), Js('Solar Magic'), Js('Spellcasting'), Js('Summoning'), Js('Technomancy'), Js('Teleportation'), Js('Transfigurations'), Js('Transformations'), Js('Transmutations'), Js('Voiceless Spellcasting'), Js('Wandless Spellcasting'), Js('Warding')]))
var.put('nm4', Js([Js('Accidents'), Js('Areas'), Js('Castles'), Js('Celebrations'), Js('Ceremonies'), Js('Devices'), Js('Displays'), Js('Exhibitions'), Js('Festivals'), Js('Gadgets'), Js('History'), Js('Holidays'), Js('Incidents'), Js('Innovations'), Js('Inventions'), Js('Libraries'), Js('Locations'), Js('Memorials'), Js('Milestones'), Js('Performances'), Js('Permutations'), Js('Phenomena'), Js('Ruins'), Js('Sights'), Js('Sites'), Js('Spectacles'), Js('Towers'), Js('Triumphs'), Js('Wonders')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('Abridged'), Js('Advanced'), Js('Basic'), Js('Beginner'), Js('Compact'), Js('Companion'), Js('Complete'), Js('Complex'), Js('Comprehensive'), Js('Core'), Js('Definitive'), Js('Detailed'), Js('Effective'), Js('Elemental'), Js('Essential'), Js('Extensive'), Js('Fundamental'), Js('Intermediate'), Js('New'), Js('Newbie'), Js('Novice'), Js('Pocket'), Js('Portable'), Js('Practical'), Js('Standard'), Js('Unabridged'), Js('Vital')]))
var.put('nm6', Js([Js('Arcane'), Js('Challenging'), Js('Cursed'), Js('Dangerous'), Js('Delicate'), Js('Demanding'), Js('Difficult'), Js('Divine'), Js('Ethereal'), Js('Fragile'), Js('Holy'), Js('Legendary'), Js('Magical'), Js('Mild'), Js('Mythical'), Js('Novice'), Js('Popular'), Js('Potent'), Js('Powerful'), Js('Precious'), Js('Rare'), Js('Strange'), Js('Uncommon'), Js('Unholy'), Js('Unusual')]))
var.put('nm7', Js([Js('Details of'), Js('Information on'), Js('Guide to'), Js('Dangers of'), Js('Handbook of'), Js('Guidebook of'), Js('Compendium of'), Js('Fundamentals of'), Js('Risks of'), Js('Stories of'), Js('Advice on'), Js('Data on')]))
var.put('nm8', Js([Js('Abnormal'), Js('Ancient'), Js('Arcane'), Js('Bizarre'), Js('Brilliant'), Js('Common'), Js('Dangerous'), Js('Deadly'), Js('Delightful'), Js('Distant'), Js('Dynamic'), Js('Enchanted'), Js('Enchanting'), Js('Ethereal'), Js('Evasive'), Js('Everlasting'), Js('Exotic'), Js('Extinct'), Js('Fabulous'), Js('Famous'), Js('Fantastic'), Js('Favorite'), Js('Fierce'), Js('Forgotten'), Js('Frozen'), Js('Gentle'), Js('Grand'), Js('Grave'), Js('Great'), Js('Grim'), Js('Harmless'), Js('Hidden'), Js('Infamous'), Js('Interesting'), Js('Juvenile'), Js('Lost'), Js('Magic'), Js('Magical'), Js('Magnificent'), Js('Mighty'), Js('Mysterious'), Js('Mystical'), Js('Mythical'), Js('Nocturnal'), Js('Outlandish'), Js('Popular'), Js('Powerful'), Js('Protected'), Js('Rare'), Js('Scaly'), Js('Secret'), Js('Simple'), Js('Spiritual'), Js('Strange'), Js('Uncommon'), Js('Unique'), Js('Unknown'), Js('Unseen'), Js('Unwelcome'), Js('Vicious'), Js('Vital'), Js('Volatile'), Js('Weird'), Js('Wild')]))
pass
pass


# Add lib to the module scope
magicBooks = var.to_python()
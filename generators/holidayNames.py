__all__ = ['holidayNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd1'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', ((var.get('names2').get(var.get('rnd'))+Js(' of '))+var.get('names3').get(var.get('rnd1'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('All Souls'), Js('Ancestor'), Js('Animal'), Js('Armistice'), Js('Art'), Js('Autumn'), Js('Beer'), Js('Bliss'), Js('Bounty'), Js('Bravery'), Js('Bread'), Js('Brew'), Js('Candle'), Js('Carnival'), Js('Cheese'), Js("Children's"), Js('Clean Water'), Js('Community'), Js('Culinary'), Js('Culture'), Js('Diversity'), Js('Dragon'), Js("Elder's"), Js('Emancipation'), Js("Emperor's"), Js("Empress'"), Js('Fairy'), Js('Family'), Js('Farming'), Js("Father's"), Js('Fertility'), Js('Fisher'), Js('Flag'), Js('Flower'), Js('Food'), Js('Friendship'), Js('Full Moon'), Js('Ghost'), Js('Harvest'), Js('Heroes'), Js('Independence'), Js('Independence'), Js("King's"), Js('Labor'), Js('Lantern'), Js('Liberation'), Js('Light'), Js('Lunar Eclipse'), Js("Martyrs'"), Js('Meat'), Js('Midsummer'), Js('Midwinter'), Js("Mother's"), Js('Music'), Js('National Flag'), Js('National Heroes'), Js('National Youth'), Js('Nature'), Js('New Moon'), Js("New Year's"), Js('Parents'), Js('Planting'), Js('Proclamation'), Js('Prosperity'), Js("Queen's"), Js('Rainbow'), Js('Recreation'), Js('Reincarnation'), Js('Relaxation'), Js('Remembrance'), Js('Republic'), Js('Respect'), Js('Science'), Js('Solar Eclipse'), Js('Solidarity'), Js('Spirit'), Js('Sport'), Js('Spring'), Js('Summer'), Js('Summer Solstice'), Js('Sunrise'), Js('Sunset'), Js("Teacher's"), Js('Traditional'), Js('Truth'), Js('Victory'), Js('Wine'), Js('Winter'), Js('Winter Solstice'), Js('Woodland')]))
var.put('names2', Js([Js('Festival'), Js('Day'), Js('Fest'), Js('Celebration'), Js('Feast')]))
var.put('names3', Js([Js('Age'), Js('All Souls'), Js('Ancestors'), Js('Animals'), Js('Armistice'), Js('Art'), Js('Ashes'), Js('Asteroids'), Js('Astronomy'), Js('Auras'), Js('Auroras'), Js('Autumn'), Js('Awe'), Js('Baking'), Js('Ballet'), Js('Beer'), Js('Birds'), Js('Birth'), Js('Blacksmiths'), Js('Bliss'), Js('Blood'), Js('Blossoms'), Js('Books'), Js('Bounties'), Js('Brass'), Js('Bravery'), Js('Bread'), Js('Brewing'), Js('Brews'), Js('Candles'), Js('Candy'), Js('Carnival'), Js('Cats'), Js('Celebration'), Js('Champions'), Js('Cheese'), Js('Chickens'), Js('Children'), Js('Chocolate'), Js('Clean Water'), Js('Clouds'), Js('Color'), Js('Colors'), Js('Comets'), Js('Communities'), Js('Competition'), Js('Construction'), Js('Conversation'), Js('Coronations'), Js('Cows'), Js('Creativity'), Js('Culinary Arts'), Js('Culture'), Js('Dance'), Js('Danger'), Js('Darkness'), Js('Death'), Js('Diversity'), Js('Dogs'), Js('Dragons'), Js('Dreams'), Js('Earth'), Js('Elders'), Js('Emancipation'), Js('Embers'), Js('Enlightenment'), Js('Fairies'), Js('Faith'), Js('Falling Stars'), Js('Families'), Js('Farming'), Js('Farms'), Js('Fathers'), Js('Fear'), Js('Fertility'), Js('Film'), Js('Films'), Js('Fire'), Js('Fireworks'), Js('Fish'), Js('Fishermen'), Js('Flames'), Js('Flight'), Js('Flowers'), Js('Folklore'), Js('Food'), Js('Forests'), Js('Friends'), Js('Friendship'), Js('Fruits'), Js('Games'), Js('Generosity'), Js('Ghosts'), Js('Gods'), Js('Grandeur'), Js('Happiness'), Js('Harmony'), Js('Harvests'), Js('Heroes'), Js('Honey'), Js('Hope'), Js('Horses'), Js('Hospitality'), Js('Hymns'), Js('Ice'), Js('Ice And Snow'), Js('Illumination'), Js('Independence'), Js('Insects'), Js('Joy'), Js('Labor'), Js('Lakes'), Js('Language'), Js('Languages'), Js('Lanterns'), Js('Laughter'), Js('Life'), Js('Light'), Js('Lights'), Js('Literature'), Js('Love'), Js('Luminescence'), Js('Magic'), Js('Meat'), Js('Medicine'), Js('Melodies'), Js('Men'), Js('Merchants'), Js('Midsummer'), Js('Midwinter'), Js('Miracles'), Js('Mirrors'), Js('Mothers'), Js('Mountains'), Js('Music'), Js('Names'), Js('National Heroes'), Js('Nations'), Js('Nature'), Js('New Life'), Js('Nightfall'), Js('Nightmares'), Js('Nights'), Js('Oceans'), Js('Ores'), Js('Our Flag'), Js('Our Freedom'), Js('Our Liberation'), Js('Paint'), Js('Parents'), Js('Parks'), Js('Peace'), Js('People'), Js('Petals'), Js('Pigs'), Js('Planting'), Js('Politics'), Js('Pollination'), Js('Proclamation'), Js('Prophets'), Js('Prosperity'), Js('Rainbows'), Js('Recreation'), Js('Reflection'), Js('Reincarnation'), Js('Relaxation'), Js('Remembrance'), Js('Respect'), Js('Rest'), Js('Resting Spirits'), Js('Restoration'), Js('Rivers'), Js('Safety'), Js('Sales'), Js('Science'), Js('Seafood'), Js('Seasons'), Js('Seeds'), Js('Serenity'), Js('Service'), Js('Shadows'), Js('Silence'), Js('Sleep'), Js('Snow'), Js('Solidarity'), Js('Solstices'), Js('Sound'), Js('Spirits'), Js('Sport'), Js('Sports'), Js('Spring'), Js('Strangers'), Js('Strength'), Js('Sugar'), Js('Summer'), Js('Superstitions'), Js('Taverns'), Js('Teachers'), Js('Technology'), Js('The Arts'), Js('The Bees'), Js('The Emperor'), Js('The Empress'), Js('The First Born'), Js('The First Moon'), Js('The Forest'), Js('The Full Moon'), Js('The God'), Js('The Goddess'), Js('The Gods'), Js('The King'), Js('The Lunar Eclipse'), Js('The Martyr'), Js('The Media'), Js('The Mountain'), Js('The National Flag'), Js('The New Moon'), Js('The New Rain'), Js('The New Sunrise'), Js('The New Sunset'), Js('The New Year'), Js('The Night'), Js('The Ocean'), Js('The Phoenix'), Js('The Prophet'), Js('The Queen'), Js('The Republic'), Js('The Sea'), Js('The Seafarer'), Js('The Solar Eclipse'), Js('The Stars'), Js('The Summer Solstice'), Js('The Virgin'), Js('The Volcano'), Js('The Wind'), Js('The Winter Solstice'), Js('Time'), Js('Titans'), Js('Trade'), Js('Traditions'), Js('Tranquility'), Js('Trees'), Js('Truth'), Js('Unity'), Js('Vegetables'), Js('Victory'), Js('Voices'), Js('Warmth'), Js('Water'), Js('Waves'), Js('Whispers'), Js('Wine'), Js('Winter'), Js('Women'), Js('Wonders'), Js('Wood'), Js('Worship'), Js('Writing'), Js('Youth')]))
pass
pass


# Add lib to the module scope
holidayNames = var.to_python()
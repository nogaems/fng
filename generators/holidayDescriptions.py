__all__ = ['holidayDescriptions']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'br', 'nm5', 'nameGen', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['rnd5a', 'rnd3', 'rnd4', 'name', 'rnd5c', 'name2', 'rnd5d', 'rnd7', 'name3', 'rnd5b', 'result', 'rnd1', 'rnd2', 'rnd6'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(3.0)):
        try:
            var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
            var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
            var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
            var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
            var.put('rnd5a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            var.put('rnd5b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            while PyJsStrictEq(var.get('rnd5a'),var.get('rnd5b')):
                var.put('rnd5b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            var.put('rnd5c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            while (PyJsStrictEq(var.get('rnd5a'),var.get('rnd5c')) or PyJsStrictEq(var.get('rnd5b'),var.get('rnd5c'))):
                var.put('rnd5c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            var.put('rnd5d', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            while ((PyJsStrictEq(var.get('rnd5a'),var.get('rnd5d')) or PyJsStrictEq(var.get('rnd5b'),var.get('rnd5d'))) or PyJsStrictEq(var.get('rnd5c'),var.get('rnd5d'))):
                var.put('rnd5d', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
            var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
            def PyJs_LONG_0_(var=var):
                return ((((((((((((Js('Every ')+var.get('nm1').get(var.get('rnd1')))+Js(' the Festival of '))+var.get('nm2').get(var.get('rnd2')))+Js(' is celebrated with '))+var.get('nm3').get(var.get('rnd3')))+Js(". It's a holiday with "))+var.get('nm4').get(var.get('rnd4')))+Js(' roots, but today it is mostly associated with '))+var.get('nm5').get(var.get('rnd5a')))+Js(', '))+var.get('nm5').get(var.get('rnd5b')))+Js(', '))
            var.put('name', ((((PyJs_LONG_0_()+var.get('nm5').get(var.get('rnd5c')))+Js(' and '))+var.get('nm5').get(var.get('rnd5d')))+Js('.')))
            var.put('name2', ((((Js('It is officially celebrated for ')+var.get('nm6').get(var.get('rnd6')))+Js(', but '))+var.get('nm7').get(var.get('rnd7')))+Js('.')))
            var.put('name3', Js(''))
            if (var.get('i')<Js(2.0)):
                var.put('name3', Js('------------------------------------------'))
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<Js(3.0)):
                try:
                    pass
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('year'), Js('2 years'), Js('9 months'), Js('6 months'), Js('4 months')]))
var.put('nm2', Js([Js('Age'), Js('All Souls'), Js('Ancestors'), Js('Animals'), Js('Art'), Js('Ashes'), Js('Asteroids'), Js('Auras'), Js('Auroras'), Js('Awe'), Js('Baking'), Js('Ballet'), Js('Beer'), Js('Birds'), Js('Birth'), Js('Bliss'), Js('Blossoms'), Js('Books'), Js('Bounties'), Js('Brass'), Js('Bravery'), Js('Bread'), Js('Brewing'), Js('Brews'), Js('Candles'), Js('Candy'), Js('Carnival'), Js('Cats'), Js('Champions'), Js('Cheese'), Js('Chickens'), Js('Children'), Js('Chocolate'), Js('Clouds'), Js('Color'), Js('Comets'), Js('Communities'), Js('Competition'), Js('Construction'), Js('Coronations'), Js('Cows'), Js('Creativity'), Js('Culinary Arts'), Js('Culture'), Js('Dance'), Js('Darkness'), Js('Death'), Js('Diversity'), Js('Dogs'), Js('Dragons'), Js('Dreams'), Js('Earth'), Js('Elders'), Js('Embers'), Js('Enlightenment'), Js('Fairies'), Js('Faith'), Js('Falling Stars'), Js('Families'), Js('Farming'), Js('Fear'), Js('Fertility'), Js('Film'), Js('Fire'), Js('Fireworks'), Js('Fish'), Js('Flames'), Js('Flight'), Js('Flowers'), Js('Folklore'), Js('Food'), Js('Forests'), Js('Friends'), Js('Friendship'), Js('Fruits'), Js('Games'), Js('Generosity'), Js('Ghosts'), Js('Gods'), Js('Grandeur'), Js('Happiness'), Js('Harmony'), Js('Harvests'), Js('Heroes'), Js('Honey'), Js('Hope'), Js('Horses'), Js('Hospitality'), Js('Hymns'), Js('Ice'), Js('Ice and Snow'), Js('Independence'), Js('Insects'), Js('Joy'), Js('Lakes'), Js('Languages'), Js('Lanterns'), Js('Laughter'), Js('Life'), Js('Light'), Js('Lights'), Js('Literature'), Js('Love'), Js('Luminescence'), Js('Magic'), Js('Meat'), Js('Melodies'), Js('Merchants'), Js('Miracles'), Js('Mirrors'), Js('Mountains'), Js('Music'), Js('Names'), Js('Nations'), Js('Nature'), Js('New Life'), Js('Nightfall'), Js('Nights'), Js('Oceans'), Js('Paint'), Js('Parents'), Js('Parks'), Js('Peace'), Js('Petals'), Js('Pigs'), Js('Planting'), Js('Prophets'), Js('Prosperity'), Js('Rainbows'), Js('Recreation'), Js('Reflection'), Js('Reincarnation'), Js('Relaxation'), Js('Remembrance'), Js('Respect'), Js('Rest'), Js('Restoration'), Js('Rivers'), Js('Seafood'), Js('Seeds'), Js('Serenity'), Js('Shadows'), Js('Silence'), Js('Sleep'), Js('Snow'), Js('Solidarity'), Js('Solstices'), Js('Sound'), Js('Spirits'), Js('Sports'), Js('Strangers'), Js('Strength'), Js('Sugar'), Js('Superstitions'), Js('Taverns'), Js('Technology'), Js('Time'), Js('Titans'), Js('Trade'), Js('Tranquility'), Js('Trees'), Js('Truth'), Js('Unity'), Js('Victory'), Js('Voices'), Js('Warmth'), Js('Water'), Js('Waves'), Js('Whispers'), Js('Wine'), Js('Wonders'), Js('Wood'), Js('Worship'), Js('Writing'), Js('Youth')]))
var.put('nm3', Js([Js('great pleasure'), Js('much enthusiasm'), Js('great participation'), Js('a lot of anticipation'), Js('pure delight'), Js('enchanted hearts'), Js('much gratification'), Js('a lot of gusto'), Js('great expectations'), Js('many preparations'), Js('high hopes'), Js('eager participation'), Js('a lot of fascination'), Js('much bewilderment'), Js('excited hearts'), Js('awe and wonder'), Js('much creativity'), Js('big imaginations'), Js('grandeur'), Js('much joy')]))
var.put('nm4', Js([Js('age-old'), Js('ancient'), Js('archaic'), Js('distant'), Js('divine'), Js('fairly modern'), Js('long established'), Js('long-lived'), Js('mysterious'), Js('mystical'), Js('mythical'), Js('relatively young'), Js('religious'), Js('seemingly ancient'), Js('spiritual'), Js('time lost'), Js('time-honored'), Js('undiscovered'), Js('unknown'), Js('untold')]))
var.put('nm5', Js([Js('acts of courage'), Js('athletic competitions'), Js('bonding with family'), Js('bonding with friends'), Js('celebrating imagination'), Js('charitable donations'), Js('colorful lights'), Js('coming of age rituals'), Js('costumed mascots'), Js('creating charity gift baskets'), Js('creation of art'), Js('dance parties'), Js('decorating homes'), Js('decorating the streets'), Js('exchanging gifts'), Js('face painting'), Js('fireworks'), Js('forgiving others'), Js('gag gifts'), Js('games of chance'), Js('giving compliments'), Js('going out for dinner'), Js('group games'), Js('hanging around campfires'), Js('helping strangers'), Js('helping those in need'), Js('holiday meals'), Js('holiday related drinks'), Js('holiday themed sports games'), Js('holiday treats'), Js('homemade costumes'), Js('homemade gifts'), Js('homemade holiday decorations'), Js('hot beverages'), Js('humility'), Js('kindness for others'), Js('lighting candles'), Js('love and romance'), Js('marriage proposals'), Js('neighborhood parties'), Js('night walks'), Js('outdoor food parties'), Js('parades'), Js('playing board games'), Js('playing instruments'), Js('playing pranks'), Js('playing with pets'), Js('preparing big feasts'), Js('preparing holiday themed foods'), Js('random acts of kindness'), Js('rights of passage'), Js('romantic gestures'), Js('scavenger hunts'), Js('secret gift giving'), Js('seeing holiday movies'), Js('self discovery'), Js('singing songs'), Js('skill-based contests'), Js('spirituality'), Js('telling jokes'), Js('telling of stories'), Js('togetherness'), Js('traditional clothing'), Js('traditional dances'), Js('traditional hair styling'), Js('traditional plays'), Js('truth and dare games'), Js('watching a natural phenomena'), Js('watching special shows'), Js('wearing homemade costumes')]))
var.put('nm6', Js([Js('one day'), Js('two days'), Js('three days'), Js('four days'), Js('five days'), Js('six days'), Js('1 week'), Js('eight days'), Js('nine days'), Js('ten days'), Js('eleven days'), Js('twelve days'), Js('thirteen days'), Js('2 weeks'), Js('1 week'), Js('2 weeks')]))
var.put('nm7', Js([Js('decorations and festivities are often found well before and after that time as well'), Js('decorations are often found well before and after that time as well'), Js('it often continues well after that time as well'), Js('festivities often start earlier than that as well'), Js('the final half is often celebrated more strongly and looked forward to the most'), Js('the first half is often celebrated more strongly and looked forward to the most'), Js('the periods before and after that time are so festive it may as well be 4 weeks long'), Js('the final celebrations often lasts deep into the night and even into the next day'), Js('decorations often stay around for weeks after the celebrations'), Js('decorations are often seen weeks before the actual celebrations'), Js('a generally festive atmosphere continues to fill the streets for weeks after the celebrations'), Js('it can be both shorter and longer, depending on personal preferences'), Js('enthusiastic people often celebrate it for a few days more by starting earlier'), Js('a strong sense of community often gets people to celebrate it for a few days more'), Js('the final hours are by far the most intense and the most beloved hours'), Js('the opening hours are by far the most beloved hours and looked forward to by all'), Js('the opening ceremony is often the part with the most participation'), Js('the closing celebrations are what everybody looks forward to the most'), Js("it's not until the second half that celebrations really go all out"), Js('the climax of the celebrations are in the final hours and is what everybody looks forward to'), Js('another holiday starts soon after this one ends, resulting in a much longer period of festivities'), Js('this holiday ties in closely with another, so festivities continue for a much longer time'), Js('preparations often start weeks before, so many decorations can be seen much earlier'), Js("there's a long period of joy and satisfaction after the celebrations, adding to the festive atmosphere"), Js('many people will celebrate it longer by starting earlier and ending later')]))
var.put('br', Js([]))
pass
pass


# Add lib to the module scope
holidayDescriptions = var.to_python()
__all__ = ['farmDescriptions']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'rnd15', 'rnd11', 'nm16', 'rnd8', 'name', 'nm2b', 'nm2c', 'nm3b', 'rnd14', 'rnd', 'rnd2', 'nm3a', 'name2', 'nm14', 'nm3c', 'tp', 'nm7', 'nm10', 'nm15', 'rnd5', 'nm12', 'nm3d', 'nm5', 'rnd4', 'rnd7', 'nm2d', 'result', 'nm3e', 'nm6', 'rnd6', 'rnd13', 'nm4', 'nm2a', 'rnd3', 'nm8', 'nm2e', 'nm13', 'nm9', 'rnd10', 'rnd16', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('as far as the eye could see'), Js('all around, bordered only by the thick forests in the distance'), Js('all around, broken up only by an enormous lake at the bottom of a mountain'), Js('stretching to the horizons, divided by picket fences, and rows of bushes'), Js('everywhere, their patterns only broken up by the occasional tree left to grow in peace'), Js('everywhere, on each hill, and every slope'), Js('bathing in the sun all around'), Js('uninterrupted for as far as the eye could see'), Js('all around, interrupted only by a steep mountain cliff, which casted its shadow on the fields in the morning'), Js('far and wide, interrupted here and there by patches of forests left for local animals and plants'), Js('far and wide, broken up only by the picket fences, and rows of coniferous trees saying in the wind'), Js('far and near, each one bigger than the other'), Js('far and near, seemingly with no end beyond the horizons'), Js('all over the place, spread sporadically between the patches of forests left to grow in peace'), Js('all over the place, many of which surrounded a small lake'), Js('scattered all around, their homogeny broken up by overgrown hills of rock and boulders'), Js('stretching to the horizons, their otherwise homogenous patterns only broken up by the shadows cast by the clouds above'), Js('spread all around, curving around, and waving over hill after hill'), Js('spread far and wide, curving and zigzagging around hills and slopes'), Js('reaching for the horizons, only disappearing after rolling over the hills in the distance'), Js('stretching on forever, broken up only by a river curling and swirling its way through the landscape'), Js('as far as you could see, their view only broken by ros of trees surrounding the river flowing through this landscape'), Js('covering great lengths, their patterns forming a mosaic in the landscape'), Js('stretching over great distances, their mosaic marked further by the picket fences around them'), Js('reaching far and wide, broken up only by gutters of water inhabited by frogs and insects')]))
    var.put('nm2a', Js([Js('cows'), Js('sheep'), Js('horses'), Js('goats'), Js('deer')]))
    var.put('nm2b', Js([Js('chickens'), Js('ducks'), Js('geese'), Js('pigs'), Js('rabbits'), Js('turkeys')]))
    var.put('nm2c', Js([Js('flowers'), Js('bean plants'), Js('soy plants'), Js('canola'), Js('safflower'), Js('flax'), Js('buckwheat'), Js('lavender'), Js('barley'), Js('corn'), Js('millet'), Js('oats'), Js('onions'), Js('potato plants'), Js('rye'), Js('sugar cane'), Js('sunflowers'), Js('wheat'), Js('rice plants')]))
    var.put('nm2d', Js([Js('Brussel sprouts'), Js('artichokes'), Js('beetroots'), Js('beets'), Js('broccoli'), Js('cabbages'), Js('carrots'), Js('cauliflowers'), Js('celery'), Js('chards'), Js('cucumbers'), Js('garlic plants'), Js('kale'), Js('melons'), Js('onions'), Js('potato plants'), Js('pumpkins'), Js('scallions'), Js('spinach'), Js('strawberries'), Js('turnips')]))
    var.put('nm2e', Js([Js('orchards'), Js('vineyards'), Js('plantations')]))
    var.put('nm3a', Js([Js('frolicked and foraged'), Js('frolicked and loitered'), Js('gently grazed'), Js('gently grazed and ran'), Js('grazed and lounged'), Js('ran and frolicked'), Js('ran and lounged'), Js('rested and grazed'), Js('slept and grazed'), Js('slepts and loitered')]))
    var.put('nm3b', Js([Js('scavenged and strolled'), Js('strolled and fed'), Js('strolled and sunbathed'), Js('grazed and scavenged'), Js('strolled and loitered'), Js('rummaged and scavenged'), Js('sunbathed and loitered'), Js('lolled and grazed'), Js('wandered and grazed'), Js('slepts and loitered')]))
    var.put('nm3c', Js([Js('swayed in the wind'), Js('waved back and forth in the wind'), Js('grew to tall heights'), Js('dominated'), Js('covered'), Js('grew gently'), Js('flourished'), Js('thrived'), Js('rustled in the wind'), Js('bustled with insects and birds')]))
    var.put('nm3d', Js([Js('decorated'), Js('dominated'), Js('bustled with insects and birds'), Js('blossomed'), Js('flourished'), Js('dotted'), Js('entertained bees and other insects'), Js('carpeted'), Js('spread across'), Js('sprinkled')]))
    var.put('nm3e', Js([Js('swayed in the wind'), Js('bustled with birds and insects'), Js('entertained bees and insects'), Js('housed birds of all kinds'), Js('waved back and forth in the wind'), Js('rustled in the wind'), Js('dominated'), Js('blossomed'), Js('flourished'), Js('grew gently')]))
    var.put('nm4', Js([Js('breezy'), Js('gentle'), Js('hushed'), Js('isolated'), Js('luscious'), Js('lush'), Js('open'), Js('opulent'), Js('peaceful'), Js('quiet'), Js('radiant'), Js('secluded'), Js('serene'), Js('silent'), Js('sunlit'), Js('sunny'), Js('tranquil'), Js('verdant'), Js('wide open'), Js('windy')]))
    var.put('nm5', Js([Js('along the edge of the fields'), Js('amidst the many fields'), Js('burrowing its way through and around the many fields'), Js('crossing straight through the landscape'), Js('curving and slithering through the landscape'), Js('looping around most fields'), Js('making its way through some of the fields'), Js('passing around many of the fields'), Js('passing field after field'), Js('passing through the various fields'), Js('right in the center of the fields'), Js('snaking its way through the landscape'), Js('touring around most fields')]))
    var.put('nm6', Js([Js('a dusty'), Js('a dusty old'), Js('a dusty, gravel'), Js('a grass-covered, cobblestone'), Js('a grass-covered, gravel'), Js('a gravelly'), Js('a mossy, cobblestone'), Js('a muddy'), Js('a sandy'), Js('a weathered, cobblestone'), Js('a weed-ridden, cobblestone'), Js('a weed-ridden, dusty old'), Js('a weed-ridden, gravel'), Js('a weed-ridden, sandy'), Js('an old cobblestone'), Js('an overgrown, cobblestone'), Js('an overgrown, dusty'), Js('an overgrown, dusty old'), Js('an overgrown, stone')]))
    var.put('nm7', Js([Js('ended at'), Js('eventually arrived at'), Js('eventually reached'), Js('lead to'), Js('made its way to'), Js('stopped at')]))
    var.put('nm8', Js([Js('a picturesque'), Js('a charming'), Js('a beautiful'), Js('a scenic'), Js('a pleasant'), Js('a tremendous'), Js('a vast'), Js('a modest'), Js('an extensive'), Js('an immense'), Js('a humble'), Js('a quiet'), Js('a simple'), Js('a typical'), Js('an ordinary'), Js('a classic'), Js('a traditional')]))
    var.put('nm9', Js([Js('ranch'), Js('farmhouse'), Js('mansion'), Js('estate'), Js('farmhouse'), Js('farmhouse')]))
    var.put('nm10', Js([Js("after passing a billboard with the farm's name and logo"), Js('after passing a rickety welcome sign'), Js("after passing a sign with the farm's name"), Js('after passing a simple welcome sign'), Js('covered in vines and wall shrubs'), Js('covered in wall flowers'), Js('eclipsed by the flower covered seating area next to it'), Js('eclipsed by the stunning pagoda in the back of the courtyard'), Js('guarded by a sleepy, old dog'), Js('guarded by honking geese'), Js('guarded by several excited dogs'), Js('overshadowed by a giant tree in the center of the courtyard'), Js('overshadowed by several enormous oak trees'), Js('overshadowed completely by the floral pergola right next to it'), Js('surrounded by a tall hedge'), Js('surrounded by a wooden fence'), Js('surrounded by an old, stone wall'), Js('with a huge courtyard'), Js('with a modest courtyard'), Js('with a vast courtyard')]))
    var.put('nm12', Js([Js('A chicken coop stood next to the house'), Js('A giant barn housed the hay for the winter'), Js('A giant barn housed various animals'), Js('A giant silo was filled with grains'), Js('A huge stable housed dozens of horses'), Js('A humble stable housed a couple of horses'), Js('A large barn housed livestock durinng harsher weather'), Js('A large granary held an ample supply of animal feed'), Js('A long row of silos was filled with various grains'), Js('A milking facility stood in the corner of the courtyard'), Js('A tall silo was filled with silage'), Js('Several barns housed the various livestock at night'), Js('Several barns provided shelter to livestock'), Js('Several milk tanks were filled to the brim'), Js('Several tall silos held silage')]))
    var.put('nm13', Js([Js('a couple of dogs rested under the tree in the center of the courtyard'), Js('a giant well stood just off to the side of the courtyard'), Js('a huge, blackened pit for campfires was dug at the back of the courtyard'), Js('a large, home-built barbecue stood at the edge of the courtyard'), Js('a round pen for horse training stood at the back of the courtyard'), Js('all sorts of flowers grew in the lush gardens next to buildings'), Js('an outdoor kitchen including a clay oven was built to the side of the courtyard'), Js('bees buzzed all around the cacaphony of flowers near the entrance'), Js('birds bathed in the large fountain near the entrance'), Js('chickens rummaged all around the courtyard'), Js('dozens of swallows had made their nests under the rooftop gutters'), Js('farm machinery was scattered all around the courtyard'), Js('large tractors were parked beneath a rickety roof'), Js('pigeons cooed on the roofs of the farm'), Js('piles and piles of logs were stacked against the walls of the farm'), Js('several beehives stood just behind the main buildings')]))
    var.put('nm14', Js([Js('a large pond full of fish attracted cats to the side of the courtyard'), Js('a large windmill could be seen over the rooftops, its blades going round and round in the wind'), Js('a small guesthouse stood to the side of the main farmhouse like a miniature copy'), Js('a small pen housing a couple of chickens, rabbits, and other small animals was almost hidden in a corner'), Js('a small plot of land was used for a breathtaking flower garden'), Js('a small plot of land was used for a private vegetable garden'), Js('a small seating area provided a resting place for those enjoying some of the products sold right here on the farm'), Js('a small shed with all sorts of small projects and inventions stood lost in a corner'), Js('a small wind turbine charged a generator at the back of the farm'), Js("a stork's nest could be seen atop the silo roof"), Js('a well kept greenhouse stood at the back, filled with all sorts of fruit and vegetable plants'), Js('an old greenhouse stood to the side of the courtyard, no longer used, and with a few cracked glass panes'), Js('dozens of frogs living in a small pond to the side filled the air with croaks and splashes'), Js('several grape vines climbed their way up and over the open gazebo to the side of the courtyard'), Js('the smell of compost hung in the air despite the hidden location of the bin behind the granary'), Js('a few rows of solar pannels stood just beyond the courtyard')]))
    var.put('nm15', Js([Js('charming'), Js('cheerful'), Js('comforting'), Js('comfy'), Js('cozy'), Js('delightful'), Js('familiar'), Js('freeing'), Js('friendly'), Js('homely'), Js('homey'), Js('mellow'), Js('peaceful'), Js('pleasant'), Js('pleasing'), Js('serene'), Js('snug'), Js('soothing'), Js('tranquil'), Js('welcoming')]))
    var.put('nm16', Js([Js('closing your eyes you could feel the sun rays on your skin, the gentle breeze through your hair, and you could hear the distant sounds of all sorts of animals'), Js('it could be felt in everything from the landscape to the farmhouse itself'), Js('it was a combination of the tranquil landscape, and the isolation of the farm within these lush fields'), Js("it was one of those farms you'd gladly spend an entire summer at"), Js('mainly thanks to the smell of home cooked food clinging to the air'), Js('much of this was thanks to how stereotypical the farmhouse looked, it made everything seem commonplace'), Js('much of this was thanks to the smells of ripe fruits carried by the wind, and the sounds of birds chirping in the trees'), Js('the beauty of the landscape only added to this'), Js('the sounds of nature, the creeking of wood of the farm buildings, and the serenity of nature all around contributed greatly to this'), Js('the warm sunrays, and the gentle breeze were the main contributors to this'), Js('there was just something about the farm that felt very intimate and welcoming'), Js('this was largely due to the little things, like the welcome sign, the seating areas, and the overall hospitality the farmhouse radiated'), Js('which was helped by the gentle breeze carrying the scent of ripe fruits across the fields'), Js('which was mostly because of the smell of fruit pies spreading through the air'), Js('which was mostly thanks to the gentle breeze, and the sounds of nature all around')]))
    var.put('rnd1', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('tp', ((var.get('Math').get('random')*Js(5.0))|Js(0.0)))
    if PyJsStrictEq(var.get('tp'),Js(0.0)):
        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2a').get('length'))|Js(0.0)))
        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2a').get('length'))|Js(0.0)))
        while PyJsStrictEq(var.get('rnd'),var.get('rnd2')):
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2a').get('length'))|Js(0.0)))
        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3a').get('length'))|Js(0.0)))
        var.put('tFrm', ((((var.get('nm2a').get(var.get('rnd'))+Js(' and '))+var.get('nm2a').get(var.get('rnd2')))+Js(' '))+var.get('nm3a').get(var.get('rnd3'))))
    else:
        if PyJsStrictEq(var.get('tp'),Js(1.0)):
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2b').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2b').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('rnd'),var.get('rnd2')):
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2b').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3b').get('length'))|Js(0.0)))
            var.put('tFrm', ((((var.get('nm2b').get(var.get('rnd'))+Js(' and '))+var.get('nm2b').get(var.get('rnd2')))+Js(' '))+var.get('nm3b').get(var.get('rnd3'))))
        else:
            if PyJsStrictEq(var.get('tp'),Js(2.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2c').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2c').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('rnd'),var.get('rnd2')):
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2c').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3c').get('length'))|Js(0.0)))
                var.put('tFrm', ((((var.get('nm2c').get(var.get('rnd'))+Js(' and '))+var.get('nm2c').get(var.get('rnd2')))+Js(' '))+var.get('nm3c').get(var.get('rnd3'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(3.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2d').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2d').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('rnd'),var.get('rnd2')):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2d').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3d').get('length'))|Js(0.0)))
                    var.put('tFrm', ((((var.get('nm2d').get(var.get('rnd'))+Js(' and '))+var.get('nm2d').get(var.get('rnd2')))+Js(' '))+var.get('nm3d').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2e').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2e').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('rnd'),var.get('rnd2')):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2e').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3e').get('length'))|Js(0.0)))
                    var.put('tFrm', ((((var.get('nm2e').get(var.get('rnd'))+Js(' and '))+var.get('nm2e').get(var.get('rnd2')))+Js(' '))+var.get('nm3e').get(var.get('rnd3'))))
    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
    var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
    var.put('rnd9', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
    var.put('rnd10', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
    var.put('rnd11', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
    var.put('rnd12', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
    var.put('rnd13', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
    var.put('rnd14', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
    var.put('rnd15', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
    var.put('rnd16', ((var.get('Math').callprop('random')*var.get('nm16').get('length'))|Js(0.0)))
    var.put('name', ((((((((((Js('There were fields ')+var.get('nm1').get(var.get('rnd1')))+Js('. All around you '))+var.get('tFrm'))+Js(' in the '))+var.get('nm4').get(var.get('rnd4')))+Js(' pastures, and '))+var.get('nm5').get(var.get('rnd5')))+Js(' ran '))+var.get('nm6').get(var.get('rnd6')))+Js(' road.')))
    def PyJs_LONG_0_(var=var):
        return (((((((((((((((Js('The road ')+var.get('nm7').get(var.get('rnd7')))+Js(' '))+var.get('nm8').get(var.get('rnd8')))+Js(' '))+var.get('nm9').get(var.get('rnd9')))+Js(' '))+var.get('nm10').get(var.get('rnd10')))+Js('. The '))+var.get('nm9').get(var.get('rnd9')))+Js(' was '))+var.get('nm11').get(var.get('rnd11')))+Js('. '))+var.get('nm12').get(var.get('rnd12')))+Js(', '))+var.get('nm13').get(var.get('rnd13')))
    var.put('name2', (((((((PyJs_LONG_0_()+Js(', and '))+var.get('nm14').get(var.get('rnd14')))+Js('. The farm had a '))+var.get('nm15').get(var.get('rnd15')))+Js(' feel to it, '))+var.get('nm16').get(var.get('rnd16')))+Js('.')))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
farmDescriptions = var.to_python()
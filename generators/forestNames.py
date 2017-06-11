__all__ = ['forestNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('i')<Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((((var.get('nm5').get(var.get('rnd'))+Js(' '))+var.get('nm6').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm4').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                            var.put('names', ((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd4')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
                        else:
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                            var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                            var.put('names', ((((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3b')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('White'), Js('Black'), Js('Brown'), Js('Gray'), Js('Majestic'), Js('Pygmy'), Js('Little'), Js('Giant'), Js('Northern'), Js('Southern'), Js('Eastern'), Js('Western'), Js('Greater'), Js('Lesser'), Js('Masked'), Js('Grass'), Js('Water'), Js('Common'), Js('Mountain'), Js('Prairie'), Js('Grassland'), Js('Taiga'), Js('Tundra'), Js('Savanna'), Js('Alpine'), Js('Collared'), Js('Grand'), Js('Pacific'), Js('Oriental'), Js('Spotted'), Js('Speckled'), Js('Striped'), Js('Dotted'), Js('Rusty'), Js('Maned'), Js('Cloud'), Js('Long-tailed'), Js('Short-tailed'), Js('Crowned'), Js('Golden'), Js('Imperial'), Js('Royal'), Js('Noble'), Js('Laughing'), Js('Lined'), Js('Banded'), Js('Snow'), Js('Ivory'), Js('Ebony'), Js('Wild'), Js('Reagal')]))
var.put('nm2', Js([Js('Panda'), Js('Gerbil'), Js('Hare'), Js('Hedgehog'), Js('Jackal'), Js('Warthog'), Js('Coyote'), Js('Cat'), Js('Badger'), Js('Hyena'), Js('Jaguar'), Js('Gorilla'), Js('Sloth'), Js('Anteater'), Js('Ocelot'), Js('Lion'), Js('Porcupine'), Js('Beaver'), Js('Otter'), Js('Ant'), Js('Bandicoot'), Js('Crocodile'), Js('Alligator'), Js('Treefrog'), Js('Wolverine'), Js('Goat'), Js('Spider'), Js('Mouse'), Js('Snail'), Js('Crab'), Js('Deer'), Js('Fox'), Js('Lizard'), Js('Toad'), Js('Mole'), Js('Turtle'), Js('Frog'), Js('Squirrel'), Js('Tortoise'), Js('Gazelle'), Js('Panther'), Js('Bear'), Js('Rat'), Js('Lynx'), Js('Okapi'), Js('Leopard'), Js('Tiger'), Js('Wolf'), Js('Rhino'), Js('Wallaby'), Js('Yak'), Js('Pelican'), Js('Swallow'), Js('Duck'), Js('Eagle'), Js('Hawk'), Js('Falcon'), Js('Vulture'), Js('Sunbird'), Js('Macaw'), Js('Woodpecker'), Js('Kingfisher'), Js('Hummingbird'), Js('Pygmy Owl'), Js('Sandpiper'), Js('Mockingbird')]))
var.put('nm3', Js([Js('Forest'), Js('Grove'), Js('Woods'), Js('Covert'), Js('Woodland'), Js('Thicket'), Js('Forest'), Js('Grove'), Js('Woods'), Js('Covert'), Js('Woodland'), Js('Wilds'), Js('Wood'), Js('Wood'), Js('Timberland'), Js('Timberland')]))
var.put('nm4', Js([Js('Calm'), Js('Sacred'), Js('Massive'), Js('Huge'), Js('Teeny'), Js('Tiny'), Js('Puny'), Js('Mammoth'), Js('Gigantic'), Js('Colossal'), Js('Big'), Js('Faint'), Js('Hissing'), Js('Quiet'), Js('Thundering'), Js('Whispering'), Js('Beautiful'), Js('Fancy'), Js('Magnificent'), Js('Mysterious'), Js('Old'), Js('Broken'), Js('Creepy'), Js('Abandoned'), Js('Light'), Js('Earthy'), Js('Elegent'), Js('Deep'), Js('Enchanted'), Js('Detailed'), Js('Deserted'), Js('Exclusive'), Js('Dramatic'), Js('Curious'), Js('Awesome'), Js('Jaded'), Js('Jagged'), Js('Incredible'), Js('Healthy'), Js('Heavenly'), Js('High'), Js('Hollow'), Js('Huge'), Js('Gentle'), Js('Giant'), Js('Glistening'), Js('Glorious'), Js('Gorgeous'), Js('Groovy'), Js('Free'), Js('Frightened'), Js('Frightening'), Js('Little'), Js('Lively'), Js('Lonely'), Js('Lush'), Js('Magical'), Js('Majestic'), Js('Marvelous'), Js('Mellow'), Js('Mighty'), Js('Misty'), Js('Moldy'), Js('Narrow'), Js('Oceanic'), Js('Quiet'), Js('Panoramic'), Js('Parallel'), Js('Peaceful'), Js('Plain'), Js('Pleasant'), Js('Precious'), Js('Private'), Js('Rainy'), Js('Reflecting'), Js('Romantic'), Js('Rotten'), Js('Royal'), Js('Terrible'), Js('Terrific'), Js('Thick'), Js('Thin'), Js('Threatening'), Js('Towering'), Js('Scattered'), Js('Secret'), Js('Sickly'), Js('Dark'), Js('Shadow'), Js('Simple'), Js('Special'), Js('Spectacular'), Js('Spiritual'), Js('Square'), Js('Round'), Js('Triangular'), Js('Stormy'), Js('Young'), Js('Wandering'), Js('Whimsical'), Js('Wicked'), Js('Wild'), Js('Windy'), Js('Wise'), Js('Wretched'), Js('Venomous'), Js('Violent'), Js('Violet'), Js('Unknown'), Js('Alien')]))
var.put('nm5', Js([Js('Jolly'), Js('Broad'), Js('Brass'), Js('Copper'), Js('Golden'), Js('Silver'), Js('Bronze'), Js('Massive'), Js('Huge'), Js('Teeny'), Js('Tiny'), Js('Puny'), Js('Mammoth'), Js('Gigantic'), Js('Colossal'), Js('Big'), Js('Quiet'), Js('Thundering'), Js('Whispering'), Js('Ancient'), Js('Beautiful'), Js('Fancy'), Js('Magnificent'), Js('Mysterious'), Js('Old'), Js('Short'), Js('Heavy'), Js('Light'), Js('Elegent'), Js('Enchanted'), Js('Exclusive'), Js('Exotic'), Js('Dramatic'), Js('Curious'), Js('Aromatic'), Js('Awesome'), Js('Imaginary'), Js('Incredible'), Js('Healthy'), Js('Heavenly'), Js('Hollow'), Js('Huge'), Js('Hypnotic'), Js('Gentle'), Js('Giant'), Js('Glistening'), Js('Glorious'), Js('Goofy'), Js('Gorgeous'), Js('Greasy'), Js('Groovy'), Js('Gruesome'), Js('Fabulous'), Js('Faded'), Js('False'), Js('Familiar'), Js('Fancy'), Js('Fantastic'), Js('Fascinating'), Js('Foolish'), Js('Fragile'), Js('Free'), Js('Frightened'), Js('Frightening'), Js('Last'), Js('Little'), Js('Lonely'), Js('Lush'), Js('Magical'), Js('Majestic'), Js('Mellow'), Js('Mighty'), Js('Misty'), Js('Minor'), Js('Misty'), Js('Moldy'), Js('Naive'), Js('Narrow'), Js('Nonstalgic'), Js('Quiet'), Js('Peaceful'), Js('Plain'), Js('Pleasant'), Js('Precious'), Js('Private'), Js('Rare'), Js('Regular'), Js('Reflecting'), Js('Royal'), Js('Tall'), Js('Terrific'), Js('Thick'), Js('Thin'), Js('Threatening'), Js('Tired'), Js('Towering'), Js('Scattered'), Js('Secret'), Js('Shaggy'), Js('Sickly'), Js('Simple'), Js('Sleepy'), Js('Special'), Js('Spectacular'), Js('Spotless'), Js('Spotted'), Js('Stormy'), Js('Young'), Js('Waiting'), Js('Wandering'), Js('Whimsical'), Js('Wicked'), Js('Wild'), Js('Windy'), Js('Wise'), Js('Wretched'), Js('Violet'), Js('Unique'), Js('Unknown'), Js('Unnatural'), Js('Alien')]))
var.put('nm6', Js([Js('Alder'), Js('Ash'), Js('Ash'), Js('Ash'), Js('Beech'), Js('Birch'), Js('Birch'), Js('Birch'), Js('Bladdernut'), Js('Buckeye'), Js('Cedar'), Js('Chestnut'), Js('Cypress'), Js('Devilwood'), Js('Dogwood'), Js('Elderberry'), Js('Elm'), Js('Fir'), Js('Harlequin'), Js('Hemlock'), Js('Hickory'), Js('Holly'), Js('Ironwood'), Js('Jacktree'), Js('Juniper'), Js('Linden'), Js('Locust'), Js('Magnolia'), Js('Maple'), Js('Maple'), Js('Maple'), Js('Maple'), Js('Musclewood'), Js('Oak'), Js('Oak'), Js('Oak'), Js('Oak'), Js('Olive'), Js('Palm'), Js('Pawpaw'), Js('Peach'), Js('Pine'), Js('Pine'), Js('Pine'), Js('Pine'), Js('Apple'), Js('Raspberry'), Js('Plum'), Js('Poplar'), Js('Redbud'), Js('Redwood'), Js('Redwood'), Js('Silverbell'), Js('Spruce'), Js('Spruce'), Js('Spruce'), Js('Spruce'), Js('Sumac'), Js('Tupelo'), Js('Walnut'), Js('Willow'), Js('Willow'), Js('Willow'), Js('Willow'), Js('Hazulnut'), Js('Blueberry'), Js('Chestnut'), Js('Blackberry'), Js('Butternut'), Js('Pecan'), Js('River'), Js('Lake'), Js('Wetland'), Js('Stream'), Js('Creek'), Js('Brook'), Js('Rivulet'), Js('Basin'), Js('Lagoon'), Js('Loch'), Js('Pond'), Js('Spring'), Js('Reservoir'), Js('Basin'), Js('Marsh'), Js('Quagmire'), Js('Swampland'), Js('Bog'), Js('Clearing'), Js('Glade'), Js('Field'), Js('Hill'), Js('Garden'), Js('Range'), Js('Territory'), Js('Meadow'), Js('Mead'), Js('Grassland'), Js('Bluff'), Js('Cliff'), Js('Highland'), Js('Knoll'), Js('Mound'), Js('Mount'), Js('Thorn')]))
var.put('nm7', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm8', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm9', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm11', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
forestNames = var.to_python()
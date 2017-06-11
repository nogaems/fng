__all__ = ['grasslandNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'names9', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names3', 'names1', 'names7'])
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
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd0'))+Js(' '))+var.get('names2').get(var.get('rnd1')))+Js(' '))+var.get('names3').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', ((var.get('names4').get(var.get('rnd1'))+Js(' '))+var.get('names3').get(var.get('rnd0'))))
                else:
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names9').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('names', ((((((var.get('names5').get(var.get('rnd0'))+var.get('names6').get(var.get('rnd1')))+var.get('names7').get(var.get('rnd2')))+var.get('names8').get(var.get('rnd3')))+var.get('names9').get(var.get('rnd4')))+Js(' '))+var.get('names3').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('White'), Js('Black'), Js('Brown'), Js('Gray'), Js('Majestic'), Js('Pygmy'), Js('Little'), Js('Giant'), Js('Northern'), Js('Southern'), Js('Eastern'), Js('Western'), Js('Greater'), Js('Lesser'), Js('Masked'), Js('Grass'), Js('Water'), Js('Common'), Js('Mountain'), Js('Prairie'), Js('Grassland'), Js('Taiga'), Js('Tundra'), Js('Savanna'), Js('Alpine'), Js('Collared'), Js('Grand'), Js('Pacific'), Js('Oriental'), Js('Spotted'), Js('Speckled'), Js('Striped'), Js('Dotted'), Js('Rusty'), Js('Maned'), Js('Cloud'), Js('Long-tailed'), Js('Short-tailed'), Js('Crowned'), Js('Golden'), Js('Imperial'), Js('Royal'), Js('Noble'), Js('Laughing'), Js('Lined'), Js('Banded'), Js('Snow'), Js('Ivory'), Js('Ebony'), Js('Wild'), Js('Reagal')]))
var.put('names2', Js([Js('Aardvark'), Js('Alpaca'), Js('Anaconda'), Js('Ant'), Js('Anteater'), Js('Antelope'), Js('Armadillo'), Js('Baboon'), Js('Badger'), Js('Bandicoot'), Js('Bat'), Js('Bear'), Js('Bee'), Js('Beetle'), Js('Bird'), Js('Bison'), Js('Boa'), Js('Buffalo'), Js('Butterfly'), Js('Buzzard'), Js('Caterpillar'), Js('Chipmunk'), Js('Cobra'), Js('Cougar'), Js('Coyote'), Js('Crane'), Js('Cricket'), Js('Crow'), Js('Deer'), Js('Dingo'), Js('Dove'), Js('Duck'), Js('Eagle'), Js('Elephant'), Js('Elk'), Js('Fox'), Js('Frog'), Js('Gazelle'), Js('Grasshopper'), Js('Groundhog'), Js('Hawk'), Js('Hedgehog'), Js('Hyena'), Js('Jackal'), Js('Kangaroo'), Js('Ladybug'), Js('Lion'), Js('Meerkat'), Js('Mouse'), Js('Rabbit'), Js('Rat'), Js('Raven'), Js('Rhino'), Js('Snake'), Js('Toad'), Js('Tortoise'), Js('Warthog'), Js('Wasp'), Js('Weasel'), Js('Wild Dog')]))
var.put('names3', Js([Js('Grasslands'), Js('Grassland'), Js('Savanna'), Js('Pastures'), Js('Plains'), Js('Prairie'), Js('Steppe'), Js('Range'), Js('Fields'), Js('Meadow'), Js('Gardens'), Js('Terrain'), Js('Territory'), Js('Expanse'), Js('Plateau'), Js('Valley')]))
var.put('names4', Js([Js('Abandoned'), Js('Awesome'), Js('Beautiful'), Js('Big'), Js('Blooming'), Js('Blossoming'), Js('Broken'), Js('Calm'), Js('Colossal'), Js('Creepy'), Js('Curious'), Js('Deep'), Js('Deserted'), Js('Detailed'), Js('Dramatic'), Js('Dry'), Js('Earthy'), Js('Elegent'), Js('Enchanted'), Js('Exclusive'), Js('Faint'), Js('Fancy'), Js('Free'), Js('Gentle'), Js('Giant'), Js('Gigantic'), Js('Glistening'), Js('Glorious'), Js('Gorgeous'), Js('Green'), Js('Groovy'), Js('Healthy'), Js('Heavenly'), Js('High'), Js('Hissing'), Js('Hollow'), Js('Huge'), Js('Incredible'), Js('Jaded'), Js('Jagged'), Js('Light'), Js('Little'), Js('Lively'), Js('Lonely'), Js('Luscious'), Js('Lush'), Js('Magical'), Js('Magnificent'), Js('Majestic'), Js('Mammoth'), Js('Marvelous'), Js('Massive'), Js('Mellow'), Js('Mighty'), Js('Misty'), Js('Moldy'), Js('Mysterious'), Js('Narrow'), Js('Old'), Js('Panoramic'), Js('Parallel'), Js('Peaceful'), Js('Plain'), Js('Pleasant'), Js('Precious'), Js('Private'), Js('Quiet'), Js('Rainy'), Js('Reflecting'), Js('Romantic'), Js('Rotten'), Js('Round'), Js('Royal'), Js('Sacred'), Js('Scattered'), Js('Secret'), Js('Shimmering'), Js('Sickly'), Js('Simple'), Js('Special'), Js('Spectacular'), Js('Spiritual'), Js('Stormy'), Js('Teeny'), Js('Terrible'), Js('Terrific'), Js('Thick'), Js('Thin'), Js('Thundering'), Js('Tiny'), Js('Unknown'), Js('Violent'), Js('Violet'), Js('Wandering'), Js('Whimsical'), Js('Whispering'), Js('Wicked'), Js('Wild'), Js('Windy'), Js('Young')]))
var.put('names5', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names7', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names8', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names9', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
grasslandNames = var.to_python()
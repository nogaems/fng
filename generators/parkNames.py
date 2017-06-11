__all__ = ['parkNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('name', ((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('name', ((((((var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2')))+var.get('names5').get(var.get('rnd3')))+var.get('names6').get(var.get('rnd4')))+var.get('names7').get(var.get('rnd5')))+Js(' '))+var.get('names2').get(var.get('rnd6'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Almond'), Js('Angel'), Js('Angel Island'), Js('Angelwing'), Js('Antelope'), Js('Bamboo'), Js('Bayview'), Js('Bearhug'), Js('Big Pond'), Js('Birch'), Js('Birdsong'), Js('Blossom'), Js('Blue Laguna'), Js('Boulderfield'), Js('Briarwood'), Js('Broadview'), Js('Bronze Arch'), Js('Cascade'), Js('Castle'), Js('Cherry Blossom'), Js('Chestnut'), Js('City Hall'), Js('City Square'), Js('Clear Lake'), Js('Clearview'), Js('Coldwater'), Js('Community'), Js('Cottonfield'), Js('Creekside'), Js('Crescent'), Js('Crossroad'), Js('Crow Feather'), Js('Crown'), Js('Crystal Cove'), Js('Crystal Lake'), Js('Cypress'), Js('Diamond'), Js('Discovery'), Js('Dogwood'), Js('Eagle Eye'), Js('East River'), Js('Echo'), Js('Elm'), Js('Emerald'), Js('Emerald Moss'), Js('Exploration'), Js('Fairview'), Js('Fletcher'), Js('Flower'), Js('Flowerscent'), Js('Foxtail'), Js('Gardenland'), Js('Glacier Bay'), Js('Gladstone'), Js('Golden'), Js('Golden Gate'), Js('Grand Avenue'), Js('Grand Lake'), Js('Grandview'), Js('Great Valley'), Js('Green Marine'), Js('Greenbelt'), Js('Greenfair'), Js('Greenwood'), Js('Grizzle Forest'), Js('Habitat'), Js('Harborview'), Js('Harmony'), Js('Hazelnut'), Js('Heavenly'), Js('High Valley'), Js('Highland'), Js('Hope'), Js('Hot Spring'), Js('Hummingbird'), Js('Ironbark'), Js('Jade'), Js('Junction'), Js('Juniper'), Js('Keystone'), Js("King's"), Js('Ladybug'), Js('Lakeview'), Js('Lakewood'), Js('Liberty'), Js('Lighthouse'), Js('Little Brook'), Js('Little River'), Js('Long Lake'), Js('Mahogany'), Js('Majestic'), Js('Maple'), Js('Maple Grove'), Js('Maple Leaf'), Js('Maple Wood'), Js('Marine'), Js('Meadows'), Js('Memorial'), Js('Mercy'), Js('Midland'), Js('Mirror Lake'), Js('Moonlight'), Js('Morning Dew'), Js('Mountain Spring'), Js('Mushroom'), Js('Natural Bridge'), Js('New Creek'), Js('New Forest'), Js('Nightingale'), Js('Northlake'), Js('Oakland'), Js('Observatory'), Js('Ocean Breeze'), Js('Oceanside'), Js('Old Forest'), Js('Open Water'), Js('Oracle'), Js('Orchard'), Js('Owlfeather'), Js('Owlwing'), Js('Pandora'), Js('Peace'), Js('Petal'), Js('Phoenix'), Js('Pigeon Point'), Js('Pineneedle'), Js('Pioneer'), Js('Pleasant View'), Js('Portal'), Js('Prospect'), Js('Pygmy'), Js('Raccoon'), Js('Rainbow'), Js('Ravine'), Js('Red Fern'), Js('Red Squirrel'), Js('Red Tail'), Js('Redwood'), Js('River View'), Js('Riverbank'), Js('Riverfront'), Js('Riverside'), Js('Riverview'), Js('Rosemary'), Js('Rosewood'), Js('Royal Isle'), Js('Ruby'), Js('Runestone'), Js('Salt Point'), Js('Sand Cove'), Js('Sapphire'), Js('Sapphire Creek'), Js('Sea Breeze'), Js('Seacrest'), Js('Seashore'), Js('Seaside'), Js('Serenity'), Js('Shadow'), Js('Shore'), Js('Sierra'), Js('Silver'), Js('Silver Lake'), Js('Silver Oak'), Js('Silver Rock'), Js('Silverwood'), Js('Small Pond'), Js('Snowflake'), Js('Solstice'), Js('Songbird'), Js('Soundscape'), Js('South Point'), Js('Southside'), Js('Spring'), Js('Spring Creek'), Js('Stone Lake'), Js('Strawberry'), Js('Summit'), Js('Sun Valley'), Js('Sunnyside'), Js('Sunrise'), Js('Sunset'), Js('Temple'), Js('Thornbush'), Js('Thyme Point'), Js('Tranquil'), Js('Triangle'), Js('Trillium'), Js('Twilight'), Js('Twin Lake'), Js('Twin River'), Js('Two River'), Js('University'), Js('Virgin'), Js('Waterfront'), Js('West Beach'), Js('White Stag'), Js('Wild Rose'), Js('Wildlife'), Js('Wildwood'), Js('Willow'), Js('Windy'), Js('Wolf Point')]))
var.put('names2', Js([Js('Park'), Js('Gardens'), Js('Meadows'), Js('Garden'), Js('Plaza'), Js('Grounds')]))
var.put('names3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('names7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
parkNames = var.to_python()
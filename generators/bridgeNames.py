__all__ = ['bridgeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('i')<Js(4.0)):
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
            else:
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abandoned'), Js('Admired'), Js('Adored'), Js('Aged'), Js('Anchored'), Js('Ancient'), Js('Angelic'), Js('Antique'), Js('Austere'), Js('Autumn'), Js('Bare'), Js('Barren'), Js('Big'), Js('Black'), Js('Bland'), Js('Blank'), Js('Bleak'), Js('Blond'), Js('Blue'), Js('Bold'), Js('Bouncy'), Js('Brave'), Js('Bright'), Js('Broken'), Js('Bronze'), Js('Brown'), Js('Burly'), Js('Calm'), Js('Capital'), Js('Chief'), Js('Classic'), Js('Clear'), Js('Coarse'), Js('Cold'), Js('Colossal'), Js('Common'), Js('Complex'), Js('Composed'), Js('Conquest'), Js('Courage'), Js('Crimson'), Js('Crystal'), Js('Dark'), Js('Dearest'), Js('Deep'), Js('Deepest'), Js('Defiant'), Js('Deserted'), Js('Diamond'), Js('Diligent'), Js('Double'), Js('Dry'), Js('East'), Js('Elegant'), Js('Emerald'), Js('Empty'), Js('Enchanted'), Js('Enlightened'), Js('Exalted'), Js('Fair'), Js('Free'), Js('Freedom'), Js('Gentle'), Js('Giant'), Js('Glistening'), Js('Golden'), Js('Graceful'), Js('Grand'), Js('Grim'), Js('Grizzly'), Js('Harmony'), Js('Heavenly'), Js('Heavy'), Js('Hollow'), Js('Humble'), Js('Idle'), Js('Infinite'), Js('Infinity'), Js('Innocence'), Js('International'), Js('Iron'), Js('Jade'), Js('Jagged'), Js('Last'), Js('Liberty'), Js('Light'), Js('Little'), Js('Lone'), Js('Lonely'), Js('Long'), Js('Lost'), Js('Majestic'), Js('Major'), Js('Mammoth'), Js('Massive'), Js('Mellow'), Js('Merry'), Js('Millennium'), Js('Misty'), Js('Mithril'), Js('Muddy'), Js('Murky'), Js('Mysterious'), Js('Mystery'), Js('Narrow'), Js('New'), Js('North'), Js('Old'), Js('Open'), Js('Ornate'), Js('Oval'), Js('Pale'), Js('Parallel'), Js('Peace'), Js('Peaceful'), Js('Plain'), Js('Pleasant'), Js('Precious'), Js('Pride'), Js('Prime'), Js('Pristine'), Js('Proud'), Js('Pure'), Js('Quiet'), Js('Regal'), Js('Remote'), Js('Round'), Js('Royal'), Js('Ruby'), Js('Rusty'), Js('Sandy'), Js('Sapphire'), Js('Serene'), Js('Serenity'), Js('Serpent'), Js('Shallow'), Js('Sharp'), Js('Shimmering'), Js('Short'), Js('Silent'), Js('Silver'), Js('Simple'), Js('Single'), Js('Sleepy'), Js('Slim'), Js('Small'), Js('Smooth'), Js('Somber'), Js('South'), Js('Spring'), Js('Steel'), Js('Stormy'), Js('Straight'), Js('Summer'), Js('Tall'), Js('Thin'), Js('Tranquility'), Js('Trinity'), Js('Twin'), Js('Velvet'), Js('Victory'), Js('Warped'), Js('West'), Js('Wide'), Js('Wild'), Js('Winding'), Js('Windy'), Js('Winter')]))
var.put('nm2', Js([Js('Abyss'), Js('Arch'), Js('Avenue'), Js('Bank'), Js('Banks'), Js('Bay'), Js('Beach'), Js('Bluff'), Js('Border'), Js('Branch'), Js('Brim'), Js('Brink'), Js('Brook'), Js('Canal'), Js('Canyon'), Js('Cay'), Js('Chasm'), Js('Cliff'), Js('Coast'), Js('Creek'), Js('Edge'), Js('Estuary'), Js('Falls'), Js('Flow'), Js('Gate'), Js('Gates'), Js('Gateway'), Js('Glacier'), Js('Gorge'), Js('Gulch'), Js('Harbor'), Js('Haven'), Js('Inlet'), Js('Island'), Js('Isle'), Js('Jubilee'), Js('Lake'), Js('Lane'), Js('Ledge'), Js('Memorial'), Js('Pass'), Js('Passage'), Js('Path'), Js('Point'), Js('Port'), Js('Portal'), Js('Ravine'), Js('River'), Js('Road'), Js('Route'), Js('Sails'), Js('Shore'), Js('Spring'), Js('Star'), Js('Stream'), Js('Street'), Js('Summit'), Js('Terrace'), Js('Trail'), Js('Tributary'), Js('Vale'), Js('Valley'), Js('Water'), Js('Way'), Js('Wharf')]))
var.put('nm3', Js([Js('Bridge'), Js('Bridge'), Js('Bridge'), Js('Bridge'), Js('Overpass'), Js('Viaduct'), Js('Aqueduct'), Js('Suspension Bridge'), Js('Footbridge'), Js('Crossing'), Js('Bridge'), Js('Bridge'), Js('Bridge'), Js('Bridge'), Js('Bridge'), Js('Bridge'), Js('Bridge'), Js('Bridge')]))
pass
pass


# Add lib to the module scope
bridgeNames = var.to_python()
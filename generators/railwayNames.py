__all__ = ['railwayNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Alligator Shallows'), Js('Ancient Heights'), Js('Angel Harbor'), Js('Arrow Point'), Js('Bamboo Park'), Js('Bamboo Wetland'), Js('Black Loch'), Js('Black Waters'), Js('Bog Forest'), Js('Borderlands'), Js('Boreal Plains'), Js('Boulder Shore'), Js('Boulderland'), Js('Breakwater'), Js('Central Snowland'), Js('Chasewater'), Js('Cherry Blossom'), Js('City Hall'), Js('Coastway'), Js('Community'), Js('Cottonfield'), Js('Creekside'), Js('Cross Country'), Js('Crystal Castle'), Js('Crystal Lake'), Js('Distant Waters'), Js('Dragonfly'), Js('Eagle Forest'), Js('East Coast'), Js('East Tropics'), Js('Eastern'), Js('Eastern City'), Js('Eastern Hills'), Js('Eastern Steppes'), Js('Echo Valley'), Js('Ethereal Wilds'), Js('Evergreen Glades'), Js('False River'), Js('Flat Water'), Js('Flower Gardens'), Js('Fogland'), Js('Fozen Tundra'), Js('Frost Mountain'), Js('Frostfire'), Js('Frozen Pinnacle'), Js('Gentle Coast'), Js('Glacier Forest'), Js('Golden Palace'), Js('Grand Central'), Js('Grand Coastal'), Js('Grand Continental'), Js('Grand Forest'), Js('Grand Island'), Js('Grand Meadows'), Js('Grand Temple'), Js('Grand Valley'), Js('Gray Pinnacle'), Js('Great Central'), Js('Greenbelt'), Js('Greencoast'), Js('Grizzly Forest'), Js('Harborview'), Js('Harmony Creek'), Js('Harmony Morass'), Js('High Mountain'), Js('High Valley'), Js('Highland'), Js('Hollow Rock'), Js('Hope Meadows'), Js('Hope Valley'), Js('Ice Crowned'), Js('Iceberg'), Js('Iron Fjord'), Js('Iron Lake'), Js('Ironbark'), Js('Ivory Fields'), Js('Jade Gardens'), Js('Jade Waters'), Js('Kings Harbor'), Js('Lillypad'), Js('Little Rock'), Js('Little Valley'), Js('Lonely Mountain'), Js('Lotus Lake'), Js('Low Valley'), Js('Lowland'), Js('Maiden Stone'), Js('Maple Grove'), Js('Marble Cliff'), Js('Marble Coast'), Js('Marble Harbor'), Js('Maritime'), Js('Marshland'), Js('Meltwater'), Js('Midland'), Js('Midnight'), Js('Midsummer'), Js('Midwinter'), Js('Mighty Mountains'), Js('Mirror Lake'), Js('Mirror Pools'), Js('Misty Meadow'), Js('Molten Bay'), Js('Moonshadow'), Js('Murky Marsh'), Js('Narrow Fields'), Js('Narrow Wilds'), Js('New Channel'), Js('New Forest'), Js('New Haven'), Js('New North'), Js('New South'), Js('Nightingale'), Js('North Central'), Js('Northbound'), Js('Northern'), Js('Northern City'), Js('Oakland'), Js('Observatory'), Js('Old Forest'), Js('Orchard Park'), Js('Palm Shore'), Js('Paradise Coast'), Js('Pelican Beach'), Js('Phantom Falls'), Js('Pleasant View'), Js('Precious Wilds'), Js('Pristine Gardens'), Js('Quiet Field'), Js('Quiet Fields'), Js('Rain Forest'), Js('Red Wasteland'), Js('Redwood'), Js('Riverfront'), Js('Rivermouth'), Js('Riverview'), Js('Coal Belt'), Js('Hunter Country'), Js('Sacred Woods'), Js('Salmon Pier'), Js('Salt Lake'), Js('Sapphire Coast'), Js('Savage Coast'), Js('Savannah'), Js('Sea Breeze'), Js('Serenity'), Js('Serenity Beach'), Js('Serenity Hills'), Js('Serpent Channel'), Js('Serpent Falls'), Js('Settlers Point'), Js('Seven Palace'), Js('Shadow Fields'), Js('Shadow Lake'), Js('Shark Harbor'), Js('Shrimp Bay'), Js('Silent Tundra'), Js('Silver Hills'), Js('Silver Lake'), Js('Silver Wall'), Js('Silverstone'), Js('Six Mountain'), Js('Sleeping Mountain'), Js('Sleeping Rivers'), Js('Snow Crystal'), Js('Snow Meadow'), Js('Snowman'), Js('Somerset'), Js('Songbird'), Js('Soundscape'), Js('South Beach'), Js('South Central'), Js('Southern'), Js('Southside'), Js('Spring Blossom'), Js('Spring Valley'), Js('Spruce Forest'), Js('Stone Coast'), Js('Stone Lake'), Js('Storm Coast'), Js('Sunflower'), Js('Sunny Cay'), Js('Sunny Fields'), Js('Sunrise'), Js('Sunset'), Js('Sunshine Coast'), Js('Surfer Coast'), Js('Tadpole River'), Js('Tree Valley'), Js('Tropic Wetland'), Js('Turtle Coast'), Js('Turtle Swamp'), Js('Twelve City'), Js('Twin Mountain'), Js('Twin River'), Js('Uncanny Valley'), Js('University'), Js('Virgin Garden'), Js('Virgin Rapids'), Js('Virgin Valley'), Js('West Beach'), Js('West Coast'), Js('Wester Bog'), Js('Western'), Js('Wetlands'), Js('Whale Water'), Js('Whisper Valley'), Js('White Bay'), Js('White Sand'), Js('White Tundra'), Js('White Water'), Js('Whitehaven'), Js('Wild Ocean'), Js('Wild Rose'), Js('Willowvale'), Js('Windy Woods'), Js('Wolf Meadow')]))
var.put('nm2', Js([Js('Route'), Js('Main Line'), Js('Speed Line'), Js('Loop Line'), Js('Branch Line'), Js('Line'), Js('Rail Line'), Js('Tracks'), Js('Train Line'), Js('Line'), Js('Line'), Js('Line'), Js('Route'), Js('Route'), Js('Route'), Js('Tracks'), Js('Tracks'), Js('Tracks')]))
pass
pass


# Add lib to the module scope
railwayNames = var.to_python()
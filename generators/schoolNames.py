__all__ = ['schoolNames']

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
            var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Acadia'), Js('Angelwood'), Js('Apple Valley'), Js('Bayshore'), Js('Bear Mountain'), Js('Bear River'), Js('Bear Valley'), Js('Big Pine'), Js('Big Valley'), Js('Blue River'), Js('Broad River'), Js('Canyon View'), Js('Cape Coral'), Js('Central'), Js('Central Valley'), Js('Clear Lake'), Js('Clearwater'), Js('Columbus'), Js('Copper Cove'), Js('Coral Coast'), Js('Coral Springs'), Js('Crossroads'), Js('Crystal River'), Js('Cypress'), Js('Da Vinci'), Js('Darwin'), Js('Deer River'), Js('Deer Valley'), Js('Desert Sands'), Js('Desert Winds'), Js('Diamond'), Js('Eagle Mountain'), Js('East Bridge'), Js('East Shores'), Js('Eastside'), Js('Eastview'), Js('Eastwood'), Js('Edgewater'), Js('Edgewood'), Js('Einstein'), Js('Elk Creek'), Js('Elk Grove'), Js('Elk Valley'), Js('Enterprise'), Js('Eureka'), Js('Evergreen'), Js('Faith'), Js('Faraday'), Js('Foothill'), Js('Forest Lake'), Js('Fortuna'), Js('Freedom'), Js('Frozen Lake'), Js('Garden Grove'), Js('Golden Oak'), Js('Golden Sierra'), Js('Golden Valley'), Js('Grand Mountain'), Js('Grand Ridge'), Js('Grandview'), Js('Granite Bay'), Js('Granite Hills'), Js('Grapevine'), Js('Great Oak'), Js('Green Meadows'), Js('Green Valley'), Js('Greenfield'), Js('Greenlands'), Js('Greenville'), Js('Harbor View'), Js('Hawking'), Js('Hercules'), Js('Heritage'), Js('Highland'), Js('Hillview'), Js('Holy Oaks'), Js('Horizon'), Js('Independence'), Js('Laguna Bay'), Js('Laguna Beach'), Js('Laguna Creek'), Js('Lakeside'), Js('Lakewood'), Js('Liberty'), Js('Lincoln'), Js('Little Valley'), Js('Littlerock'), Js('Littlewood'), Js('Lone Oak'), Js('Lone Pine'), Js('Long Beach'), Js('Mammoth'), Js('Maple Hills'), Js('Maple Leaf'), Js('Maple Park'), Js('Maple Ridge'), Js('Marble Hills'), Js('Marie Curie'), Js('Martin Luther King'), Js('Meadows'), Js('Meadows Ridge'), Js('Millenium'), Js('Monarch'), Js('Mountain Oak'), Js('Mountainridge'), Js('Mountainview'), Js('Northride'), Js('Northview'), Js('Oak Grove'), Js('Oak Hills'), Js('Oak Park'), Js('Oak Ridge'), Js('Oakland'), Js('Oakleaf'), Js('Oakwood'), Js('Ocean View'), Js('Oceanside'), Js('Oyster Harbour'), Js('Pacific Grove'), Js('Palm Valley'), Js('Panorama'), Js('Paradise'), Js('Paramount'), Js('Patriot'), Js('Pine Hill'), Js('Pine Hills'), Js('Pinewood'), Js('Pioneer'), Js('Pleasant Grove'), Js('Pleasant Hill'), Js('Pleasant Valley'), Js('Promise'), Js('Providence'), Js('Rainbow'), Js('Ravenwood'), Js('Redlands'), Js('Redwood'), Js('Ridgeview'), Js('River Fork'), Js('River Valley'), Js('Riverbank'), Js('Riverdale'), Js('Riverview'), Js('Rutherford'), Js('Sacred Heart'), Js('Saint Helena'), Js("Saint Mary's"), Js('Sandalwood'), Js('Savanna'), Js('Seacoast'), Js('Seal Bay'), Js('Seal Coast'), Js('Seal Gulch'), Js('Seaside'), Js('Sierra'), Js('Silver Creek'), Js('Silver Oak'), Js('Silver Valley'), Js('Silverleaf'), Js('Skyline'), Js('Somerset'), Js('South Fork'), Js('Southview'), Js('Spring Gardens'), Js('Spring Hill'), Js('Springfield'), Js('Stonewall'), Js('Storm Coast'), Js('Summerfield'), Js('Summers'), Js('Summerville'), Js('Summit'), Js('Sun Valley'), Js('Sunny Coast'), Js('Sunny Hills'), Js('Sunnyside'), Js('Sunset'), Js('Sunshine'), Js('Timber Creek'), Js('Tranquillity'), Js('Trinity'), Js('Upper Lake'), Js('Valley View'), Js('Village'), Js('Vista'), Js('Waterfall'), Js('Waterfalls'), Js('Waterford'), Js('West Bridge'), Js('West Shores'), Js('Westside'), Js('Westview'), Js('Westwood'), Js('Whale Coast'), Js('Whale Gulch'), Js('White Mountain'), Js('Whitewater'), Js('Wildwood'), Js('Willow'), Js('Willow Creek'), Js('Willow Park'), Js('Winters'), Js('Winterville'), Js('Woodcreek'), Js('Woodside')]))
var.put('names2', Js([Js('Academy'), Js('College'), Js('High'), Js('High School'), Js('School'), Js('University'), Js('Elementary'), Js('Middle School'), Js('Institute'), Js('Charter School'), Js('School of Fine Arts'), Js('Secondary School'), Js('School for Girls'), Js('School for Boys'), Js('Conservatory'), Js('Grammar School'), Js('Kindergarten'), Js('Technical School')]))
pass
pass


# Add lib to the module scope
schoolNames = var.to_python()
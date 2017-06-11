__all__ = ['streetNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
var.put('nm1', Js([Js('Achorage'), Js('Acorn'), Js('Amber'), Js('Anchor'), Js('Angel'), Js('Apollo'), Js('Apostle'), Js('Arcade'), Js('Arch'), Js('Archer'), Js('Arctic'), Js('Art'), Js('Ash'), Js('Ashland'), Js('Auburn'), Js('Aurora'), Js('Autumn'), Js('Aviation'), Js('Azure'), Js('Baker'), Js('Bard'), Js('Barley'), Js('Bath'), Js('Bay'), Js('Bay View'), Js('Beach'), Js('Beachside'), Js('Beacon'), Js('Beaver'), Js('Beech'), Js('Bell'), Js('Bellow'), Js('Berry'), Js('Blessing'), Js('Bliss'), Js('Bloomfield'), Js('Blossom'), Js('Boulder'), Js('Brewer'), Js('Bridgewater'), Js('Bridgeway'), Js('Bright'), Js('Broad'), Js('Brook'), Js('Broom'), Js('Brown'), Js('Bury'), Js('Bush'), Js('Butcher'), Js('Campus'), Js('Canal'), Js('Cannon'), Js('Castle'), Js('Cathedral'), Js('Cave'), Js('Cavern'), Js('Cedar'), Js('Central'), Js('Centre'), Js('Champion'), Js('Chapel'), Js('Cherry'), Js('Chestnut'), Js('Circus'), Js('Clarity'), Js('Clearance'), Js('Cliff'), Js('Clove'), Js('Coach'), Js('Coastline'), Js('College'), Js('Colonel'), Js('Commercial'), Js('Congress'), Js('Copper'), Js('Coral'), Js('Corporation'), Js('Cottage'), Js('Crescent'), Js('Crimson'), Js('Cross'), Js('Crown'), Js('Crystal'), Js('Cypress'), Js('Dawn'), Js('Delta'), Js('Dew'), Js('Diamond'), Js('Dove'), Js('Duchess'), Js('Duke'), Js('Earl'), Js('East'), Js('Ebon'), Js('Elm'), Js('Elmwood'), Js('Ember'), Js('Emerald'), Js('Estate'), Js('Fair'), Js('Farmer'), Js('Feathers'), Js('Ferry'), Js('Flax'), Js('Fleet'), Js('Fletcher'), Js('Flint'), Js('Forest'), Js('Fortune'), Js('Fountain'), Js('Fox'), Js('Frost'), Js('Garden'), Js('Garnet'), Js('Gem'), Js('General'), Js('Gilded'), Js('Globe'), Js('Gold'), Js('Grace'), Js('Grand'), Js('Granite'), Js('Gravel'), Js('Gray'), Js('Great'), Js('Green'), Js('Greenfield'), Js('Grime'), Js('Grotto'), Js('Grove'), Js('Guild'), Js('Harbor'), Js('Hart'), Js('Haven'), Js('Hawthorne'), Js('Hazelnut'), Js('Heart'), Js('Heirloom'), Js('Heritage'), Js('High'), Js('Highland'), Js('Hill'), Js('Hind'), Js('Honor'), Js('Hope'), Js('Innovation'), Js('Ironwood'), Js('Ivory'), Js('Ivy'), Js('Jade'), Js('Java'), Js('Jewel'), Js('Judge'), Js('Juniper'), Js('Justice'), Js('King'), Js('Kings'), Js('Kingwood'), Js('Knight'), Js('Lake'), Js('Lavender'), Js('Law'), Js('Lawn'), Js('Legend'), Js('Liberty'), Js('Lily'), Js('Lilypad'), Js('Little'), Js('Locust'), Js('Long'), Js('Lotus'), Js('Love'), Js('Low'), Js('Lower'), Js('Lowland'), Js('Lumber'), Js('Luna'), Js('Main'), Js('Mandarin'), Js('Manor'), Js('Maple'), Js('Marble'), Js('Marine'), Js('Market'), Js('Mason'), Js('Meadow'), Js('Medieval'), Js('Merchant'), Js('Middle'), Js('Mill'), Js('Monument'), Js('Moon'), Js('Moonlight'), Js('Mount'), Js('Museum'), Js('National'), Js('New Castle'), Js('Nightingale'), Js('Noble'), Js('North'), Js('Nova'), Js('Oak'), Js('Ocean'), Js('Oceanview'), Js('Old'), Js('Olive'), Js('Onyx'), Js('Orchard'), Js('Orchid'), Js('Oval'), Js('Palm'), Js('Paradise'), Js('Park'), Js('Parkside'), Js('Parkview'), Js('Peace'), Js('Pearl'), Js('Pebble'), Js('Pegasus'), Js('Penrose'), Js('Petal'), Js('Phoenix'), Js('Pine'), Js('Pinnacle'), Js('Pioneer'), Js('Plaza'), Js('Polygon'), Js('Poplar'), Js('Prince'), Js('Princess'), Js('Prospect'), Js('Providence'), Js('Quarry'), Js('Queen'), Js('Railway'), Js('Ranger'), Js('Redwood'), Js('Revolution'), Js('River'), Js('Rose'), Js('Rosemary'), Js('Rowan'), Js('Royalty'), Js('Ruby'), Js('Saffron'), Js('Sapphire'), Js('School'), Js('Seacoast'), Js('Seaview'), Js('Senna'), Js('Serenity'), Js('Shade'), Js('Shadow'), Js('Silver'), Js('Smith'), Js('Snowflake'), Js('South'), Js('Spring'), Js('Spruce'), Js('Star'), Js('Starfall'), Js('Starlight'), Js('Station'), Js('Steam'), Js('Stone'), Js('Storm'), Js('Sugarplum'), Js('Summer'), Js('Summit'), Js('Sun'), Js('Sunny'), Js('Sunshine'), Js('Sycamore'), Js('Temple'), Js('Terrace'), Js('Theater'), Js('Timber'), Js('Tower'), Js('Trinity'), Js('Underwood'), Js('Union'), Js('University'), Js('Upper'), Js('Vale'), Js('Valley'), Js('Vermilion'), Js('Victory'), Js('Vine'), Js('Vista'), Js('Walnut'), Js('Water'), Js('Wellness'), Js('West'), Js('Wetland'), Js('Wharf'), Js('Willow'), Js('Windmill'), Js('Winter'), Js('Wright'), Js('Yew')]))
var.put('nm2', Js([Js('Street'), Js('Avenue'), Js('Lane'), Js('Row'), Js('Boulevard'), Js('Way'), Js('Route'), Js('Passage'), Js('Street'), Js('Avenue'), Js('Lane')]))
pass
pass


# Add lib to the module scope
streetNames = var.to_python()
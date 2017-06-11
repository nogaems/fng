__all__ = ['hotelNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names4', 'names2', 'nameGen', 'names3'])
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
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names4').get(var.get('rnd3'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('names', ((var.get('names3').get(var.get('rnd'))+Js(' '))+var.get('names4').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Ancient'), Js('Antique'), Js('Aquamarine'), Js('Atlantic'), Js('Atlantis'), Js('Autumn'), Js('Azure'), Js('Brass'), Js('Bronze'), Js('Cerulean'), Js('Crimson'), Js('Crown'), Js('Double'), Js('Dual'), Js('Eastern'), Js('Ebony'), Js('Elder'), Js('Elite'), Js('Emerald'), Js('Exalted'), Js('Gentle'), Js('Glorious'), Js('Golden'), Js('Grand'), Js('Grandiose'), Js('Historic'), Js('Illustrious'), Js('Ivory'), Js('Jade'), Js("King's"), Js('Light'), Js("Lord's"), Js('Lunar'), Js('Majestic'), Js('Malachite'), Js('Marina'), Js('Mellow'), Js('Modest'), Js('Noble'), Js('Northern'), Js('Obsidian'), Js('Olive'), Js('Onyx'), Js('Oriental'), Js('Pacific'), Js('Parallel'), Js('Peaceful'), Js('Pleasant'), Js('Primal'), Js("Prince's"), Js('Private'), Js("Queen's"), Js('Quiet'), Js('Regal'), Js('Remote'), Js('Riverside'), Js('Rose'), Js('Royal'), Js('Ruby'), Js('Saffron'), Js('Sapphire'), Js('Scarlet'), Js('Secluded'), Js('Secret'), Js('Serene'), Js('Silver'), Js('Snowy'), Js('Soft'), Js('Southern'), Js('Spring'), Js('Sublime'), Js('Summer'), Js('Sunny'), Js('Sunrise'), Js('Sunset'), Js('Supreme'), Js('Tranquil'), Js('Triple'), Js('Twin'), Js('Viridian'), Js('Western'), Js('White'), Js('Winter')]))
var.put('names2', Js([Js('Aegis'), Js('Angel'), Js('Arc'), Js('Atoll'), Js('Aurora'), Js('Baron'), Js('Basin'), Js('Bay'), Js('Bazaar'), Js('Beach'), Js('Bear'), Js('Bliss'), Js('Blossom'), Js('Bluff'), Js('Brewery'), Js('Brook'), Js('Cabin'), Js('Camp'), Js('Canopy'), Js('Canyon'), Js('Carnaval'), Js('Castle'), Js('Cave'), Js('Cavern'), Js('Chasm'), Js('Circus'), Js('Citadel'), Js('Cliff'), Js('Cloak'), Js('Cloud'), Js('Coast'), Js('Comfort'), Js('Cosmos'), Js('Cottage'), Js('Court'), Js('Courtyard'), Js('Cove'), Js('Covert'), Js('Creek'), Js('Crow'), Js('Crown'), Js('Dawn'), Js('Dome'), Js('Dream'), Js('Dune'), Js('Echo'), Js('Elephant'), Js('Emperor'), Js('Estate'), Js('Excalibur'), Js('Expanse'), Js('Fjord'), Js('Flower'), Js('Forest'), Js('Galaxy'), Js('Garden'), Js('Gardens'), Js('Gem'), Js('Gorge'), Js('Grotto'), Js('Grove'), Js('Gulf'), Js('Harbor'), Js('Haven'), Js('Heights'), Js('Heirloom'), Js('Heritage'), Js('Hill'), Js('Horizon'), Js('House'), Js('Island'), Js('Isle'), Js('Jewel'), Js('Jungle'), Js('Keep'), Js('Lagoon'), Js('Lake'), Js('Landscape'), Js('Legacy'), Js('Lion'), Js('Loch'), Js('Lodge'), Js('Luxury'), Js('Majesty'), Js('Manor'), Js('Mansion'), Js('Mantle'), Js('Maple'), Js('Market'), Js('Meadows'), Js('Memorial'), Js('Mill'), Js('Mirror'), Js('Monarch'), Js('Mountain'), Js('Nebula'), Js('Nimbus'), Js('Nugget'), Js('Oak'), Js('Obelisk'), Js('Ocean'), Js('Orb'), Js('Oyster'), Js('Palace'), Js('Palms'), Js('Panorama'), Js('Paradise'), Js('Park'), Js('Pass'), Js('Pastures'), Js('Peak'), Js('Peaks'), Js('Peninsula'), Js('Petal'), Js('Phoenix'), Js('Pier'), Js('Pinnacle'), Js('Plains'), Js('Plaza'), Js('Point'), Js('Pool'), Js('Prairie'), Js('Pyramid'), Js('Quest'), Js('Rainbow'), Js('Raven'), Js('Refuge'), Js('Renaissance'), Js('Residence'), Js('Ribbon'), Js('Ridge'), Js('River'), Js('Rose'), Js('Safari'), Js('Sanctuary'), Js('Sanctum'), Js('Seashore'), Js('Seaside'), Js('Season'), Js('Shack'), Js('Shield'), Js('Shore'), Js('Shores'), Js('Shrine'), Js('Shroud'), Js('Sierra'), Js('Spa'), Js('Spire'), Js('Spring'), Js('Square'), Js('Star'), Js('Summit'), Js('Sword'), Js('Temple'), Js('Thicket'), Js('Tide'), Js('Time'), Js('Tower'), Js('Treasure'), Js('Trinket'), Js('Tropic'), Js('Tundra'), Js('Universe'), Js('Vale'), Js('Valley'), Js('Veil'), Js('Vertex'), Js('View'), Js('Vista'), Js('Willow'), Js('Wolf'), Js('Woodland')]))
var.put('names3', Js([Js('Abundance'), Js('Amber'), Js('Amenity'), Js('Amuse'), Js('Anomaly'), Js('Antique'), Js('Antiquity'), Js('Apex'), Js('Asylum'), Js('Azure'), Js('Baroque'), Js('Beverage'), Js('Blizzard'), Js('Breakwater'), Js('Celestial'), Js('Chateau'), Js('Cinnamon'), Js('Citadel'), Js('Cloud'), Js('Coastline'), Js('Coffee'), Js('Comfort'), Js('Copper'), Js('Cosmos'), Js('Countryside'), Js('Courtyard'), Js('Cozy'), Js('Crescent'), Js('Crown'), Js('Curiosity'), Js('Daydream'), Js('Delight'), Js('Deluge'), Js('Deluxe'), Js('Diamond'), Js('Diorama'), Js('Drizzle'), Js('Echo'), Js('Elegant'), Js('Elysium'), Js('Emerald'), Js('Enigma'), Js('Enterprise'), Js('Epitome'), Js('Essence'), Js('Everland'), Js('Exalted'), Js('Excursion'), Js('Expedition'), Js('Fairyland'), Js('Fancy'), Js('Fantasy'), Js('Farmhouse'), Js('Felicity'), Js('Freedom'), Js('Galaxy'), Js('Glacier'), Js('Glee'), Js('Globetrotter'), Js('Golden Nugget'), Js('Grand'), Js('Harborview'), Js('History'), Js('Holiday'), Js('Iceberg'), Js('Icecap'), Js('Imperial'), Js('Jade'), Js('Leisure'), Js('Lethargy'), Js('Liberty'), Js('Lunar'), Js('Luxury'), Js('Mahogany'), Js('Majestic'), Js('Mirage'), Js('Mirror'), Js('Mirth'), Js('Monolith'), Js('Monsoon'), Js('Moonlight'), Js('Moss'), Js('Mountain'), Js('Muse'), Js('Nature'), Js('Nebula'), Js('Nimbus'), Js('Nostalgia'), Js('Nourish'), Js('Nova'), Js('Obelisk'), Js('Ocean'), Js('Oceanside'), Js('Oceanview'), Js('Opportunity'), Js('Oracle'), Js('Orbit'), Js('Oriental'), Js('Ornate'), Js('Outlook'), Js('Palace'), Js('Panorama'), Js('Paradise'), Js('Paragon'), Js('Parellel'), Js('Pinnacle'), Js('Prism'), Js('Prophecy'), Js('Radiance'), Js('Rain'), Js('Rainbow'), Js('Ranch'), Js('Recreation'), Js('Refresh'), Js('Regal'), Js('Relaxation'), Js('Renaissance'), Js('Repose'), Js('Retro'), Js('Revelation'), Js('Road Trip'), Js('Rosewood'), Js('Royal'), Js('Salt Water'), Js('Sanctuary'), Js('Sanctum'), Js('Sapphire'), Js('Seacoast'), Js('Seascape'), Js('Seashore'), Js('Seaside'), Js('Seven Seas'), Js('Shoreline'), Js('Sierra'), Js('Sightsee'), Js('Slumber'), Js('Smile'), Js('Snooze'), Js('Solar'), Js('Spare Time'), Js('Spectrum'), Js('Stardust'), Js('Stargaze'), Js('Starlight'), Js('Stellar'), Js('Stratosphere'), Js('Summit'), Js('Sunway'), Js('Sweet Dreams'), Js('Tower'), Js('Travel'), Js('Traveller'), Js('Triumph'), Js('Troposphere'), Js('Universe'), Js('Utopia'), Js('Vacation'), Js('Vanilla'), Js('Vertex'), Js('Viewpoint'), Js('Vision'), Js('Vortex'), Js('Voyage'), Js('Voyager'), Js('Wanderlust'), Js('Windmill'), Js('Wonderland'), Js('Yesteryear'), Js('Zion')]))
var.put('names4', Js([Js('Hotel'), Js('Resort'), Js('Resort & Spa'), Js('Hotel & Spa'), Js('Hotel'), Js('Hotel'), Js('Resort')]))
pass
pass


# Add lib to the module scope
hotelNames = var.to_python()
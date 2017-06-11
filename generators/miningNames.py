__all__ = ['miningNames']

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
var.put('nm1', Js([Js('Apex'), Js('Apex Empire'), Js('Astral'), Js('Astral Minerals'), Js('Avalon'), Js('Base Works'), Js('Basic Burrows'), Js('Bedrock Bed'), Js('Bedrock Bonanza'), Js('Bedrock Bottom'), Js('Big Burrows'), Js('Black Burrows'), Js('Blackrock'), Js("Bottom's Up"), Js('Bouldercreek'), Js('Boulderfist'), Js('Brave Depths'), Js('Brave Ventures'), Js('Breakwater'), Js('Brimming Grounds'), Js('Brimstone'), Js('Broken Hill'), Js('Bursting Gorge'), Js('Carbon Copy'), Js('Carbon in the Rough'), Js('Carbonhill'), Js('Centurion'), Js('Century'), Js('Coal Creek'), Js('Coal Field'), Js('Cobalt Cove'), Js('Cobalt Grove'), Js('Copper Capers'), Js('Coppervale'), Js('Covert Coal'), Js('Crag Works'), Js('Crevice Creek'), Js('Dark Depths'), Js('Darkness'), Js('Deep Delves'), Js('Delta Depths'), Js('Deposit Depths'), Js('Depth Delvers'), Js('Diamond Delta'), Js('Diamond Depths'), Js('Diamond Downs'), Js('Diamond Drifts'), Js('Diamond Hill'), Js('Diamond Rush'), Js('Diamonds in the Rough'), Js('Dirty Delves'), Js('Dirty Depths'), Js('Draft Shaft'), Js('Eager Extracts'), Js('East Range'), Js('Ebon Depths'), Js('Ebony Abyss'), Js('Ebony Hill'), Js('Echo Depths'), Js('Echo Grounds'), Js('Elemental Elevation'), Js('Elemental Expanse'), Js('Elemental Extents'), Js('Elemental Extracts'), Js('Elemental Fundamentals'), Js('Energy Grounds'), Js('Extension Hill'), Js('Firestone'), Js('Fortune Fields'), Js('Fracture Field'), Js('Fracture Hill'), Js('Gem Packed'), Js('Gem-Packed Expanse'), Js('Gold Banks'), Js('Gold Creek'), Js('Gold Drops'), Js('Gold Field'), Js('Gold Grove'), Js('Gold Nugget'), Js('Gold Springs'), Js('Goldrush'), Js('Goldworth'), Js('Grand Chasm'), Js('Grand Expedition'), Js('Grand Exploration'), Js('Grand Grounds'), Js('Grand Measures'), Js('Grand Metal'), Js('Grand Nugget'), Js('Grand Quarry'), Js('Grand Range'), Js('Grand Resources'), Js('Grand Ridge'), Js('Grand Ventures'), Js('Grimestone'), Js('Grimstone'), Js('Groundworks'), Js('Hidden Gem'), Js('Hidden Nugget'), Js('Hope Downs'), Js('Intrepid Depths'), Js('Intrepid Ventures'), Js('Iron Baron'), Js('Iron Field'), Js('Iron Isles'), Js('Iron Legacy'), Js('Iron Mountain'), Js('Iron Peaks'), Js('Ironskin'), Js('Ironwing'), Js('Landscrape'), Js('Lead Leaders'), Js('Lead Legacy'), Js('Legacy'), Js('Metal Depths'), Js('Metal Exploration'), Js('Metal Miles'), Js('Metal Picks'), Js('Metal Springs'), Js('Metal Ventures'), Js('Minecorp'), Js('Mineral Chasm'), Js('Mineral Creek'), Js('Mineral Expanse'), Js('Mineral Field'), Js('Mineral Foundations'), Js('Mineral Grove'), Js('Mineral Picks'), Js('Mineral Pit'), Js('Mineral Reserve'), Js('Mineral Store'), Js('Mineral Ventures'), Js('Mount Venture'), Js('Mulligan'), Js('Nether Region'), Js('Netherwork'), Js('Nordic Gold'), Js('Nordic Ventures'), Js('North Peak'), Js('Nugget Field'), Js('Obsidian Depths'), Js('Onyx Depths'), Js('Opulence Depths'), Js('Panworks'), Js('Pinnacle'), Js('Precipice Paradise'), Js('Prosperity Hill'), Js('Prosperity Precipice'), Js('Quarry Query'), Js('Rainbow Minerals'), Js('Rare Reserve'), Js('Rich Rocks'), Js('Rock Bottom'), Js('Rocky Road'), Js('Sediment Banks'), Js('Sediment Creek'), Js('Sediment Hill'), Js('Sediment Vale'), Js('Silver Banks'), Js('Silver Expanse'), Js('Silver Nugget'), Js('Silver Shovel'), Js('Silver Silts'), Js('Silver Slivers'), Js('Silver Surveys'), Js('Silver Veil'), Js('Silverstone'), Js('Slate Works'), Js('Smashing Works'), Js('Smudgehill'), Js('Soothill'), Js('Southstone'), Js('Sparkling Grounds'), Js('Stonework'), Js('Talc Treasures'), Js('Talc Trench'), Js('Terra Firma'), Js('Terra Formations'), Js('Terra Nova'), Js('Terra Territory'), Js('Terra Tunnels'), Js('Terrain Titans'), Js('Thunder'), Js('Thunderrock'), Js('Tin Terrains'), Js('Tin Terrane'), Js('Tin Titans'), Js('Tin Trench'), Js('Tin Trove'), Js('Tin Tunnels'), Js('Titan Trove'), Js('Treasure Trove'), Js('Tunnelworks'), Js('Twin Creek'), Js('Twin Springs'), Js('Underground'), Js('Wealth Well'), Js('Wellspring'), Js('West Field'), Js('Zinc Holes')]))
var.put('nm2', Js([Js('Mining'), Js('Mining Companies'), Js('Mines'), Js('Mining Group'), Js('Mineshaft'), Js('Company'), Js('Corporation'), Js('Industries'), Js('Mining Corporation')]))
pass
pass


# Add lib to the module scope
miningNames = var.to_python()
__all__ = ['prisonNames']

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
var.put('names1', Js([Js('Ailing Woods'), Js('Angelwood'), Js('Ashfield'), Js('Ashgate'), Js('Ashmount'), Js('Ashtomb'), Js('Atonement'), Js('Big Spring'), Js('Bitterhold'), Js('Black Castle'), Js('Black Citadel'), Js('Black Crow'), Js('Black Forest'), Js('Black Fortress'), Js('Black Garden'), Js('Black Mountain'), Js('Iron Valley'), Js('Black Tower'), Js('Blackford'), Js('Blackport'), Js('Blackstorm'), Js('Blacktomb'), Js('Blackwater'), Js('Boarwood'), Js('Boulder Mountain'), Js('Bouldergate'), Js('Boulderkeep'), Js('Brinestone'), Js('Broken Bridge'), Js('Broken Dreams'), Js('Broken Hill'), Js('Broken Mountain'), Js('Bronzefield'), Js('Burned Bridge'), Js("Butcher's Cove"), Js('Charred Cove'), Js('Closed Gate'), Js('Cold Heart'), Js('Coldwater'), Js('Crimson Cove'), Js('Dark Citadel'), Js('Dark Fortress'), Js('Dark Portal'), Js('Dark Vaults'), Js('Darkside'), Js('Darkwater'), Js('Deadwater'), Js('Deephold'), Js('Desolation'), Js('Desperation'), Js("Devil's Gate"), Js('Doveport'), Js('Downwater'), Js('Dragon Isle'), Js('Dragontooth'), Js('Early Grave'), Js('Edgefield'), Js('Edgeville'), Js('Ember Island'), Js('Firevault'), Js('Flamewood'), Js('Forest Edge'), Js('Forsaken Forest'), Js('Frenzy Cay'), Js('Frost Cave'), Js('Frost Mountain'), Js('Frostgate'), Js('Frozen Citadel'), Js('Frozen Desert'), Js('Frozen Lake'), Js('Frozen River'), Js('Frozen Time'), Js('Game Over'), Js('Gatehouse'), Js('Ghost Isle'), Js('Golden Cay'), Js('Goldengate'), Js('Goldfield'), Js('Grandhaven'), Js('Graveworth'), Js('Greyrock'), Js('Grimway'), Js('Hallow Hill'), Js('Hellbound'), Js('Hot Spring'), Js('Howling Fjord'), Js('Howling Wind'), Js('Illwood'), Js('Imp Mountain'), Js('Iron Gate'), Js('Iron Keep'), Js('Ironbolt'), Js('Ironfist'), Js('Irongate'), Js('Irongrasp'), Js('Ironport'), Js('Joyville'), Js('Killingfield'), Js('Last Chance'), Js('Last Door'), Js('Last Rites'), Js('Limbo'), Js('Lonewood'), Js('Long Bay'), Js('Long Wait'), Js('Madstone'), Js('Maincastle'), Js('Mallhaven'), Js('New Chance'), Js('New Hope'), Js('Newgate'), Js('Nightmare'), Js('Nightstone'), Js('No Refuge'), Js('Numb Mountain'), Js('Numbwater'), Js('Oak Creek'), Js('Oakwood'), Js('Oblivion'), Js('Obsidian Dungeon'), Js('Obsidian Maze'), Js('Obsidian Retreat'), Js('Obsidian Tower'), Js('Old Mountain'), Js('Outcast'), Js('Pale Forest'), Js('Phoenix'), Js('Pineneedle'), Js('Pinewood'), Js('Purgatory'), Js('Pyreford'), Js("Raven's Nest"), Js('Ravenhold'), Js('Ravenwing'), Js('Ravenwood'), Js('Red Garden'), Js('Redemption'), Js('Retirement'), Js('River Bank'), Js('River Garrison'), Js('Riverbend'), Js('Rockwood'), Js('Rotten Creek'), Js('Saltwater'), Js('Sanctuary'), Js('Sanguine Isle'), Js('Sanguine Wood'), Js('Scarlet Bay'), Js('Scarlet Mountain'), Js('Scarlet Tower'), Js('Scorchwood'), Js('Shadow Citadel'), Js('Shadow Isle'), Js('Shadow Keep'), Js('Shark Bay'), Js('Shroudcliff'), Js('Silent Gallows'), Js('Silent Heights'), Js('Silent Wind'), Js('Silver Lining'), Js('Silver Shield'), Js('Silverbay'), Js('Silverchain'), Js('Silvercloud'), Js('Silverhold'), Js('Silverwater'), Js('Sky Vaults'), Js('Solidgate'), Js('Solitude'), Js('Stillwater'), Js('Stoneward'), Js('Storm Bay'), Js('Storm Cape'), Js('Storm Cave'), Js('Storm Desert'), Js('Stormford'), Js('Stormpits'), Js('Stormvault'), Js('Strongford'), Js('Strongwall'), Js('Terminus'), Js('Thunder Bay'), Js('Time Out'), Js('Tinderland'), Js('Tortoise Isle'), Js('Turtle Bay'), Js('Ultimatum'), Js('Wallbottom'), Js('Warfield'), Js('Wargate'), Js('Wasteland'), Js('Whisperwind'), Js('White Forest'), Js('White Garden'), Js('Wild River'), Js('Wildlands'), Js('Willow Creek'), Js('Winter Fortress'), Js('Woodford'), Js('Wormwood'), Js('Wrong Path')]))
var.put('names2', Js([Js('Asylum'), Js('Correctional Center'), Js('Correctional Facility'), Js('Detention Center'), Js('Holding Center'), Js('Institute'), Js('Institution'), Js('Juvenile Holding Center'), Js('Low Security Prison'), Js('Max Security Prison'), Js('Medium Security Prison'), Js('Penitentiary'), Js('Prison'), Js('Regional Prison'), Js('Work Camp')]))
pass
pass


# Add lib to the module scope
prisonNames = var.to_python()
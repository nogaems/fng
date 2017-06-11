__all__ = ['graveyards']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js("Ancestor's Rest"), Js('Angel Point'), Js('Angelwatch'), Js('Angelwing'), Js('Autumn Spring'), Js('Azure Gardens'), Js('Azure River'), Js('Big Rock'), Js('Bliss Garden'), Js('Boulder Creek'), Js('Cedar Grove'), Js('Cherry Blossom'), Js('Crescent Garden'), Js('Crown Hill'), Js('Crystal Grove'), Js('Crystal Lake'), Js('Darkwood'), Js('Eastlawn'), Js('Eastpark'), Js('Eden'), Js('Elmwood'), Js('Emerald Forest'), Js('Eternal Light'), Js('Eternal Rest'), Js('Evergreen'), Js('Fairhill'), Js('Fairmount'), Js('Fairview'), Js('Felicity'), Js('Field of Ancestry'), Js('Field of Honor'), Js('Flowerbed'), Js('Forest View'), Js('Free Spirit'), Js('Garden Terrace'), Js('Gentle Heart'), Js('Gentle Oak'), Js('Glory Gardens'), Js('Golden Gate'), Js('Golden Road'), Js('Goodheart Garden'), Js('Goodrest'), Js('Goodsprings'), Js('Graceland'), Js('Grand Lake'), Js('Grandforest'), Js('Grandview'), Js('Green Grass'), Js('Greenhill'), Js('Harmony'), Js('Harmony Grove'), Js('Harmony Springs'), Js('Heirloom Garden'), Js('Heritage'), Js("Heroes' Field"), Js("Heroes' Rest"), Js('Hillcrest'), Js('Holly Grove'), Js('Holy Oak'), Js('Hope Hill'), Js('Independence'), Js('Jade Forest'), Js('Juniper Gardens'), Js('Keystone'), Js('Kingshill'), Js('Lakeview'), Js('Last Honor'), Js('Last Rest'), Js('Legacy Lawn'), Js('Liberty'), Js('Little Light'), Js('Little River'), Js('Little Rock'), Js('Loving Oak'), Js('Maple Hill'), Js('Memorial Park'), Js('Memory Field'), Js('Memory Garden'), Js('Moonlight'), Js('Mountain Crest'), Js('Mountain Ridge'), Js('Mountain View'), Js('Mountainside'), Js('New Forest'), Js('North Hill'), Js('North Park'), Js('Oceanview'), Js('Old Forest'), Js('Olivewood'), Js('Paradise'), Js('Paradise Garden'), Js('Park Lawn'), Js('Peace Blossom'), Js('Peace Gardens'), Js('Peace of Mind'), Js('Pearly Gates'), Js('Pine Grove'), Js('Pinewood'), Js('Pioneer'), Js('Pleasant Green'), Js('Pleasant Valley'), Js('Prestige'), Js('Rainbow Gardens'), Js('Repose Grove'), Js('Revered Grove'), Js('Riverside'), Js('Riverview'), Js('Rose Petal'), Js('Rosendale'), Js('Rosevale'), Js('Sapphire Springs'), Js('Sea Breeze'), Js('Seastone'), Js('Serenity'), Js('Serenity Park'), Js('Small Isle'), Js('Snowcrystal'), Js('Snowfall'), Js('Snowflake'), Js('Songbird'), Js('South Hill'), Js('Spring Garden'), Js('Spring Grove'), Js('Spring Heights'), Js('Spring Meadow'), Js('Spring River'), Js('Starview'), Js('Summer Grove'), Js('Summer Hill'), Js('Summer Isle'), Js('Summer Peaks'), Js('Sunnyside'), Js('Sunrise'), Js('Sunset'), Js('Swan Lake'), Js('Tranquility Gardens'), Js('Tribute Field'), Js('Tribute Lawn'), Js('Trinity'), Js('Venerate Grove'), Js('White Angel'), Js('White Beach'), Js('White Light'), Js('White Oak'), Js('White Willow'), Js('Willow Grove'), Js('Willow Park'), Js('Skyreach'), Js('Lily Vale'), Js('Lilypad Lake')]))
var.put('nm2', Js([Js('Abandoned'), Js('Abandoned Hope'), Js('Ash Field'), Js('Ash River'), Js('Ashen Oak'), Js('Ashenvale'), Js('Ashvale'), Js('Autumn Grove'), Js('Bad Judgement'), Js('Banewood'), Js('Banshee Hill'), Js('Barren Field'), Js('Beast Forest'), Js('Beast Mountain'), Js('Black Ruins'), Js('Black Snow'), Js('Black Soul'), Js('Blackburn'), Js('Blackhill'), Js('Bleak Mountain'), Js('Bloodriver'), Js('Bone Yard'), Js('Broken Bones'), Js('Broken Soul'), Js('Burned Forest'), Js('Burning Forest'), Js('Burning River'), Js('Burning Rock'), Js('Burning Ruin'), Js('Burning Soul'), Js('Burning Wrath'), Js('Calamity Park'), Js('Chaos'), Js('Condemnation Park'), Js('Corruption'), Js('Crimson Flow'), Js('Dark Willow'), Js('Darkhill'), Js('Darkview'), Js('Darkwood'), Js('Demonic Eye'), Js('Demonvale'), Js('Demonwing'), Js('Depravity Grove'), Js('Desolate Field'), Js('Desparity'), Js("Devil's Playground"), Js('Devilry Gardens'), Js('Devilswood'), Js('Diablo'), Js('Doomvale'), Js('Dragonash'), Js('Dreadfield'), Js('Dry River'), Js('Duskwallow'), Js('Ebonwood'), Js('Eternal Fire'), Js('Eternal Sorrow'), Js('Evil Eye'), Js('Extinct Park'), Js('Extinction Grove'), Js('Fallen Oak'), Js('Fireside'), Js('Fireview'), Js('Forgotten'), Js('Forsaken'), Js('Foulvale'), Js('Furyvale'), Js('Gargoyle'), Js('Ghost Town'), Js('Gloomview'), Js('Grim Garden'), Js('Grim Reaper'), Js('Grimview'), Js('Grimwood'), Js('Guilty Vale'), Js('Hallowgate'), Js('Haunted'), Js('Haunted Woods'), Js('Hollow Gardens'), Js('Hollowvale'), Js('Immortal Fire'), Js('Imp Forest'), Js('Infamy'), Js('Infernal Grove'), Js('Inferno'), Js('Lost Soul'), Js('Maleficent'), Js('Malevolent Garden'), Js('Malign'), Js('Misery Field'), Js('Mortified Grove'), Js('Murkwood'), Js('Necropolis'), Js('Nefarious Grove'), Js('Nefarious Hill'), Js('Nemesis'), Js('Netherspring'), Js('Nightmare'), Js('Nightshade'), Js('No Rest'), Js('Obsidian Grove'), Js('Obsidian Hill'), Js('Perished Grove'), Js('Plague City'), Js('Plaguewoods'), Js('Poison Spring'), Js('Reaper Garden'), Js('Rotten Grove'), Js('Rottingvale'), Js('Sanguine River'), Js('Shade'), Js('Shadow'), Js('Shadow Garden'), Js('Shadowland'), Js('Silent Gardens'), Js('Sinner Field'), Js('Sinstone'), Js('Skeletalview'), Js('Skeleton Hill'), Js('Skullside'), Js('Sombre Oak'), Js('Sorrow Pit'), Js('Sorrowwood'), Js('Soulburn'), Js('Soulriver'), Js('Spitegrove'), Js('Stiff Park'), Js('Terrorvale'), Js('Thornbush'), Js('Tragedy Grove'), Js('Tragedy Park'), Js('Twisted Oak'), Js('Unholy Oak'), Js('Venomriver'), Js('Vile Field'), Js('Vile River'), Js('Vile Spring'), Js('Vilewood'), Js('Warpwood'), Js('Wasted Forest'), Js('Wasteland'), Js('Wayward'), Js('Wicked Eye'), Js('Wicked Willow'), Js('Wicked Wood'), Js('Wickedvale'), Js('Wickedwood'), Js('Woe Garden'), Js('Wrathriver')]))
var.put('nm3', Js([Js('Cemetery'), Js('Memorial Park'), Js('Burial Grounds'), Js('Memorial Gardens'), Js('Cemetery'), Js('Cemetery')]))
var.put('nm4', Js([Js('Graveyard'), Js('Graveyard'), Js('Graveyard'), Js('Mausoleum'), Js('Mortuary'), Js('Necropolis'), Js('Crypts'), Js('Catacombs'), Js('Tombs')]))
pass
pass


# Add lib to the module scope
graveyards = var.to_python()
__all__ = ['motorsportRaces']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm4', 'nm5', 'nm3', 'nm2', 'result'])
    var.put('nm1', Js([Js('Annual'), Js('Arctic'), Js('International'), Js('Acclaimed'), Js('Accomplished'), Js('Adamant'), Js('Advanced'), Js('Extreme'), Js('Bold'), Js('Classic'), Js('Creative'), Js('Dynamic'), Js('Economic'), Js('Exalted'), Js('Exclusive'), Js('Fearless'), Js('Fierce'), Js('First'), Js('General'), Js('Golden'), Js('Grand'), Js('Great'), Js('Long'), Js('National'), Js('Velvet'), Js('Nocturnal'), Js('Nimble'), Js('Obsidian'), Js('Jade'), Js('Sapphire'), Js('Oceanic'), Js('Original'), Js('Parallel'), Js('Prime'), Js('Premium'), Js('Radiant'), Js('Rapid'), Js('Swift'), Js('Silver'), Js('Silk'), Js('Sanguine'), Js('Crimson'), Js('Super'), Js('Supreme'), Js('Twin'), Js('Ultimate'), Js('Ultra'), Js('Ivory'), Js('Sapphire'), Js('Emerald'), Js('Ruby'), Js('Ebon'), Js('Wild'), Js('Solar'), Js('Lunar')]))
    var.put('nm2', Js([Js('Achiever'), Js('Ambition'), Js('Aspect'), Js('Audience'), Js('Basin'), Js('Beach'), Js('Beast'), Js('Border'), Js('Bridge'), Js('Capital'), Js('Celebration'), Js('Challenge'), Js('Classic'), Js('Cloud'), Js('Coast'), Js('Cold'), Js('Community'), Js('Creation'), Js('Creator'), Js('Crew'), Js('Crown'), Js('Desert'), Js('Diamond'), Js('District'), Js('Divide'), Js('Downtown'), Js('Dream'), Js('Earth'), Js('Enhancement'), Js('Experience'), Js('Field'), Js('Foundation'), Js('Freedom'), Js('Harbor'), Js('Hill'), Js('Holiday'), Js('Honor'), Js('Impulse'), Js('Independence'), Js('Intelligence'), Js('Invention'), Js('Island'), Js('Liberty'), Js('Marsh'), Js('Member'), Js('Mirror'), Js('Sunset'), Js('Sunrise'), Js('Mobile'), Js('Monument'), Js('Motion'), Js('Mountain'), Js('Movement'), Js('Network'), Js('Night'), Js('Opportunity'), Js('Passage'), Js('Patriot'), Js('Performance'), Js('Perseverance'), Js('Pinnacle'), Js('Revolution'), Js('Specialist'), Js('Swamp'), Js('Territory'), Js('Thrill'), Js('Thunder'), Js('Tradition'), Js('Trail'), Js('Victory'), Js('Voyage'), Js('Wilderness')]))
    var.put('nm3', Js([Js('Acclaimed'), Js('Accomplished'), Js('Achiever'), Js('Adamant'), Js('Advanced'), Js('Ambition'), Js('Annual'), Js('Arctic'), Js('Aspect'), Js('Audience'), Js('Basin'), Js('Beach'), Js('Beast'), Js('Bold'), Js('Border'), Js('Bridge'), Js('Capital'), Js('Celebration'), Js('Challenge'), Js('Classic'), Js('Cloud'), Js('Coast'), Js('Cold'), Js('Community'), Js('Creation'), Js('Creative'), Js('Creator'), Js('Crew'), Js('Crimson'), Js('Crown'), Js('Desert'), Js('Diamond'), Js('District'), Js('Divide'), Js('Downtown'), Js('Dream'), Js('Dynamic'), Js('Earth'), Js('Ebon'), Js('Economic'), Js('Emerald'), Js('Enhancement'), Js('Exalted'), Js('Exclusive'), Js('Experience'), Js('Extreme'), Js('Fearless'), Js('Field'), Js('Fierce'), Js('First'), Js('Foundation'), Js('Freedom'), Js('General'), Js('Golden'), Js('Grand'), Js('Great'), Js('Harbor'), Js('Hill'), Js('Holiday'), Js('Honor'), Js('Impulse'), Js('Independence'), Js('Intelligence'), Js('International'), Js('Invention'), Js('Island'), Js('Ivory'), Js('Jade'), Js('Liberty'), Js('Long'), Js('Lunar'), Js('Marsh'), Js('Member'), Js('Mirror'), Js('Mobile'), Js('Monument'), Js('Motion'), Js('Mountain'), Js('Movement'), Js('National'), Js('Network'), Js('Night'), Js('Nimble'), Js('Nocturnal'), Js('Obsidian'), Js('Oceanic'), Js('Opportunity'), Js('Original'), Js('Parallel'), Js('Passage'), Js('Patriot'), Js('Performance'), Js('Perseverance'), Js('Pinnacle'), Js('Premium'), Js('Prime'), Js('Radiant'), Js('Rapid'), Js('Revolution'), Js('Ruby'), Js('Sanguine'), Js('Sapphire'), Js('Silk'), Js('Silver'), Js('Solar'), Js('Specialist'), Js('Sunrise'), Js('Sunset'), Js('Super'), Js('Supreme'), Js('Swamp'), Js('Swift'), Js('Territory'), Js('Thrill'), Js('Thunder'), Js('Tradition'), Js('Trail'), Js('Twin'), Js('Ultimate'), Js('Ultra'), Js('Velvet'), Js('Victory'), Js('Voyage'), Js('Wild'), Js('Wilderness')]))
    var.put('nm4', Js([Js('All Star'), Js('All Stars'), Js('Climb'), Js('Cross'), Js('Drag'), Js('Drag Race'), Js('Dragster'), Js('Drift'), Js('Drifter'), Js('Drifting'), Js('Elite'), Js('Endurance'), Js('Formula'), Js('Full Throttle'), Js('Hill'), Js('Hill Climb'), Js('Hot Rod'), Js('Kart'), Js('Legacy'), Js('Mini'), Js('Miniature'), Js('Modified'), Js('Motorcross'), Js('Off Road'), Js('Off-Road'), Js('Outlaw'), Js('Performance'), Js('Pro'), Js('Production Car'), Js('Rally'), Js('Rallycross'), Js('Road Racing'), Js('Speed'), Js('Speedway'), Js('Sports'), Js('Sportscar'), Js('Spring Car'), Js('Sprint'), Js('Stock'), Js('Stock Car'), Js('Superbike'), Js('Supercar'), Js('Supercross'), Js('Superkart'), Js('Supermodified'), Js('Superstar'), Js('Touring'), Js('Touring Car'), Js('Velocity')]))
    var.put('nm5', Js([Js('Champion Series'), Js('Championship'), Js('Championship Series'), Js('Cup'), Js('Formula Masters'), Js('Junior Championship'), Js('Juniors'), Js('League'), Js('Masters'), Js('Pro Series'), Js('Racing Series'), Js('Series'), Js('Superleague'), Js('World Championship'), Js('World Series')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            if (var.get('i')<Js(3.0)):
                var.put('names', (((Js('The ')+var.get('nm4').get(var.get('rnd4')))+Js(' '))+var.get('nm5').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', (((((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm4').get(var.get('rnd4')))+Js(' '))+var.get('nm5').get(var.get('rnd5'))))
                    var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', (((((Js('The ')+var.get('nm3').get(var.get('rnd')))+Js(' '))+var.get('nm4').get(var.get('rnd4')))+Js(' '))+var.get('nm5').get(var.get('rnd5'))))
                        var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm2').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', (((((((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm4').get(var.get('rnd4')))+Js(' '))+var.get('nm5').get(var.get('rnd5'))))
                        var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                        var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('nm4').callprop('splice', var.get('rnd4'), Js(1.0))
            var.get('nm5').callprop('splice', var.get('rnd5'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
motorsportRaces = var.to_python()
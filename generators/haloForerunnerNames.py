__all__ = ['haloForerunnerNames']

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
var.put('nm1', Js([Js('Accord of'), Js('Aeon of'), Js('Affinity of'), Js('Ambience of'), Js('Ambition of'), Js('Ashes of'), Js('Aspiration of'), Js('Aura of'), Js('Aurora of'), Js('Balance Brings'), Js('Balance of'), Js('Bornstellar Makes'), Js('Bright Wind of'), Js('Bringer of'), Js('Cautious Voice of'), Js('Choice of'), Js('Comet of'), Js('Darkness of'), Js('Dawn of'), Js('Desire of'), Js('Destiny of'), Js('Divinity from'), Js('Divinity of'), Js('Dreams of'), Js('Drift of'), Js('Dusk of'), Js('Dust of'), Js('Echo of'), Js('Empathy of'), Js('Eos of'), Js('Equilibrium Grants'), Js('Equilibrium of'), Js('Essence of'), Js('Eternal Rest of'), Js('Eternity Bears'), Js('Fabor of'), Js('Fallen Beneath'), Js('First Light Weaves'), Js('Fragment of'), Js('Future of'), Js('Galaxy Grants'), Js('Gift of'), Js('Glorious Light of'), Js('Gravity Grants'), Js('Harmony Gives'), Js('Harmony of'), Js('Heirloom of'), Js('Heritage of'), Js('Hope of'), Js('Hunger of'), Js('Infinity Brings'), Js('Legacy of'), Js('Life Gives'), Js('Life Grants'), Js('Light Brings'), Js('Light of'), Js('Love of'), Js('Memories of'), Js('Moment of'), Js('Nebula of'), Js('New Dawn Grants'), Js('Order of'), Js('Paradox of'), Js('Particle of'), Js('Peace of'), Js('Pleasure of'), Js('Prayer of'), Js('Pursuer of'), Js('Rays of'), Js('Resilience of'), Js('Resonance of'), Js('Rest of'), Js('Retinence Bears'), Js('Seeker of'), Js('Shadow of'), Js('Shard of'), Js('Silver Moon Brings'), Js('Sliver of'), Js('Sound of'), Js('Speed of'), Js('Spirit of'), Js('Splendid Dust of'), Js('Sympathy Makes'), Js('Tempest of'), Js('Time of'), Js('Tone of'), Js('Torrent of'), Js('Tranquility of'), Js('Truth Dreams'), Js('Truth of'), Js('Vision of'), Js('Twist of'), Js('Unity Weaves'), Js('Unity of'), Js('Veil of'), Js('Veiled Dream of'), Js('Veiled Light'), Js('Vengeance of'), Js('Voice of'), Js('Wanderer of'), Js('Wish of')]))
var.put('nm2', Js([Js('Ancient Stars'), Js('Animation and Life'), Js('Awareness'), Js('Black Void'), Js('Broken Nebula'), Js('Broken World'), Js('Caution and Poise'), Js('Celestial Body'), Js('Clarity and Purity'), Js('Clarity and Reason'), Js('Confident Future'), Js('Cosmic Infinity'), Js('Crimson Light'), Js('Curiosity'), Js('Darkness'), Js('Desire'), Js('Desired Future'), Js('Discipline'), Js('Distant Planet'), Js('Diversity'), Js('Divided World'), Js('Dying Stars'), Js('Dying World'), Js('Endless Void'), Js('Endurance and Durability'), Js('Eternal Cycles'), Js('Eternal Day'), Js('Eternal Happiness'), Js('Eternal Knowledge'), Js('Eternal Lasting'), Js('Eternal Legacies'), Js('Eternal Night'), Js('Eternal Stars'), Js('Eventual Redemption'), Js('Falling Skies'), Js('Fate and Destiny'), Js('Fire and Water'), Js('Fleeting Dreams'), Js('Fleeting Globe'), Js('Fleeting Memories'), Js('Fleeting Space'), Js('Floating Worlds'), Js('Forgotten Moon'), Js('Fortitude'), Js('Hopeful Legacy'), Js('Humble Mind'), Js('Ice and Water'), Js('Illumination'), Js('Inevitability'), Js('Infinite Knowledge'), Js('Infinite Moonlight'), Js('Infinite Starlight'), Js('Infinite Struggle'), Js('Inspiration'), Js('Intricate Design'), Js('Judgment'), Js('Knowledge and Power'), Js('Last Words'), Js('Life and Death'), Js('Light and Darkness'), Js('Limunous Bodies'), Js('Living Song'), Js('Living World'), Js('Lost Vision'), Js('Lost Worlds'), Js('Love and Grace'), Js('Luminous Light'), Js('Mind and Power'), Js('Neutrality'), Js('Night and Day'), Js('Orbital Life'), Js('Past Legacy'), Js('Perpetual Conflict'), Js('Perpetual Motion'), Js('Planetary Life'), Js('Pleasure'), Js('Primordial Light'), Js('Prominence'), Js('Quality and Purity'), Js('Reason'), Js('Reborn Planet'), Js('Redemption'), Js('Reflection and Retrospection'), Js('Renewed Faith'), Js('Sands of Time'), Js('Serenity and Trust'), Js('Shooting Star'), Js('Simplicity'), Js('Stability and Balance'), Js('Stars Eternal'), Js('Stars and Planets'), Js('Sundered Star'), Js('Symmetry'), Js('Trust and Faith'), Js('Twisted Fate'), Js('Value and Virtue'), Js('Wandering Star'), Js('Warped Space'), Js('Will and Might'), Js('Wisdom and Knowlege')]))
pass
pass


# Add lib to the module scope
haloForerunnerNames = var.to_python()
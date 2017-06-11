__all__ = ['towerNames']

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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2')))+Js(' '))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Accord'), Js('Afterlife'), Js('Ambition'), Js('Animus'), Js('Ascendance'), Js('Augury'), Js('Azure'), Js('Bloom'), Js('Bravery'), Js('Brotherhood'), Js('Calypso'), Js('Celebration'), Js('Central'), Js('Charity'), Js('Clover'), Js('Coalition'), Js('Concord'), Js('Conquest'), Js('Courage'), Js('Creed'), Js('Crystal'), Js('Daydream'), Js('Desire'), Js('Diamond'), Js('Divine'), Js('Domination'), Js('Dominion'), Js('Dragon'), Js('Dream'), Js('Dreamland'), Js('Elemental'), Js('Elysium'), Js('Endurance'), Js('Epiphany'), Js('Epoch'), Js('Essence'), Js('Eternity'), Js('Euphony'), Js('Exhibition'), Js('Faith'), Js('Fame'), Js('Fealty'), Js('Federation'), Js('Fortitude'), Js('Fortune'), Js('Freedom'), Js('Fusion'), Js('Glory'), Js('Gold'), Js('Hallow'), Js('Harmony'), Js('Heart'), Js("Heaven's"), Js('High'), Js('High Point'), Js('History'), Js('Homage'), Js('Honor'), Js('Hope'), Js('Horoscope'), Js('Independence'), Js('Infinity'), Js('Innocence'), Js('Judgment'), Js('Justice'), Js('Kinship'), Js('Labor'), Js('Liberation'), Js('Liberty'), Js('Life'), Js('Light'), Js('Melody'), Js('Memorial'), Js('Mirage'), Js('Myriad'), Js('Observation'), Js('Obsidian'), Js('Onyx'), Js('Oracle'), Js('Orbit'), Js('Orchestra'), Js('Paradise'), Js('Parallel'), Js('Patience'), Js('Peace Blossom'), Js('Perseverance'), Js('Phoenix'), Js('Piety'), Js('Pilgrimage'), Js('Pinnacle'), Js('Pixel'), Js('Power'), Js('Prestige'), Js('Promise'), Js('Prophecy'), Js('Prospect'), Js('Prosperity'), Js('Purity'), Js('Rainbow'), Js('Rebirth'), Js('Reincarnation'), Js('Rejuvenation'), Js('Renaissance'), Js('Resolution'), Js('Resurrection'), Js('Reunion'), Js('Revelation'), Js('Reverence'), Js('Rose'), Js('Salvation'), Js('Sanguine'), Js('Sentience'), Js('Serenity'), Js('Silk'), Js('Silver'), Js('Sky'), Js('Skyreach'), Js('Snowflake'), Js('Solace'), Js('Solidarity'), Js('Solitude'), Js('Soul'), Js('Space'), Js('Spirit'), Js('Star'), Js('Starlight'), Js('Strength'), Js('Summit'), Js('Supremacy'), Js('Symbiosis'), Js('Symphony'), Js('Synthesis'), Js('Temperance'), Js('Tenacity'), Js('Trade'), Js('Tranquility'), Js('Tribulation'), Js('Tribute'), Js('Triumph'), Js('Trust'), Js('Truth'), Js('Twin'), Js('Union'), Js('Unison'), Js('Universe'), Js('Utopia'), Js('Valiance'), Js('Valor'), Js('Velvet'), Js('Victory'), Js('Vigor'), Js('Virtue'), Js('Vision'), Js('Wildlife'), Js('Zion')]))
var.put('nm2', Js([Js('Ancestor'), Js('Ancient'), Js('Angel'), Js('Arch'), Js('Arrow'), Js('Ash'), Js('Azure'), Js('Barbarian'), Js('Bear'), Js('Behemoth'), Js('Berserker'), Js('Blade'), Js('Blood'), Js('Boar'), Js('Boulder'), Js('Broad'), Js('Bronze'), Js('Chaos'), Js('Corruption'), Js('Creed'), Js('Crescent'), Js('Crest'), Js('Crimson'), Js('Critter'), Js('Crown'), Js('Crypt'), Js('Crystal'), Js('Dagger'), Js('Dark'), Js('Daydream'), Js('Dead'), Js('Deer'), Js('Demon'), Js('Desolate'), Js('Dire'), Js('Dragon'), Js('Dread'), Js('Dream'), Js('Dust'), Js('East'), Js('Ebon'), Js('Echo'), Js('Ember'), Js('Emerald'), Js('Empyrean'), Js('Eternal'), Js('Fallen'), Js('Feral'), Js('Fiend'), Js('Fire'), Js('Forbidden'), Js('Forsaken'), Js('Fortune'), Js('Fossil'), Js('Freedom'), Js('Frenzy'), Js('Frost'), Js('Fury'), Js('Ghost'), Js('Gloom'), Js('Golden'), Js('Gossip'), Js('Grand'), Js('Gray'), Js('Great'), Js('Grim'), Js('Hallow'), Js('Harmony'), Js('Haunted'), Js('Heart'), Js('Heir'), Js('Heirloom'), Js('High'), Js('Hollow'), Js('Honor'), Js('Immortal'), Js('Imp'), Js('Imperial'), Js('Infinity'), Js('Iron'), Js('Jade'), Js('Lesser'), Js('Liberty'), Js('Light'), Js('Lily'), Js('Little'), Js('Low'), Js('Meditation'), Js('Memorial'), Js('Midsummer'), Js('Mighty'), Js('Miracle'), Js('Misty'), Js('Mithril'), Js('Monster'), Js('Monument'), Js('Mortal'), Js('Mystery'), Js('Nightmare'), Js('North'), Js('Oak'), Js('Obsidian'), Js('Onyx'), Js('Oracle'), Js('Outcast'), Js('Paradise'), Js('Peace'), Js('Pendulum'), Js('Phantom'), Js('Piety'), Js('Pine'), Js('Prestige'), Js('Primal'), Js('Prime'), Js('Primeval'), Js('Primordial'), Js('Rabid'), Js('Relic'), Js('Repose'), Js('Rose'), Js('Rotten'), Js('Rough'), Js('Royal'), Js('Ruby'), Js('Rune'), Js('Rust'), Js('Sacred'), Js('Sanctity'), Js('Sanguine'), Js('Sapphire'), Js('Savage'), Js('Secret'), Js('Serenity'), Js('Shade'), Js('Shadow'), Js('Silver'), Js('Sin'), Js('Skeleton'), Js('Sky'), Js('Smoke'), Js('Snow'), Js('Soul'), Js('South'), Js('Spirit'), Js('Spring'), Js('Stag'), Js('Steel'), Js('Storm'), Js('Summer'), Js('Talon'), Js('Terror'), Js('Thunder'), Js('Timeless'), Js('Trader'), Js('Traitor'), Js('Tranquility'), Js('Trinity'), Js('Twin'), Js('Velvet'), Js('Venom'), Js('Vestige'), Js('Vile'), Js('Weeping'), Js('West'), Js('Whisper'), Js('White'), Js('Wicked'), Js('Wild'), Js('Willow'), Js('Windy'), Js('Winter'), Js('Wisdom'), Js('Wolf'), Js('Wraith'), Js('Wrath'), Js('Wyvern')]))
var.put('nm3', Js([Js('Atoll'), Js('Beach'), Js('Bluff'), Js('Bog'), Js('Brook'), Js('Cave'), Js('Cavern'), Js('Cliff'), Js('Coast'), Js('Copse'), Js('Creek'), Js('Den'), Js('Desert'), Js('Dune'), Js('Fen'), Js('Field'), Js('Forest'), Js('Garden'), Js('Glade'), Js('Grotto'), Js('Grounds'), Js('Grove'), Js('Hill'), Js('Isle'), Js('Jungle'), Js('Lagoon'), Js('Lake'), Js('Land'), Js('Loch'), Js('Meadow'), Js('Mire'), Js('Moor'), Js('Morass'), Js('Mound'), Js('Mountain'), Js('Park'), Js('Pasture'), Js('Peak'), Js('Plains'), Js('Range'), Js('Ridge'), Js('River'), Js('Shore'), Js('Sierra'), Js('Slope'), Js('Strand'), Js('Stream'), Js('Swale'), Js('Swamp'), Js('Territory'), Js('Thicket'), Js('Woods')]))
var.put('nm4', Js([Js('Tower'), Js('Spire'), Js('Lookout'), Js('Mast'), Js('Pillar'), Js('Obelisk'), Js('Tower'), Js('Tower'), Js('Tower')]))
pass
pass


# Add lib to the module scope
towerNames = var.to_python()
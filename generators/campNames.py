__all__ = ['campNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('names', (Js('Camp ')+var.get('names1').get(var.get('rnd'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('names', (Js('Camp ')+var.get('names2').get(var.get('rnd'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('names', (Js('Camp ')+var.get('names3').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Aegis'), Js('Ambition'), Js('Amnesty'), Js('Armor'), Js('Bastion'), Js('Blessing'), Js('Chance'), Js('Charity'), Js('Chastity'), Js('Cherish'), Js('Citadel'), Js('Clemency'), Js('Comfort'), Js('Companion'), Js('Companionship'), Js('Company'), Js('Compassion'), Js('Conquest'), Js('Control'), Js('Courage'), Js('Covenant'), Js('Custody'), Js('Daydream'), Js('Delight'), Js('Desire'), Js('Dignity'), Js('Divinity'), Js('Dominion'), Js('Dream'), Js('Duty'), Js('Ecstasy'), Js('Eden'), Js('Elation'), Js('Elysium'), Js('Euphoria'), Js('Faith'), Js('Fantasy'), Js('Favor'), Js('Felicity'), Js('Fellowship'), Js('Fortitude'), Js('Fortune'), Js('Foster'), Js('Freedom'), Js('Glee'), Js('Glory'), Js('Goodwill'), Js('Guidance'), Js('Happiness'), Js('Harmony'), Js('Heart'), Js('Honesty'), Js('Honor'), Js('Hope'), Js('Immunity'), Js('Joy'), Js('Jubilee'), Js('Karma'), Js('Kudos'), Js('Liberty'), Js('Love'), Js('Luck'), Js('Majesty'), Js('Mercy'), Js('Mirth'), Js('Nourish'), Js('Nurture'), Js('Paradise'), Js('Parry'), Js('Passion'), Js('Piety'), Js('Prestige'), Js('Pride'), Js('Privilege'), Js('Promise'), Js('Purity'), Js('Redemption'), Js('Reliance'), Js('Remedy'), Js('Resistance'), Js('Respect'), Js('Return'), Js('Revolution'), Js('Safeguard'), Js('Salvation'), Js('Sanctuary'), Js('Solitude'), Js('Supremacy'), Js('Sweetness'), Js('Sympathy'), Js('Synthesis'), Js('Tribute'), Js('Triumph'), Js('Trust'), Js('Truth'), Js('Unity'), Js('Utopia'), Js('Victory'), Js('Vindicate'), Js('Virtue'), Js('Wish'), Js('Wonder'), Js('Zeal'), Js('Zion')]))
var.put('names2', Js([Js('Abolition'), Js('Abyss'), Js('Agony'), Js('Anarchy'), Js('Animus'), Js('Annihilation'), Js('Apathy'), Js('Assassin'), Js('Aversion'), Js('Bane'), Js('Betrayal'), Js('Blaze'), Js('Blockade'), Js('Calamity'), Js('Carnage'), Js('Chaos'), Js('Condemned'), Js('Cruelty'), Js('Decimation'), Js('Defeat'), Js('Delirium'), Js('Demolition'), Js('Denial'), Js('Desertion'), Js('Desolation'), Js('Despair'), Js('Destruction'), Js('Detention'), Js('Disarray'), Js('Disbelief'), Js('Disgrace'), Js('Dishonor'), Js('Disruption'), Js('Disunion'), Js('Dominance'), Js('Doom'), Js('Doubt'), Js('Downfall'), Js('Elimination'), Js('Entropy'), Js('Eternity'), Js('Extermination'), Js('Extinction'), Js('Fear'), Js('Ferocity'), Js('Fluke'), Js('Forfeit'), Js('Forsake'), Js('Frenzy'), Js('Fury'), Js('Hallow'), Js('Hate'), Js('Hatred'), Js('Havoc'), Js('Hazard'), Js('Hostility'), Js('Hysteria'), Js('Impotence'), Js('Inferno'), Js('Injury'), Js('Isolation'), Js('Limbo'), Js('Malevolence'), Js('Malice'), Js('Mania'), Js('Massacre'), Js('Mayhem'), Js('Melancholy'), Js('Misfortune'), Js('Murder'), Js('Nether'), Js('Nightmare'), Js('Obstruction'), Js('Overlook'), Js('Peril'), Js('Pity'), Js('Poverty'), Js('Prohibition'), Js('Rage'), Js('Rampage'), Js('Ravage'), Js('Relinquish'), Js('Restraint'), Js('Riot'), Js('Sanctity'), Js('Shatter'), Js('Silence'), Js('Slaughter'), Js('Slayer'), Js('Sorrow'), Js('Spite'), Js('Stigma'), Js('Storm'), Js('Struggle'), Js('Submission'), Js('Surrender'), Js('Torment'), Js('Treachery'), Js('Turmoil'), Js('Umbrage'), Js('Uproar'), Js('Venom'), Js('Violence'), Js('Void'), Js('Wasteland'), Js('Wilderness'), Js('Woe'), Js('Worship'), Js('Wrath'), Js('Wreckage')]))
var.put('names3', Js([Js('Alpha'), Js('Alpine'), Js('Altar'), Js('Angel'), Js('Angel Wings'), Js('Anomaly'), Js('Aqua'), Js('Aquamarine'), Js('Arachnid'), Js('Arrowtip'), Js('Astro'), Js('Aurora'), Js('Avalanche'), Js('Azure'), Js('Bandana'), Js('Bear Paw'), Js('Black Crow'), Js('Blue Banner'), Js('Boulderfist'), Js('Braveheart'), Js('Brown Bear'), Js('Bullet'), Js('Bullettooth'), Js('Bumblebee'), Js('Butterfly'), Js('Cannonball'), Js('Castaway'), Js('Comet'), Js('Coyote'), Js('Crescent Moon'), Js('Crimson'), Js('Crossbow'), Js('Daemon'), Js('Darkwind'), Js('Dawn'), Js('Daybreak'), Js('Daylight'), Js('Demon'), Js('Diamond'), Js('Dragonfire'), Js('Dragonfly'), Js('Dragontooth'), Js('Dusk'), Js('Eagle Eye'), Js('Ebony'), Js('Echo'), Js('Eclipse'), Js('Effigy'), Js('Emerald'), Js('Energy'), Js('Enigma'), Js('Eventide'), Js('Fable'), Js('Falcon'), Js('Fallen Oak'), Js('Firefly'), Js('Frozen Lake'), Js('Full Moon'), Js('Gadget'), Js('Gemini'), Js('Gizmo'), Js('Glacier'), Js('Grasshopper'), Js('Heartbreak'), Js('Heartfire'), Js('High Tide'), Js('Highlands'), Js('Howling Wolf'), Js('Hummingbird'), Js('Hurricane'), Js('Ivory'), Js('Jadefire'), Js('Jasmine'), Js('Jester'), Js('Kite Shield'), Js('Light Beacon'), Js('Lightning'), Js('Lightning Strike'), Js('Lion Roar'), Js('Lockdown'), Js('Lockheart'), Js('Lone Wolf'), Js('Maggot'), Js('Major'), Js('Malachite'), Js('Maple Leaf'), Js('Maverick'), Js('Merlin'), Js('Midnight'), Js('Minor'), Js('Mirage'), Js('Mirror Image'), Js('Monsoon'), Js('Moonstone'), Js('Morningstar'), Js('Mountain Peak'), Js('Nemo'), Js('New Moon'), Js('Night Beacon'), Js('Night Owl'), Js('Nightfall'), Js('Nighttide'), Js('Omega'), Js('Open Door'), Js('Overlook'), Js('Pedestal'), Js('Phantasm'), Js('Phoenix'), Js('Quicksilver'), Js("Rabbit's Foot"), Js('Radiance'), Js('Raindrop'), Js('Red Banner'), Js('Saffron'), Js('Sapphire'), Js('Satellite'), Js('Scarlet'), Js('Serpent'), Js('Shark Fin'), Js('Shooting Star'), Js('Silver Lining'), Js('Silver Shadow'), Js('Snowflake'), Js('Solar Beam'), Js('Solar Flare'), Js('Solstice'), Js('Stardust'), Js('Starfall'), Js('Starlight'), Js('Stormgaze'), Js('Straight Arrow'), Js('Sundance'), Js('Sundown'), Js('Sunset'), Js('Sunshine'), Js('Thunderclap'), Js('Thunderstorm'), Js('Tiger Claw'), Js('Tiger Lilly'), Js('Torchbearer'), Js('Tortoise'), Js('Turtle Shell'), Js('Twilight'), Js('Viper'), Js('Waterfall'), Js('Whisper'), Js('Wild Card'), Js('Wild Horse'), Js('Willow'), Js('Woodpecker')]))
pass
pass


# Add lib to the module scope
campNames = var.to_python()
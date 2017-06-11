__all__ = ['hqNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (Js('The ')+var.get('nm3').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abyss'), Js('Allegiance'), Js('Animus'), Js('Argent'), Js('August'), Js('Basilisk'), Js("Blood's"), Js('Bravery'), Js('Brotherhood'), Js('Paradise'), Js('Bulwark'), Js('Cardinal'), Js('Bloodlust'), Js('Bloodfall'), Js('Bloodmoon'), Js('Deepwood'), Js('Dragonclaw'), Js('Dragontooth'), Js('Dreamland'), Js('Ironbark'), Js('Liontooth'), Js('Thunderstorm'), Js('Blackwing'), Js('Stormkeeper'), Js('Archangel'), Js('Dynasty'), Js('Nemesis'), Js('Blackout'), Js('Illusion'), Js('Soulseeker'), Js('Nemo'), Js('Ironwing'), Js('Ashes'), Js('Fullmoon'), Js('Diablo'), Js('Clockwork'), Js('Otherworld'), Js('Winterspell'), Js('Juggernaut'), Js('Whiteheart'), Js('Starfall'), Js('Starlight'), Js('Nova'), Js('Requiem'), Js('Armada'), Js('Ironheart'), Js('Stormwatch'), Js('Vanguard'), Js('Battlestar'), Js('Miracle'), Js('Lifeblood'), Js('Compass'), Js('Nightsong'), Js('Vengeance'), Js('Starchild'), Js('Moonsong'), Js('Shadowsong'), Js('Shadowheart'), Js('Dragonland'), Js('Dragonfire'), Js('Destiny'), Js('Stormkeeper'), Js('Battleborn'), Js('Salvation'), Js('Flameheart'), Js('Stonebend'), Js('Ironscream'), Js('Shademantle'), Js('Hallowflame'), Js('Mastervale'), Js('Doomvale'), Js('Doomwhisper'), Js('Burningtide'), Js('Blackhallow'), Js('Sacredcrest'), Js('Sungazer'), Js('Moongazer'), Js('Saurhorn'), Js('Highbreeze'), Js('Stormbreath'), Js('Frostvale'), Js('Starchaser'), Js('Embermane'), Js('Cresthelm'), Js('Whiteblood'), Js('Runeforge'), Js('Spiritcrest'), Js('Cloudspire'), Js('Brightforest'), Js('Coldhammer'), Js('Skysword'), Js('Skyward'), Js('Battlebloom'), Js('Crimsonblade'), Js('Amberwood'), Js('Frostwolf'), Js('Flamewarden'), Js('Stormweaver'), Js('Lunacrest'), Js('Solarcrest'), Js('Skullcrest'), Js('Frozenhell'), Js('Cinderbane'), Js('Moonblade'), Js('Winterwatch'), Js('Crimsonwatch'), Js('Summerguard'), Js('Autumnward'), Js('Springforge'), Js('Shadowhorn'), Js('Titanrun'), Js('Darksong'), Js('Whispervale'), Js('Swiftstrike'), Js('Pathfinder'), Js('Vagabond'), Js('Trailblazer'), Js('Centurion'), Js('Sentinel'), Js('Shepherd'), Js('Watchdog'), Js('Curator'), Js('Cerberus'), Js('Steward'), Js('Custodian'), Js('Overseer'), Js('Gamekeeper'), Js('Chaos'), Js('Cinder'), Js('Cobalt'), Js('Conquest'), Js("Creed's"), Js('Crossroad'), Js('Dawn'), Js('Daydream'), Js("Death's"), Js('Demise'), Js('Desolation'), Js('Dragon'), Js('Dusk'), Js('Echo'), Js('Eclipse'), Js('Elysium'), Js('Ember'), Js('Enigma'), Js('Epoch'), Js('Exile'), Js('Exodus'), Js('Falcon'), Js('Fortitude'), Js('Freedom'), Js('Fury'), Js('Galaxy'), Js('Glory'), Js('Grace'), Js('Grim'), Js('Harbinger'), Js('Harmony'), Js("Heaven's"), Js('Herald'), Js("Honor's"), Js("Hope's"), Js('Independence'), Js('Judgement'), Js('Justice'), Js('Karma'), Js('Liberty'), Js("Light's"), Js('Memorial'), Js('Mercy'), Js('Mirage'), Js('Mirror'), Js('Nexus'), Js('Oblivion'), Js('Oracle'), Js('Outcast'), Js('Phoenix'), Js('Pilgrimage'), Js('Pinnacle'), Js('Plague'), Js('Premonition'), Js('Promise'), Js('Prophecy'), Js('Purpose'), Js('Rebirth'), Js('Renegade'), Js('Revelation'), Js('Sabre'), Js('Salvation'), Js('Serenity'), Js('Serpent'), Js('Shadow'), Js("Shadow's"), Js('Sisterhood'), Js('Solace'), Js('Solitude'), Js('Solstice'), Js('Specter'), Js('Spirit'), Js('Tempest'), Js('The Adamantine'), Js('The Amaranthine'), Js('The Amber'), Js('The Ancestral'), Js('The Arcane'), Js('The Astral'), Js('The Azure'), Js('The Black'), Js('The Blessed'), Js('The Bronze'), Js('The Celestial'), Js('The Cerulean'), Js('The Crescent'), Js('The Crimson'), Js('The Crystal'), Js('The Divine'), Js('The Ebon'), Js('The Emerald'), Js('The Eternal'), Js('The Ethereal'), Js('The Fel'), Js('The Frozen'), Js('The Granite'), Js('The Grim'), Js('The Hallow'), Js('The Infernal'), Js('The Invincible'), Js('The Invisible'), Js('The Iron'), Js('The Ivory'), Js('The Jade'), Js('The Lost'), Js('The Matriarch'), Js('The Misty'), Js('The Mithril'), Js('The Molten'), Js('The Moon'), Js('The Mythic'), Js('The Nether'), Js('The Night'), Js('The Nightmare'), Js('The Obsidian'), Js('The Onyx'), Js('The Patriarch'), Js('The Sanguine'), Js('The Scarlet'), Js('The Shadow'), Js('The Silent'), Js('The Silver'), Js('The Solar'), Js('The Sun'), Js('The Titan'), Js('The Velvet'), Js('The Violet'), Js('The Vortex'), Js('Thunder'), Js("Titan's"), Js('Tranquility'), Js('Tribute'), Js('Triumph'), Js('Utopia'), Js('Vengeance'), Js('Victory'), Js('Virtue'), Js('Vitality'), Js('Warden'), Js("Watcher's"), Js('Wisdom')]))
var.put('nm2', Js([Js('Base'), Js('Bastion'), Js('Castle'), Js('Citadel'), Js('Estate'), Js('Fortress'), Js('Garrison'), Js('Harbor'), Js('Headquarters'), Js('Island'), Js('Isle'), Js('Keep'), Js('Manor'), Js('Mansion'), Js('Post'), Js('Sanctuary'), Js('Sanctum'), Js('Station'), Js('Stronghold'), Js('Tower'), Js('Towers'), Js('Watchtower')]))
var.put('nm3', Js([Js('Abyss'), Js('Aerie'), Js('Animus'), Js('Anomaly'), Js('Anvil'), Js('Apex'), Js('Archetype'), Js('Armada'), Js('Asteroid'), Js('Asylum'), Js('Aurora'), Js('Bastion'), Js('Beacon'), Js('Bulwark'), Js('Burrow'), Js('Cardinal'), Js('Centurion'), Js('Citadel'), Js('Clover'), Js('Compass'), Js('Crescent'), Js('Curiosity'), Js('Dragonclaw'), Js('Echo'), Js('Eclipse'), Js('Elysium'), Js('Ender'), Js('Enterprise'), Js('Epoch'), Js('Exodus'), Js('Felicity'), Js('Garden'), Js('Glory'), Js('Hammer'), Js('Haven'), Js('Heart'), Js('Homage'), Js('Horoscope'), Js('Jewel'), Js('Jubilee'), Js('Juggernaut'), Js('Lament'), Js('Lodestar'), Js('Majesty'), Js('Marshal'), Js('Matriarch'), Js('Matron'), Js('Memento'), Js('Minaret'), Js('Miracle'), Js('Mirage'), Js('Monolith'), Js('Nemesis'), Js('Nest'), Js('Nexus'), Js('Oasis'), Js('Obelisk'), Js('Odyssey'), Js('Omen'), Js('Onyx'), Js('Oracle'), Js('Ornament'), Js('Outcast'), Js('Paradox'), Js('Paragon'), Js('Patriarch'), Js('Patron'), Js('Phenomenon'), Js('Phoenix'), Js('Pinnacle'), Js('Prodigy'), Js('Pyre'), Js('Razor'), Js('Requiem'), Js('Sanctum'), Js('Serenity'), Js('Snowflake'), Js('Solstice'), Js('Spectacle'), Js('Spire'), Js('Talon'), Js('Tempest'), Js('Torch'), Js('Tribute'), Js('Triumph'), Js('Twin'), Js('Utopia'), Js('Veil'), Js('Vendetta'), Js('Vertex'), Js('Void'), Js('Vortex'), Js('Zenith')]))
pass
pass


# Add lib to the module scope
hqNames = var.to_python()
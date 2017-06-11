__all__ = ['shieldNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2')))+Js(' '))+var.get('nm4').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((var.get('nm7').get(var.get('rnd'))+Js(', '))+var.get('nm5').get(var.get('rnd2')))+Js(' '))+var.get('nm6').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aegeus'), Js('Alpha'), Js('Amnesia'), Js('Anguish'), Js('Apocalypse'), Js('Armageddon'), Js('Barrage'), Js('Bear'), Js('Behemoth'), Js('Berg'), Js('Betrayal'), Js('Blackest Heart'), Js('Blackout'), Js('Blazeguard'), Js('Blind Hate'), Js('Blind Hatred'), Js('Bloodlust'), Js('Bombardment'), Js('Broken Promise'), Js('Calamity'), Js('Cataclysm'), Js('Catastrophe'), Js('Cerberus'), Js('Chaos'), Js('Chasm'), Js('Coliseum'), Js('Colossus'), Js('Combustion'), Js('Cometfall'), Js('Convergence'), Js('Curator'), Js('Cyclone'), Js('Darkheart'), Js('Darkness'), Js('Dawn'), Js('Dawnbreaker'), Js('Dawnguard'), Js("Death's Bargain"), Js("Death's Deflection"), Js("Death's Touch"), Js('Deathgate'), Js('Deluge'), Js('Desolation'), Js('Despair'), Js("Destiny's Song"), Js("Destiny's Will"), Js('Devinity'), Js('Divine Light'), Js('Domination'), Js('Doom'), Js('Dragonheart'), Js('Dragonscale'), Js('Due Diligence'), Js('Dusk'), Js('Ebony'), Js('Echo'), Js('Eclipse'), Js('Enforcer'), Js('Enigma'), Js('Epilogue'), Js('Eruption'), Js('Eulogy'), Js('Extinction'), Js('Face of Death'), Js('Face of Insanity'), Js('Faithkeeper'), Js('Fate'), Js('Final Favor'), Js('Ghostwalker'), Js('Glacier'), Js('Glimmer'), Js('Gloom'), Js('Headache'), Js("Hell's Scream"), Js("Hero's Calling"), Js("Hero's Stand"), Js("Hero's Surrender"), Js("Honor's Call"), Js("Honor's End"), Js("Honor's Grasp"), Js("Honor's Guard"), Js("Honor's Pride"), Js("Honor's Will"), Js('Hope'), Js('Interrogator'), Js('Ironbark'), Js('Ivory'), Js('Justice'), Js("King's Defender"), Js("King's Honor"), Js("King's Legacy"), Js("Kingdom's Heart"), Js("Kingdom's Honor"), Js("Kingdom's Pride"), Js("Knight's Fall"), Js('Knightfall'), Js('Lament'), Js('Last Rites'), Js('Last Words'), Js('Lazarus'), Js('Lightbringer'), Js('Limbo'), Js('Lionheart'), Js('Lost Paradise'), Js('Loyalty'), Js('Maelstrom'), Js('Malice'), Js('Mercy'), Js("Misery's End"), Js('Monster'), Js('Moonlight'), Js('Nethersbane'), Js("Night's End"), Js("Night's Fall"), Js('Nightbane'), Js('Nightfall'), Js('Nirvana'), Js('Oathbreaker'), Js('Oathkeeper'), Js('Oathsworn'), Js('Oblivion'), Js('Ogre'), Js('Omega'), Js('Overture'), Js('Painkiller'), Js('Path of Exile'), Js('Peace Maker'), Js('Peacekeeper'), Js('Perfect Storm'), Js('Permission'), Js('Persuasion'), Js('Prelude'), Js("Pride's Honor"), Js('Prologue'), Js('Purifier'), Js('Rage'), Js('Ragnarok'), Js('Rand'), Js('Reckoning'), Js('Red Dwarf'), Js('Redemption'), Js('Reign Breaker'), Js('Reign Maker'), Js('Remorse'), Js('Requiem'), Js('Retirement'), Js('Ruin'), Js('Rumpel Steelskin'), Js('Sanctify'), Js('Scar'), Js('Selfreflection'), Js('Shepherd'), Js('Shroud'), Js('Sierra'), Js('Silence'), Js('Silverlight'), Js('Skullcrusher'), Js('Stalker'), Js('Starlight'), Js('Steelskin'), Js('Storm'), Js('Storm Breaker'), Js('Stormbringer'), Js('Stormcaller'), Js('Sunward'), Js('Supernova'), Js('Supremacy'), Js('Suspension'), Js('Swan Song'), Js('The Abyss'), Js('The Ambassador'), Js('The Barricade'), Js('The Beast'), Js('The Black Hole'), Js('The Blockade'), Js('The Boon'), Js('The Brute'), Js('The Curator'), Js('The End'), Js('The Grand Slam'), Js('The Iron Maid'), Js('The Iron Maiden'), Js('The Keeper'), Js('The Light'), Js('The Mirror'), Js('The Mountain'), Js('The Observer'), Js('The Oculus'), Js('The Righteous'), Js('The Sentinel'), Js('The Sentry'), Js('The Shadow'), Js('The Titan'), Js('The Voice'), Js('The Void'), Js('Thunder'), Js('Thundercloud'), Js('Torrent'), Js('Tranquility'), Js('Treachery'), Js('Trinity'), Js('Triumph'), Js('Truthbreaker'), Js('Typhoon'), Js('Tyranny'), Js('Vacancy'), Js('Vacuum'), Js('Valkyrie'), Js('Vanquisher'), Js('Vengeance'), Js('Vigilant'), Js('Vigilante'), Js('Voice of Honor'), Js('Voice of Insanity'), Js('Voice of Madness'), Js('Voice of Pride'), Js('Voice of Reason'), Js('Volcano'), Js('Vortex'), Js('Wall of Honor'), Js('Wall of Insanity'), Js('Wall of Madness'), Js('Wall of Pain'), Js('Wall of Pride'), Js('Wall of Sorrow'), Js('Wall of the Dead'), Js('Warcry'), Js('Warmonger'), Js('Warsong'), Js('Willbreaker'), Js("Wisdom's Grasp"), Js("Wisdom's Hold"), Js("Wit's End"), Js('Witherbrand')]))
var.put('nm2', Js([Js('Ancient'), Js('Antique'), Js('Arcane'), Js('Atuned'), Js("Bandit's"), Js('Baneful'), Js('Banished'), Js('Barbarian'), Js('Barbaric'), Js('Battleworn'), Js('Blood Infused'), Js('Blood-Forged'), Js('Bloodcursed'), Js('Bloodied'), Js("Bloodlord's"), Js('Bloodsurge'), Js('Bloodvenom'), Js('Brutal'), Js('Brutality'), Js('Burnished'), Js("Captain's"), Js('Cataclysm'), Js('Cataclysmic'), Js('Challenger'), Js("Challenger's"), Js('Champion'), Js("Champion's"), Js('Cold-Forged'), Js('Conqueror'), Js("Conqueror's"), Js('Corroded'), Js('Corrupted'), Js('Crazed'), Js('Crying'), Js('Curator'), Js('Cursed'), Js('Curved'), Js('Dancing'), Js('Defender'), Js("Defender's"), Js('Defiled'), Js('Deluded'), Js('Demonic'), Js('Deserted'), Js("Desire's"), Js('Desolation'), Js("Destiny's"), Js('Dire'), Js('Doom'), Js("Doom's"), Js("Dragon's"), Js('Dragonbreath'), Js('Ebon'), Js('Eerie'), Js('Enchanted'), Js('Engraved'), Js('Eternal'), Js('Exiled'), Js('Extinction'), Js("Faith's"), Js('Faithful'), Js('Fancy'), Js('Fearful'), Js('Feral'), Js('Fierce'), Js('Fiery'), Js('Fire Infused'), Js('Firesoul'), Js('Flimsy'), Js('Forsaken'), Js("Fortune's"), Js('Fragile'), Js('Frail'), Js('Frenzied'), Js('Frost'), Js('Frozen'), Js('Furious'), Js('Fusion'), Js('Ghastly'), Js('Ghost-Forged'), Js('Ghostly'), Js('Gladiator'), Js("Gladiator's"), Js('Grieving'), Js("Guard's"), Js("Guardian's"), Js('Hailstorm'), Js('Hateful'), Js('Haunted'), Js('Heartless'), Js('Hero'), Js("Hero's"), Js('Hollow'), Js('Holy'), Js('Honed'), Js("Honor's"), Js("Hope's"), Js('Hopeless'), Js('Howling'), Js('Hungering'), Js('Improved'), Js('Incarnated'), Js('Infused'), Js('Inherited'), Js('Isolated'), Js('Jade Infused'), Js('Judgement'), Js("Keeper's"), Js('Knightly'), Js("Legionnaire's"), Js("Liar's"), Js('Lich'), Js('Lightning'), Js('Lonely'), Js('Loyal'), Js('Lustful'), Js('Lusting'), Js('Malevolent'), Js('Malicious'), Js('Malignant'), Js('Massive'), Js('Mended'), Js('Mercenary'), Js('Military'), Js("Misfortune's"), Js('Mourning'), Js('Nightmare'), Js("Oathkeeper's"), Js('Ominous'), Js('Peacekeeper'), Js("Peacekeeper's"), Js('Phantom'), Js('Polished'), Js('Possessed'), Js("Pride's"), Js('Prideful'), Js('Primal'), Js('Prime'), Js('Primitive'), Js('Promised'), Js("Protector's"), Js('Proud'), Js("Recruit's"), Js('Reforged'), Js('Reincarnated'), Js('Relentless'), Js('Remorseful'), Js('Renewed'), Js('Renovated'), Js('Replica'), Js('Restored'), Js('Retribution'), Js('Ritual'), Js('Roaring'), Js('Ruby Infused'), Js('Rune-Forged'), Js('Savage'), Js('Sentinel'), Js('Shadow'), Js('Silent'), Js('Singing'), Js('Sinister'), Js('Skyfall'), Js('Smooth'), Js("Soldier's"), Js("Solitude's"), Js("Sorrow's"), Js('Soul'), Js('Soul Infused'), Js('Soul-Forged'), Js('Soulless'), Js('Spectral'), Js('Spiteful'), Js('Storm'), Js('Storm-Forged'), Js('Stormfury'), Js('Stormguard'), Js('Terror'), Js('Thirsting'), Js('Thirsty'), Js('Thunder'), Js('Thunder-Forged'), Js('Thunderfury'), Js('Thunderguard'), Js('Thundersoul'), Js('Thunderstorm'), Js('Timeworn'), Js('Tormented'), Js("Trainee's"), Js("Treachery's"), Js('Twilight'), Js("Twilight's"), Js('Twisted'), Js('Tyrannical'), Js('Undead'), Js('Unholy'), Js('Vanquisher'), Js('Vengeance'), Js('Vengeful'), Js('Venom'), Js('Vicious'), Js('Victor'), Js('Vindication'), Js('Vindicator'), Js('Vindictive'), Js('Volcanic'), Js('Vowed'), Js('War-Forged'), Js("Warden's"), Js("Warlord's"), Js('Warp'), Js('Warped'), Js('Warrior'), Js("Warrior's"), Js('Whistling'), Js('Wicked'), Js("Wind's"), Js('Wind-Forged'), Js('Windsong'), Js('Woeful'), Js('Wrathful'), Js('Wretched'), Js('Yearning'), Js('Zealous')]))
var.put('nm3', Js([Js('Adamantite'), Js('Ashwood'), Js('Bone'), Js('Bronze'), Js('Bronzed'), Js('Copper'), Js('Ivory'), Js('Ebon'), Js('Glass'), Js('Golden'), Js('Hardwood'), Js('Iron'), Js('Ironbark'), Js('Maple'), Js('Mithril'), Js('Oak'), Js('Obsidian'), Js('Redwood'), Js('Silver'), Js('Skeletal'), Js('Steel'), Js('Titanium'), Js('Warpwood'), Js('Willow'), Js('Yew')]))
var.put('nm4', Js([Js('Shield'), Js('Bulwark'), Js('Carapace'), Js('Ward'), Js('Wall'), Js('Visage'), Js('Armament'), Js('Barrier'), Js('Greatshield'), Js('Barricade'), Js('Blockade'), Js('Kite Shield'), Js('Buckler'), Js('Heater'), Js('Light Shield'), Js('Heavy Shield'), Js('Tower Shield'), Js('Shield Wall'), Js('Buffer'), Js('Guard'), Js('Aegis'), Js('Warden'), Js('Guardian'), Js('Keeper'), Js('Defender'), Js('Bastion')]))
var.put('nm5', Js([Js('Aegis'), Js('Angel'), Js('Armament'), Js('Bane'), Js('Barricade'), Js('Barrier'), Js('Bastion'), Js('Blockade'), Js('Bond'), Js('Boon'), Js('Breaker'), Js('Bringer'), Js('Buckler'), Js('Buffer'), Js('Bulwark'), Js('Call'), Js('Caretaker'), Js('Champion'), Js('Conqueror'), Js('Conservator'), Js('Crusader'), Js('Cry'), Js('Cunning'), Js('Curator'), Js('Dawn'), Js('Defender'), Js('Defiler'), Js('Deflector'), Js('Destroyer'), Js('Emissary'), Js('Ender'), Js('Favor'), Js('Ferocity'), Js('Foe'), Js('Gift'), Js('Glory'), Js('Greatshield'), Js('Guard'), Js('Guardian'), Js('Heater'), Js('Heavy Shield'), Js('Heirloom'), Js('Hero'), Js('Hope'), Js('Incarnation'), Js('Keeper'), Js('Kite Shield'), Js('Last Hope'), Js('Last Stand'), Js('Legacy'), Js('Light Shield'), Js('Memory'), Js('Might'), Js('Oath'), Js('Pact'), Js('Pledge'), Js('Promise'), Js('Protection'), Js('Protector'), Js('Reach'), Js('Savagery'), Js('Secret'), Js('Shepherd'), Js('Shield'), Js('Shield Wall'), Js('Soul'), Js('Steward'), Js('Terror'), Js('Token'), Js('Tower Shield'), Js('Tribute'), Js('Vengeance'), Js('Vindicator'), Js('Visage'), Js('Voice'), Js('Wall'), Js('Ward'), Js('Warden'), Js('Whisper'), Js('Wit')]))
var.put('nm6', Js([Js('of Agony'), Js('of Ancient Power'), Js('of Anguish'), Js('of Ashes'), Js('of Assassins'), Js('of Black Magic'), Js('of Blessed Fortune'), Js('of Blessings'), Js('of Blight'), Js('of Blood'), Js('of Bloodlust'), Js('of Broken Bones'), Js('of Broken Dreams'), Js('of Broken Families'), Js('of Burdens'), Js('of Chaos'), Js('of Closing Eyes'), Js('of Conquered Worlds'), Js('of Corruption'), Js('of Cruelty'), Js('of Cunning'), Js('of Dark Magic'), Js('of Dark Souls'), Js('of Darkness'), Js('of Decay'), Js('of Deception'), Js('of Degradation'), Js('of Delusions'), Js('of Denial'), Js('of Desecration'), Js('of Diligence'), Js('of Dismay'), Js('of Dragonsouls'), Js('of Due Diligence'), Js('of Echoes'), Js('of Ended Dreams'), Js('of Ending Hope'), Js('of Ending Misery'), Js('of Eternal Bloodlust'), Js('of Eternal Damnation'), Js('of Eternal Glory'), Js('of Eternal Justice'), Js('of Eternal Rest'), Js('of Eternal Sorrow'), Js('of Eternal Struggles'), Js('of Eternity'), Js('of Executions'), Js('of Faded Memories'), Js('of Fallen Souls'), Js('of Fools'), Js('of Frost'), Js('of Frozen Hells'), Js('of Fury'), Js('of Giants'), Js('of Giantslaying'), Js('of Grace'), Js('of Grieving Widows'), Js('of Hate'), Js('of Hatred'), Js("of Hell's Games"), Js('of Hellish Torment'), Js('of Heroes'), Js('of Holy Might'), Js('of Honor'), Js('of Hope'), Js('of Horrid Dreams'), Js('of Horrors'), Js('of Illuminated Dreams'), Js('of Illumination'), Js('of Immortality'), Js('of Inception'), Js('of Infinite Trials'), Js('of Insanity'), Js('of Invocation'), Js('of Justice'), Js("of Light's Hope"), Js('of Lost Comrades'), Js('of Lost Hope'), Js('of Lost Voices'), Js('of Lost Worlds'), Js('of Magic'), Js('of Mercy'), Js('of Misery'), Js('of Mountains'), Js('of Mourning'), Js('of Mystery'), Js('of Necromancy'), Js('of Nightmares'), Js('of Oblivion'), Js('of Perdition'), Js('of Phantoms'), Js('of Power'), Js('of Pride'), Js("of Pride's Fall"), Js('of Putrefaction'), Js('of Reckoning'), Js('of Redemption'), Js('of Regret'), Js('of Riddles'), Js('of Secrecy'), Js('of Secrets'), Js('of Shadow Strikes'), Js('of Shadows'), Js('of Shifting Sands'), Js('of Shifting Worlds'), Js('of Silence'), Js('of Slaughter'), Js('of Souls'), Js('of Stealth'), Js('of Storms'), Js('of Subtlety'), Js('of Suffering'), Js("of Suffering's End"), Js('of Summoning'), Js('of Terror'), Js('of Thunder'), Js('of Time-Lost Memories'), Js('of Timeless Battles'), Js('of Titans'), Js('of Torment'), Js('of Traitors'), Js('of Trembling Hands'), Js('of Trials'), Js('of Truth'), Js("of Twilight's End"), Js('of Twisted Visions'), Js('of Unholy Blight'), Js('of Unholy Might'), Js('of Vengeance'), Js('of Visions'), Js('of Wasted Time'), Js('of Widows'), Js('of Wizardry'), Js('of Woe'), Js('of Wraiths'), Js('of Zeal'), Js('of the Ancients'), Js('of the Banished'), Js('of the Basilisk'), Js('of the Beast'), Js('of the Blessed'), Js('of the Breaking Storm'), Js('of the Brotherhood'), Js('of the Burning Sun'), Js('of the Caged Mind'), Js('of the Cataclysm'), Js('of the Champion'), Js('of the Claw'), Js('of the Corrupted'), Js('of the Covenant'), Js('of the Crown'), Js('of the Damned'), Js('of the Daywalker'), Js('of the Dead'), Js('of the Depth'), Js('of the Dreadlord'), Js('of the Earth'), Js('of the East'), Js('of the Emperor'), Js('of the Empty Void'), Js('of the End'), Js('of the Enigma'), Js('of the Fallen'), Js('of the Falling Sky'), Js('of the Flame'), Js('of the Forest'), Js('of the Forgotten'), Js('of the Forsaken'), Js('of the Gladiator'), Js('of the Harvest'), Js('of the Immortal'), Js('of the Incoming Storm'), Js('of the Insane'), Js('of the King'), Js('of the Lasting Night'), Js('of the Leviathan'), Js('of the Light'), Js('of the Lion'), Js('of the Lionheart'), Js('of the Lone Victor'), Js('of the Lone Wolf'), Js('of the Lost'), Js('of the Moon'), Js('of the Moonwalker'), Js('of the Night Sky'), Js('of the Night'), Js('of the Nightstalker'), Js('of the North'), Js('of the Occult'), Js('of the Oracle'), Js('of the Phoenix'), Js('of the Plague'), Js('of the Prince'), Js('of the Protector'), Js('of the Queen'), Js('of the Serpent'), Js('of the Setting Sun'), Js('of the Shadows'), Js('of the Sky'), Js('of the South'), Js('of the Stars'), Js('of the Storm'), Js('of the Summoner'), Js('of the Sun'), Js('of the Sunwalker'), Js('of the Talon'), Js('of the Undying'), Js('of the Victor'), Js('of the Void'), Js('of the West'), Js('of the Whispers'), Js('of the Wicked'), Js('of the Wind'), Js('of the Wolf'), Js('of the World'), Js('of the Wretched')]))
var.put('nm7', Js([Js('Aegeus'), Js('Alpha'), Js('Amnesia'), Js('Anguish'), Js('Apocalypse'), Js('Armageddon'), Js('Barrage'), Js('Bear'), Js('Behemoth'), Js('Berg'), Js('Betrayal'), Js('Blackout'), Js('Blazeguard'), Js('Blind Hate'), Js('Blind Hatred'), Js('Bloodlust'), Js('Bombardment'), Js('Broken Promise'), Js('Calamity'), Js('Cataclysm'), Js('Catastrophe'), Js('Cerberus'), Js('Chaos'), Js('Chasm'), Js('Coliseum'), Js('Colossus'), Js('Combustion'), Js('Cometfall'), Js('Convergence'), Js('Curator'), Js('Cyclone'), Js('Darkheart'), Js('Darkness'), Js('Dawn'), Js('Dawnbreaker'), Js('Dawnguard'), Js("Death's Bargain"), Js('Deathgate'), Js('Deluge'), Js('Desolation'), Js('Despair'), Js("Destiny's Song"), Js("Destiny's Will"), Js('Devinity'), Js('Divine Light'), Js('Domination'), Js('Doom'), Js('Dragonheart'), Js('Dragonscale'), Js('Due Diligence'), Js('Dusk'), Js('Ebony'), Js('Echo'), Js('Eclipse'), Js('Enforcer'), Js('Enigma'), Js('Epilogue'), Js('Eruption'), Js('Eulogy'), Js('Extinction'), Js('Faithkeeper'), Js('Fate'), Js('Final Favor'), Js('Ghostwalker'), Js('Glacier'), Js('Glimmer'), Js('Gloom'), Js('Headache'), Js("Hell's Scream"), Js("Hero's Calling"), Js("Hero's Stand"), Js("Hero's Surrender"), Js("Honor's Call"), Js("Honor's End"), Js("Honor's Grasp"), Js("Honor's Guard"), Js("Honor's Pride"), Js("Honor's Will"), Js('Hope'), Js('Interrogator'), Js('Ironbark'), Js('Ivory'), Js('Justice'), Js("King's Defender"), Js("King's Honor"), Js("King's Legacy"), Js("Kingdom's Heart"), Js("Kingdom's Honor"), Js("Kingdom's Pride"), Js("Knight's Fall"), Js('Knightfall'), Js('Lament'), Js('Last Rites'), Js('Last Words'), Js('Lazarus'), Js('Lightbringer'), Js('Limbo'), Js('Lionheart'), Js('Lost Paradise'), Js('Loyalty'), Js('Maelstrom'), Js('Malice'), Js('Mercy'), Js("Misery's End"), Js('Monster'), Js('Moonlight'), Js('Nethersbane'), Js("Night's End"), Js("Night's Fall"), Js('Nightbane'), Js('Nightfall'), Js('Nirvana'), Js('Oathbreaker'), Js('Oathkeeper'), Js('Oathsworn'), Js('Oblivion'), Js('Ogre'), Js('Omega'), Js('Overture'), Js('Painkiller'), Js('Path of Exile'), Js('Peace Maker'), Js('Peacekeeper'), Js('Perfect Storm'), Js('Permission'), Js('Persuasion'), Js('Prelude'), Js("Pride's Honor"), Js('Prologue'), Js('Purifier'), Js('Rage'), Js('Ragnarok'), Js('Rand'), Js('Reckoning'), Js('Red Dwarf'), Js('Redemption'), Js('Reign Breaker'), Js('Reign Maker'), Js('Remorse'), Js('Requiem'), Js('Retirement'), Js('Ruin'), Js('Sanctify'), Js('Scar'), Js('Shepherd'), Js('Shroud'), Js('Sierra'), Js('Silence'), Js('Silverlight'), Js('Skullcrusher'), Js('Stalker'), Js('Starlight'), Js('Steelskin'), Js('Storm'), Js('Storm Breaker'), Js('Stormbringer'), Js('Stormcaller'), Js('Sunward'), Js('Supernova'), Js('Supremacy'), Js('Suspension'), Js('Swan Song'), Js('The Abyss'), Js('The Ambassador'), Js('The Barricade'), Js('The Beast'), Js('The Black Hole'), Js('The Blockade'), Js('The Boon'), Js('The Brute'), Js('The Curator'), Js('The End'), Js('The Grand Slam'), Js('The Iron Maid'), Js('The Iron Maiden'), Js('The Keeper'), Js('The Light'), Js('The Mirror'), Js('The Mountain'), Js('The Observer'), Js('The Oculus'), Js('The Righteous'), Js('The Sentinel'), Js('The Sentry'), Js('The Shadow'), Js('The Titan'), Js('The Voice'), Js('The Void'), Js('Thunder'), Js('Thundercloud'), Js('Torrent'), Js('Tranquility'), Js('Treachery'), Js('Trinity'), Js('Triumph'), Js('Truthbreaker'), Js('Typhoon'), Js('Tyranny'), Js('Vacancy'), Js('Vacuum'), Js('Valkyrie'), Js('Vanquisher'), Js('Vengeance'), Js('Vigilant'), Js('Vigilante'), Js('Voice of Honor'), Js('Voice of Insanity'), Js('Voice of Madness'), Js('Voice of Pride'), Js('Voice of Reason'), Js('Volcano'), Js('Vortex'), Js('Warcry'), Js('Warmonger'), Js('Warsong'), Js('Willbreaker'), Js("Wisdom's Grasp"), Js("Wisdom's Hold"), Js("Wit's End"), Js('Witherbrand')]))
pass
pass


# Add lib to the module scope
shieldNames = var.to_python()
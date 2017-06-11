__all__ = ['whipNames']

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
var.put('nm1', Js([Js('Blackjack'), Js('Headache'), Js('Migraine'), Js('Grimace'), Js('Abomination'), Js('Agatha'), Js('Agony'), Js('Allegiance'), Js('Alpha'), Js('Amnesia'), Js('Anduril'), Js('Apocalypse'), Js('Armageddon'), Js('Arondite'), Js('Ash'), Js('Ashes'), Js('Ashrune'), Js('Back Breaker'), Js('Battlestar'), Js('Betrayal'), Js('Betrayer'), Js('Blackout'), Js('Blazeguard'), Js('Blessing'), Js('Blind Justice'), Js('Bloodfury'), Js('Bloodmoon'), Js('Bloodquench'), Js('Bloodrage'), Js('Bloodspiller'), Js('Bloodweep'), Js('Bone Warden'), Js('Bonesnapper'), Js('Braindead'), Js('Broken Promise'), Js('Brutality'), Js('Brutalizer'), Js('Cataclysm'), Js('Catastrophe'), Js('Celeste'), Js('Chance'), Js('Chaos'), Js('Chasm'), Js('Chieftain'), Js('Comet'), Js('Cometfall'), Js('Concussion'), Js('Convergence'), Js('Corpsemaker'), Js('Corruption'), Js('Cosmos'), Js('Crash'), Js('Crimson'), Js('Crush'), Js('Cryptmaker'), Js('Cyclone'), Js('Darkness'), Js('Dawn'), Js('Dawnbreaker'), Js('Daytime'), Js('Deathbringer'), Js('Deathraze'), Js('Decimation'), Js('Demise'), Js('Desolation'), Js('Despair'), Js('Destiny'), Js('Destruction'), Js('Devastation'), Js('Devine'), Js('Devotion'), Js('Devourer'), Js('Disturbance'), Js('Divine Light'), Js('Dominance'), Js('Dominion'), Js('Doom'), Js('Doombringer'), Js('Dragonfist'), Js('Dragonmaw'), Js('Dragonstrike'), Js('Due Diligence'), Js('Early Retirement'), Js('Earthquake'), Js('Earthshaker'), Js('Earthshaper'), Js('Earthwarden'), Js('Echo'), Js('Eclipse'), Js('Emergency'), Js('End of Dreams'), Js('Endbringer'), Js('Enigma'), Js('Epilogue'), Js('Eternal Rest'), Js('Eternity'), Js('Eveningstar'), Js('Extermination'), Js('Extinction'), Js('Faithkeeper'), Js('Falcon'), Js('Falling Star'), Js('Fate'), Js('Finality'), Js('Frenzy'), Js('Frostwind'), Js('Fury'), Js("Fury's Gaze"), Js('Galaxy'), Js('Gatecrasher'), Js('Ghost Reaver'), Js('Ghostwalker'), Js('Glimmer'), Js('Godslayer'), Js('Grace'), Js('Guiding Star'), Js('Harbinger'), Js('Harmony'), Js('Harvester'), Js('Hatred'), Js('Heartcrusher'), Js("Hell's Scream"), Js('Hellfire'), Js('Homage'), Js("Honor's Call"), Js("Hope's End"), Js('Humongous'), Js('Hurricane'), Js('Icebreaker'), Js('Infamy'), Js('Infinity'), Js('Interrogator'), Js('Jackhammer'), Js('Jawbone'), Js('Justice'), Js('Justifier'), Js("King's Defender"), Js("King's Legacy"), Js('Kinslayer'), Js("Knight's Fall"), Js("Knight's Honor"), Js('Knightfall'), Js('Lament'), Js('Last Chance'), Js('Last Laugh'), Js('Last Rites'), Js('Last Word'), Js('Last Words'), Js('Lazarus'), Js('Legacy'), Js('Legionaire'), Js("Life's Limit"), Js("Light's Bane"), Js('Lightbane'), Js('Lightbringer'), Js('Lightning'), Js('Limbo'), Js('Lockjaw'), Js('Magma'), Js('Malice'), Js('Maneater'), Js('Massacre'), Js('Mercy'), Js('Midnight'), Js("Misery's End"), Js('Monsoon'), Js('Morningstar'), Js('Narcoleptic'), Js('Nethersbane'), Js("Night's Fall"), Js('Nightbane'), Js('Nightfall'), Js('Nightglow'), Js('Nightmare'), Js('Nighttime'), Js('Nirvana'), Js('Oathbreaker'), Js('Oathkeeper'), Js('Oblivion'), Js('Old Age'), Js('Omega'), Js('Orbit'), Js('Orenmir'), Js('Oxheart'), Js('Party Pooper'), Js('Patience'), Js('Peacekeeper'), Js('Peacemaker'), Js('Pendulum'), Js('Perfect Storm'), Js('Persuasion'), Js('Piece Maker'), Js('Piety'), Js('Pride'), Js('Prophecy'), Js('Punisher'), Js('Purifier'), Js('Rage'), Js('Ragnarok'), Js('Rapture'), Js("Reaper's Toll"), Js('Reckoning'), Js('Red Dwarf'), Js('Reign'), Js('Remorse'), Js('Requiem'), Js('Retirement'), Js('Righteous Might'), Js('Rigormortis'), Js('Rising Tide'), Js('Savagery'), Js('Scar'), Js('Scourgeborne'), Js('Second Chance'), Js('Seism'), Js('Seismic'), Js('Serenity'), Js('Severance'), Js('Shadowfury'), Js('Shadowmoon'), Js('Shatterskull'), Js('Shooting Star'), Js('Silence'), Js('Skullcrusher'), Js('Soul Breaker'), Js('Spinefall'), Js('Stalker'), Js('Stonefist'), Js('Storm'), Js('Storm Breaker'), Js('Storm-Weaver'), Js('Stormbringer'), Js('Stormcaller'), Js('Stormedge'), Js('Stormherald'), Js('Stormrider'), Js('Sucker Punch'), Js('Sundown'), Js('Supernova'), Js('Supremacy'), Js('Suspension'), Js('Swan Song'), Js('Tank'), Js('Tenderiser'), Js('Termination'), Js('The Ambassador'), Js('The Chancellor'), Js('The Chief'), Js('The End'), Js('The Light'), Js('The Minotaur'), Js('The Oculus'), Js('The Oracle'), Js('The Sundering'), Js('The Void'), Js('The Warden'), Js('Thunder'), Js('Trauma'), Js('Treachery'), Js('Tremor'), Js('Trinity'), Js('Twilight'), Js('Typhoon'), Js('Ubiquity'), Js('Undoing'), Js('Vacancy'), Js('Valkyrie'), Js('Vanquisher'), Js('Vengeance'), Js('Warbringer'), Js('Warmonger'), Js('Whirlwind'), Js('Wicked'), Js('Widow Maker'), Js('Willbreaker'), Js("Winter's Bite"), Js("Wit's End"), Js('Witherbrand'), Js('Wolf'), Js('Worldbreaker'), Js('Worldcarver'), Js('Worldslayer')]))
var.put('nm2', Js([Js('Ancient'), Js('Antique'), Js('Apocalypse'), Js('Apocalyptic'), Js('Arcane'), Js('Arched'), Js('Atuned'), Js("Bandit's"), Js('Baneful'), Js('Banished'), Js('Barbarian'), Js('Barbaric'), Js('Battleworn'), Js('Blazefury'), Js('Blood Infused'), Js('Blood-Forged'), Js('Bloodcursed'), Js('Bloodied'), Js("Bloodlord's"), Js('Bloodsurge'), Js('Bloodvenom'), Js('Bonecarvin'), Js('Brutal'), Js('Brutality'), Js('Burnished'), Js('Cataclysm'), Js('Cataclysmic'), Js('Challenger'), Js("Challenger's"), Js('Champion'), Js("Champion's"), Js('Cold-Forged'), Js('Conqueror'), Js("Conqueror's"), Js('Corroded'), Js('Corrupted'), Js('Crazed'), Js('Crying'), Js('Cursed'), Js('Curved'), Js('Dancing'), Js('Dark'), Js('Darkness'), Js('Defender'), Js("Defender's"), Js('Defiled'), Js('Defiling'), Js('Deluded'), Js('Demonic'), Js('Deserted'), Js("Desire's"), Js('Desolation'), Js("Destiny's"), Js('Diabolical'), Js('Dire'), Js('Doom'), Js("Doom's"), Js("Dragon's"), Js('Dragonbreath'), Js('Eerie'), Js('Enchanted'), Js('Engraved'), Js('Enlightened'), Js('Eternal'), Js('Exiled'), Js('Extinction'), Js("Faith's"), Js('Faithful'), Js('Fancy'), Js('Fearful'), Js('Feral'), Js('Ferocious'), Js('Fierce'), Js('Fiery'), Js('Fire Infused'), Js('Fireguard'), Js('Firesoul'), Js('Firestorm'), Js('Flaming'), Js('Flimsy'), Js('Forsaken'), Js("Fortune's"), Js('Foul'), Js('Fragile'), Js('Frail'), Js('Frenzied'), Js('Frost'), Js('Frozen'), Js('Furious'), Js('Fusion'), Js('Ghastly'), Js('Ghost'), Js('Ghost-Forged'), Js('Ghostly'), Js('Gladiator'), Js("Gladiator's"), Js('Gleaming'), Js('Glinting'), Js('Greedy'), Js('Grieving'), Js('Grim'), Js("Guard's"), Js("Guardian's"), Js('Hailstorm'), Js('Harmonized'), Js('Hateful'), Js('Haunted'), Js('Heartless'), Js('Heinous'), Js('Hero'), Js("Hero's"), Js('Hollow'), Js('Holy'), Js('Honed'), Js("Honor's"), Js("Hope's"), Js('Hopeless'), Js('Howling'), Js('Hungering'), Js('Improved'), Js('Impure'), Js('Incarnated'), Js('Infused'), Js('Inherited'), Js('Isolated'), Js('Jade Infused'), Js('Judgement'), Js("Keeper's"), Js('Knightly'), Js("Knight's"), Js("Legionnaire's"), Js("Liar's"), Js('Lich'), Js('Lightning'), Js('Lonely'), Js('Loyal'), Js('Lustful'), Js('Lusting'), Js('Malevolent'), Js('Malicious'), Js('Malificent'), Js('Malignant'), Js('Massive'), Js('Mended'), Js('Mercenary'), Js('Military'), Js("Misfortune's"), Js('Misty'), Js('Moonlit'), Js('Mourning'), Js('Nightmare'), Js("Oathkeeper's"), Js('Ominous'), Js('Peacekeeper'), Js("Peacekeeper's"), Js('Phantom'), Js('Polished'), Js('Possessed'), Js("Pride's"), Js('Prideful'), Js('Primal'), Js('Prime'), Js('Primitive'), Js('Promised'), Js("Protector's"), Js('Proud'), Js('Pure'), Js('Putrid'), Js('Raging'), Js("Recruit's"), Js('Refined'), Js('Reforged'), Js('Reincarnated'), Js('Relentless'), Js('Remorseful'), Js('Renewed'), Js('Renovated'), Js('Replica'), Js('Restored'), Js('Retribution'), Js('Ritual'), Js('Roaring'), Js('Ruby Infused'), Js('Rune-Forged'), Js('Runed'), Js('Rusty'), Js('Savage'), Js('Sentinel'), Js('Shadow'), Js('Shamanic'), Js('Sharpened'), Js('Silent'), Js('Singed'), Js('Singing'), Js('Sinister'), Js('Skyfall'), Js('Smooth'), Js("Soldier's"), Js("Solitude's"), Js("Sorcerer's"), Js("Sorrow's"), Js('Soul'), Js('Soul Infused'), Js('Soul-Forged'), Js('Soulcursed'), Js('Soulless'), Js('Spectral'), Js('Spectral-Forged'), Js('Spiteful'), Js('Storm'), Js('Storm-Forged'), Js('Stormfury'), Js('Stormguard'), Js('Terror'), Js('Thirsting'), Js('Thirsty'), Js('Thunder'), Js('Thunder-Forged'), Js('Thunderfury'), Js('Thunderguard'), Js('Thundersoul'), Js('Thunderstorm'), Js('Timeworn'), Js('Tormented'), Js("Trainee's"), Js("Treachery's"), Js('Twilight'), Js("Twilight's"), Js('Twisted'), Js('Tyrannical'), Js('Undead'), Js('Unholy'), Js('Vanquisher'), Js('Vengeance'), Js('Vengeful'), Js('Venom'), Js('Vicious'), Js('Victor'), Js('Vile'), Js('Vindication'), Js('Vindicator'), Js('Vindictive'), Js('Void'), Js('Volcanic'), Js('Vowed'), Js('War'), Js('War-Forged'), Js("Warden's"), Js("Warlord's"), Js('Warp'), Js('Warped'), Js('Warrior'), Js("Warrior's"), Js('Whistling'), Js('Wicked'), Js("Wind's"), Js('Wind-Forged'), Js('Windsong'), Js('Woeful'), Js('Wrathful'), Js('Wretched'), Js('Yearning'), Js('Zealous')]))
var.put('nm3', Js([Js('Adamantite'), Js('Bone'), Js('Bronze'), Js('Bronzed'), Js('Ivory'), Js('Ebon'), Js('Glass'), Js('Golden'), Js('Gilded'), Js('Iron'), Js('Ironbark'), Js('Mithril'), Js('Obsidian'), Js('Silver'), Js('Skeletal'), Js('Steel'), Js('Titanium')]))
var.put('nm4', Js([Js('Whip'), Js('Crop'), Js('Belt'), Js('Lash'), Js('Wire'), Js('Snare'), Js('Lasso'), Js('Lariat'), Js('Riata')]))
var.put('nm5', Js([Js('Allegiance'), Js('Annihilation'), Js('Belt'), Js('Snare'), Js('Lasso'), Js('Lariat'), Js('Riata'), Js('Betrayer'), Js('Bond'), Js('Boon'), Js('Breaker'), Js('Bringer'), Js('Butcher'), Js('Call'), Js('Champion'), Js('Conqueror'), Js('Crop'), Js('Crusader'), Js('Cry'), Js('Cunning'), Js('Dawn'), Js('Defender'), Js('Defiler'), Js('Destroyer'), Js('Ender'), Js('Etcher'), Js('Executioner'), Js('Favor'), Js('Ferocity'), Js('Foe'), Js('Gift'), Js('Glory'), Js('Guardian'), Js('Heirloom'), Js('Hope'), Js('Incarnation'), Js('Lash'), Js('Last Hope'), Js('Last Stand'), Js('Legacy'), Js('Memory'), Js('Might'), Js('Oath'), Js('Pact'), Js('Piercer'), Js('Pledge'), Js('Promise'), Js('Prophecy'), Js('Protector'), Js('Ravager'), Js('Reach'), Js('Reaper'), Js('Reaver'), Js('Sculptor'), Js('Secret'), Js('Slayer'), Js('Soul'), Js('Terror'), Js('Token'), Js('Tribute'), Js('Vengeance'), Js('Voice'), Js('Wacker'), Js('Whip'), Js('Whisper'), Js('Wire'), Js('Wit')]))
var.put('nm6', Js([Js('of Agony'), Js('of Ancient Power'), Js('of Anguish'), Js('of Ashes'), Js('of Assassins'), Js('of Black Magic'), Js('of Blessed Fortune'), Js('of Blessings'), Js('of Blight'), Js('of Blood'), Js('of Bloodlust'), Js('of Broken Bones'), Js('of Broken Dreams'), Js('of Broken Families'), Js('of Burdens'), Js('of Chaos'), Js('of Closing Eyes'), Js('of Conquered Worlds'), Js('of Corruption'), Js('of Cruelty'), Js('of Cunning'), Js('of Dark Magic'), Js('of Dark Souls'), Js('of Darkness'), Js('of Decay'), Js('of Deception'), Js('of Degradation'), Js('of Delusions'), Js('of Denial'), Js('of Desecration'), Js('of Diligence'), Js('of Dismay'), Js('of Dragonsouls'), Js('of Due Diligence'), Js('of Echoes'), Js('of Ended Dreams'), Js('of Ending Hope'), Js('of Ending Misery'), Js('of Eternal Bloodlust'), Js('of Eternal Damnation'), Js('of Eternal Glory'), Js('of Eternal Justice'), Js('of Eternal Rest'), Js('of Eternal Sorrow'), Js('of Eternal Struggles'), Js('of Eternity'), Js('of Executions'), Js('of Faded Memories'), Js('of Fallen Souls'), Js('of Fools'), Js('of Frost'), Js('of Frozen Hells'), Js('of Fury'), Js('of Giants'), Js('of Giantslaying'), Js('of Grace'), Js('of Grieving Widows'), Js('of Hate'), Js('of Hatred'), Js("of Hell's Games"), Js('of Hellish Torment'), Js('of Heroes'), Js('of Holy Might'), Js('of Honor'), Js('of Hope'), Js('of Horrid Dreams'), Js('of Horrors'), Js('of Illuminated Dreams'), Js('of Illumination'), Js('of Immortality'), Js('of Inception'), Js('of Infinite Trials'), Js('of Insanity'), Js('of Invocation'), Js('of Justice'), Js("of Light's Hope"), Js('of Lost Comrades'), Js('of Lost Hope'), Js('of Lost Voices'), Js('of Lost Worlds'), Js('of Magic'), Js('of Mercy'), Js('of Misery'), Js('of Mountains'), Js('of Mourning'), Js('of Mystery'), Js('of Necromancy'), Js('of Nightmares'), Js('of Oblivion'), Js('of Perdition'), Js('of Phantoms'), Js('of Power'), Js('of Pride'), Js("of Pride's Fall"), Js('of Putrefaction'), Js('of Reckoning'), Js('of Redemption'), Js('of Regret'), Js('of Riddles'), Js('of Secrecy'), Js('of Secrets'), Js('of Shadow Strikes'), Js('of Shadows'), Js('of Shifting Sands'), Js('of Shifting Worlds'), Js('of Silence'), Js('of Slaughter'), Js('of Souls'), Js('of Stealth'), Js('of Storms'), Js('of Subtlety'), Js('of Suffering'), Js("of Suffering's End"), Js('of Summoning'), Js('of Terror'), Js('of Thunder'), Js('of Time-Lost Memories'), Js('of Timeless Battles'), Js('of Titans'), Js('of Torment'), Js('of Traitors'), Js('of Trembling Hands'), Js('of Trials'), Js('of Truth'), Js("of Twilight's End"), Js('of Twisted Visions'), Js('of Unholy Blight'), Js('of Unholy Might'), Js('of Vengeance'), Js('of Visions'), Js('of Wasted Time'), Js('of Widows'), Js('of Wizardry'), Js('of Woe'), Js('of Wraiths'), Js('of Zeal'), Js('of the Ancients'), Js('of the Banished'), Js('of the Basilisk'), Js('of the Beast'), Js('of the Blessed'), Js('of the Breaking Storm'), Js('of the Brotherhood'), Js('of the Burning Sun'), Js('of the Caged Mind'), Js('of the Cataclysm'), Js('of the Champion'), Js('of the Claw'), Js('of the Corrupted'), Js('of the Covenant'), Js('of the Crown'), Js('of the Damned'), Js('of the Daywalker'), Js('of the Dead'), Js('of the Depth'), Js('of the Dreadlord'), Js('of the Earth'), Js('of the East'), Js('of the Emperor'), Js('of the Empty Void'), Js('of the End'), Js('of the Enigma'), Js('of the Fallen'), Js('of the Falling Sky'), Js('of the Flame'), Js('of the Forest'), Js('of the Forgotten'), Js('of the Forsaken'), Js('of the Gladiator'), Js('of the Harvest'), Js('of the Immortal'), Js('of the Incoming Storm'), Js('of the Insane'), Js('of the King'), Js('of the Lasting Night'), Js('of the Leviathan'), Js('of the Light'), Js('of the Lion'), Js('of the Lionheart'), Js('of the Lone Victor'), Js('of the Lone Wolf'), Js('of the Lost'), Js('of the Moon'), Js('of the Moonwalker'), Js('of the Night Sky'), Js('of the Night'), Js('of the Nightstalker'), Js('of the North'), Js('of the Occult'), Js('of the Oracle'), Js('of the Phoenix'), Js('of the Plague'), Js('of the Prince'), Js('of the Protector'), Js('of the Queen'), Js('of the Serpent'), Js('of the Setting Sun'), Js('of the Shadows'), Js('of the Sky'), Js('of the South'), Js('of the Stars'), Js('of the Storm'), Js('of the Summoner'), Js('of the Sun'), Js('of the Sunwalker'), Js('of the Talon'), Js('of the Undying'), Js('of the Victor'), Js('of the Void'), Js('of the West'), Js('of the Whispers'), Js('of the Wicked'), Js('of the Wind'), Js('of the Wolf'), Js('of the World'), Js('of the Wretched')]))
var.put('nm7', Js([Js('Morning Glory'), Js('Morning Star'), Js('Mourning Star'), Js('Blackjack'), Js('Tresher'), Js('Good Morning'), Js('Headache'), Js('Migraine'), Js('Grimace'), Js('Macerator'), Js('Abomination'), Js('Agatha'), Js('Agony'), Js('Allegiance'), Js('Alpha'), Js('Amnesia'), Js('Anduril'), Js('Apocalypse'), Js('Armageddon'), Js('Arondite'), Js('Ash'), Js('Ashes'), Js('Ashrune'), Js('Back Breaker'), Js('Battlestar'), Js('Betrayal'), Js('Betrayer'), Js('Blackout'), Js('Blazeguard'), Js('Blessing'), Js('Blind Justice'), Js('Bloodfury'), Js('Bloodmoon'), Js('Bloodquench'), Js('Bloodrage'), Js('Bloodspiller'), Js('Bloodweep'), Js('Bone Warden'), Js('Bonesnapper'), Js('Braindead'), Js('Broken Promise'), Js('Brutality'), Js('Brutalizer'), Js('Cataclysm'), Js('Catastrophe'), Js('Celeste'), Js('Chance'), Js('Chaos'), Js('Chasm'), Js('Chieftain'), Js('Comet'), Js('Cometfall'), Js('Concussion'), Js('Convergence'), Js('Corpsemaker'), Js('Corruption'), Js('Cosmos'), Js('Crash'), Js('Crimson'), Js('Crush'), Js('Cryptmaker'), Js('Cyclone'), Js('Darkness'), Js('Dawn'), Js('Dawnbreaker'), Js('Daytime'), Js('Deathbringer'), Js('Deathraze'), Js('Decimation'), Js('Demise'), Js('Desolation'), Js('Despair'), Js('Destiny'), Js('Destruction'), Js('Devastation'), Js('Devine'), Js('Devotion'), Js('Devourer'), Js('Disturbance'), Js('Divine Light'), Js('Dominance'), Js('Dominion'), Js('Doom'), Js('Doombringer'), Js('Dragonfist'), Js('Dragonmaw'), Js('Dragonstrike'), Js('Due Diligence'), Js('Earthquake'), Js('Earthshaker'), Js('Earthshaper'), Js('Earthwarden'), Js('Echo'), Js('Eclipse'), Js('Emergency'), Js('End of Dreams'), Js('Endbringer'), Js('Enigma'), Js('Epilogue'), Js('Eternal Rest'), Js('Eternity'), Js('Eveningstar'), Js('Extermination'), Js('Extinction'), Js('Faithkeeper'), Js('Falcon'), Js('Falling Star'), Js('Fate'), Js('Finality'), Js('Frenzy'), Js('Frostwind'), Js('Fury'), Js("Fury's Gaze"), Js('Galaxy'), Js('Gatecrasher'), Js('Ghost Reaver'), Js('Ghostwalker'), Js('Glimmer'), Js('Godslayer'), Js('Grace'), Js('Guiding Star'), Js('Harbinger'), Js('Harmony'), Js('Harvester'), Js('Hatred'), Js('Heartcrusher'), Js("Hell's Scream"), Js('Hellfire'), Js('Homage'), Js("Honor's Call"), Js("Hope's End"), Js('Humongous'), Js('Hurricane'), Js('Icebreaker'), Js('Infamy'), Js('Infinity'), Js('Interrogator'), Js('Jackhammer'), Js('Jawbone'), Js('Justice'), Js('Justifier'), Js("King's Defender"), Js("King's Legacy"), Js('Kinslayer'), Js("Knight's Fall"), Js("Knight's Honor"), Js('Knightfall'), Js('Lament'), Js('Last Chance'), Js('Last Laugh'), Js('Last Rites'), Js('Last Word'), Js('Last Words'), Js('Lazarus'), Js('Legacy'), Js('Legionaire'), Js("Life's Limit"), Js("Light's Bane"), Js('Lightbane'), Js('Lightbringer'), Js('Lightning'), Js('Limbo'), Js('Lockjaw'), Js('Magma'), Js('Malice'), Js('Maneater'), Js('Massacre'), Js('Mercy'), Js('Midnight'), Js("Misery's End"), Js('Monsoon'), Js('Morningstar'), Js('Narcoleptic'), Js('Nethersbane'), Js("Night's Fall"), Js('Nightbane'), Js('Nightfall'), Js('Nightglow'), Js('Nightmare'), Js('Nighttime'), Js('Nirvana'), Js('Oathbreaker'), Js('Oathkeeper'), Js('Oblivion'), Js('Old Age'), Js('Omega'), Js('Orbit'), Js('Orenmir'), Js('Oxheart'), Js('Party Pooper'), Js('Patience'), Js('Peacekeeper'), Js('Peacemaker'), Js('Pendulum'), Js('Perfect Storm'), Js('Persuasion'), Js('Piety'), Js('Pride'), Js('Prophecy'), Js('Punisher'), Js('Purifier'), Js('Rage'), Js('Ragnarok'), Js('Rapture'), Js('Reckoning'), Js('Red Dwarf'), Js('Reign'), Js('Remorse'), Js('Requiem'), Js('Retirement'), Js('Rigormortis'), Js('Rising Tide'), Js('Savagery'), Js('Seism'), Js('Seismic'), Js('Serenity'), Js('Severance'), Js('Shadowfury'), Js('Shatterskull'), Js('Shooting Star'), Js('Silence'), Js('Skullcrusher'), Js('Soul Breaker'), Js('Spinefall'), Js('Stalker'), Js('Stonefist'), Js('Storm'), Js('Storm Breaker'), Js('Storm-Weaver'), Js('Stormbringer'), Js('Stormcaller'), Js('Stormedge'), Js('Stormherald'), Js('Stormrider'), Js('Sucker Punch'), Js('Sundown'), Js('Supernova'), Js('Supremacy'), Js('Suspension'), Js('Swan Song'), Js('Tank'), Js('Tenderiser'), Js('Termination'), Js('The Ambassador'), Js('The Chancellor'), Js('The Chief'), Js('The End'), Js('The Light'), Js('The Minotaur'), Js('The Oculus'), Js('The Oracle'), Js('The Sundering'), Js('The Void'), Js('The Warden'), Js('Thunder'), Js('Trauma'), Js('Treachery'), Js('Tremor'), Js('Trinity'), Js('Twilight'), Js('Typhoon'), Js('Ubiquity'), Js('Undoing'), Js('Vacancy'), Js('Valkyrie'), Js('Vanquisher'), Js('Vengeance'), Js('Warbringer'), Js('Warmonger'), Js('Whirlwind'), Js('Wicked'), Js('Widow Maker'), Js('Willbreaker'), Js("Winter's Bite"), Js("Wit's End"), Js('Witherbrand'), Js('Wolf'), Js('Worldbreaker'), Js('Worldcarver'), Js('Worldslayer'), Js("Von Karma's Whip")]))
pass
pass


# Add lib to the module scope
whipNames = var.to_python()
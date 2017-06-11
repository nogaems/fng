__all__ = ['clawNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js(', '))+var.get('nm5').get(var.get('rnd2')))+Js(' '))+var.get('nm6').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abomination'), Js('Advisary'), Js('Allowance'), Js('Alpha'), Js('Amnesia'), Js('Angerfist'), Js('Anguish'), Js('Appointment'), Js('Armageddon'), Js('Blackeye'), Js('Blacktalon'), Js('Blade Dance'), Js('Blinder'), Js('Blindstrike'), Js('Blinkstrike'), Js('Bloodfist'), Js('Bloodfury'), Js('Bloodrage'), Js('Bloodspiller'), Js('Brawler'), Js('Bruiser'), Js('Brutality'), Js('Brutalizer'), Js('Brute'), Js('Brutus'), Js('Bully'), Js('Can Opener'), Js('Carnage'), Js('Carver'), Js('Cat'), Js('Chaos'), Js('Checkpoint'), Js('Chillspike'), Js('Creature'), Js('Creep'), Js('Critter'), Js('Dawnbreaker'), Js("Death's Touch"), Js('Deathraze'), Js('Deception'), Js('Decimation'), Js('Delirium'), Js('Devourer'), Js('Dissector'), Js('Doom'), Js("Doom's Fist"), Js("Doom's Punch"), Js('Doombringer'), Js('Drillbit'), Js('Echo'), Js('Eclipse'), Js('Enigma'), Js('Epilogue'), Js('Etcher'), Js('Facebreaker'), Js('Facepalm'), Js('Faceplant'), Js('Faceslicer'), Js('Fistbumper'), Js('Frenzy'), Js('Fury'), Js('Gargoyle'), Js('Gash'), Js('Gladiator'), Js('Glutton'), Js('Greed'), Js('Grieve'), Js('Gripe'), Js('Grizzly'), Js('Gutpuncher'), Js('Hacker'), Js('Heartseeker'), Js("Hell's Fist"), Js("Hell's Fury"), Js('Hole In One'), Js('Homage'), Js("Honor's Hand"), Js('Hurricane'), Js('Infamy'), Js('Infinity'), Js('Insanity'), Js('Itch'), Js('Jaeger'), Js('Jawbreaker'), Js('Lacerator'), Js('Lament'), Js('Lance'), Js('Lazarus'), Js('Limbo'), Js('Lobster'), Js('Malevolence'), Js('Malice'), Js('Marrowstrike'), Js('Massacre'), Js('Masticator'), Js('Mitigator'), Js('Narcoleptic'), Js('Needle'), Js('Needles'), Js('Nibble'), Js('Nibbler'), Js("Night's Reach"), Js('Nightbane'), Js('Nightfall'), Js('Oathbinder'), Js('Oathbreaker'), Js('Oathkeeper'), Js('Oblivion'), Js('Omega'), Js('Paws'), Js('Perforator'), Js('Permeater'), Js('Phoenix'), Js('Pierce'), Js('Piercer'), Js('Piety'), Js('Pincer'), Js('Pincey'), Js('Pique'), Js('Predator'), Js('Prick'), Js('Prickler'), Js('Pride'), Js('Puncturer'), Js('Quota'), Js('Rage'), Js('Raptor'), Js('Rapture'), Js('Reflex'), Js('Reign'), Js('Requiem'), Js('Rodent'), Js('Ruthless'), Js('Savage'), Js('Savagery'), Js('Scar'), Js('Scratches'), Js('Scratchy'), Js('Scyther'), Js('Seism'), Js('Severance'), Js('Shadowfury'), Js('Shadowstrike'), Js('Shards'), Js('Shredder'), Js('Silence'), Js('Skinner'), Js('Skirmisher'), Js('Slice of Life'), Js('Snip'), Js('Spike'), Js('Spikey'), Js('Spite'), Js('Splinter'), Js('Stalker'), Js('Sting'), Js('Storm'), Js('Striker'), Js('Stripper'), Js('Sunder'), Js('Tenderizer'), Js('Terror'), Js('Thunder'), Js('Thunderstrike'), Js('Tickles'), Js('Tingle'), Js('Torment'), Js('Trickster'), Js('Trinity'), Js('Twister'), Js('Vacancy'), Js('Valkyrie'), Js('Vermin'), Js('Vice'), Js('Vile'), Js('Whirlwind'), Js('Wicked'), Js('Widow Maker'), Js('Willbreaker')]))
var.put('nm2', Js([Js('Ancient'), Js('Antique'), Js('Apocalypse'), Js('Apocalyptic'), Js('Arcane'), Js('Arched'), Js('Atuned'), Js("Bandit's"), Js('Baneful'), Js('Banished'), Js('Barbarian'), Js('Barbaric'), Js('Battleworn'), Js('Blazefury'), Js('Blood Infused'), Js('Blood-Forged'), Js('Bloodcursed'), Js('Bloodied'), Js("Bloodlord's"), Js('Bloodsurge'), Js('Bloodvenom'), Js('Bonecarvin'), Js('Brutal'), Js('Brutality'), Js('Burnished'), Js('Cataclysm'), Js('Cataclysmic'), Js('Challenger'), Js("Challenger's"), Js('Champion'), Js("Champion's"), Js('Cold-Forged'), Js('Conqueror'), Js("Conqueror's"), Js('Corroded'), Js('Corrupted'), Js('Crazed'), Js('Crying'), Js('Cursed'), Js('Curved'), Js('Dancing'), Js('Dark'), Js('Darkness'), Js('Defender'), Js("Defender's"), Js('Defiled'), Js('Defiling'), Js('Deluded'), Js('Demonic'), Js('Deserted'), Js("Desire's"), Js('Desolation'), Js("Destiny's"), Js('Diabolical'), Js('Dire'), Js('Doom'), Js("Doom's"), Js("Dragon's"), Js('Dragonbreath'), Js('Eerie'), Js('Enchanted'), Js('Engraved'), Js('Enlightened'), Js('Eternal'), Js('Exiled'), Js('Extinction'), Js("Faith's"), Js('Faithful'), Js('Fancy'), Js('Fearful'), Js('Feral'), Js('Ferocious'), Js('Fierce'), Js('Fiery'), Js('Fire Infused'), Js('Fireguard'), Js('Firesoul'), Js('Firestorm'), Js('Flaming'), Js('Flimsy'), Js('Forsaken'), Js("Fortune's"), Js('Foul'), Js('Fragile'), Js('Frail'), Js('Frenzied'), Js('Frost'), Js('Frozen'), Js('Furious'), Js('Fusion'), Js('Ghastly'), Js('Ghost'), Js('Ghost-Forged'), Js('Ghostly'), Js('Gladiator'), Js("Gladiator's"), Js('Gleaming'), Js('Glinting'), Js('Greedy'), Js('Grieving'), Js('Grim'), Js("Guard's"), Js("Guardian's"), Js('Hailstorm'), Js('Harmonized'), Js('Hateful'), Js('Haunted'), Js('Heartless'), Js('Heinous'), Js('Hero'), Js("Hero's"), Js('Hollow'), Js('Holy'), Js('Honed'), Js("Honor's"), Js("Hope's"), Js('Hopeless'), Js('Howling'), Js('Hungering'), Js('Improved'), Js('Impure'), Js('Incarnated'), Js('Infused'), Js('Inherited'), Js('Isolated'), Js('Jade Infused'), Js('Judgement'), Js("Keeper's"), Js('Knightly'), Js("Knight's"), Js("Legionnaire's"), Js("Liar's"), Js('Lich'), Js('Lightning'), Js('Lonely'), Js('Loyal'), Js('Lustful'), Js('Lusting'), Js('Malevolent'), Js('Malicious'), Js('Malificent'), Js('Malignant'), Js('Massive'), Js('Mended'), Js('Mercenary'), Js('Military'), Js("Misfortune's"), Js('Misty'), Js('Moonlit'), Js('Mourning'), Js('Nightmare'), Js("Oathkeeper's"), Js('Ominous'), Js('Peacekeeper'), Js("Peacekeeper's"), Js('Phantom'), Js('Polished'), Js('Possessed'), Js("Pride's"), Js('Prideful'), Js('Primal'), Js('Prime'), Js('Primitive'), Js('Promised'), Js("Protector's"), Js('Proud'), Js('Pure'), Js('Putrid'), Js('Raging'), Js("Recruit's"), Js('Refined'), Js('Reforged'), Js('Reincarnated'), Js('Relentless'), Js('Remorseful'), Js('Renewed'), Js('Renovated'), Js('Replica'), Js('Restored'), Js('Retribution'), Js('Ritual'), Js('Roaring'), Js('Ruby Infused'), Js('Rune-Forged'), Js('Runed'), Js('Rusty'), Js('Savage'), Js('Sentinel'), Js('Shadow'), Js('Shamanic'), Js('Sharpened'), Js('Silent'), Js('Singed'), Js('Singing'), Js('Sinister'), Js('Skyfall'), Js('Smooth'), Js("Soldier's"), Js("Solitude's"), Js("Sorcerer's"), Js("Sorrow's"), Js('Soul'), Js('Soul Infused'), Js('Soul-Forged'), Js('Soulcursed'), Js('Soulless'), Js('Spectral'), Js('Spectral-Forged'), Js('Spiteful'), Js('Storm'), Js('Storm-Forged'), Js('Stormfury'), Js('Stormguard'), Js('Terror'), Js('Thirsting'), Js('Thirsty'), Js('Thunder'), Js('Thunder-Forged'), Js('Thunderfury'), Js('Thunderguard'), Js('Thundersoul'), Js('Thunderstorm'), Js('Timeworn'), Js('Tormented'), Js("Trainee's"), Js("Treachery's"), Js('Twilight'), Js("Twilight's"), Js('Twisted'), Js('Tyrannical'), Js('Undead'), Js('Unholy'), Js('Vanquisher'), Js('Vengeance'), Js('Vengeful'), Js('Venom'), Js('Vicious'), Js('Victor'), Js('Vile'), Js('Vindication'), Js('Vindicator'), Js('Vindictive'), Js('Void'), Js('Volcanic'), Js('Vowed'), Js('War'), Js('War-Forged'), Js("Warden's"), Js("Warlord's"), Js('Warp'), Js('Warped'), Js('Warrior'), Js("Warrior's"), Js('Whistling'), Js('Wicked'), Js("Wind's"), Js('Wind-Forged'), Js('Windsong'), Js('Woeful'), Js('Wrathful'), Js('Wretched'), Js('Yearning'), Js('Zealous')]))
var.put('nm3', Js([Js('Adamantite'), Js('Mithril'), Js('Obsidian'), Js('Silver'), Js('Skeletal'), Js('Steel'), Js('Ebon'), Js('Ivory'), Js('Ironbark'), Js('Ebonsteel'), Js('Ebony'), Js('Onyx'), Js('Shadowsteel')]))
var.put('nm4', Js([Js('Bruiser'), Js('Claw'), Js('Maul'), Js('Paw'), Js('Razor'), Js('Render'), Js('Ripper'), Js('Slasher'), Js('Talon'), Js('Razors'), Js('Blades'), Js('Fangs'), Js('Grapple')]))
var.put('nm5', Js([Js('Bruiser'), Js('Claw'), Js('Maul'), Js('Paw'), Js('Razor'), Js('Render'), Js('Ripper'), Js('Slasher'), Js('Talon'), Js('Razors'), Js('Blades'), Js('Fangs'), Js('Grapple'), Js('Allegiance'), Js('Annihilation'), Js('Betrayer'), Js('Bond'), Js('Boon'), Js('Breaker'), Js('Bringer'), Js('Bruiser'), Js('Call'), Js('Champion'), Js('Conqueror'), Js('Crusader'), Js('Cry'), Js('Cunning'), Js('Dawn'), Js('Defender'), Js('Defiler'), Js('Destroyer'), Js('Destruction'), Js('Edge'), Js('Ender'), Js('Executioner'), Js('Fan'), Js('Favor'), Js('Ferocity'), Js('Foe'), Js('Gift'), Js('Glory'), Js('Guardian'), Js('Heirloom'), Js('Hope'), Js('Incarnation'), Js('Last Hope'), Js('Last Stand'), Js('Legacy'), Js('Memory'), Js('Might'), Js('Oath'), Js('Pact'), Js('Pledge'), Js('Promise'), Js('Prophecy'), Js('Protector'), Js('Ravager'), Js('Reach'), Js('Sculptor'), Js('Secret'), Js('Slayer'), Js('Soul'), Js('Terror'), Js('Token'), Js('Touch'), Js('Tribute'), Js('Vengeance'), Js('Voice'), Js('Whisper'), Js('Wit')]))
var.put('nm6', Js([Js('of Agony'), Js('of Ancient Power'), Js('of Anguish'), Js('of Ashes'), Js('of Assassins'), Js('of Black Magic'), Js('of Blessed Fortune'), Js('of Blessings'), Js('of Blight'), Js('of Blood'), Js('of Bloodlust'), Js('of Broken Bones'), Js('of Broken Dreams'), Js('of Broken Families'), Js('of Burdens'), Js('of Chaos'), Js('of Closing Eyes'), Js('of Conquered Worlds'), Js('of Corruption'), Js('of Cruelty'), Js('of Cunning'), Js('of Dark Magic'), Js('of Dark Souls'), Js('of Darkness'), Js('of Decay'), Js('of Deception'), Js('of Degradation'), Js('of Delusions'), Js('of Denial'), Js('of Desecration'), Js('of Diligence'), Js('of Dismay'), Js('of Dragonsouls'), Js('of Due Diligence'), Js('of Echoes'), Js('of Ended Dreams'), Js('of Ending Hope'), Js('of Ending Misery'), Js('of Eternal Bloodlust'), Js('of Eternal Damnation'), Js('of Eternal Glory'), Js('of Eternal Justice'), Js('of Eternal Rest'), Js('of Eternal Sorrow'), Js('of Eternal Struggles'), Js('of Eternity'), Js('of Executions'), Js('of Faded Memories'), Js('of Fallen Souls'), Js('of Fools'), Js('of Frost'), Js('of Frozen Hells'), Js('of Fury'), Js('of Giants'), Js('of Giantslaying'), Js('of Grace'), Js('of Grieving Widows'), Js('of Hate'), Js('of Hatred'), Js("of Hell's Games"), Js('of Hellish Torment'), Js('of Heroes'), Js('of Holy Might'), Js('of Honor'), Js('of Hope'), Js('of Horrid Dreams'), Js('of Horrors'), Js('of Illuminated Dreams'), Js('of Illumination'), Js('of Immortality'), Js('of Inception'), Js('of Infinite Trials'), Js('of Insanity'), Js('of Invocation'), Js('of Justice'), Js("of Light's Hope"), Js('of Lost Comrades'), Js('of Lost Hope'), Js('of Lost Voices'), Js('of Lost Worlds'), Js('of Magic'), Js('of Mercy'), Js('of Misery'), Js('of Mountains'), Js('of Mourning'), Js('of Mystery'), Js('of Necromancy'), Js('of Nightmares'), Js('of Oblivion'), Js('of Perdition'), Js('of Phantoms'), Js('of Power'), Js('of Pride'), Js("of Pride's Fall"), Js('of Putrefaction'), Js('of Reckoning'), Js('of Redemption'), Js('of Regret'), Js('of Riddles'), Js('of Secrecy'), Js('of Secrets'), Js('of Shadow Strikes'), Js('of Shadows'), Js('of Shifting Sands'), Js('of Shifting Worlds'), Js('of Silence'), Js('of Slaughter'), Js('of Souls'), Js('of Stealth'), Js('of Storms'), Js('of Subtlety'), Js('of Suffering'), Js("of Suffering's End"), Js('of Summoning'), Js('of Terror'), Js('of Thunder'), Js('of Time-Lost Memories'), Js('of Timeless Battles'), Js('of Titans'), Js('of Torment'), Js('of Traitors'), Js('of Trembling Hands'), Js('of Trials'), Js('of Truth'), Js("of Twilight's End"), Js('of Twisted Visions'), Js('of Unholy Blight'), Js('of Unholy Might'), Js('of Vengeance'), Js('of Visions'), Js('of Wasted Time'), Js('of Widows'), Js('of Wizardry'), Js('of Woe'), Js('of Wraiths'), Js('of Zeal'), Js('of the Ancients'), Js('of the Banished'), Js('of the Basilisk'), Js('of the Beast'), Js('of the Blessed'), Js('of the Breaking Storm'), Js('of the Brotherhood'), Js('of the Burning Sun'), Js('of the Caged Mind'), Js('of the Cataclysm'), Js('of the Champion'), Js('of the Claw'), Js('of the Corrupted'), Js('of the Covenant'), Js('of the Crown'), Js('of the Damned'), Js('of the Daywalker'), Js('of the Dead'), Js('of the Depth'), Js('of the Dreadlord'), Js('of the Earth'), Js('of the East'), Js('of the Emperor'), Js('of the Empty Void'), Js('of the End'), Js('of the Enigma'), Js('of the Fallen'), Js('of the Falling Sky'), Js('of the Flame'), Js('of the Forest'), Js('of the Forgotten'), Js('of the Forsaken'), Js('of the Gladiator'), Js('of the Harvest'), Js('of the Immortal'), Js('of the Incoming Storm'), Js('of the Insane'), Js('of the King'), Js('of the Lasting Night'), Js('of the Leviathan'), Js('of the Light'), Js('of the Lion'), Js('of the Lionheart'), Js('of the Lone Victor'), Js('of the Lone Wolf'), Js('of the Lost'), Js('of the Moon'), Js('of the Moonwalker'), Js('of the Night Sky'), Js('of the Night'), Js('of the Nightstalker'), Js('of the North'), Js('of the Occult'), Js('of the Oracle'), Js('of the Phoenix'), Js('of the Plague'), Js('of the Prince'), Js('of the Protector'), Js('of the Queen'), Js('of the Serpent'), Js('of the Setting Sun'), Js('of the Shadows'), Js('of the Sky'), Js('of the South'), Js('of the Stars'), Js('of the Storm'), Js('of the Summoner'), Js('of the Sun'), Js('of the Sunwalker'), Js('of the Talon'), Js('of the Undying'), Js('of the Victor'), Js('of the Void'), Js('of the West'), Js('of the Whispers'), Js('of the Wicked'), Js('of the Wind'), Js('of the Wolf'), Js('of the World'), Js('of the Wretched')]))
pass
pass


# Add lib to the module scope
clawNames = var.to_python()
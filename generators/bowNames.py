__all__ = ['bowNames']

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
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
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
var.put('nm1', Js([Js("Hornet's Sting"), Js('Blackened Sky'), Js('Darkened Sky'), Js('Steel Hail'), Js('Archangel'), Js('Archdemon'), Js('Arcus'), Js('Armadillo'), Js('Armageddon'), Js('Arrowsong'), Js('Arrowspike'), Js('Avalance'), Js('Back Pain'), Js('Backsnipe'), Js('Ballista'), Js('Barrage'), Js('Beesting'), Js('Betrayal'), Js("Betrayal's Sting"), Js('Bolt'), Js('Bolt Action'), Js('Bon Voyage'), Js('Bristleblitz'), Js('Bullseye'), Js('Calamity'), Js('Chimera'), Js('Clutch'), Js('Comet'), Js('Courier'), Js('Crier'), Js('Curvey'), Js('Cyclone'), Js('Dash'), Js('Dead Air'), Js("Death's Kiss"), Js("Death's Sigh"), Js("Death's Whisper"), Js('Decimate'), Js('Deliverance'), Js('Deluge'), Js("Destiny's Song"), Js("Devil's Kiss"), Js("Devil's Recurve"), Js("Devil's Sting"), Js("Devil's Whisper"), Js('Doomcaster'), Js('Drawback'), Js('Drawling'), Js('Drawstring'), Js('Dream Catcher'), Js('Eagle'), Js('Eagle Strike'), Js("Emily's Curve"), Js('Euthanasia'), Js('Eye of Eternity'), Js('Eye of Fidelity'), Js('Eye of Precision'), Js('Eye of Truth'), Js('Falling Star'), Js('Featherdraw'), Js('Final Breath'), Js('Final Voyage'), Js('Final Whisper'), Js('Final Whistle'), Js('Firestarter'), Js('Fling'), Js('Flux'), Js('Fury'), Js('Gargoyle'), Js('Graviton'), Js('Hailstorm'), Js('Hamstring'), Js('Hamstrung'), Js('Harbinger'), Js("Hatred's Sting"), Js('Hawkeye'), Js('Heartbeat'), Js('Heartpiercer'), Js('Heartstriker'), Js('Heartstring'), Js('Hedgehog'), Js("Hell's Whistle"), Js('High-Strung'), Js('Hooty Tooty Aim and Shooty'), Js("Hope's End"), Js('Hornet'), Js('Huntress'), Js('Hurricane'), Js('Hush'), Js('Imminent Doom'), Js('Impending Doom'), Js('Irk'), Js('Jugular'), Js('Kiss of Death'), Js('Lash'), Js('Last Kiss'), Js('Last Vision'), Js('Last Whisper'), Js('Lightning'), Js('Lightning Strike'), Js('Long Shot'), Js('Messenger'), Js('Meteor'), Js('Meteor Strike'), Js('Midge'), Js('Mirage'), Js("Misery's End"), Js('Molten Fury'), Js('Mosquito'), Js('Needle Shooter'), Js('Needle Threader'), Js('Netherstrand'), Js('Penetrator'), Js('Perfidy'), Js('Phantom'), Js('Phantom Strike'), Js('Phoenix'), Js('Pierce'), Js('Pinch'), Js('Pique'), Js('Pluck'), Js('Porcupine'), Js('Precise'), Js('Precision'), Js('Prickle'), Js('Prophet'), Js('Puncture'), Js('Quickstrike'), Js('Quillshooter'), Js('Quintain'), Js('Rain Maker'), Js('Razorsong'), Js('Razorwind'), Js('Recurve'), Js('Rigormortis'), Js('Salvation'), Js('Scorpio'), Js('Scorpion'), Js('Scorpion Sting'), Js('Shadow Strike'), Js("Shadow's Bane"), Js("Shadow's Strike"), Js('Shatter Storm'), Js('Shooting Star'), Js('Shriek'), Js('Silent Messenger'), Js('Silentsong'), Js("Siren's Call"), Js("Siren's Cry"), Js("Siren's Song"), Js('Sky Piercer'), Js('Skyfire'), Js('Snatch'), Js('Snipe'), Js('Snitch'), Js('Soulstring'), Js('Special Delivery'), Js('Spitfire'), Js('Splinter'), Js('Splintermark'), Js('Squawk'), Js('Squirm'), Js("Star's Fury"), Js('Starshot'), Js('Starstruck'), Js('Sting'), Js('Stormsong'), Js("Striker's Mark"), Js('Stryker'), Js('Sudden Death'), Js('Surprise'), Js('Swiftwind'), Js('Swoosh'), Js('Talonstrike'), Js('Tempest'), Js('The Ambassador'), Js('The Messenger'), Js('Thunder'), Js('Thunderstrike'), Js('Tiebreaker'), Js('Tranquility'), Js('Trophy Chord'), Js('Trophy Gatherer'), Js('Trophy Mark'), Js('Truestrike'), Js('Tweak'), Js('Twisted'), Js('Twister'), Js('Twitch'), Js('Typhoon'), Js('Valkyrie'), Js('Vehement Chord'), Js('Venomstrike'), Js('Viper'), Js('Vixen'), Js('Vulture'), Js('Warsong'), Js('Wasp'), Js("Wasp's Sting"), Js('Whelm'), Js('Whisper'), Js('Whisperwind'), Js('Windbreaker'), Js('Windforce'), Js('Windlass'), Js('Windrunner'), Js('Windstalker'), Js('Windtalker'), Js('WithDraw')]))
var.put('nm2', Js([Js('Advanced'), Js('Amber Infused'), Js('Ancient'), Js("Anguish'"), Js('Annihilation'), Js('Antique'), Js('Arcane'), Js('Arched'), Js("Archer's"), Js('Assassination'), Js('Atuned'), Js("Bandit's"), Js('Baneful'), Js('Banished'), Js('Barbarian'), Js('Barbaric'), Js('Battleworn'), Js('Blazefury'), Js('Blessed'), Js('Blood Infused'), Js('Bloodcursed'), Js('Bloodied'), Js("Bloodlord's"), Js('Bloodsurge'), Js('Bloodvenom'), Js('Bone Crushing'), Js("Bowman's"), Js('Brutal'), Js('Brutality'), Js('Burnished'), Js('Cataclysm'), Js('Cataclysmic'), Js('Charmed'), Js('Corrupted'), Js('Crazed'), Js('Crying'), Js('Cursed'), Js('Curved'), Js('Dancing'), Js('Defiled'), Js('Deluded'), Js('Demonic'), Js('Deserted'), Js("Desire's"), Js('Desolation'), Js("Destiny's"), Js('Dire'), Js('Doom'), Js("Doom's"), Js("Dragon's"), Js('Dragonbreath'), Js('Dreadful'), Js('Ebon'), Js('Eerie'), Js('Enchanted'), Js('Engraved'), Js('Eternal'), Js('Ethereal'), Js('Executing'), Js('Exiled'), Js("Expert's"), Js('Extinction'), Js("Faith's"), Js('Faithful'), Js('Fancy'), Js('Fearful'), Js('Feather-Wrapped'), Js('Featherdraw'), Js('Feral'), Js('Fierce'), Js('Fiery'), Js('Fine'), Js('Firestorm'), Js('Flimsy'), Js('Forsaken'), Js("Fortune's"), Js('Fragile'), Js('Frail'), Js('Frenzied'), Js('Frost'), Js('Frozen'), Js('Furious'), Js('Fusion'), Js('Ghastly'), Js('Ghostly'), Js('Gladiator'), Js("Gladiator's"), Js('Grieving'), Js("Guard's"), Js("Guardian's"), Js('Hateful'), Js('Haunted'), Js('Heavy'), Js('Hollow'), Js('Holy'), Js('Honed'), Js("Honor's"), Js("Hope's"), Js('Hopeless'), Js('Howling'), Js('Hungering'), Js('Improved'), Js('Incarnated'), Js('Infused'), Js('Inherited'), Js('Isolated'), Js('Jade Infused'), Js('Judgement'), Js("Liar's"), Js('Lich'), Js('Lightning'), Js('Lonely'), Js('Loyal'), Js('Lustful'), Js('Lusting'), Js("Mage's"), Js('Malevolent'), Js('Malicious'), Js('Malignant'), Js('Massive'), Js("Master Hunter's"), Js('Mended'), Js('Mercenary'), Js('Military'), Js("Misfortune's"), Js('Mourning'), Js('Nightmare'), Js('Nightstalker'), Js('Ominous'), Js('Peacekeeper'), Js('Phantom'), Js('Possessed'), Js("Pride's"), Js('Prideful'), Js('Primitive'), Js('Promised'), Js("Protector's"), Js('Proud'), Js("Ranger's"), Js("Recruit's"), Js('Reincarnated'), Js('Relentless'), Js('Remorseful'), Js('Renewed'), Js('Renovated'), Js('Replica'), Js('Restored'), Js('Retribution'), Js('Ritual'), Js('Roaring'), Js('Savage'), Js("Oathkeeper's"), Js('Shadow'), Js('Shadowleaf'), Js('Shrieking'), Js('Silent'), Js('Singed'), Js('Singing'), Js('Sinister'), Js('Skullforge'), Js('Skyfall'), Js('Smooth'), Js("Solitude's"), Js("Sorrow's"), Js('Soul'), Js('Soul Infused'), Js('Soulcursed'), Js('Soulless'), Js('Spectral'), Js('Spiteful'), Js('Storm'), Js("Storm's"), Js('Stormfury'), Js('Stormguard'), Js('Stout'), Js("Striker's"), Js('Sturdy'), Js('Terror'), Js('Thirsting'), Js('Thirsty'), Js('Thunder'), Js('Thunderfury'), Js('Thunderguard'), Js('Thundersoul'), Js('Timeworn'), Js('Tormented'), Js('Tracking'), Js("Trainee's"), Js("Trapper's"), Js("Treachery's"), Js('Twilight'), Js("Twilight's"), Js('Twisted'), Js('Tyrannical'), Js('Undead'), Js('Unholy'), Js('Vengeance'), Js('Vengeful'), Js('Venom'), Js('Vicious'), Js('Vindication'), Js('Vindictive'), Js('Void'), Js('Volcanic'), Js('Vowed'), Js('War-Forged'), Js("Warlord's"), Js('Warp'), Js('Warped'), Js('Warsong'), Js('Well Crafted'), Js('Whistling'), Js('Wicked'), Js("Wind's"), Js('Windsong'), Js('Woeful'), Js('Wrathful'), Js('Wretched'), Js('Yearning'), Js('Yielding'), Js('Zealous')]))
var.put('nm3', Js([Js('Ashwood'), Js('Bone'), Js('Bronzed'), Js('Driftwood'), Js('Ebon'), Js('Hardwood'), Js('Iron'), Js('Ironbark'), Js('Maple'), Js('Oak'), Js('Redwood'), Js('Skeletal'), Js('Steel'), Js('Titanium'), Js('Warpwood'), Js('Willow'), Js('Yew')]))
var.put('nm4', Js([Js('Longbow'), Js('Shortbow'), Js('Crossbow'), Js('Speargun'), Js('Launcher'), Js('Repeater'), Js('Shooter'), Js('Crossfire'), Js('Bolter'), Js('Heavy Crossbow'), Js('Arbalest'), Js('Piercer'), Js('Striker'), Js('Warbow'), Js('Chord'), Js('Recurve'), Js('Bow'), Js('Compound Bow'), Js('Hunting Bow'), Js('Warp-Bow'), Js('Flatbow'), Js('Reflex Bow'), Js('Composite Bow'), Js('Compound Crossbow'), Js('Straight Bow'), Js('Self Bow')]))
var.put('nm5', Js([Js('Annihilation'), Js('Arbalest'), Js('Arch'), Js('Betrayer'), Js('Bite'), Js('Bolter'), Js('Bond'), Js('Boon'), Js('Bow'), Js('Breaker'), Js('Bringer'), Js('Call'), Js('Champion'), Js('Chord'), Js('Composite Bow'), Js('Compound Bow'), Js('Crescent'), Js('Crook'), Js('Crossbow'), Js('Crossfire'), Js('Cry'), Js('Cunning'), Js('Curve'), Js('Dawn'), Js('Defiler'), Js('Destroyer'), Js('Eclipse'), Js('Ellipse'), Js('Ender'), Js('Etcher'), Js('Executioner'), Js('Eye'), Js('Favor'), Js('Ferocity'), Js('Flatbow'), Js('Foe'), Js('Gift'), Js('Glory'), Js('Guardian'), Js('Heavy Crossbow'), Js('Heirloom'), Js('Hope'), Js('Hunting Bow'), Js('Incarnation'), Js('Kiss'), Js('Last Hope'), Js('Last Stand'), Js('Launcher'), Js('Legacy'), Js('Longbow'), Js('Memory'), Js('Might'), Js('Oath'), Js('Pact'), Js('Piercer'), Js('Pique'), Js('Pledge'), Js('Poke'), Js('Prick'), Js('Promise'), Js('Protector'), Js('Ravager'), Js('Reach'), Js('Recurve'), Js('Reflex Bow'), Js('Repeater'), Js('Savagery'), Js('Secret'), Js('Self Bow'), Js('Shooter'), Js('Shortbow'), Js('Skewer'), Js('Soul'), Js('Speargun'), Js('Spike'), Js('Spine'), Js('Straight Bow'), Js('Striker'), Js('String'), Js('Terror'), Js('Token'), Js('Tribute'), Js('Vengeance'), Js('Voice'), Js('Warbow'), Js('Warp-Bow'), Js('Whisper'), Js('Wit')]))
var.put('nm6', Js([Js('of Agony'), Js('of Ancient Power'), Js('of Anguish'), Js('of Ashes'), Js('of Assassins'), Js('of Black Magic'), Js('of Blessed Fortune'), Js('of Blessings'), Js('of Blight'), Js('of Blood'), Js('of Bloodlust'), Js('of Broken Bones'), Js('of Broken Dreams'), Js('of Broken Families'), Js('of Burdens'), Js('of Chaos'), Js('of Closing Eyes'), Js('of Conquered Worlds'), Js('of Corruption'), Js('of Cruelty'), Js('of Cunning'), Js('of Dark Magic'), Js('of Dark Souls'), Js('of Darkness'), Js('of Decay'), Js('of Deception'), Js('of Degradation'), Js('of Delusions'), Js('of Denial'), Js('of Desecration'), Js('of Diligence'), Js('of Dismay'), Js('of Dragonsouls'), Js('of Due Diligence'), Js('of Echoes'), Js('of Ended Dreams'), Js('of Ending Hope'), Js('of Ending Misery'), Js('of Eternal Bloodlust'), Js('of Eternal Damnation'), Js('of Eternal Glory'), Js('of Eternal Justice'), Js('of Eternal Rest'), Js('of Eternal Sorrow'), Js('of Eternal Struggles'), Js('of Eternity'), Js('of Executions'), Js('of Faded Memories'), Js('of Fallen Souls'), Js('of Fools'), Js('of Frost'), Js('of Frozen Hells'), Js('of Fury'), Js('of Giants'), Js('of Giantslaying'), Js('of Grace'), Js('of Grieving Widows'), Js('of Hate'), Js('of Hatred'), Js("of Hell's Games"), Js('of Hellish Torment'), Js('of Heroes'), Js('of Holy Might'), Js('of Honor'), Js('of Hope'), Js('of Horrid Dreams'), Js('of Horrors'), Js('of Illuminated Dreams'), Js('of Illumination'), Js('of Immortality'), Js('of Inception'), Js('of Infinite Trials'), Js('of Insanity'), Js('of Invocation'), Js('of Justice'), Js("of Light's Hope"), Js('of Lost Comrades'), Js('of Lost Hope'), Js('of Lost Voices'), Js('of Lost Worlds'), Js('of Magic'), Js('of Mercy'), Js('of Misery'), Js('of Mountains'), Js('of Mourning'), Js('of Mystery'), Js('of Necromancy'), Js('of Nightmares'), Js('of Oblivion'), Js('of Perdition'), Js('of Phantoms'), Js('of Power'), Js('of Pride'), Js("of Pride's Fall"), Js('of Putrefaction'), Js('of Reckoning'), Js('of Redemption'), Js('of Regret'), Js('of Riddles'), Js('of Secrecy'), Js('of Secrets'), Js('of Shadow Strikes'), Js('of Shadows'), Js('of Shifting Sands'), Js('of Shifting Worlds'), Js('of Silence'), Js('of Slaughter'), Js('of Souls'), Js('of Stealth'), Js('of Storms'), Js('of Subtlety'), Js('of Suffering'), Js("of Suffering's End"), Js('of Summoning'), Js('of Terror'), Js('of Thunder'), Js('of Time-Lost Memories'), Js('of Timeless Battles'), Js('of Titans'), Js('of Torment'), Js('of Traitors'), Js('of Trembling Hands'), Js('of Trials'), Js('of Truth'), Js("of Twilight's End"), Js('of Twisted Visions'), Js('of Unholy Blight'), Js('of Unholy Might'), Js('of Vengeance'), Js('of Visions'), Js('of Wasted Time'), Js('of Widows'), Js('of Wizardry'), Js('of Woe'), Js('of Wraiths'), Js('of Zeal'), Js('of the Ancients'), Js('of the Banished'), Js('of the Basilisk'), Js('of the Beast'), Js('of the Blessed'), Js('of the Breaking Storm'), Js('of the Brotherhood'), Js('of the Burning Sun'), Js('of the Caged Mind'), Js('of the Cataclysm'), Js('of the Champion'), Js('of the Claw'), Js('of the Corrupted'), Js('of the Covenant'), Js('of the Crown'), Js('of the Damned'), Js('of the Daywalker'), Js('of the Dead'), Js('of the Depth'), Js('of the Dreadlord'), Js('of the Earth'), Js('of the East'), Js('of the Emperor'), Js('of the Empty Void'), Js('of the End'), Js('of the Enigma'), Js('of the Fallen'), Js('of the Falling Sky'), Js('of the Flame'), Js('of the Forest'), Js('of the Forgotten'), Js('of the Forsaken'), Js('of the Gladiator'), Js('of the Harvest'), Js('of the Immortal'), Js('of the Incoming Storm'), Js('of the Insane'), Js('of the King'), Js('of the Lasting Night'), Js('of the Leviathan'), Js('of the Light'), Js('of the Lion'), Js('of the Lionheart'), Js('of the Lone Victor'), Js('of the Lone Wolf'), Js('of the Lost'), Js('of the Moon'), Js('of the Moonwalker'), Js('of the Night Sky'), Js('of the Night'), Js('of the Nightstalker'), Js('of the North'), Js('of the Occult'), Js('of the Oracle'), Js('of the Phoenix'), Js('of the Plague'), Js('of the Prince'), Js('of the Protector'), Js('of the Queen'), Js('of the Serpent'), Js('of the Setting Sun'), Js('of the Shadows'), Js('of the Sky'), Js('of the South'), Js('of the Stars'), Js('of the Storm'), Js('of the Summoner'), Js('of the Sun'), Js('of the Sunwalker'), Js('of the Talon'), Js('of the Undying'), Js('of the Victor'), Js('of the Void'), Js('of the West'), Js('of the Whispers'), Js('of the Wicked'), Js('of the Wind'), Js('of the Wolf'), Js('of the World'), Js('of the Wretched')]))
var.put('nm7', Js([Js('Archangel'), Js('Archdemon'), Js('Arcus'), Js('Armadillo'), Js('Armageddon'), Js('Arrowsong'), Js('Arrowspike'), Js('Avalance'), Js('Back Pain'), Js('Backsnipe'), Js('Ballista'), Js('Barrage'), Js('Beesting'), Js('Betrayal'), Js("Betrayal's Sting"), Js('Bolt'), Js('Bon Voyage'), Js('Bristleblitz'), Js('Bullseye'), Js('Calamity'), Js('Chimera'), Js('Clutch'), Js('Comet'), Js('Courier'), Js('Crier'), Js('Curvey'), Js('Cyclone'), Js('Dash'), Js('Dead Air'), Js("Death's Kiss"), Js("Death's Sigh"), Js("Death's Whisper"), Js('Decimate'), Js('Deliverance'), Js('Deluge'), Js("Destiny's Song"), Js("Devil's Kiss"), Js("Devil's Recurve"), Js("Devil's Sting"), Js("Devil's Whisper"), Js('Doomcaster'), Js('Drawback'), Js('Drawling'), Js('Drawstring'), Js('Dream Catcher'), Js('Eagle'), Js('Eagle Strike'), Js("Emily's Curve"), Js('Euthanasia'), Js('Falling Star'), Js('Featherdraw'), Js('Firestarter'), Js('Fling'), Js('Flux'), Js('Fury'), Js('Gargoyle'), Js('Graviton'), Js('Hailstorm'), Js('Hamstring'), Js('Hamstrung'), Js('Harbinger'), Js("Hatred's Sting"), Js('Hawkeye'), Js('Heartbeat'), Js('Heartpiercer'), Js('Heartstriker'), Js('Heartstring'), Js('Hedgehog'), Js("Hell's Whistle"), Js('High-Strung'), Js("Hope's End"), Js('Hornet'), Js('Huntress'), Js('Hurricane'), Js('Hush'), Js('Irk'), Js('Jugular'), Js('Kiss of Death'), Js('Lash'), Js('Lightning'), Js('Long Shot'), Js('Messenger'), Js('Meteor'), Js('Midge'), Js('Mirage'), Js("Misery's End"), Js('Molten Fury'), Js('Mosquito'), Js('Netherstrand'), Js('Penetrator'), Js('Perfidy'), Js('Phantom'), Js('Phantom Strike'), Js('Phoenix'), Js('Pierce'), Js('Pinch'), Js('Pique'), Js('Pluck'), Js('Porcupine'), Js('Precise'), Js('Precision'), Js('Prickle'), Js('Prophet'), Js('Puncture'), Js('Quickstrike'), Js('Quintain'), Js('Rain Maker'), Js('Razorsong'), Js('Razorwind'), Js('Recurve'), Js('Rigormortis'), Js('Salvation'), Js('Scorpio'), Js('Scorpion'), Js('Shadow Strike'), Js('Shooting Star'), Js('Shriek'), Js('Silent Messenger'), Js('Silentsong'), Js("Siren's Call"), Js("Siren's Cry"), Js("Siren's Song"), Js('Sky Piercer'), Js('Skyfire'), Js('Snatch'), Js('Snipe'), Js('Snitch'), Js('Soulstring'), Js('Spitfire'), Js('Splinter'), Js('Splintermark'), Js('Squawk'), Js('Squirm'), Js("Star's Fury"), Js('Starshot'), Js('Starstruck'), Js('Sting'), Js('Stormsong'), Js('Stryker'), Js('Surprise'), Js('Swiftwind'), Js('Swoosh'), Js('Talonstrike'), Js('Tempest'), Js('The Ambassador'), Js('The Messenger'), Js('Thunder'), Js('Thunderstrike'), Js('Tiebreaker'), Js('Tranquility'), Js('Truestrike'), Js('Tweak'), Js('Twisted'), Js('Twister'), Js('Twitch'), Js('Typhoon'), Js('Valkyrie'), Js('Venomstrike'), Js('Viper'), Js('Vixen'), Js('Vulture'), Js('Warsong'), Js('Wasp'), Js('Whelm'), Js('Whisper'), Js('Whisperwind'), Js('Windbreaker'), Js('Windforce'), Js('Windlass'), Js('Windrunner'), Js('Windstalker'), Js('Windtalker'), Js('WithDraw')]))
pass
pass


# Add lib to the module scope
bowNames = var.to_python()
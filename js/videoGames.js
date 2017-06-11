var br = "";
function nameGen(){
	var choice = $("#radioChoice input[type='radio']:checked").val();
	var names1 = ["Ace","Alien","Alpha","Ancient","Android","Angel","Arctic","Armageddon","Armed","Armored","Atomic","Bad","Battle","Bio","Bionic","Blood","Broken","Brutal","Bullet","Cannibal","Carnivore","Celestial","Chaos","Chrome","Cloud","Cold","Combat","Cosmic","Covert","Crimson","Cursed","Dark","Dead","Death","Demon","Dragon","Ebon","Emergency","Enemy","Eternal","Evil","Final","Forbidden","Forgotten","Frozen","Fury","Future","Galaxy","Ghost","Grand","Hallowed","Honor","Human","Hunting","Immortal","Infected","Infernal","Infinite","Just","Killing","Lifeless","Light","Lost","Lunar","Mass","Metal","Midnight","Monster","Mortal","Nuclear","Obscure","Parasite","Phantom","Primal","Prime","Private","Red","Sacred","Saint","Secret","Shadow","Silent","Silver","Solar","Solitary","Soul","Space","Special","Spirit","Star","Storm","Tactical","Thunder","Titan","Twilight","Vampire","Warrior","Werewolf","Zero","Zombie"];
	var names2 = ["Abyss","Aftermath","Age","Agent","Alert","Alias","Alliance","Apocalypse","Armada","Assault","Asylum","Attack","Barrage","Betrayal","Blade","Bounty","Breakout","Breed","Calamity","Call","Campaign","Carnage","Castle","Cavern","Cell","Chronicles","Collapse","Command","Complex","Conflict","Conquest","Conspiracy","Crossing","Crusade","Cry","Curse","Dream","Edge","Ego","Elements","Emergency","Escape","Evolution","Experiment","Fear","Freedom","Frontier","Games","Guardians","Harvest","Haven","Hazard","Heart","Hero","Impact","Inquisition","Invasion","Island","Kingdom","Legacy","Legend","Machine","Mask","Master","Matters","Mercenary","Money","Network","Nightmare","Omen","Operation","Panic","Possession","Predator","Premonition","Project","Prototype","Rage","Realm","Reaver","Resurrection","Retribution","Rising","Road","Signs","Siren","State","Survival","Syndrome","System","Tales","Theft","Tombs","Universe","Vendetta","Virus","Voyage","Warfare","Woods","World","Wrath"];
	var names3 = ["Arm","Assault","Attack","Battle","Besiege","Blast","Bombard","Breakout","Burn","Charge","Chase","Clash","Command","Conquer","Counter","Crash","Crush","Decimate","Defeat","Demolish","Destroy","Divide","Escape","Fight","Fortify","Guard","Hunt","Incinerate","Infect","Invade","Kill","Knockout","Pillage","Plan","Protect","Raid","Rescue","Resist","Retaliate","Revolt","Rise","Rule","Run","Shoot","Strategize","Strife","Strike","Struggle","Vengeance","Wipe Out"];
	var names4 = ["Aggression","Assault","Atonement","Autonomy","Betrayal","Campaigns","Combat","Conflict","Deception","Democracy","Duplicity","Enforce","Execution","Freedom","Friction","Heroes","Heroics","Hypocrisy","Immunity","Infringement","Invasion","Law","Liberty","Lies","Logic","Opportunity","Order","Power","Privilige","Prosecution","Reason","Redemption","Regulations","Rescue","Resitution","Retribution","Rivalry","Rule","Salvation","Stipulation","Strife","Struggle","Transgression","Treachery","Trickery","Truth","Vengeance","Violation","War","Wrath"];
	var names5 = ["Age","Annihilation","Apocalypse","Barrage","Battle","Battlefield","Born","Bridge","Burial","Century","Chamber","Chase","Chronicle","City","Codename","Command","Contract","Crime","Crisis","Cult","Danger","Day","Days","Death","Decade","Defense","Descent","Destruction","Dimension","Doom","Dream","Dynasty","Echoes","Edge","Embers","Empire","Epoch","Escalation","Execution","Extinction","Fight","Flashbacks","Force","Fortress","Galaxy","Game","Garden","Gateway","Genesis","Genocide","Ghosts","Glitch","Graves","Guns","Hazard","Home","House","Hunt","Impact","Invasion","Journey","Knights","Land","Law","Life","Matter","Maze","Memories","Murder","Nature","Order","Paradise","Planet","Power","Quest","Raid","Remorse","Renegade","Retribution","Revenge","Revival","Rush","Science","Shadow","Sons","Source","Space","Spells","Streets","Sword","Symphony","Thunder","Treasures","Voyage","Weapons","Week","Whispers","Words","World","Year"];
	var names6 = ["Action","Agony","Ambition","Anarchy","Androids","Angels","Armor","Awe","Barbarians","Blood","Chaos","Conflict","Control","Death","Demons","Despair","Destruction","Disarray","Disorder","Domination","Doubt","Dragons","Dread","Dust","Duty","Earth","Evil","Evolution","Existence","Explosions","Faith","Fate","Fear","Fire","Fortune","Freedom","Frenzy","Gangs","Gods","Harmony","Havoc","Hell","Heroes","Honor","Hope","Immortals","Infinity","Innocents","Insanity","Kings","Legends","Liberty","Lies","Logic","Mayhem","Misery","Mortals","Mutants","Mystery","Nature","Nightmares","Nothing","Oracles","Order","Pain","Panic","Power","Predators","Prototypes","Rage","Reason","Reckoning","Redemption","Resistance","Revolution","Riddles","Rubble","Sacrifice","Salvation","Sanity","Secrets","Shadows","Skeletons","Skulls","Solitude","Souls","Stealth","Struggle","Terror","Time","Treason","Truth","Twisted Dreams","Valor","Vampires","Victory","War","Warfare","Werewolves","Zombies"];
	var names7 = ["Air","Alpha","Alter","Anti","Arche","Astro","Back","Battle","Bio","Blade","Blaster","Block","Blood","Blue","Body","Border","Brutal","Bullet","Castle","Chroma","Cloud","Cluster","Cross","Crystal","Cyber","Data","Dead","Def","Delta","Demon","Dragon","Dread","Dream","Dyna","Ember","Endor","Ever","Evo","Ex","Far","Fire","Fuse","Fusion","Geo","Grim","Hell","Mad","Master","Ultra","War"];
	var names8 = ["back","blade","blast","blaze","borne","bot","cell","chase","core","craft","craze","cry","doom","droid","dude","fight","fire","flight","force","gene","heart","hunt","land","life","light","line","lust","mania","mind","nite","phobia","plan","point","rage","rain","reign","rush","scape","shock","shot","side","site","sky","space","star","storm","tech","watch","wind","works","zone"];

	switch(choice){
		case("adventure"):
			names1 = ["Alien","Altered","Amber","Angelic","Bad","Banished","Bionic","Black","Blind","Blood","Broken","Brutal","Chaos","Chrono","Clockwork","Covert","Criminal","Crimson","Crystal","Cyber","Dark","Dead","Demonic","Digital","Dragon","Dread","Dual","Eastern","Ebon","Eclipsed","Elder","Enchanted","Endless","Epic","Eternal","Evil","Faery","Fatal","Fearless","Forbidden","Forgotten","Forsaken","Fortunate","Full On","Future","Global","Grand","Gray","Guilty","Happy","Hard","Haunted","Hero","Heroic","Hidden","Holy","Immoral","Immortal","Innocent","Invisible","Iron","Jade","Jungle","King's","Last","Magic","Midnight","Midsummer","Missing","Mortal","Mystery","Necro","Obsidian","Paradise","Parellel","Phantom","Primal","Prime","Project","Red","Rising","Robo","Royal","Sanguine","Shadow","Silent","Silver","Solar","Solstice","Space","Star","Tiny","Twilight","Twisted","Uncanny","Vampire","War","Werewolf","Whispering","Wild"];
			names2 = ["Abyss","Adventure","Age","Agent","Alchemy","Alien","Angel","Assassin","Assault","Attack","Betrayal","Blade","Canvas","Castle","Chamber","Circle","Code","Codex","Colony","Command","Conspiracy","Core","Crisis","Crown","Cry","Curse","Dawn","Days","Death","Demon","Destiny","Dimension","Disciple","Downfall","Dragon","Dream","Earth","Echo","Ego","Empire","Enigma","Escape","Evolution","Fantasy","Force","Gates","Guard","Halo","Heart","Honor","Inferno","Invasion","Investigation","Island","Kingdom","Kiss","Knight","Legacy","Lesson","Life","Light","Magic","Master","Memory","Mind","Mirror","Moon","Murder","Mystery","Nemesis","Nightmare","Oblivion","Oracle","Origin","Paragon","Path","Planet","Power","Pride","Realm","Report","Resurrection","Secrets","Sect","Seed","Shadows","Smile","Soul","Sun","Sword","Syndrome","Tide","Time","Tomb","Trail","Treasure","Tribe","Trinity","Venture","Wish"];
			names3 = ["Angels","Barbarians","Castles","Codes","Conquest","Crowns","Curses","Demons","Dragons","Dreams","Elves","Ghosts","Giants","Goblins","Illusions","Kings","Knights","Legends","Lords","Love","Magic","Monsters","Mysteries","Nightmares","Orcs","Outlaws","Phantoms","Pirates","Power","Prophecies","Realms","Riddles","Robots","Sailors","Secrets","Shadows","Shields","Ships","Sorcery","Souls","Spells","Spirits","Swords","Traitors","Treasures","Vampires","Vikings","War","Werewolves","Wizards"];
			names4 = ["Betrayal","Blasphemy","Bravery","Conquest","Conspiracies","Danger","Darkness","Death","Deception","Discipline","Dishonor","Eternity","Exploration","Faith","Fate","Fortune","Hauntings","Honor","Hope","Horrors","Infinity","Justice","Labyrinths","Legacies","Legends","Lies","Madness","Memories","Miracles","Murder","Mystery","Nightmares","Origins","Power","Revelations","Riddles","Rituals","Romance","Secrets","Shadows","Silence","Sins","Solitude","Sorrow","Stories","Theories","Time","Traps","Vengeance","War"];
			names5 = ["Abyss","Adventure","Age","Agent","Angel","Art","Assassins","Awakening","Beginning","Betrayal","Blade","Book","Burden","Case","Children","Chronicles","Circle","City","Conquest","Core","Creatures","Crypt","Cult","Curse","Danger","Darkness","Dawn","Death","Deception","Demon","Desire","Division","Doom","Dream","Dungeon","Edge","Enemy","Evil","Face","Fall","Fate","Forest","Game","Gate","God","Gravity","Guardians","Guilt","Hand","Heart","Heroes","House","Illusion","Immortals","Journey","King","Kingdom","Knight","Lair","Land","Last","Legacy","Legend","Light","Lord","Magic","Memories","Messenger","Monsters","Mortals","Mountain","Murder","Mystery","Oracle","Origin","Passage","Path","Phantom","Planet","Prisoner","Quest","Revelation","Riddles","Search","Secret","Seed","Shadows","Society","Soul","Sword","Tales","Temptation","Throne","Time","Tombs","Traitor","Truth","Voice","Whispers","World"];
			names6 = ["Adventure","Agony","Alchemy","Ancestors","Ancients","Angels","Autumn","Beasts","Blood","Chaos","Clans","Conspiracies","Corruption","Curses","Dark Motives","Darkness","Death","Desire","Destiny","Destruction","Dimensions","Doom","Dragons","Dreams","Echos","Eden","Elements","Enlightenment","Eternity","Evidence","Experiments","Faith","Fear","Fire","Giants","Gods","Gold","Happiness","Hatred","Heaven","Hell","Heroes","History","Honor","Hope","Illusions","Immortality","Infection","Infinity","Invention","Justice","Kings","Lies","Light","Love","Magic","Memories","Monsters","Mortality","Murder","Mutation","Mystery","Nightmares","Nothing","Obedience","Obsidian","Paradise","Power","Prophecies","Redemption","Relics","Riddles","Secrets","Separation","Serenity","Shadows","Silence","Silver","Sin","Sorrow","Souls","Space","Spirits","Spring","Stars","Summer","Survival","Time","Time Travel","Tomorrow","Tranquility","Treasure","Trinkets","Trust","Twilight","Valor","Vengeance","War","Winter","Wisdom"];
			names7 = ["Abyss","Alter","Anti","Arche","Astro","Battle","Bio","Blood","Border","Brutal","Bullet","Castle","Chrono","Cloud","Crystal","Cyber","Dark","Data","Dead","Demon","Dragon","Dread","Dream","Dyna","Ebon","Ember","Ever","Evo","Far","Fire","Fuse","Ghost","Grim","Hallow","Heaven","Hell","Hero","Inner","Iron","Knight","Light","Mad","Magic","Master","Mortal","Night","Phantom","Quest","Soul","War"];
			names8 = ["blade","scape","blaze","borne","bot","cast","cell","craft","crest","cry","doom","drift","droid","fight","fire","flight","force","heart","hunt","kin","land","light","line","mare","master","mind","mist","more","nite","path","piece","point","polis","rage","realm","reign","rite","rush","scape","ship","side","space","star","storm","tale","tomb","trail","view","ville","watch","way"];
			break;
		case("role-playing"):
			names1 = ["Alien","Ancestor","Arcane","Assassin","Battle","Birthright","Blood","Bloodline","Brave","Broken","Castle","Chaos","Chosen","Clone","Covert","Creature","Crystal","Dark","Dawn","Death","Demon","Divine","Dragon","Dungeon","Endless","Epic","Eternal","Exiled","Fallen","Fantasy","Forbidden","Forsaken","Freedom","Full Moon","Ghost","Golden","Gothic","Grand","Grim","Holy","Honest","Immortal","Incredible","Infernal","Infinite","Iron","Kingdom","Knight","Knightmare","Last","Lifeless","Lightning","Lost","Love","Mage","Magic","Majestic","Master","Metal","Monster","Moonlight","Morbid","Mortal","Mutant","Mystic","Nether","Night","Obsidian","Paradise","Phantom","Pioneer","Pirate","Plague","Planetary","Raiding","Rainbow","Reborn","Royal","Rune","Sacred","Scarlet","Shadow","Shapeshifter","Shattered","Simple","Soul","Space","Spellborn","Star","Stolen","Storm","Sunset","Tempest","Thunder","Ultimate","Undead","Undercover","Underworld","Vampire","Werewolf"];
			names2 = ["Adventure","Age","Awakening","Blade","Blitz","Brotherhood","Call","Challenge","Champions","Choice","Chronicles","Citizen","City","Clans","Clash","Colony","Crusade","Curse","Dawn","Defender","Desciple","Destiny","Dimension","Dominion","Dungeon","Empire","Evolution","Expedition","Faction","Fate","Flames","Force","Gates","Genesis","God","Guilds","Harbinger","Harvest","Heaven","Hell","Hero","Heroes","History","Hunter","Inferno","Invasion","Isle","King","Labyrinth","Lair","Lands","Legacy","Legend","Legends","Legions","Lord","Might","Mythos","Nightmare","Oath","Odyssey","Omen","Origins","Paradise","Past","Power","Prince","Prophecy","Quest","Reach","Realm","Reaper","Reign","Revelations","Rise","Rising","Saga","Sanctuary","School","Secrets","Siege","Skies","Sorcery","Soul","Spyre","Story","Stronghold","Surprise","Tale","Throne","Time","Treasure","Tribes","Universe","Vaults","War","Ward","Watch","Wizards","World"];
			names3 = ["Angels","Barbarians","Castles","Codes","Conquest","Crowns","Curses","Demons","Dragons","Dreams","Elves","Ghosts","Giants","Goblins","Illusions","Kings","Knights","Legends","Lords","Love","Magic","Monsters","Mysteries","Nightmares","Orcs","Outlaws","Phantoms","Pirates","Power","Prophecies","Realms","Riddles","Robots","Sailors","Secrets","Shadows","Shields","Ships","Sorcery","Souls","Spells","Spirits","Swords","Traitors","Treasures","Vampires","Vikings","War","Werewolves","Wizards"];
			names4 = ["Betrayal","Bravery","Conjury","Conquest","Danger","Darkness","Death","Deception","Enigmas","Exploration","Fables","Faith","Fate","Fortune","Hauntings","Heirlooms","Heritage","Honor","Hope","Horrors","Justice","Labyrinths","Legacies","Legends","Lore","Love","Magic","Memories","Miracles","Murder","Mystery","Mythology","Mythos","Myths","Nightmares","Oracles","Origins","Riddles","Rituals","Romance","Runes","Secrets","Shadows","Sins","Sorrow","Supremacy","Time","Triumph","Victory","Witchcraft"];
			names5 = ["Aeon","Age","Agent","Angel","Armies","Ashes","Aura","Blade","Book","Burden","Case","Century","Challenges","Champions","Children","Chronicles","Circle","City","Clans","Core","Corruption","Creatures","Crypt","Cult","Curse","Dawn","Death","Demons","Destiny","Dimension","Division","Dominion","Doom","Dreams","Dungeons","Edge","Empire","Enemy","Era","Evil","Fables","Face","Faith","Fall","Fate","Fire","Forest","Game","God","Gods","Guardians","Guilds","Heart","Heroes","Immortals","Invasion","Journey","Kingdom","Kings","Knights","Lair","Land","Legacy","Legend","Legends","Lords","Masters","Monsters","Mortals","Mysteries","Myths","Oracles","Origin","Path","Planet","Quests","Realm","Revelations","Rise","Saga","Saints","School","Search","Secret","Seed","Shadows","Souls","Swords","Tale","Tales","Throne","Time","Titans","Tombs","Tribes","Voice","Voices","Whispers","Winds","World"];
			names6 = ["Alchemy","Aliens","Anarchy","Ancestors","Angels","Autumn","Blood","Chaos","Crimson","Crisis","Darkness","Death","Destruction","Discovery","Dominion","Doom","Dragons","Dreams","Dust","Dystopia","Earth","Echoes","Eden","Elements","Eternity","Euphoria","Evil","Evolution","Exiles","Exploration","Fate","Fear","Fire","Fortune","Fury","Gods","Gold","Greed","Grimoires","Guilds","Heaven","History","Honesty","Honor","Hope","Infernals","Infinity","Iron","Judgement","Kings","Knights","Labyrinths","Legions","Light","Lore","Love","Magic","Malice","Mankind","Might","Money","Moonlight","Mystery","Necromancy","New Earth","Nightmares","Power","Prophecies","Rage","Realms","Rebirth","Reckoning","Retribution","Romance","Ruins","Runes","Savagery","Science","Sin","Sorcery","Souls","Spring","Stars","Steel","Summer","Thieves","Thunder","Time","Trials","Truth","Twilight","Undeath","Utopia","Valor","Vampires","Vengeance","Virtue","War","Werewolves","Winter"];
			names7 = ["Arcane","Arche","Astro","Battle","Bio","Blood","Brutal","Castle","Chrono","Dark","Dead","Demon","Dragon","Dream","Ember","Ever","Far","Fire","Ghost","Grim","Heaven","Hell","Hero","Iron","Knight","Light","Mage","Magic","Master","Mortal","Night","Phantom","Quest","Raid","Rune","Sacred","Scarlet","Shadow","Shard","Siege","Sky","Soul","Space","Spell","Star","Storm","Strong","Thunder","Trade","War"];
			names8 = ["age","band","blade","borne","child","craft","crest","cry","doom","fight","fire","flight","force","gate","guard","guild","heart","hunt","kin","land","line","mare","master","mind","more","night","path","phase","realm","reign","rite","run","scape","shift","side","slayer","space","sphere","star","stone","storm","tale","tide","time","trail","vale","view","ville","watch","way"];
			break;
		case("simulation"):
			names1 = ["Bow","Gun","Crossbow","Rifle","Blade","Sword","Cannon","Agriculture","Airport","Alien","Android","Apocalypse","Armored","Assault","Base","Battle","Battlecruiser","Beach","Boat","Business","Car","Chaos","City","Colony","Combat","Conflict","Construction","Cooking","Corporation","Crime","Crisis","Damage","Demolition","Destruction","Disaster","Disease","Drive","Driving","Droid","Empire","Evolution","Exploration","Family","Farm","Fishing","Flight","Future","Galactic","Galaxy","God","Helicopter","History","Hospital","House","Hunter","Jet","Jetfighter","Kingdom","Knight","Lightspeed","Lunar","Mech","Medieval","Mining","Nation","Nuclear","Panzer","Party","Patrol","Pilot","Plane","Police","President","Rail","Railroad","Robot","Rollercoaster","Sail","Science","Ship","Space","Spacebase","Spaceflight","Squadron","Star","Sub","Submarine","Subway","Surgeon","Tank","Town","Traffic","Train","Transit","Tribe","Universe","Vampire","Vehicle","Village","War","Weather","Werewolf","Wildlife","Wing","World","Zombie","Zoo"];
			names2 = ["Aces","Adventure","Alliance","Assassin","Battle","Builder","Captain","Challenge","Challenger","Champion","Chronicles","Collection","Combat","Command","Commander","Company","Conflict","Control","Corp","Creator","Days","Defender","Deluxe","Design","Designer","Driver","Dynasty","Edge","Elite","Engineer","Expedition","Express","Fighter","Force","Horizon","Initiative","Kingdom","Legacy","Legend","Machines","Manager","Mania","Memories","Mercenary","Operation","Pilot","Playground","Program","Project","Race","Realm","Renegade","Rescue","Revelation","School","Service","Sim","Simulator","Tales","Tycoon","Typhoon","Universe","Unlimited","Venture","War","World"];
			names3 = ["Airplanes","Aliens","Androids","Assassins","Beasts","Clans","Creatures","Disasters","Diseases","Doctors","Dragons","Droids","Empires","Engineers","Gods","Helicopters","Hunters","Kingdoms","Knights","Magic","Mercenaries","Monsters","Mutants","Nations","Nature","Pilots","Planes","Realms","Robots","Sails","Science","Ships","Skeletons","Soldiers","Space","Spells","Stars","Tanks","Titans","Towns","Tribes","Vampires","Villages","Viruses","Warships","Weather","Werewolves","Wildlife","Wings","Zombies"];
			names4 = ["Adventures","Alliances","Assassins","Battles","Builders","Captains","Challengers","Challenges","Champions","Chronicles","Civilizations","Commanders","Companies","Conflicts","Constructions","Creators","Defenders","Designers","Discoveries","Drivers","Dynasties","Explorations","Flights","Formations","Guns","Kingdoms","Legacies","Legends","Machines","Madness","Managers","Memories","Mercenaries","Motions","Operations","Pilots","Programs","Projects","Races","Realms","Renegades","Revelations","Risks","Simulations","Tactics","Tales","Universes","Victory","Warriors","Worlds"];
			names5 = ["Aces","Adventures","Age","Art","Battles","Beasts","Builders","Castle","Champions","Chronicles","City","Clans","Company","Conflict","Contracts","Creation","Creators","Creatures","Crew","Dawn","Days","Defenders","Designers","Drivers","Empire","Engineers","Era","Family","Force","Fortress","Galaxy","Gods","Heroes","History","Kingdom","Kings","Legacy","Legend","Legends","Machines","Manager","Monsters","Motions","Operation","Pilots","Projects","Realm","Rise","Rulers","School","Tales","Titans","Towns","Tribes","Universe","Ventures","Village","World"];
			names6 = ["Alliances","Androids","Animals","Cargo","Cars","Chemicals","Cities","Co-Op","Colonies","Combat","Construction","Creation","Demolition","Destiny","Discovery","Droids","Emergency","Empires","Evolution","Farming","Farms","Fire","Flight","Food","Freedom","Glory","Guns","Honor","Iron","Knights","Mining","Minions","Mutation","Nations","Nature","Oceans","Planets","Power","Racing","Rails","Roads","Shadows","Skies","Space","Spaceflight","Stars","Steel","Tanks","Time","Timetravel","Transport","Vengeance","War","Wildlife","Worlds"];
			names7 = ["Agri","Air","Arcane","Arche","Astro","Battle","Bio","Bow","Build","Castle","City","Combat","Demo","Family","Farm","Fight","Flight","Food","Gun","Heli","Hero","Hunt","Iron","Jet","Knight","Life","Mage","Magic","Mecha","Mining","Mortal","Phantom","Plane","Police","Race","Rail","Robot","Shadow","Sky","Soul","Space","Spell","Star","Stealth","Storm","Tank","Trade","Train","Truck","War"];
			names8 = ["base","blade","block","bots","clad","command","corp","craft","fighter","force","front","gear","hero","life","light","line","lite","mania","master","path","plan","pro","raid","realm","rise","scape","sim","space","speed","state","strike","tech","ville","ways","works"];
			break;
		case("sports"):
			names1 = ["Angler","Bar Games","World Class","Baseball","Basket","Basketball","Beach","Biathlon","Big Game","Big Match","Bow","Bowling","Boxing","Bullrider","College Games","Cricket","Crossbow","Cycling","Dart","Decathlon","Deep Sea","Dirt Race","Dodgeball","Downhill","Extreme Sports","Fantasy Sports","Field","Fighting","Fishing","Football","Formula One","Freestyle","Freshwater","Golf","Grandslam","Gun","Gym","Gymnast","Handball","Heavyweight","Hockey","Horse Race","Hunting","Ice Hockey","Karate","Marathon","Martial Arts","Master League","Mountain Bike","Olympic","Open Ice","Outdoor","Pro Fighter","Racing","Rifle","Rock Climbing","Rodeo","Rugby","Safari","Ski","Skydive","Snooker","Snow Sports","Soccer","Sports","Street Racing","Strongest Man","Summer Sports","Tennis","Touchdown","Volleyball","Water Sports","Whitewater","Winter Sports","Wrestling"];
			names2 = ["Challenger","Champions","Championship","Coach","Deluxe","Evolution","Experience","Extreme","Games","Generation","Heroes","Icons","League","Legends","Manager","Master Challenge","Master Series","Masters","Meta Game","Online","Paradise","Pro","Pro Tournament","Professionals","Revolution","Simulator","Stars","Street Edition","Super Challenge","Super Stars","Titans","Top Shots","Tournament","Training Manager","Tycoons","Unleashed","Unlimited","World Championship","World Cup"];
			names3 = ["All-Stars","Heavyweights","Rising Stars","Amateurs","Athletes","Avengers","Challengers","Champions","Champs","Clubs","Coaches","Competitors","Crews","Failures","Heroes","Hunters","Jocks","Legends","Losers","Managers","Masters","Medalists","Mentors","Newcomers","Opponents","Participants","Players","Professionals","Pros","Rookies","Squads","Teams","Trainees","Trainers","Underdogs","Victors","Winners"];
			names4 = ["Adrenaline","Boot Camp","Challenges","Championships","Defeats","Face Offs","Fame","Front Pages","Games","Infamy","Leagues","Major Leagues","Management","Medals","Meta Games","Olympic Games","Playoffs","Power Plays","Premier League","Premierships","Prizes","Seasons","Signatures","Tournaments","Trainings","Trophies","Trophy Hunting","Victories","World Cups","World Tours"];
			names5 = ["Athletes","Challenges","Championships","Champs","Clubs","Coach","Crews","Day","Drive","Games","Generation","Gladiators","Heroes","Hunts","Kicks","Kings","Leagues","Legends","Lords","Managers","Masters","Medals","Plays","Pros","Rush","Season","Shots","Speed","Sports","Stars","Teams","Times","Tournaments","Trainers","Trophies","Uniforms","World","World Cup","World Tour"];
			names6 = ["Adrenaline","Archery","Baseball","Basket","Basketball","Big Game","Boot Camp","Boxing","Cricket","Cycling","Dirt Racing","Dodgeball","Extra Time","Extreme","Fight","Fighting","Fishing","Football","Formula One","Freestyle","Golf","Grand Slams","Guns","Handball","Hockey","Ice Hockey","Karate","Martial Arts","Perfection","Pro Fighting","Race","Rock Climbing","Rugby","Snow Sports","Soccer","Sport","Street Racing","Strength","Summer","Tennis","Touchdown","Volleyball","Water Sports","Whitewater","Winter","Winter Sports","World Class","Wrestling","the Field","the Gym","the Hunt"];
			names7 = ["Baseball","Basket","Basketball","Bat","Boxing","Cricket","Dodgeball","Field","Fight","Fighting","Football","Freestyle","Game","Golf","Handball","Hockey","Hunt","Hunting","Karate","Kick","Martial","Puck","Punch","Race","Racket","Riding","Rugby","Snow","Soccer","Speed","Sport","Street","Strength","Summer","Tennis","Volleyball","Water","Winter","Wrestling"];
			names8 = ["X","ace","art","champ","life","master","max","pro","pros","sim","slam","star","style","time","world"];
			break;
		case("strategy"):
			names1 = ["Air","Airborne","Alien","Ancient","Android","Angel","Arcane","Armored","Asteroid","Barbarian","Battlefield","Battlefront","Battleground","Blood","Border","Boundless","Brave","Cannon","Castle","Celtic","Champion","Chaos","City","Civil","Clan","Colonial","Covert","Creature","Crown","Crusader","Cultural","Dark","Demon","Destiny","Dragon","Dread","Drone","Dungeon","Elemental","Emergency","Empire","Enemy","Fantasy","Fire","Frontier","Frontline","Future","Galactic","Galaxy","Gladiator","Global","God","Grand","Guardian","Guild","Hacker","Hero","History","Honorbound","Immortal","Infinite","Iron","Kingdom","Knight","Liberty","Magic","Medieval","Metal","Midnight","Military","Monster","Mortal","Mutant","Mythic","Nation","Nature","Naval","Nightmare","Ninja","Nuclear","Ocean","Pirate","Planet","Revolution","Rune","Samurai","Sanguine","Settler","Silent","Solar","Space","Star","Syndicate","Titan","Toxic","Trade","Tribal","Undead","Vampire","Wonder"];
			names2 = ["Academy","Aftermath","Age","Alert","Allegiance","Alliances","Ambition","Apocalypse","Armageddon","Armies","Ascension","Assault","Awakening","Battalion","Brigade","Campaign","Cataclysm","Chronicles","Civilization","Combat","Command","Commander","Conflict","Conquest","Conspiracy","Counterstrike","Crisis","Defence","Defender","Destination","Destruction","Diplomacy","Discovery","Domination","Dominion","Dynasty","Earth","Empire","Enterprise","Evolution","Expansion","Exploration","Frenzy","Genesis","Glory","Heritage","Infestation","Intelligence","Invasion","Kingdoms","Laws","League","Legacy","Legends","Legion","Liberation","Masters","Mayhem","Mogul","Nation","Nemesis","Offensive","Operation","Outbreak","Outcasts","Overlord","Project","Prophecy","Realm","Redemption","Renaissance","Resistance","Resurrection","Retaliation","Revolution","Rising","Siege","Strategies","Strategy","Strike Force","Survival","Tactics","Termination","Tournament","Tribulation","Twilight","Tycoon","Union","Universe","Unrest","Uprising","Vendetta","Vengeance","Warcraft","Warfare","Warlords","Warriors","World","Wrath","Zone"];
			names3 = ["Act","Acts","Age","Creatures","Angels","Arena","Armies","Army","Art","Ascension","Awakening","Balance","Band","Beasts","Blood","Bombs","Bullets","Cannons","Champions","Chariots","Clans","Clash","Colonies","Company","Cost","Crown","Curse","Dawn","Defender","Demons","Dungeons","Elements","Empire","End","Faces","Fall","Fields","Fires","Flames","Force","Galaxy","Game","Gates","God","Gods","Guardians","Guns","Hearts","Heritage","Hero","Heroes","Hordes","King","Kingdom","Kingdoms","Kings","Knights","Land","Legacies","Legacy","Legends","Legions","Light","Lord","Lords","Machines","Magic","March","Master","Mastermind","Masters","Memories","Mercenaries","Monsters","Monuments","Planet","Price","Realm","Realms","Rise","Siege","Soldier","Songs","Space","Spells","Spirit","Spirits","Swords","Tales","Titans","Towers","Treasures","Tribes","Vampires","Virtues","Warlords","Werewolves","Whispers","World","Worlds"];
			names4 = ["Adventure","Agony","Anarchy","Annihilation","Ashes","Assault","Battle","Betrayal","Blood","Carnage","Chaos","Civilization","Combat","Conflict","Conquest","Control","Corruption","Courage","Danger","Death","Defeat","Destiny","Destruction","Disaster","Discipline","Domination","Dominion","Doom","Dust","Elysium","Embers","Empires","Eternity","Evil","Expansion","Faith","Fate","Fire","Flames","Fortune","Generations","Glory","Gore","Havoc","Hazard","Heaven","Honor","Infamy","Invasion","Iron","Law","Liberation","Liberty","Life","Light","Limbo","Magic","Malice","Mayhem","Might","Misery","Mutiny","Myths","Nowhere","Oblivion","Pain","Peace","Peril","Power","Prestige","Retaliation","Retribution","Ruins","Shadows","Siege","Souls","Spite","Steel","Strategy","Strife","Supremacy","Tactics","Terror","Thunder","Tomorrow","Tragedy","Treason","Turmoil","Twilight","Undoing","Valor","Vengeance","Victory","Violence","War","Warfare","Woe","Wonder","Wrath","Zion"];
			names5 = ["Ancestors","Ancients","Androids","Angels","Armies","Assassins","Barbarians","Bombs","Cannons","Castles","Champions","Chariots","Clans","Creatures","Crowns","Demons","Dragons","Dungeons","Empires","Ghosts","Giants","Gladiators","Gods","Guardians","Guilds","Heroes","Immortals","Kingdoms","Kings","Knights","Leaders","Legions","Lords","Machines","Magic","Masters","Mercenaries","Monsters","Mortals","Settlers","Soldiers","Spells","Spirits","Tibes","Titans","Traitors","Vampires","Villains","Warlords","Weapons","Werewolves"];
			names6 = ["Adventure","Alliances","Anarchy","Annihilation","Assault","Betrayal","Blood","Carnage","Chaos","Combat","Command","Conflict","Conquest","Control","Corruption","Courage","Death","Defeat","Destiny","Destruction","Domination","Fame","Flames","Fortune","Glory","Havoc","Honor","Infamy","Law","Liberation","Life","Malice","Mayhem","Might","Misery","Mutiny","Mystery","Pain","Peril","Power","Retaliation","Retribution","Strategy","Strife","Supremacy","Tactics","Terror","Tragedy","Treason","Turmoil","Valor","Vengeance","Victory","Violence","War","Warfare","Woe","Wonder","Wrath"];
			names7 = ["Air","Angel","Anti","Arche","Ash","Astro","Battle","Bio","Blade","Blood","Bullet","Castle","Clan","Combat","Cyber","Data","Dead","Demon","Dragon","Dread","Dream","Evo","Fight","Fleet","Front","Game","Gear","Grim","Gun","Heaven","Hell","Iron","Jet","Knight","Mage","Magic","Nether","Phantom","Shadow","Siege","Sky","Soul","Space","Spell","Star","Tank","Trade","Tribe","War","Witch"];
			names8 = ["age","base","blade","borne","bot","cast","clad","command","craft","crest","cry","fight","fire","flight","force","front","guard","guild","heart","hunt","kin","land","life","line","mania","master","mind","more","night","path","phase","plan","pro","rage","realm","reign","rise","rush","scape","side","slayer","space","speed","star","state","strike","tale","tide","watch","way"];
			break;
	}
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 2){
			rnd = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			names = names1[rnd] + " " + names2[rnd2];
		}else if(i < 4){
			rnd = Math.floor(Math.random() * names3.length);
			rnd2 = Math.floor(Math.random() * names4.length);
			names = names3[rnd] + " of " + names4[rnd2];
		}else if(i < 5){
			rnd = Math.floor(Math.random() * names5.length);
			rnd2 = Math.floor(Math.random() * names5.length);
			while(rnd2 === rnd){
				rnd2 = Math.floor(Math.random() * names5.length);
			}
			names = names5[rnd] + " and " + names5[rnd2];
		}else if(i < 6){
			rnd = Math.floor(Math.random() * names6.length);
			rnd2 = Math.floor(Math.random() * names6.length);
			while(rnd2 === rnd){
				rnd2 = Math.floor(Math.random() * names6.length);
			}
			names = names6[rnd] + " and " + names6[rnd2];
		}else{
			rnd = Math.floor(Math.random() * names7.length);
			rnd2 = Math.floor(Math.random() * names8.length);
			names = names7[rnd] + names8[rnd2];
		}
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}
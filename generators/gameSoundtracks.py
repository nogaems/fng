__all__ = ['gameSoundtracks']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names3', 'names1', 'names7'])
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
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', ((var.get('names3').get(var.get('rnd'))+Js(' of '))+var.get('names4').get(var.get('rnd2'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                        var.put('names', ((var.get('names5').get(var.get('rnd'))+Js(' '))+var.get('names6').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                        var.put('names', (((Js('The ')+var.get('names7').get(var.get('rnd')))+Js(' '))+var.get('names8').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Alien'), Js('Ambient'), Js('Angry'), Js('Animal'), Js('Animalistic'), Js('Autumn'), Js('Background'), Js('Battle'), Js('Beastly'), Js('Bird'), Js('Blessed'), Js('Bone'), Js('Boney'), Js('Boulder'), Js('Bronze'), Js('Burning'), Js('Calm'), Js('Canyon'), Js('Castle'), Js('Cave'), Js('Cavern'), Js('Chaos'), Js('Chaotic'), Js('Christmas'), Js('City'), Js('Corrupt'), Js('Corrupted'), Js('Crystal'), Js('Cursed'), Js('Dark'), Js('Desert'), Js('Diamond'), Js('Distant'), Js('Divine'), Js('Dragon'), Js('Dream'), Js('Dreamy'), Js('Dwarven'), Js('Dwarvish'), Js('Eastern'), Js('Elder'), Js('Electric'), Js('Elven'), Js('Elvish'), Js('Enchanted'), Js('Enemy'), Js('Evening'), Js('Evil'), Js('Fairy'), Js('Family'), Js('Fantasy'), Js('Final'), Js('Fire'), Js('Foreign'), Js('Forest'), Js('Frozen'), Js('Garden'), Js('Ghost'), Js('Giant'), Js('Glacial'), Js('Gnomish'), Js('Goblin'), Js('Golden'), Js('Graveyard'), Js('Heaven'), Js('Heavy'), Js('Hell'), Js('Hope'), Js('Island'), Js('Jungle'), Js('Knight'), Js('Lakeside'), Js('Light'), Js('Lighthouse'), Js('Lonely'), Js('Lonesome'), Js('Love'), Js('Lunar'), Js('Mage'), Js('Magical'), Js('Mammoth'), Js('Medieval'), Js('Midnight'), Js('Miracle'), Js('Monkey'), Js('Morning'), Js('Mountain'), Js('Mystery'), Js('Nightmare'), Js('Noble'), Js('Nomadic'), Js('Northern'), Js('Oasis'), Js('Ocean'), Js('Orbital'), Js('Orc'), Js('Orcish'), Js('Oriental'), Js('Party'), Js('Peace'), Js('Peasant'), Js('Phantom'), Js('Poisoned'), Js('Priest'), Js('Rain'), Js('River'), Js('Royal'), Js('Runic'), Js('Sea'), Js('Seasonal'), Js('Shadow'), Js('Silent'), Js('Silver'), Js('Skeletal'), Js('Snow'), Js('Solar'), Js('Soul'), Js('Southern'), Js('Space'), Js('Spirit'), Js('Spring'), Js('Storm'), Js('Stormy'), Js('Strange'), Js('Summer'), Js('Swamp'), Js('Talking'), Js('Temple'), Js('Thieving'), Js('Tiny'), Js('Tower'), Js('Town'), Js('Troll'), Js('Tunnel'), Js('Twilight'), Js('Undead'), Js('Underground'), Js('Underwater'), Js('Unknown'), Js('Village'), Js('Volcanic'), Js('Volcano'), Js('Voodoo'), Js('War'), Js('Warrior'), Js('Water'), Js('Waterfall'), Js('Wedding'), Js('Western'), Js('Wild'), Js('Winter'), Js('Zombie')]))
var.put('names2', Js([Js('Adventure'), Js('Ale'), Js('Arena'), Js('Armies'), Js('Arrival'), Js('Assault'), Js('Attack'), Js('Autumn'), Js('Battle'), Js('Beast'), Js('Bells'), Js('Blood'), Js('Bow'), Js('Breeze'), Js('Brew'), Js('Business'), Js('Camp'), Js('Cellar'), Js('Chamber'), Js('Champion'), Js('Circus'), Js('City'), Js('Code'), Js('Competition'), Js('Conquest'), Js('Contest'), Js('Control'), Js('Courage'), Js('Creation'), Js('Crown'), Js('Crypt'), Js('Dance'), Js('Danger'), Js('Dilemma'), Js('Dream'), Js('Drums'), Js('Dungeon'), Js('Dynasty'), Js('Escape'), Js('Essence'), Js('Factory'), Js('Faith'), Js('Fanfare'), Js('Feeling'), Js('Fever'), Js('Fight'), Js('Folk'), Js('Games'), Js('Gardens'), Js('Home'), Js('Horrors'), Js('Hunter'), Js('Illusion'), Js('Infiltration'), Js('Invader'), Js('Invasion'), Js('Island'), Js('Journey'), Js('Kingdom'), Js('Knight'), Js('Lair'), Js('Lament'), Js('Lands'), Js('Legend'), Js('Legion'), Js('Life'), Js('Logic'), Js('Lord'), Js('Lullaby'), Js('Madness'), Js('March'), Js('Market'), Js('Medley'), Js('Melody'), Js('Menace'), Js('Mind'), Js('Mine'), Js('Mirage'), Js('Mystery'), Js('Night'), Js('Order'), Js('Party'), Js('People'), Js('Peril'), Js('Power'), Js('Prison'), Js('Quest'), Js('Requiem'), Js('Rescue'), Js('Reunion'), Js('Road'), Js('Ruins'), Js('Rumble'), Js('Sage'), Js('Secret'), Js('Shield'), Js('Ship'), Js('Showdown'), Js('Smoke'), Js('Song'), Js('Spell'), Js('Spring'), Js('Story'), Js('Summer'), Js('Surprise'), Js('Sword'), Js('Tale'), Js('Talk'), Js('Theatre'), Js('Theme'), Js('Tomb'), Js('Tournament'), Js('Town'), Js('Trap'), Js('Tribe'), Js('Village'), Js('Vision'), Js('Voyage'), Js('Walk'), Js('War'), Js('Warning'), Js('Way'), Js('Whisper'), Js('Winter'), Js('Wisdom'), Js('Wonder')]))
var.put('names3', Js([Js('Adventure'), Js('Armies'), Js('Arrival'), Js('Assault'), Js('Attack'), Js('Bandit'), Js('Battle'), Js('Bells'), Js('Blight'), Js('Blood'), Js('Bow'), Js('Bravery'), Js('Call'), Js('Champion'), Js('Choice'), Js('City'), Js('Concern'), Js('Conquest'), Js('Contest'), Js('Courage'), Js('Crown'), Js('Curse'), Js('Dance'), Js('Danger'), Js('Death'), Js('Defender'), Js('Dilemma'), Js('Dread'), Js('Dream'), Js('Drums'), Js('Dungeon'), Js('Dynsasty'), Js('Empire'), Js('Enemy'), Js('Escape'), Js('Faith'), Js('Favor'), Js('Fear'), Js('Fight'), Js('Forest'), Js('Friend'), Js('Games'), Js('Gardens'), Js('Grace'), Js('Guardian'), Js('Hero'), Js('Heroism'), Js('History'), Js('Home'), Js('Hope'), Js('Horror'), Js('Invader'), Js('Invasion'), Js('Island'), Js('Journey'), Js('Kingdom'), Js('Lake'), Js('Lands'), Js('Legend'), Js('Legion'), Js('Life'), Js('Lullaby'), Js('Madness'), Js('March'), Js('Market'), Js('Melody'), Js('Memories'), Js('Memory'), Js('Menace'), Js('Miracle'), Js('Mountain'), Js('Mystery'), Js('Night'), Js('Nightmare'), Js('Ocean'), Js('Order'), Js('Power'), Js('Pride'), Js('Protector'), Js('Quest'), Js('Requiem'), Js('Rescue'), Js('Reunion'), Js('River'), Js('Road'), Js('Ruins'), Js('Sea'), Js('Secret'), Js('Secrets'), Js('Ship'), Js('Song'), Js('Souls'), Js('Spirit'), Js('Surprise'), Js('Swamp'), Js('Sword'), Js('Tale'), Js('Talk'), Js('Terror'), Js('Theme'), Js('Tomb'), Js('Town'), Js('Traitor'), Js('Trap'), Js('Valor'), Js('Village'), Js('Vision'), Js('Voyage'), Js('War'), Js('Warning'), Js('Way'), Js('Whisper'), Js('Wisdom'), Js('Wonders')]))
var.put('names4', Js([Js('Alliances'), Js('Ambition'), Js('Autumn'), Js('Battle'), Js('Beasts'), Js('Brutality'), Js('Chaos'), Js('Conflict'), Js('Culture'), Js('Darkness'), Js('Death'), Js('Desire'), Js('Destiny'), Js('Devotion'), Js('Empathy'), Js('Enchantments'), Js('Favor'), Js('Fortune'), Js('Greed'), Js('Harmony'), Js('Hatred'), Js('History'), Js('Hope'), Js('Hostility'), Js('Isolation'), Js('Joy'), Js('Lethargy'), Js('Life'), Js('Light'), Js('Loss'), Js('Love'), Js('Luck'), Js('Malice'), Js('Might'), Js('Misfortune'), Js('Modesty'), Js('Nature'), Js('Passion'), Js('Peace'), Js('Pity'), Js('Pleasure'), Js('Power'), Js('Prejudice'), Js('Prospect'), Js('Respect'), Js('Serenity'), Js('Silence'), Js('Solitude'), Js('Souls'), Js('Spells'), Js('Spring'), Js('Strife'), Js('Summer'), Js('Surrender'), Js('the Aliens'), Js('the Animals'), Js('the Barbaric'), Js('the Birds'), Js('the Champions'), Js('the Corrupt'), Js('the Cruel'), Js('the Cultured'), Js('the Day'), Js('the Depths'), Js('the Dwarves'), Js('the Elves'), Js('the Explorers'), Js('the Flawed'), Js('the Foreigners'), Js('the Forest'), Js('the Free'), Js('the Future'), Js('the Gnomes'), Js('the Goblins'), Js('the Hidden'), Js('the Holy'), Js('the Honest'), Js('the Innocent'), Js('the Just'), Js('the Kind'), Js('the Land'), Js('the Lost'), Js('the Merchants'), Js('the Moon'), Js('the Moral'), Js('the Mountain'), Js('the Night'), Js('the Ocean'), Js('the Orcs'), Js('the Past'), Js('the People'), Js('the Primitive'), Js('the Pure'), Js('the Righteous'), Js('the River'), Js('the Savage'), Js('the Sea'), Js('the Sick'), Js('the Sky'), Js('the Stars'), Js('the Strangers'), Js('the Strong'), Js('the Sun'), Js('the Tainted'), Js('the Tamed'), Js('the Truth'), Js('the Underground'), Js('the Unholy'), Js('the Untamed'), Js('the Void'), Js('the Weak'), Js('the Wild'), Js('the World'), Js('Tomorrow'), Js('Tragedy'), Js('Tranquility'), Js('Vigor'), Js('Violence'), Js('War'), Js('Winter'), Js('Yesterday')]))
var.put('names5', Js([Js("Adventure's"), Js("Alien's"), Js("Ancestor's"), Js("Angel's"), Js("Army's"), Js("Assassin's"), Js("Autumn's"), Js("Bandit's"), Js("Battle's"), Js("Cavalry's"), Js("Champion's"), Js("Chosen's"), Js("Commander's"), Js("Cook's"), Js("Corruption's"), Js("Courage's"), Js("Dark's"), Js("Death's"), Js("Demon's"), Js("Doom's"), Js("Dragon's"), Js("Dream's"), Js("Dwarf's"), Js("Elf's"), Js("Emperor's"), Js("End's"), Js("Evil's"), Js("Expedition's"), Js("Fallen's"), Js("Fanfare's"), Js("Fever's"), Js("Fight's"), Js("Fire's"), Js("Fortune's"), Js("Genie's"), Js("Ghost's"), Js("Giant's"), Js("Guardian's"), Js("Heaven's"), Js("Hell's"), Js("Hero's"), Js("Hope's"), Js("Kid's"), Js("King's"), Js("Knight's"), Js("Legend's"), Js("Life's"), Js("Light's"), Js("Love's"), Js("Market's"), Js("Mentor's"), Js("Merchant's"), Js("Meteor's"), Js("Minister's"), Js("Miracle's"), Js("Monster's"), Js("Moon's"), Js("Mythic's"), Js("Nature's"), Js("Night's"), Js("Nightmare's"), Js("Ogre's"), Js("Orc's"), Js("Parade's"), Js("Party's"), Js("Peace's"), Js("Pirate's"), Js("Player's"), Js("Prince's"), Js("Prophet's"), Js("Queen's"), Js("Rain's"), Js("Ranger's"), Js("Rogue's"), Js("Ruler's"), Js("Savior's"), Js("Shadow's"), Js("Ship's"), Js("Silence's"), Js("Slayer's"), Js("Snow's"), Js("Spirit's"), Js("Spring's"), Js("Stalker's"), Js("Storm's"), Js("Stranger's"), Js("Summer's"), Js("Sun's"), Js("Thunder's"), Js("Traitor's"), Js("Traveller's"), Js("Tribe's"), Js("Twilight's"), Js("Undead's"), Js("Unknown's"), Js("War's"), Js("Water's"), Js("Wind's"), Js("Winter's"), Js("Wizard's")]))
var.put('names6', Js([Js('Adapting'), Js('Advise'), Js('Alive'), Js('Ambition'), Js('Answer'), Js('Answering'), Js('Appearance'), Js('Appearing'), Js('Approach'), Js('Arrival'), Js('Attacking'), Js('Awakening'), Js('Back'), Js('Balance'), Js('Ballad'), Js('Beauty'), Js('Bite'), Js('Bleeding'), Js('Blemish'), Js('Blind'), Js('Bravery'), Js('Brilliance'), Js('Buzy'), Js('Ceremony'), Js('Challenge'), Js('Changing'), Js('Choice'), Js('Coming'), Js('Confused'), Js('Dance'), Js('Dangerous'), Js('Dead'), Js('Delight'), Js('Departure'), Js('Desire'), Js('Destroyed'), Js('Dirty'), Js('Elegance'), Js('Embrace'), Js('Escape'), Js('Excitement'), Js('Exciting'), Js('Exit'), Js('Fighting'), Js('Fire'), Js('Flaws'), Js('Force'), Js('Forsaken'), Js('Fortitude'), Js('Frenzy'), Js('Frozen'), Js('Glowing'), Js('Grandeur'), Js('Greeting'), Js('Guarding'), Js('Harmony'), Js('Haunted'), Js('Horrors'), Js('Humility'), Js('Humor'), Js('Hunted'), Js('Hunting'), Js('Idea'), Js('Injured'), Js('Invited'), Js('Knocking'), Js('Laughing'), Js('Leaving'), Js('Light'), Js('Love'), Js('Majesty'), Js('Mania'), Js('Might'), Js('Nature'), Js('Passion'), Js('Patience'), Js('Persistence'), Js('Pleased'), Js('Present'), Js('Prevented'), Js('Promise'), Js('Protected'), Js('Quest'), Js('Question'), Js('Rejected'), Js('Requiem'), Js('Resistance'), Js('Return'), Js('Returning'), Js('Revived'), Js('Riding'), Js('Ritual'), Js('Secured'), Js('Serenade'), Js('Serenity'), Js('Simplicity'), Js('Sleeping'), Js('Smiling'), Js('Song'), Js('Splendor'), Js('Style'), Js('Submission'), Js('Surprise'), Js('Talking'), Js('Tranquility'), Js('Transforming'), Js('Travelling'), Js('Trouble'), Js('Troubled'), Js('Tumbling'), Js('Upset'), Js('Watching'), Js('Weakness'), Js('Welcome'), Js('Worship'), Js('Yearning')]))
var.put('names7', Js([Js('Abandoned'), Js('Active'), Js('Admired'), Js('Adorable'), Js('Adored'), Js('Aged'), Js('Aggressive'), Js('Amazing'), Js('Amusing'), Js('Ancient'), Js('Angelic'), Js('Angry'), Js('Anguished'), Js('Aromatic'), Js('Awful'), Js('Awkward'), Js('Barren'), Js('Beautiful'), Js('Bewitched'), Js('Bitter'), Js('Bleak'), Js('Bright'), Js('Brilliant'), Js('Broken'), Js('Calm'), Js('Charming'), Js('Clean'), Js('Cloudy'), Js('Colorful'), Js('Colossal'), Js('Corrupted'), Js('Creepy'), Js('Cruel'), Js('Damaged'), Js('Dark'), Js('Dead'), Js('Dense'), Js('Dirty'), Js('Distant'), Js('Dramatic'), Js('Elegant'), Js('Enchanted'), Js('Evil'), Js('Exciting'), Js('False'), Js('Famous'), Js('Fancy'), Js('Faraway'), Js('Favorite'), Js('Fluffy'), Js('Forsaken'), Js('Frigid'), Js('Frozen'), Js('Funny'), Js('Gentle'), Js('Giant'), Js('Glorious'), Js('Gorgeous'), Js('Graceful'), Js('Grand'), Js('Grim'), Js('Harmless'), Js('Haunted'), Js('Heavenly'), Js('Hidden'), Js('Horrible'), Js('Humble'), Js('Hungry'), Js('Idle'), Js('Impossible'), Js('Infernal'), Js('Invisible'), Js('Little'), Js('Living'), Js('Lonely'), Js('Lost'), Js('Lucky'), Js('Majestic'), Js('Minor'), Js('Mysterious'), Js('Obvious'), Js('Ordinary'), Js('Original'), Js('Other'), Js('Perfect'), Js('Popular'), Js('Puny'), Js('Quiet'), Js('Rare'), Js('Royal'), Js('Safe'), Js('Second'), Js('Secret'), Js('Serene'), Js('Silent'), Js('Smooth'), Js('Strange'), Js('Tragic'), Js('Twin'), Js('Ultimate'), Js('Weird'), Js('Wild'), Js('Worthy')]))
var.put('names8', Js([Js('Adventure'), Js('Alien'), Js('Aliens'), Js('Ancestor'), Js('Animal'), Js('Answer'), Js('Autumn'), Js('Ballad'), Js('Beach'), Js('Beast'), Js('Bird'), Js('Camp'), Js('Canyon'), Js('Castle'), Js('Cliff'), Js('Commander'), Js('Community'), Js('Cook'), Js('Dance'), Js('Desert'), Js('Dungeon'), Js('Dwarf'), Js('Dwarves'), Js('Elf'), Js('Elves'), Js('Emperor'), Js('Expedition'), Js('Family'), Js('Farm'), Js('Feeling'), Js('Fields'), Js('Flower'), Js('Forest'), Js('Garden'), Js('Giant'), Js('Goblin'), Js('Goblins'), Js('Hamlet'), Js('Harbor'), Js('House'), Js('Hunt'), Js('Island'), Js('Journey'), Js('Jungle'), Js('Kid'), Js('King'), Js('Lake'), Js('Light'), Js('Lighthouse'), Js('Lullaby'), Js('Maestro'), Js('Maiden'), Js('Man'), Js('Master'), Js('Melody'), Js('Miracle'), Js('Mission'), Js('Mountain'), Js('Ocean'), Js('Orc'), Js('Orcs'), Js('Pastures'), Js('People'), Js('Person'), Js('Planes'), Js('Planet'), Js('Poem'), Js('Prince'), Js('Princess'), Js('Pursuit'), Js('Pygmy'), Js('Pyramid'), Js('Queen'), Js('Quest'), Js('Question'), Js('Reptile'), Js('River'), Js('Road'), Js('School'), Js('Sea'), Js('Secret'), Js('Serpent'), Js('Ship'), Js('Shrine'), Js('Song'), Js('Spider'), Js('Spirit'), Js('Spring'), Js('Spy'), Js('Storm'), Js('Summer'), Js('Swamp'), Js('Tavern'), Js('Temple'), Js('Territory'), Js('Tomb'), Js('Tower'), Js('Town'), Js('Tree'), Js('Tribute'), Js('Tune'), Js('Vault'), Js('Village'), Js('Volcano'), Js('Voyage'), Js('Waterfall'), Js('Whisper'), Js('Winter'), Js('Woman')]))
pass
pass


# Add lib to the module scope
gameSoundtracks = var.to_python()
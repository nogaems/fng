__all__ = ['writingConcepts']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A creative day with'), Js('Abandoned by'), Js('Abduction of'), Js('Accused by'), Js('Adopted by'), Js('Advice of'), Js('Alien life with'), Js('Alone in the world with'), Js('Arguements of'), Js('Attacked by'), Js('Audition of'), Js('Babysitting you'), Js('Barbecue party with'), Js('Being famous with'), Js('Being spontaneous with'), Js('Betrayal of'), Js('Birthday of'), Js('Blind date with'), Js('Boardgames with'), Js('Body switch with'), Js('Break up of'), Js('Breakfast with'), Js('Breaking the law with'), Js('Broken promise of'), Js('Campfire story of'), Js('Camping with'), Js('Car accident with'), Js('Celebrating a holiday with'), Js('Celebrating an anniversary with'), Js('Celebrating with'), Js('Changing history with'), Js('Changing lives with'), Js('Charity work with'), Js('Cheated by'), Js('Cleaning the house with'), Js('Climbing a mountain with'), Js('Climbing a volcano with'), Js('Climbing trees with'), Js('Clones of'), Js('Competing'), Js('Competition performance of'), Js('Complaints of'), Js('Cooking with'), Js('Corruption of'), Js('Cosmetic surgery of'), Js('Courage of'), Js('Culture of'), Js('Daily life of'), Js('Dancing with'), Js('Day at a convention with'), Js('Day at the beach with'), Js('Day at the park with'), Js('Day of work of'), Js('Day out with'), Js('Decision of'), Js('Disappearance of'), Js('Disappointment of'), Js('Discovering a new town with'), Js('Disease of'), Js('Double life of'), Js('Dream of'), Js('Dull evening with'), Js('Dungeon crawling with'), Js('Eating out with'), Js('Emberrassed by'), Js('End of the world with'), Js('Enemies of'), Js('Exploring ancient ruins with'), Js('Family of'), Js('Farm life with'), Js('Fears of'), Js('Fight to death with'), Js('Fighting for'), Js('First date with'), Js('Forgiven by'), Js('Forgiving'), Js('Friends of'), Js('Funny dinner with'), Js('Garage sale with'), Js('Ghost hunting with'), Js('Gift for'), Js('Gift from'), Js('Gifts from'), Js('Great day of'), Js('Guarding your house with'), Js('Habits of'), Js('Hatred of'), Js('Held hostage with'), Js('Helping others with'), Js('Helping out'), Js('History of'), Js('Hitch-hiking with'), Js('Holiday with'), Js('Homeless with'), Js('Honesty of'), Js('Hopes of'), Js('Horoscope of'), Js('Horror story of'), Js('Hurricane hunting with'), Js('Identical twin of'), Js('Imprisonment of'), Js('In heaven with'), Js('In hell with'), Js('In hospital with'), Js('Inside the mind of'), Js('Island life with'), Js('Jungle exploring with'), Js('Laughing with'), Js('Learning a new skill with'), Js('Leaving earth with'), Js('Lies of'), Js('Life with'), Js('Living on the moon with'), Js('Living the dream with'), Js('Living with'), Js('Locked in a zoo with'), Js('Locked up by'), Js('Locked up with'), Js('Long plane flight with'), Js('Long train ride with'), Js('Lost at night with'), Js('Lost at sea with'), Js('Lost in a rainforest with'), Js('Lost in the mountains with'), Js('Lost in the woods with'), Js('Lost in time with'), Js('Love of'), Js('Magic powers of'), Js('Making a movie with'), Js('Making dreams come true with'), Js('Making history with'), Js('Making three wishes with'), Js('Married to'), Js('Monster hunting with'), Js('Moving away with'), Js('Moving in with'), Js('Murder mystery with'), Js("New year's eve with"), Js('Nightmare of'), Js('On a cruise with'), Js('Party with'), Js('Performing with'), Js('Pillow fight with'), Js('Playing a TV show game with'), Js('Playing games with'), Js('Pool party with'), Js('Pranked by'), Js('Pranking'), Js('Prejudice against'), Js('Proud of'), Js('Raised by'), Js('Raising a pet with'), Js('Reality show with'), Js('Receiving 1 million from'), Js('Relaxing with'), Js('Remodelling your room with'), Js('Rescueing'), Js('Reunion of'), Js('Right choice of'), Js('Road trip with'), Js('Role model of'), Js('Ruling the world with'), Js('Running a marathon with'), Js('Saving the world with'), Js('Scuba diving with'), Js('Secret admirer of'), Js('Secret life of'), Js('Separation of'), Js('Shopping with'), Js('Sick day of'), Js('Sleepover with'), Js('Snowed in with'), Js('Space travel with'), Js('Spending 1 million on'), Js('Spending 1 million with'), Js('Spending a day with'), Js('Spending the summer with'), Js('Spending the winter with'), Js('Spending time in nature with'), Js('Staying up all night with'), Js('Sticking up for'), Js('Superpowers of'), Js('Surprise party for'), Js('Surviving a hurricane with'), Js('Surviving disaster with'), Js('Surviving the apocalypse with'), Js('Surviving war with'), Js('Taking care of'), Js('Terrible day of'), Js('Time travel with'), Js('Tournament with'), Js('Traditions of'), Js('Training animals with'), Js('Treasure hunting with'), Js('Virtual reality with'), Js('Wedding of'), Js('Weekend away with'), Js('Working with'), Js('World travel with'), Js('Wrong choice of')]))
var.put('nm2', Js([Js('a Disney character'), Js('a Muppet'), Js('a Roman'), Js('a Spartan'), Js('a band'), Js('a barbarian'), Js('a beggar'), Js('a blind person'), Js('a cat'), Js('a caveman/cavewoman'), Js('a celebrity'), Js('a centaur'), Js('a clown'), Js('a colleague'), Js('a comedian'), Js('a comic/manga/etc character'), Js('a cop'), Js('a coward'), Js('a cowboy'), Js('a crazy professor'), Js('a creepy stranger'), Js('a criminal'), Js('a cyborg'), Js('a deaf person'), Js('a demon'), Js('a dinosaur'), Js('a doctor'), Js('a dog'), Js('a dragon'), Js('a dream creature'), Js('a dwarf'), Js('a fairy'), Js('a famous musician'), Js('a fictional character'), Js('a fire fighter'), Js('a freak'), Js('a genie'), Js('a ghost'), Js('a giant'), Js('a gnome'), Js('a goblin'), Js('a god'), Js('a griffin'), Js('a hacker'), Js('a half-elf'), Js('a half-orc'), Js('a highly intelligent animal'), Js('a historic figure'), Js('a hitch-hiker'), Js('a hobo'), Js('a hologram'), Js('a horse'), Js('a hunter'), Js('a journalist'), Js('a king'), Js('a knight'), Js('a liar'), Js('a living snowman'), Js('a magician'), Js('a man'), Js('a martial art professional'), Js('a mechanic'), Js('a mermaid/mernan'), Js('a minotaur'), Js('a model'), Js('a monk'), Js('a monkey'), Js('a mutant'), Js('a mute person'), Js('a mysterious stranger'), Js('a mythical creature'), Js('a nightmare creature'), Js('a ninja'), Js('a nomad'), Js('a nurse'), Js('a paladin'), Js('a paramedic'), Js('a parrot'), Js('a pessimist'), Js('a phoenix'), Js('a pilot'), Js('a pirate'), Js('a pretentious snob'), Js('a professional thief'), Js('a psychic'), Js('a queen'), Js('a random student'), Js('a robot'), Js('a robot version of you'), Js('a rogue'), Js('a scientist'), Js('a sentient tree'), Js('a skeleton'), Js('a snake'), Js('a soldier'), Js('a spoiled person'), Js('a stranger'), Js('a super villain'), Js('a superhero'), Js('a survival expert'), Js('a telepath'), Js('a time traveller'), Js('a titan'), Js('a toddler'), Js('a traveller'), Js('a troll'), Js('a tv show character'), Js('a vampire'), Js('a very stubborn person'), Js('a viking'), Js('a waiter/waitress'), Js('a wannabe'), Js('a warlock'), Js('a werewolf'), Js('a wise old (wo)man'), Js('a witch'), Js('a wizard'), Js('a woman'), Js('a writer'), Js('a zombie'), Js('an Olympic athlete'), Js('an acrobat'), Js('an addict'), Js('an alien'), Js('an angel'), Js('an animal companion'), Js('an annoying person'), Js('an arsonist'), Js('an astronaut'), Js('an elephant'), Js('an elf'), Js('an enemy'), Js('an escaped convict'), Js('an evil fictional character'), Js('an evil historical figure'), Js('an ex'), Js('an expert'), Js('an idiot'), Js('an imaginary friend'), Js('an internet troll'), Js('an ogre'), Js('an old enemy'), Js('an online stranger'), Js('an optimist'), Js('an orc'), Js('an overly emotional person'), Js('cupid'), Js('enemies'), Js('fictional characters'), Js('five friends'), Js('five students'), Js('friends'), Js('historic figures'), Js('santa'), Js("someone who can't understand you"), Js('the abominable snowman'), Js('the boy scouts'), Js('the dentist'), Js('the ghost of somebody famous'), Js('the girl scouts'), Js('the grim reaper'), Js('the in-laws'), Js('the neighbors'), Js('the president'), Js('three friends'), Js('two friends'), Js('your (long lost) twin'), Js('your baby brother'), Js('your baby sister'), Js('your best friend'), Js('your best friends'), Js('your boss'), Js('your boyfriend'), Js('your child(ren)'), Js('your complete opposite'), Js('your cousin'), Js('your crush'), Js('your father'), Js('your father-in-law'), Js('your future self'), Js('your girlfriend'), Js('your grandfather'), Js('your grandmother'), Js('your grandparents'), Js('your husband'), Js('your mother'), Js('your mother-in-law'), Js('your older brother'), Js('your older sister'), Js('your parents'), Js('your past self'), Js('your pets'), Js('your secret admirer'), Js('your siblings'), Js('your soulmate'), Js('your teacher'), Js('your whole family'), Js('your wife'), Js('your worst enemy'), Js('yourself')]))
var.put('nm3', Js([Js('(Animal) companion in'), Js('Accusation in'), Js('Adventure of'), Js('Animal cruelty in'), Js('Animal life in'), Js('Apocalypse in'), Js('Ashes in'), Js('Assistant in'), Js('Audience in'), Js('Babysitting in'), Js('Bad advice in'), Js('Bad day in'), Js('Bag of money in'), Js('Beauty in'), Js('Best day in'), Js('Betrayal in'), Js('Birthday in'), Js('Blind date in'), Js('Blind in'), Js('Body swap in'), Js('Boss of'), Js('Bravery in'), Js('Break up in'), Js('Brief encounter in'), Js('Broken promise in'), Js('Bully of'), Js('Busted in'), Js('Camping in'), Js('Celebrity in'), Js('Ceremony in'), Js('Changes in'), Js('Chaos in'), Js('Childhood in'), Js('Children in'), Js('Chosen one in'), Js('Cleaning'), Js('Clones in'), Js('Colosseum of'), Js('Comfort of'), Js('Concert in'), Js('Contest in'), Js('Convention in'), Js('Costumed party in'), Js('Courage in'), Js('Creature of'), Js('Cruelty in'), Js('Cupid in'), Js('Day off in'), Js('Deaf in'), Js('Death in'), Js('Decisions in'), Js('Deserted in'), Js('Destruction of'), Js('Dinner in'), Js('Disappointment in'), Js('Discoveries in'), Js('Disease in'), Js('Dreams of'), Js('Drunk in'), Js('Eating in'), Js('Embarrasment in'), Js('Enemies in'), Js('Epic quest in'), Js('Escaped animal in'), Js('Eternal day in'), Js('Eternal night in'), Js('Failure in'), Js('False accusations in'), Js('Family in'), Js('Fantasies of'), Js('Fear of'), Js('Fight in'), Js('Fighting crime in'), Js('Fire in'), Js('First date in'), Js('First impressions in'), Js('First kiss in'), Js('First night in'), Js('Foes of'), Js('Followed to'), Js('Framed in'), Js('Freaks of'), Js('Freedom in'), Js('Fresh start in'), Js('Friendship in'), Js('Frustration in'), Js('Future of'), Js('Games in'), Js('Gang of'), Js('Ghosts of'), Js('Giant in'), Js('Greed in'), Js('Guardians of'), Js('Guilt in'), Js('Haunting in'), Js('Hermit in'), Js('Heroism in'), Js('Hiding in'), Js('Honesty in'), Js('Honor in'), Js('Horrible choice in'), Js('Humility in'), Js('Identical you in'), Js('Imposters in'), Js('Incident in'), Js('Incriminating photograph in'), Js('Infestation of'), Js('Insecurity in'), Js('Insomnia in'), Js('Invasion in'), Js('Inventions in'), Js('Invitation to'), Js('Job in'), Js('Justice in'), Js('Kindness in'), Js('Knife in'), Js('Language barrier in'), Js('Leader of'), Js('Life in'), Js('Long lost twin in'), Js('Lost in'), Js('Love in'), Js('Love note in'), Js('Loyalty in'), Js('Machines in'), Js('Madness in'), Js('Magic of'), Js('Marriage in'), Js('Midnight in'), Js('Misfits in'), Js('Misfortune in'), Js('Monsters of'), Js('Murder in'), Js('Music from'), Js('Mutation in'), Js('Mute in'), Js('Mysterious door in'), Js('Mysterious package in'), Js('New family in'), Js('New friend in'), Js('New identity in'), Js('New rules in'), Js('New technology in'), Js('Nightmare of'), Js('Noises from'), Js('Only hope in'), Js('Peace of mind in'), Js('Peer pressure'), Js('Personification of'), Js('Pollution of'), Js('Possession in'), Js('Power outages in'), Js('Prejudice in'), Js('Pride in'), Js('Promises in'), Js('Recipe for disaster in'), Js('Reenactment in'), Js('Respect in'), Js('Reunited in'), Js('Romance in'), Js('Romantic encounter in'), Js('Ruler of'), Js('Secret map of'), Js('Security in'), Js('Self-respect in'), Js('Shadows in'), Js('Signs of trouble in'), Js('Sinister stranger in'), Js('Sloth in'), Js('Special delivery in'), Js('Spirits of'), Js('Sports in'), Js('Storm in'), Js('Stranger in'), Js('Strangers of'), Js('Stray animal in'), Js('Super powers in'), Js('Super villain in'), Js('Superhero in'), Js('Surprise in'), Js('Telepathy in'), Js('Terror of'), Js('Three wishes in'), Js('Time travel in'), Js('Tour of'), Js('Tragedy in'), Js('Treasure hunting in'), Js('Treasure of'), Js('Trust in'), Js('Unpaid debts in'), Js('Vacation in'), Js('Vanity in'), Js('Vengeance in'), Js('Waking up in'), Js('War of'), Js('Weapon test in'), Js('Wish granted in'), Js('World record in'), Js('Wrong choice in'), Js('Zombies in')]))
var.put('nm4', Js([Js('a bank'), Js('a biodome'), Js('a bus stop'), Js('a cartoon universe'), Js('a chicken coop'), Js('a circus'), Js('a construction yard'), Js('a coral reef'), Js('a cornfield'), Js('a different continent'), Js('a different planet'), Js('a dry lake'), Js('a dystopian world'), Js('a fairy tale universe'), Js('a farmhouse'), Js('a fire station'), Js('a fjord'), Js('a forest clearing'), Js('a forgotten bunker'), Js("a friend's party"), Js('a future world'), Js('a glacier'), Js('a glacier cave'), Js('a historical setting'), Js('a hospital'), Js('a hotel'), Js('a junkyard'), Js('a laboratory'), Js('a lagoon'), Js('a lake'), Js('a luxury hotel'), Js('a meteor crater'), Js('a metro station'), Js('a mountain summit'), Js('a movie universe'), Js('a natural sanctuary'), Js('a police station'), Js('a power plant'), Js('a sanctuary'), Js('a sand castle'), Js('a sinkhole'), Js('a spa'), Js('a stable'), Js('a storm cellar'), Js('a strange tower'), Js('a strange town'), Js('a treehouse'), Js('a tv show'), Js('a utopian world'), Js('a video game universe'), Js('a volcanic island'), Js('a wasteland'), Js('a waterfall'), Js('an asylum'), Js('an empty field'), Js('an underground lair'), Js('an underground pit'), Js('an undiscovered cave system'), Js('an uninhabited island'), Js('another country'), Js('another dimension'), Js('autumn'), Js('castle'), Js("earth's orbit"), Js('forbidden ruins'), Js('heaven'), Js('hell'), Js('hot water springs'), Js('nursing home'), Js('paradise'), Js('paradise gardens'), Js('space'), Js('spring'), Js('summer'), Js('the abandoned building'), Js('the abandoned tunnel'), Js('the airport'), Js('the beach'), Js('the broken bridge'), Js('the capitol'), Js('the cinema'), Js('the city center'), Js('the clubhouse'), Js('the concert hall'), Js('the forest'), Js('the garden of Eden'), Js('the graveyard'), Js('the harbor'), Js('the kitchen'), Js('the library'), Js('the local market'), Js('the local restaurant'), Js('the local store'), Js('the local university'), Js('the mall'), Js('the mountains'), Js('the nearby village'), Js('the neighborhood'), Js('the online world'), Js('the park'), Js('the pet store'), Js('the playground'), Js('the prison'), Js('the river'), Js('the river bridge'), Js('the royal palace'), Js('the sacred grounds'), Js('the sea'), Js('the sport stadium'), Js('the streets'), Js('the swamp'), Js('the theater'), Js('the town hall'), Js('the toy store'), Js('the woods'), Js('the workplace'), Js('the zoo'), Js('winter'), Js('your dream house'), Js('your dreams'), Js('your garden'), Js('your house'), Js("your neighbor's house"), Js('your new house'), Js("your parents in law's house"), Js('your room'), Js('your school')]))
pass
pass


# Add lib to the module scope
writingConcepts = var.to_python()
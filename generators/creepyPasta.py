__all__ = ['creepyPasta']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Alaxesis'), Js('Alley Ally'), Js('Ash'), Js('Bear Chills'), Js('Bedtime Barry'), Js('Big Bad Bully'), Js('Bladesmith'), Js('Blissful Bessy'), Js('Carni Clown'), Js('Coach'), Js('Creative Mandy'), Js('Creepy Crawlies'), Js('Cruel Kevin'), Js('Curious George'), Js('Daddy'), Js('Dancing Devil'), Js('Dawn'), Js('Delivery Boy'), Js('Dispatch'), Js('Dollface'), Js('Dreamer'), Js('Elyse of Elysium'), Js('Eternal Jenny'), Js('FPS Pro'), Js('Fairy Tale Fiona'), Js('Fantasy Fiona'), Js('Flower Girl'), Js('Footsteps'), Js('Gallow Garry'), Js('Garry Gargoyle'), Js('Gash'), Js('Gazer'), Js('Goofy Garry'), Js('Grater'), Js('Graveyard Garry'), Js('Grimace'), Js('Guardian Angel'), Js('Guardian Demon'), Js('Hangman'), Js('Harry The Hoarder'), Js('Hollow Houdini'), Js('House Guest'), Js("Jack's Lantern"), Js('Joking Jenny'), Js('Long Lost Lover'), Js('Loopy Luna'), Js('Lucid Luna'), Js('Lucky Lucy'), Js('Lunch Lady'), Js('MMO Master'), Js('Mad Mandy'), Js("Mary's Sister"), Js('Mike The Magician'), Js('Mirror Image'), Js('Mirror Man'), Js('Miss Chitchat'), Js('Missing Misses'), Js('Moonlight Mandy'), Js('Mourning Widow'), Js('Mr. Mystery'), Js('Mr. Prick'), Js('Mr. Punchline'), Js('My Lady'), Js('My Sunshine'), Js('Newbie'), Js('Nibbler'), Js('Night Nurse'), Js('Night Stalker'), Js('Nightowl'), Js('OCD Andy'), Js('One Penny'), Js('Online Emily'), Js('Outsiders'), Js('Parry Perry'), Js('Phanton Phill'), Js('Pig Face'), Js('Pig Nose'), Js('Prancer'), Js('Quiet Boy'), Js('RPG Master'), Js('Ratface'), Js('Red Riding Hood'), Js('Salem'), Js('Salty Sally'), Js('Scaredy Cat'), Js('Scarlet'), Js('Scratches'), Js('Secret Santa'), Js('Seven Minute Alice'), Js('Skeleton Boy'), Js('Skinny Sally'), Js('Sleepy Sally'), Js('Smiles'), Js('Smokers'), Js('Snake Eyes'), Js('Sneezing Sam'), Js('Snow Demon'), Js('Solace'), Js('Stargazer'), Js('Stinky Stan'), Js('Stumper'), Js('Succubusy'), Js('Sweaty Sally'), Js('Terminal Tessa'), Js('The Adoptee'), Js('The Adrenaline Junkie'), Js('The Animator'), Js('The Attention Seeker'), Js('The Babysitter'), Js('The Bellboy'), Js('The Best Friends'), Js('The Bookworm'), Js('The Bride'), Js('The Butterfly'), Js('The Buzz Killer'), Js('The Candyman'), Js('The Caretaker'), Js('The Cheerleader'), Js('The Clicker'), Js('The Collectionist'), Js('The Crawler'), Js('The Crow'), Js('The Dentist'), Js('The Digital Friend'), Js('The Drama Queen'), Js('The Dreamer'), Js('The Familiar Stranger'), Js('The GM'), Js('The Genie'), Js('The Genius'), Js('The Gentle Prisoner'), Js('The Ghostbuster'), Js('The Gingerbread Man'), Js('The Glutton'), Js('The Good Dog'), Js('The Good Priest'), Js('The Gossip'), Js('The Grazer'), Js('The Happy Camper'), Js('The Hermit'), Js('The Hipster'), Js('The Huntress'), Js('The Hypnotist'), Js('The Insomniac'), Js('The Introvert'), Js('The Jester'), Js('The Larper'), Js('The Lurker'), Js('The New Kid'), Js('The Night Terror'), Js('The One Night Stand'), Js('The Orphan'), Js('The Other Twin'), Js('The Outcast'), Js('The Parasite'), Js('The Pastry Chef'), Js('The Photographer'), Js('The Pianist'), Js('The Pioneer'), Js('The Prankster'), Js('The Pregnant Lady'), Js('The Psychiatrist'), Js('The Puppet Master'), Js('The Quiet One'), Js('The Reaper'), Js('The Replacement'), Js('The Replica'), Js('The Returning Lover'), Js('The Salesman'), Js('The Sandman'), Js('The Scientist'), Js('The Scream Queen'), Js('The Sculpter'), Js('The Shadow'), Js('The Shadowless Man'), Js('The Sleeper'), Js('The Special One'), Js('The Stare'), Js('The Substitute'), Js('The Surgeon'), Js('The Survivalist'), Js('The Team Player'), Js('The Third Wheel'), Js('The Tooth Fairy'), Js('The Tourguide'), Js('The Visitor'), Js('The Volunteer'), Js('The Waitress'), Js('The Whisper'), Js('The White Knight'), Js('The Woodchucker'), Js('Tick Tack'), Js('Tinfoil Luna'), Js('Toothless'), Js('Trespassers'), Js('Tweety Bird'), Js('Twins'), Js('Vacation Vance'), Js('Volatile Vance'), Js('Weeping Wife'), Js('Wet Willy'), Js('Wicked Wendy'), Js('Window Licker'), Js('Wolf')]))
var.put('nm2', Js([Js('A Lifetime'), Js('A Small Sting'), Js('Alibi'), Js('All Are Welcome'), Js('Always Hungry'), Js('As The Bell Tolls'), Js('Ask For Directions'), Js('Autumn Falls'), Js('Bad Feeling'), Js('Bad Marriage'), Js("Barking Dogs Don't Bite"), Js('Bathing Time'), Js('Bedtime Story'), Js('Best Friends Forever'), Js('Blind Date'), Js('Born This Way'), Js('Candlelight Dinner'), Js('Change Is For The Better'), Js('Chase'), Js('Clear Your Mind'), Js('Coincidences'), Js('Come Back'), Js('Conscienceness'), Js('Control Alt Delete'), Js('Corrupted Memory'), Js('Counting The Days'), Js('Creaking Floors'), Js('Creature In My Mind'), Js('Curtain Falls'), Js('Dancing Flames'), Js('Daydreaming'), Js('Death Wish'), Js("Death's Warm Embrace"), Js('Death, O Death'), Js('Depths Of My Mind'), Js('Dinner For Two'), Js('Dreamland'), Js('Driving Insanity'), Js('Echoes'), Js("Emily's Fantasy"), Js('End Of The Bus'), Js('Entrepid Journey'), Js('Eternity'), Js('Everything Changes'), Js('Fairplay'), Js('Family Heirloom'), Js('Figments Of My Imagination'), Js('Fingers'), Js('Flirting With Death'), Js('Footsteps'), Js('For Whom The Bell Tolls'), Js('Freak Accident'), Js('Game Of The Year'), Js('Game Over'), Js('Gaming Friends'), Js('Get Freaky'), Js('Give A Man A Fish'), Js('Glamour And Fame'), Js('Going Underground'), Js('Gone In The Morning'), Js('Guarded By Demons'), Js('Hallowed'), Js('Handprints'), Js('Harvest Season'), Js('Hear No Evil'), Js('Heartbeat Rises'), Js('Heave Ho'), Js('Hidden Potential'), Js('Hide And Seek'), Js('History Repeats Itself'), Js('Honey Coated Words'), Js("I'm A Survivor"), Js("I'm An Artist"), Js('I.O.U.'), Js('Ice Cold Hands'), Js('Idle Hands'), Js('Ignorance Is Bliss'), Js('Illusions and Delusions'), Js('Imagine All The People'), Js('In The Corn Fields'), Js('Insomnia'), Js('Into The Dungeons'), Js('It Was My Pleasure'), Js("It's Just A Game"), Js('Just A Prank, Bro'), Js('Just Do It'), Js('Just Ignore Them'), Js('Keep A Secret'), Js('Keeping Watch'), Js('Knock Knock'), Js('Little Voice In My Head'), Js('Love Note'), Js('Lucid Dreams'), Js('Makeover'), Js('Making Headlines'), Js('Masquerade Ball'), Js('Me And My Imagination'), Js('Merry Christmas'), Js('Miracle Eyes'), Js("Money Can't Buy Happiness"), Js('Mountain Pass'), Js('Moving Homes'), Js('Murdery Mystery Dinner'), Js('My Angel'), Js('My Happy Place'), Js('My Legacy'), Js('My Tombstone'), Js('Mysterious Cold'), Js("Nature's Cruel"), Js('Neighbourhood Watchers'), Js('Nevermind My Love'), Js('Next In Line'), Js('Night At The Museum'), Js('Night Out'), Js('Nightmare, Just A Nightmare'), Js('Nightshift'), Js('No Answer'), Js('Not An Asylum'), Js('Not My Thoughts'), Js('OCD'), Js('Oblivion'), Js('Off The Grid'), Js('On Thin Ice'), Js('Oneway Ticket'), Js('Painfully Shy'), Js('Painkillers'), Js('Phobias'), Js('Pitch Black'), Js('Playing With Fire'), Js('Point Of No Return'), Js('Prank Calls'), Js('Presumed Dead'), Js('Price To Pay'), Js('Prison Lockdown'), Js('Pull My Finger'), Js('Quarantine'), Js('Quenching Thirst'), Js('Recipe For Disaster'), Js('Red Flags'), Js('Respawn'), Js('Retched Stench'), Js('Reunion'), Js('Rise And Shine'), Js('Safety In Numbers'), Js('Satisfaction'), Js('Saving Up'), Js('Say The Word'), Js("Scout's Honor"), Js('Screentime'), Js('Secret Admirer'), Js('Seductive Solitude'), Js('See You Tomorrow'), Js('Seeing My Psychiatrist'), Js('Seven Minutes In Hell'), Js('Shadow Plays'), Js('Silent Bells Are Ringing'), Js('Silver Lining'), Js('Skeletons In My Closet'), Js('Sleeping Pills'), Js('Sleeping Together'), Js('Sleepwalker'), Js('Smooth Skin'), Js('Something In The Shadows'), Js('Sorry, Wrong Number'), Js('Spared'), Js('Special Delivery'), Js('Splitting Headache'), Js('Stepping Out Of My Comfort Zone'), Js('Sticks And Stones'), Js('Summer Camp'), Js('Super Soldier'), Js('Sweet Embrace'), Js('Sweet Release'), Js("Tag, You're It"), Js('Teenage Experiments'), Js("That's Illogical"), Js('The Digital World'), Js('The Funeral'), Js('The Gifts Keep Coming'), Js('This Little Piggy'), Js('Three Two One'), Js('Touchdown'), Js('Track Of Time'), Js('Trick Up My Sleeve'), Js('Under My Blanket'), Js('Undercover'), Js('Unexpected Results'), Js('Victim Of Circumstance'), Js('Virtual Reality'), Js('Voice Of Reason'), Js('Waiting For You'), Js('Wasting Time'), Js('We Stick Together'), Js('Wedding Buffet'), Js('Weeping Willows'), Js('Wendighost'), Js('When The Devil Takes Hold'), Js('Who Am I?'), Js('Who Do You Voodoo'), Js('Wish Upon A Star'), Js('Written In The Stars'), Js('Wrong Turn')]))
pass
pass


# Add lib to the module scope
creepyPasta = var.to_python()
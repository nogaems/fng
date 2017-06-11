__all__ = ['curseWords']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+Js('!')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Oh doodle robots'), Js('Oh fish eyes'), Js('Shoodlepoppers'), Js('Jongle toys'), Js('Arrow to the knee'), Js('Bad gravy'), Js('Bag of potatoes'), Js('Balderdash'), Js('Bane of my blight'), Js('Barnacles'), Js('Bird brain'), Js('Birdbrained bandit'), Js('Blangdang'), Js('Blasted bandits'), Js('Blasted burrito'), Js('Blastfurnace'), Js('Blazing inferno'), Js('Blind mole'), Js('Blood and ashes'), Js('Blood and tears'), Js('Bloodsucking barnacle'), Js('Bloody bandages'), Js('Blunderbuss'), Js('Bootlicking barnacle'), Js('Boulderdash'), Js('Boulderhead'), Js('Bouncing balls'), Js('Branded idiot'), Js('Bread bandit'), Js('Broken scarecrow'), Js('Broken swords'), Js('Bullspit'), Js('Burned Bird Brain'), Js('Burned gravy'), Js('Burps and farts'), Js('Butt bushroom'), Js('Butterscotch'), Js("By Bozo's beard"), Js('Cabbagehead'), Js("Caesar's ghost"), Js('Candied nuts'), Js('Cheese and crackers'), Js('Cold brain'), Js('Cookie crumbles'), Js('Cookie dough'), Js('Cookoo bananas'), Js('Crab cakes'), Js('Crab muffin'), Js('Craven raven'), Js('Crazy caribou'), Js('Cream and crackers'), Js('Cripes'), Js('Curses'), Js('Dagnabbit'), Js('Dastardly dimwit'), Js('Deadbeat dingo'), Js('Deadbeat dodo'), Js('Death and taxes'), Js('Dingo dung'), Js('Dipstick'), Js('Dirt Nugget'), Js('Dirty socks'), Js('Disco dancing donkey'), Js('Dodge ram it'), Js('Doubleheaded nimwit'), Js('Duck herder'), Js('Dump truck'), Js('Dung beetle'), Js('Dust and ashes'), Js('Dust farmer'), Js('Dust on crackers'), Js('Eternal oblivion'), Js('Eyesore'), Js('Fairydust'), Js('Feeble pheasant'), Js('Fiddlesticks'), Js('Fire and brimstone'), Js('Flaming fire'), Js('Flaming hell'), Js('Flipping frogs'), Js('Frak'), Js('Freaking A'), Js('Frick'), Js('Friggers'), Js('Frinx'), Js('Friscuit'), Js('Frizzle frazzle'), Js('Frozen satan on a flying pig'), Js('Fudgemuffin'), Js('Fudgepuppies'), Js('Fun on a bun'), Js('Garbage'), Js('Garbage truck'), Js('Ghostbrain'), Js('Gobbledygook'), Js('Good gravy'), Js('Goof nugget'), Js('Boogers'), Js('Grave stalker'), Js('Grief magician'), Js('Grief wizard'), Js('Grime reaper'), Js('Gunk gecko'), Js('Hockey sticks'), Js('Hogwash'), Js('Holy carp'), Js('Holy cows of India'), Js('Holy wack a moly'), Js('Hopping hippos'), Js('Horse feathers'), Js('Horse hockey'), Js('Ignorant ogre'), Js('Ish'), Js('Jingle jangle'), Js('Jumping jacks'), Js('King of the void'), Js('Kitty whiskers'), Js('Loud noises'), Js('Mad mud mason'), Js('Marble brain'), Js('Eternal Anguish'), Js('Mashed potato'), Js("Merlin's beard"), Js('Mice droppings'), Js('Monkey disco'), Js('Monkey poop'), Js('Moronic maniac'), Js('Mosquito bite'), Js('Mother father'), Js('Mother of pearl'), Js('Muckdweller'), Js('Mud professor'), Js('Mudbrain'), Js('Mudscraper'), Js('Muttonhead'), Js('Noodle sticks'), Js('Nun on a bun'), Js('Oblivious ogre'), Js('Ogre booger'), Js('Oh coconuts'), Js('Oh crumbcake'), Js('Oh gargoyle'), Js('Oh mistletoe'), Js('Oh patches'), Js('Oh pickles'), Js('Paltry parasite'), Js('Parasite peasant'), Js('Party of pigs'), Js('Patchwork pigeon brain'), Js('Pea shoots'), Js('Pheasant peasant'), Js('Pickled onion'), Js('Pigeon peasant'), Js('Pigeon peon'), Js('Pile of pebbles'), Js('Poop giant'), Js('Puddlegoo'), Js('Rainbow chaser'), Js('Roaring tiger'), Js('Rotbrain'), Js('Rusting spoons'), Js('Sand cake baker'), Js('Sand crackers'), Js('Sand in a sandwich'), Js('Schnikes'), Js('Sewer pipe'), Js('Shallow swallow'), Js('Shoot a mile'), Js('Shriveling worm'), Js('Shut the front door'), Js('Slip and slide'), Js('Sludge fudger'), Js('Slug racer'), Js('Slushy icecream'), Js('Snitching sneazel'), Js('Son of a banshee'), Js('Son of a beaver'), Js('Son of a biscuit'), Js('Son of a gun'), Js('Son of a sea cook'), Js('Son of a troll'), Js('Soup fly'), Js('Spells and curses'), Js('Storm and thunder'), Js('Storm chaser'), Js('Stuff yourself'), Js('Sugarlumps'), Js('Sweet cheese'), Js('Sweet onions'), Js('Sweet silver sands'), Js('Swizzle sticks'), Js('Thunder and lightning'), Js('Toe fungus'), Js('Toe mushroom'), Js('Turd in a suit'), Js('Twaddle Taddle'), Js('Twisting nether'), Js('Vacant skull'), Js('Venomtongue'), Js('Weenie in a beanie'), Js('Whack a holy moly'), Js('What the jig'), Js('What the what now'), Js('Wind and water'), Js('Withered bird brain'), Js('Worm feeder'), Js('Worthless wormfood')]))
pass
pass


# Add lib to the module scope
curseWords = var.to_python()
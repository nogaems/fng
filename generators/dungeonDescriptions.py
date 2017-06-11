__all__ = ['dungeonDescriptions']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm19', 'nm1', 'nm11', 'rnd18', 'rnd15', 'rnd19', 'rnd11', 'rnd22', 'nm16', 'rnd8', 'name', 'rnd6a', 'nm3', 'rnd14', 'name3', 'rnd17', 'nm2', 'rnd2', 'br', 'name2', 'nm22', 'nm14', 'nm7', 'nm10', 'nm21', 'nm15', 'nm20', 'rnd21', 'rnd5', 'nm12', 'nm5', 'rnd4', 'rnd6b', 'rnd7', 'result', 'nm6', 'rnd6', 'rnd20', 'rnd13', 'nm4', 'rnd3', 'nm8', 'nm18', 'nm17', 'nm13', 'nm9', 'rnd10', 'rnd16', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('A grand'), Js('A large'), Js('A massive'), Js('A minor'), Js('A modest'), Js('A narrow'), Js('A short'), Js('A small'), Js('A tall'), Js('A wide')]))
    var.put('nm2', Js([Js('overgrown boulder'), Js('granite door'), Js('pair of granite doors'), Js('broken statue'), Js('worn statue'), Js('pair of worn statues'), Js('boulder'), Js('dark cave'), Js('murky cave'), Js('fallen tree'), Js('waterfall'), Js('crypt'), Js('broken temple'), Js('fallen temple'), Js('graveyard'), Js('fallen tower')]))
    var.put('nm3', Js([Js('bog'), Js('boulder field'), Js('cliff side'), Js('forest'), Js('grove'), Js('marsh'), Js('morass'), Js('mountain base'), Js('mountain range'), Js('mountain top'), Js('snowland'), Js('swamp'), Js('thicket'), Js('wasteland'), Js('woodlands'), Js('woods')]))
    var.put('nm4', Js([Js('large'), Js('small'), Js('massive'), Js('grand'), Js('modest'), Js('scanty'), Js('narrow')]))
    var.put('nm5', Js([Js('broken'), Js('clammy'), Js('crumbling'), Js('damp'), Js('dank'), Js('dark'), Js('deteriorated'), Js('dusty'), Js('filthy'), Js('foggy'), Js('grimy'), Js('humid'), Js('putrid'), Js('ragged'), Js('shady'), Js('timeworn'), Js('weary'), Js('worn')]))
    var.put('nm6', Js([Js('ash'), Js('bat droppings'), Js('broken pottery'), Js('broken stone'), Js('cobwebs'), Js('crawling insects'), Js('dead insects'), Js('dead vermin'), Js('dirt'), Js('large bones'), Js('moss'), Js('puddles of water'), Js('rat droppings'), Js('remains'), Js('roots'), Js('rubble'), Js('small bones')]))
    var.put('nm7', Js([Js('a broken statue part of a fountain'), Js('a broken tomb'), Js('a pillaged treasury'), Js('an altar'), Js('an overgrown underground garden'), Js('broken arrows, rusty swords and skeletal remains'), Js('broken cages and torture devices'), Js('broken mining equipment'), Js('broken vats and flasks'), Js('carved out openings filled with pottery'), Js('cases of explosives and mining equipment'), Js('drawings and symbols on the walls'), Js('empty chests and broken statues'), Js('empty shelves and broken pots'), Js('locked chests, vats, crates and pieces of broken wood'), Js('prison cells'), Js('remnants of a small camp'), Js('remnants of sacks, crates and caskets'), Js('remnants of statues'), Js("remnants of what once must've been a mess hall of sorts"), Js('remnants of what was once a decorated room with a now unknown purpose'), Js('rows of statues'), Js('rows of tombs and several statues'), Js('rows of vertical tombs'), Js('ruins of what seems to be a crude throne room'), Js('the remnants of a pillaged burial chamber'), Js('triggered traps and skeletal remains'), Js('warped and molten metal remnants'), Js('weapons racks and locked crates'), Js('what seems like some form of a sacrificial chamber')]))
    var.put('nm8', Js([Js('is a single path'), Js('are two paths, you take the right'), Js('are two paths, but the right is a dead end'), Js('are two paths, you take the left'), Js('are two paths, but the left is a dead end'), Js('are three paths, you take the right'), Js('are three paths, you take the left'), Js('are three paths, you take the middle')]))
    var.put('nm9', Js([Js('downwards'), Js('onwards'), Js('passed broken and pillaged tombs'), Js('passed collapsed rooms and pillaged treasuries'), Js('passed countless other pathways'), Js('passed countless rooms'), Js('passed long lost rooms and tombs'), Js('passed lost treasuries, unknown rooms and armories'), Js('passed pillaged rooms'), Js('passed several empty rooms')]))
    var.put('nm10', Js([Js('clammy'), Js('crumbled'), Js('damp'), Js('dank'), Js('dark'), Js('dusty'), Js('filthy'), Js('foggy'), Js('ghastly'), Js('ghostly'), Js('grimy'), Js('humid'), Js('putrid'), Js('ragged'), Js('shady'), Js('timeworn'), Js('weary'), Js('worn')]))
    var.put('nm11', Js([Js('An altar in the center is covered in runes, some of which are glowing'), Js('An enormous beastly skeleton is chained to the walls'), Js("Countless traps, swinging axes and other devices move all around. They're either still active, or just activated"), Js("It's filled with hanging cages which still hold skeletal remains"), Js("It's filled with strange glowing crystals and countless dead vermin"), Js("It's filled with tombs, but their owners are spread across the floor"), Js("It's filled with tombs, some of which no longer hold their owner"), Js("It's littered with skeletons, but no weaponry in sight"), Js("It's packed with boxes full of runes and magical equipment, as well as skeletons"), Js('Piles and piles of gold lie in the center, several skeletons lie next to it'), Js("Remnants of a makeshift barricade still 'guard' the group of skeletons behind it"), Js('Rows upon rows of shelves are packed with books or remnants of books. In the center sits a single skeleton'), Js('Several cages hold skeletal remains of various animals. Next to the cages are odd machines'), Js('Several stacks of gunpowder barrels are stacked against a wall. A skeleton holding a torch lies before it'), Js('Small holes and carved paths cover the walls, it looks like a community or burrow for small creatures'), Js('Spiderwebs cover everything, large figures seem to be wrapped in the same web'), Js('The floor is riddled with shredded blue prints and a half finished machine sits in a corner'), Js('The room is filled with lifelike statues of terrified people'), Js("There are several braziers scattered around, somehow they're still burning, or burning again"), Js('There\'s a demolished door with a sign that says "don\'t open"'), Js("There's a huge skeleton in the center, along with dozens of human skeletons"), Js("There's a pile of skeletons in the center, all burned and black"), Js("There's a round stone in the center, around it are a dozen skeletons in a circle"), Js("There's a seemingly endless hole in the center. Around it are what seem like runes"), Js("There's machinery all over the place, probably part of a workshop of sorts")]))
    var.put('nm12', Js([Js('advance carefully'), Js('carefully continue'), Js('cautiously proceed'), Js('continue'), Js('move'), Js('press'), Js('proceed'), Js('slowly march'), Js('slowly move'), Js('tread')]))
    var.put('nm13', Js([Js('darkness'), Js('depths'), Js('expanse'), Js('mysteries'), Js('secret passages'), Js('secrets'), Js('shadows')]))
    var.put('nm14', Js([Js('a few more passages'), Js('a few more rooms and passages'), Js('countless passages'), Js('dozens of similar rooms and passages'), Js('many different passages'), Js('many rooms and passages'), Js('various different rooms and countless passages'), Js('various passages')]))
    var.put('nm15', Js([Js('A big'), Js('A grand'), Js('A huge'), Js('A large'), Js('A massive'), Js('A mysterious'), Js('A tall'), Js('A thick'), Js('A vast'), Js('A wide'), Js('An enormous'), Js('An immense'), Js('An ominous')]))
    var.put('nm16', Js([Js('wooden'), Js('granite'), Js('metal')]))
    var.put('nm17', Js([Js('some are dead ends, others lead to who knows where, or what'), Js('some have collapsed, others are dead ends or too dangerous to try'), Js('most of which are far too ominous looking to try out'), Js('most of which have collapsed or were dead ends to begin with'), Js('some of them have collapsed, others seem to go on forever'), Js('some are dead ends, others seem to have no end at all'), Js('each leading to who knows where, or what'), Js('most of which probably lead to other depths of this dungeon'), Js('most of which look just like the other'), Js('they all look so similar, this whole place is a maze'), Js('each seem to go on forever, leading to who knows what'), Js('some look awfully familiar, others stranger everything else'), Js('each with their own twists, turns and destinations'), Js('most lead to nowhere or back to this same path'), Js("it's one big labyrinth of twists and turns")]))
    var.put('nm18', Js([Js('Ash and soot is'), Js('Countless odd symbols are'), Js('Countless runes are'), Js('Dire warning messages are'), Js('Dried blood splatters are'), Js('Intricate carvings are'), Js('Large claw marks are'), Js('Messages in strange languages are'), Js('Ominous symbols are'), Js('Strange writing is'), Js('Various odd symbols are')]))
    var.put('nm19', Js([Js('did something just move behind this door?'), Js("you're sure you saw a shadow under the cracks of the door."), Js('did the door just change its appearance?'), Js('what was that sound?'), Js("you're pretty sure you're being watched."), Js('was that a growl coming from behind the door?'), Js('did somebody just knock on the door?'), Js('you hear the faint sound of footsteps behind you.'), Js('is that a scratching sound coming from behind the door?'), Js('you think you can hear a whisper coming from behind the door.'), Js("light's coming through the gap below the door."), Js('you hear a loud bang in the distance from which you came.'), Js('you hear a faint laugh coming from behind the door.'), Js('suddenly the door slowly opens on its own.'), Js('something just grabbed your shoulder.')]))
    var.put('nm20', Js([Js('bleak'), Js('dark'), Js('dire'), Js('eerie'), Js('foggy'), Js('gloomy'), Js('grim'), Js('misty'), Js('murky'), Js('overcast'), Js('shadowy'), Js('shady'), Js('sinister'), Js('somber')]))
    var.put('nm21', Js([Js('aged'), Js('battered'), Js('busted'), Js('decayed'), Js('demolished'), Js('destroyed'), Js('deteriorated'), Js('forgotten'), Js('frayed'), Js('long lost'), Js('pillaged'), Js('tattered'), Js('wasted'), Js('weathered'), Js('worn'), Js('worn down')]))
    var.put('nm22', Js([Js('absorbed'), Js('butchered'), Js('claimed'), Js('consumed'), Js('defaced'), Js('desolated'), Js('devoured'), Js('dismantled'), Js('drained'), Js('eaten'), Js('maimed'), Js('mutilated'), Js('ravaged'), Js('ravished'), Js('spoiled'), Js('taken'), Js('wiped out'), Js('wrecked')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd6a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd6b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length')))))
    var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length')))))
    var.put('rnd20', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length')))))
    var.put('rnd21', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length')))))
    var.put('rnd22', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length')))))
    def PyJs_LONG_0_(var=var):
        return (((((((((((((var.get('nm1').get(var.get('rnd1'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' in a '))+var.get('nm20').get(var.get('rnd20')))+Js(' '))+var.get('nm3').get(var.get('rnd3')))+Js(' marks the entrance to this dungeon. Beyond the '))+var.get('nm2').get(var.get('rnd2')))+Js(' lies a '))+var.get('nm4').get(var.get('rnd4')))+Js(', '))+var.get('nm5').get(var.get('rnd5')))+Js(" room. It's covered in "))
    var.put('name', ((((((PyJs_LONG_0_()+var.get('nm6').get(var.get('rnd6')))+Js(', '))+var.get('nm6').get(var.get('rnd6a')))+Js(' and '))+var.get('nm6').get(var.get('rnd6b')))+Js('.')))
    var.put('name2', ((((((Js('Your torch allows you to see ')+var.get('nm7').get(var.get('rnd7')))+Js(', '))+var.get('nm21').get(var.get('rnd21')))+Js(' and '))+var.get('nm22').get(var.get('rnd22')))+Js(' by time itself.')))
    var.put('name3', ((((((((Js('Further ahead ')+var.get('nm8').get(var.get('rnd8')))+Js('. Its twisted trail leads '))+var.get('nm9').get(var.get('rnd9')))+Js(' and soon you enter a '))+var.get('nm10').get(var.get('rnd10')))+Js(' area. '))+var.get('nm11').get(var.get('rnd11')))+Js('. What happened in this place?')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(5.0)):
        try:
            pass
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
dungeonDescriptions = var.to_python()
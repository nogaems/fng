__all__ = ['castleDescriptions']

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
    var.registers(['nm19', 'nm1', 'nm11', 'rnd18', 'rnd15', 'rnd19', 'rnd11', 'nm16', 'rnd8', 'name', 'nm3', 'rnd14', 'name3', 'rnd17', 'nm2', 'rnd2', 'br', 'name2', 'nm14', 'nm7', 'nm10', 'name4', 'nm15', 'rnd5', 'nm12', 'nm5', 'rnd4', 'rnd7', 'result', 'nm6', 'rnd6', 'rnd13', 'nm4', 'rnd3', 'nm8', 'nm18', 'nm17', 'nm13', 'nm9', 'rnd10', 'rnd16', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('Four'), Js('Five'), Js('Six'), Js('Seven'), Js('Eight'), Js('Nine'), Js('Ten'), Js('Eleven'), Js('Twelve'), Js('Thirteen'), Js('Fourteen'), Js('Fifteen')]))
    var.put('nm2', Js([Js('broad'), Js('lean'), Js('massive'), Js('narrow'), Js('skinny'), Js('slim'), Js('solid'), Js('strong'), Js('thick'), Js('thin')]))
    var.put('nm3', Js([Js('round'), Js('square')]))
    var.put('nm4', Js([Js("piercing the sky are the first you'll see of this castle"), Js('dominate the sky line of this massive castle'), Js('dwarf everything below them'), Js('reach twice the height of the next tallest building in this elegant castle'), Js('surround the castle, they reach twice the height of the walls'), Js('form a protective wall on two sides of the castle'), Js('are low, but set firm and strong for a great defensive line'), Js('guard the weakest points of this castle'), Js('form a protective barrier all around the castle'), Js('have been build on various tactical spots for an ideal defense'), Js('are scattered in a seemingly random pattern, but have been build for an ideal defense'), Js('form an almost perfectly squared barrier around this marvelous castle'), Js('surround the castle in almost a perfect circle around this incredible castle'), Js('are both a defensive and decorational aspect of this elegant castle'), Js("tower above all, they're linked with small bridges")]))
    var.put('nm5', Js([Js('big'), Js('enormous'), Js('fairly low'), Js('fortified'), Js('giant'), Js('high'), Js('huge'), Js('large'), Js('lower'), Js('reinforced'), Js('strengthened'), Js('tall'), Js('towering')]))
    var.put('nm6', Js([Js('thick'), Js('massive'), Js('chunky'), Js('heavy'), Js('solid'), Js('firm'), Js('thin'), Js('narrow'), Js('wide'), Js('vast')]))
    var.put('nm7', Js([Js('basalt'), Js('black stone'), Js('blue stone'), Js('bronze stone'), Js('brown stone'), Js('dark brown stone'), Js('dark green stone'), Js('dark grey stone'), Js('dark red stone'), Js('golden stone'), Js('granite'), Js('green stone'), Js('grey stone'), Js('light brown stone'), Js('light green stone'), Js('light grey stone'), Js('light pink stone'), Js('light red stone'), Js('obsidian'), Js('red stone'), Js('sandstone'), Js('silver stone'), Js('white marble'), Js('white stone'), Js('yellow stone')]))
    var.put('nm8', Js([Js('Small'), Js('Tall'), Js('Wide'), Js('Tall, wide'), Js('Stylish'), Js('Refined'), Js('Elegant'), Js('Simple'), Js('Grand'), Js('Ornate'), Js('Crude'), Js('Dull'), Js('Rough')]))
    var.put('nm9', Js([Js('generously across the walls in a seemingly random pattern'), Js('generously across the walls in an asymmetric pattern'), Js('generously around the walls in fairly symmetrical patterns'), Js('generously around the walls in seeminly perfect symmetry'), Js('thinly across the walls in a seemingly random pattern'), Js('thinly across the walls in an asymmetric pattern'), Js('thinly around the walls in fairly symmetrical patterns'), Js('thinly around the walls in seeminly perfect symmetry'), Js('here and there across the walls in a seemingly random pattern'), Js('here and there across the walls in an asymmetric pattern'), Js('here and there around the walls in fairly symmetrical patterns'), Js('here and there around the walls in seeminly perfect symmetry')]))
    var.put('nm10', Js([Js('holes of various sizes'), Js('symmetric holes'), Js('same-sized holes'), Js('small holes'), Js('symmetric crenelations'), Js('asymmetric crenelations'), Js('overhanging crenelations'), Js('huge crenelations')]))
    var.put('nm11', Js([Js('sizable'), Js('huge'), Js('moderate'), Js('regular'), Js('great'), Js('vast')]))
    var.put('nm12', Js([Js('broad'), Js('colossal'), Js('enormous'), Js('giant'), Js('great'), Js('heavy'), Js('hefty'), Js('huge'), Js('large'), Js('massive'), Js('tall'), Js('thick'), Js('wide')]))
    var.put('nm13', Js([Js('metal'), Js('wooden')]))
    var.put('nm14', Js([Js(', a draw bridge'), Js(', a regular bridge'), Js('')]))
    var.put('nm15', Js([Js('hot oil pots'), Js('archer holes'), Js('a moat'), Js('strong defenses'), Js('large crenelations'), Js('various artillery equipment')]))
    var.put('nm16', Js([Js('guards the only easy way across the river'), Js('protects those in need of aid in this rough mountain pass'), Js('guards the last stronghold along this rough shoreline'), Js('offers a safe home to all those in need in these cold mountains'), Js('gives a safe place to rest in this forest stronghold'), Js('offers a warm haven within these cold, isolated lands'), Js('guards the only place with water within these hot, dry lands'), Js('guards the only passage into the castle build upon a mountain top'), Js('guards the only entrance to the castle build at the edges of a shoreline'), Js('protects those in need from the treacherous lands outside'), Js('guards the inhabitants of this island castle'), Js('guards a tranquil city within this extinguished volcano')]))
    var.put('nm17', Js([Js("and it's the only way in, at least to those unfamiliar with the castle and its surroundings"), Js(" and it's the only easy way in, any other side would be futile"), Js(", but it's not the only way in, which fortunately only very few know"), Js(", but it's not the only way in, but it'll be your best shot if you wish to conquer this castle"), Js(" and it's the only way in, at least without taking down the castle walls"), Js(" and it's the only way in, if you can make it that is"), Js(", but it's not the only way in when you know the castle's secret passages"), Js(" and it's the only easy way in, but easy is very relative here")]))
    var.put('nm18', Js([Js('Huge statues of heroes and kings decorate the bridge outside, memories of glories of the past'), Js('Statues of kings are lined up outside of the castle gates, serving as reminders of the past'), Js('Remnants of broken siege engines, swords and shields litter the fields outside, a painful reminder of a past war'), Js('Well kept gardens with fragrant flowers, gorgeous trees and many bushes decorate the outside of the castle'), Js('Carts, boxes, tents and various trade goods are stacked and packed outside the castle, ready to be sold'), Js('Huge dragon bones litter the fields outside the castle, half overgrown, but still a painful reminder of the past'), Js('Fields of nothingness stretch out outside the castle, allowing to see people coming far before they pose a threat'), Js('Small buildings, houses and other structures populate the grounds outside the castle walls, homes for the poorest of the poor'), Js('Large boulders litter the fields outside the castle, paths to and from the castle snake around them and farm plots are small and scattered all around'), Js("Plain fields of a type of grass cover most of the fields outside of the castle, adding to the castle's aesthetics"), Js('A handful of waterfalls flow into various small rivers and provide the precious farm fields outside the castle with needed water'), Js('Trees grow close to the castle gates and provide it with valuable wood for all sorts of purposes'), Js('Lush fields of crops surround the castle walls and provides the inhabitants with food all year round'), Js('The forest outside of the castle gates is light up with bioluminescent creatues, adding to the atmosphere of the castle'), Js('Various large houses are scattered outside the castle gates, surprisingly the rich are comfortable with living outside the gates as well')]))
    var.put('nm19', Js([Js('has clearly stood the test of time and its inhabitants are intend on making sure it stays that way for ages to come'), Js('has stood the test of time, it stood it well, but cracks begin to show here and there'), Js('has clearly stood the test of time, the rocks of the walls are aged and vines and plants grow inside the cracks, but this castle will last for ages to come'), Js("is relatively new, but so far it stood its ground with ease and it'll likely do so for ages to come"), Js("has clearly been around for at least a thousand years, but it doesn't seem like it will collapse any time soon"), Js("looks very new, but without knowing its history it's impossible to tell if it's a newly build castle or a well kept one"), Js('shows signs of decay after being around for ages, but its inhabitants are determined to repair any weaknesses to make sure this castle will be around for ages to come'), Js('shows signs of expansion as some parts are clearly build more recently than others, the inhabitants are already working on another part and hope to keep expanding'), Js('has been improved and improved over the ages, some parts of the castle are clearly newer than others, the inhabitants are determined to keep their castle as modern as possible'), Js('has stood the test of time and despite knowing some very rough times, the castle still stands and it looks like it will do so for many years to come')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
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
    var.put('name', (((((((((((((var.get('nm1').get(var.get('rnd1'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(', '))+var.get('nm3').get(var.get('rnd3')))+Js(' towers '))+var.get('nm4').get(var.get('rnd4')))+Js(' and are connected by '))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('nm6').get(var.get('rnd6')))+Js(' walls made of '))+var.get('nm7').get(var.get('rnd7')))+Js('.')))
    var.put('name2', (((((var.get('nm8').get(var.get('rnd8'))+Js(' windows are scattered '))+var.get('nm9').get(var.get('rnd9')))+Js(', along with '))+var.get('nm10').get(var.get('rnd10')))+Js(' for archers and artillery.')))
    var.put('name3', (((((((((((((Js('A ')+var.get('nm11').get(var.get('rnd11')))+Js(' gate with '))+var.get('nm12').get(var.get('rnd12')))+Js(' '))+var.get('nm13').get(var.get('rnd13')))+Js(' doors'))+var.get('nm14').get(var.get('rnd14')))+Js(' and '))+var.get('nm15').get(var.get('rnd15')))+Js(' '))+var.get('nm16').get(var.get('rnd16')))+var.get('nm17').get(var.get('rnd17')))+Js('.')))
    var.put('name4', (((var.get('nm18').get(var.get('rnd18'))+Js('. This castle '))+var.get('nm19').get(var.get('rnd19')))+Js('.')))
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
castleDescriptions = var.to_python()
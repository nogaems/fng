__all__ = ['dragonDescriptions']

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
    var.registers(['nm19', 'nm1', 'nm11', 'nm24', 'nm29', 'rnd15', 'rnd11', 'rnd18', 'rnd19', 'nm16', 'rnd22', 'rnd8', 'rnd29', 'nm23', 'nm31', 'name', 'name7', 'nm3', 'rnd14', 'nm33', 'nm34', 'rnd17', 'rnd23', 'rnd26', 'name3', 'nm2', 'rnd2', 'name6', 'nm27', 'nm26', 'nm30', 'br', 'rnd32', 'name2', 'nm22', 'rnd22a', 'nm14', 'nm7', 'nm10', 'nm21', 'nm25', 'name4', 'rnd28', 'nm15', 'nm20', 'rnd21', 'rnd5', 'nm12', 'nm32', 'nm5', 'rnd7b', 'rnd7', 'rnd17a', 'rnd24', 'rnd31', 'rnd30', 'rnd33', 'name8', 'rnd4b', 'result', 'nm6', 'rnd6', 'rnd4a', 'rnd20', 'rnd13', 'nm4', 'rnd3', 'nm8', 'nm28', 'nm18', 'name5', 'nm17', 'nm13', 'rnd27', 'nm9', 'rnd10', 'rnd16', 'rnd25', 'rnd34', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('Angry'), Js('Bright'), Js('Calm'), Js('Dark'), Js('Enormous'), Js('Fierce'), Js('Gentle'), Js('Large'), Js('Narrow'), Js('Piercing'), Js('Restless'), Js('Savage'), Js('Small'), Js('Tranquil'), Js('Wide')]))
    var.put('nm2', Js([Js('amber'), Js('azure'), Js('blazing'), Js('cerulean'), Js('cobalt'), Js('crimson'), Js('ebony'), Js('emerald'), Js('fiery'), Js('flaming'), Js('ivory'), Js('jade'), Js('obsidian'), Js('onyx'), Js('pearly'), Js('ruby'), Js('sapphire'), Js('scarlet'), Js('umber'), Js('viridian')]))
    var.put('nm3', Js([Js('deep'), Js('narrowly'), Js('buried'), Js('far'), Js('rooted'), Js('well'), Js('low'), Js('high'), Js('sunken'), Js('lightly'), Js('thightly'), Js('graciously'), Js('concealed'), Js('delicately'), Js('elegantly'), Js('gracefully'), Js('dreadfully'), Js('wickedly')]))
    var.put('nm4', Js([Js('angular'), Js('bony'), Js('hard'), Js('thorny'), Js('narrow'), Js('horned'), Js('long'), Js('scaled'), Js('rounded'), Js('soft')]))
    var.put('nm5', Js([Js('rather menacing'), Js('menacing'), Js('terrifying'), Js('fierce'), Js('frightening'), Js('very ominous'), Js('rather intimidating'), Js('vicious'), Js('threatening'), Js('savage'), Js('rather gentle'), Js('fairly mellow'), Js('mild'), Js('disciplined'), Js('rather peaceful'), Js('sympathetic'), Js('fairly kind'), Js('considerate'), Js('rather docile'), Js('merciful')]))
    var.put('nm6', Js([Js('Two enormous horns'), Js('Two small horns'), Js('Two horns'), Js('Several enormous horns'), Js('Several small horns'), Js('Several horns'), Js('One enormous central horn'), Js('One small central horn'), Js('One central horn'), Js('Several enormous central horns'), Js('Several small central horns'), Js('Several central horns'), Js('Several large tendrils'), Js('Several small tendrils'), Js('Several tendrils'), Js('Two crystal growths'), Js('Two enormous crystal growths'), Js('Two small crystal growths'), Js('Several crystal growths'), Js('Several enormous crystal growths'), Js('Several small crystal growths')]))
    var.put('nm7', Js([Js('small'), Js('large'), Js('enormous'), Js('tiny'), Js('narrow'), Js('wide'), Js('thick'), Js('thin'), Js('long'), Js('short')]))
    var.put('nm8', Js([Js('pointy'), Js('round'), Js('cat-like'), Js('dog-like'), Js('angular'), Js('curved'), Js('warped')]))
    var.put('nm9', Js([Js('A row of small horns'), Js('A row of small tendrils'), Js('A row of small crystal growths'), Js('A row of crystal growths'), Js('A row of horns'), Js('A row of tendrils'), Js('Several rows of small horns'), Js('Several rows of small tendrils'), Js('Several rows of small crystal growths'), Js('Several rows of crystal growths'), Js('Several rows of horns'), Js('Several rows of tendrils'), Js('Large fan-like skin and bone structures'), Js('Small fan-like skin and bone structures'), Js('Several large fan-like skin and bone structures'), Js('Several small fan-like skin and bone structures')]))
    var.put('nm10', Js([Js('pointy'), Js('round'), Js('wide'), Js('thick'), Js('thing'), Js('long'), Js('short'), Js('stubby'), Js('flat'), Js('large'), Js('small')]))
    var.put('nm11', Js([Js('rounded'), Js('curved'), Js('slitted'), Js('pointy'), Js('angular'), Js('warped'), Js('oval')]))
    var.put('nm12', Js([Js("there's a small horn"), Js("there's a small crystal growth"), Js("there's a small tendril"), Js('there are small horns'), Js('there are small crystal growths'), Js('there are small tendrils'), Js("there's a horn"), Js("there's a crystal growth"), Js("there's a tendril"), Js('there are horns'), Js('there are crystal growths'), Js('there are tendrils')]))
    var.put('nm13', Js([Js('A few sharp teeth'), Js('Rows of sharp teeth'), Js('Two huge teeth'), Js('Several huge teeth'), Js('Several sharp teeth'), Js('Several rows of sharp teeth'), Js('Rows of large teeth'), Js('A few large teeth'), Js('Several rows of large teeth'), Js('Four large teeth')]))
    var.put('nm14', Js([Js('reveal only a fraction of'), Js('give a slight hint at'), Js('show a glimpse of'), Js('give a preview of')]))
    var.put('nm15', Js([Js('short'), Js('thick'), Js('muscular'), Js('long'), Js('wide'), Js('huge'), Js('thin'), Js('broad'), Js('strong'), Js('lean')]))
    var.put('nm16', Js([Js('massive'), Js('huge'), Js('slim'), Js('slender'), Js('long'), Js('short'), Js('bulky'), Js('colossal'), Js('narrow'), Js('snake-like'), Js('muscular')]))
    var.put('nm17', Js([Js('massive scales'), Js('small scales'), Js('thick scales'), Js('narrow scales'), Js('wide scales'), Js('rounded scales'), Js('curved scales'), Js('warped scales'), Js('smooth skin'), Js('coarse skin'), Js('thick skin'), Js('radiant skin'), Js('crystal-like skin'), Js('reptilian skin'), Js('stone-like scales'), Js('scale-like skin')]))
    var.put('nm18', Js([Js('a row of spikes'), Js('rows of spikes'), Js('a row of thick armor plating'), Js('rows of thick armor plating'), Js('a row of small spikes'), Js('rows of small spikes'), Js('a row of armor plating'), Js('rows of armor plating'), Js('a row of crystal growths'), Js('rows of crystal growths'), Js('a row of fan-like growths'), Js('rows of fan-like growths'), Js('a row of small crystal growths'), Js('rows of small crystal growths'), Js('a row of small fan-like growths'), Js('rows of small fan-like growths'), Js('a row of tendrils'), Js('a row of small tendrils'), Js('rows of tendrils'), Js('rows of small tendrils'), Js('a crystal ridge'), Js('an armored ridge'), Js('a fan-like growth')]))
    var.put('nm19', Js([Js('much lighter'), Js('slightly lighter'), Js('lighter'), Js('darker'), Js('slightly darker'), Js('much darker'), Js('differently')]))
    var.put('nm20', Js([Js('Four'), Js('Six'), Js('Two'), Js('Four'), Js('Two'), Js('Four')]))
    var.put('nm21', Js([Js('huge'), Js('muscular'), Js('slim'), Js('slender'), Js('bulky'), Js('thick'), Js('long'), Js('massive'), Js('powerful'), Js('mighty')]))
    var.put('nm22', Js([Js('graceful'), Js('proud'), Js('tall'), Js('sturdy'), Js('elegantly'), Js('poised'), Js('noble'), Js('illustrious'), Js('dignified'), Js('imposing'), Js('intimidating'), Js('towering'), Js('mighty'), Js('elevated'), Js('arrogantly')]))
    var.put('nm23', Js([Js('3'), Js('4'), Js('5'), Js('6')]))
    var.put('nm24', Js([Js('sharp'), Js('thick'), Js('strong'), Js('long'), Js('narrow'), Js('massive'), Js('huge'), Js('pointy'), Js('barbed'), Js('keen'), Js('spiny'), Js('thorny')]))
    var.put('nm25', Js([Js('claws'), Js('talons'), Js('nails')]))
    var.put('nm26', Js([Js('bone'), Js('obsidian'), Js('onyx'), Js('crystal'), Js('stone')]))
    var.put('nm27', Js([Js('Enormous'), Js('Massive'), Js('Gigantic'), Js('Huge'), Js('Colossal'), Js('Monstrous'), Js('Giant'), Js('Humongous'), Js('Magnificent'), Js('Freakish'), Js('Terrifying'), Js('Horrendous'), Js('Graceful'), Js('Delicate'), Js('Slender')]))
    var.put('nm28', Js([Js('its shoulders'), Js('just below its shoulders'), Js('just above its shoulders'), Js('its shoulders')]))
    var.put('nm29', Js([Js('all the way down at its pelvis'), Js('at the middle of its back'), Js('at the lower end of its back'), Js('at the end of its shoulder blades'), Js('at its hips'), Js('just passed its shoulder blades')]))
    var.put('nm30', Js([Js('angular'), Js('rounded'), Js('curved'), Js('bat-like'), Js('somewhat triangular'), Js('scythe-shaped'), Js('bladed in structure'), Js('almost butterfly-like'), Js('almost angel-like'), Js('almost demonic')]))
    var.put('nm31', Js([Js('bone structures are clearly visible through the thin layer of skin'), Js("a specialized layer of skin is all that's visible inside"), Js('the inside is almost entirely see-through, especially when viewed from a distance'), Js('thick skin and eerie bone structures make up most of the wing'), Js('a specialized layer of seeminly color-changing skin makes up most of the wing'), Js('the edges of the skin inside the wings are tattered and damaged'), Js('the inner sides of the wing are full of minor holes'), Js('the insides of the wing seem to be made of thin crystals'), Js('the skin of the wings seems to glow as if made from fire itself')]))
    var.put('nm32', Js([Js('curved talons grow from each ending like giant scythes'), Js('sharp hooks grow from the endings of each bone'), Js('long tendril-like growths grow from many parts of the bottom sides of each wing'), Js("armor-like scales grow on top of the wing's primary bones"), Js('small, sharp tips grow from each ending like massive spears'), Js('each bone structures ends in a curved, yet blunt tip'), Js('sharp, spiky scales cover the top of each visible bone'), Js('jagged edges at the bottom almost give it a feathered look')]))
    var.put('nm33', Js([Js('long'), Js('massive'), Js('elegant'), Js('fairly short'), Js('graceful'), Js('barbed'), Js('spiky'), Js('simple'), Js('thick'), Js('narrow'), Js('wide'), Js('flat')]))
    var.put('nm34', Js([Js('sharp tip'), Js('curved talon'), Js('single tendril'), Js('seemingly fluffy tip'), Js('mace-like growth'), Js('sword-like edge'), Js('sharp, arrowhead shaped tip'), Js('gentle point'), Js('scythe-like blade'), Js('hammer-like growth'), Js('curled tip'), Js('fan-like tip')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd4b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    if (var.get('rnd4a')<Js(8.0)):
        while (var.get('rnd4b')>Js(7.0)):
            var.put('rnd4b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
            while PyJsStrictEq(var.get('rnd4a'),var.get('rnd4b')):
                var.put('rnd4b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    if ((var.get('rnd4a')<Js(5.0)) or (var.get('rnd4b')<Js(5.0))):
        while (var.get('rnd5')>Js(9.0)):
            var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd7b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
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
    var.put('rnd17a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    while PyJsStrictEq(var.get('rnd17'),var.get('rnd17a')):
        var.put('rnd17a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length')))))
    var.put('rnd20', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length')))))
    var.put('rnd21', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length')))))
    var.put('rnd22', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length')))))
    var.put('rnd22a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length')))))
    var.put('rnd23', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length')))))
    var.put('rnd24', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length')))))
    var.put('rnd25', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length')))))
    var.put('rnd26', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length')))))
    var.put('rnd27', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length')))))
    var.put('rnd28', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length')))))
    var.put('rnd29', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm29').get('length')))))
    var.put('rnd30', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm30').get('length')))))
    var.put('rnd31', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length')))))
    var.put('rnd32', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm32').get('length')))))
    var.put('rnd33', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm33').get('length')))))
    var.put('rnd34', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm34').get('length')))))
    var.put('name', (((((((((((var.get('nm1').get(var.get('rnd1'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' eyes sit '))+var.get('nm3').get(var.get('rnd3')))+Js(" within the creature's "))+var.get('nm4').get(var.get('rnd4a')))+Js(', '))+var.get('nm4').get(var.get('rnd4b')))+Js(' skull, which gives the creature a '))+var.get('nm5').get(var.get('rnd5')))+Js(' looking appearance.')))
    var.put('name2', (((((((var.get('nm6').get(var.get('rnd6'))+Js(' sit atop its head, just above its '))+var.get('nm7').get(var.get('rnd7')))+Js(', '))+var.get('nm8').get(var.get('rnd8')))+Js(' ears. '))+var.get('nm9').get(var.get('rnd9')))+Js(' runs down the sides of each of its jaw lines.')))
    def PyJs_LONG_0_(var=var):
        return ((((((((((((Js('Its nose is ')+var.get('nm10').get(var.get('rnd10')))+Js(' and has two '))+var.get('nm7').get(var.get('rnd7b')))+Js(', '))+var.get('nm11').get(var.get('rnd11')))+Js(' nostrils and '))+var.get('nm12').get(var.get('rnd12')))+Js(' on its chin. '))+var.get('nm13').get(var.get('rnd13')))+Js(' poke out from the side of its mouth and '))+var.get('nm14').get(var.get('rnd14')))+Js(' the terror hiding inside.'))
    var.put('name3', PyJs_LONG_0_())
    var.put('name4', ((((((((Js('A ')+var.get('nm15').get(var.get('rnd15')))+Js(' neck runs down from its head and into a '))+var.get('nm16').get(var.get('rnd16')))+Js(' body. The top is covered in '))+var.get('nm17').get(var.get('rnd17')))+Js(' and '))+var.get('nm18').get(var.get('rnd18')))+Js(' runs down its spine.')))
    var.put('name5', ((((Js('Its bottom is covered in ')+var.get('nm17').get(var.get('rnd17a')))+Js(' and is colored '))+var.get('nm19').get(var.get('rnd19')))+Js(' than the rest of its body. ')))
    def PyJs_LONG_1_(var=var):
        return ((((((((((((var.get('nm20').get(var.get('rnd20'))+Js(' '))+var.get('nm21').get(var.get('rnd21')))+Js(' limbs carry its body and allow the creature to stand '))+var.get('nm22').get(var.get('rnd22')))+Js(' and '))+var.get('nm22').get(var.get('rnd22a')))+Js('. Each limb has '))+var.get('nm23').get(var.get('rnd23')))+Js(' digits, each of which end in '))+var.get('nm24').get(var.get('rnd24')))+Js(' '))+var.get('nm25').get(var.get('rnd25')))
    var.put('name6', (((PyJs_LONG_1_()+Js(' seemingly made of '))+var.get('nm26').get(var.get('rnd26')))+Js('.')))
    var.put('name7', (((((((((((var.get('nm27').get(var.get('rnd27'))+Js(' wings grow starting from '))+var.get('nm28').get(var.get('rnd28')))+Js(' and end '))+var.get('nm29').get(var.get('rnd29')))+Js('. The wings are '))+var.get('nm30').get(var.get('rnd30')))+Js(', '))+var.get('nm31').get(var.get('rnd31')))+Js(' and '))+var.get('nm32').get(var.get('rnd32')))+Js('.')))
    var.put('name8', ((((((Js('Its ')+var.get('nm33').get(var.get('rnd33')))+Js(' tail ends in a '))+var.get('nm34').get(var.get('rnd34')))+Js(' and is covered in the same '))+var.get('nm17').get(var.get('rnd17')))+Js(' as its body.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(12.0)):
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
dragonDescriptions = var.to_python()
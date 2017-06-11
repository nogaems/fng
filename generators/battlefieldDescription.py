__all__ = ['battlefieldDescription']

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
    var.registers(['nm19', 'nm1', 'nm11', 'nm24', 'rnd15', 'rnd18', 'rnd11', 'rnd19', 'rnd22', 'nm16', 'rnd28a', 'rnd8', 'name', 'nm23', 'nm3', 'rnd23', 'rnd26', 'rnd27a', 'name3', 'nm2', 'nm27', 'nm26', 'rnd27b', 'br', 'name2', 'nm22', 'nm14', 'rnd3a', 'nm7', 'nm10', 'nm21', 'nm25', 'rnd2c', 'rnd3b', 'name4', 'nm15', 'nm20', 'rnd21', 'rnd5', 'nm12', 'nm5', 'rnd28c', 'rnd2a', 'rnd4', 'rnd27c', 'rnd7', 'rnd17a', 'rnd24', 'result', 'nm6', 'rnd2b', 'rnd6', 'rnd13', 'rnd28b', 'nm4', 'nm8', 'nm28', 'nm18', 'rnd17b', 'name5', 'nm17', 'nm13', 'nm9', 'rnd10', 'rnd25', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('field'), Js('forest'), Js('farm field'), Js('beach'), Js('village'), Js('town'), Js('city')]))
    var.put('nm2', Js([Js('bodies'), Js('blood'), Js('gore'), Js('suits'), Js('weapons'), Js('shells'), Js('carnage'), Js('wounded fighters'), Js('destruction')]))
    var.put('nm3', Js([Js('pink'), Js('silver'), Js('brown'), Js('blue'), Js('black'), Js('gray'), Js('khaki')]))
    var.put('nm4', Js([Js('peaceful, '), Js('quiet, '), Js('tranquil, '), Js('serene, '), Js('beautiful, '), Js('harmonious, '), Js('marvelous, '), Js('vast, '), Js('delicate, ')]))
    var.put('nm5', Js([Js('green'), Js('lush'), Js('snowy'), Js('tender'), Js('luscious'), Js('rich')]))
    var.put('nm6', Js([Js('ruthless battle'), Js('disastrous fight'), Js('long, destructive battle'), Js('devastating war'), Js('tragic civil war'), Js('full-blown invasion'), Js('large scale assault'), Js('terrible battle'), Js('bloody war'), Js('cruel war')]))
    var.put('nm7', Js([Js('be filled with the scent of food from a nearby town'), Js('be rich with scents from nearby breweries'), Js('carry the sounds of birds, rivers and wildlife'), Js('be soft and carry a gentle breeze'), Js('be rich in sound from a nearby town and a forest full of wildlife'), Js("be full of nature's sounds"), Js('be delicate and quiet'), Js("be fresh and smell of nature's wonders"), Js('carry the delicate scents of flowers and fruits'), Js("carry the sounds of a large waterfall, small rivers and nature's wildlife")]))
    var.put('nm8', Js([Js('thick with the scent of death and decay'), Js('heavy and thick with the scent of smoke'), Js('carrying a thick, black smoke and small embers'), Js('deafening loud, the sound of explosions drowns any other sound in the area'), Js('a hellish symphony of screams, explosions and gunfire'), Js('a barrage of sounds of explosions, war cries and the screams of the wounded'), Js('merely a canvas for the stench of death and the cries of the dying'), Js('thick with the stench of gunpowder, blood, gore and death'), Js('heavy with the screams of dying fighters and the scent of their blood'), Js('glowing red with fire and thick with smoke, ash and embers')]))
    var.put('nm9', Js([Js('enough to make even the bravest tremble in fear'), Js('something no survivor will ever forget'), Js('hell has descended upon this area'), Js('a sight of pure nightmares'), Js('the mere sense of it will make you want to run'), Js("there's no coming back from this"), Js('enough to destroy whatever courage is left in the survivors')]))
    var.put('nm10', Js([Js('Two armies'), Js('Two parties'), Js('Two trained armies'), Js('Two barely trained groups'), Js('An army and a rebellion'), Js('An army of rebels and an army of warriors')]))
    var.put('nm11', Js([Js('for supremacy'), Js('for resources'), Js('over a mere difference in lifestyle and belief'), Js('for independance'), Js('because of a betrayal'), Js('because of the lies of their leaders'), Js('without knowing the true reason'), Js('for control of the area'), Js('due to a difference in beliefs')]))
    var.put('nm12', Js([Js("it's clear who will win"), Js('the victor is obvious'), Js("it's becoming clear which side will win"), Js("at this point it's undeniable which side will win"), Js("it's starting to become clear which side will win"), Js("it's yet to be determined which side's on the winning hand"), Js("the battle is in nobody's favor yet"), Js("there's no hint of which side will win"), Js('with no side on the winning hand, this battle could go on for a long time'), Js('this battle has yet to find its winning side')]))
    var.put('nm13', Js([Js('dead'), Js('dead and wounded'), Js('wounded')]))
    var.put('nm14', Js(' the losing side '))
    var.put('nm15', Js([Js('lay in heaps across'), Js('are scattered across'), Js('are abundant and lay in heaps around'), Js('are spread around'), Js('lay in large groups across')]))
    var.put('nm16', Js(' grim '))
    var.put('nm17', Js([Js('despair'), Js('the certainty of death'), Js('anguish'), Js('gloom'), Js('pain'), Js('sorrow'), Js('horror'), Js('agony'), Js('strain'), Js('exhaustion'), Js('fatigue')]))
    var.put('nm18', Js([Js('yet they fight on'), Js('but they force themselves to fight nonetheless'), Js('but they refuse to give up'), Js('they want to give up, but somehow keep fighting'), Js('their spirit will be broken soon'), Js('they continue to fight, but their fight is a hopeless one'), Js('fighting is useless, but they will fight to the death')]))
    var.put('nm19', Js([Js('the rush of victory coursing through their bodies'), Js('victory ready for the taking'), Js('victory becoming more and more likely'), Js('a certainty of victory'), Js('the thought of victory in their minds')]))
    var.put('nm20', Js(' the winning side '))
    var.put('nm21', Js([Js('pushes harder and harder on their enemies'), Js('pushes on and on'), Js('fights even harder and with more tenacity'), Js('fights with a sense of relief knowing all will be over soon'), Js('has gained a morale boost and is fighting their enemies with more determination'), Js("fights as if they're invinsible"), Js('fights with new found strength')]))
    var.put('nm22', Js([Js('bloodlust'), Js('a frenzy'), Js('rage'), Js('panic'), Js('hysteria'), Js('terror'), Js('exhaustion'), Js('fatigue')]))
    var.put('nm23', Js([Js('frantically killing any enemy in sight'), Js('on a rampage against anybody standing in their way'), Js('killing any enemy they see in a fury of blood and gore'), Js('recklessly charging towards the enemy with only the aim to kill all'), Js('carelessly charging any enemy without a care for their own safety')]))
    var.put('nm24', Js([Js('just wish all this was over'), Js('can only think of home and what they left behind'), Js('fight on in the hopes to survive this terror'), Js('fight merely for the sake of survival'), Js('seem to be fairly unaffected by the terrors around them'), Js('fight by only focusing on their enemy and not the carnage around them'), Js('long for the end of this battle')]))
    var.put('nm25', Js([Js('heavy'), Js('enormous'), Js('unimaginable'), Js('tremendous'), Js('immense'), Js('disastrous'), Js('tragic'), Js('devastating')]))
    var.put('nm26', Js([Js('years'), Js('decades'), Js('ages'), Js('generations'), Js('a lifetime')]))
    var.put('nm27', Js([Js('explosion holes'), Js('broken siege engines'), Js('metal'), Js('bodies'), Js('weaponry'), Js('lost bombs'), Js('rubble'), Js('debris'), Js('blood'), Js('gore')]))
    var.put('nm28', Js([Js('trees'), Js('flowers'), Js('grass'), Js('bushes'), Js('shrubs'), Js('plants')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    if ((var.get('rnd1')>Js(1.0)) and (var.get('rnd1')<Js(4.0))):
        var.put('nm4', Js([Js('peaceful '), Js('quiet '), Js('tranquil '), Js('serene '), Js('beautiful '), Js('vast '), Js('stunning '), Js('tremendous ')]))
        var.put('nm5', Js([Js('')]))
    else:
        if ((var.get('rnd1')>Js(3.0)) and (var.get('rnd1')<Js(6.0))):
            var.put('nm4', Js([Js('peaceful, '), Js('quiet, '), Js('tranquil, '), Js('serene, '), Js('beautiful, '), Js('harmonious, '), Js('small, '), Js('reserved, ')]))
            var.put('nm5', Js([Js('harbor'), Js('fishing'), Js('small'), Js('trading'), Js('growing'), Js('farming'), Js('hard working'), Js('dynamic')]))
            var.put('nm7', Js([Js('be rich in scents of food, fresh fish and new brews'), Js('be rich in the scents and sounds of hard work'), Js('be filled with the scent of freshly baked bread and the sound of people'), Js('carry the sound of working people and large tools'), Js('be vibrant with the sound of work, trade and craftsmanship')]))
            var.put('nm28', Js([Js('homes'), Js('market stalls'), Js('schools'), Js('businesses'), Js('buildings'), Js('monuments'), Js('roads'), Js('gardens'), Js('parks')]))
        else:
            if PyJsStrictEq(var.get('rnd1'),Js(6.0)):
                var.put('nm4', Js([Js('busy '), Js('lively '), Js('bright '), Js('spirited '), Js('bustling '), Js('hectic ')]))
                var.put('nm5', Js([Js('')]))
                def PyJs_LONG_0_(var=var):
                    return var.put('nm7', Js([Js('be rich in scents of food, fresh fish and new brews'), Js('be rich in the scents and sounds of hard work'), Js('be filled with the scent of freshly baked bread and the sound of people'), Js('carry the sound of working people and large tools'), Js('be vibrant with the sound of work, trade and craftsmanship'), Js('be packed with a wide array of city sounds'), Js('be loud and bustling with sounds of the city')]))
                PyJs_LONG_0_()
                var.put('nm28', Js([Js('homes'), Js('market stalls'), Js('schools'), Js('businesses'), Js('buildings'), Js('monuments'), Js('roads'), Js('gardens'), Js('parks')]))
    var.put('rnd2a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd2b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    while PyJsStrictEq(var.get('rnd2b'),var.get('rnd2a')):
        var.put('rnd2b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd2c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    while (PyJsStrictEq(var.get('rnd2c'),var.get('rnd2a')) or PyJsStrictEq(var.get('rnd2c'),var.get('rnd2b'))):
        var.put('rnd2c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd3b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    while PyJsStrictEq(var.get('rnd3b'),var.get('rnd3a')):
        var.put('rnd3b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
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
    if (var.get('rnd12')>Js(4.0)):
        var.put('nm14', Js(' one side '))
        var.put('nm16', Js(' hopeful '))
        var.put('nm17', Js([Js('victory in mind'), Js('hope in their hearts'), Js('adrenaline rushing through their bodies'), Js('weapons clenched in their hands'), Js('gritting teeth'), Js('their muscles tense and anxious'), Js('boots stepping firmly'), Js('eyes searching their surroundings'), Js('nervous, yet steady breathing')]))
        var.put('nm18', Js([Js('they courageously fight on'), Js('they push harder and harder on the enemy'), Js('they fight their enemy in an equal battle'), Js('they take on their enemies'), Js('they carry out their orders in a tough fight')]))
        def PyJs_LONG_1_(var=var):
            return var.put('nm19', Js([Js('the uncertainty of battle coursing through their minds'), Js('a lack of confidence in a postive outcome'), Js("no way of knowing they're winning or losing"), Js('the chaos of battle concealing any sense of victory or defeat'), Js('both confidence and panic'), Js('a strong possibility of pain or death'), Js('the possibility of death shaking their knees'), Js("no way to know if they'll live or die")]))
        PyJs_LONG_1_()
        var.put('nm20', Js(' the other side '))
        def PyJs_LONG_2_(var=var):
            return var.put('nm21', Js([Js('fights like their lives depend on it, which they do'), Js('fights with fear flowing through their veins'), Js('battles their enemies head on in the hope to come out on top'), Js('does whatever it can in order to try to defeat their enemies'), Js('ferociously battles their enemies'), Js('desperately fights their enemies without knowing which side is stronger'), Js('courageously fights their enemies with the hope of being the stronger side')]))
        PyJs_LONG_2_()
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length')))))
    var.put('rnd17a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd17b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    while PyJsStrictEq(var.get('rnd17b'),var.get('rnd17a')):
        var.put('rnd17b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length')))))
    var.put('rnd21', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length')))))
    var.put('rnd22', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length')))))
    if ((var.get('rnd22')>Js(2.0)) and (var.get('rnd22')<Js(6.0))):
        var.put('nm23', Js([Js('barely able to force their bodies in motion'), Js('bursting out in tears and screams'), Js('mumbling things about home and family'), Js('hiding or running away from the fight'), Js('no longer capable of moving, let alone defending themselves')]))
    else:
        if (var.get('rnd22')>Js(5.0)):
            var.put('nm23', Js([Js('collapsing left and right'), Js('doing all they can to force their body in motion'), Js('sleeping amidst debris, rubble and their wounded'), Js('barely able to stand, let along lift an arm to defend themselves'), Js('giving in to whatever fate this battle has in story for them'), Js('no longer able to defend themselves and too tired to care')]))
    var.put('rnd23', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length')))))
    var.put('rnd24', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length')))))
    var.put('rnd25', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length')))))
    var.put('rnd26', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length')))))
    var.put('rnd27a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length')))))
    var.put('rnd27b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length')))))
    while PyJsStrictEq(var.get('rnd27b'),var.get('rnd27a')):
        var.put('rnd27b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length')))))
    var.put('rnd27c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length')))))
    while (PyJsStrictEq(var.get('rnd27c'),var.get('rnd27a')) or PyJsStrictEq(var.get('rnd27c'),var.get('rnd27b'))):
        var.put('rnd27c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length')))))
    var.put('rnd28a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length')))))
    var.put('rnd28b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length')))))
    while PyJsStrictEq(var.get('rnd3b'),var.get('rnd3a')):
        var.put('rnd28b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length')))))
    var.put('rnd28c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length')))))
    while (PyJsStrictEq(var.get('rnd28c'),var.get('rnd28a')) or PyJsStrictEq(var.get('rnd28c'),var.get('rnd28b'))):
        var.put('rnd28c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length')))))
    def PyJs_LONG_3_(var=var):
        return (((((((((((((Js('The ')+var.get('nm1').get(var.get('rnd1')))+Js(' is littered with '))+var.get('nm2').get(var.get('rnd2a')))+Js(', '))+var.get('nm2').get(var.get('rnd2b')))+Js(' and '))+var.get('nm2').get(var.get('rnd2c')))+Js('. Red, '))+var.get('nm3').get(var.get('rnd3a')))+Js(' and '))+var.get('nm3').get(var.get('rnd3b')))+Js(' are the new colors of what was once a '))+var.get('nm4').get(var.get('rnd4')))
    var.put('name', ((((((PyJs_LONG_3_()+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm1').get(var.get('rnd1')))+Js(', which has now become the stage of a '))+var.get('nm6').get(var.get('rnd6')))+Js('.')))
    var.put('name2', ((((((Js('The air which would normally ')+var.get('nm7').get(var.get('rnd7')))+Js(' is now '))+var.get('nm8').get(var.get('rnd8')))+Js(', '))+var.get('nm9').get(var.get('rnd9')))+Js('.')))
    def PyJs_LONG_4_(var=var):
        return ((((((((((((((var.get('nm10').get(var.get('rnd10'))+Js(' fight each other '))+var.get('nm11').get(var.get('rnd11')))+Js(', but '))+var.get('nm12').get(var.get('rnd12')))+Js('. The '))+var.get('nm13').get(var.get('rnd13')))+Js(' of'))+var.get('nm14'))+var.get('nm15').get(var.get('rnd15')))+Js(' the '))+var.get('nm1').get(var.get('rnd1')))+Js(' and the faces of the fighters are'))+var.get('nm16'))+Js('with '))
    var.put('name3', ((((((PyJs_LONG_4_()+var.get('nm17').get(var.get('rnd17a')))+Js(' and '))+var.get('nm17').get(var.get('rnd17b')))+Js(', '))+var.get('nm18').get(var.get('rnd18')))+Js('.')))
    var.put('name4', ((((((((((Js('With ')+var.get('nm19').get(var.get('rnd19')))+var.get('nm20'))+var.get('nm21').get(var.get('rnd21')))+Js('. Some have succumbed to '))+var.get('nm22').get(var.get('rnd22')))+Js(' and are '))+var.get('nm23').get(var.get('rnd23')))+Js(', while others '))+var.get('nm24').get(var.get('rnd24')))+Js('.')))
    def PyJs_LONG_5_(var=var):
        return (((((((((((Js('The toll on both nature and humanity is ')+var.get('nm25').get(var.get('rnd25')))+Js(". It'll likely take "))+var.get('nm26').get(var.get('rnd26')))+Js(' before this '))+var.get('nm1').get(var.get('rnd1')))+Js(" will have recovered. It's clear "))+var.get('nm27').get(var.get('rnd27a')))+Js(', '))+var.get('nm27').get(var.get('rnd27b')))+Js(' and '))+var.get('nm27').get(var.get('rnd27c')))
    var.put('name5', (((((((PyJs_LONG_5_()+Js(' have taken the place of '))+var.get('nm28').get(var.get('rnd28a')))+Js(', '))+var.get('nm28').get(var.get('rnd28b')))+Js(' and '))+var.get('nm28').get(var.get('rnd28c')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(7.0)):
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
battlefieldDescription = var.to_python()
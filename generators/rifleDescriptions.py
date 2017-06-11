__all__ = ['rifleDescriptions']

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
    var.registers(['nm19', 'nm1', 'nm11', 'nm24', 'nm29', 'rnd15', 'rnd11', 'rnd18', 'rnd19', 'nm16', 'rnd22', 'rnd29', 'rnd31a', 'nm23', 'nm31', 'rnd1b', 'name', 'name7', 'nm3', 'rnd14', 'rnd23', 'rnd26', 'rnd17', 'rnd13a', 'name3', 'name6', 'nm2', 'rnd2', 'name9', 'nm27', 'nm26', 'nm30', 'br', 'rnd32', 'rnd24a', 'nm22', 'name2', 'nm14', 'rnd30b', 'nm7', 'nm10', 'nm21', 'nm25', 'name4', 'rnd28', 'nm15', 'nm20', 'rnd21', 'nm1b', 'nm12', 'rnd31d', 'nm32', 'nm5', 'rnd4', 'name10', 'rnd31c', 'rnd7', 'name8', 'result', 'rnd13b', 'nm6', 'rnd20', 'rnd30a', 'nm4', 'rnd3', 'rnd24b', 'nm8', 'nm28', 'name5', 'rnd31b', 'nm17', 'nm13', 'rnd27', 'nm9', 'rnd10', 'rnd16', 'rnd25', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('a classic'), Js('a beauty'), Js('excellent'), Js('fear inducing'), Js('intimidating'), Js('near perfect'), Js('amazing'), Js('terrifying'), Js('a new release'), Js('a prototype'), Js('an odd one'), Js('a new model'), Js('a one of a kind'), Js('a new design'), Js('different from most'), Js('unique')]))
    var.put('nm1b', Js(', but '))
    var.put('nm2', Js([Js('admired by many'), Js('commissioned for many around the world'), Js('desired across the globe'), Js('famous around the world'), Js('in high demand'), Js('infamous around the world'), Js('made a name for itself'), Js('noted by many across the world'), Js('praised by many'), Js('prominent across the globe'), Js('purchased and sold by many'), Js('sold to people across the globe'), Js('well-known across the world'), Js('world renowned')]))
    var.put('nm3', Js([Js('celebrated for its consistent aim and accuracy'), Js('celebrated for its precision and reliability'), Js('known as a low cost, high value weapon'), Js('known for its deadly accuracy'), Js('known for its versatility and adaptability'), Js('praised as bang for your buck, due to its low manufacturing cost'), Js('praised for its deadly precision'), Js('praised for its reliability in almost any situation'), Js('praised for its stability, reliability and versatility'), Js('prominent due to its cheap cost and good reliability')]))
    var.put('nm4', Js([Js('overall length'), Js('standard length'), Js('length'), Js('typical length')]))
    var.put('nm5', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(500.0))+Js(600.0))))
    var.put('nm6', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(255.0))+Js(295.0))))
    var.put('nm7', Js([Js('roughly around'), Js('about'), Js('roughly'), Js('around'), Js('approximately')]))
    var.put('nm8', (var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(27.0))+Js(27.0)))/Js(10.0)))
    var.put('nm9', Js([Js('5.45x39'), Js('5.56x45'), Js('5.8x42'), Js('6.5x39'), Js('6.8x43'), Js('7.62x33'), Js('7.62x35'), Js('7.62x39'), Js('7.62x45'), Js('7.62x51'), Js('7.92x33')]))
    var.put('nm10', Js([Js('a few other calibers have been produced as well'), Js('all other standard calibers are available as well'), Js('it can come in a wide variety of different calibers'), Js('many other calibers are produced as well'), Js('most other calibers are available'), Js('one other caliber is available'), Js('other calibers are available'), Js('other calibers are available, although harder to come by'), Js('other calibers are currently in production'), Js('other calibers have yet to be produced')]))
    var.put('nm11', Js([Js('an upper and lower receiver for easier maintenance'), Js('an upper and lower receiver to allow for easier customization'), Js('an upper and lower receiver to make potential repairs easier and low cost'), Js('its receiver located in front of the pistol grip to increase customizability'), Js('its receiver located in front of the pistol grip which helped increase the barrel length'), Js('its receiver located in front of the pistol grip, allowing for a more ergonomic design'), Js('its receiver located behind the pistol grip for a more compact design'), Js('its receiver located behind the pistol grip to improve maneuverability'), Js('its receiver located behind the pistol grip to save on weight')]))
    var.put('nm12', Js([Js('wood'), Js('plastic'), Js('metal')]))
    var.put('nm13', Js([Js('wood'), Js('plastic'), Js('metal'), Js('premium wood'), Js('ivory'), Js('pearl'), Js('engraved wood'), Js('exotic wood'), Js('horn')]))
    var.put('nm14', Js([Js('your wishes'), Js('your desires'), Js('your purpose'), Js('your goals'), Js('your needs')]))
    var.put('nm15', Js([Js('walnut'), Js('maple'), Js('myrtle wood'), Js('birch'), Js('plastic'), Js('metal'), Js('laminated wood')]))
    var.put('nm16', Js([Js('other materials are available'), Js('other stocks will soon go in production'), Js('a few other stock materials are available'), Js('other stock materials are unfortunately not available yet'), Js('stocks made from a different material have to be custom made'), Js('most other stock materials are widely available'), Js('some other stock materials can be acquired with some effort'), Js('other materials, including luxury materials, are available as well'), Js('other materials have yet to be made available'), Js("other materials aren't available yet and may never be")]))
    var.put('nm17', Js([Js('folding stock'), Js('extendable stock'), Js('detachable stock'), Js('shoulder stock'), Js('wooden stock'), Js('plastic stock'), Js('straight grip stock'), Js('full grip stock'), Js('semi-grip stock')]))
    var.put('nm19', Js([Js('very common as well'), Js('the next most common stock available'), Js('high up on the list of demand'), Js('often preferred instead'), Js('used more often'), Js('just as common and popular'), Js('second in line, although not as common'), Js('very popular as well, despite being less common'), Js('slowly becoming the new standard'), Js('a close second in terms of popularity')]))
    var.put('nm20', Js([Js('drum'), Js('detachable box'), Js('horizontal box'), Js('casket'), Js('rotary'), Js('spool'), Js('STANAG'), Js('hopper'), Js('helical'), Js('saddle-drum'), Js('semi-curved')]))
    var.put('nm21', Js([Js('10'), Js('20'), Js('30'), Js('40'), Js('50'), Js('60'), Js('70'), Js('80'), Js('90'), Js('100')]))
    var.put('nm22', Js([Js('other magazine are available'), Js('plenty of other magazine are available'), Js('a few other magazines are available as well'), Js('this is generally the only available magazine'), Js('other sizes are available'), Js('the magazine comes in various sizes'), Js('while this is the only magazine type, it does come in other sizes'), Js('other magazines types and magazine sizes are available'), Js('two more sizes and one other magazine type is available'), Js('customization for other magazine types and sizes is possible')]))
    var.put('nm23', Js([Js('a push button'), Js('a paddle'), Js('a lever'), Js('both a button and lever')]))
    var.put('nm24', Js([Js('automatic'), Js('semi-auto'), Js('2-round burst'), Js('3-round burst')]))
    var.put('nm25', Js([Js('secret forces'), Js('military police'), Js('military'), Js('freedom fighters'), Js('rebels'), Js('revolutionists'), Js('separatists'), Js('army'), Js('special forces'), Js('marines'), Js('armed forces'), Js('secret service')]))
    var.put('nm26', Js([Js('winning a war'), Js('winning a civil war'), Js('preventing more crime'), Js('preventing war through a show of power'), Js('keeping the peace'), Js('increasing security'), Js('fighting crime on a bigger scale'), Js('upgrading the existing inventory'), Js('updating the existing inventory'), Js('preparing for a likely war'), Js('gaining the upper hand in a guerrilla war'), Js('providing more versatility in terms of weapon choice'), Js('increasing the amount of weapons available'), Js('fighting new threats'), Js('fighting terrorism more efficiently')]))
    var.put('nm27', Js([Js('Japanese man named H. Yoshimitsu'), Js('German man named G. Klauss'), Js('British man named E. Fawkes'), Js('American man named G. Jones'), Js('Canadian man names L. Coats'), Js('South-African man named A. Botha'), Js('Chinese man named B. Chan'), Js('Israeli man named D. Mizrahi'), Js('Russian man named T. Yakovich'), Js('Korean man named Sung S. W'), Js('Indian man named C. Mahal'), Js('Iranian man named B. Javan'), Js('Turkish man named T. Almaz'), Js('Italian man named W. Brocato'), Js('French man named C. Bouvard'), Js('Spanish man named D. Cruz')]))
    var.put('nm28', Js([Js('There are a few other variants of this weapon'), Js('Many other variants of this weapon are available'), Js('There are three other variants of this weapon'), Js('This weapon has quite a few other variants'), Js('Several other variants of this weapon are in production as well'), Js('Two other variants of this weapon are currently in production'), Js('Quite a few other variants of this weapon are available, with more nearing production'), Js('A few variants of this weapon will soon be in production')]))
    var.put('nm29', Js([Js('including a civilian version'), Js('including a semi-auto civilian version'), Js('including two less powerful civilian versions'), Js("but there's no civilian version yet"), Js('but there are no plans for a civilian version'), Js('but a civilian version is most likely out of the question'), Js('but a civilian version is currently on hold'), Js('but the plans for a less powerful civilian version have been delayed')]))
    var.put('nm30', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9')]))
    var.put('nm31', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('nm32', Js([Js('Desert Viper'), Js('Black Mamba'), Js('Peacekeeper'), Js('The Ambassador'), Js('Oathkeeper'), Js('Due Diligence'), Js('Boomer'), Js('Bulldog'), Js('Valkyrie'), Js('Vengeance'), Js('Rattlesnake'), Js('Thunder'), Js('Big Daddy'), Js('The Punisher'), Js('The Judge')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    if (var.get('rnd1')<Js(8.0)):
        var.put('rnd1b', Js(' and '))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd13a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    while PyJsStrictEq(var.get('rnd13a'),var.get('rnd12')):
        var.put('rnd13a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd13b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    while (PyJsStrictEq(var.get('rnd13b'),var.get('rnd12')) or PyJsStrictEq(var.get('rnd13b'),var.get('rnd13a'))):
        var.put('rnd13b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length')))))
    var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    while PyJsStrictEq(var.get('rnd18'),var.get('rnd17')):
        var.put('rnd18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length')))))
    var.put('rnd20', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length')))))
    var.put('rnd21', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length')))))
    if PyJsStrictEq(var.get('rnd20'),Js(0.0)):
        while (var.get('rnd21')<Js(5.0)):
            var.put('rnd21', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length')))))
    else:
        while (var.get('rnd21')>Js(4.0)):
            var.put('rnd21', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length')))))
    var.put('rnd22', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length')))))
    var.put('rnd23', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length')))))
    var.put('rnd24a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length')))))
    var.put('rnd24b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length')))))
    while PyJsStrictEq(var.get('rnd24a'),var.get('rnd24b')):
        var.put('rnd24b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length')))))
    if (PyJsStrictEq(var.get('rnd24b'),Js(2.0)) or PyJsStrictEq(var.get('rnd24b'),Js(3.0))):
        while (var.get('rnd24a')>Js(1.0)):
            var.put('rnd24a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length')))))
    var.put('rnd25', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length')))))
    var.put('rnd26', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length')))))
    var.put('rnd27', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length')))))
    var.put('rnd28', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length')))))
    var.put('rnd29', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm29').get('length')))))
    var.put('rnd30a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm30').get('length')))))
    var.put('rnd30b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm30').get('length')))))
    var.put('rnd31a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length')))))
    var.put('rnd31b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length')))))
    var.put('rnd31c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length')))))
    var.put('rnd31d', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length')))))
    var.put('rnd32', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm32').get('length')))))
    var.put('name', ((((((Js('This weapon is ')+var.get('nm1').get(var.get('rnd1')))+var.get('nm1b'))+var.get('nm2').get(var.get('rnd2')))+Js(' and '))+var.get('nm3').get(var.get('rnd3')))+Js('.')))
    var.put('name2', ((((((((((Js('The ')+var.get('nm4').get(var.get('rnd4')))+Js(' of the weapon is '))+var.get('nm5'))+Js('mm, with a '))+var.get('nm6'))+Js('mm barrel and the weapon weighs '))+var.get('nm7').get(var.get('rnd7')))+Js(' '))+var.get('nm8'))+Js('kg.')))
    var.put('name3', ((((Js('It uses ')+var.get('nm9').get(var.get('rnd9')))+Js('mm rounds, but '))+var.get('nm10').get(var.get('rnd10')))+Js('.')))
    var.put('name4', ((((((((((Js('The weapon has ')+var.get('nm11').get(var.get('rnd11')))+Js('. The pistol grip is made out of '))+var.get('nm12').get(var.get('rnd12')))+Js(', but can also be made out of '))+var.get('nm13').get(var.get('rnd13a')))+Js(' and '))+var.get('nm13').get(var.get('rnd13b')))+Js(' depending on '))+var.get('nm14').get(var.get('rnd14')))+Js('.')))
    var.put('name5', ((((((((((Js('The stock is made out of ')+var.get('nm15').get(var.get('rnd15')))+Js(', but '))+var.get('nm16').get(var.get('rnd16')))+Js('. The standard stock is a '))+var.get('nm17').get(var.get('rnd17')))+Js(', but the '))+var.get('nm17').get(var.get('rnd18')))+Js(' is '))+var.get('nm19').get(var.get('rnd19')))+Js('.')))
    var.put('name6', ((((((((Js('The standard issue magazine is a ')+var.get('nm20').get(var.get('rnd20')))+Js(' which carries '))+var.get('nm21').get(var.get('rnd21')))+Js(' rounds, but '))+var.get('nm22').get(var.get('rnd22')))+Js('. It has '))+var.get('nm23').get(var.get('rnd23')))+Js(' mechanism to release the magazine.')))
    var.put('name7', ((((Js('The selective fire modes are safe mode, ')+var.get('nm24').get(var.get('rnd24a')))+Js(' and '))+var.get('nm24').get(var.get('rnd24b')))+Js('.')))
    var.put('name8', ((((((Js('This weapon was designed for the ')+var.get('nm25').get(var.get('rnd25')))+Js(' with the purpose of '))+var.get('nm26').get(var.get('rnd26')))+Js('. It was designed by a '))+var.get('nm27').get(var.get('rnd27')))+Js('.')))
    var.put('name9', (((var.get('nm28').get(var.get('rnd28'))+Js(', '))+var.get('nm29').get(var.get('rnd29')))+Js('.')))
    var.put('name10', ((((((((((Js('The weapon is called the ')+var.get('nm30').get(var.get('rnd30a')))+var.get('nm31').get(var.get('rnd31a')))+var.get('nm31').get(var.get('rnd31b')))+Js('-'))+var.get('nm30').get(var.get('rnd30b')))+var.get('nm31').get(var.get('rnd31c')))+var.get('nm31').get(var.get('rnd31d')))+Js(", but it usally goes by its nickname '"))+var.get('nm32').get(var.get('rnd32')))+Js("'.")))
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
rifleDescriptions = var.to_python()
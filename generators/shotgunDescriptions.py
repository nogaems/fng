__all__ = ['shotgunDescriptions']

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
    var.registers(['nm19', 'nm1', 'nm11', 'rnd19', 'rnd15', 'rnd11c', 'rnd16a', 'nm16', 'name', 'rnd18b', 'name7', 'nm3', 'name3', 'name6', 'rnd13a', 'nm2', 'rnd2', 'br', 'rnd18d', 'name2', 'nm14', 'rnd12c', 'nm7', 'nm10', 'name4', 'nm15', 'rnd14b', 'rnd5', 'nm12', 'rnd14c', 'rnd12a', 'nm5', 'rnd4', 'rnd11b', 'rnd16c', 'rnd16b', 'name8', 'rnd17a', 'rnd13c', 'result', 'rnd13b', 'nm6', 'rnd11a', 'nm4', 'rnd11d', 'rnd3', 'rnd12b', 'nm8', 'rnd18a', 'name5', 'nm18', 'rnd14a', 'rnd17b', 'nm17', 'nm13', 'rnd18c', 'nm9', 'rnd10', 'rnd16', 'rnd9', 'rnd1'])
    var.put('nm1', Js([Js('single barreled'), Js('double barreled'), Js('triple barreled'), Js('quadruple barreled'), Js('single barreled'), Js('double barreled')]))
    var.put('nm2', Js([Js('a beauty'), Js('a classic'), Js('a new design'), Js('a new model'), Js('a popular one'), Js('a prototype'), Js('a unique piece'), Js('amazing'), Js('fairly simple'), Js('powerful'), Js('pretty standard'), Js('quite intimidating'), Js('stunning'), Js('very popular'), Js('very powerful')]))
    var.put('nm3', Js([Js('around the world'), Js('in many countries'), Js('legally in a few countries'), Js('illegally in many countries'), Js('globally'), Js('in only a few countries'), Js('across 2 continents'), Js('across 3 continents'), Js('in almost every country'), Js('legally in many countries')]))
    var.put('nm4', Js([Js('a high-power, high-efficiency weapon'), Js('a high-power, high-value weapon'), Js('a low-cost, high-efficiency weapon'), Js('a low-cost, high-power weapon'), Js('a low-cost, high-value weapon'), Js('a reliable, high-efficiency weapon'), Js('a reliable, high-value weapon'), Js('a reliable, low-cost weapon'), Js('a versatile, high-power weapon'), Js('a weapon with a low manufacturing cost'), Js('accurate, reliable and easy to maintain'), Js('an accurate and highly efficient weapon'), Js('an efficient and easy to maintain weapon'), Js('consistent in aim and accuracy'), Js('deadly accurate'), Js('known for its easy maintenance and reliability'), Js('known to be very reliable'), Js('reliable and precise'), Js('reliable even for its low-cost'), Js('versatile and adaptable')]))
    var.put('nm5', Js([Js('overall length'), Js('standard length'), Js('length'), Js('typical length')]))
    var.put('nm6', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(500.0))+Js(600.0))))
    var.put('nm7', (var.get('nm6')-var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(200.0))+Js(100.0)))))
    var.put('nm8', (var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(27.0))+Js(21.0)))/Js(10.0)))
    var.put('nm9', Js([Js('.360 gauge'), Js('.410 gauge'), Js('10 gauge'), Js('12 gauge'), Js('14 gauge'), Js('16 gauge'), Js('18 gauge'), Js('20 gauge'), Js('28 gauge'), Js('32 gauge'), Js('36 gauge'), Js('4 gauge'), Js('40 gauge'), Js('8 gauge')]))
    var.put('nm10', Js([Js('bolt-action'), Js('break-action'), Js('lever-action'), Js('pump-action'), Js('semi-automatic')]))
    var.put('nm11', Js([Js('baton rounds'), Js('bird bombs'), Js('breaching rounds'), Js('brenneke'), Js('buckshot'), Js("dragon's breath"), Js('flares'), Js('flechette'), Js('frag-12'), Js('gas'), Js('grenade'), Js('rock salt'), Js('rubber slugs'), Js('sabots'), Js('screechers'), Js('shotshells'), Js('slugs'), Js('stingers')]))
    var.put('nm12', Js([Js('an English fishtail stock'), Js('a Monte Carlo stock'), Js('an adjustable stock'), Js('a cheek piece stock'), Js('a folding stock'), Js('a pistol grip'), Js('a round knob stock'), Js('a standard stock'), Js('a straight English stock'), Js('a trap stock'), Js('an extendable stock')]))
    var.put('nm13', Js([Js('a cheaper type of wood'), Js('an expensive wood'), Js('exotic wood'), Js('metal'), Js('plastic'), Js('premium wood')]))
    var.put('nm14', Js([Js('custom carvings'), Js('expensive decorations'), Js('horn decorations'), Js('ivory decorations'), Js('leather decorations'), Js('marble decorations'), Js('metal decorations'), Js('no decorations at all'), Js('pearl decorations')]))
    var.put('nm15', Js([Js('Japanese man named H. Yoshimitsu'), Js('German man named G. Klauss'), Js('British man named E. Fawkes'), Js('American man named G. Jones'), Js('Canadian man names L. Coats'), Js('South-African man named A. Botha'), Js('Chinese man named B. Chan'), Js('Israeli man named D. Mizrahi'), Js('Russian man named T. Yakovich'), Js('Korean man named Sung S. W'), Js('Indian man named C. Mahal'), Js('Iranian man named B. Javan'), Js('Turkish man named T. Almaz'), Js('Italian man named W. Brocato'), Js('French man named C. Bouvard'), Js('Spanish man named D. Cruz')]))
    var.put('nm16', Js([Js('civil protection'), Js('civil warfare'), Js('crime prevention'), Js('fighting terrorism'), Js('guerilla warfare'), Js('hunting'), Js('recreational sports'), Js('riot control'), Js('the fight on drugs'), Js('warfare')]))
    var.put('nm17', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9')]))
    var.put('nm18', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('nm19', Js([Js('Armageddon'), Js('Boomer'), Js('Boomstick'), Js('Brass Rain'), Js('Bulldog'), Js('Cataclysm'), Js('Chaos'), Js('Dominion'), Js('Doom'), Js('Echo'), Js('Jaeger'), Js('Nightbane'), Js('Orbit'), Js('Patience'), Js('Rage'), Js('Requiem'), Js('Snapper'), Js('Storm'), Js('Tremor'), Js('Trinity')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    var.put('rnd11a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd11b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    while PyJsStrictEq(var.get('rnd11a'),var.get('rnd11b')):
        var.put('rnd11b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd11c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    while (PyJsStrictEq(var.get('rnd11a'),var.get('rnd11c')) or PyJsStrictEq(var.get('rnd11b'),var.get('rnd11c'))):
        var.put('rnd11c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd11d', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    while ((PyJsStrictEq(var.get('rnd11a'),var.get('rnd11d')) or PyJsStrictEq(var.get('rnd11b'),var.get('rnd11d'))) or PyJsStrictEq(var.get('rnd11c'),var.get('rnd11d'))):
        var.put('rnd11d', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd12a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd12b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    while PyJsStrictEq(var.get('rnd12a'),var.get('rnd12b')):
        var.put('rnd12b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd12c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    while (PyJsStrictEq(var.get('rnd12a'),var.get('rnd12c')) or PyJsStrictEq(var.get('rnd12b'),var.get('rnd12c'))):
        var.put('rnd12c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd13a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd13b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    while PyJsStrictEq(var.get('rnd13a'),var.get('rnd13b')):
        var.put('rnd13b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd13c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    while (PyJsStrictEq(var.get('rnd13a'),var.get('rnd13c')) or PyJsStrictEq(var.get('rnd13b'),var.get('rnd13c'))):
        var.put('rnd13c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd14a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd14b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    while PyJsStrictEq(var.get('rnd14a'),var.get('rnd14b')):
        var.put('rnd14b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd14c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    while (PyJsStrictEq(var.get('rnd14a'),var.get('rnd14c')) or PyJsStrictEq(var.get('rnd14b'),var.get('rnd14c'))):
        var.put('rnd14c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length')))))
    var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd16a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd16b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    while PyJsStrictEq(var.get('rnd16a'),var.get('rnd16b')):
        var.put('rnd16b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd16c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    while (PyJsStrictEq(var.get('rnd16a'),var.get('rnd16c')) or PyJsStrictEq(var.get('rnd16b'),var.get('rnd16c'))):
        var.put('rnd16c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd17a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd17b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd18a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd18b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd18c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd18d', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length')))))
    var.put('name', ((((((((Js('This ')+var.get('nm1').get(var.get('rnd1')))+Js(' shotgun is '))+var.get('nm2').get(var.get('rnd2')))+Js(", it's used "))+var.get('nm3').get(var.get('rnd3')))+Js(" as it's "))+var.get('nm4').get(var.get('rnd4')))+Js('.')))
    var.put('name2', ((((((((Js('The ')+var.get('nm5').get(var.get('rnd5')))+Js(' of the weapon is '))+var.get('nm6'))+Js('mm and has a barrel length of '))+var.get('nm7'))+Js('mm. The weapon weighs '))+var.get('nm8'))+Js('kg.')))
    def PyJs_LONG_0_(var=var):
        return (((((((((((Js('The caliber used in this weapon is a ')+var.get('nm9').get(var.get('rnd9')))+Js(' and uses a '))+var.get('nm10').get(var.get('rnd10')))+Js(' firing mechanism. The ammo used most commonly are '))+var.get('nm11').get(var.get('rnd11a')))+Js(', but it also takes '))+var.get('nm11').get(var.get('rnd11b')))+Js(', '))+var.get('nm11').get(var.get('rnd11c')))+Js(' and '))+var.get('nm11').get(var.get('rnd11d')))
    var.put('name3', (PyJs_LONG_0_()+Js('.')))
    var.put('name4', ((((((Js('This shotgun comes with ')+var.get('nm12').get(var.get('rnd12a')))+Js(', but '))+var.get('nm12').get(var.get('rnd12b')))+Js(' and '))+var.get('nm12').get(var.get('rnd12c')))+Js(' are also available.')))
    var.put('name5', ((((((Js('The stock is made out of ')+var.get('nm13').get(var.get('rnd13a')))+Js(', but it can also be made out of '))+var.get('nm13').get(var.get('rnd13b')))+Js(' and '))+var.get('nm13').get(var.get('rnd13c')))+Js(' if you so desire.')))
    var.put('name6', ((((((Js('There are ')+var.get('nm14').get(var.get('rnd14a')))+Js(' on the stock, but '))+var.get('nm14').get(var.get('rnd14b')))+Js(' or '))+var.get('nm14').get(var.get('rnd14c')))+Js(' are available as well.')))
    var.put('name7', ((((((((((Js('This weapon was designed by a ')+var.get('nm15').get(var.get('rnd15')))+Js(' who initially disgned it for use in '))+var.get('nm16').get(var.get('rnd16')))+Js(", today it's used for "))+var.get('nm16').get(var.get('rnd16a')))+Js(', '))+var.get('nm16').get(var.get('rnd16b')))+Js(' and '))+var.get('nm16').get(var.get('rnd16c')))+Js('.')))
    var.put('name8', ((((((((((Js('The name of this weapon is the ')+var.get('nm17').get(var.get('rnd17a')))+var.get('nm17').get(var.get('rnd17b')))+Js('-'))+var.get('nm18').get(var.get('rnd18a')))+var.get('nm18').get(var.get('rnd18b')))+var.get('nm18').get(var.get('rnd18c')))+var.get('nm18').get(var.get('rnd18d')))+Js(', but it usually goes by its nickname, '))+var.get('nm19').get(var.get('rnd19')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(9.0)):
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
shotgunDescriptions = var.to_python()
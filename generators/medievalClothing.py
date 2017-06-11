__all__ = ['medievalClothing']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm24', 'nm29', 'nm16', 'nm23', 'nm31', 'nm3', 'nm33', 'nm2', 'nm27', 'nm26', 'nm30', 'nm36', 'nm39', 'nm22', 'nm14', 'nm7', 'nm10', 'nm21', 'nm25', 'nm15', 'nm20', 'nm12', 'nm32', 'nm5', 'nm6', 'nm35', 'nm4', 'nameGen', 'nm8', 'nm28', 'nm18', 'nm37', 'nm17', 'nm13', 'nm9', 'nm38'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['rnd19', 'rnd18', 'rnd15', 'rnd29', 'rnd11', 'rnd22', 'rnd8', 'name', 'rnd23', 'rnd14', 'name3', 'rnd26', 'rnd17', 'rnd', 'rnd2', 'rnd35', 'br', 'rnd32', 'type', 'name2', 'tp', 'rnd28', 'rnd21', 'rnd38', 'rnd5', 'rnd4', 'rnd37', 'rnd16b', 'rnd7', 'rnd31', 'rnd30', 'rnd33', 'result', 'rnd6', 'rnd20', 'rnd13', 'rnd3', 'rnd27', 'rnd16', 'rnd10', 'rnd25', 'rnd34', 'rnd36', 'rnd9', 'rnd12', 'rnd1'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('rnd', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
        var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
        var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
        var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
        while PyJsStrictEq(var.get('rnd'),var.get('rnd1')):
            var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
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
        var.put('rnd16b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
        var.put('rnd17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
        var.put('rnd18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
        def PyJs_LONG_0_(var=var):
            return ((((((((((((Js('Her ')+var.get('nm1').get(var.get('rnd')))+Js(' dress flows from top to bottom and has a '))+var.get('nm2').get(var.get('rnd2')))+Js(', which '))+var.get('nm3').get(var.get('rnd3')))+Js(' reveals the '))+var.get('nm1').get(var.get('rnd1')))+Js(' dress worn below it. The '))+var.get('nm4').get(var.get('rnd4')))+Js(', '))+var.get('nm5').get(var.get('rnd5')))+Js(' of her dress covers her stomach where the continuous flow is broken up by a '))
        var.put('name', ((((((PyJs_LONG_0_()+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+Js(' worn '))+var.get('nm8').get(var.get('rnd8')))+Js(' around her waist.')))
        var.put('name2', ((((((((((Js('Below the ')+var.get('nm7').get(var.get('rnd7')))+Js(' the dress '))+var.get('nm9').get(var.get('rnd9')))+Js(' the dress below. The front of the top dress '))+var.get('nm10').get(var.get('rnd10')))+Js(', the back continues to flow a '))+var.get('nm11').get(var.get('rnd11')))+Js(' length behind her and ends in a '))+var.get('nm12').get(var.get('rnd12')))+Js('.')))
        def PyJs_LONG_1_(var=var):
            return ((((((((((((Js('Her sleeves are ')+var.get('nm13').get(var.get('rnd13')))+Js(' and '))+var.get('nm14').get(var.get('rnd14')))+Js(', their flow is broken up '))+var.get('nm15').get(var.get('rnd15')))+Js(' where '))+var.get('nm16').get(var.get('rnd16')))+Js("they're divided by "))+var.get('nm6').get(var.get('rnd16b')))+Js(', '))+var.get('nm17').get(var.get('rnd17')))+Js(' bands, these are the same fabric and color used to outline the '))
        var.put('name3', ((PyJs_LONG_1_()+var.get('nm18').get(var.get('rnd18')))+Js(' of the dress.')))
    else:
        var.put('rnd19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length')))))
        var.put('rnd20', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length')))))
        var.put('rnd21', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length')))))
        var.put('rnd22', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length')))))
        var.put('rnd23', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length')))))
        if (var.get('rnd19')>Js(2.0)):
            var.put('rnd24', Js(' shirt '))
        var.put('rnd25', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length')))))
        var.put('rnd26', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length')))))
        var.put('rnd27', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length')))))
        var.put('rnd28', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length')))))
        var.put('rnd29', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm29').get('length')))))
        var.put('rnd30', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm30').get('length')))))
        var.put('rnd31', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length')))))
        var.put('rnd32', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm32').get('length')))))
        var.put('rnd33', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm33').get('length')))))
        var.put('rnd34', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length')))))
        var.put('rnd35', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm35').get('length')))))
        var.put('rnd36', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm36').get('length')))))
        var.put('rnd37', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm37').get('length')))))
        var.put('rnd38', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm38').get('length')))))
        def PyJs_LONG_2_(var=var):
            return ((((((((((((((Js('His ')+var.get('nm19').get(var.get('rnd19')))+Js(' sleeved, '))+var.get('nm20').get(var.get('rnd20')))+Js(' jacket covers him to '))+var.get('nm21').get(var.get('rnd21')))+Js(' and is '))+var.get('nm22').get(var.get('rnd22')))+Js(' '))+var.get('nm23').get(var.get('rnd23')))+Js('. The sleeves of his'))+var.get('nm24'))+Js('are '))+var.get('nm25').get(var.get('rnd25')))+Js(' and reach down to '))
        var.put('name', ((((PyJs_LONG_2_()+var.get('nm26').get(var.get('rnd26')))+Js(", they're decorated with "))+var.get('nm27').get(var.get('rnd27')))+Js('.')))
        def PyJs_LONG_3_(var=var):
            return (((((((((((Js('The jacket has a ')+var.get('nm28').get(var.get('rnd28')))+Js(' which reveals part of the '))+var.get('nm29').get(var.get('rnd29')))+Js(' shirt worn below it and is worn with a '))+var.get('nm30').get(var.get('rnd30')))+Js(' '))+var.get('nm31').get(var.get('rnd31')))+Js(', which is held together by '))+var.get('nm32').get(var.get('rnd32')))+Js('. The '))+var.get('nm31').get(var.get('rnd31')))
        var.put('name2', (((PyJs_LONG_3_()+Js(' is '))+var.get('nm33').get(var.get('rnd33')))+Js('.')))
        def PyJs_LONG_4_(var=var):
            return (((((((((((((Js('His pants are simple and ')+var.get('nm25').get(var.get('rnd34')))+Js(' and reach down to his '))+var.get('nm35').get(var.get('rnd35')))+Js(' '))+var.get('nm38').get(var.get('rnd38')))+Js('. The '))+var.get('nm38').get(var.get('rnd38')))+Js(' are made from a '))+var.get('nm36').get(var.get('rnd36')))+Js(' '))+var.get('nm39').get(var.get('rnd35')))+Js(', but are otherwise '))+var.get('nm37').get(var.get('rnd37')))
        var.put('name3', (PyJs_LONG_4_()+Js('.')))
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
var.put('nm1', Js([Js('delicate'), Js('elegant'), Js('fancy'), Js('graceful'), Js('luxurious'), Js('relatively simple'), Js('majestic'), Js('modest'), Js('noble'), Js('ornate'), Js('rather simple'), Js('refined'), Js('stylish'), Js('traditional')]))
var.put('nm2', Js([Js('Queen Anne neckline'), Js('court neckline'), Js('cowl neckline'), Js('draped neckline'), Js('halter neckline'), Js('jewel neckline'), Js('keyhole neckline'), Js('round neckline'), Js('scoop neckline'), Js('semi-sweethear neckline'), Js('square neckline'), Js('sweetheart neckline'), Js('v-neck')]))
var.put('nm3', Js([Js('charmingly'), Js('daintily'), Js('delicately'), Js('elegantly'), Js('entrancingly'), Js('gracefully'), Js('graciously'), Js('harmoniously'), Js('lightly'), Js('subtly'), Js('tastefully'), Js('wonderfully')]))
var.put('nm4', Js([Js('comfortable'), Js('delectable'), Js('delicate'), Js('exquisite'), Js('fine'), Js('flowing'), Js('gentle'), Js('ornate'), Js('satiny'), Js('silky'), Js('smooth'), Js('soft'), Js('velvety')]))
var.put('nm5', Js([Js('buttoned up fabric'), Js('loosely tied fabric'), Js('tightly tied fabric'), Js('corset-like tied fabric'), Js('corset')]))
var.put('nm6', Js([Js('thin'), Js('thick'), Js('simple'), Js('small'), Js('slender'), Js('light'), Js('dark'), Js('large'), Js('long'), Js('wide'), Js('small')]))
var.put('nm7', Js([Js('leather belt'), Js('ribbon'), Js('cloth belt'), Js('rope belt'), Js('cloth band')]))
var.put('nm8', Js([Js('fairly high'), Js('quite high'), Js('low'), Js('high'), Js('fairly low'), Js('quite low')]))
var.put('nm9', Js([Js('opens up slightly and reveals'), Js('opens up to the right and reveals'), Js('opens up to the left and reveals'), Js('opens up and reveals'), Js('opens up wide and reveals'), Js('flows down and hides'), Js('opens up left and right and reveals'), Js('flows down wide and hides')]))
var.put('nm10', Js([Js('is shorter at the front and curves outwards'), Js('is much shorter at the front and curves outwards'), Js('is shorter at the front and flows straight down'), Js('reaches the ground generously'), Js('easily reaches the ground in the front'), Js('is longer than the bottom dress and flows straight down'), Js('is longer than the bottom dress and curves outwards'), Js('makes it just to the ground to cover her feet')]))
var.put('nm11', Js([Js('fair'), Js('large'), Js('good'), Js('short'), Js('decent'), Js('long'), Js('small')]))
var.put('nm12', Js([Js('broad curve'), Js('narrow curve'), Js('narrow tip'), Js('broad tip'), Js('narrow rectangle'), Js('broad rectangle')]))
var.put('nm13', Js([Js('very long'), Js('quite long'), Js('a little too long'), Js('purposely too long'), Js('incredibly long'), Js('the length of her arms'), Js('longer than her arms'), Js('slightly shorter than her arms'), Js('almost the length of her arms'), Js('fairly short'), Js('a little short')]))
var.put('nm14', Js([Js('incredibly wide'), Js('very wide'), Js('quite wide'), Js('wide'), Js('a little wide'), Js('narrow'), Js('quite narrow'), Js('a little narrow'), Js('a comfortable fit'), Js('a loose fit')]))
var.put('nm15', Js([Js('just below the shoulder'), Js('just below the elbow'), Js('just above the elbow'), Js('below the shoulder'), Js('below the elbow'), Js('above the elbow'), Js('well below the shoulder'), Js('well below the elbow'), Js('well above the elbow'), Js('at the elbow'), Js('at the shoulder')]))
var.put('nm16', Js([Js('they change color and where '), Js('')]))
var.put('nm17', Js([Js('decorative'), Js('elegant'), Js('ornamental'), Js('cosmetic'), Js('embellishing'), Js('ornate'), Js('delicate'), Js('graceful'), Js('luxurious'), Js('simple'), Js('modest'), Js('refined'), Js('stylish')]))
var.put('nm18', Js([Js('edges'), Js('sleeves'), Js('sleeves and bottom'), Js('bottom'), Js('neckline'), Js('bottom and neckline'), Js('sleeves, bottom and neckline'), Js('sleeves and neckline')]))
var.put('nm19', Js([Js('long'), Js('very long'), Js('fairly long'), Js('short'), Js('very short'), Js('fairly short')]))
var.put('nm20', Js([Js('leather'), Js('hide'), Js('furred'), Js('cloth'), Js('animal skin'), Js('silky'), Js('velvety')]))
var.put('nm21', Js([Js('just below his waist'), Js('well below his waist'), Js('just below his groin'), Js('well below his groin'), Js('just below his knees'), Js('well below his knees'), Js('just above his waist'), Js('well above his waist'), Js('just above his groin'), Js('well above his groin'), Js('just above his knees'), Js('well above his knees'), Js('his waist'), Js('his knees'), Js('his groin')]))
var.put('nm22', Js([Js('tightly tied with string'), Js('loosely tied with string'), Js('buttoned up completely'), Js('almost completely buttoned up'), Js('half buttoned up'), Js('barely tied with string'), Js('barely buttoned up'), Js('bound')]))
var.put('nm23', Js([Js('at the center'), Js('at the left side'), Js('at the right side'), Js('at the top left side'), Js('at the top right side'), Js('at the bottom left side'), Js('at the bottom right side'), Js('slightly off-center')]))
var.put('nm24', Js(' jacket '))
var.put('nm25', Js([Js('incredibly wide'), Js('very wide'), Js('quite wide'), Js('wide'), Js('a little wide'), Js('narrow'), Js('quite narrow'), Js('a little narrow'), Js('a comfortable fit'), Js('a loose fit')]))
var.put('nm26', Js([Js('his hands'), Js('just above his hands'), Js('well below his hands'), Js('below his hands'), Js('well above his hands'), Js('his wrists'), Js('just below his wrists'), Js('just above his wrists'), Js('well above his wrists'), Js('well below his wrists')]))
var.put('nm27', Js([Js('a single thread lining from top to bottom'), Js('several thread linings from top to bottom'), Js('a single thread lining at the sleeve ends'), Js('several thread linings at the sleeve ends'), Js('a decorative band at the edges'), Js('a decorative band almost at the edges'), Js('a single thread lining and a decorative band')]))
var.put('nm28', Js([Js('round neckline'), Js('wide, round neckline'), Js('narrow, round neckline'), Js('deep, round neckline'), Js('wide v-neck'), Js('narrow v-neck'), Js('deep v-neck'), Js('rectangular neckline'), Js('wide, rectangular neckline'), Js('narrow, rectangular neckline'), Js('deep, rectangular neckline')]))
var.put('nm29', Js([Js('rough'), Js('elegant'), Js('fancy'), Js('graceful'), Js('luxurious'), Js('relatively simple'), Js('majestic'), Js('modest'), Js('noble'), Js('ornate'), Js('rather simple'), Js('refined'), Js('stylish'), Js('traditional')]))
var.put('nm30', Js([Js('thin'), Js('thick'), Js('simple'), Js('small'), Js('big'), Js('light'), Js('dark'), Js('large'), Js('long'), Js('wide'), Js('small')]))
var.put('nm31', Js([Js('leather belt'), Js('cloth belt'), Js('rope belt'), Js('cloth band')]))
var.put('nm32', Js([Js('a big belt buckle'), Js('a simple knot'), Js('a small belt buckle'), Js('an intricate knot'), Js('an ornate pin'), Js('a decorative pin')]))
var.put('nm33', Js([Js('purely decorative and a sign of wealth'), Js('mostly decorative and a sign of wealth'), Js('entirely decorative and a way to show off'), Js('solely decorative and a status symbol'), Js('mostly decorative, but does serve its purpose'), Js('partially decorative, but mostly a purposeful addition'), Js('slightly decorative, but mostly there to hang things from'), Js('almost entirely a functional addition'), Js('purely a functional addition'), Js('a functional addition, but does have some decorative value')]))
var.put('nm35', Js([Js('leather'), Js('hide'), Js('furred'), Js('soft leather'), Js('hard leather'), Js('bound cloth')]))
var.put('nm36', Js([Js('rare'), Js('very rare'), Js('fairly rare'), Js('fairly uncommon'), Js('very uncommon'), Js('pretty uncommon'), Js('pretty rare'), Js('pretty unusual'), Js('pretty unique')]))
var.put('nm37', Js([Js('quite simple'), Js('a simple design'), Js('an ordinary design'), Js('a common design'), Js('a common type'), Js('not that special'), Js('a design found commonly'), Js('not any different from others')]))
var.put('nm38', Js([Js('boots'), Js('shoes')]))
var.put('nm39', Js([Js('leather'), Js('hide'), Js('fur'), Js('leather'), Js('leather'), Js('cloth')]))
pass
pass


# Add lib to the module scope
medievalClothing = var.to_python()
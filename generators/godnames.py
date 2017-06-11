__all__ = ['godnames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd5')))+Js(', Goddess of '))+var.get('nm6').get(var.get('rnd6'))))
            else:
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+Js(', God of '))+var.get('nm6').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('y')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('agi'), Js('aldir'), Js('aos'), Js('arus'), Js('borh'), Js('bris'), Js('bum'), Js('bus'), Js('dall'), Js('dar'), Js('darr'), Js('des'), Js('dis'), Js('dite'), Js('dohr'), Js('don'), Js('dos'), Js('dros'), Js('dum'), Js('dur'), Js('emis'), Js('enar'), Js('esis'), Js('eus'), Js('eyar'), Js('eyr'), Js('her'), Js('ion'), Js('ione'), Js('ius'), Js('jun'), Js('ldir'), Js('lios'), Js('lo'), Js('lous'), Js('mes'), Js('mir'), Js('mjir'), Js('mos'), Js('mus'), Js('nia'), Js('lotl'), Js('zotz'), Js('zotl'), Js('nir'), Js('nos'), Js('nus'), Js('ohr'), Js('orr'), Js('rasil'), Js('reus'), Js('ros'), Js('ruer'), Js('rus'), Js('ses'), Js('stus'), Js('tar'), Js('tarr'), Js('teus'), Js('thar'), Js('ther'), Js('tia'), Js('ton'), Js('tos'), Js('tyx'), Js('ysus')]))
var.put('nm5', Js([Js('ra'), Js('ara'), Js('ella'), Js('elia'), Js('nja'), Js('yja'), Js('ulla'), Js('la'), Js('na'), Js('ana'), Js('otz'), Js('otl'), Js('neas'), Js('phine'), Js('tris'), Js('gyn'), Js('syn'), Js('dite'), Js('ena'), Js('hena'), Js('tia'), Js('anke'), Js('mera'), Js('nera'), Js('soi'), Js('heia'), Js('mis'), Js('thys'), Js('asis'), Js('one'), Js('dione'), Js('dona'), Js('ona'), Js('phion'), Js('trix'), Js('tix'), Js('lene'), Js('lena'), Js('phy'), Js('tune'), Js('va'), Js('una'), Js('tuna'), Js('arae'), Js('aris'), Js('ris'), Js('tia'), Js('rena'), Js('raura'), Js('dea'), Js('enta'), Js('dia'), Js('ta')]))
var.put('nm6', Js([Js('Abundance'), Js('Agriculture'), Js('Animals'), Js('Battle'), Js('Beauty'), Js('Beer'), Js('Beginnings'), Js('Blacksmiths'), Js('Chaos'), Js('Children'), Js('Chivalry'), Js('Commerce'), Js('Conquest'), Js('Dawn'), Js('Day'), Js('Death'), Js('Destiny'), Js('Destruction'), Js('Dreams'), Js('Dusk'), Js('Duty'), Js('Earth'), Js('Education'), Js('Endings'), Js('Envy'), Js('Fall'), Js('Fame'), Js('Fertility'), Js('Finance'), Js('Fire'), Js('Forgiveness'), Js('Fortune'), Js('Freedom'), Js('Funerals'), Js('Good Luck'), Js('Governance'), Js('Harvest'), Js('Hatred'), Js('Health'), Js('Home'), Js('Honesty'), Js('Honor'), Js('Hope'), Js('Hunting'), Js('Infamy'), Js('Jealousy'), Js('Judgement'), Js('Justice'), Js('Law'), Js('Life'), Js('Life & Death'), Js('Light'), Js('Logic'), Js('Love'), Js('Loyalty'), Js('Magic'), Js('Marriage'), Js('Medicine'), Js('Mercy'), Js('Messages'), Js('Miracles'), Js('Misfortune'), Js('Music'), Js('Nature'), Js('Night'), Js('Night & Day'), Js('Oracles'), Js('Order'), Js('Peace'), Js('Penance'), Js('Pleasure'), Js('Poetry'), Js('Prosperity'), Js('Revenge'), Js('Science'), Js('Secrecy'), Js('Shadows'), Js('Sleep'), Js('Spring'), Js('Strength'), Js('Success'), Js('Summer'), Js('Thunder'), Js('Time'), Js('Torture'), Js('Trade'), Js('Tranquility'), Js('Tricks'), Js('Truth'), Js('Vengeance'), Js('Victory'), Js('Virtues'), Js('War'), Js('Water'), Js('Weddings'), Js('Wind'), Js('Wine'), Js('Winter'), Js('Wisdom'), Js('Work'), Js('Youth'), Js('the Afterlife'), Js('the Dark'), Js('the Hearth'), Js('the Hunt'), Js('the Insane'), Js('the Land'), Js('the Military'), Js('the Moon'), Js('the Mountains'), Js('the Ocean'), Js('the Ostracized'), Js('the Rivers'), Js('the Sea'), Js('the Sky'), Js('the Stars'), Js('the Sun'), Js('the Underworld')]))
pass
pass


# Add lib to the module scope
godnames = var.to_python()
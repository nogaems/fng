__all__ = ['mgtGods']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while PyJsStrictEq(var.get('nm9').get(var.get('rnd3')),var.get('nm7').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('names', (((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+Js(', God of '))+var.get('nm12').get(var.get('rnd12'))))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', (((((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd5')))+Js(', God of '))+var.get('nm12').get(var.get('rnd12'))))
                    else:
                        var.put('names', (((((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm8').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd4')))+Js(', God of '))+var.get('nm12').get(var.get('rnd12'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+Js(', God of '))+var.get('nm12').get(var.get('rnd12'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd5')))+Js(', God of '))+var.get('nm12').get(var.get('rnd12'))))
                    else:
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+Js(', God of '))+var.get('nm12').get(var.get('rnd12'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('cr'), Js('h'), Js('k'), Js('kr'), Js('m'), Js('n'), Js('ph'), Js('v'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('fr'), Js('g'), Js('l'), Js('ll'), Js('lr'), Js('n'), Js('ph'), Js('r'), Js('rph'), Js('rv'), Js('rc'), Js('rk'), Js('rl'), Js('th'), Js('thr'), Js('v'), Js('z')]))
var.put('nm4', Js([Js('a'), Js('i'), Js('o'), Js('a'), Js('i'), Js('o'), Js('io'), Js('ia'), Js('oa'), Js('eo')]))
var.put('nm5', Js([Js('b'), Js('d'), Js('g'), Js('l'), Js('n'), Js('r'), Js('t'), Js('z')]))
var.put('nm6', Js([Js('d'), Js('s'), Js('t'), Js('th'), Js('x'), Js('s'), Js('s'), Js('x'), Js('x'), Js('s'), Js('s'), Js('s')]))
var.put('nm7', Js([Js('c'), Js('f'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('th')]))
var.put('nm8', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('y')]))
var.put('nm9', Js([Js('l'), Js('ll'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('rr'), Js('s'), Js('sh'), Js('ss'), Js('th')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('ea'), Js('ae'), Js('ia'), Js('oe')]))
var.put('nm11', Js([Js('c'), Js('h'), Js('k'), Js('l'), Js('n'), Js('r'), Js('ss'), Js('tr'), Js('y')]))
var.put('nm12', Js([Js('Abundance'), Js('Agriculture'), Js('Animals'), Js('Battle'), Js('Beauty'), Js('Beer'), Js('Beginnings'), Js('Blacksmiths'), Js('Chaos'), Js('Children'), Js('Chivalry'), Js('Commerce'), Js('Conquest'), Js('Dawn'), Js('Day'), Js('Death'), Js('Destiny'), Js('Destruction'), Js('Dreams'), Js('Dusk'), Js('Duty'), Js('Earth'), Js('Education'), Js('Endings'), Js('Envy'), Js('Fall'), Js('Fame'), Js('Fertility'), Js('Finance'), Js('Fire'), Js('Forgiveness'), Js('Fortune'), Js('Freedom'), Js('Funerals'), Js('Good Luck'), Js('Governance'), Js('Harvest'), Js('Hatred'), Js('Health'), Js('Home'), Js('Honesty'), Js('Honor'), Js('Hope'), Js('Hunting'), Js('Infamy'), Js('Jealousy'), Js('Judgement'), Js('Justice'), Js('Law'), Js('Life'), Js('Life & Death'), Js('Light'), Js('Logic'), Js('Love'), Js('Loyalty'), Js('Magic'), Js('Marriage'), Js('Medicine'), Js('Mercy'), Js('Messages'), Js('Miracles'), Js('Misfortune'), Js('Music'), Js('Nature'), Js('Night'), Js('Night & Day'), Js('Oracles'), Js('Order'), Js('Peace'), Js('Penance'), Js('Pleasure'), Js('Poetry'), Js('Prosperity'), Js('Revenge'), Js('Science'), Js('Secrecy'), Js('Shadows'), Js('Sleep'), Js('Spring'), Js('Strength'), Js('Success'), Js('Summer'), Js('Thunder'), Js('Time'), Js('Torture'), Js('Trade'), Js('Tranquility'), Js('Tricks'), Js('Truth'), Js('Vengeance'), Js('Victory'), Js('Virtues'), Js('War'), Js('Water'), Js('Weddings'), Js('Wind'), Js('Wine'), Js('Winter'), Js('Wisdom'), Js('Work'), Js('Youth'), Js('the Afterlife'), Js('the Dark'), Js('the Hearth'), Js('the Hunt'), Js('the Insane'), Js('the Land'), Js('the Military'), Js('the Moon'), Js('the Mountains'), Js('the Ocean'), Js('the Ostracized'), Js('the Rivers'), Js('the Sea'), Js('the Sky'), Js('the Stars'), Js('the Sun'), Js('the Underworld')]))
pass
pass


# Add lib to the module scope
mgtGods = var.to_python()
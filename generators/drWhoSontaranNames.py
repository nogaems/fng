__all__ = ['drWhoSontaranNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('names', ((((((((((var.get('nm8').get(var.get('rnd7'))+var.get('nm4').get(var.get('rnd8')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd10')))+var.get('nm6').get(var.get('rnd11')))+Js('  '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(' the '))+var.get('nm7').get(var.get('rnd4'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    def PyJs_LONG_0_(var=var):
                        return (((((((((((var.get('nm8').get(var.get('rnd7'))+var.get('nm4').get(var.get('rnd8')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd10')))+var.get('nm6').get(var.get('rnd11')))+Js('  '))+var.get('nm1').get(var.get('rnd')))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+Js(' the '))
                    var.put('names', (PyJs_LONG_0_()+var.get('nm7').get(var.get('rnd6'))))
                else:
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    def PyJs_LONG_1_(var=var):
                        return (((((((((((var.get('nm8').get(var.get('rnd7'))+var.get('nm4').get(var.get('rnd8')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd10')))+var.get('nm6').get(var.get('rnd11')))+Js('  '))+var.get('nm1').get(var.get('rnd')))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+Js(' the '))
                    var.put('names', (PyJs_LONG_1_()+var.get('nm7').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('Br'), Js('D'), Js('Dr'), Js('Gr'), Js('J'), Js('K'), Js('Kr'), Js('L'), Js('N'), Js('M'), Js('S'), Js('Sk'), Js('Sn'), Js('St'), Js('T'), Js('Tr'), Js('V'), Js('Vr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('aa'), Js('ee')]))
var.put('nm3', Js([Js('g'), Js('gg'), Js('gt'), Js('gh'), Js('k'), Js('kt'), Js('kk'), Js('l'), Js('ll'), Js('nt'), Js('nx'), Js('r'), Js('rl'), Js('rr'), Js('rk'), Js('rn'), Js('rg'), Js('sk')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm5', Js([Js('d'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('mt'), Js('ng'), Js('nt'), Js('r'), Js('rt'), Js('rn'), Js('st'), Js('ts'), Js('th'), Js('v')]))
var.put('nm6', Js([Js(''), Js(''), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('x')]))
var.put('nm7', Js([Js('Adept'), Js('Admired'), Js('Aggressive'), Js('Aggressor'), Js('Agile'), Js('Ambitious'), Js('Assassin'), Js('Avenger'), Js('Beast'), Js('Behemoth'), Js('Bloodbringer'), Js('Bloodhunter'), Js('Bloodied'), Js('Bold'), Js('Brave'), Js('Brilliant'), Js('Brutal'), Js('Butcher'), Js('Champion'), Js('Clever'), Js('Corruptor'), Js('Crafty'), Js('Crooked'), Js('Cunning'), Js('Danger'), Js('Dapper'), Js('Defiant'), Js('Diligent'), Js('Doombringer'), Js('Eliminator'), Js('Enforcer'), Js('Enormous'), Js('Exalted'), Js('Executioner'), Js('Expert'), Js('Fearless'), Js('Glorious'), Js('Grand'), Js('Great'), Js('Hunter'), Js('Illustrious'), Js('Immortal'), Js('Incredible'), Js('Infamous'), Js('Inventor'), Js('Killer'), Js('Knowing'), Js('Loyal'), Js('Magnificent'), Js('Marvelous'), Js('Master'), Js('Masterful'), Js('Menace'), Js('Merciless'), Js('Mighty'), Js('Paragon'), Js('Powerful'), Js('Prestigious'), Js('Proud'), Js('Razor'), Js('Reckless'), Js('Reliable'), Js('Ruthless'), Js('Slayer'), Js('Sneaky'), Js('Stark'), Js('Stout'), Js('Strong'), Js('Terrific'), Js('Terror'), Js('Turbulent'), Js('Undefeated'), Js('Valiant'), Js('Vengeful'), Js('Victorious'), Js('Vigilant'), Js('Warlord'), Js('Warmonger'), Js('Warrior'), Js('Wild'), Js('Wonderful'), Js('Wrathful'), Js('Wretched'), Js('Zealous')]))
var.put('nm8', Js([Js('B'), Js('D'), Js('G'), Js('J'), Js('K'), Js('L'), Js('N'), Js('M'), Js('S'), Js('T'), Js('V')]))
var.put('nm9', Js([Js('d'), Js('g'), Js('gg'), Js('gr'), Js('k'), Js('kr'), Js('kk'), Js('l'), Js('ll'), Js('ng'), Js('n'), Js('nn'), Js('r'), Js('rl'), Js('rr'), Js('rk'), Js('rn'), Js('rg'), Js('st'), Js('sk'), Js('th'), Js('v')]))
pass
pass


# Add lib to the module scope
drWhoSontaranNames = var.to_python()
__all__ = ['mgtDwarfs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
            var.put('lName', ((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd5'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    while PyJsStrictEq(var.get('nm7').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        while PyJsStrictEq(var.get('nm8').get(var.get('rnd5')),var.get('nm7').get(var.get('rnd3'))):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', (((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd5')),var.get('nm7').get(var.get('rnd3'))):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('names', ((var.get('nm14').get(var.get('rnd'))+Js(' '))+var.get('nm15').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('names', ((var.get('nm14').get(var.get('rnd'))+Js(' '))+var.get('nm15').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('r'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('i')]))
var.put('nm3', Js([Js('br'), Js('dd'), Js('dr'), Js('fn'), Js('fg'), Js('kn'), Js('km'), Js('kd'), Js('kg'), Js('kr'), Js('ld'), Js('lth'), Js('lg'), Js('lb'), Js('ldr'), Js('lz'), Js('lv'), Js('mg'), Js('md'), Js('mk'), Js('mz'), Js('ng'), Js('nk'), Js('nd'), Js('nv'), Js('rb'), Js('rd'), Js('rg'), Js('rk'), Js('rt'), Js('sg'), Js('sk'), Js('sr'), Js('tr'), Js('tk'), Js('tg'), Js('yl'), Js('yr'), Js('yg'), Js('yz'), Js('yv'), Js('zr'), Js('zg'), Js('zn')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('m'), Js('n'), Js('r')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('h'), Js('k'), Js('n'), Js('m'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ee'), Js('aa')]))
var.put('nm7', Js([Js('d'), Js('g'), Js('k'), Js('p'), Js('r'), Js('v'), Js('z')]))
var.put('nm8', Js([Js('d'), Js('g'), Js('j'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm9', Js([Js('d'), Js('l'), Js('n'), Js('s')]))
var.put('nm10', Js([Js('b'), Js('d'), Js('j'), Js('g'), Js('k'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm11', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm12', Js([Js('bb'), Js('br'), Js('gg'), Js('gn'), Js('gr'), Js('gl'), Js('kr'), Js('km'), Js('kn'), Js('kl'), Js('lg'), Js('lm'), Js('lr'), Js('lv'), Js('mb'), Js('md'), Js('mv'), Js('ml'), Js('ng'), Js('nd'), Js('nb'), Js('nl'), Js('rm'), Js('rk'), Js('rg'), Js('rl'), Js('rn'), Js('tn'), Js('tl')]))
var.put('nm13', Js([Js('d'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm14', Js([Js('Academic'), Js('Acclaimed'), Js('Accomplished'), Js('Adept'), Js('Advanced'), Js('Aerial'), Js('Aviary'), Js('Bomb'), Js('Brave'), Js('Bridge'), Js('Brilliant'), Js('Bruised'), Js('Cautious'), Js('Chief'), Js("Consul's"), Js('Dapper'), Js('Defensive'), Js('Defiant'), Js('Demolition'), Js('Devoted'), Js('Diligent'), Js('Dutiful'), Js('Dwarven'), Js('Eager'), Js('Esteemed'), Js('Exalted'), Js('Examplar'), Js('Examplary'), Js('Expert'), Js('Fearless'), Js('Gearshift'), Js('Gifted'), Js('Grand'), Js('Great'), Js('Illustrious'), Js('Infamous'), Js('Junior'), Js('Liberated'), Js('Lone'), Js('Lost'), Js('Loyal'), Js('Master'), Js('Nimble'), Js('Powerful'), Js('Prestigious'), Js('Prime'), Js('Reckless'), Js('Robust'), Js('Rough'), Js('Rowdy'), Js('Savant'), Js('Sneaky'), Js('Sturdy'), Js('Swift'), Js('Thunderous'), Js('Trained'), Js('Troubled'), Js('Venerated'), Js('Vengeful'), Js('Veteran'), Js('Villainous'), Js('Violent'), Js('Visionary'), Js('Wicked'), Js('Wild'), Js('Wrathful')]))
var.put('nm15', Js([Js('Armorer'), Js('Artificer'), Js('Artisan'), Js('Assailant'), Js('Augmenter'), Js('Berserker'), Js('Blacksmith'), Js('Blastminer'), Js('Cadet'), Js('Captain'), Js('Conjurer'), Js('Crafter'), Js('Craftsman'), Js('Defender'), Js('Digger'), Js('Driller'), Js('Excavator'), Js('Gearshift'), Js('Grease Monkey'), Js('Grunt'), Js('Guard'), Js('Machinist'), Js('Mage'), Js('Mechanic'), Js('Mender'), Js('Mercenary'), Js('Miner'), Js('Motorist'), Js('Nomad'), Js('Operator'), Js('Patrol'), Js('Pilot'), Js('Prospector'), Js('Recruit'), Js('Recruiter'), Js('Scorcher'), Js('Scout'), Js('Sentinel'), Js('Sentry'), Js('Shieldguard'), Js('Soldier'), Js('Specialist'), Js('Swordsmith'), Js('Technician'), Js('Thaumaturgist'), Js('Tinketeer'), Js('Toolcraft'), Js('Trader'), Js('Trinketeer'), Js('Trooper'), Js('Veteran'), Js('Vigilante'), Js('Ward'), Js('Warden'), Js('Warrior'), Js('Weaponsmith'), Js('Wizard'), Js('Wright')]))
pass
pass


# Add lib to the module scope
mgtDwarfs = var.to_python()
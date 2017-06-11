__all__ = ['mgtOrcs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm1b', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    while PyJsStrictEq(var.get('nm9').get(var.get('rnd')),var.get('nm10').get(var.get('rnd3'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    while PyJsStrictEq(var.get('nm11').get(var.get('rnd5')),var.get('nm10').get(var.get('rnd3'))):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((var.get('nm9').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        while PyJsStrictEq(var.get('nm12').get(var.get('rnd')),var.get('nm13').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('names', (((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+Js(' '))+var.get('nm14').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('names', ((var.get('nm15').get(var.get('rnd'))+Js(' '))+var.get('nm14').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1b').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        while PyJsStrictEq(var.get('nm1b').get(var.get('rnd5')),var.get('nm4').get(var.get('rnd7'))):
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd8')))+var.get('nm1b').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd7'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        while PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm7').get(var.get('rnd'))):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', ((((var.get('nm7').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        while PyJsStrictEq(var.get('nm12').get(var.get('rnd')),var.get('nm13').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('names', (((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+Js(' '))+var.get('nm14').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('names', ((var.get('nm15').get(var.get('rnd'))+Js(' '))+var.get('nm14').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm1b', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('q'), Js('r'), Js('z')]))
var.put('nm4', Js([Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm5', Js([Js("'"), Js('-')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('ua'), Js('uu'), Js('aa'), Js('au'), Js('ao'), Js('ia'), Js('ou')]))
var.put('nm7', Js([Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gr'), Js('gn'), Js('k'), Js('kn'), Js('kr'), Js('m'), Js('n'), Js('s'), Js('st'), Js('t'), Js('tr'), Js('v'), Js('z'), Js('zh')]))
var.put('nm8', Js([Js('c'), Js('cr'), Js('cd'), Js('d'), Js('dr'), Js('dg'), Js('dk'), Js('g'), Js('gr'), Js('gn'), Js('gd'), Js('gz'), Js('k'), Js('kr'), Js('kd'), Js('kv'), Js('kz'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('ng'), Js('nd'), Js('q'), Js('qr'), Js('r'), Js('rr'), Js('rk'), Js('rz'), Js('rv'), Js('rd'), Js('rg'), Js('z'), Js('zk'), Js('zr'), Js('zz')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z')]))
var.put('nm10', Js([Js('d'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm11', Js([Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm12', Js([Js('alder'), Js('ash'), Js('bane'), Js('black'), Js('blood'), Js('boulder'), Js('brass'), Js('bronze'), Js('cinder'), Js('dark'), Js('dawn'), Js('dead'), Js('death'), Js('doom'), Js('dust'), Js('ember'), Js('fire'), Js('flame'), Js('gloom'), Js('haze'), Js('heavy'), Js('hell'), Js('iron'), Js('keen'), Js('lone'), Js('molten'), Js('mourn'), Js('nether'), Js('proud'), Js('rage'), Js('rapid'), Js('rough'), Js('scream'), Js('shadow'), Js('sharp'), Js('silent'), Js('skull'), Js('slate'), Js('steel'), Js('stern'), Js('stone'), Js('storm'), Js('swift'), Js('thunder'), Js('void'), Js('war'), Js('wild')]))
var.put('nm13', Js([Js('bane'), Js('bellow'), Js('blade'), Js('blaze'), Js('blood'), Js('bone'), Js('brace'), Js('brand'), Js('brow'), Js('burn'), Js('claw'), Js('cleave'), Js('crest'), Js('cut'), Js('doom'), Js('eye'), Js('fang'), Js('fist'), Js('flaw'), Js('force'), Js('forge'), Js('fury'), Js('gaze'), Js('gloom'), Js('grip'), Js('growl'), Js('hand'), Js('heart'), Js('keep'), Js('mane'), Js('mantle'), Js('mark'), Js('maul'), Js('maw'), Js('mourn'), Js('rage'), Js('reach'), Js('ridge'), Js('run'), Js('scar'), Js('shade'), Js('shard'), Js('spark'), Js('stalk'), Js('stride'), Js('surge'), Js('sworn'), Js('thorn')]))
var.put('nm14', Js([Js('Artificer'), Js('Artisan'), Js('Assailant'), Js('Assassin'), Js('Barbarian'), Js('Bigwig'), Js('Brawler'), Js('Bruiser'), Js('Brute'), Js('Cannoneer'), Js('Captain'), Js('Chief'), Js('Colonist'), Js('Conscript'), Js('Enforcer'), Js('Executioner'), Js('Fanatic'), Js('General'), Js('Gladiator'), Js('Healer'), Js('Horde'), Js('Hordechief'), Js('Hunter'), Js('Looter'), Js('Lumberjack'), Js('Maniac'), Js('Marauder'), Js('Mechanic'), Js('Mercenary'), Js('Militant'), Js('Operative'), Js('Orc'), Js('Outlaw'), Js('Overlord'), Js('Overseer'), Js('Paratrooper'), Js('Patrol'), Js('Pillager'), Js('Pioneer'), Js('Raider'), Js('Ravager'), Js('Recruit'), Js('Rider'), Js('Roughrider'), Js('Sadist'), Js('Savage'), Js('Scout'), Js('Settler'), Js('Shaman'), Js('Slayer'), Js('Soldier'), Js('Spy'), Js('Technician'), Js('Vanguard'), Js('Veteran'), Js('Warbringer'), Js('Warlord'), Js('Warmonger'), Js('Watcher'), Js('Zealot')]))
var.put('nm15', Js([Js('Acclaimed'), Js('Aggressive'), Js('Agitated'), Js('Ambush'), Js('Angry'), Js('Anguished'), Js('Battle'), Js('Bellowing'), Js('Bitter'), Js('Blind'), Js('Broken'), Js('Brutal'), Js('Careless'), Js('Corrupt'), Js('Corrupted'), Js('Crazed'), Js('Crazy'), Js('Cruel'), Js('Daring'), Js('Defiant'), Js('Delirious'), Js('Devoted'), Js('Diligent'), Js('Disguised'), Js('Dutiful'), Js('Eager'), Js('Enraged'), Js('Fearless'), Js('Forsaken'), Js('Gleeful'), Js('Grave'), Js('Grim'), Js('Grumpy'), Js('Idle'), Js('Insane'), Js('Ire'), Js('Jealous'), Js('Mad'), Js('Merciless'), Js('Monstrous'), Js('Obedient'), Js('Pitiless'), Js('Powerful'), Js('Proud'), Js('Puzzled'), Js('Raging'), Js('Rash'), Js('Reckless'), Js('Sadistic'), Js('Shady'), Js('Stark'), Js('Swift'), Js('Terrifying'), Js('Thick'), Js('Trifling'), Js('Unfit'), Js('Unwilling'), Js('Vengeful'), Js('Vicious'), Js('Villainous'), Js('Violent'), Js('Wicked'), Js('Wild'), Js('Wretched')]))
pass
pass


# Add lib to the module scope
mgtOrcs = var.to_python()
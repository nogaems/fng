__all__ = ['mgtOgre']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('lName', ((var.get('nm5').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd8'))))
                else:
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd9')),var.get('nm5').get(var.get('rnd6'))):
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('lName', ((((var.get('nm5').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm6').get(var.get('rnd8'))))
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+Js(' '))+var.get('lName')))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd4')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd3')))+Js(' '))+var.get('lName')))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    while PyJsStrictEq(var.get('nm7').get(var.get('rnd')),var.get('nm8').get(var.get('rnd2'))):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('names', (((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+Js(' '))+var.get('nm9').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('names', ((var.get('nm10').get(var.get('rnd'))+Js(' '))+var.get('nm9').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('g'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('uo'), Js('uu'), Js('ua'), Js('ou'), Js('au'), Js('aa')]))
var.put('nm3', Js([Js('d'), Js('dd'), Js('dg'), Js('dr'), Js('g'), Js('gr'), Js('gg'), Js('gd'), Js('gz'), Js('gv'), Js('k'), Js('kk'), Js('kd'), Js('kz'), Js('kv'), Js('kr'), Js('lk'), Js('lg'), Js('lkr'), Js('lz'), Js('ldr'), Js('lg'), Js('lgr'), Js('ng'), Js('ngr'), Js('nd'), Js('ndr'), Js('nr'), Js('r'), Js('rd'), Js('rb'), Js('rk'), Js('rz'), Js('rg'), Js('rgr'), Js('rg'), Js('rkr'), Js('rn'), Js('rz'), Js('sg'), Js('sgr'), Js('z'), Js('zc'), Js('zcr'), Js('zd'), Js('zg'), Js('zgr'), Js('zk'), Js('zkr')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('n'), Js('r'), Js('t'), Js('th')]))
var.put('nm6', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('n'), Js('r'), Js('s')]))
var.put('nm7', Js([Js('amber'), Js('ash'), Js('battle'), Js('blaze'), Js('blood'), Js('bone'), Js('boulder'), Js('burn'), Js('burning'), Js('cinder'), Js('dark'), Js('dead'), Js('death'), Js('doom'), Js('ember'), Js('fire'), Js('flame'), Js('fuse'), Js('gloom'), Js('gore'), Js('grim'), Js('grizzly'), Js('hell'), Js('hollow'), Js('molten'), Js('mourn'), Js('nether'), Js('poison'), Js('pyre'), Js('rage'), Js('rough'), Js('rumble'), Js('saur'), Js('saw'), Js('serpent'), Js('shade'), Js('shadow'), Js('skull'), Js('slate'), Js('slaughter'), Js('stone'), Js('storm'), Js('thunder'), Js('titan'), Js('twilight'), Js('void'), Js('war'), Js('wild')]))
var.put('nm8', Js([Js('bane'), Js('belly'), Js('blade'), Js('blaze'), Js('blight'), Js('blood'), Js('bone'), Js('breath'), Js('chewer'), Js('cleaver'), Js('crest'), Js('crusher'), Js('curse'), Js('doom'), Js('eye'), Js('eyes'), Js('fall'), Js('field'), Js('fire'), Js('flame'), Js('flayer'), Js('force'), Js('forge'), Js('fury'), Js('gaze'), Js('gazer'), Js('gloom'), Js('hell'), Js('hole'), Js('house'), Js('howl'), Js('lash'), Js('limb'), Js('mourn'), Js('rage'), Js('reaper'), Js('reaver'), Js('ripper'), Js('roar'), Js('scar'), Js('stride'), Js('tooth')]))
var.put('nm9', Js([Js('Aggressor'), Js('Annihilator'), Js('Arsonist'), Js('Assassin'), Js('Barbarian'), Js('Battler'), Js('Berserker'), Js('Bleeder'), Js('Bouncer'), Js('Brawler'), Js('Bruiser'), Js('Brute'), Js('Bully'), Js('Champion'), Js('Charmer'), Js('Contender'), Js('Destroyer'), Js('Diabolist'), Js('Dragger'), Js('Enforcer'), Js('Eradicator'), Js('Fighter'), Js('Flailer'), Js('Freebooter'), Js('Gatecrasher'), Js('Gladiator'), Js('Guardian'), Js('Heavy'), Js('Hireling'), Js('Hulk'), Js('Invader'), Js('Maniac'), Js('Marauder'), Js('Mercenary'), Js('Oaf'), Js('Ogre'), Js('Oozer'), Js('Outlaw'), Js('Pillager'), Js('Pummeler'), Js('Pyromaniac'), Js('Rager'), Js('Raider'), Js('Renegade'), Js('Savage'), Js('Scrapper'), Js('Sentry'), Js('Shaman'), Js('Slugger'), Js('Slumlord'), Js('Tanker'), Js('Taskmaster'), Js('Tyrant'), Js('Vandal'), Js('Warbrute'), Js('Ward'), Js('Warlord'), Js('Warrior'), Js('Wildcat'), Js('Wrecker')]))
var.put('nm10', Js([Js('Aggravated'), Js('Aggressive'), Js('Agitated'), Js('Angry'), Js('Anguished'), Js('Barrage'), Js('Bitter'), Js('Blissful'), Js('Blood'), Js('Bloodthirsty'), Js('Bold'), Js('Bossy'), Js('Bruised'), Js('Careless'), Js('Colossal'), Js('Corrupt'), Js('Corrupted'), Js('Crazed'), Js('Crooked'), Js('Cruel'), Js('Crypt'), Js('Defiant'), Js('Delirious'), Js('Drooling'), Js('Energetic'), Js('Enormous'), Js('Enraged'), Js('Exhausted'), Js('Fearless'), Js('Foolish'), Js('Forsaken'), Js('Frenzied'), Js('Frightening'), Js('Grave'), Js('Greedy'), Js('Grim'), Js('Heartless'), Js('Hulking'), Js('Hungry'), Js('Husky'), Js('Idle'), Js('Infernal'), Js('Insane'), Js('Jumbo'), Js('Limping'), Js('Livid'), Js('Lone'), Js('Mad'), Js('Marsh'), Js('Mausoleum'), Js('Menacing'), Js('Monstrous'), Js('Noxious'), Js('Rash'), Js('Reckless'), Js('Robust'), Js('Savage'), Js('Shady'), Js('Tomb'), Js('Tough'), Js('Towering'), Js('Treasonous'), Js('Vengeful'), Js('Vicious'), Js('Villainous'), Js('Vindictive'), Js('Violent'), Js('Wicked'), Js('Wild'), Js('Wrathful'), Js('Wrecking'), Js('Wretched')]))
pass
pass


# Add lib to the module scope
mgtOgre = var.to_python()
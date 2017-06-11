__all__ = ['mgtGoblins']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(8.0)):
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+Js('-'))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm2').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3')))+Js('-'))+var.get('nm2').get(var.get('rnd')))+var.get('nm3').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                while PyJsStrictEq(var.get('nm9').get(var.get('rnd')),var.get('nm10').get(var.get('rnd2'))):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('names', (((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+Js(' '))+var.get('nm11').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('g'), Js('k'), Js('m'), Js('n'), Js('t'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('g'), Js('gg'), Js('k'), Js('kk'), Js('n'), Js('ng'), Js('sh'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('k'), Js('m'), Js('n'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('kr'), Js('sk'), Js('sl'), Js('sq'), Js('tr'), Js('t'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm7', Js([Js('b'), Js('bz'), Js('d'), Js('dz'), Js('dv'), Js('gr'), Js('gg'), Js('gn'), Js('gq'), Js('kr'), Js('kn'), Js('kz'), Js('kq'), Js('lk'), Js('lq'), Js('mz'), Js('mk'), Js('mg'), Js('nk'), Js('nz'), Js('nv'), Js('qv'), Js('qz'), Js('qr'), Js('rg'), Js('rl'), Js('rv'), Js('rz'), Js('zr'), Js('zl'), Js('zz')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('kk'), Js('k'), Js('rt'), Js('rd'), Js('sk'), Js('t'), Js('x')]))
var.put('nm9', Js([Js('adder'), Js('alder'), Js('ash'), Js('asp'), Js('beetle'), Js('blister'), Js('boar'), Js('bone'), Js('cask'), Js('claw'), Js('coal'), Js('dew'), Js('dust'), Js('earth'), Js('ember'), Js('face'), Js('feather'), Js('fern'), Js('fire'), Js('fist'), Js('flame'), Js('flint'), Js('frog'), Js('frost'), Js('fuse'), Js('gem'), Js('goat'), Js('grass'), Js('hearh'), Js('heart'), Js('ice'), Js('iron'), Js('knuckle'), Js('lava'), Js('leaf'), Js('locust'), Js('marble'), Js('moss'), Js('mud'), Js('nettle'), Js('oat'), Js('orb'), Js('peach'), Js('pebble'), Js('pine'), Js('pyre'), Js('rock'), Js('sheep'), Js('slate'), Js('snake'), Js('spider'), Js('spike'), Js('spit'), Js('steam'), Js('sting'), Js('stink'), Js('thistle'), Js('toad'), Js('tusk'), Js('vine'), Js('wood')]))
var.put('nm10', Js([Js('back'), Js('basher'), Js('belly'), Js('blade'), Js('blower'), Js('bone'), Js('brawler'), Js('breaker'), Js('breath'), Js('brow'), Js('button'), Js('chaser'), Js('dancer'), Js('drifter'), Js('fall'), Js('fang'), Js('fire'), Js('fist'), Js('flare'), Js('flinger'), Js('flogger'), Js('fright'), Js('fume'), Js('gazer'), Js('glider'), Js('guard'), Js('hunter'), Js('jumper'), Js('keeper'), Js('limbs'), Js('mantle'), Js('mark'), Js('napper'), Js('palm'), Js('rider'), Js('ripper'), Js('runner'), Js('scourger'), Js('seeker'), Js('shot'), Js('singer'), Js('speaker'), Js('splitter'), Js('sprinter'), Js('staff'), Js('stalker'), Js('stand'), Js('step'), Js('stick'), Js('striker'), Js('taker'), Js('thorn'), Js('tosser'), Js('trapper'), Js('tusk'), Js('vaulter'), Js('walker'), Js('watcher'), Js('wave'), Js('weaver'), Js('wild'), Js('wilde')]))
var.put('nm11', Js([Js('Assassin'), Js('Bandit'), Js('Blaster'), Js('Bomber'), Js('Boss'), Js('Brigade'), Js('Buffoon'), Js('Bully'), Js('Butcher'), Js('Cohort'), Js('Commander'), Js('Commando'), Js('Conscript'), Js('Crackshot'), Js('Crew'), Js('Cultist'), Js('Daredevil'), Js('Dealer'), Js('Enforcer'), Js('Engineer'), Js('Explorer'), Js('Fanatic'), Js('Goblin'), Js('Gorger'), Js('Grappler'), Js('Grenadier'), Js('Grunt'), Js('Grunts'), Js('Guide'), Js('Handler'), Js('Harasser'), Js('Hermit'), Js('Hero'), Js('Hobgoblin'), Js('Hooligan'), Js('Hopper'), Js('Hunter'), Js('Initiate'), Js('Instigator'), Js('Jailer'), Js('Jocker'), Js('Kaboomist'), Js('Legionnaire'), Js('Lookout'), Js('Machinist'), Js('Maniac'), Js('Marauder'), Js('Marshal'), Js('Mason'), Js('Matron'), Js('Medic'), Js('Mob Boss'), Js('Mountaineer'), Js('Mutant'), Js('Outlander'), Js('Outrider'), Js('Patrol'), Js('Piker'), Js('Pilferer'), Js('Prospector'), Js('Psychopath'), Js('Punisher'), Js('Pyromancer'), Js('Rackateer'), Js('Raider'), Js('Recruiter'), Js('Rider'), Js('Ringleader'), Js('Roughrider'), Js('Ruffian'), Js('Runner'), Js('Sapper'), Js('Scout'), Js('Scrapper'), Js('Sentry'), Js('Sergeant'), Js('Settler'), Js('Shaman'), Js('Shortcutter'), Js('Sky Raider'), Js('Skycutter'), Js('Sledder'), Js('Snitch'), Js('Soothsayer'), Js('Spelunker'), Js('Spy'), Js('Squad'), Js('Striker'), Js('Tactician'), Js('Taskmaster'), Js('Tinkerer'), Js('Trader'), Js('Tunneler'), Js('Turncoat'), Js('Underling'), Js('Underminer'), Js('Vandal'), Js('Warchief'), Js('Warden'), Js('Wardriver'), Js('Welder'), Js('Witch'), Js('Wizard')]))
pass
pass


# Add lib to the module scope
mgtGoblins = var.to_python()
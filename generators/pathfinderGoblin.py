__all__ = ['pathfinderGoblin']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            if PyJsStrictEq(var.get('tp'),Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('names', (var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    if (var.get('i')<Js(6.0)):
                        var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(4.0)):
                        while (var.get('rnd')<Js(4.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        while (var.get('rnd5')<Js(5.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                        else:
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('dr'), Js('fl'), Js('g'), Js('gh'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('oo'), Js('ou'), Js('oa')]))
var.put('nm3', Js([Js('bb'), Js('bbl'), Js('bm'), Js('br'), Js('bn'), Js('bz'), Js('d'), Js('dd'), Js('dr'), Js('dz'), Js('dg'), Js('ff'), Js('g'), Js('ggl'), Js('gm'), Js('gn'), Js('gt'), Js('gv'), Js('gb'), Js('gd'), Js('m'), Js('md'), Js('mb'), Js('mz'), Js('mg'), Js('mk'), Js('nth'), Js('nz'), Js('nd'), Js('ng'), Js('ngb'), Js('ngl'), Js('nd'), Js('nv'), Js('rg'), Js('rk'), Js('rp'), Js('rs'), Js('rt'), Js('rd'), Js('rg'), Js('tf'), Js('tv'), Js('tt'), Js('tg'), Js('v'), Js('vg'), Js('vd'), Js('vn'), Js('vm')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ff'), Js('g'), Js('k'), Js('n'), Js('nk'), Js('rch'), Js('rd'), Js('rg'), Js('rk'), Js('rnk'), Js('rt'), Js('s'), Js('sh'), Js('t'), Js('wg'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('f'), Js('g'), Js('gh'), Js('gr'), Js('h'), Js('j'), Js('kl'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('v'), Js('vr'), Js('y'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('e'), Js('i'), Js('o'), Js('ee'), Js('ie'), Js('oo')]))
var.put('nm7', Js([Js('ck'), Js('dl'), Js('dg'), Js('dr'), Js('dn'), Js('dk'), Js('g'), Js('gl'), Js('gn'), Js('gm'), Js('gl'), Js('k'), Js('kk'), Js('kl'), Js('kn'), Js('km'), Js('kch'), Js('kt'), Js('lk'), Js('ld'), Js('lg'), Js('lv'), Js('lb'), Js('ll'), Js('mb'), Js('ml'), Js('mp'), Js('md'), Js('mk'), Js('mr'), Js('nb'), Js('nch'), Js('nd'), Js('ng'), Js('nk'), Js('p'), Js('ph'), Js('phr'), Js('phl'), Js('rk'), Js('rg'), Js('rd'), Js('rb'), Js('rbl'), Js('s'), Js('sh'), Js('ss'), Js('sk'), Js('st'), Js('t'), Js('tr'), Js('tl'), Js('tch'), Js('vv'), Js('x')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('h'), Js('l'), Js('k'), Js('n'), Js('ns'), Js('ms'), Js('s'), Js('sh'), Js('th')]))
var.put('nm9', Js([Js('Amber'), Js('Ash'), Js('Bear'), Js('Blade'), Js('Blood'), Js('Bone'), Js('Boulder'), Js('Cask'), Js('Claw'), Js('Crag'), Js('Crow'), Js('Crystal'), Js('Dead'), Js('Dew'), Js('Dog'), Js('Doom'), Js('Ear'), Js('Earth'), Js('Elf'), Js('Ember'), Js('Far'), Js('Finger'), Js('Fire'), Js('Fist'), Js('Flame'), Js('Flint'), Js('Forest'), Js('Frost'), Js('Fuse'), Js('Gloom'), Js('Gold'), Js('Gore'), Js('Grass'), Js('Gut'), Js('Hallow'), Js('Hard'), Js('Haze'), Js('Heart'), Js('Heavy'), Js('Hell'), Js('High'), Js('Hill'), Js('Hog'), Js('Horse'), Js('Ice'), Js('Iron'), Js('Keen'), Js('Long'), Js('Man'), Js('Marble'), Js('Marsh'), Js('Meadow'), Js('Moon'), Js('Moss'), Js('Nettle'), Js('Nose'), Js('Orb'), Js('Pine'), Js('Plain'), Js('Poke'), Js('Rage'), Js('Rain'), Js('Raven'), Js('Rip'), Js('River'), Js('Rock'), Js('Rough'), Js('Shadow'), Js('Silver'), Js('Skull'), Js('Snake'), Js('Snow'), Js('Spider'), Js('Stab'), Js('Star'), Js('Steel'), Js('Stern'), Js('Stone'), Js('Storm'), Js('Strong'), Js('Stump'), Js('Swamp'), Js('Toe'), Js('Tree'), Js('Water'), Js('Wild'), Js('Wind'), Js('Wold'), Js('Wood')]))
var.put('nm10', Js([Js('bane'), Js('bash'), Js('basher'), Js('belly'), Js('bender'), Js('binder'), Js('bite'), Js('biter'), Js('blazer'), Js('bleeder'), Js('blight'), Js('brace'), Js('brand'), Js('breaker'), Js('breath'), Js('brew'), Js('brook'), Js('brow'), Js('bumper'), Js('caller'), Js('chaser'), Js('chew'), Js('chewer'), Js('chopper'), Js('cleaver'), Js('cooker'), Js('crag'), Js('crest'), Js('crusher'), Js('cut'), Js('cutter'), Js('dancer'), Js('draft'), Js('dreamer'), Js('dust'), Js('eye'), Js('fall'), Js('fang'), Js('flaw'), Js('flayer'), Js('force'), Js('fury'), Js('gloom'), Js('grip'), Js('gripper'), Js('guard'), Js('gut'), Js('hammerer'), Js('horn'), Js('hunter'), Js('jumper'), Js('killer'), Js('lasher'), Js('mark'), Js('mauler'), Js('maw'), Js('more'), Js('nugget'), Js('part'), Js('parts'), Js('pike'), Js('punch'), Js('puncher'), Js('rage'), Js('rager'), Js('reaper'), Js('reaver'), Js('rip'), Js('ripper'), Js('roar'), Js('rock'), Js('scar'), Js('scream'), Js('seeker'), Js('shard'), Js('shield'), Js('shooter'), Js('shot'), Js('singer'), Js('slaver'), Js('slayer'), Js('snacker'), Js('snarl'), Js('snouth'), Js('spark'), Js('spear'), Js('splitter'), Js('stalk'), Js('stalker'), Js('steel'), Js('stick'), Js('stomper'), Js('strike'), Js('striker'), Js('surge'), Js('taker'), Js('tracker'), Js('trapper'), Js('wad'), Js('walker'), Js('watcher'), Js('wound')]))
pass
pass


# Add lib to the module scope
pathfinderGoblin = var.to_python()
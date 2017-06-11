__all__ = ['warhammerWarriorsOfChaos']

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
            if PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                while PyJsStrictEq(var.get('nm8').get(var.get('rnd')),var.get('nm9').get(var.get('rnd2'))):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('lName', (var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('lName', (Js('the ')+var.get('nm10').get(var.get('rnd'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('lName')))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('lName')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(6.0)):
                    if (var.get('rnd')<Js(3.0)):
                        while (var.get('rnd5')<Js(2.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('d'), Js('dr'), Js('dj'), Js('f'), Js('fr'), Js('g'), Js('gr'), Js('gh'), Js('k'), Js('kh'), Js('kr'), Js('m'), Js('r'), Js('s'), Js('sc'), Js('sr'), Js('sk'), Js('sz'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('w')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ao'), Js('au'), Js('oa'), Js('ay')]))
var.put('nm3', Js([Js('d'), Js('gg'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('r'), Js('rr'), Js('z'), Js('zh'), Js('zz'), Js('d'), Js('gg'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('r'), Js('rr'), Js('z'), Js('zh'), Js('zz'), Js('d'), Js('gg'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('r'), Js('rr'), Js('z'), Js('zh'), Js('zz'), Js('d'), Js('gg'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('r'), Js('rr'), Js('z'), Js('zh'), Js('zz'), Js('d'), Js('dr'), Js('dz'), Js('gv'), Js('gg'), Js('gr'), Js('gn'), Js('gtr'), Js('gz'), Js('k'), Js('kr'), Js('kz'), Js('kh'), Js('ktr'), Js('kth'), Js('kx'), Js('l'), Js('lr'), Js('lfr'), Js('lvr'), Js('lv'), Js('lg'), Js('lgr'), Js('ld'), Js('ldr'), Js('m'), Js('mk'), Js('mkr'), Js('mz'), Js('mv'), Js('mvr'), Js('r'), Js('rr'), Js('rx'), Js('rz'), Js('rzr'), Js('rk'), Js('rkh'), Js('rch'), Js('rgh'), Js('rb'), Js('sz'), Js('str'), Js('sgr'), Js('sg'), Js('sk'), Js('skr'), Js('st'), Js('sht'), Js('shtr'), Js('shk'), Js('szh'), Js('z'), Js('zh'), Js('zz'), Js('zr')]))
var.put('nm4', Js([Js(''), Js(''), Js('b'), Js('ch'), Js('k'), Js('l'), Js('lk'), Js('ld'), Js('n'), Js('nd'), Js('r'), Js('rd'), Js('rk'), Js('rt'), Js('rr'), Js('s'), Js('sk'), Js('t'), Js('tts'), Js('tch'), Js('x')]))
var.put('nm5', Js([Js('bh'), Js('br'), Js('d'), Js('dh'), Js('f'), Js('fr'), Js('fh'), Js('g'), Js('gh'), Js('gr'), Js('kh'), Js('kr'), Js('k'), Js('m'), Js('mh'), Js('n'), Js('nh'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('sl'), Js('sm'), Js('sn'), Js('st'), Js('sth'), Js('t'), Js('th'), Js('thr'), Js('tr'), Js('v'), Js('vh'), Js('vr'), Js('w'), Js('wh')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('a'), Js('a'), Js('ia'), Js('ea'), Js('ae')]))
var.put('nm7', Js([Js('d'), Js('g'), Js('gg'), Js('gh'), Js('k'), Js('kk'), Js('kh'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('z'), Js('zh'), Js('zz'), Js('d'), Js('g'), Js('gg'), Js('gh'), Js('k'), Js('kk'), Js('kh'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('z'), Js('zh'), Js('zz'), Js('d'), Js('g'), Js('gg'), Js('gh'), Js('k'), Js('kk'), Js('kh'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('z'), Js('zh'), Js('zz'), Js('d'), Js('dj'), Js('dn'), Js('fr'), Js('fg'), Js('gg'), Js('g'), Js('gr'), Js('gh'), Js('gn'), Js('gm'), Js('gz'), Js('k'), Js('kk'), Js('kn'), Js('kh'), Js('kr'), Js('kz'), Js('kt'), Js('kth'), Js('l'), Js('ll'), Js('lr'), Js('lx'), Js('lt'), Js('lth'), Js('ln'), Js('lk'), Js('m'), Js('mm'), Js('mn'), Js('mr'), Js('mv'), Js('mz'), Js('mk'), Js('nk'), Js('ng'), Js('nm'), Js('nr'), Js('nth'), Js('nz'), Js('nv'), Js('r'), Js('rr'), Js('rth'), Js('rsh'), Js('rz'), Js('rzh'), Js('rl'), Js('rc'), Js('rch'), Js('s'), Js('ss'), Js('sz'), Js('sh'), Js('shz'), Js('shn'), Js('sq'), Js('shq'), Js('sht'), Js('shtr'), Js('szh'), Js('z'), Js('zz'), Js('zh'), Js('zn'), Js('zhn')]))
var.put('nm8', Js([Js('amber'), Js('battle'), Js('bitter'), Js('black'), Js('blaze'), Js('blazing'), Js('blood'), Js('burn'), Js('burning'), Js('chaos'), Js('cinder'), Js('daemon'), Js('dark'), Js('dead'), Js('death'), Js('demon'), Js('doom'), Js('ember'), Js('fiery'), Js('fire'), Js('flame'), Js('fuse'), Js('gloom'), Js('haze'), Js('hell'), Js('moon'), Js('nether'), Js('night'), Js('pyre'), Js('rage'), Js('rot'), Js('shade'), Js('shadow'), Js('silent'), Js('storm'), Js('sun'), Js('thunder'), Js('twice'), Js('void'), Js('wild'), Js('wraith'), Js('wrath')]))
var.put('nm9', Js([Js('bane'), Js('bash'), Js('blaze'), Js('blight'), Js('bone'), Js('born'), Js('bound'), Js('breath'), Js('buster'), Js('chaser'), Js('cleaver'), Js('eater'), Js('fall'), Js('fang'), Js('fire'), Js('flame'), Js('flare'), Js('flaw'), Js('force'), Js('forge'), Js('forged'), Js('fury'), Js('gaze'), Js('guard'), Js('gut'), Js('hand'), Js('heart'), Js('lash'), Js('mark'), Js('marked'), Js('might'), Js('more'), Js('mourn'), Js('rage'), Js('reaper'), Js('reaver'), Js('scar'), Js('scream'), Js('seeker'), Js('shade'), Js('shadow'), Js('shard'), Js('spawn'), Js('spawned'), Js('spew'), Js('spit'), Js('strength'), Js('stride'), Js('sunder'), Js('surge'), Js('sworn'), Js('wrath')]))
var.put('nm10', Js([Js('Abandoned'), Js('Aggressor'), Js('Anguished'), Js('Beast'), Js('Befouled'), Js('Behemoth'), Js('Berserker'), Js('Bewitched'), Js('Blood Bathed'), Js('Blood Soaked'), Js('Bloodied'), Js('Bloody'), Js('Bone Crusher'), Js('Corrupted Mind'), Js('Corruption Lord'), Js('Corruptor'), Js('Crooked Smile'), Js('Cunning'), Js('Cunning Mind'), Js('Curseling'), Js('Dark Lord'), Js('Dark Master'), Js('Dark Night'), Js('Dead Mind'), Js('Defiled'), Js('Dread Lord'), Js('Eternal'), Js('Everchosen'), Js('Explosive'), Js('Faithless'), Js('Forsaken'), Js('Fury'), Js('Gory'), Js('Grave Digger'), Js('Grave Robber'), Js('Grim Reaper'), Js('Grotesque'), Js('Hollow'), Js('Hound'), Js('Ill Tempered'), Js('Impure'), Js('Insane'), Js('Irrational'), Js('Jester'), Js('Leechlord'), Js('Lone Wolf'), Js('Lost Mind'), Js('Magnificent'), Js('Mammoth'), Js('Maneater'), Js('Manslayer'), Js('Menace'), Js('Merciless'), Js('Mutant'), Js('Necromancer'), Js('Nightmare'), Js('Nomad'), Js('Parasite'), Js('Pollutor'), Js('Rash'), Js('Roamer'), Js('Rotten'), Js('Rotting'), Js('Sanguine'), Js('Sanguine Lord'), Js('Serpent'), Js('Serpent Tongue'), Js('Shadow Dweller'), Js('Sinner'), Js('Skeptic'), Js('Skinner'), Js('Slaughterer'), Js('Soothsayer'), Js('Suneater'), Js('Transient'), Js('Unstable'), Js('Vagrant'), Js('Vengeful'), Js('Volatile'), Js('Wanderer'), Js('Warmonger'), Js('Wicked'), Js('Wrathful'), Js('Wreckage'), Js('Wretched')]))
pass
pass


# Add lib to the module scope
warhammerWarriorsOfChaos = var.to_python()
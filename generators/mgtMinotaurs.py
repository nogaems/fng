__all__ = ['mgtMinotaurs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        while PyJsStrictEq(var.get('nm8').get(var.get('rnd')),var.get('nm9').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('names', (((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+Js(' '))+var.get('nm10').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('names', ((var.get('nm11').get(var.get('rnd'))+Js(' '))+var.get('nm10').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        while PyJsStrictEq(var.get('nm8').get(var.get('rnd')),var.get('nm9').get(var.get('rnd2'))):
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('names', (((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+Js(' '))+var.get('nm10').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('names', ((var.get('nm11').get(var.get('rnd'))+Js(' '))+var.get('nm10').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('n'), Js('q'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('i'), Js('e'), Js('a'), Js('o'), Js('u'), Js('aa'), Js('au'), Js('uu')]))
var.put('nm3', Js([Js('dr'), Js('dg'), Js('dv'), Js('hg'), Js('hn'), Js('hnd'), Js('hrg'), Js('hrd'), Js('hlg'), Js('hln'), Js('hld'), Js('hng'), Js('ng'), Js('nd'), Js('ndr'), Js('ngr'), Js('nr'), Js('nz'), Js('nv'), Js('ntr'), Js('qr'), Js('qn'), Js('ql'), Js('rc'), Js('rd'), Js('rdr'), Js('rg'), Js('rgr'), Js('rk'), Js('rq'), Js('sc'), Js('scr'), Js('sdr'), Js('skr'), Js('sq'), Js('sqr'), Js('st'), Js('str'), Js('tg'), Js('tgr'), Js('tk'), Js('tkr'), Js('tr'), Js('vd'), Js('vg'), Js('vgr'), Js('vdr'), Js('vr'), Js('zg'), Js('zr'), Js('zq')]))
var.put('nm4', Js([Js('d'), Js('dh'), Js('g'), Js('k'), Js('q'), Js('qt'), Js('qth'), Js('r'), Js('rk'), Js('rd'), Js('rq'), Js('rt'), Js('rth'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('u'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ee'), Js('uu'), Js('ue'), Js('eu'), Js('au')]))
var.put('nm7', Js([Js('b'), Js('bb'), Js('br'), Js('d'), Js('dd'), Js('dn'), Js('dr'), Js('g'), Js('gg'), Js('gd'), Js('gn'), Js('gr'), Js('gv'), Js('gz'), Js('k'), Js('kk'), Js('kn'), Js('kr'), Js('kz'), Js('ld'), Js('lg'), Js('lr'), Js('lz'), Js('nd'), Js('ng'), Js('nr'), Js('nv'), Js('nz'), Js('q'), Js('qr'), Js('qn'), Js('r'), Js('rr'), Js('rb'), Js('rd'), Js('rg'), Js('rgr'), Js('rq'), Js('rs'), Js('tv'), Js('rz'), Js('sc'), Js('sg'), Js('sk'), Js('sq'), Js('sr'), Js('sqr'), Js('sz'), Js('szr'), Js('t'), Js('tg'), Js('tr'), Js('thr'), Js('thn'), Js('thg'), Js('zc'), Js('zg'), Js('zk'), Js('zl'), Js('zr')]))
var.put('nm8', Js([Js('amber'), Js('ash'), Js('battle'), Js('bitter'), Js('blade'), Js('blaze'), Js('blood'), Js('cinder'), Js('cruel'), Js('dark'), Js('dead'), Js('death'), Js('doom'), Js('elder'), Js('ember'), Js('end'), Js('fall'), Js('fel'), Js('fire'), Js('flame'), Js('flare'), Js('fright'), Js('furor'), Js('fury'), Js('gloom'), Js('gore'), Js('grim'), Js('haze'), Js('hell'), Js('mad'), Js('mourn'), Js('nether'), Js('pain'), Js('pyre'), Js('rage'), Js('rough'), Js('ruin'), Js('scorch'), Js('shade'), Js('shadow'), Js('skull'), Js('storm'), Js('taint'), Js('tinder'), Js('war'), Js('wild')]))
var.put('nm9', Js([Js('bane'), Js('bellow'), Js('binder'), Js('blade'), Js('blaze'), Js('blood'), Js('breaker'), Js('bringer'), Js('caller'), Js('chanter'), Js('crest'), Js('doom'), Js('drifter'), Js('fall'), Js('fang'), Js('fist'), Js('flayer'), Js('force'), Js('forge'), Js('fury'), Js('guard'), Js('haze'), Js('hide'), Js('horn'), Js('hunter'), Js('mane'), Js('mantle'), Js('maul'), Js('maw'), Js('might'), Js('monger'), Js('mourn'), Js('rage'), Js('reaper'), Js('reaver'), Js('rider'), Js('ripper'), Js('roar'), Js('runner'), Js('shade'), Js('shadow'), Js('shot'), Js('slayer'), Js('stalker'), Js('stride'), Js('strider'), Js('strike'), Js('striker'), Js('surge'), Js('sworn')]))
var.put('nm10', Js([Js('Aggressor'), Js('Ancestor'), Js('Assailant'), Js('Bodyguard'), Js('Brawler'), Js('Bruiser'), Js('Butcher'), Js('Cerberus'), Js('Champion'), Js('Commando'), Js('Crew'), Js('Defender'), Js('Disciple'), Js('Elite'), Js('Enforcer'), Js('Envoy'), Js('Executioner'), Js('Explorer'), Js('Fighter'), Js('Guard'), Js('Guardian'), Js('Guerrilla'), Js('Hero'), Js('Hunter'), Js('Illusionist'), Js('Keeper'), Js('Lookout'), Js('Mercenary'), Js('Minotaur'), Js('Outrider'), Js('Patrol'), Js('Raider'), Js('Ranger'), Js('Runner'), Js('Safeguard'), Js('Scout'), Js('Sentinel'), Js('Shaman'), Js('Shepherd'), Js('Slayer'), Js('Sorcerer'), Js('Spiritbinder'), Js('Squad'), Js('Squadron'), Js('Stalker'), Js('Tactician'), Js('Trapper'), Js('Trooper'), Js('Vanguard'), Js('Veteran'), Js('Vigilante'), Js('Warlord'), Js('Warrior')]))
var.put('nm11', Js([Js('Adventurous'), Js('Agitated'), Js('Angered'), Js('Angry'), Js('Bitter'), Js('Blaze'), Js('Bold'), Js('Border'), Js('Borderland'), Js('Brave'), Js('Canyon'), Js('Confused'), Js('Corrupt'), Js('Courageous'), Js('Cruel'), Js('Daring'), Js('Defiant'), Js('Delirious'), Js('Diligent'), Js('Energetic'), Js('Enraged'), Js('Exhausted'), Js('Fanatic'), Js('Fearless'), Js('Focused'), Js('Forsaken'), Js('Frightening'), Js('Furious'), Js('Grim'), Js('Haunting'), Js('Heavy'), Js('Humongous'), Js('Juvenile'), Js('Keen'), Js('Labyrinth'), Js('Lone'), Js('Lost'), Js('Mad'), Js('Mysterious'), Js('Noxious'), Js('Powerful'), Js('Prime'), Js('Ragged'), Js('Raging'), Js('Rash'), Js('Reckless'), Js('Robust'), Js('Silent'), Js('Stark'), Js('Swift'), Js('Thunderous'), Js('Vengeful'), Js('Vicious'), Js('Vigilant'), Js('Violent'), Js('Vivid'), Js('Watchful'), Js('Wicked'), Js('Wild'), Js('Wrathful'), Js('Wretched')]))
pass
pass


# Add lib to the module scope
mgtMinotaurs = var.to_python()
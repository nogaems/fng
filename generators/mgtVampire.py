__all__ = ['mgtVampire']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm18', 'nm14', 'nm17', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
                var.put('rnm', ((var.get('Math').callprop('random')*Js(4.0))|Js(0.0)))
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm10').get(var.get('rnd')),var.get('nm14').get(var.get('rnd3'))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                if PyJsStrictEq(var.get('rnm'),Js(0.0)):
                    var.put('lName', ((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd3'))))
                else:
                    if PyJsStrictEq(var.get('rnm'),Js(1.0)):
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm12').get(var.get('rnd5')),var.get('nm14').get(var.get('rnd3'))):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                        var.put('lName', ((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm12').get(var.get('rnd5')),var.get('nm14').get(var.get('rnd3'))):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm14').get(var.get('rnd3')),var.get('nm13').get(var.get('rnd7'))):
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        var.put('lName', ((((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd3'))))
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', (((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm9').get(var.get('rnd4'))):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        var.put('names', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm16').get('length'))|Js(0.0)))
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm17').get('length'))|Js(0.0)))
                        while (PyJsStrictEq(var.get('nm15').get(var.get('rnd')),var.get('nm16').get(var.get('rnd2'))) or PyJsStrictEq((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2'))),var.get('nm17').get(var.get('rnd3')))):
                            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm16').get('length'))|Js(0.0)))
                        var.put('names', (((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2')))+Js(' '))+var.get('nm17').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm18').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm17').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm18').get(var.get('rnd'))+Js(' '))+var.get('nm17').get(var.get('rnd2'))))
            else:
                var.put('rnm', ((var.get('Math').callprop('random')*Js(4.0))|Js(0.0)))
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm10').get(var.get('rnd')),var.get('nm14').get(var.get('rnd3'))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                if PyJsStrictEq(var.get('rnm'),Js(0.0)):
                    var.put('lName', ((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd3'))))
                else:
                    if PyJsStrictEq(var.get('rnm'),Js(1.0)):
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm12').get(var.get('rnd5')),var.get('nm14').get(var.get('rnd3'))):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                        var.put('lName', ((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm12').get(var.get('rnd5')),var.get('nm14').get(var.get('rnd3'))):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm14').get(var.get('rnd3')),var.get('nm13').get(var.get('rnd7'))):
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        var.put('lName', ((((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd3'))))
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm16').get('length'))|Js(0.0)))
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm17').get('length'))|Js(0.0)))
                        while (PyJsStrictEq(var.get('nm15').get(var.get('rnd')),var.get('nm16').get(var.get('rnd2'))) or PyJsStrictEq((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2'))),var.get('nm17').get(var.get('rnd3')))):
                            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm16').get('length'))|Js(0.0)))
                        var.put('names', (((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2')))+Js(' '))+var.get('nm17').get(var.get('rnd3'))))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm18').get('length'))|Js(0.0)))
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm17').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm18').get(var.get('rnd'))+Js(' '))+var.get('nm17').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('cr'), Js('ch'), Js('gr'), Js('k'), Js('kr'), Js('m'), Js('n'), Js('r'), Js('rh'), Js('s'), Js('sz'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('dd'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('lk'), Js('lv'), Js('lr'), Js('n'), Js('nk'), Js('nv'), Js('nz'), Js('rq'), Js('rk'), Js('rr'), Js('rv'), Js('rl'), Js('sk'), Js('sv'), Js('sz'), Js('v'), Js('vk'), Js('vz'), Js('vn'), Js('z'), Js('zk'), Js('zn'), Js('zl')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('k'), Js('n'), Js('r'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('g'), Js('k'), Js('n'), Js('s'), Js('sh'), Js('x')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gh'), Js('j'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('th'), Js('v'), Js('z')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ia'), Js('ou'), Js('ai')]))
var.put('nm8', Js([Js('d'), Js('dd'), Js('dn'), Js('dv'), Js('dz'), Js('fn'), Js('f'), Js('ff'), Js('fn'), Js('k'), Js('kh'), Js('kn'), Js('kv'), Js('l'), Js('lz'), Js('lv'), Js('lr'), Js('ln'), Js('lg'), Js('n'), Js('nv'), Js('ny'), Js('ng'), Js('nz'), Js('rv'), Js('ry'), Js('rn'), Js('rg'), Js('rz'), Js('vn'), Js('vl'), Js('vz'), Js('z'), Js('zn'), Js('zr'), Js('zl')]))
var.put('nm9', Js([Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z'), Js('v')]))
var.put('nm10', Js([Js('ch'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('z')]))
var.put('nm11', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o')]))
var.put('nm12', Js([Js('gd'), Js('gn'), Js('gv'), Js('gl'), Js('lv'), Js('lz'), Js('lg'), Js('ld'), Js('ng'), Js('nd'), Js('nv'), Js('nz'), Js('rg'), Js('rv'), Js('rz'), Js('ry'), Js('sg'), Js('sk'), Js('sz'), Js('sv'), Js('sd'), Js('vd'), Js('vg'), Js('vn'), Js('vz'), Js('zd'), Js('zg'), Js('zl'), Js('zn')]))
var.put('nm13', Js([Js('g'), Js('l'), Js('n'), Js('r'), Js('v'), Js('z')]))
var.put('nm14', Js([Js('d'), Js('dh'), Js('g'), Js('l'), Js('n'), Js('r'), Js('s'), Js('ss'), Js('sk'), Js('x')]))
var.put('nm15', Js([Js('ash'), Js('beast'), Js('bitter'), Js('blaze'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('blood'), Js('bone'), Js('chain'), Js('chaos'), Js('cliff'), Js('cloud'), Js('coven'), Js('crag'), Js('cross'), Js('cull'), Js('dark'), Js('dawn'), Js('dead'), Js('death'), Js('dim'), Js('doom'), Js('down'), Js('dread'), Js('dusk'), Js('ember'), Js('fore'), Js('fury'), Js('gloom'), Js('glum'), Js('gore'), Js('grand'), Js('grim'), Js('haven'), Js('haze'), Js('hell'), Js('iron'), Js('lone'), Js('mist'), Js('mourn'), Js('nether'), Js('night'), Js('onyx'), Js('pale'), Js('pride'), Js('ruby'), Js('saur'), Js('shade'), Js('shadow'), Js('sky'), Js('storm'), Js('strom'), Js('swift'), Js('void'), Js('whit')]))
var.put('nm16', Js([Js('bane'), Js('blade'), Js('blaze'), Js('blight'), Js('blood'), Js('bond'), Js('bone'), Js('born'), Js('bound'), Js('brand'), Js('burn'), Js('chief'), Js('claw'), Js('cloak'), Js('copse'), Js('crest'), Js('crown'), Js('curse'), Js('down'), Js('drawn'), Js('fall'), Js('fang'), Js('flaw'), Js('flow'), Js('force'), Js('forged'), Js('fury'), Js('gaze'), Js('gleam'), Js('glory'), Js('grog'), Js('gut'), Js('hall'), Js('haven'), Js('heart'), Js('hell'), Js('howl'), Js('hunter'), Js('husk'), Js('jaw'), Js('keeper'), Js('lash'), Js('line'), Js('mad'), Js('mane'), Js('mantle'), Js('mark'), Js('maul'), Js('maw'), Js('more'), Js('mourn'), Js('rage'), Js('root'), Js('run'), Js('seeker'), Js('shade'), Js('shadow'), Js('shard'), Js('shroud'), Js('song'), Js('spine'), Js('stalk'), Js('stalker'), Js('surge'), Js('sworn'), Js('thorn'), Js('throne'), Js('tide'), Js('tooth'), Js('way')]))
var.put('nm17', Js([Js('arbiter'), Js('aristocrat'), Js('ascendant'), Js('assassin'), Js('barbarian'), Js('bloodchief'), Js('bloodlord'), Js('bloodseeker'), Js('bloodsucker'), Js('bloodsworn'), Js('brawler'), Js('bruiser'), Js('brute'), Js('butcher'), Js('captain'), Js('champion'), Js('chancellor'), Js('collector'), Js('condemned'), Js('crusader'), Js('cullblade'), Js('cutthroat'), Js('denizen'), Js('dreadknight'), Js('dreadlord'), Js('drinker'), Js('duelist'), Js('emissary'), Js('enigma'), Js('executioner'), Js('exterminator'), Js('feaster'), Js('fiend'), Js('gorger'), Js('harbinger'), Js('healer'), Js('heir'), Js('hexmage'), Js('highborn'), Js('horror'), Js('host'), Js('hunter'), Js('impaler'), Js('interloper'), Js('knight'), Js('lacerator'), Js('mage'), Js('marauder'), Js('mentor'), Js('merc'), Js('mercenary'), Js('nighthawk'), Js('nightmare'), Js('nightowl'), Js('nightwatch'), Js('noble'), Js('nocturnus'), Js('occulist'), Js('oracle'), Js('outcast'), Js('outrider'), Js('overseer'), Js('pariah'), Js('patrol'), Js('prophet'), Js('prowler'), Js('reaper'), Js('reaver'), Js('regent'), Js('reveler'), Js('revenant'), Js('ripper'), Js('ritualist'), Js('sage'), Js('savage'), Js('scourge'), Js('scout'), Js('seer'), Js('sentinel'), Js('servant'), Js('soothsayer'), Js('stalker'), Js('terror'), Js('thief'), Js('thrall'), Js('tormentor'), Js('torturer'), Js('tracker'), Js('traitor'), Js('tyrant'), Js('vampire'), Js('vanguard'), Js('visitor'), Js('warlord'), Js('watch'), Js('zealot')]))
var.put('nm18', Js([Js('Aggressive'), Js('Agile'), Js('Agitated'), Js('Ancient'), Js('Arrogant'), Js('Asylum'), Js('Balcony'), Js('Balustrade'), Js('Bleak'), Js('Blind'), Js('Bloodied'), Js('Bold'), Js('Broken'), Js('Careless'), Js('Catacomb'), Js('Chosen'), Js('Corrupt'), Js('Corrupted'), Js('Courteous'), Js('Crafty'), Js('Crawling'), Js('Crimson'), Js('Crooked'), Js('Cruel'), Js('Crypt'), Js('Cursed'), Js('Dark'), Js('Defiant'), Js('Delirious'), Js('Discrete'), Js('Dusk'), Js('Eager'), Js('Energetic'), Js('Enraged'), Js('Eternal'), Js('Fearless'), Js('Feisty'), Js('Forsaken'), Js('Grave'), Js('Graveyard'), Js('Grim'), Js('Haunting'), Js('Hollow'), Js('Hopeless'), Js('Hungering'), Js('Hungry'), Js('Indulgent'), Js('Insatiable'), Js('Insolent'), Js('Juvenile'), Js('Lone'), Js('Lost'), Js('Loyal'), Js('Mad'), Js('Mania'), Js('Meek'), Js('Meger'), Js('Midnight'), Js('Mindless'), Js('Mysterious'), Js('Necropolis'), Js('Night'), Js('Nightmare'), Js('Nimble'), Js('Noxious'), Js('Obelisk'), Js('Powerful'), Js('Primal'), Js('Prime'), Js('Quick'), Js('Rapid'), Js('Rash'), Js('Ravenous'), Js('Reckless'), Js('Rooftop'), Js('Ruin'), Js('Ruthless'), Js('Sanguine'), Js('Shady'), Js('Silent'), Js('Skeletal'), Js('Sneaky'), Js('Soaked'), Js('Stalking'), Js('Stark'), Js('Swift'), Js('Thirsting'), Js('Tomb'), Js('Tombstone'), Js('Troubled'), Js('Twin'), Js('Vengeful'), Js('Vicious'), Js('Vile'), Js('Villainous'), Js('Void'), Js('Wicked'), Js('Wrathful'), Js('Wretched')]))
pass
pass


# Add lib to the module scope
mgtVampire = var.to_python()
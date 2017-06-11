__all__ = ['mgtKithkin']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    while PyJsStrictEq(var.get('nm7').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nm9').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd8'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    while PyJsStrictEq(var.get('nm12').get(var.get('rnd')),var.get('nm13').get(var.get('rnd2'))):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('names', (((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+Js(' '))+var.get('nm14').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nm9').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd8'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    while PyJsStrictEq(var.get('nm12').get(var.get('rnd')),var.get('nm13').get(var.get('rnd2'))):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('names', (((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+Js(' '))+var.get('nm14').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('g'), Js('h'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('e'), Js('i'), Js('u'), Js('a'), Js('o')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('d'), Js('dd'), Js('l'), Js('ll'), Js('lr'), Js('lm'), Js('ln'), Js('m'), Js('mm'), Js('mn'), Js('mr'), Js('ml'), Js('n'), Js('nn'), Js('nm'), Js('nd'), Js('nl'), Js('nt'), Js('nr'), Js('nz'), Js('r'), Js('rr'), Js('rl'), Js('rd'), Js('rb'), Js('rv'), Js('rz'), Js('v'), Js('vr'), Js('vl')]))
var.put('nm4', Js([Js('c'), Js('ck'), Js('d'), Js('g'), Js('k'), Js('t'), Js('z')]))
var.put('nm5', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('g'), Js('n'), Js('s'), Js('v'), Js('w'), Js('z')]))
var.put('nm6', Js([Js('e'), Js('i'), Js('e'), Js('i'), Js('a'), Js('o')]))
var.put('nm7', Js([Js('c'), Js('ch'), Js('g'), Js('j'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('r'), Js('rl'), Js('rs'), Js('rv'), Js('rw'), Js('sr'), Js('str'), Js('sg'), Js('sl'), Js('sm'), Js('sn'), Js('tr'), Js('thr'), Js('ts'), Js('z'), Js('zz'), Js('zg'), Js('zl')]))
var.put('nm8', Js([Js('d'), Js('f'), Js('h'), Js('n'), Js('t'), Js('th')]))
var.put('nm9', Js([Js('d'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z')]))
var.put('nm10', Js([Js('ee'), Js('ie'), Js('ia'), Js('ea'), Js('ei'), Js('ai'), Js('oo')]))
var.put('nm11', Js([Js('c'), Js('g'), Js('j'), Js('k'), Js('l'), Js('p'), Js('z')]))
var.put('nm12', Js([Js('alder'), Js('amber'), Js('bally'), Js('bare'), Js('barren'), Js('blan'), Js('bon'), Js('bri'), Js('bright'), Js('burren'), Js('char'), Js('cin'), Js('cinder'), Js('cloud'), Js('col'), Js('cold'), Js('crest'), Js('dawn'), Js('day'), Js('dew'), Js('dusk'), Js('ember'), Js('even'), Js('far'), Js('fir'), Js('fog'), Js('fore'), Js('glum'), Js('gold'), Js('grin'), Js('haze'), Js('hazel'), Js('hil'), Js('hill'), Js('keen'), Js('kin'), Js('kins'), Js('ligh'), Js('light'), Js('lon'), Js('lone'), Js('long'), Js('low'), Js('marsh'), Js('mil'), Js('mild'), Js('mist'), Js('moon'), Js('moss'), Js('nettle'), Js('night'), Js('plain'), Js('rain'), Js('rose'), Js('sage'), Js('saur'), Js('shade'), Js('shadow'), Js('snow'), Js('spring'), Js('stone'), Js('stout'), Js('sun'), Js('tall'), Js('thistle'), Js('whit'), Js('wil')]))
var.put('nm13', Js([Js('baile'), Js('ban'), Js('beam'), Js('bend'), Js('blossom'), Js('bluff'), Js('bough'), Js('bow'), Js('brace'), Js('bramble'), Js('branch'), Js('brand'), Js('breeze'), Js('bron'), Js('brook'), Js('brooke'), Js('brow'), Js('caer'), Js('copse'), Js('crag'), Js('crest'), Js('dane'), Js('dew'), Js('down'), Js('fall'), Js('flaw'), Js('flow'), Js('for'), Js('forest'), Js('gaze'), Js('gem'), Js('glade'), Js('gleam'), Js('glide'), Js('glow'), Js('grove'), Js('gust'), Js('heart'), Js('jack'), Js('keep'), Js('leaf'), Js('less'), Js('lock'), Js('mane'), Js('mark'), Js('maw'), Js('meadow'), Js('moon'), Js('more'), Js('nock'), Js('nut'), Js('pad'), Js('ridge'), Js('river'), Js('root'), Js('run'), Js('scaer'), Js('shade'), Js('shadow'), Js('shine'), Js('snow'), Js('song'), Js('spark'), Js('spell'), Js('spine'), Js('spire'), Js('sprout'), Js('spur'), Js('stand'), Js('star'), Js('tide'), Js('ton'), Js('vale'), Js('ward'), Js('wind')]))
var.put('nm14', Js([Js('Adept'), Js('Alchemist'), Js('Balloonist'), Js('Bombardier'), Js('Bomber'), Js('Borderguard'), Js('Captain'), Js('Cavalier'), Js('Champion'), Js('Cleric'), Js('Cohort'), Js('Dodger'), Js('Escort'), Js('Explorer'), Js('Guard'), Js('Guardian'), Js('Guide'), Js('Harbinger'), Js('Harpoonist'), Js('Harrier'), Js('Healer'), Js('Hero'), Js('Initiate'), Js('Kithkin'), Js('Knight'), Js('Liege'), Js('Lookout'), Js('Mage'), Js('Medic'), Js('Mentor'), Js('Patrol'), Js('Pioneer'), Js('Recruiter'), Js('Rogue'), Js('Runner'), Js('Sage'), Js('Scout'), Js('Seeker'), Js('Sentinel'), Js('Shepherd'), Js('Shield-Bearer'), Js('Skirmisher'), Js('Soldier'), Js('Spellduster'), Js('Spy'), Js('Squad'), Js('Stalwart'), Js('Tactician'), Js('Tender'), Js('Trapper'), Js('Vanguard'), Js('Warrior'), Js('Watch'), Js('Watcher'), Js('Witch'), Js('Zealot')]))
pass
pass


# Add lib to the module scope
mgtKithkin = var.to_python()
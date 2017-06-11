__all__ = ['mgtGiants']

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
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd5'))):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(2.0)):
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    while PyJsStrictEq(var.get('nm5').get(var.get('rnd')),var.get('nm6').get(var.get('rnd2'))):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', (((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+Js(' '))+var.get('nm7').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('names', ((var.get('nm8').get(var.get('rnd'))+Js(' '))+var.get('nm9').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('ch'), Js('cr'), Js('dr'), Js('d'), Js('j'), Js('g'), Js('k'), Js('kr'), Js('r'), Js('sk'), Js('sr'), Js('sg'), Js('sc'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('u'), Js('a'), Js('u'), Js('o'), Js('e'), Js('a'), Js('u'), Js('a'), Js('u'), Js('o'), Js('e'), Js('a'), Js('u'), Js('a'), Js('u'), Js('o'), Js('e'), Js('ou')]))
var.put('nm3', Js([Js('d'), Js('dr'), Js('g'), Js('gg'), Js('gr'), Js('gv'), Js('h'), Js('k'), Js('kk'), Js('kr'), Js('kdr'), Js('kv'), Js('kd'), Js('kl'), Js('n'), Js('nn'), Js('ndr'), Js('nr'), Js('ng'), Js('nk'), Js('rr'), Js('rk'), Js('rg'), Js('rrg'), Js('rt'), Js('rv'), Js('zg'), Js('zk'), Js('zr')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('k'), Js('l'), Js('n'), Js('rg'), Js('rd')]))
var.put('nm5', Js([Js('amber'), Js('ash'), Js('axe'), Js('axel'), Js('barren'), Js('battle'), Js('bitter'), Js('blaze'), Js('blood'), Js('bone'), Js('boon'), Js('boulder'), Js('cinder'), Js('cold'), Js('cruel'), Js('dark'), Js('dawn'), Js('deep'), Js('dire'), Js('doom'), Js('down'), Js('durk'), Js('ember'), Js('far'), Js('fir'), Js('fist'), Js('flesh'), Js('flow'), Js('frost'), Js('full'), Js('fury'), Js('gloom'), Js('gore'), Js('grand'), Js('grave'), Js('great'), Js('hammer'), Js('hard'), Js('haze'), Js('heart'), Js('hearth'), Js('hell'), Js('high'), Js('hill'), Js('ice'), Js('keen'), Js('lair'), Js('loam'), Js('lone'), Js('low'), Js('mad'), Js('marsh'), Js('molten'), Js('nether'), Js('night'), Js('pale'), Js('rage'), Js('rough'), Js('shade'), Js('shadow'), Js('sharp'), Js('shatter'), Js('skull'), Js('sky'), Js('solid'), Js('splinter'), Js('star'), Js('stern'), Js('stone'), Js('storm'), Js('stout'), Js('strong'), Js('taint'), Js('thunder'), Js('wild')]))
var.put('nm6', Js([Js('bane'), Js('bark'), Js('basher'), Js('beard'), Js('bellow'), Js('bleeder'), Js('blower'), Js('bough'), Js('brace'), Js('breaker'), Js('breath'), Js('bringer'), Js('brow'), Js('cage'), Js('chaser'), Js('chewer'), Js('cleaver'), Js('cloud'), Js('comber'), Js('crag'), Js('crest'), Js('crusher'), Js('cutter'), Js('doom'), Js('dozer'), Js('dragger'), Js('drinker'), Js('fall'), Js('fire'), Js('fist'), Js('flaw'), Js('flayer'), Js('follower'), Js('fray'), Js('fury'), Js('grave'), Js('grinder'), Js('grip'), Js('grove'), Js('growl'), Js('guard'), Js('hammer'), Js('hand'), Js('heim'), Js('hewer'), Js('hold'), Js('land'), Js('mark'), Js('maul'), Js('mist'), Js('pulper'), Js('rage'), Js('raker'), Js('reaper'), Js('reaver'), Js('ridge'), Js('ripper'), Js('roar'), Js('seeker'), Js('shield'), Js('shock'), Js('shot'), Js('shroud'), Js('skull'), Js('snarl'), Js('sorrow'), Js('splinter'), Js('splitter'), Js('stalker'), Js('stoke'), Js('stone'), Js('stride'), Js('strider'), Js('striker'), Js('sworn'), Js('thorn'), Js('trunk'), Js('wake'), Js('ward'), Js('watch'), Js('watcher'), Js('weaver'), Js('wood')]))
var.put('nm7', Js([Js('Behemoth'), Js('Colossus'), Js('Cyclops'), Js('Giant'), Js('Goliath'), Js('Titan')]))
var.put('nm8', Js([Js('abandoned'), Js('aged'), Js('agile'), Js('amber'), Js('ancient'), Js('angry'), Js('arctic'), Js('armory'), Js('ash'), Js('average'), Js('barren'), Js('battle'), Js('bitter'), Js('blaze'), Js('blind'), Js('blood'), Js('bold'), Js('bone'), Js('border'), Js('bossy'), Js('boulder'), Js('broken'), Js('bruised'), Js('caravan'), Js('carefree'), Js('careless'), Js('chief'), Js('cinder'), Js('clever'), Js('clumsy'), Js('craven'), Js('cruel'), Js('daring'), Js('dark'), Js('dawn'), Js('deep'), Js('defiant'), Js('desolation'), Js('dim'), Js('dire'), Js('dirty'), Js('doom'), Js('ember'), Js('far'), Js('fearless'), Js('focused'), Js('forsaken'), Js('free'), Js('frost'), Js('frosty'), Js('fury'), Js('gentle'), Js('gloom'), Js('gore'), Js('grand'), Js('grave'), Js('great'), Js('greedy'), Js('grim'), Js('hard'), Js('heavy'), Js('hell'), Js('high'), Js('hill'), Js('hungry'), Js('ice'), Js('idle'), Js('intrepid'), Js('lair'), Js('last'), Js('limping'), Js('lone'), Js('low'), Js('lumpy'), Js('mad'), Js('marsh'), Js('molten'), Js('monstrous'), Js('nether'), Js('night'), Js('oblivious'), Js('pale'), Js('powerful'), Js('prime'), Js('pyre'), Js('rage'), Js('remote'), Js('selfish'), Js('shadow'), Js('silent'), Js('stark'), Js('stone'), Js('storm'), Js('swift'), Js('thunder'), Js('vengeful'), Js('vigilant'), Js('wild')]))
var.put('nm9', Js([Js('Bearer'), Js('Behemoth'), Js('Brute'), Js('Butcher'), Js('Champion'), Js('Colossus'), Js('Crusher'), Js('Custodian'), Js('Cyclops'), Js('Drifter'), Js('Enforcer'), Js('Explorer'), Js('Giant'), Js('Goliath'), Js('Graybeard'), Js('Grunt'), Js('Guard'), Js('Guardian'), Js('Harbinger'), Js('Heavyweight'), Js('Intimidator'), Js('Keeper'), Js('Legionnaire'), Js('Meanderer'), Js('Mentor'), Js('Nomad'), Js('Oaf'), Js('Overseer'), Js('Pilgrim'), Js('Protector'), Js('Ranger'), Js('Recruit'), Js('Roamer'), Js('Savage'), Js('Scout'), Js('Sentinel'), Js('Shaman'), Js('Shepherd'), Js('Slavedriver'), Js('Stroller'), Js('Taskmaster'), Js('Titan'), Js('Traveler'), Js('Tyrant'), Js('Vagabond'), Js('Valleymaker'), Js('Wanderer'), Js('Warchief'), Js('Warden'), Js('Watcher')]))
pass
pass


# Add lib to the module scope
mgtGiants = var.to_python()
__all__ = ['ghoulNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
            if (var.get('i')<Js(6.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    while ((var.get('rnd')<Js(3.0)) or PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm4').get(var.get('rnd3')))):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
                else:
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    while (PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd5'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd5')),var.get('nm4').get(var.get('rnd3')))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd3'))))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm5').get(var.get('rnd')),var.get('nm6').get(var.get('rnd2'))):
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                var.put('names', (var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('g'), Js('j'), Js('k'), Js('kh'), Js('r'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('ao'), Js('au'), Js('ou'), Js('ua')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('bl'), Js('bn'), Js('br'), Js('dr'), Js('g'), Js('gd'), Js('gg'), Js('gr'), Js('gy'), Js('gz'), Js('j'), Js('k'), Js('kd'), Js('kg'), Js('kk'), Js('kn'), Js('ks'), Js('kt'), Js('ktr'), Js('kv'), Js('kz'), Js('ld'), Js('lg'), Js('lgr'), Js('lk'), Js('lkr'), Js('m'), Js('mg'), Js('mk'), Js('mm'), Js('n'), Js('ng'), Js('ngr'), Js('nk'), Js('nkr'), Js('nt'), Js('ntr'), Js('nz'), Js('q'), Js('qr'), Js('r'), Js('rb'), Js('rd'), Js('rdr'), Js('rg'), Js('rv'), Js('rz'), Js('sg'), Js('sk'), Js('skr'), Js('sq'), Js('t'), Js('tg'), Js('th'), Js('tr'), Js('tt'), Js('tz'), Js('x'), Js('xn'), Js('xx'), Js('xz'), Js('zb'), Js('zd'), Js('zl'), Js('zn'), Js('zz')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('q'), Js('t'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('ash'), Js('bane'), Js('bitter'), Js('blight'), Js('blood'), Js('bone'), Js('boulder'), Js('brick'), Js('bruise'), Js('carrion'), Js('chain'), Js('claw'), Js('cliff'), Js('corpse'), Js('crow'), Js('curse'), Js('dark'), Js('dead'), Js('death'), Js('dim'), Js('dirt'), Js('doom'), Js('dung'), Js('dust'), Js('earth'), Js('ember'), Js('eye'), Js('face'), Js('fang'), Js('feather'), Js('filth'), Js('fire'), Js('fist'), Js('flame'), Js('flint'), Js('forge'), Js('frost'), Js('gash'), Js('giant'), Js('gloom'), Js('glop'), Js('goo'), Js('gore'), Js('gravel'), Js('grief'), Js('grim'), Js('grime'), Js('grumble'), Js('gunk'), Js('hair'), Js('hell'), Js('ice'), Js('iron'), Js('lead'), Js('leather'), Js('limb'), Js('marble'), Js('marrow'), Js('mire'), Js('muck'), Js('mud'), Js('mug'), Js('nether'), Js('ooze'), Js('pebble'), Js('pest'), Js('pine'), Js('plague'), Js('pus'), Js('rash'), Js('rock'), Js('scourge'), Js('shock'), Js('silt'), Js('skin'), Js('skull'), Js('slate'), Js('sleaze'), Js('slime'), Js('sludge'), Js('slush'), Js('smut'), Js('snow'), Js('sore'), Js('spider'), Js('steel'), Js('storm'), Js('swamp'), Js('teeth'), Js('tooth'), Js('trash'), Js('tusk'), Js('void'), Js('wood'), Js('wound')]))
var.put('nm6', Js([Js('bane'), Js('bash'), Js('basher'), Js('bellow'), Js('belly'), Js('blight'), Js('blower'), Js('bone'), Js('brace'), Js('breaker'), Js('breath'), Js('breather'), Js('brewer'), Js('bringer'), Js('brow'), Js('buster'), Js('chaser'), Js('chewer'), Js('claw'), Js('crest'), Js('crown'), Js('crusher'), Js('cutter'), Js('delver'), Js('digger'), Js('dribbler'), Js('dripper'), Js('drooler'), Js('eye'), Js('eyes'), Js('face'), Js('fang'), Js('feet'), Js('finger'), Js('flayer'), Js('foot'), Js('froth'), Js('fury'), Js('gaze'), Js('gazer'), Js('gobbler'), Js('gorger'), Js('grip'), Js('growl'), Js('guard'), Js('gulper'), Js('gut'), Js('guzzler'), Js('hand'), Js('head'), Js('hide'), Js('hunter'), Js('keeper'), Js('leg'), Js('legs'), Js('limb'), Js('mark'), Js('maul'), Js('maw'), Js('muncher'), Js('reaper'), Js('reaver'), Js('ripper'), Js('robber'), Js('runner'), Js('scrub'), Js('seeker'), Js('shadow'), Js('shaper'), Js('shoulder'), Js('slobber'), Js('snarl'), Js('snout'), Js('sorrow'), Js('splitter'), Js('stalker'), Js('stride'), Js('strider'), Js('strike'), Js('striker'), Js('stuffer'), Js('surge'), Js('sworn'), Js('taker'), Js('walker'), Js('watcher'), Js('weaver')]))
pass
pass


# Add lib to the module scope
ghoulNames = var.to_python()
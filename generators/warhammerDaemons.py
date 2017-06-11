__all__ = ['warhammerDaemons']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            while PyJsStrictEq(var.get('nm6').get(var.get('rnd7')),var.get('nm7').get(var.get('rnd8'))):
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd6')))+Js(' '))+var.get('nm8').get(var.get('rnd9')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('cr'), Js('cz'), Js('g'), Js('gr'), Js('k'), Js('kr'), Js('kh'), Js('n'), Js('q'), Js('qh'), Js('qr'), Js('r'), Js('rh'), Js('sc'), Js('str'), Js('sk'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('i'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('i'), Js('e'), Js('e'), Js('ai')]))
var.put('nm3', Js([Js("'"), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('ch'), Js('dr'), Js('dj'), Js('dz'), Js('g'), Js('gh'), Js('gg'), Js('gr'), Js('gd'), Js('gb'), Js('k'), Js('kr'), Js('kz'), Js('m'), Js('mn'), Js('mz'), Js('mr'), Js('n'), Js('nn'), Js('nd'), Js('ng'), Js('nz'), Js('ndr'), Js('nbr'), Js('ngr'), Js('r'), Js('rr'), Js('rdr'), Js('rgr'), Js('rz'), Js('rzh'), Js('rzr'), Js('rbr'), Js('sr'), Js('sg'), Js('sgh'), Js('shr'), Js('zh'), Js('zr'), Js('zhr'), Js('zg'), Js('zk')]))
var.put('nm5', Js([Js('c'), Js('k'), Js('l'), Js('n'), Js('nd'), Js('s'), Js('th'), Js('z')]))
var.put('nm6', Js([Js('amber'), Js('ash'), Js('battle'), Js('bitter'), Js('blade'), Js('blaze'), Js('blazing'), Js('blood'), Js('bone'), Js('chain'), Js('chaos'), Js('cinder'), Js('claw'), Js('dead'), Js('death'), Js('ember'), Js('fate'), Js('fire'), Js('flame'), Js('fury'), Js('gore'), Js('grim'), Js('heart'), Js('hell'), Js('horn'), Js('lone'), Js('mourn'), Js('nether'), Js('night'), Js('obsidian'), Js('onyx'), Js('plague'), Js('pyre'), Js('rage'), Js('shadow'), Js('silent'), Js('skull'), Js('slate'), Js('storm'), Js('void'), Js('wild'), Js('wrath')]))
var.put('nm7', Js([Js('bane'), Js('bender'), Js('binder'), Js('blaze'), Js('bleeder'), Js('blight'), Js('born'), Js('brand'), Js('breaker'), Js('breath'), Js('bringer'), Js('caller'), Js('chaser'), Js('cleaver'), Js('crest'), Js('dancer'), Js('drifter'), Js('father'), Js('flayer'), Js('force'), Js('forged'), Js('gaze'), Js('gazer'), Js('grip'), Js('heart'), Js('hunter'), Js('keeper'), Js('maker'), Js('master'), Js('might'), Js('mourn'), Js('reaper'), Js('reaver'), Js('rider'), Js('ripper'), Js('seeker'), Js('shade'), Js('shadow'), Js('shaper'), Js('strider'), Js('striker'), Js('sworn'), Js('taker'), Js('thane'), Js('watcher'), Js('weaver')]))
var.put('nm8', Js([Js('the '), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
warhammerDaemons = var.to_python()
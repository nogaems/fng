__all__ = ['warhammerOgres']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            while PyJsStrictEq(var.get('nm5').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd4'))):
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('lName', ((Js(' ')+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
            if (var.get('i')<Js(5.0)):
                var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+var.get('lName')))
            else:
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('lName')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('cr'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('gl'), Js('k'), Js('kr'), Js('n'), Js('q'), Js('qr'), Js('r'), Js('skr'), Js('sk'), Js('sg'), Js('sgr'), Js('tr'), Js('v'), Js('vr'), Js('z'), Js('zr')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('e'), Js('e'), Js('ea'), Js('ao'), Js('ua'), Js('au')]))
var.put('nm3', Js([Js('cl'), Js('cr'), Js('dgr'), Js('ddr'), Js('dz'), Js('g'), Js('gz'), Js('gdr'), Js('gbr'), Js('gr'), Js('gk'), Js('gkr'), Js('k'), Js('kr'), Js('kgz'), Js('kg'), Js('kgr'), Js('kdr'), Js('kb'), Js('lgr'), Js('lkf'), Js('lgf'), Js(''), Js('ldr'), Js('lgb'), Js('lgd'), Js('lgdr'), Js('lzr'), Js('lz'), Js('ng'), Js('ngr'), Js('nd'), Js('ndr'), Js('nk'), Js('nkz'), Js('r'), Js('rg'), Js('rgr'), Js('rgz'), Js('rz'), Js('s'), Js('sgr'), Js('sd'), Js('sfl'), Js('sgl')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('dd'), Js('g'), Js('gg'), Js('k'), Js('kk'), Js('s')]))
var.put('nm5', Js([Js('barb'), Js('beast'), Js('bitter'), Js('black'), Js('blood'), Js('blunt'), Js('bone'), Js('boulder'), Js('brick'), Js('bristle'), Js('bronze'), Js('brown'), Js('cask'), Js('chain'), Js('chest'), Js('coal'), Js('cold'), Js('dark'), Js('dew'), Js('dim'), Js('dirt'), Js('dust'), Js('earth'), Js('ember'), Js('fern'), Js('fire'), Js('flame'), Js('flint'), Js('frost'), Js('froth'), Js('gold'), Js('gore'), Js('granite'), Js('gravel'), Js('green'), Js('gut'), Js('guts'), Js('hill'), Js('horn'), Js('horse'), Js('iron'), Js('keg'), Js('krag'), Js('lone'), Js('long'), Js('man'), Js('metal'), Js('molten'), Js('mud'), Js('oat'), Js('orb'), Js('ore'), Js('pebble'), Js('rage'), Js('rain'), Js('rock'), Js('simple'), Js('slate'), Js('snow'), Js('stone'), Js('stout'), Js('strong'), Js('tusk'), Js('wild')]))
var.put('nm6', Js([Js('back'), Js('bane'), Js('bash'), Js('basher'), Js('beard'), Js('belly'), Js('belt'), Js('bender'), Js('bite'), Js('biter'), Js('bone'), Js('brace'), Js('branch'), Js('breaker'), Js('breath'), Js('bringer'), Js('brow'), Js('buckle'), Js('buster'), Js('chaser'), Js('chew'), Js('chewer'), Js('cleaver'), Js('crush'), Js('crusher'), Js('cut'), Js('cutter'), Js('dig'), Js('digger'), Js('eater'), Js('eye'), Js('eyes'), Js('feet'), Js('fist'), Js('foot'), Js('force'), Js('gaze'), Js('gazer'), Js('grip'), Js('hammer'), Js('hand'), Js('head'), Js('hunter'), Js('mark'), Js('maul'), Js('maw'), Js('might'), Js('munch'), Js('muncher'), Js('pelt'), Js('punch'), Js('ripper'), Js('seeker'), Js('shoulder'), Js('slayer'), Js('snarl'), Js('spine'), Js('splinter'), Js('splitter'), Js('strength'), Js('stride'), Js('strider'), Js('striker'), Js('teeth'), Js('tooth'), Js('watcher')]))
pass
pass


# Add lib to the module scope
warhammerOgres = var.to_python()
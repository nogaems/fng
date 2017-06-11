__all__ = ['warhammerSkaven']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            while PyJsStrictEq(var.get('nm5').get(var.get('rnd')),var.get('nm6').get(var.get('rnd2'))):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('lName', ((Js(' ')+var.get('nm5').get(var.get('rnd')))+var.get('nm6').get(var.get('rnd2'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(6.0)):
                while (var.get('rnd')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('cr'), Js('chr'), Js('ch'), Js('kr'), Js('khr'), Js('kh'), Js('q'), Js('qh'), Js('qr'), Js('qhr'), Js('sn'), Js('sk'), Js('sr'), Js('str'), Js('st'), Js('skr'), Js('th'), Js('thr'), Js('tr'), Js('t'), Js('v'), Js('x'), Js('z'), Js('zr'), Js('zh'), Js('zn')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ie'), Js('ee'), Js('uo'), Js('ue'), Js('uee'), Js('ia'), Js('ua')]))
var.put('nm3', Js([Js('ch'), Js('cn'), Js('cr'), Js('cq'), Js('cx'), Js('gz'), Js('gr'), Js('gch'), Js('gq'), Js('k'), Js('kh'), Js('kr'), Js('kz'), Js('ktr'), Js('kn'), Js('nq'), Js('nk'), Js('nkr'), Js('nqr'), Js('q'), Js('qr'), Js('qz'), Js('qtr'), Js('sh'), Js('shr'), Js('shq'), Js('sq'), Js('sqh'), Js('sqr'), Js('sk'), Js('skr'), Js('t'), Js('thr'), Js('tr'), Js('tz'), Js('x'), Js('xr'), Js('xk'), Js('xkr'), Js('xq'), Js('zq'), Js('zk'), Js('zkr')]))
var.put('nm4', Js([Js('ch'), Js('k'), Js('kch'), Js('l'), Js('lk'), Js('n'), Js('nq'), Js('t'), Js('tch')]))
var.put('nm5', Js([Js('amber'), Js('ash'), Js('ashen'), Js('barb'), Js('barbed'), Js('bitter'), Js('black'), Js('blazing'), Js('bone'), Js('bristle'), Js('broad'), Js('cask'), Js('cinder'), Js('claw'), Js('coven'), Js('crag'), Js('craven'), Js('crest'), Js('crow'), Js('dark'), Js('dead'), Js('death'), Js('deep'), Js('dusk'), Js('dust'), Js('ember'), Js('farrow'), Js('feather'), Js('fiery'), Js('fire'), Js('flint'), Js('fore'), Js('great'), Js('grim'), Js('head'), Js('heart'), Js('high'), Js('iron'), Js('keen'), Js('krag'), Js('lone'), Js('low'), Js('mourn'), Js('night'), Js('pine'), Js('pride'), Js('rapid'), Js('rough'), Js('shadow'), Js('silent'), Js('silver'), Js('skull'), Js('sky'), Js('slate'), Js('steel'), Js('stern'), Js('stone'), Js('tusk'), Js('vermin'), Js('wild'), Js('wind')]))
var.put('nm6', Js([Js('back'), Js('basher'), Js('bender'), Js('binder'), Js('bleeded'), Js('blight'), Js('blood'), Js('bone'), Js('born'), Js('bough'), Js('breaker'), Js('breath'), Js('brow'), Js('buster'), Js('chaser'), Js('chest'), Js('chewer'), Js('chin'), Js('claw'), Js('cleaver'), Js('crest'), Js('crusher'), Js('cutter'), Js('digger'), Js('fang'), Js('fangs'), Js('finger'), Js('fingers'), Js('fist'), Js('flayer'), Js('fury'), Js('gaze'), Js('gazer'), Js('grip'), Js('hunter'), Js('jaw'), Js('lash'), Js('lasher'), Js('master'), Js('maul'), Js('maw'), Js('reaper'), Js('reaver'), Js('ripper'), Js('runner'), Js('sbark'), Js('scar'), Js('scream'), Js('seeker'), Js('shrieker'), Js('slayer'), Js('snout'), Js('spine'), Js('spire'), Js('splitter'), Js('stalker'), Js('striker'), Js('tail'), Js('taker'), Js('thorn'), Js('walker'), Js('watcher'), Js('weaver')]))
pass
pass


# Add lib to the module scope
warhammerSkaven = var.to_python()
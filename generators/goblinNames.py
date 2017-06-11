__all__ = ['goblinNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ba'), Js('Bax'), Js('Dan'), Js('Fi'), Js('Fix'), Js('Fiz'), Js('Gi'), Js('Gix'), Js('Giz'), Js('Gri'), Js('Gree'), Js('Greex'), Js('Grex'), Js('Ja'), Js('Jax'), Js('Jaz'), Js('Jex'), Js('Ji'), Js('Jix'), Js('Ka'), Js('Kax'), Js('Kay'), Js('Kaz'), Js('Ki'), Js('Kix'), Js('Kiz'), Js('Klee'), Js('Kleex'), Js('Kwee'), Js('Kweex'), Js('Kwi'), Js('Kwix'), Js('Kwy'), Js('Ma'), Js('Max'), Js('Ni'), Js('Nix'), Js('No'), Js('Nox'), Js('Qi'), Js('Rez'), Js('Ri'), Js('Ril'), Js('Rix'), Js('Riz'), Js('Ro'), Js('Rox'), Js('So'), Js('Sox'), Js('Vish'), Js('Wi'), Js('Wix'), Js('Wiz'), Js('Za'), Js('Zax'), Js('Ze'), Js('Zee'), Js('Zeex'), Js('Zex'), Js('Zi'), Js('Zix'), Js('Zot')]))
var.put('nm2', Js([Js('b'), Js('ba'), Js('be'), Js('bi'), Js('d'), Js('da'), Js('de'), Js('di'), Js('e'), Js('eb'), Js('ed'), Js('eg'), Js('ek'), Js('em'), Js('en'), Js('eq'), Js('ev'), Js('ez'), Js('g'), Js('ga'), Js('ge'), Js('gi'), Js('ib'), Js('id'), Js('ig'), Js('ik'), Js('im'), Js('in'), Js('iq'), Js('iv'), Js('iz'), Js('k'), Js('ka'), Js('ke'), Js('ki'), Js('m'), Js('ma'), Js('me'), Js('mi'), Js('n'), Js('na'), Js('ni'), Js('q'), Js('qa'), Js('qe'), Js('qi'), Js('v'), Js('va'), Js('ve'), Js('vi'), Js('z'), Js('za'), Js('ze'), Js('zi'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js('ald'), Js('ard'), Js('art'), Js('az'), Js('azy'), Js('bit'), Js('bles'), Js('eek'), Js('eka'), Js('et'), Js('ex'), Js('ez'), Js('gaz'), Js('geez'), Js('get'), Js('giez'), Js('iek'), Js('igle'), Js('ik'), Js('il'), Js('in'), Js('ink'), Js('inkle'), Js('it'), Js('ix'), Js('ixle'), Js('lax'), Js('le'), Js('lee'), Js('les'), Js('lex'), Js('lyx'), Js('max'), Js('maz'), Js('mex'), Js('mez'), Js('mix'), Js('miz'), Js('mo'), Js('old'), Js('rax'), Js('raz'), Js('reez'), Js('rex'), Js('riez'), Js('tee'), Js('teex'), Js('teez'), Js('to'), Js('uek'), Js('x'), Js('xaz'), Js('xeez'), Js('xik'), Js('xink'), Js('xiz'), Js('xonk'), Js('yx'), Js('zeel'), Js('zil')]))
var.put('nm4', Js([Js('Ami'), Js('Amy'), Js('Bli'), Js('Bliz'), Js('Blyz'), Js('Cal'), Js('Eep'), Js('Fiz'), Js('Flux'), Js('Fyz'), Js('Gle'), Js('Glee'), Js('Gly'), Js('Gre'), Js('Gree'), Js('Gui'), Js('Ix'), Js('Iz'), Js('Izi'), Js('Izzi'), Js('Kim'), Js('Kin'), Js('Kle'), Js('Lil'), Js('Lily'), Js('Lin'), Js('Liz'), Js('Ly'), Js('Lyl'), Js('Lyz'), Js('Lys'), Js('Me'), Js('Meg'), Js('Mex'), Js('Mez'), Js('Min'), Js('Mef'), Js('Mix'), Js('Mo'), Js('Myg'), Js('Nal'), Js('Nex'), Js('Nez'), Js('Pen'), Js('Pi'), Js('Pix'), Js('Pixi'), Js('Puzz'), Js('Py'), Js('Pyx'), Js('Pyxi'), Js('Ry'), Js('Sa'), Js('Sal'), Js('Sas'), Js('Saz'), Js('Sli'), Js('Slin'), Js('Sly'), Js('Ti'), Js('Tin'), Js('Tink'), Js('Trix'), Js('Twix'), Js('Yp')]))
var.put('nm5', Js([Js('b'), Js('ba'), Js('be'), Js('bi'), Js('d'), Js('da'), Js('de'), Js('di'), Js('e'), Js('eb'), Js('ed'), Js('eg'), Js('ek'), Js('em'), Js('en'), Js('eq'), Js('ev'), Js('ez'), Js('g'), Js('ga'), Js('ge'), Js('gi'), Js('ib'), Js('id'), Js('ig'), Js('ik'), Js('im'), Js('in'), Js('iq'), Js('iv'), Js('iz'), Js('k'), Js('ka'), Js('ke'), Js('ki'), Js('m'), Js('ma'), Js('me'), Js('mi'), Js('n'), Js('na'), Js('ni'), Js('q'), Js('qa'), Js('qe'), Js('qi'), Js('v'), Js('va'), Js('ve'), Js('vi'), Js('z'), Js('za'), Js('ze'), Js('zi'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('bels'), Js('bles'), Js('els'), Js('ette'), Js('eys'), Js('inee'), Js('ini'), Js('inky'), Js('iz'), Js('ky'), Js('le'), Js('lee'), Js('leex'), Js('les'), Js('lex'), Js('lez'), Js('liz'), Js('lope'), Js('ly'), Js('lyx'), Js('lyz'), Js('nee'), Js('neez'), Js('nex'), Js('ney'), Js('nez'), Js('nix'), Js('ny'), Js('ope'), Js('sal'), Js('see'), Js('sel'), Js('sy'), Js('syl'), Js('tink'), Js('twex'), Js('twinkle'), Js('twizz'), Js('twyx'), Js('twyzz'), Js('wee'), Js('weez'), Js('wiz'), Js('wyz'), Js('xee'), Js('xi'), Js('xie'), Js('xy'), Js('ynee'), Js('yni'), Js('yx'), Js('za'), Js('zee'), Js('zel'), Js('zelly'), Js('zex'), Js('zey'), Js('zi'), Js('zy')]))
var.put('nm7', Js([Js('Bolt'), Js('Boom'), Js('Bot'), Js('Cog'), Js('Copper'), Js('Damp'), Js('Dead'), Js('Far'), Js('Fast'), Js('Fiz'), Js('Fizz'), Js('Fizzle'), Js('Fuse'), Js('Gear'), Js('Giga'), Js('Gold'), Js('Grapple'), Js('Grease'), Js('Greasy'), Js('Ground'), Js('Haggle'), Js('Hard'), Js('Knee'), Js('Leaf'), Js('Loose'), Js('Man'), Js('Mega'), Js('Money'), Js('Mud'), Js('Multi'), Js('Peddle'), Js('Pepper'), Js('Pick'), Js('Rocket'), Js('Rust'), Js('Salt'), Js('Salty'), Js('Sand'), Js('Scroll'), Js('Shadow'), Js('Sharp'), Js('Silver'), Js('Spark'), Js('Steam'), Js('Top'), Js('Wrench')]))
var.put('nm8', Js([Js('basher'), Js('blade'), Js('blast'), Js('blaster'), Js('bolt'), Js('bomb'), Js('boot'), Js('bottom'), Js('bub'), Js('button'), Js('buttons'), Js('cash'), Js('clamp'), Js('digger'), Js('feet'), Js('fingers'), Js('flare'), Js('fuel'), Js('fuse'), Js('gear'), Js('gleam'), Js('gob'), Js('grinder'), Js('grubber'), Js('hallow'), Js('hammer'), Js('head'), Js('knob'), Js('mine'), Js('nose'), Js('nozzle'), Js('pinch'), Js('pocket'), Js('pot'), Js('racket'), Js('rocket'), Js('screw'), Js('shatter'), Js('shiv'), Js('skimmer'), Js('snap'), Js('snipe'), Js('spark'), Js('sprocket'), Js('task'), Js('tongue'), Js('tooth'), Js('tweak'), Js('twister'), Js('volt'), Js('watts'), Js('well'), Js('wick'), Js('wizzle'), Js('wrench')]))
pass
pass


# Add lib to the module scope
goblinNames = var.to_python()
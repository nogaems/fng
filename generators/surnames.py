__all__ = ['surnames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm2').get(var.get('rnd2'))):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('alpen'), Js('amber'), Js('ash'), Js('autumn'), Js('axe'), Js('barley'), Js('battle'), Js('bear'), Js('black'), Js('blade'), Js('blaze'), Js('blood'), Js('blue'), Js('bone'), Js('boulder'), Js('bright'), Js('bronze'), Js('burning'), Js('cask'), Js('chest'), Js('cinder'), Js('clan'), Js('claw'), Js('clear'), Js('cliff'), Js('cloud'), Js('cold'), Js('common'), Js('coven'), Js('crag'), Js('crest'), Js('crow'), Js('crystal'), Js('dark'), Js('dawn'), Js('day'), Js('dead'), Js('death'), Js('deep'), Js('dew'), Js('dirge'), Js('distant'), Js('doom'), Js('down'), Js('dragon'), Js('dream'), Js('dusk'), Js('dust'), Js('eagle'), Js('earth'), Js('elf'), Js('ember'), Js('even'), Js('fallen'), Js('far'), Js('farrow'), Js('feather'), Js('fern'), Js('fire'), Js('fist'), Js('flame'), Js('flat'), Js('flint'), Js('fog'), Js('fore'), Js('forest'), Js('four'), Js('free'), Js('frost'), Js('frozen'), Js('full'), Js('fuse'), Js('gloom'), Js('glory'), Js('glow'), Js('gold'), Js('gore'), Js('grand'), Js('grass'), Js('gray'), Js('great'), Js('green'), Js('grizzly'), Js('hallow'), Js('hallowed'), Js('hammer'), Js('hard'), Js('haven'), Js('hawk'), Js('haze'), Js('heart'), Js('heavy'), Js('hell'), Js('high'), Js('hill'), Js('holy'), Js('honor'), Js('horse'), Js('humble'), Js('hydra'), Js('ice'), Js('iron'), Js('keen'), Js('laughing'), Js('leaf'), Js('light'), Js('lightning'), Js('lion'), Js('lone'), Js('long'), Js('low'), Js('luna'), Js('marble'), Js('marsh'), Js('master'), Js('meadow'), Js('mild'), Js('mirth'), Js('mist'), Js('molten'), Js('monster'), Js('moon'), Js('morning'), Js('moss'), Js('mountain'), Js('mourn'), Js('mourning'), Js('nether'), Js('nickle'), Js('night'), Js('noble'), Js('nose'), Js('oat'), Js('ocean'), Js('orb'), Js('pale'), Js('peace'), Js('phoenix'), Js('pine'), Js('plain'), Js('pride'), Js('proud'), Js('pyre'), Js('rage'), Js('rain'), Js('rapid'), Js('raven'), Js('red'), Js('regal'), Js('rich'), Js('river'), Js('rock'), Js('rose'), Js('rough'), Js('rumble'), Js('rune'), Js('sacred'), Js('sage'), Js('saur'), Js('sea'), Js('serpent'), Js('shade'), Js('shadow'), Js('sharp'), Js('shield'), Js('silent'), Js('silver'), Js('simple'), Js('single'), Js('skull'), Js('sky'), Js('slate'), Js('smart'), Js('snake'), Js('snow'), Js('soft'), Js('solid'), Js('spider'), Js('spirit'), Js('spring'), Js('stag'), Js('star'), Js('steel'), Js('stern'), Js('still'), Js('stone'), Js('storm'), Js('stout'), Js('strong'), Js('summer'), Js('sun'), Js('swift'), Js('tall'), Js('tarren'), Js('terra'), Js('three'), Js('thunder'), Js('titan'), Js('tree'), Js('true'), Js('truth'), Js('tusk'), Js('twilight'), Js('two'), Js('void'), Js('war'), Js('water'), Js('wheat'), Js('whisper'), Js('whit'), Js('white'), Js('wild'), Js('willow'), Js('wind'), Js('winter'), Js('wise'), Js('wolf'), Js('wood'), Js('wooden'), Js('wyvern'), Js('young')]))
var.put('nm2', Js([Js('arm'), Js('arrow'), Js('ash'), Js('axe'), Js('bane'), Js('bash'), Js('basher'), Js('beam'), Js('beard'), Js('belly'), Js('bend'), Js('bender'), Js('binder'), Js('blade'), Js('blaze'), Js('bleeder'), Js('blight'), Js('blood'), Js('bloom'), Js('blossom'), Js('blower'), Js('bluff'), Js('bone'), Js('bough'), Js('bow'), Js('brace'), Js('braid'), Js('branch'), Js('brand'), Js('breaker'), Js('breath'), Js('breeze'), Js('brew'), Js('bringer'), Js('brook'), Js('brooke'), Js('brow'), Js('caller'), Js('chaser'), Js('chewer'), Js('claw'), Js('cleaver'), Js('cloud'), Js('crag'), Js('creek'), Js('crest'), Js('crusher'), Js('cut'), Js('cutter'), Js('dancer'), Js('dane'), Js('dew'), Js('doom'), Js('down'), Js('draft'), Js('dream'), Js('dreamer'), Js('drifter'), Js('dust'), Js('eye'), Js('eyes'), Js('fall'), Js('fallow'), Js('fang'), Js('feather'), Js('fire'), Js('fist'), Js('flame'), Js('flare'), Js('flaw'), Js('flayer'), Js('flow'), Js('flower'), Js('follower'), Js('force'), Js('forest'), Js('forge'), Js('fury'), Js('gaze'), Js('gazer'), Js('gem'), Js('glade'), Js('gleam'), Js('glide'), Js('gloom'), Js('glory'), Js('glow'), Js('grain'), Js('grip'), Js('grove'), Js('guard'), Js('gust'), Js('hair'), Js('hammer'), Js('hand'), Js('heart'), Js('hell'), Js('helm'), Js('hide'), Js('horn'), Js('hunter'), Js('jumper'), Js('keep'), Js('keeper'), Js('killer'), Js('lance'), Js('lash'), Js('leaf'), Js('less'), Js('light'), Js('mane'), Js('mantle'), Js('mark'), Js('maul'), Js('maw'), Js('might'), Js('moon'), Js('more'), Js('mourn'), Js('oak'), Js('orb'), Js('ore'), Js('peak'), Js('pelt'), Js('pike'), Js('punch'), Js('rage'), Js('reaper'), Js('reaver'), Js('rider'), Js('ridge'), Js('ripper'), Js('river'), Js('roar'), Js('rock'), Js('root'), Js('run'), Js('runner'), Js('scar'), Js('scream'), Js('scribe'), Js('seeker'), Js('shade'), Js('shadow'), Js('shaper'), Js('shard'), Js('shield'), Js('shine'), Js('shot'), Js('shout'), Js('singer'), Js('sky'), Js('slayer'), Js('snarl'), Js('snout'), Js('snow'), Js('soar'), Js('song'), Js('sorrow'), Js('spark'), Js('spear'), Js('spell'), Js('spire'), Js('spirit'), Js('splitter'), Js('sprinter'), Js('stalker'), Js('star'), Js('steam'), Js('steel'), Js('stone'), Js('stream'), Js('strength'), Js('stride'), Js('strider'), Js('strike'), Js('striker'), Js('sun'), Js('surge'), Js('swallow'), Js('swift'), Js('sword'), Js('sworn'), Js('tail'), Js('taker'), Js('talon'), Js('thorn'), Js('thorne'), Js('tide'), Js('toe'), Js('track'), Js('trap'), Js('trapper'), Js('tree'), Js('vale'), Js('valor'), Js('vigor'), Js('walker'), Js('ward'), Js('watcher'), Js('water'), Js('weaver'), Js('whirl'), Js('whisk'), Js('whisper'), Js('willow'), Js('wind'), Js('winds'), Js('wing'), Js('wolf'), Js('wood'), Js('woods'), Js('wound')]))
pass
pass


# Add lib to the module scope
surnames = var.to_python()
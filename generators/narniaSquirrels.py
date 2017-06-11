__all__ = ['narniaSquirrels']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('babble'), Js('banter'), Js('bashing'), Js('bicker'), Js('blather'), Js('boggle'), Js('bristle'), Js('bubble'), Js('bumble'), Js('bundle'), Js('burble'), Js('burrow'), Js('bustle'), Js('caper'), Js('chuckle'), Js('clamor'), Js('cobble'), Js('crackle'), Js('crinkle'), Js('crumble'), Js('cuddle'), Js('dabble'), Js('dally'), Js('dandle'), Js('dangle'), Js('dazzle'), Js('dibble'), Js('dimple'), Js('dither'), Js('doodle'), Js('drabble'), Js('dribble'), Js('fiddle'), Js('fidget'), Js('flatter'), Js('flitter'), Js('flutter'), Js('fumble'), Js('gambol'), Js('gibber'), Js('giggle'), Js('gobble'), Js('grapple'), Js('heckle'), Js('hiccup'), Js('hinder'), Js('hobble'), Js('huddle'), Js('hustle'), Js('jabber'), Js('jangle'), Js('jiggle'), Js('jingle'), Js('jitter'), Js('jostle'), Js('juggle'), Js('jumble'), Js('lumber'), Js('meddle'), Js('mingle'), Js('muffle'), Js('mumble'), Js('murmur'), Js('mutter'), Js('nibble'), Js('paddle'), Js('patter'), Js('pebble'), Js('pedal'), Js('ponder'), Js('prattle'), Js('puddle'), Js('quarrel'), Js('quibble'), Js('ramble'), Js('rattle'), Js('riddle'), Js('ruffle'), Js('rumble'), Js('rustle'), Js('scuttle'), Js('shiver'), Js('shuffle'), Js('skitter'), Js('slumber'), Js('snicker'), Js('sniffle'), Js('spatter'), Js('spattle'), Js('spitter'), Js('spittle'), Js('splutter'), Js('sprinkle'), Js('startle'), Js('tickle'), Js('trickle'), Js('tumble'), Js('twiddle'), Js('twinkle'), Js('twitter'), Js('waddle'), Js('wander'), Js('whistle'), Js('wiggle'), Js('wobble')]))
    var.put('nm2', Js([Js('badge'), Js('band'), Js('bean'), Js('bell'), Js('bells'), Js('berry'), Js('bit'), Js('bug'), Js('bun'), Js('cheek'), Js('cheeks'), Js('chess'), Js('chest'), Js('chin'), Js('chip'), Js('chips'), Js('click'), Js('cloud'), Js('coat'), Js('coin'), Js('cord'), Js('cork'), Js('cup'), Js('dig'), Js('dish'), Js('doll'), Js('dot'), Js('drop'), Js('fan'), Js('feat'), Js('feet'), Js('flow'), Js('fluke'), Js('foot'), Js('gift'), Js('glove'), Js('hat'), Js('heart'), Js('jam'), Js('joint'), Js('joke'), Js('joy'), Js('kiss'), Js('knot'), Js('leaf'), Js('link'), Js('mark'), Js('mask'), Js('patch'), Js('pie'), Js('piece'), Js('pitch'), Js('ray'), Js('ring'), Js('rub'), Js('run'), Js('rush'), Js('shine'), Js('side'), Js('slide'), Js('slip'), Js('spark'), Js('spot'), Js('star'), Js('step'), Js('straw'), Js('strip'), Js('tail'), Js('tale'), Js('teeth'), Js('tip'), Js('toe'), Js('toes'), Js('tooth'), Js('top'), Js('trick'), Js('tune'), Js('twig'), Js('twigs'), Js('twist'), Js('will'), Js('wish'), Js('wit')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm2').get(var.get('rnd2'))):
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
narniaSquirrels = var.to_python()
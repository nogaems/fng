__all__ = ['narniaMoles']

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
    var.put('nm1', Js([Js('aloe'), Js('anise'), Js('apple'), Js('aster'), Js('beet'), Js('bloom'), Js('blossom'), Js('breeze'), Js('butter'), Js('cabbage'), Js('carrot'), Js('cherry'), Js('clover'), Js('cluster'), Js('coco'), Js('cocoa'), Js('comet'), Js('cotton'), Js('crocus'), Js('daisy'), Js('feather'), Js('fern'), Js('flake'), Js('flannel'), Js('flora'), Js('floral'), Js('flower'), Js('fluff'), Js('fluffy'), Js('garden'), Js('gilly'), Js('gravel'), Js('grotto'), Js('grove'), Js('herb'), Js('holly'), Js('iris'), Js('jewel'), Js('jute'), Js('laurel'), Js('lemon'), Js('lilac'), Js('lily'), Js('lotus'), Js('mango'), Js('marble'), Js('melon'), Js('mistle'), Js('moss'), Js('myrtle'), Js('nugget'), Js('onion'), Js('orchid'), Js('parsnip'), Js('pebble'), Js('pepper'), Js('petal'), Js('plume'), Js('poppy'), Js('prim'), Js('puff'), Js('pumpkin'), Js('quill'), Js('radish'), Js('ribbon'), Js('rose'), Js('shell'), Js('shrub'), Js('thistle'), Js('truffle'), Js('tuber'), Js('tulip'), Js('tumble'), Js('turnip'), Js('veggie'), Js('vine'), Js('violet'), Js('whisper'), Js('wool')]))
    var.put('nm2', Js([Js('ball'), Js('bead'), Js('blanket'), Js('bloom'), Js('bow'), Js('brim'), Js('bud'), Js('bump'), Js('cap'), Js('cloak'), Js('clog'), Js('coat'), Js('comb'), Js('cup'), Js('drape'), Js('feet'), Js('fig'), Js('flake'), Js('flint'), Js('fluff'), Js('foot'), Js('frill'), Js('gem'), Js('glove'), Js('gloves'), Js('glow'), Js('hat'), Js('hoop'), Js('leaf'), Js('lid'), Js('lock'), Js('lump'), Js('mask'), Js('mitt'), Js('mitten'), Js('moss'), Js('plume'), Js('puff'), Js('rout'), Js('sash'), Js('scarf'), Js('scarfs'), Js('shawl'), Js('shell'), Js('shoe'), Js('shoes'), Js('shrub'), Js('sock'), Js('socks'), Js('stem'), Js('stone'), Js('straw'), Js('tie'), Js('web'), Js('wig'), Js('wrap')]))
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
narniaMoles = var.to_python()
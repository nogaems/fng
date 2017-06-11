__all__ = ['entNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Algal'), Js('Bare'), Js('Barren'), Js('Dense'), Js('Dwarf'), Js('Hard'), Js('Pygmy'), Js('Scorched'), Js('Scorch'), Js('Scrub'), Js('Tender'), Js('Wild'), Js('Nettle'), Js('Shadow'), Js('Splint'), Js('Splinter'), Js('Mad'), Js('Gentle'), Js('Spring'), Js('Summer'), Js('Winter'), Js('Autumn'), Js('Fall'), Js('Snow'), Js('Iron'), Js('Wise'), Js('Clever'), Js('Cunning'), Js('Sharp'), Js('Bland'), Js('Taint'), Js('Tainted'), Js('Mellow'), Js('Weeping'), Js('Tender'), Js('Kind'), Js('Soft'), Js('Quiet'), Js('Silent'), Js('Mild'), Js('Bitter'), Js('Cruel'), Js('Mean'), Js('Vine'), Js('Black'), Js('Gray'), Js('Charred'), Js('Burn'), Js('Burned')]))
var.put('nm2', Js([Js('acorn'), Js('alder'), Js('ash'), Js('beech'), Js('birch'), Js('cedar'), Js('cherry'), Js('cypress'), Js('elm'), Js('fir'), Js('juniper'), Js('larch'), Js('locust'), Js('maple'), Js('oak'), Js('peach'), Js('pine'), Js('poplar'), Js('spruce'), Js('walnut'), Js('willow'), Js('yew'), Js('tree'), Js('hazel'), Js('twig'), Js('trunk'), Js('root'), Js('nut'), Js('trunk'), Js('herb'), Js('limb'), Js('beard'), Js('leaf'), Js('husk'), Js('spur'), Js('sprout'), Js('wood'), Js('stump'), Js('thorn'), Js('talon'), Js('blossom'), Js('leg'), Js('legs'), Js('limbs'), Js('tendril')]))
var.put('nm3', Js([Js('Acorn'), Js('Alder'), Js('Ash'), Js('Beech'), Js('Birch'), Js('Cedar'), Js('Cherry'), Js('Cypress'), Js('Elm'), Js('Fir'), Js('Juniper'), Js('Larch'), Js('Locust'), Js('Maple'), Js('Oak'), Js('Oaken'), Js('Peach'), Js('Pine'), Js('Poplar'), Js('Spruce'), Js('Walnut'), Js('Willow'), Js('Yew'), Js('Tree'), Js('Hazel'), Js('Thistle')]))
var.put('nm4', Js([Js('bark'), Js('beard'), Js('blade'), Js('bramble'), Js('nettle'), Js('spray'), Js('bush'), Js('shell'), Js('husk'), Js('claw'), Js('fang'), Js('talon'), Js('paw'), Js('crown'), Js('fern'), Js('copse'), Js('scrub'), Js('flesh'), Js('fury'), Js('grove'), Js('covert'), Js('stand'), Js('herb'), Js('leaf'), Js('growl'), Js('howl'), Js('trunk'), Js('root'), Js('bellow'), Js('roar'), Js('snarl'), Js('shade'), Js('shadow'), Js('flower'), Js('blossom'), Js('limb'), Js('lock'), Js('spine'), Js('pad'), Js('needle'), Js('stalk'), Js('splint'), Js('splinter'), Js('spur'), Js('twig'), Js('stub'), Js('stump'), Js('shrub'), Js('skin'), Js('thorn'), Js('tip'), Js('tooth'), Js('twig'), Js('wood'), Js('burn'), Js('scar'), Js('eye'), Js('brow'), Js('sprout'), Js('tendril')]))
pass
pass


# Add lib to the module scope
entNames = var.to_python()
__all__ = ['phoenixNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
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
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ash'), Js('Ashes'), Js('Aura'), Js('Aurora'), Js('Beacon'), Js('Beak'), Js('Beam'), Js('Blaze'), Js('Blazetalon'), Js('Blink'), Js('Bonfi'), Js('Brilliancy'), Js('Brim'), Js('Cinder'), Js('Cinders'), Js('Crux'), Js('Dawn'), Js('Dazzle'), Js('Deja'), Js('Dusty'), Js('Elemence'), Js('Ember'), Js('Eos'), Js('Eterna'), Js('Eternus'), Js('Feathers'), Js('Ferno'), Js('Fiere'), Js('Flambeau'), Js('Flame'), Js('Flametalon'), Js('Flare'), Js('Flash'), Js('Flayme'), Js('Fume'), Js('Fury'), Js('Fye'), Js('Fyre'), Js('Genesis'), Js('Glaze'), Js('Glint'), Js('Gloss'), Js('Glow'), Js('Heat'), Js('Icarus'), Js('Ignite'), Js('Illume'), Js('Illumine'), Js('Inferno'), Js('Juvenate'), Js('Kindle'), Js('Light'), Js('Lucent'), Js('Lumino'), Js('Luminos'), Js('Morte'), Js('Nether'), Js('Nite'), Js('Onyx'), Js('Pharos'), Js('Pire'), Js('Plume'), Js('Pyre'), Js('Radiance'), Js('Raise'), Js('Ray'), Js('Raye'), Js('Revi'), Js('Rise'), Js('Ryse'), Js('Ryze'), Js('Scorch'), Js('Scorchey'), Js('Sheen'), Js('Shimmer'), Js('Shine'), Js('Slag'), Js('Soar'), Js('Sol'), Js('Solar'), Js('Solaris'), Js('Soleil'), Js('Soot'), Js('Soots'), Js('Soul'), Js('Spark'), Js('Sparkle'), Js('Sparkles'), Js('Spirit'), Js('Sprout'), Js('Smoke'), Js('Sunbeam'), Js('Sunny'), Js('Surge'), Js('Tinder'), Js('Torch'), Js('Vitality'), Js('Vitally'), Js('Viva'), Js('Vu'), Js('Zeal')]))
pass
pass


# Add lib to the module scope
phoenixNames = var.to_python()
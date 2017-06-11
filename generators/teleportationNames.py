__all__ = ['teleportationNames']

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
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('Apparate'), Js('Beam'), Js('Blink'), Js('Body Flicker'), Js('Bounce'), Js('Broadcast'), Js('Bunnyhop'), Js('Burst'), Js('Bypass'), Js('Conversion'), Js('Cross'), Js('Crosscut'), Js('Crossover'), Js('Depart'), Js('Detour'), Js('Deviate'), Js('Dimension Door'), Js('Discharge'), Js('Echo'), Js('Escape'), Js('Ether Leap'), Js('Ethereal Pass'), Js('Etheric Transfer'), Js('Fae Walk'), Js('Flash'), Js('Flicker'), Js('Flip-flop'), Js('Flutter'), Js('Flux'), Js('Fluxuate'), Js('Geo Burst'), Js('Geo Dash'), Js('Geo Deflect'), Js('Geo Leap'), Js('Geo Pass'), Js('Geo Relocation'), Js('Geocast'), Js('Geodrift'), Js('Geoflect'), Js('Geogenerate'), Js('Geomorphosis'), Js('Geoport'), Js('Geostep'), Js('Geotemper'), Js('Geovolve'), Js('Glimmer'), Js('Jolt'), Js('Light Step'), Js('Lightning Step'), Js('Localeap'), Js('Omit'), Js('Pass'), Js('Pass Through'), Js('Plane Step'), Js('Plane Walk'), Js('Portal'), Js('Pulse'), Js('Pulse Pass'), Js('Quantum Leap'), Js('Quick Shift'), Js('Quick Switch'), Js('Quick Transit'), Js('Quick Travel'), Js('Quickstep'), Js('Radiate'), Js('Relocaleap'), Js('Relocate'), Js('Relocation'), Js('Relocus'), Js('Resurge'), Js('Shadowstep'), Js('Shift'), Js('Shortcut'), Js('Sidestep'), Js('Skip'), Js('Skipstep'), Js('Skirt'), Js('Slipstream'), Js('Space Jump'), Js('Split Step'), Js('Stream'), Js('Streamstep'), Js('Switch'), Js('Take Flight'), Js('Tele'), Js('Tele Out'), Js('Telecast'), Js('Teleskip'), Js('Transfer'), Js('Transflux'), Js('Transkip'), Js('Translocation'), Js('Transmaterialize'), Js('Transmit'), Js('Transtep'), Js('Transwarp'), Js('Tripskip'), Js('Void Step'), Js('Warp'), Js('Wink')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
teleportationNames = var.to_python()
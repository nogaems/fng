__all__ = ['gethNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names4', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['names2', 'result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('names2', var.get('Math').callprop('floor', ((var.get('Math').callprop('random')*Js(250.0))+Js(1.0))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', (((var.get('names1').get(var.get('rnd'))+Js('-'))+var.get('names2'))+var.get('names3').get(var.get('rnd1'))))
            else:
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('names', var.get('names4').get(var.get('rnd0')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Unit'), Js('Platform'), Js('Mod'), Js('System'), Js('SysMod'), Js('GU'), Js('G-Unit'), Js('Geth-Unit'), Js('Module')]))
var.put('names3', Js([Js('a'), Js('b'), Js('c'), Js('e'), Js('s'), Js('x')]))
var.put('names4', Js([Js('Armada'), Js('Batallion'), Js('Alpha'), Js('Omega'), Js('Myriad'), Js('Sundry'), Js('Horde'), Js('Brigade'), Js('Phalanx'), Js('Host'), Js('Enigma'), Js('Terminus'), Js('Prophet'), Js('Genesis'), Js('Dawn'), Js('Oracle'), Js('Anomaly'), Js('Centurion'), Js('Obelisk'), Js('Pinnacle'), Js('Goliath'), Js('Apex'), Js('Vortex'), Js('Vertex'), Js('Armageddon'), Js('Oblivion'), Js('Eternity'), Js('Daemon'), Js('Demise'), Js('Destiny')]))
pass
pass


# Add lib to the module scope
gethNames = var.to_python()
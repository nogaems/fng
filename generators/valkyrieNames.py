__all__ = ['valkyrieNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', (var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('A'), Js('Aga'), Js('Ar'), Js('Bry'), Js('Ey'), Js('Fri'), Js('Fria'), Js('Ge'), Js('Gei'), Js('Go'), Js('Guo'), Js('He'), Js('Hi'), Js('Hja'), Js('Hjo'), Js('Hla'), Js('Hlo'), Js('Hri'), Js('Hru'), Js('Ka'), Js('Mi'), Js('O'), Js('Re'), Js('Regi'), Js('Ro'), Js('Sa'), Js('San'), Js('Si'), Js('Ska'), Js('Ske'), Js('Sko'), Js('Sku'), Js('Sva'), Js('Sve'), Js('Svei'), Js('Svi'), Js('Tho'), Js('Thri'), Js('Thru'), Js('Va')]))
var.put('names2', Js([Js('dana'), Js('dis'), Js('dmadra'), Js('dne'), Js('dr'), Js('dra'), Js('drifa'), Js('dul'), Js('gabi'), Js('gin'), Js('ginleif'), Js('gjold'), Js('grdrifa'), Js('grior'), Js('grun'), Js('gul'), Js('hildr'), Js('hylde'), Js('ja'), Js('la'), Js('ld'), Js('ldana'), Js('ldr'), Js('leif'), Js('lmold'), Js('lna'), Js('lrun'), Js('ma'), Js('madra'), Js('mold'), Js('nd'), Js('ndul'), Js('ngrior'), Js('nhildr'), Js('nhylde'), Js('nul'), Js('pul'), Js('ra'), Js('rdmadra'), Js('rifa'), Js('rior'), Js('rja'), Js('ronul'), Js('run'), Js('rvif'), Js('st'), Js('ta'), Js('tha'), Js('va'), Js('vif')]))
pass
pass


# Add lib to the module scope
valkyrieNames = var.to_python()
__all__ = ['wildstarMechari']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('lname', (var.get('nm9').get(var.get('rnd6'))+var.get('nm10').get(var.get('rnd7'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    if (var.get('rnd')<Js(5.0)):
                        while (var.get('rnd5')<Js(5.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('lname')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+Js(' '))+var.get('lname')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd')<Js(5.0)):
                    while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('gl'), Js('h'), Js('l'), Js('m'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('io'), Js('au'), Js('ei')]))
var.put('nm3', Js([Js('c'), Js('cr'), Js('chr'), Js('ct'), Js('g'), Js('gn'), Js('gz'), Js('kr'), Js('kt'), Js('kx'), Js('kn'), Js('l'), Js('lb'), Js('ll'), Js('mph'), Js('n'), Js('ph'), Js('pr'), Js('ps'), Js('r'), Js('rx'), Js('rc'), Js('rct'), Js('rm'), Js('rv'), Js('rz'), Js('st'), Js('sp'), Js('t'), Js('tr'), Js('v'), Js('x'), Js('xt'), Js('c'), Js('g'), Js('l'), Js('n'), Js('r'), Js('t'), Js('v'), Js('x')]))
var.put('nm4', Js([Js(''), Js('c'), Js('cs'), Js('n'), Js('m'), Js('r'), Js('s'), Js('t'), Js('x')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('phr'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('y'), Js('y'), Js('y'), Js('ia'), Js('au'), Js('ie'), Js('io')]))
var.put('nm7', Js([Js('b'), Js('br'), Js('c'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fn'), Js('fl'), Js('gh'), Js('lv'), Js('ln'), Js('lm'), Js('lz'), Js('lph'), Js('lf'), Js('m'), Js('mz'), Js('mr'), Js('mn'), Js('n'), Js('nv'), Js('nz'), Js('r'), Js('rk'), Js('rv'), Js('rz'), Js('rs'), Js('t'), Js('th'), Js('v'), Js('x'), Js('z'), Js('zn'), Js('b'), Js('c'), Js('d'), Js('f'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('x'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('x'), Js('z')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('h'), Js('n'), Js('l'), Js('ll'), Js('s'), Js('sh'), Js('th'), Js('x')]))
var.put('nm9', Js([Js('Alpha'), Js('Beta'), Js('Bi'), Js('Cen'), Js('Cent'), Js('Centi'), Js('Chi'), Js('Dec'), Js('Deca'), Js('Decem'), Js('Delta'), Js('Di'), Js('Dodeca'), Js('Du'), Js('Duo'), Js('Duodec'), Js('Ennea'), Js('Epsilon'), Js('Eta'), Js('Gamma'), Js('Hec'), Js('Hecato'), Js('Hect'), Js('Hep'), Js('Hept'), Js('Hepta'), Js('Hex'), Js('Hexa'), Js('Iota'), Js('Kappa'), Js('Kilo'), Js('Lambda'), Js('Milli'), Js('Mono'), Js('Mu'), Js('Non'), Js('Nove'), Js('Nu'), Js('Nulli'), Js('Oc'), Js('Oct'), Js('Octa'), Js('Octo'), Js('Ogdo'), Js('Omega'), Js('Penta'), Js('Phi'), Js('Pi'), Js('Psi'), Js('Quadri'), Js('Quadru'), Js('Rho'), Js('Sedec'), Js('Semi'), Js('Sep'), Js('Sept'), Js('Sigma'), Js('Tau'), Js('Tetra'), Js('Theta'), Js('Tri'), Js('Trio'), Js('Unci'), Js('Uni'), Js('Upsilon'), Js('Xi'), Js('Zeta')]))
var.put('nm10', Js([Js('bit'), Js('byt'), Js('coil'), Js('col'), Js('cue'), Js('cy'), Js('frag'), Js('gine'), Js('helix'), Js('hicle'), Js('jet'), Js('lap'), Js('lic'), Js('lit'), Js('lix'), Js('logy'), Js('loop'), Js('maton'), Js('mech'), Js('mic'), Js('mics'), Js('net'), Js('nic'), Js('nics'), Js('niq'), Js('nis'), Js('nism'), Js('nix'), Js('nogy'), Js('nox'), Js('pin'), Js('ping'), Js('pute'), Js('ram'), Js('rom'), Js('ron'), Js('ser'), Js('sor'), Js('tec'), Js('tic'), Js('tics'), Js('ton'), Js('tred'), Js('tric'), Js('tron'), Js('vex'), Js('vox'), Js('ware'), Js('xis'), Js('zip')]))
pass
pass


# Add lib to the module scope
wildstarMechari = var.to_python()
__all__ = ['warhammerOrkNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4')))+var.get('names5').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                var.put('names', (var.get('names6').get(var.get('rnd'))+var.get('names7').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('b'), Js('br'), Js('ch'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gh'), Js('gr'), Js('hr'), Js('k'), Js('kh'), Js('kr'), Js('m'), Js('n'), Js('r'), Js('sk'), Js('sm'), Js('sn'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('wr'), Js('z'), Js('zh'), Js('zr'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names2', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('u')]))
var.put('names3', Js([Js('b'), Js('d'), Js('dbr'), Js('dr'), Js('g'), Js('gb'), Js('gd'), Js('gg'), Js('gh'), Js('gn'), Js('gt'), Js('gz'), Js('hrbl'), Js('k'), Js('kg'), Js('kk'), Js('kt'), Js('lgr'), Js('nz'), Js('r'), Js('rb'), Js('rg'), Js('rgn'), Js('rgr'), Js('rk'), Js('rkr'), Js('rl'), Js('rz'), Js('sk'), Js('skr'), Js('t'), Js('tgr'), Js('tzm'), Js('tzn'), Js('zdr'), Js('zg'), Js('zgr')]))
var.put('names4', Js([Js('a'), Js('o'), Js('u')]))
var.put('names5', Js([Js('d'), Js('g'), Js('gar'), Js('gas'), Js('gg'), Js('gus'), Js('k'), Js('kh'), Js('kk'), Js('m'), Js('nak'), Js('r'), Js('rd'), Js('rk'), Js('x'), Js('z'), Js('zak'), Js('zz')]))
var.put('names6', Js([Js('Barb'), Js('Battle'), Js('Big'), Js('Blood'), Js('Blud'), Js('Bone'), Js('Brain'), Js('Crook'), Js('Crown'), Js('Dark'), Js('Dome'), Js('Doom'), Js('Dream'), Js('Ead'), Js('Ed'), Js('Face'), Js('Fire'), Js('Fist'), Js('Gloom'), Js('Glum'), Js('God'), Js('Gore'), Js('Grave'), Js('Grim'), Js('Gut'), Js('Gutz'), Js('Hed'), Js('Hell'), Js('Ice'), Js('Iron'), Js('Jaw'), Js('Jowl'), Js('Kill'), Js('Klaw'), Js('Krook'), Js('Mad'), Js('Mighty'), Js('Mug'), Js('Muzzle'), Js('Rabid'), Js('Rage'), Js('Rekk'), Js('Rock'), Js('Scalp'), Js('Skar'), Js('Skull'), Js('Slay'), Js('Strong'), Js('War'), Js('Wild')]))
var.put('names7', Js([Js('acka'), Js('ackah'), Js('basha'), Js('bashah'), Js('boila'), Js('boilah'), Js('braka'), Js('brakah'), Js('brakka'), Js('brakkah'), Js('breaka'), Js('breakah'), Js('busta'), Js('choppa'), Js('choppah'), Js('cleava'), Js('cleavah'), Js('clompa'), Js('clompah'), Js('cooka'), Js('cookah'), Js('cracka'), Js('crackah'), Js('crasha'), Js('crashah'), Js('crumpa'), Js('crumpah'), Js('crusha'), Js('crushah'), Js('cutta'), Js('cuttah'), Js('dagga'), Js('daggah'), Js('fang'), Js('fist'), Js('gasha'), Js('gashah'), Js('gutta'), Js('guttah'), Js('hacka'), Js('hackah'), Js('kleava'), Js('kleavah'), Js('krak'), Js('kraka'), Js('krakah'), Js('krumpa'), Js('krumpah'), Js('krusha'), Js('krushah'), Js('rippa'), Js('rippah'), Js('shredda'), Js('shreddah'), Js('skar'), Js('skorcha'), Js('skorchah'), Js('slasha'), Js('slashah'), Js('smasha'), Js('smashah'), Js('snagga'), Js('snaggah'), Js('snappa'), Js('snappah'), Js('spitta'), Js('spittah'), Js('splitta'), Js('splittah'), Js('stampa'), Js('stampah'), Js('stompa'), Js('stompah'), Js('trasha'), Js('trashah'), Js('wakka'), Js('wakkah'), Js('whacka'), Js('whackah')]))
pass
pass


# Add lib to the module scope
warhammerOrkNames = var.to_python()
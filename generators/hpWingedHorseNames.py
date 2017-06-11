__all__ = ['hpWingedHorseNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('ae'), Js('ea'), Js('i'), Js('o'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('ba'), Js('bli'), Js('blo'), Js('bra'), Js('bri'), Js('cae'), Js('ci'), Js('cra'), Js('cro'), Js('da'), Js('do'), Js('dra'), Js('dro'), Js('fae'), Js('fo'), Js('fra'), Js('fre'), Js('glo'), Js('gra'), Js('gre'), Js('gri'), Js('la'), Js('lea'), Js('lia'), Js('lo'), Js('ma'), Js('mae'), Js('me'), Js('mea'), Js('nae'), Js('nea'), Js('nei'), Js('ni'), Js('phae'), Js('phri'), Js('pio'), Js('po'), Js('pri'), Js('ra'), Js('rae'), Js('rea'), Js('ro'), Js('she'), Js('sho'), Js('sli'), Js('sna'), Js('tae'), Js('the'), Js('tho'), Js('tri')]))
var.put('nm3', Js([Js('ban'), Js('bian'), Js('bral'), Js('can'), Js('cian'), Js('ddan'), Js('dial'), Js('dian'), Js('din'), Js('hal'), Js('han'), Js('hian'), Js('lan'), Js('lian'), Js('lin'), Js('llan'), Js('man'), Js('mian'), Js('min'), Js('mman'), Js('nan'), Js('nial'), Js('nian'), Js('nnal'), Js('nnan'), Js('phal'), Js('phian'), Js('phion'), Js('ppan'), Js('ral'), Js('ran'), Js('rian'), Js('rin'), Js('rran'), Js('sal'), Js('san'), Js('sin'), Js('ssin'), Js('stral'), Js('tan'), Js('thian'), Js('tian'), Js('tin'), Js('tral'), Js('xal'), Js('xan'), Js('xian'), Js('xxin')]))
pass
pass


# Add lib to the module scope
hpWingedHorseNames = var.to_python()
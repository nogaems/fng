__all__ = ['gnomeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ba'), Js('Bil'), Js('Bim'), Js('Bin'), Js('Bink'), Js('Bo'), Js('Bom'), Js('Bon'), Js('Bonk'), Js('Bu'), Js('Bur'), Js('Car'), Js('Do'), Js('Don'), Js('Donk'), Js('Di'), Js('Dim'), Js('Din'), Js('Dink'), Js('El'), Js('Fen'), Js('Fil'), Js('Fim'), Js('Fin'), Js('Fink'), Js('Gel'), Js('Gim'), Js('Glim'), Js('Glin'), Js('Glink'), Js('Gno'), Js('Hin'), Js('Hink'), Js('Klo'), Js('La'), Js('Lo'), Js('Mit'), Js('Mittle'), Js('Nit'), Js('Nittle'), Js('Pit'), Js('Pith'), Js('Tal'), Js('Ten'), Js('Teen'), Js('Then'), Js('Thin'), Js('Think'), Js('Tin'), Js('To'), Js('Toc'), Js('Tyn')]))
var.put('nm2', Js([Js('k'), Js('b'), Js('l'), Js('ka'), Js('ba'), Js('la'), Js('lo'), Js('bo'), Js('ko'), Js('li'), Js('bi'), Js('ki'), Js('da'), Js('do'), Js('di'), Js('bee'), Js('lee'), Js('kee'), Js('dee'), Js('le'), Js('a'), Js('o'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js('ago'), Js('an'), Js('argo'), Js('arn'), Js('ash'), Js('bick'), Js('bik'), Js('bink'), Js('ble'), Js('brik'), Js('brick'), Js('bus'), Js('dink'), Js('dus'), Js('fink'), Js('finkle'), Js('flink'), Js('fonk'), Js('flonk'), Js('fizz'), Js('go'), Js('gus'), Js('kink'), Js('klink'), Js('klonk'), Js('link'), Js('mac'), Js('mink'), Js('nk'), Js('nus'), Js('onk'), Js('rgo'), Js('sizz'), Js('ris'), Js('tink'), Js('tonk'), Js('tank'), Js('think'), Js('thin'), Js('ulo'), Js('vash'), Js('vizz'), Js('wick'), Js('win'), Js('wack'), Js('wizz')]))
var.put('nm4', Js([Js('Ba'), Js('Bil'), Js('Bim'), Js('Bin'), Js('Bink'), Js('Bip'), Js('Bix'), Js('Bixi'), Js('Bo'), Js('Bon'), Js('By'), Js('Bur'), Js('Car'), Js('Di'), Js('Dim'), Js('Din'), Js('Dink'), Js('Do'), Js('El'), Js('Fen'), Js('Fil'), Js('Fim'), Js('Fyn'), Js('Fynk'), Js('Gel'), Js('Gim'), Js('Gin'), Js('Ginn'), Js('Glin'), Js('Glink'), Js('Gno'), Js('Gyn'), Js('Gynn'), Js('Hin'), Js('Hink'), Js('Jul'), Js('Kat'), Js('Kath'), Js('Kel'), Js('Ket'), Js('Keth'), Js('Kit'), Js('Kith'), Js('Klo'), Js('La'), Js('Lis'), Js('Liss'), Js('Lo'), Js('Lym'), Js('Lys'), Js('Lyss'), Js('Mer'), Js('Mit'), Js('Mittle'), Js('Nit'), Js('Nittle'), Js('Pit'), Js('Pith'), Js('Syr'), Js('Seel'), Js('Soo'), Js('Tal'), Js('Tan'), Js('Teel'), Js('Teen'), Js('Ten'), Js('Then'), Js('Thin'), Js('Think'), Js('Til'), Js('Tin'), Js('To'), Js('Toc'), Js('Tyl'), Js('Tyn')]))
var.put('nm5', Js([Js('ky'), Js('by'), Js('la'), Js('lo'), Js('bo'), Js('ko'), Js('li'), Js('bi'), Js('ki'), Js('da'), Js('do'), Js('di'), Js('bee'), Js('lee'), Js('kee'), Js('dee'), Js('le'), Js('a'), Js('o'), Js('y'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('ago'), Js('an'), Js('arn'), Js('ash'), Js('bick'), Js('bik'), Js('bink'), Js('ble'), Js('brik'), Js('brick'), Js('bus'), Js('dink'), Js('dinkey'), Js('dinkle'), Js('dus'), Js('fink'), Js('finkle'), Js('flink'), Js('flynk'), Js('fonk'), Js('flonk'), Js('fizz'), Js('fizzy'), Js('fizzle'), Js('go'), Js('gus'), Js('kin'), Js('kink'), Js('klinkle'), Js('linkey'), Js('ly'), Js('mac'), Js('mink'), Js('nk'), Js('nus'), Js('onk'), Js('rgo'), Js('sizz'), Js('sizzle'), Js('ris'), Js('tink'), Js('tinkle'), Js('tonk'), Js('think'), Js('thinkle'), Js('thin'), Js('ulo'), Js('vash'), Js('vizz'), Js('vizzle'), Js('wick'), Js('win'), Js('wack')]))
var.put('nm7', Js([Js('Acer'), Js('Berry'), Js('Bizz'), Js('Black'), Js('Cast'), Js('Click'), Js('Cog'), Js('Draxle'), Js('Fast'), Js('Fine'), Js('Fizzle'), Js('Gear'), Js('Grind'), Js('Mecha'), Js('Mekka'), Js('Over'), Js('Porter'), Js('Puddle'), Js('Sad'), Js('Shine'), Js('Short'), Js('Spanner'), Js('Spark'), Js('Spring'), Js('Spry'), Js('Steam'), Js('Storm'), Js('Swift'), Js('Thistle'), Js('Tink'), Js('Tossle'), Js('Twist'), Js('Wobble')]))
var.put('nm8', Js([Js('bang'), Js('blast'), Js('bonk'), Js('bus'), Js('crank'), Js('dwadle'), Js('fizz'), Js('fizzle'), Js('fuse'), Js('fuzz'), Js('gauge'), Js('gear'), Js('grinder'), Js('house'), Js('kettle'), Js('master'), Js('needle'), Js('nozzle'), Js('pipe'), Js('span'), Js('spanner'), Js('spark'), Js('spindle'), Js('spinner'), Js('spring'), Js('sprocket'), Js('steel'), Js('strip'), Js('torque'), Js('whistle'), Js('wizzle'), Js('wrench')]))
pass
pass


# Add lib to the module scope
gnomeNames = var.to_python()
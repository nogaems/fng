__all__ = ['dbHakaishin']

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
    var.put('nm1', Js([Js('Absi'), Js('Ager'), Js('Alus'), Js('Arak'), Js('Arkis'), Js('Arma'), Js('Awa'), Js('Bassi'), Js('Beerus'), Js('Bourbu'), Js('Bouru'), Js('Calva'), Js('Calvad'), Js('Cha'), Js('Champa'), Js('Chi'), Js('Cid'), Js('Cide'), Js('Cog'), Js('Cogna'), Js('Daiqui'), Js('Deira'), Js('Deiras'), Js('Gani'), Js('Ginge'), Js('Gria'), Js('Guino'), Js('Gyn'), Js('Ider'), Js('Ine'), Js('Jen'), Js('Jenev'), Js('Jenne'), Js('Jiu'), Js('Kari'), Js('Karis'), Js('Keffi'), Js('Kefi'), Js('Kumi'), Js('Kuras'), Js('Lagus'), Js('Magna'), Js('Magnac'), Js('Manche'), Js('Manchi'), Js('Marsa'), Js('Mea'), Js('Meada'), Js('Meadas'), Js('Mez'), Js('Mezca'), Js('Moonshi'), Js('Mooshi'), Js('Nac'), Js('Neve'), Js('Never'), Js('Niha'), Js('Pache'), Js('Pagne'), Js('Para'), Js('Paras'), Js('Perie'), Js('Quiri'), Js('Rai'), Js('Raici'), Js('Raicil'), Js('Raki'), Js('Rakis'), Js('Sak'), Js('Sakis'), Js('Sakus'), Js('Sala'), Js('Salas'), Js('Sangris'), Js('Santis'), Js('Shou'), Js('Sin'), Js('Singa'), Js('Sinthe'), Js('Sojus'), Js('Sontis'), Js('Teq'), Js('Teqi'), Js('Tequi'), Js('Tes'), Js('Tonton'), Js('Vado'), Js('Vados'), Js('Vod'), Js('Vodkis'), Js('Waine'), Js('Whis'), Js('Wynn')]))
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
dbHakaishin = var.to_python()
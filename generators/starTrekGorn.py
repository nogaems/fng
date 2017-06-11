__all__ = ['starTrekGorn']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Acu'), Js('Are'), Js('Aza'), Js('Azsa'), Js('Ba'), Js('Besa'), Js('Bra'), Js('Bre'), Js('Dasu'), Js('Deza'), Js('Di'), Js('Dra'), Js('Era'), Js('Esee'), Js('Essa'), Js('Eza'), Js('Fe'), Js('Fee'), Js('Fidi'), Js('Fra'), Js('Ga'), Js('Garee'), Js('Gli'), Js('Graa'), Js('He'), Js('Hesa'), Js('Hi'), Js('Hra'), Js("K'a"), Js("K'sa"), Js("K'staa"), Js('Kee'), Js('Ko'), Js('Kra'), Js('La'), Js('Lazsa'), Js('Lera'), Js('Loze'), Js('Masa'), Js('Me'), Js('Meka'), Js('Mo'), Js('Morsi'), Js('Na'), Js('Ne'), Js('Neko'), Js('Nha'), Js('Re'), Js('Reri'), Js('Rla'), Js('Roza'), Js("S'a"), Js("S'ka"), Js("S'kaa"), Js("S'la"), Js("S'ree"), Js("S'sa"), Js("S'sha"), Js("S'slee"), Js("S'sme"), Js("S'sne"), Js("S'sra"), Js("S'sta"), Js("S'ta"), Js("S'taa"), Js("S'tra"), Js("S'za"), Js('See'), Js('Sla'), Js('So'), Js('Sozze'), Js('Sra'), Js('Sree'), Js('Tare'), Js('Tee'), Js('Tha'), Js('Tra'), Js('Xa'), Js('Xazi'), Js('Xee'), Js('Xra'), Js('Zho'), Js('Zo'), Js('Zogo'), Js('Zra')]))
var.put('nm2', Js([Js('bahr'), Js('bas'), Js('bet'), Js('bizs'), Js('bus'), Js('cees'), Js('ch'), Js('chat'), Js('chium'), Js('cus'), Js('d'), Js('daar'), Js('das'), Js('dous'), Js('drees'), Js('g'), Js('gazs'), Js('get'), Js('girb'), Js('gozin'), Js('hlik'), Js('hr'), Js('hrid'), Js('hris'), Js('hs'), Js('k'), Js('kah'), Js('kan'), Js('kazs'), Js('kouk'), Js('l'), Js('lak'), Js('lath'), Js('let'), Js('leus'), Js('lis'), Js('lk'), Js('llk'), Js('m'), Js('mal'), Js('mar'), Js('msek'), Js('mus'), Js('n'), Js('nbet'), Js('nd'), Js('ndas'), Js('nzaar'), Js('r'), Js('rash'), Js('rd'), Js('rith'), Js('rozs'), Js('rr'), Js('s'), Js('sek'), Js('sh'), Js('sibus'), Js('ss'), Js('szan'), Js('tar'), Js('tezs'), Js('th'), Js('this'), Js('ts'), Js('yah'), Js('yak'), Js('yas'), Js('yin'), Js('yith'), Js('z'), Js('zaar'), Js('zin'), Js('zs'), Js('zzan')]))
pass
pass


# Add lib to the module scope
starTrekGorn = var.to_python()
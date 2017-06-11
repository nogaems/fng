__all__ = ['starTrekRemans']

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
var.put('nm1', Js([Js('Aku'), Js('Anra'), Js('Ari'), Js('Axio'), Js('Bera'), Js('Bi'), Js('Bia'), Js('Bru'), Js('Dena'), Js('Dira'), Js('Do'), Js('Dri'), Js('Ja'), Js('Jeru'), Js('Jia'), Js('Jo'), Js('Ka'), Js('Kara'), Js('Kia'), Js('Kru'), Js('Lira'), Js('Lita'), Js('Lo'), Js('Lori'), Js('Me'), Js('Mekri'), Js('Mi'), Js('Mia'), Js('Na'), Js('Ni'), Js('Nira'), Js('Nori'), Js('Obi'), Js('Onu'), Js('Ora'), Js('Ovi'), Js("R'Da"), Js("R'Ki"), Js("R'Ve"), Js("R'Xi"), Js('Ra'), Js('Rena'), Js('Ria'), Js('Risu'), Js("S'Ha"), Js("S'Ki"), Js("S'Ma"), Js("S'Ri"), Js('Sa'), Js('Si'), Js('Sio'), Js('Sira'), Js('Tare'), Js('Te'), Js('Tena'), Js('Ti'), Js('Tira'), Js('Via'), Js('Vkru'), Js('Vri'), Js('Vro'), Js('Xa'), Js('Xena'), Js('Xio'), Js('Xiro')]))
var.put('nm2', Js([Js('clado'), Js('clek'), Js('crek'), Js('crix'), Js('kad'), Js('karix'), Js('kir'), Js('kirud'), Js('kix'), Js('krax'), Js('krikuk'), Js('kruvek'), Js('kuk'), Js('marik'), Js('mek'), Js('mix'), Js('mosik'), Js('muk'), Js('narix'), Js('natek'), Js('nuk'), Js('nuvik'), Js('nux'), Js('rad'), Js('rarix'), Js('rix'), Js('ruk'), Js('ruvix'), Js('sarix'), Js('sek'), Js('sik'), Js('srix'), Js('stuk'), Js('tek'), Js('tix'), Js('trik'), Js('tuk'), Js('turik'), Js('vek'), Js('vik'), Js('vrex'), Js('vurik'), Js('vux')]))
pass
pass


# Add lib to the module scope
starTrekRemans = var.to_python()
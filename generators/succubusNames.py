__all__ = ['succubusNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aer'), Js('Arlen'), Js('Azer'), Js('Boren'), Js('Brax'), Js('Bren'), Js('Caran'), Js('Char'), Js('Col'), Js('Cryn'), Js('Dhar'), Js('Drac'), Js('Dyn'), Js('Eor'), Js('Eran'), Js('Ezrin'), Js('Faren'), Js('Fhar'), Js('Forn'), Js('Fyz'), Js('Garan'), Js('Gnar'), Js('Grul'), Js('Har'), Js('Hurin'), Js('Hyir'), Js('Iar'), Js('Igar'), Js('Inor'), Js('Jar'), Js('Jhor'), Js('Joran'), Js('Kran'), Js('Kuron'), Js('Kyl'), Js('Lanar'), Js('Lar'), Js('Lohr'), Js('Mahr'), Js('Maran'), Js('Maz'), Js('Nahar'), Js('Naj'), Js('Nyr'), Js('Ohir'), Js('Ohm'), Js('Oran'), Js('Pam'), Js('Phir'), Js('Prax'), Js('Qahr'), Js('Qrin'), Js('Qur'), Js('Rhar'), Js('Rizar'), Js('Ryz'), Js('Sal'), Js('Sur'), Js('Suran'), Js('Syl'), Js('Thal'), Js('Tor'), Js('Traz'), Js('Unor'), Js('Ur'), Js('Uran'), Js('Vohr'), Js('Vox'), Js('Vyl'), Js('Wahr'), Js('Wes'), Js('Wrax'), Js('Xahr'), Js('Xal'), Js('Xin'), Js('Yhr'), Js('Ylan'), Js('Ynar'), Js('Zael'), Js('Zahr'), Js('Zaran'), Js('Zohn')]))
var.put('nm2', Js([Js('aer'), Js('ahr'), Js('an'), Js('anin'), Js('arax'), Js('aris'), Js('ath'), Js('axis'), Js('ear'), Js('ed'), Js('el'), Js('elon'), Js('enar'), Js('er'), Js('errith'), Js('eth'), Js('ex'), Js('ez'), Js('ied'), Js('igar'), Js('ihr'), Js('ilan'), Js('irad'), Js('ith'), Js('ix'), Js('ixan'), Js('ixar'), Js('lagar'), Js('lahin'), Js('lan'), Js('larin'), Js('lax'), Js('lead'), Js('liar'), Js('lynx'), Js('lyx'), Js('nar'), Js('narax'), Js('near'), Js('neth'), Js('nex'), Js('nihr'), Js('nil'), Js('niran'), Js('nyx'), Js('olan'), Js('on'), Js('orad'), Js('oriad'), Js('orin'), Js('oth'), Js('ovan'), Js('ox'), Js('rad'), Js('rahn'), Js('rel'), Js('renar'), Js('riad'), Js('ryd'), Js('rydar'), Js('ryn'), Js('sahr'), Js('san'), Js('syn'), Js('syx'), Js('tar'), Js('taran'), Js('tihr'), Js('tiran'), Js('trax'), Js('tyz'), Js('vahr'), Js('vile'), Js('viraz'), Js('vix'), Js('vyce'), Js('vyn'), Js('yd'), Js('yhad'), Js('ylan'), Js('ynad'), Js('ynir'), Js('yth'), Js('yx'), Js('yxir')]))
var.put('nm3', Js([Js('Aez'), Js('Aries'), Js('Azaer'), Js('Berin'), Js('Briz'), Js('Bwyn'), Js('Cahr'), Js('Caril'), Js('Cat'), Js('Char'), Js('Daem'), Js('Dhys'), Js('Dren'), Js('Elin'), Js('Eshir'), Js('Elrin'), Js('Fel'), Js('Fyr'), Js('Fyrel'), Js('Fyser'), Js('Ginor'), Js('Glys'), Js('Gryn'), Js('Harel'), Js('Hel'), Js('Hyr'), Js('Iphis'), Js('Irin'), Js('Isir'), Js('Jaen'), Js('Jil'), Js('Jyn'), Js('Kel'), Js('Kryn'), Js('Kyl'), Js('Lil'), Js('Lilin'), Js('Lynn'), Js('Merid'), Js('Mez'), Js('Mhyr'), Js('Nemor'), Js('Ness'), Js('Nym'), Js('Ohir'), Js('Or'), Js('Orin'), Js('Pen'), Js('Phis'), Js('Pris'), Js('Qhes'), Js('Qin'), Js('Qyr'), Js('Rhel'), Js('Ris'), Js('Ryr'), Js('Sar'), Js('Shar'), Js('Shirin'), Js('Shy'), Js('Thel'), Js('Tin'), Js('Tryx'), Js('Uhr'), Js('Uril'), Js('Usin'), Js('Vhes'), Js('Vilin'), Js('Vyl'), Js('Win'), Js('Wylin'), Js('Wys'), Js('Xen'), Js('Xis'), Js('Xyl'), Js('Ynis'), Js('Yrel'), Js('Yser'), Js('Zaeh'), Js('Zarin'), Js('Zell'), Js('Zrix')]))
var.put('nm4', Js([Js('aela'), Js('aith'), Js('ana'), Js('ania'), Js('anya'), Js('arah'), Js('aris'), Js('aya'), Js('eli'), Js('elin'), Js('era'), Js('erris'), Js('esh'), Js('esha'), Js('ess'), Js('eth'), Js('eva'), Js('evera'), Js('iana'), Js('ielle'), Js('ienne'), Js('iesh'), Js('ieth'), Js('ira'), Js('ith'), Js('ixia'), Js('ixis'), Js('lea'), Js('lenne'), Js('less'), Js('lia'), Js('lienne'), Js('lisa'), Js('lith'), Js('lyn'), Js('lyss'), Js('nara'), Js('nell'), Js('nessa'), Js('neth'), Js('ney'), Js('nila'), Js('nixi'), Js('nore'), Js('nys'), Js('ola'), Js('ona'), Js('ora'), Js('oria'), Js('orin'), Js('oris'), Js('oth'), Js('ova'), Js('rahne'), Js('raya'), Js('reia'), Js('relle'), Js('riane'), Js('rya'), Js('ryna'), Js('ryss'), Js('sea'), Js('sha'), Js('sya'), Js('syss'), Js('tarish'), Js('thine'), Js('tia'), Js('tila'), Js('tora'), Js('tyse'), Js('via'), Js('vielle'), Js('vienne'), Js('vyn'), Js('vynia'), Js('vyra'), Js('yera'), Js('yla'), Js('ynore'), Js('yra'), Js('ysh'), Js('ysha'), Js('yss'), Js('yxih')]))
pass
pass


# Add lib to the module scope
succubusNames = var.to_python()
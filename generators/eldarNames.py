__all__ = ['eldarNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names4', 'names2', 'nameGen', 'names3'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('names', (var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2'))))
            else:
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
var.put('names1', Js([Js('Al'), Js('Am'), Js('Amo'), Js('Amon'), Js('Ar'), Js('Arag'), Js('Arg'), Js('Arro'), Js('Asur'), Js('Bahar'), Js('Bale'), Js('Bar'), Js('Bara'), Js('Baran'), Js('Bel'), Js('Bele'), Js('Bene'), Js('Bore'), Js('Caen'), Js('Caer'), Js('Caera'), Js('Cal'), Js('Dal'), Js('Dara'), Js('Don'), Js('Dun'), Js('El'), Js('Elam'), Js('Elra'), Js('Esar'), Js('Faen'), Js('Fan'), Js('Far'), Js('For'), Js('Fue'), Js('Gala'), Js('Galan'), Js('Gil'), Js('Gilfa'), Js('Gon'), Js('Gul'), Js('Idra'), Js('Idran'), Js('Iril'), Js('Ise'), Js('Isen'), Js('Kae'), Js('Kal'), Js('Karan'), Js('Kay'), Js('Kel'), Js('Lae'), Js('Lan'), Js('Lau'), Js('Len'), Js('Lo'), Js('Mach'), Js('Mau'), Js('Men'), Js('Mene'), Js('Mener'), Js('Mor'), Js('Morro'), Js('Ola'), Js('On'), Js('Ora'), Js('Oro'), Js('Osu'), Js('Tae'), Js('Tal'), Js('Tan'), Js('Ten'), Js('Yl'), Js('Yra'), Js('Ysu')]))
var.put('names2', Js([Js('baer'), Js('ban'), Js('bas'), Js('bryn'), Js('byn'), Js('davar'), Js('deer'), Js('dor'), Js('drad'), Js('dras'), Js('duin'), Js('gan'), Js('gard'), Js('gen'), Js('groth'), Js('hidon'), Js('hith'), Js('hyn'), Js('kas'), Js('kin'), Js('kon'), Js('kyn'), Js('las'), Js('lath'), Js('leath'), Js('leth'), Js('lim'), Js('lion'), Js('lon'), Js('lyth'), Js('maer'), Js('mar'), Js('mas'), Js('men'), Js('mes'), Js('mon'), Js('more'), Js('naer'), Js('nar'), Js('nedor'), Js('nel'), Js('nyl'), Js('rad'), Js('ran'), Js('ranel'), Js('rendil'), Js('rian'), Js('riel'), Js('rion'), Js('rith'), Js('ros'), Js('roth'), Js('ruin'), Js('rys'), Js('saar'), Js('san'), Js('seith'), Js('sen'), Js('seth'), Js('shin'), Js('shor'), Js('sys'), Js('tar'), Js('tari'), Js('telar'), Js('thanil'), Js('tharal'), Js('thorn'), Js('tien'), Js('tyr'), Js('van'), Js('var'), Js('vel'), Js('vor'), Js('vyn')]))
var.put('names3', Js([Js('Al'), Js('Aem'), Js('Ami'), Js('Aeme'), Js('Ali'), Js('Ara'), Js('Aris'), Js('Arre'), Js('Ashe'), Js('Baha'), Js('Bela'), Js('Baer'), Js('Baera'), Js('Balan'), Js('Bel'), Js('Baele'), Js('Behne'), Js('Bore'), Js('Caen'), Js('Cela'), Js('Caella'), Js('Cel'), Js('Dil'), Js('Dera'), Js('Den'), Js('Daen'), Js('El'), Js('Ela'), Js('Elra'), Js('Elsar'), Js('Faen'), Js('Fen'), Js('Fir'), Js('Fo'), Js('Fae'), Js('Gela'), Js('Gellan'), Js('Gil'), Js('Gilsa'), Js('Gen'), Js('Gil'), Js('Ilra'), Js('Ilro'), Js('Irli'), Js('Ise'), Js('Isen'), Js('Kae'), Js('Khel'), Js('Kaera'), Js('Kay'), Js('Kel'), Js('Lae'), Js('Lana'), Js('Lae'), Js('Len'), Js('Li'), Js('Mes'), Js('Mae'), Js('Mena'), Js('Mene'), Js('Menel'), Js('Meh'), Js('Mello'), Js('Ola'), Js('One'), Js('Ore'), Js('Osi'), Js('Oasa'), Js('Tae'), Js('Tel'), Js('Taphe'), Js('Ten'), Js('Yl'), Js('Yna'), Js('Yse')]))
var.put('names4', Js([Js('bala'), Js('benne'), Js('bera'), Js('brae'), Js('bryn'), Js('daen'), Js('daer'), Js('dole'), Js('dona'), Js('dra'), Js('dynn'), Js('gil'), Js('gith'), Js('gren'), Js('gwen'), Js('hina'), Js('hish'), Js('hynn'), Js('kae'), Js('keza'), Js('kia'), Js('kra'), Js('laeth'), Js('lara'), Js('leth'), Js('lira'), Js('lith'), Js('lone'), Js('lya'), Js('lyth'), Js('mae'), Js('mela'), Js('mena'), Js('mere'), Js('mia'), Js('myn'), Js('myna'), Js('nae'), Js('nel'), Js('nelle'), Js('nera'), Js('nys'), Js('rana'), Js('raniel'), Js('rena'), Js('ria'), Js('riel'), Js('rio'), Js('ris'), Js('rith'), Js('rosa'), Js('rye'), Js('ryna'), Js('rys'), Js('sa'), Js('sae'), Js('sela'), Js('shae'), Js('sho'), Js('sis'), Js('sya'), Js('sys'), Js('tara'), Js('tela'), Js('tera'), Js('thala'), Js('thanis'), Js('tiren'), Js('tyra'), Js('tys'), Js('vae'), Js('vara'), Js('vela'), Js('vena'), Js('vyss')]))
pass
pass


# Add lib to the module scope
eldarNames = var.to_python()
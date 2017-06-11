__all__ = ['draeneiNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3'))))
            else:
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
var.put('nm1', Js([Js('Aho'), Js('Ak'), Js('Ar'), Js('Art'), Js('Az'), Js('Beh'), Js('Beho'), Js('Bra'), Js("Bran'"), Js('Bre'), Js('Cae'), Js('Caed'), Js('Cem'), Js('Dek'), Js('Der'), Js('Dere'), Js("Dran'"), Js('Du'), Js('Dug'), Js('Eoc'), Js('Fal'), Js('Fan'), Js('Fin'), Js('Fun'), Js('Ga'), Js('Gan'), Js('Han'), Js('Har'), Js('Hob'), Js('Hoba'), Js('Iz'), Js('Jov'), Js('Kav'), Js('Kel'), Js('Kha'), Js('Kil'), Js('Luc'), Js('Ma'), Js('Mah'), Js('Maho'), Js('Mu'), Js('Mua'), Js('Nah'), Js('Naho'), Js('Nob'), Js('Nobu'), Js('Oc'), Js('Ock'), Js('On'), Js('Os'), Js('Rem'), Js('Ste'), Js('Tal'), Js('Tho'), Js('Tor'), Js('Tora'), Js('Toral'), Js('Uz'), Js('Vel'), Js("Vel'"), Js('Ven'), Js('Vor'), Js('Yil')]))
var.put('nm2', Js([Js('g'), Js('n'), Js('ph'), Js('f'), Js('r'), Js('t'), Js('h'), Js('d'), Js('m'), Js('ga'), Js('na'), Js('pha'), Js('fa'), Js('ra'), Js('ta'), Js('ha'), Js('da'), Js('ma'), Js('go'), Js('no'), Js('pho'), Js('fo'), Js('ro'), Js('to'), Js('ho'), Js('do'), Js('mo'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js('aam'), Js('aan'), Js('ag'), Js('aid'), Js('allius'), Js('allus'), Js('alus'), Js('am'), Js('an'), Js('anaar'), Js('anos'), Js('ard'), Js('as'), Js('at'), Js('ath'), Js('co'), Js('daan'), Js('diir'), Js('ed'), Js('el'), Js('en'), Js('fik'), Js('iir'), Js('il'), Js('in'), Js('ir'), Js('iru'), Js('is'), Js('khen'), Js('lac'), Js('lag'), Js('lat'), Js('liir'), Js('lir'), Js('luun'), Js('mat'), Js('miir'), Js('miis'), Js('mir'), Js('mis'), Js('mos'), Js('naar'), Js('nan'), Js('niir'), Js('nis'), Js('ogg'), Js('omat'), Js('onan'), Js('ord'), Js('orhan'), Js('oth'), Js('ras'), Js('red'), Js('tun'), Js('ul'), Js('undo'), Js('uun')]))
var.put('nm4', Js([Js('Aal'), Js('Ael'), Js('Aelle'), Js('Aello'), Js('Aev'), Js('Aeva'), Js('Aeve'), Js('Al'), Js('Alta'), Js('Av'), Js('Ava'), Js('Ave'), Js('Ba'), Js('Bet'), Js('Bel'), Js('Bil'), Js('Cuz'), Js('Ed'), Js('Edi'), Js('Edir'), Js('Ego'), Js('El'), Js('Elle'), Js('Ello'), Js('En'), Js('Er'), Js('Ere'), Js('Far'), Js('Fe'), Js('Fin'), Js('Go'), Js('Gor'), Js('Got'), Js('Haf'), Js('Hafe'), Js('Ir'), Js('Ire'), Js('Ires'), Js('Is'), Js('Ja'), Js('Jael'), Js('Jal'), Js('Ji'), Js('Jol'), Js('Kha'), Js('Kaz'), Js('Lun'), Js('Luna'), Js('Ma'), Js('Mah'), Js('Mam'), Js('Mer'), Js('Mes'), Js('Mi'), Js('Mia'), Js('Mo'), Js('Mom'), Js('Mon'), Js('Mu'), Js('Muh'), Js('Mum'), Js('Mus'), Js('Ne'), Js('Nes'), Js('Nur'), Js('Nurg'), Js('Nus'), Js('Pha'), Js('Phae'), Js('Phe'), Js('Rem'), Js('Reme'), Js('Ruk'), Js('Se'), Js('Ses'), Js('Si'), Js('Sul'), Js('Thel'), Js('Thela'), Js('Tre'), Js('Tri'), Js('Um'), Js('Ura'), Js('Val'), Js('Valu')]))
var.put('nm5', Js([Js('b'), Js('ba'), Js('be'), Js('bo'), Js('d'), Js('da'), Js('de'), Js('do'), Js('h'), Js('ha'), Js('he'), Js('ho'), Js('la'), Js('le'), Js('lo'), Js('r'), Js('ra'), Js('re'), Js('ro'), Js('s'), Js('sa'), Js('se'), Js('so'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('aan'), Js('al'), Js('all'), Js('ally'), Js('araa'), Js('ca'), Js('dine'), Js('ela'), Js('elle'), Js('elli'), Js('era'), Js('ere'), Js('ett'), Js('ette'), Js('gin'), Js('guni'), Js('haa'), Js('hi'), Js('hri'), Js('in'), Js('ine'), Js('irah'), Js('kua'), Js('la'), Js('laa'), Js('laana'), Js('lae'), Js('laena'), Js('lun'), Js('mae'), Js('mena'), Js('mere'), Js('mis'), Js('mon'), Js('nii'), Js('nora'), Js('oh'), Js('ora'), Js('raa'), Js('rah'), Js('ran'), Js('ret'), Js('rette'), Js('ri'), Js('rii'), Js('rua'), Js('sa'), Js('stra'), Js('straa'), Js('taa'), Js('ti'), Js('tia'), Js('tra'), Js('traa'), Js('ua'), Js('un'), Js('uni'), Js('zi')]))
pass
pass


# Add lib to the module scope
draeneiNames = var.to_python()
__all__ = ['lamiaNames']

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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
            else:
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
var.put('nm1', Js([Js('Absyr'), Js('Acast'), Js('Acher'), Js('Adelph'), Js('Adr'), Js('Aeac'), Js('Aes'), Js('Aesc'), Js('Agath'), Js('Alc'), Js('Alex'), Js('Alph'), Js('Amph'), Js('Amyc'), Js('Anast'), Js('Anaszt'), Js('Anath'), Js('Anc'), Js('Anch'), Js('Anst'), Js('Ant'), Js('Antiph'), Js('Aphol'), Js('Aphr'), Js('Arist'), Js('Ars'), Js('Arth'), Js('Ashat'), Js('Ath'), Js('Athan'), Js('Bas'), Js('Bast'), Js('Baz'), Js('Bras'), Js('Buth'), Js('Caes'), Js('Caphan'), Js('Cas'), Js('Cast'), Js('Cel'), Js('Ceph'), Js('Cir'), Js('Cyr'), Js('Das'), Js('Dath'), Js('Demith'), Js('Demoph'), Js('Deph'), Js('Deuc'), Js('Dionys'), Js('Eph'), Js('Eras'), Js('Erasm'), Js('Eus'), Js('Eust'), Js('Hel'), Js('Heph'), Js('Her'), Js('Hesp'), Js('Ibys'), Js('Icel'), Js('Inach'), Js('Iphicr'), Js('Iphit'), Js('Isocr'), Js('Ix'), Js('Jas'), Js('Kos'), Js('Kosm'), Js('Krath'), Js('Laest'), Js('Lich'), Js('Lox'), Js('Lyc'), Js('Lys'), Js('Mops'), Js('Mos'), Js('Naph'), Js('Nis'), Js('Ocean'), Js('Oediph'), Js('Orthr'), Js('Paph'), Js('Parth'), Js('Pestr'), Js('Phaeth'), Js('Phal'), Js('Phalaem'), Js('Phant'), Js('Phil'), Js('Phleg'), Js('Phyl'), Js('Phrix'), Js('Priaph'), Js('Proph'), Js('Protes'), Js('Pyras'), Js('Rasm'), Js('Rist'), Js('Salm'), Js('Scop'), Js('Socr'), Js('Sot'), Js('Soter'), Js('Spyr'), Js('Stam'), Js('Stef'), Js('Steph'), Js('Taras'), Js('Thadd'), Js('Thal'), Js('Than'), Js('Tharas'), Js('Thelam'), Js('Theoph'), Js('Ther'), Js('Therr'), Js('Thers'), Js('Thes'), Js('Thim'), Js('Thit'), Js('Thyest'), Js('Troph'), Js('Tyliss'), Js('Typh'), Js('Ulyss'), Js('Vas'), Js('Vasil'), Js('Xanth'), Js('Xen'), Js('Xerx'), Js('Xuth'), Js('Zal'), Js('Zeph'), Js('Zet')]))
var.put('nm2', Js([Js('ades'), Js('adus'), Js('aestus'), Js('aethon'), Js('aeus'), Js('alus'), Js('amas'), Js('anos'), Js('anthus'), Js('aphus'), Js('apius'), Js('aris'), Js('as'), Js('asius'), Js('asos'), Js('astos'), Js('astus'), Js('ates'), Js('athan'), Js('athis'), Js('atius'), Js('atos'), Js('aus'), Js('ax'), Js('eas'), Js('edes'), Js('eithes'), Js('elaus'), Js('elix'), Js('elos'), Js('elous'), Js('elphos'), Js('ephon'), Js('epios'), Js('erios'), Js('eros'), Js('ersis'), Js('erus'), Js('es'), Js('eseus'), Js('esio'), Js('etheus'), Js('ethon'), Js('etrios'), Js('etus'), Js('eus'), Js('exei'), Js('exia'), Js('exis'), Js('iaraus'), Js('ias'), Js('ice'), Js('idas'), Js('illes'), Js('inos'), Js('ios'), Js('ippus'), Js('ips'), Js('ipus'), Js('is'), Js('ises'), Js('isius'), Js('iss'), Js('iste'), Js('isthus'), Js('istos'), Js('ithous'), Js('itos'), Js('itrius'), Js('itus'), Js('ix'), Js('ixi'), Js('ixus'), Js('obus'), Js('ochus'), Js('ocia'), Js('oebus'), Js('oeus'), Js('olas'), Js('olos'), Js('oneus'), Js('onis'), Js('oph'), Js('ophe'), Js('ophon'), Js('ophor'), Js('ophoros'), Js('orus'), Js('os'), Js('ose'), Js('osyne'), Js('otheos'), Js('othius'), Js('ous'), Js('ukas'), Js('us'), Js('ux'), Js('ypnos'), Js('yptus'), Js('yrtus'), Js('ys'), Js('ysios'), Js('yx')]))
var.put('nm3', Js([Js('Acal'), Js('Acos'), Js('Acs'), Js('Adoz'), Js('Adras'), Js('Ael'), Js('Aeth'), Js('Akis'), Js('Aleth'), Js('Alethr'), Js('Alex'), Js('Amath'), Js('Amiph'), Js('Anth'), Js('Aph'), Js('Areth'), Js('Ash'), Js('Astr'), Js('Ath'), Js('Athil'), Js('Athiz'), Js('Axiph'), Js('Bath'), Js('Breth'), Js('Calyph'), Js('Cast'), Js('Chal'), Js('Cir'), Js('Cnass'), Js('Creph'), Js('Creth'), Js('Daph'), Js('Daphn'), Js('Dios'), Js('Dor'), Js('Eriph'), Js('Eth'), Js('Ethem'), Js('Euph'), Js('Euth'), Js('Evith'), Js('Galix'), Js('Gath'), Js('Harph'), Js('Has'), Js('Hys'), Js('Ias'), Js('Idaph'), Js('Iph'), Js('Is'), Js('Kaliph'), Js('Kaph'), Js('Kath'), Js('Kis'), Js('Kiss'), Js('Kleph'), Js('Leph'), Js('Leuc'), Js('Lis'), Js('Lith'), Js('Lys'), Js('Math'), Js('Meniph'), Js('Meph'), Js('Mess'), Js('Mis'), Js('Myrith'), Js('Myst'), Js('Neph'), Js('Nes'), Js('Neth'), Js('Nix'), Js('Nys'), Js('Nysh'), Js('Nyx'), Js('Olith'), Js('Ophi'), Js('Oreth'), Js('Oriph'), Js('Orph'), Js('Othr'), Js('Paph'), Js('Pas'), Js('Pesh'), Js('Peth'), Js('Phaeth'), Js('Phais'), Js('Phal'), Js('Pher'), Js('Phil'), Js('Pho'), Js('Phrix'), Js('Phys'), Js('Pix'), Js('Prax'), Js('Pris'), Js('Prix'), Js('Pros'), Js('Psal'), Js('Rhaen'), Js('Rheth'), Js('Sab'), Js('Sag'), Js('Sal'), Js('Salaph'), Js('Sam'), Js('Saph'), Js('Savar'), Js('Sel'), Js('Selest'), Js('Sil'), Js('Sin'), Js('Sylph'), Js('Syn'), Js('Syr'), Js('Taph'), Js('Thal'), Js('Than'), Js('Theam'), Js('Thean'), Js('Theis'), Js('Thel'), Js('Thes'), Js('Thesp'), Js('Thos'), Js('Thron'), Js('Thyx'), Js('Xan'), Js('Zel'), Js('Zeph'), Js('Zeux')]))
var.put('nm4', Js([Js('acia'), Js('aeia'), Js('ahria'), Js('aia'), Js('ais'), Js('ali'), Js('alise'), Js('allis'), Js('alphia'), Js('anea'), Js('anise'), Js('anthe'), Js('anthei'), Js('aphaura'), Js('aphine'), Js('assa'), Js('assea'), Js('axaura'), Js('axise'), Js('ea'), Js('easi'), Js('edice'), Js('eila'), Js('eilise'), Js('eilla'), Js('eis'), Js('eisa'), Js('eithe'), Js('eleia'), Js('elia'), Js('elis'), Js('elphise'), Js('elsa'), Js('enia'), Js('enis'), Js('eosis'), Js('ephia'), Js('ephila'), Js('ephine'), Js('eris'), Js('ertes'), Js('ertise'), Js('eshi'), Js('esi'), Js('esis'), Js('essei'), Js('ethe'), Js('ethia'), Js('ethis'), Js('etis'), Js('eusa'), Js('ia'), Js('iaphe'), Js('iasse'), Js('iax'), Js('ice'), Js('iche'), Js('ilis'), Js('ine'), Js('inix'), Js('ionis'), Js('iophai'), Js('iphae'), Js('iphaeia'), Js('iphe'), Js('iphei'), Js('iphelia'), Js('iphi'), Js('iphia'), Js('iphis'), Js('iphise'), Js('iphite'), Js('iphoia'), Js('is'), Js('isa'), Js('ise'), Js('isei'), Js('isha'), Js('ishae'), Js('ishia'), Js('ishis'), Js('isia'), Js('issis'), Js('istae'), Js('ite'), Js('ithe'), Js('ithea'), Js('ithis'), Js('ithise'), Js('ithoe'), Js('iusei'), Js('ixa'), Js('ixera'), Js('ixia'), Js('ixie'), Js('oche'), Js('oesa'), Js('ohsa'), Js('olphi'), Js('one'), Js('ophai'), Js('ophe'), Js('opheu'), Js('ophi'), Js('ophia'), Js('ophila'), Js('ophis'), Js('ophise'), Js('orise'), Js('osa'), Js('ose'), Js('osi'), Js('osia'), Js('osise'), Js('ossia'), Js('thise'), Js('usa'), Js('usei'), Js('usi'), Js('ymes'), Js('yphe'), Js('yphise'), Js('ypise'), Js('ypso'), Js('yse'), Js('yxio'), Js('yxo')]))
pass
pass


# Add lib to the module scope
lamiaNames = var.to_python()
__all__ = ['mayanNames']

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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Acan'), Js('Acat'), Js('Ah Ciliz'), Js('Ah Mun'), Js('Ah Tabai'), Js("Ah-Bolom-Dz'acab"), Js('Ah-Bolom-Tzacab'), Js('Ah-Cancum'), Js('Ah-Chun-Caan'), Js('Ah-Chuy-Kat'), Js('Ah-Ciliz'), Js('Ah-Cun-Can'), Js('Ah-Cuxtal'), Js('Ah-Hulneb'), Js('Ah-Kin'), Js('Ah-Kinchil'), Js('Ah-Kuhmix-Unicob'), Js('Ah-Mun'), Js('Ah-Muzencab'), Js('Ah-Patnar-Unicob'), Js('Ah-Pekku'), Js('Ah-Puch'), Js('Ah-Tabai'), Js("Ah-Uncir-Dz'acab"), Js('Ah-Uuc-Ticab'), Js('Ah-Xoc-Xin'), Js('Ahau Chamahez'), Js('Ahau-Chamahez'), Js('Ahau-Kin'), Js('Ahluic'), Js('Ahmakiq'), Js('Ahmucen-Cab'), Js('Ahulane'), Js('Ajbit'), Js('Ajtzak'), Js('Akbit'), Js('Alom'), Js('Atl'), Js('Backlum Chaam'), Js('Balam'), Js('Bitol'), Js("Bolon-D'zacab"), Js('Buluc-Chabtan'), Js('Cabaguil'), Js('Cabrakan'), Js('Cacoch'), Js('Cakulha'), Js('Camalotz'), Js('Camaxtli'), Js('Camazotz'), Js('Caprakan'), Js('Chac'), Js('Chac-Uayab-Xoc'), Js('Chamer'), Js('Chicahua'), Js('Chicchan'), Js('Chipahua'), Js('Cit-Bolon-Tum'), Js('Cizin'), Js('Colop-U-Uichikin'), Js('Cotzbalam'), Js('Coyopa'), Js('Cualli'), Js('Cuauc'), Js('Cuchumaquic'), Js('Cum Hau'), Js('Ekchauh'), Js('Ekchuah'), Js('Eztli'), Js('Gucumatz'), Js('Gucup Cakix'), Js('Gukumatz'), Js("Hacha'kyum"), Js('Hapikern'), Js('Hobnil'), Js('Hozanek'), Js('Hun Batz'), Js('Hun-Batz'), Js('Hun-Came'), Js('Hun-Cane'), Js('Hun-Chowen'), Js('Hun-Hunahpu'), Js('Hun-Nal-Ye'), Js('Hunab-Ku'), Js('Hunaphu'), Js('Hunaphu-Gutch'), Js('Hunaphu-Utiu'), Js('Huracan'), Js('Ikal'), Js('Iktan'), Js('Itzam-Ye'), Js('Itzamatul'), Js('Itzamna'), Js('Ix'), Js('Ix-Tub-Tun'), Js('Ixbalanque'), Js('Ixmacane'), Js('Ixmucane'), Js('Ixpiyacoc'), Js('Izel'), Js("K'awai"), Js("K'awi"), Js('Kabil'), Js('Kan'), Js('Kan-U-Uayeyab'), Js('Kan-Xib-Yui'), Js('Kawil'), Js('Kianto'), Js('Kichigonai'), Js('Kinich Ahau'), Js('Kinich Kakmo'), Js('Kisin'), Js('Kukulcan'), Js('Manik'), Js('Metnal'), Js('Mitnal'), Js('Mulac'), Js('Muluc'), Js('Nacon'), Js('Nanochacyum'), Js('Necahual'), Js('Och-Kan'), Js('Papan'), Js('Pawahtuun'), Js('Poxlom'), Js("Q'uq'umatz"), Js('Qaholom'), Js('Tecumbalam'), Js('Tepeu'), Js('Teyacapan'), Js('Tlacolotl'), Js('Tohil'), Js('Tzacol'), Js('Tzultacaj'), Js('Uc-Zip'), Js('Usukan'), Js('Uyitzin'), Js('Voltan'), Js('Votan'), Js('Vucub-Caquix'), Js('Vukub-Cakix'), Js('Vukubcane'), Js('Xaman Ek'), Js("Xaman'Ek"), Js('Xamaniqinqu'), Js('Xbalanque'), Js('Xecotcovach'), Js('Xibalba'), Js('Xipil'), Js('Xpiayoc'), Js('Xumucane'), Js('Yaluk'), Js('Yantho'), Js('Yaotl'), Js('Yum Caax'), Js('Yum Cimil'), Js('Yumbalamob'), Js('Yumchakob'), Js('Zac-Cimi'), Js('Zipacna'), Js('Zotz'), Js('Zyanya')]))
var.put('nm2', Js([Js('Ah-Uaynih'), Js('Ah-Wink-Ir-Masa'), Js('Akhustal'), Js('Akna'), Js('Alaghom-Naom-Tzentel'), Js('Amoxtili'), Js('Chachiuitl'), Js('Chen'), Js('Chichuaton'), Js('Chimalmat'), Js('Chin'), Js('Chirakan-Ixmucane'), Js('Citlali'), Js('Citlamina'), Js('Colel'), Js('Colel Cab'), Js('Coszcatl'), Js('Cualli'), Js('Eleuia'), Js('Ichtaca'), Js('Ihuicatl'), Js('Iktan'), Js('Itotia'), Js('Itzamatul'), Js('Itzel'), Js('Iuitl'), Js('Ix Kaknab'), Js('Ixazaluoh'), Js('Ixazalvoh'), Js('Ixchel'), Js('Ixcuiname'), Js('Ixik'), Js('Ixtab'), Js('Ixtel'), Js('Ixtli'), Js('Mecatl'), Js('Meztli'), Js('Nelli'), Js('Nenetl'), Js('Patli'), Js('Sacniete'), Js('Sacnite'), Js('Tecuith'), Js('Tepin'), Js('Tlalli'), Js('Tonalnan'), Js('Xmucane'), Js('Xoc'), Js('Xochitl'), Js('Xoco'), Js('Xpiayoc'), Js('Xquic'), Js('Xquiq'), Js('Yatzil'), Js('Yoltzin'), Js('Zac-Kuk'), Js('Zeltzin'), Js('Zyanya')]))
pass
pass


# Add lib to the module scope
mayanNames = var.to_python()
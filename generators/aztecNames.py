__all__ = ['aztecNames']

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
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', var.get('nm4').get(var.get('rnd')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', var.get('nm1').get(var.get('rnd')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', (var.get('nm2').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Acalan'), Js('Acamapichtli'), Js('Achcauhtli'), Js('Acolmixtli'), Js('Ahuiliztli'), Js('Ahuitzotl'), Js('Amoxtli'), Js('Atl'), Js('Axayacatl'), Js('Camaxtli'), Js('Chicahua'), Js('Chimalli'), Js('Chimalpopoca'), Js('Chipahua'), Js('Cipac'), Js('Cipactli'), Js('Citlali'), Js('Citlalli'), Js('Coatl'), Js('Coyotl'), Js('Cozahtli'), Js('Cualli'), Js('Cuauhtemoc'), Js('Cuauhtl'), Js('Cuetlachtli'), Js('Cuetzpalli'), Js('Cuixtli'), Js('Ehecatl'), Js('Eleuia'), Js('Eloxochitl'), Js('Etalpalli'), Js('Eztli'), Js('Huemac'), Js('Huitzilihuitl'), Js('Huitzilin'), Js('Huitzilli'), Js('Huitzitl'), Js('Huitztecol'), Js('Iccauhtli'), Js('Ichtaca'), Js('Icnoyotl'), Js('Ihuicatl'), Js('Ilhicamina'), Js('Ilhuitl'), Js('Itotia'), Js('Itzcali'), Js('Itzcoatl'), Js('Itzcuintli'), Js('Itzli'), Js('Itztli'), Js('Iuitl'), Js('Ixtli'), Js('Ixtlilxochitl'), Js('Izel'), Js('Mahuizoh'), Js('Manauia'), Js('Matlal'), Js('Matlalihuitl'), Js('Maxtla'), Js('Mazatl'), Js('Mecatl'), Js('Meztli'), Js('Mictlantecuhtli'), Js('Milintica'), Js('Miztli'), Js('Momoztli'), Js('Montezuma'), Js('Moquihuix'), Js('Moyolehuani'), Js('Nahuatl'), Js('Namacuix'), Js('Natlalihuitl'), Js('Necahual'), Js('Necalli'), Js('Necuametl'), Js('Nelli'), Js('Nezahualcoyotl'), Js('Nezahualpilli'), Js('Nochehuatl'), Js('Nochtli'), Js('Nopaltzin'), Js('Ocelotl'), Js('Ocuil'), Js('Ohtli'), Js('Olli'), Js('Ollin'), Js('Ozomatli'), Js('Patli'), Js('Quauhtli'), Js('Quetzalcoatl'), Js('Tapayaxi'), Js('Tecolotl'), Js('Tenoch'), Js('Teoxihuitl'), Js('Tepiltzin'), Js('Tepin'), Js('Tezcacoatl'), Js('Tezozomoc'), Js('Tizoc'), Js('Tlacaelel'), Js('Tlacelel'), Js('Tlachinolli'), Js('Tlalli'), Js('Tlaloc'), Js('Tlanextic'), Js('Tlanextli'), Js('Tlazohtlaloni'), Js('Tlazopilli'), Js('Tlexictli'), Js('Tlilpotonqui'), Js('Tochtli'), Js('Toltecatl'), Js('Tonauac'), Js('Topiltzin'), Js('Tototl'), Js('Tupac'), Js('Ueman'), Js('Uetzcayotl'), Js('Xicohtencatl'), Js('Xihuitl'), Js('Xipil'), Js('Xipilli'), Js('Xiuhcoatl'), Js('Xiuhpilli'), Js('Xochipepe'), Js('Xochipilli'), Js('Xochitl'), Js('Yaotl'), Js('Yayauhqui'), Js('Yolotli'), Js('Yolyamanitzin'), Js('Zipactonal'), Js('Zolin'), Js('Zuma')]))
var.put('nm2', Js([Js('Achcauh'), Js('Ahuiliz'), Js('Amox'), Js('Azcalxochi'), Js('Cente'), Js('Chalchiuh'), Js('Chalchiui'), Js('Chica'), Js('Chicome'), Js('Chimal'), Js('Chipa'), Js('Cihua'), Js('Citla'), Js('Citlal'), Js('Coa'), Js('Coszca'), Js('Cozama'), Js('Cual'), Js('Cuica'), Js('Eloxo'), Js('Eren'), Js('Etal'), Js('Ez'), Js('Hue'), Js('Huitzil'), Js('Huitzili'), Js('Iccauh'), Js('Ich'), Js('Icnoyo'), Js('Ihuica'), Js('Ilhica'), Js('Ilhui'), Js('Ito'), Js('Itz'), Js('Iui'), Js('Ix'), Js('Ixca'), Js('Mahui'), Js('Malinal'), Js('Maza'), Js('Meca'), Js('Mez'), Js('Miahua'), Js('Miyaoa'), Js('Mizqui'), Js('Momoz'), Js('Moyole'), Js('Nahua'), Js('Neca'), Js('Nel'), Js('Nene'), Js('Noch'), Js('Noxochi'), Js('Oh'), Js('Pa'), Js('Que'), Js('Quetzal'), Js('Quiauh'), Js('Sac'), Js('Te'), Js('Tei'), Js('Teoxi'), Js('Teui'), Js('Teya'), Js('Tla'), Js('Tlachi'), Js('Tlah'), Js('Tlal'), Js('Tlanex'), Js('Tlazoh'), Js('Tlexic'), Js('Toch'), Js('Tolte'), Js('Tonal'), Js('Xi'), Js('Xihui'), Js('Xilo'), Js('Xio'), Js('Xitlal'), Js('Xiuh'), Js('Xo'), Js('Xochi'), Js('Xoco'), Js('Yao'), Js('Yare'), Js('Yayauh'), Js('Yol'), Js('Yoli'), Js('Yolo'), Js('Yolyamani'), Js('Zani'), Js('Zel'), Js('Zya')]))
var.put('nm3', Js([Js('capan'), Js('catl'), Js('chel'), Js('chitl'), Js('co'), Js('coatl'), Js('coehua'), Js('coh'), Js('cotl'), Js('cotzin'), Js('coztli'), Js('cui'), Js('cuih'), Js('dira'), Js('hua'), Js('hual'), Js('huani'), Js('huitl'), Js('li'), Js('lotl'), Js('ma'), Js('mac'), Js('mara'), Js('mina'), Js('nan'), Js('nen'), Js('nite'), Js('noch'), Js('nolli'), Js('nya'), Js('pa'), Js('palli'), Js('pan'), Js('pil'), Js('pilli'), Js('pin'), Js('quetzal'), Js('qui'), Js('taca'), Js('tia'), Js('ticue'), Js('tli'), Js('ton'), Js('tonal'), Js('tzal'), Js('tzi'), Js('tzin'), Js('xahual'), Js('xaual'), Js('xiuitl'), Js('xoch'), Js('xochitl'), Js('yah'), Js('yotl'), Js('zoh')]))
var.put('nm4', Js([Js('Achcauhtli'), Js('Ahuiliztli'), Js('Amoxtli'), Js('AmoxtliAtl'), Js('Atl'), Js('Azcalxochitzin'), Js('Centehua'), Js('Chalchiuhticue'), Js('Chalchiuitl'), Js('Chicahua'), Js('Chicomecoatl'), Js('Chimalma'), Js('Chipahua'), Js('Cihuaton'), Js('Citlali'), Js('Citlalli'), Js('Citlalmina'), Js('Coaxoch'), Js('Coszcatl'), Js('Cozamalotl'), Js('Cualli'), Js('Cuicatl'), Js('Eleuia'), Js('Eloxochitl'), Js('Erendira'), Js('Etalpalli'), Js('Eztli'), Js('Huemac'), Js('Huitzilihuitl'), Js('Huitzilli'), Js('Iccauhtli'), Js('Ichtaca'), Js('Icnoyotl'), Js('Ihuicatl'), Js('Ilhicamina'), Js('Ilhuitl'), Js('Itotia'), Js('Itzel'), Js('Itztli'), Js('Iuitl'), Js('Ixcatzin'), Js('Ixchel'), Js('Ixtli'), Js('Izel'), Js('Mahuizoh'), Js('Malinalxochitl'), Js('Manauia'), Js('Mazatl'), Js('Mecatl'), Js('Meztli'), Js('Miahuaxiuitl'), Js('Miyaoaxochitl'), Js('Mizquixahual'), Js('Mizquixaual'), Js('Momoztli'), Js('Moyolehuani'), Js('Nahuatl'), Js('Necahual'), Js('Nelli'), Js('Nenetl'), Js('Nochtli'), Js('Noxochicoztli'), Js('Ohtli'), Js('Papa'), Js('Papan'), Js('Patli'), Js('Quetzal'), Js('Quetzalxochitl'), Js('Quiauhxochitl'), Js('Sacnite'), Js('Teicuih'), Js('Teiuc'), Js('Tenoch'), Js('Teoxihuitl'), Js('Tepin'), Js('Teuicui'), Js('Teyacapan'), Js('Tlachinolli'), Js('Tlaco'), Js('Tlacoehua'), Js('Tlacotl'), Js('Tlahco'), Js('Tlahcoehua'), Js('Tlalli'), Js('Tlanextli'), Js('Tlazohtzin'), Js('Tlexictli'), Js('Tochtli'), Js('Toltecatl'), Js('Tonalnan'), Js('Xihuitl'), Js('Xilonen'), Js('Xiloxoch'), Js('Xiomara'), Js('Xipil'), Js('Xitlalli'), Js('Xiuhcoatl'), Js('Xiuhtonal'), Js('Xochicotzin'), Js('Xochipilli'), Js('Xochiquetzal'), Js('Xochitl'), Js('Xochiyotl'), Js('Xoco'), Js('Xocoh'), Js('Xocoyotl'), Js('Yaotl'), Js('Yaretzi'), Js('Yayauhqui'), Js('Yolihuani'), Js('Yolotli'), Js('Yoloxochitl'), Js('Yoltzin'), Js('Yolyamanitzin'), Js('Zaniyah'), Js('Zeltzin'), Js('Zuma'), Js('Zyanya')]))
var.put('nm5', Js([Js('Aca'), Js('Ach'), Js('Acol'), Js('Ahui'), Js('Amox'), Js('Axa'), Js('Camax'), Js('Chica'), Js('Chimal'), Js('Chipa'), Js('Cipac'), Js('Citla'), Js('Citlal'), Js('Coa'), Js('Coyo'), Js('Cozah'), Js('Cual'), Js('Cuauh'), Js('Cuetlach'), Js('Cuetzpal'), Js('Cuix'), Js('Ehe'), Js('Eloxo'), Js('Etal'), Js('Ez'), Js('Hue'), Js('Huitz'), Js('Huitzi'), Js('Huitzil'), Js('Iccauh'), Js('Ich'), Js('Icno'), Js('Ihui'), Js('Ilhi'), Js('Ilhui'), Js('Ito'), Js('Itz'), Js('Iui'), Js('Ix'), Js('Ixtli'), Js('Mahui'), Js('Mat'), Js('Matlali'), Js('Max'), Js('Maza'), Js('Meca'), Js('Mez'), Js('Mictlan'), Js('Milin'), Js('Miz'), Js('Momoz'), Js('Monte'), Js('Moqui'), Js('Moyole'), Js('Nahua'), Js('Nama'), Js('Natlali'), Js('Neca'), Js('Necal'), Js('Necua'), Js('Nel'), Js('Nezahual'), Js('Noch'), Js('Noche'), Js('Nopal'), Js('Ocelo'), Js('Oh'), Js('Ol'), Js('Ozoma'), Js('Pa'), Js('Quauh'), Js('Quetzal'), Js('Tapa'), Js('Te'), Js('Tecolo'), Js('Teoxi'), Js('Tepil'), Js('Tezca'), Js('Tezo'), Js('Ti'), Js('Tla'), Js('Tlacae'), Js('Tlace'), Js('Tlachi'), Js('Tlal'), Js('Tlanex'), Js('Tlazo'), Js('Tlazoht'), Js('Tlexic'), Js('Tlilpo'), Js('Toch'), Js('Tolteca'), Js('Topil'), Js('Toto'), Js('Uetz'), Js('Xicoh'), Js('Xihui'), Js('Xipil'), Js('Xiuh'), Js('Xochi'), Js('Yao'), Js('Yayauh'), Js('Yolo'), Js('Yolyamani'), Js('Zipac'), Js('Zo'), Js('Zu')]))
var.put('nm6', Js([Js('cali'), Js('camina'), Js('catl'), Js('cauhtli'), Js('cayotl'), Js('chitl'), Js('coatl'), Js('coyotl'), Js('cuintli'), Js('cuix'), Js('hua'), Js('hual'), Js('huani'), Js('huatl'), Js('huitl'), Js('huix'), Js('lal'), Js('laloni'), Js('lan'), Js('lel'), Js('li'), Js('lihuitl'), Js('lin'), Js('liztli'), Js('loc'), Js('lxochitl'), Js('mac'), Js('mapichtli'), Js('metl'), Js('mixtli'), Js('nolli'), Js('palli'), Js('pepe'), Js('pilli'), Js('pin'), Js('popoca'), Js('qui'), Js('taca'), Js('tecol'), Js('tecuhtli'), Js('temoc'), Js('tencatl'), Js('tia'), Js('tic'), Js('tica'), Js('tla'), Js('tli'), Js('tonal'), Js('tonqui'), Js('tzin'), Js('tzotl'), Js('yacatl'), Js('yaxi'), Js('yotli'), Js('zoc'), Js('zoh'), Js('zomoc'), Js('zuma')]))
pass
pass


# Add lib to the module scope
aztecNames = var.to_python()
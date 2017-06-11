__all__ = ['assyrianNames']

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
var.put('nm1', Js([Js('Hermes'), Js('Nenos'), Js('Toma'), Js('Abazu'), Js('Abel'), Js('Abudemio'), Js('Adad-nirari'), Js('Adad-salulu'), Js('Adamu'), Js('Adasi'), Js('Ador'), Js('Ador eil'), Js('Ador palasar'), Js('Aileen'), Js('Ajdina'), Js('Akhiban'), Js('Akhiqar'), Js('Akhiseen'), Js('Akiya'), Js('Aminu'), Js('Ammina'), Js('Anlel'), Js('Anokeen'), Js('Apiashal'), Js('Aprim'), Js('Aram'), Js('Aram seen'), Js('Arik-den-ili'), Js('Arseen'), Js('Ashur'), Js('Ashur ban'), Js('Ashur dan'), Js('Ashur leed'), Js('Ashur ram'), Js('Ashur seen'), Js('Ashur-Dan'), Js('Ashur-apla-idi'), Js('Ashur-bel-nisheshu'), Js('Ashur-dugul'), Js('Ashur-etil-ilani'), Js('Ashur-nadin-ahhe'), Js('Ashur-nadin-apli'), Js('Ashur-nasir-pal'), Js('Ashur-nirari'), Js('Ashur-rabi'), Js('Ashur-rim-nisheshu'), Js('Ashur-shaduni'), Js('Ashur-uballit'), Js('Ashurbanipal'), Js('Asinum'), Js('Asor'), Js('Asor khadon'), Js('Asu'), Js('Athan'), Js('Atrus'), Js('Aulada'), Js('Aumana'), Js('Auneir'), Js('Aurnina'), Js('Awa'), Js('Awbaleet'), Js('Awi bail'), Js('Awi eil'), Js('Awidan'), Js('Awimalich'), Js('Awinam'), Js('Awiqam'), Js('Awiram'), Js('Awiseen'), Js('Awitar'), Js('Awiya'), Js('Awrahim'), Js('Awshalim'), Js('Azarah'), Js('Bail'), Js('Bailbrone'), Js('Baildan'), Js('Bailnam'), Js('Bailram'), Js('Bailseen'), Js('Bailshar'), Js('Banipal'), Js('Bardeen'), Js('Bardisan'), Js('Bareil'), Js('Barseen'), Js('Barsheen'), Js('Baryamin'), Js('Baryoom'), Js('Bazaya'), Js('Bel-bani'), Js('Belu'), Js('Bibla'), Js('Binatour'), Js('Bineil'), Js('Borseen'), Js('Dani eil'), Js('Dem ashur'), Js('Dem atour'), Js('Dem eil'), Js('Dem seen'), Js('Didanu'), Js('Dinkha'), Js('Domara'), Js('Dorara'), Js('Eil'), Js('Eilbra'), Js('Eilbroon'), Js('Eilmar'), Js('Eilram'), Js('Eliya'), Js('Enlil'), Js('Enlil-kudurri-usur'), Js('Enlil-nasir'), Js('Enlil-nirari'), Js('Eriba-Adad'), Js('Erishum'), Js('ErishumI'), Js('Esarhaddon'), Js('Esho'), Js('Gamri eil'), Js('Gawri eil'), Js('Gbar eil'), Js('Giliana'), Js('Ha wail'), Js('Habib'), Js('Hadirseen'), Js('Hale'), Js('Hamed'), Js('Hanodeen'), Js('Hanu'), Js('Harharu'), Js('Harshu'), Js('Hayani'), Js('Hda eil'), Js('Ikunum'), Js('Ila-kabkabu'), Js('Ilu-Mer'), Js('Ilu-shuma'), Js('Imshu'), Js('Ipqi-Ishtar'), Js('Iptar-Sin'), Js('Ishme-Dagan'), Js('Khaled'), Js('Khalil'), Js('Khammo'), Js('Khnan eil'), Js('Khnan seen'), Js('KhnanishoAa'), Js('Khnanya'), Js('Khonayn'), Js('Khza eil'), Js('Kikkiya'), Js('Kushi'), Js('Laith'), Js('Lammo bail'), Js('Lammo eil'), Js('Libaya'), Js('Lullaya'), Js('Madsa'), Js('Malik'), Js("Man'nah"), Js('Mandaru'), Js('Mar bail'), Js('Mar eil'), Js('Mardeen'), Js('Mardokh'), Js('Maro eil'), Js('Marodeen'), Js('Maron'), Js('Marona'), Js('Meesha'), Js('Mekha eil'), Js('Mlimar'), Js('Musa'), Js('Mut-Ashkur'), Js('NaSsir'), Js('Nabo'), Js('Nabo bail'), Js('Nabo eil'), Js('Nabo need'), Js('Nabo pal'), Js('Nabo ram'), Js('Naheer seen'), Js('Nahroona'), Js('Naram eil'), Js('Naram seen'), Js('Naram-Suen'), Js('Nardeen'), Js('Nasir-Sin'), Js('Nasirpal'), Js('Natan'), Js('Natni eil'), Js('Nebu'), Js('Nebuchadnezzar'), Js('Neen eil'), Js('Nin seen'), Js('Nineel'), Js('Ninos'), Js('Ninurta-apal-Ekur'), Js('Nirar'), Js('Nosard eil'), Js('Nuabu'), Js('Nur-ili'), Js('Paldeen'), Js('Paseena'), Js('Pera'), Js('Pnu eil'), Js('Pol'), Js('Puzur-Ashur'), Js('Rab bail'), Js('Rab eil'), Js('Rab seen'), Js('Rabila'), Js('Rabona'), Js('Rafa eil'), Js('Ram bail'), Js('Ram eil'), Js('Ram seen'), Js('Raman'), Js('Ramsen'), Js('Rimush of Assyria'), Js('Romrama'), Js('Samani'), Js('Sard eil'), Js('Sardanapal'), Js('Sargon'), Js('Seen'), Js('Seen eil'), Js('Seena'), Js('Semiramis'), Js('Sennacherib'), Js("Sha'ol"), Js('Shalim-ahum'), Js('Shalmaneser'), Js('Shalmanisar'), Js('Shammina'), Js('Shamshi-Adad'), Js('Shar eil'), Js('Sharma-Adad'), Js('Sharo'), Js('Sharokeen'), Js('Shaybo'), Js('Shimmokeen'), Js('Shmou eil'), Js('Shnina'), Js('Shu-Ninua'), Js('Sin-namir'), Js('Sin-shar-ishkun'), Js('Sin-shumu-lishir'), Js('Suhlamu'), Js('Sulili'), Js('Tiglath-Pileser'), Js('Ttwa eil'), Js('Tudiya'), Js('Tukulti-Ninurta'), Js('Ushpia'), Js('Ward eil'), Js('Ward seen'), Js('Warda'), Js('Wardeen'), Js('Yadida'), Js('Yakmeni'), Js('Yakmesi'), Js('Yangi'), Js('Yau seen'), Js('Yaw bail'), Js('Yaw eil'), Js('Yazkur-el'), Js('Yomadan'), Js('Zah eil'), Js('Zah seen'), Js('Zaia'), Js('Zda eil'), Js('Zomaya'), Js('Zuabu')]))
var.put('nm2', Js([Js('Mariam'), Js('Nardeen'), Js('Yamima'), Js('Danila'), Js('Sadi'), Js('Abella'), Js('Achadina'), Js('Adorina'), Js('Akhita'), Js('Anochina'), Js('Aramina'), Js('Arbella'), Js('Ari eil'), Js('Ashourina'), Js('Asia'), Js('Asia'), Js('Asiah'), Js('Atourina'), Js('Aurhai'), Js('Aurya'), Js('Awijil'), Js('Awita'), Js('Baila'), Js('Baileet'), Js('Beerta'), Js('Bet eil'), Js('Biblina'), Js('Brat bail'), Js('Brat eil'), Js('Brat youm'), Js('Damrina'), Js('Domarina'), Js('Eilbrat'), Js('Eilina'), Js('Emmita'), Js("Hani'ata"), Js('Hano'), Js('Huda'), Js('Ishtar'), Js('Ishtar'), Js('Khannah'), Js('Kushi'), Js('Larsa'), Js('Lawita'), Js('Lea'), Js('Leah'), Js('Leah'), Js('Leja'), Js('Lejka'), Js('Lelu'), Js('Lilith'), Js('Lolita'), Js('Lwita'), Js('Madjida'), Js('Marbita'), Js('Mardina'), Js('Marina'), Js('Marjanita'), Js('Marnita'), Js('Martha'), Js('Milta'), Js('Muneera'), Js('Nahida'), Js('Nahrina'), Js('Naramsina'), Js('Nardina'), Js('Nashiram'), Js('Nasibin'), Js('Nineveh'), Js('Ninorta'), Js('Ninsina'), Js('Ninsun'), Js('Osmet'), Js('Paldina'), Js('Panna'), Js('Pari'), Js('Ramina'), Js('Ramsina'), Js('Rashomta'), Js('Rdita'), Js('Sahdina'), Js('Sawrina'), Js('Shamiram'), Js('Shamiran'), Js('Shamyran'), Js('Shamreta'), Js('Shamrina'), Js('Shamura'), Js('Sharokina'), Js('Shimta'), Js('Shirat'), Js('Simta'), Js('Sorme'), Js('Ur'), Js('Walita'), Js('Wardina'), Js('Wardiya'), Js('Yaeeta'), Js('Yata'), Js('Yayota')]))
pass
pass


# Add lib to the module scope
assyrianNames = var.to_python()
__all__ = ['maoriNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen', 'names3'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', ((var.get('names2').get(var.get('rnd'))+Js(' '))+var.get('names3').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Ahera'), Js('Ahia'), Js('Ahuru'), Js('Aika'), Js('Aketu'), Js('Amako'), Js('Amiri'), Js('Amonga'), Js('Anaru'), Js('Anewa'), Js('Arama'), Js('Ariki'), Js('Atama'), Js('Atua'), Js('Eau'), Js('Eiwi'), Js('Ekara'), Js('Eraka'), Js('Erehe'), Js('Erepu'), Js('Erorangi'), Js('Eru'), Js('Eruera'), Js('Eteka'), Js('Eti'), Js('Hakara'), Js('Hamahona'), Js('Hamakona'), Js('Hamonga'), Js('Hangakore'), Js('Hani'), Js('Hanu'), Js('Hare'), Js('Haru'), Js('Hemi'), Js('Heriko'), Js('Hirini'), Js('Hohepa'), Js('Hori'), Js('Huatare'), Js('Iaka'), Js('Ianga'), Js('Ikei'), Js('Imua'), Js('Io'), Js('Iramai'), Js('Itu'), Js('Kae'), Js('Kahi'), Js('Kahorere'), Js('Kauri'), Js('Kea'), Js('Keka'), Js('Kiki'), Js('Kingi'), Js('Kiri'), Js('Kiwi'), Js('Koro'), Js('Maaka'), Js('Mahora'), Js('Maiope'), Js('Maipi'), Js('Mairo'), Js('Maka'), Js('Manu'), Js('Marama'), Js('Maro'), Js('Matewa'), Js('Mikaere'), Js('Mirama'), Js('Moana'), Js('Mokihi'), Js('Nahi'), Js('Naihi'), Js('Nanui'), Js('Napo'), Js('Natana'), Js('Ngaire'), Js('Okiara'), Js('Opi'), Js('Oraora'), Js('Ori'), Js('Otikoro'), Js('Paau'), Js('Pahu'), Js('Paipa'), Js('Paipau'), Js('Paiwa'), Js('Paiwai'), Js('Pakanga'), Js('Paki-Iwi'), Js('Pana'), Js('Pango'), Js('Paora'), Js('Patariki'), Js('Petera'), Js('Piki'), Js('Piripi'), Js('Pita'), Js('Poto'), Js('Puta'), Js('Raiepe'), Js('Raione'), Js('Rana'), Js('Rangi'), Js('Raru'), Js('Rawiri'), Js('Rera'), Js('Rewi'), Js('Rongo'), Js('Rua'), Js('Ruhi'), Js('Ruki'), Js('Ruru'), Js('Taanga'), Js('Taaura'), Js('Tahiwai'), Js('Taipo'), Js('Tama'), Js('Tamati'), Js('Tana'), Js('Tane'), Js('Tangaroa'), Js('Taonga'), Js('Tapu'), Js('Tiki'), Js('Timoti'), Js('Tipene'), Js('Tua'), Js('Tuna'), Js('Tupai'), Js('Turi'), Js('Uamutu'), Js('Ungu'), Js('Uniki'), Js('Urepa'), Js('Urepo'), Js('Uru Reio'), Js('Uru Tonga'), Js('Urutu'), Js('Wa'), Js('Waiapi'), Js('Waiara'), Js('Waraki'), Js('Whiro'), Js('Wiremu'), Js('Witi')]))
var.put('names2', Js([Js('Ahuaiti'), Js('Ai Kauri'), Js('Aia'), Js('Airini'), Js('Aka'), Js('Akona'), Js('Aku'), Js('Akumatua'), Js('Amiria'), Js('Anahera'), Js('Ani'), Js('Ano Matao'), Js('Ao Mania'), Js('Aperira'), Js('Aputa'), Js('Areta'), Js('Aroha'), Js('Arona'), Js('Aronui'), Js('Ataahua'), Js('Atamarie'), Js('Ea'), Js('Eitu'), Js('Emere'), Js('Ena'), Js('Enutanga'), Js('Erihapeti'), Js('Eriki'), Js('Erina'), Js('Ha Amu'), Js('Haki'), Js('Hakina'), Js('Hara'), Js('Harakoke'), Js('Heeni'), Js('Hine'), Js('Huhana'), Js('Ie'), Js('Ihanga'), Js('Ihiko'), Js('Iria'), Js('Irihapeti'), Js('Kaewa'), Js('Keke'), Js('Kiri'), Js('Kura'), Js('Lani'), Js('Maa Rei'), Js('Maata'), Js('Mahuika'), Js('Maia'), Js('Maiore'), Js('Mairana'), Js('Makareta'), Js('Makei'), Js('Makoro'), Js('Makuku'), Js('Makutu'), Js('Mami'), Js('Manewa'), Js('Marama'), Js('Marika'), Js('Mere'), Js('Mirama'), Js('Moana'), Js('Mokihi'), Js('Naihi'), Js('Nako'), Js('Neina'), Js('Neni'), Js('Neumia'), Js('Newea'), Js('Nga Mimi'), Js('Ngaio'), Js('Ngaire'), Js('Oea'), Js('Oenga'), Js('Oia'), Js('Oie'), Js('Oki'), Js('Okitu'), Js('Oma'), Js('Omaka'), Js('Ori'), Js('Paiti'), Js('Pakeha'), Js('Pakeka'), Js('Pania'), Js('Panoti'), Js('Pianga'), Js('Pihi'), Js('Pipi'), Js('Pora'), Js('Poroka'), Js('Poto'), Js('Pouriwa'), Js('Puhi'), Js('Rakina Au'), Js('Ramarie'), Js('Rangi'), Js('Rangi Area'), Js('Rea'), Js('Reka'), Js('Rere'), Js('Riana'), Js('Roha'), Js('Roimata'), Js('Rona'), Js('Ruhi'), Js('Ruiha'), Js('Ruihi'), Js('Tahi-Popa'), Js('Tahupotiki'), Js('Taikaroa'), Js('Taiko'), Js('Taimana'), Js('Taiomi'), Js('Tapu'), Js('Tarore'), Js('Te Pura'), Js('Tui'), Js('Uariki'), Js('Ukuroa'), Js('Urangi'), Js('Urehu'), Js('Uri Kino'), Js('Uri Wai'), Js('Uru Manau'), Js('Uru Pari'), Js('Uru Rewa'), Js('Uru Tarangi'), Js('Uruanga'), Js('Uruau'), Js('Uruewa'), Js('Wa'), Js('Waauru'), Js('Waewai'), Js('Wai Oro'), Js('Wai Paku'), Js('Waiano'), Js('Waikomanawa'), Js('Whetu'), Js('Whina')]))
var.put('names3', Js([Js('Akarana'), Js('Aperahama'), Js('Arana'), Js('Arepata'), Js('Arona'), Js('Arono'), Js('Eketone'), Js('Enoka'), Js('Hakopa'), Js('Hamuera'), Js('Hamutana'), Js('Hariwana'), Js('Henare'), Js('Herangi'), Js('Herewini'), Js('Himona'), Js('Hohepa'), Js('Karaka'), Js('Karauna'), Js('Kawhena'), Js('Keeti'), Js('Kerehoma'), Js('Keretene'), Js('Kingi'), Js('Manuera'), Js('Matene'), Js('Mete'), Js('Munu'), Js('Natana'), Js('Nepe'), Js('Nopera'), Js('Paora'), Js('Paraone'), Js('Pekama'), Js('Petera'), Js('Pihere'), Js('Pihopa'), Js('Pikari'), Js('Piripi'), Js('Puhipi'), Js('Raharuhi'), Js('Rakena'), Js('Rara'), Js('Rata'), Js('Rehipeti'), Js('Romana'), Js('Ropata'), Js('Taera'), Js('Tahana'), Js('Taimana'), Js('Taimona'), Js('Tame'), Js('Tamihana'), Js('Taneti'), Js('Tapihana'), Js('Teira'), Js('Tereiti'), Js('Terere'), Js('Tiki'), Js('Timoti'), Js('Tipene'), Js('Topia'), Js('Waaka'), Js('Waata'), Js('Wati'), Js('Watihana'), Js('Wetere'), Js('Wihone'), Js('Wikiriwhi'), Js('Winiata'), Js('Wirihana'), Js('Witika')]))
pass
pass


# Add lib to the module scope
maoriNames = var.to_python()
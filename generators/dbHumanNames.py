__all__ = ['dbHumanNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen', 'namesMale', 'namesFemale'])
@Js
def PyJsHoisted_nameGen_(namesFirst, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'namesFirst':namesFirst}, var)
    var.registers(['names1', 'result', 'namesFirst'])
    var.put('names1', var.get('namesFirst'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('names', var.get('names1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('namesMale', Js([Js('Acon'), Js('Acoron'), Js('Aise'), Js('Alamond'), Js('Alcoh'), Js('Almon'), Js('Ayos'), Js('Bakpa'), Js('Bakpak'), Js('Barush'), Js('Batone'), Js('Batto'), Js('Beare'), Js('Bedd'), Js('Beere'), Js('Bere'), Js('Bereef'), Js('Bet'), Js('Bouk'), Js('Braed'), Js('Bred'), Js('Brieve'), Js('Brus'), Js('Butta'), Js('Caff'), Js('Calcula'), Js('Callacu'), Js('Cassew'), Js('Chap'), Js('Chapz'), Js('Char'), Js('Chayer'), Js('Chaznut'), Js('Chesnu'), Js('Cilpen'), Js('Coco'), Js('Coconu'), Js('Coff'), Js('Cohol'), Js('Conut'), Js('Cray'), Js('Cube'), Js('Culator'), Js('Darc'), Js('Darrek'), Js('Delnoo'), Js('Dennim'), Js('Dimsu'), Js('Dinnem'), Js('Drawar'), Js('Drawe'), Js('Eci'), Js('Faso'), Js('Fizz'), Js('Fizzy'), Js('Forook'), Js('Fungu'), Js('Futo'), Js('Gallue'), Js('Garmant'), Js('Garmen'), Js('Geenz'), Js('Glew'), Js('Gus'), Js('Hazzel'), Js('Jaenz'), Js('Jean'), Js('Juiz'), Js('Juze'), Js('Krad'), Js('Krof'), Js('Ligh'), Js('Lite'), Js('Makker'), Js('Marka'), Js('Milke'), Js('Millek'), Js('Naife'), Js('Naive'), Js('Niar'), Js('Noudel'), Js('Painte'), Js('Panz'), Js('Payned'), Js('Peelo'), Js('Pensil'), Js('Pents'), Js('Phorc'), Js('Pillo'), Js('Pistasio'), Js('Pran'), Js('Prinro'), Js('Pudden'), Js('Puds'), Js('Qube'), Js('Rayne'), Js('Rayo'), Js('Rayon'), Js('Reeb'), Js('Ryce'), Js('Salado'), Js('Salla'), Js('Sano'), Js('Sanow'), Js('Shewca'), Js('Shrim'), Js('Shrin'), Js('Sisor'), Js('Sisso'), Js('Soi'), Js('Soia'), Js('Soofa'), Js('Soya'), Js('Spoune'), Js('Sprinro'), Js('Stachio'), Js('Stapeler'), Js('Stapple'), Js('Staypel'), Js('Storrem'), Js('Strom'), Js('Sumai'), Js('Sumdi'), Js('Taibbel'), Js('Terbut'), Js('Thunda'), Js('Thunder'), Js('Tofoo'), Js('Tonba'), Js('Tonwon'), Js('Trousa'), Js('Trouse'), Js('Truff'), Js('Truffel'), Js('Waine'), Js('Walnu'), Js('Wonto'), Js('Wryce'), Js('Yogu'), Js('Yogur'), Js('Zelnu')]))
var.put('namesFemale', Js([Js('Acore'), Js('Alcohi'), Js('Alicoh'), Js('Almo'), Js('Almone'), Js('Ayos'), Js('Bara'), Js('Beckpek'), Js('Bedde'), Js('Beeri'), Js('Bett'), Js('Betto'), Js('Betton'), Js('Biki'), Js('Book'), Js('Bouke'), Js('Brishe'), Js('Brusse'), Js('Buttey'), Js('Caffey'), Js('Calci'), Js('Calculi'), Js('Carmente'), Js('Cashey'), Js('Chaire'), Js('Chare'), Js('Chessynu'), Js('Cilpenne'), Js('Coco'), Js('Coconu'), Js('Coffey'), Js('Coholi'), Js('Conuco'), Js('Corna'), Js('Crayo'), Js('Crayone'), Js('Culati'), Js('Darke'), Js('Deni'), Js('Denime'), Js('Dimsue'), Js('Fizzy'), Js('Forkey'), Js('Fungee'), Js('Fungey'), Js('Garme'), Js('Garmen'), Js('Gerielin'), Js('Glew'), Js('Glu'), Js('Hazel'), Js('Hazzel'), Js('Icorne'), Js('Ise'), Js('Isey'), Js('Jean'), Js('Jeanz'), Js('Juce'), Js('Jucey'), Js('Kibini'), Js('Kichey'), Js('Kini'), Js('Kinibi'), Js('Kitchy'), Js('Knaife'), Js('Ladsa'), Js('Ligh'), Js('Lingee'), Js('Lingie'), Js('Lite'), Js('Llowpi'), Js('Melkey'), Js('Milleke'), Js('Naife'), Js('Needle'), Js('Noudelle'), Js('Nucoco'), Js('Painte'), Js('Pannetey'), Js('Pantee'), Js('Parawne'), Js('Payntee'), Js('Penci'), Js('Pentey'), Js('Pillo'), Js('Pilow'), Js('Pista'), Js('Prawne'), Js('Puddey'), Js('Puddy'), Js('Qubey'), Js('Raicey'), Js('Raine'), Js('Rayce'), Js('Rayne'), Js('Sala'), Js('Saladi'), Js('Sano'), Js('Shewca'), Js('Shisu'), Js('Shorette'), Js('Shortee'), Js('Shrimme'), Js('Shumay'), Js('Shumi'), Js('Sisso'), Js('Skurtey'), Js('Sladi'), Js('Sno'), Js('Sofai'), Js('Sorsi'), Js('Soufa'), Js('Soye'), Js('Spinro'), Js('Spone'), Js('Sprinro'), Js('Srimpee'), Js('Stachi'), Js('Stapely'), Js('Stapley'), Js('Storme'), Js('Stormey'), Js('Sueshi'), Js('Sumdi'), Js('Susi'), Js('Tabelle'), Js('Tofi'), Js('Tofue'), Js('Tonwo'), Js('Truffelle'), Js('Truffs'), Js('Undey'), Js('Undi'), Js('Wonto'), Js('Yaso'), Js('Yogi'), Js('Yoguri')]))
pass
pass


# Add lib to the module scope
dbHumanNames = var.to_python()
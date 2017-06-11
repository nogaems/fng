__all__ = ['hittiteNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('Abbi-Teshub'), Js('Akhsheri'), Js('Aki-Teshup'), Js('Akia'), Js('Alakshandu'), Js('Alarandu'), Js('Ambaris'), Js('Ammikhatna'), Js('Anittas'), Js('Anuwanza'), Js('Arame'), Js('Arandas'), Js('Arandash'), Js('Arnuanta'), Js('Arnuwandas'), Js('Artatamash'), Js('Asiri'), Js('Aulkia'), Js('Bakhianu'), Js('Bit-Burutish'), Js('Biyassili'), Js('Burutash'), Js('Dudkaliya'), Js('Dudkhalia'), Js('Dushratta'), Js('Erisinni'), Js('Esarhaddon'), Js('Etaqama'), Js('Gil-Teshup'), Js('Giliyash'), Js('Gunzinanu'), Js('Hasammeli'), Js('Hattusilis'), Js('Hishimisharruma'), Js('Ishganshar'), Js('Ishtanu'), Js('Kali-Teshup'), Js('Karparune'), Js('Katuzili'), Js('Khalpashshulubis'), Js('Khapashshubilish'), Js('Khattasulis'), Js('Khattushar'), Js('Khulli'), Js('Kielranu'), Js('Kil-Teshup'), Js('Kili-Teshup'), Js('Kilundu'), Js('Kundashpi'), Js('Kurirpa'), Js('Kuruntash'), Js('Kushtashpi'), Js('Labarnas'), Js('Lubarna'), Js('Lutipri'), Js('Manapa-Tarhunda'), Js('Manapa-Teshup'), Js('Murshil'), Js('Murshilish'), Js('Mursilis'), Js('Mutallu'), Js('Muttallu'), Js('Muwatalis'), Js('Muwatallis'), Js('Nabushezibanni'), Js('Pappash'), Js('Pikkandu'), Js('Pilandu'), Js('Pisandu'), Js('Pisiris'), Js('Pisirish'), Js('Piyamaradus'), Js('Purutash'), Js('Qatazilu'), Js('Sangar'), Js('Sapalulme'), Js('Sardur'), Js('Shadi-Teshup'), Js('Shalmaneser'), Js('Shama-Teshup'), Js('Sharkenkate-Ashira'), Js('Shaushkash'), Js('Shipa'), Js('Shirindu'), Js('Shubbiluliuma'), Js('Sin-Teshupash'), Js('Suppiliamus'), Js('Suppiliumash'), Js('Suppiluliuma'), Js('Surash'), Js('Surri'), Js('Sutarna'), Js('Sutatarra'), Js('Tarhu'), Js('Tarhunnas'), Js('Tarkhundapi'), Js('Tarkhundaraba'), Js('Tarkhundarabush'), Js('Tarkhuntash'), Js('Tarkondemos'), Js('Tashshu-Dasha'), Js('Te-Teshub'), Js('Telipinus'), Js('Teshub'), Js('Teti'), Js('Tudhaliuas'), Js('Tudhaliyas'), Js('Tudkhalias'), Js('Tudkhaliya'), Js('Tushratta'), Js('Ualli'), Js('Uassurme'), Js('Ullusunu'), Js('Urhiteshub'), Js('Uriah'), Js('Urikki'), Js('Urimme'), Js('Ushkhitti'), Js('Zananzash'), Js('Zannanza'), Js('Zurashar')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
hittiteNames = var.to_python()
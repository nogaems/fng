__all__ = ['sundaneseNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Aa'), Js('Aam'), Js('Aang'), Js('Ace'), Js('Aceng'), Js('Adang'), Js('Ade'), Js('Adeng'), Js('Adun'), Js('Aep'), Js('Agah'), Js('Agan'), Js('Ageng'), Js('Agus'), Js('Ahmad'), Js('Ajang'), Js('Ajat'), Js('Amar'), Js('Amat'), Js('Amin'), Js('Amir'), Js('Ammaar'), Js('Anang'), Js('Aqan'), Js('Asep'), Js('Asta'), Js('Astrajingga'), Js('Atang'), Js('Atep'), Js('Atong'), Js('Badjuri'), Js('Bagja'), Js('Bagong'), Js('Barna'), Js('Bayu'), Js('Botak'), Js('Cahya'), Js('Cece'), Js('Ceceng'), Js('Cecep'), Js('Cepot'), Js('Cucu'), Js('Dadan'), Js('Dadang'), Js('Dana'), Js('Dani'), Js('Dawala'), Js('Dayat'), Js('Deden'), Js('Dedeng'), Js('Dedi'), Js('Dewata'), Js('Dewawarman'), Js('Dian'), Js('Didin'), Js('Djaka'), Js('Durahman'), Js('Ece'), Js('Edi'), Js('Eep'), Js('Elan'), Js('Empep'), Js('Ence'), Js('Encep'), Js('Endang'), Js('Endeung'), Js('Engkos'), Js('Engkus'), Js('Enjang'), Js('Entang'), Js('Fauzan'), Js('Galih'), Js('Gandana'), Js('Ganjar'), Js('Gareng'), Js('Gembira'), Js('Gilang'), Js('Ginanjar'), Js('Gugum'), Js('Gugun'), Js('Gumbira'), Js('Gumelar'), Js('Gun-gun'), Js('Guna'), Js('Hamdan'), Js('Hardi'), Js('Harisdarma'), Js('Harja'), Js('Harsana'), Js('Hendra'), Js('Henhen'), Js('Hikmat'), Js('Idang'), Js('Idi'), Js('Idih'), Js('Ihin'), Js('Ijang'), Js('Indra'), Js('Jajang'), Js('Jaka'), Js('Jalu'), Js('Jangkung'), Js('Jaya'), Js('Jayadarma'), Js('Kabayan'), Js('Kamandaka'), Js('Karta'), Js('Kartasasmita'), Js('Kertarajasa'), Js('Komar'), Js('Koswara'), Js('Kurniawan'), Js('Kuswara'), Js('Kusworo'), Js('Lalan'), Js('Linggabuwana'), Js('Maman'), Js('Mamat'), Js('Markasih'), Js('Marsudi'), Js('Memed'), Js('Mulyana'), Js('Nanang'), Js('Nandang'), Js('Nang'), Js('Nataprawira'), Js('Nugraha'), Js('Odang'), Js('Oleh'), Js('Oman'), Js('Oto'), Js('Otong'), Js('Otoy'), Js('Parta'), Js('Pepep'), Js('Permana'), Js('Petruk'), Js('Prawatasari'), Js('Prawira'), Js('Prawiraharja'), Js('Purnama'), Js('Purnawarman'), Js('Ragasuci'), Js('Raharja'), Js('Rahmat'), Js('Rakha'), Js('Romli'), Js('Rosidi'), Js('Sadeli'), Js('Sanjaya'), Js('Sapari'), Js('Sapariah'), Js('Sasmita'), Js('Sastranagara'), Js('Semar'), Js('Sepri'), Js('Sesep'), Js('Setiadji'), Js('Setiaji'), Js('Sobarna'), Js('Solihin'), Js('Soma'), Js('Somawisesa'), Js('Sudarsana'), Js('Sudarsono'), Js('Sudirja'), Js('Sudrajat'), Js('Suganda'), Js('Sujana'), Js('Sujoni'), Js('Sukarsa'), Js('Sukarso'), Js('Sukarya'), Js('Sumantri'), Js('Supardi'), Js('Sura'), Js('Surawijaya'), Js('Surya'), Js('Suteja'), Js('Sutikno'), Js('Sutisna'), Js('Sutresna'), Js('Sutrisno'), Js('Tangguh'), Js('Tata'), Js('Tatang'), Js('Tetep'), Js('Tirta'), Js('Tisna'), Js('Totong'), Js('Udung'), Js('Ujang'), Js('Ule'), Js('Undang'), Js('Usep'), Js('Uus'), Js('Wahyu'), Js('Waluya'), Js('Wawan'), Js('Wijaya'), Js('Wisesa'), Js('Wowon'), Js('Yanyan'), Js('Yayan'), Js('Yayat')]))
    var.put('nm2', Js([Js('Adang'), Js('Ade'), Js('Ai'), Js('Ani'), Js('Asih'), Js('Atikah'), Js('Ayi'), Js('Cempaka'), Js('Dadah'), Js('Dahlia'), Js('Dasimah'), Js('Dedeh'), Js('Denok'), Js('Dewi'), Js('Diah'), Js('Dian'), Js('Eem'), Js('Een'), Js('Ela'), Js('Ema'), Js('Emar'), Js('Enah'), Js('Enang'), Js('Endah'), Js('Eneng'), Js('Engkom'), Js('Ening'), Js('Enok'), Js('Enong'), Js('Entin'), Js('Eros'), Js('Esih'), Js('Etty'), Js('Euis'), Js('Galuh'), Js('Gina'), Js('Icih'), Js('Ida'), Js('Idah'), Js('Iin'), Js('Ijah'), Js('Imas'), Js('Ira'), Js('Irma'), Js('Ita'), Js('Iteung'), Js('Itoh'), Js('Iyah'), Js('Jayanti'), Js('Kanaya'), Js('Kania'), Js('Karomah'), Js('Kartika'), Js('Kartikasari'), Js('Karto'), Js('Kencana'), Js('Khodijah'), Js('Kokom'), Js('Komariah'), Js('Lia'), Js('Lilis'), Js('Lina'), Js('Malati'), Js('Mamah'), Js('Mariah'), Js('Mariam'), Js('Meida'), Js('Melati'), Js('Nani'), Js('Nenden'), Js('Neneng'), Js('Neni'), Js('Neny'), Js('Nia'), Js('Nining'), Js('Nonon'), Js('Nunung'), Js('Nurlaela'), Js('Nurlela'), Js('Nyai'), Js('Ocih'), Js('Odah'), Js('Omah'), Js('Ombah'), Js('Omoh'), Js('Onong'), Js('Oom'), Js('Pitaloka'), Js('Purbasari'), Js('Puspita'), Js('Putri'), Js('Ratih'), Js('Ratna'), Js('Ratnasari'), Js('Ratnasih'), Js('Ratu'), Js('Rela'), Js('Rella'), Js('Rengganis'), Js('Rusita'), Js('Sadiyah'), Js('Saidah'), Js('Saodah'), Js('Sapariah'), Js('Sari'), Js('Sartika'), Js('Sekar'), Js('Sinar'), Js('Suminar'), Js('Tati'), Js('Teti'), Js('Tia'), Js('Tiktik'), Js('Tini'), Js('Tirta'), Js('Tita'), Js('Titin'), Js('Ule'), Js('Unung'), Js('Wati'), Js('Wida'), Js('Wulan'), Js('Wulansari'), Js('Yani'), Js('Yanti'), Js('Yayah'), Js('Yoyoh'), Js('Yuyu'), Js('Yuyun')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', var.get('nm2').get(var.get('rnd')))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
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
sundaneseNames = var.to_python()
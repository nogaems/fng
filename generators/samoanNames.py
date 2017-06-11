__all__ = ['samoanNames']

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
    var.registers(['nm1', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Afasa'), Js('Afu'), Js('Ainalani'), Js('Akeakami'), Js("Ala'i"), Js('Aleki'), Js('Alepati'), Js('Alesana'), Js('Amosa'), Js('Aneterea'), Js('Apa'), Js('Apelu'), Js('Aperamo'), Js('Apineru'), Js('Apisaloma'), Js('Aputi'), Js('Arona'), Js('Atamu'), Js('Atini'), Js('Elekana'), Js('Eli'), Js('Elia'), Js('Elisaia'), Js('Elisara'), Js('Enele'), Js('Esekielu'), Js('Esera'), Js('Etano'), Js('Etena'), Js('Falaniko'), Js("Falelauli'i"), Js('Falevalu'), Js('Faresa'), Js('Fatu'), Js('Feleti'), Js('Fetu'), Js('Filiki'), Js('Fiti'), Js('Hawea'), Js('Hemana'), Js('Henare'), Js('Iakopo'), Js('Iareto'), Js('Iasona'), Js('Iese'), Js('Ietero'), Js('Ieti'), Js('Ioelu'), Js('Iona'), Js('Ionatana'), Js('Iosefa'), Js('Iosia'), Js('Iosua'), Js('Ira'), Js('Isaako'), Js('Isaia'), Js('Iuta'), Js('Kainano'), Js('Kaisara'), Js('Kalepo'), Js('Kaperielu'), Js('Kiliona'), Js('Kisona'), Js('Kitiona'), Js('Kiuga'), Js('Kuresa'), Js('Lafi'), Js('Lagi'), Js('Laki'), Js('Lalo'), Js('Lasalo'), Js('Leasu'), Js('Levi'), Js('Losi'), Js('Loto'), Js('Malosi'), Js('Manaia'), Js('Manuia'), Js('Mareko'), Js('Mariota'), Js('Mataio'), Js('Mauga'), Js("Mo'e"), Js('Natano'), Js("Ne'igalomeatiga"), Js('Niko'), Js('Nikotemo'), Js('Noa'), Js("Nu'u"), Js('Nunu'), Js('Ofo'), Js('Omeri'), Js('Opetaia'), Js('Pati'), Js('Patolomaio'), Js('Peni'), Js('Peniamina'), Js('Pili'), Js('Pisa'), Js('Pita'), Js("Pu'a"), Js('Pule'), Js('Rangi'), Js('Reupena'), Js('Ropati'), Js('Sailo'), Js('Saipele'), Js('Sakaria'), Js('Salema'), Js('Samasoni'), Js('Samuelu'), Js('Saulo'), Js('Setu'), Js('Siaki'), Js('Siali'), Js('Siaosi'), Js('Sila'), Js('Simi'), Js('Siona'), Js('Sione'), Js('Solomona'), Js('Tala'), Js('Tamasese'), Js('Tamati'), Js('Tamotu'), Js('Tanielu'), Js('Tapu'), Js('Tariua'), Js('Tasura'), Js('Tataio'), Js('Tau'), Js('Taua'), Js('Tavita'), Js('Temetiu'), Js('Timoteo'), Js('Toa'), Js('Tolani'), Js('Toma'), Js('Ualese'), Js('Ualesi'), Js('Ula'), Js('Vai'), Js('Viliamu')]))
    var.put('nm2', Js([Js('Agelu'), Js('Aiono'), Js('Akenese'), Js('Alea'), Js("Ali'tasi"), Js('Alofa'), Js('Ana'), Js('Aokuso'), Js('Aperila'), Js('Apikaila'), Js('Arieta'), Js('Arihi'), Js('Asoese'), Js('Ata'), Js('Atalia'), Js('Elei'), Js('Elisapeta'), Js('Emere'), Js('Eseta'), Js('Etena'), Js('Eunike'), Js('Eva'), Js("Fa'afetai"), Js("Fa'alupe"), Js("Fa'atasi"), Js("Fa'auma"), Js('Faigofie'), Js('Felesita'), Js('Fetu'), Js('Fetuilelagi'), Js('Fiafia'), Js('Fili'), Js('Hana'), Js('Ioana'), Js('Ituau'), Js('Iulia'), Js('Iuni'), Js('Iutita'), Js('Kaila'), Js('Kalautia'), Js('Kanake'), Js('Keise'), Js('Keloe'), Js('Kenese'), Js('Kolone'), Js("La'ei"), Js('Lagi'), Js('Lalago'), Js('Lama'), Js('Lanuola'), Js('Lea'), Js('Leigalo'), Js('Lele'), Js('Lelei'), Js('Lili'), Js('Lisa'), Js('Litia'), Js('Loi'), Js('Lua'), Js('Lulu'), Js('Lupelele'), Js('Lusi'), Js('Makatala'), Js('Makerita'), Js('Malae'), Js('Malamaisaua'), Js('Malia'), Js('Malie'), Js('Manamea'), Js('Maota'), Js('Mara'), Js('Mareta'), Js('Masina'), Js('Mata'), Js('Mere'), Js('Miriama'), Js('Moana'), Js('Mura'), Js('Nafanua'), Js('Naomi'), Js('Natia'), Js('Nuanua'), Js("Onosa'i"), Js('Peka'), Js('Pele'), Js('Penina'), Js('Pepe'), Js('Perenike'), Js('Rongomaiwhenua'), Js("Sa'ea"), Js('Salamasina'), Js('Sali'), Js('Samaria'), Js('Seepa'), Js('Sefina'), Js('Seine'), Js('Siliva'), Js('Sina'), Js('Sinasamoa'), Js('Solosolo'), Js('Suluama'), Js('Taeao'), Js('Tagilima'), Js('Taimane'), Js('Talalelei'), Js('Talia'), Js('Taligi'), Js('Tama'), Js('Tamah'), Js("Tava'esina"), Js('Telila'), Js('Tepora'), Js('Teuila'), Js('Tiana'), Js('Tina'), Js("Tui'uli"), Js('Tupuasa'), Js('Tusila'), Js('Upumoni'), Js('Venis'), Js('Wiki')]))
    var.put('nm3', Js([Js('Afakasi'), Js('Afamasaga'), Js("Ala'ilima"), Js('Alofipo'), Js('Alovili'), Js('Anae'), Js('Apatu'), Js('Asau'), Js('Asiata'), Js('Asoau'), Js('Ausage'), Js('Autagavaia'), Js('Enesi'), Js('Esera'), Js("Fa'amoe"), Js('Faaeteete'), Js('Faamate'), Js('Faamoana'), Js('Faasoo'), Js('Faatasi'), Js('Faiivae'), Js("Fainu'u"), Js('Falagi'), Js('Faleafa'), Js('Fanaafi'), Js('Fanene'), Js('Faraimo'), Js('Faresa'), Js('Fepuleai'), Js('Feresa'), Js('Fiso'), Js('Foai'), Js('Fualema'), Js('Fuga'), Js('Fuima'), Js('Galuvao'), Js('Ierome'), Js('Ioane'), Js('Isaia'), Js('Kuresa'), Js('Latu'), Js('Lavea'), Js("Le'au"), Js("Lea'ai"), Js('Leapai'), Js('Leapama'), Js('Lemalu'), Js('Lemaota'), Js('Leniu'), Js('Leoso'), Js('Levaai'), Js('Levaopolo'), Js('Lofipo'), Js('Lopamaua'), Js('Lotomau'), Js('Lotulelei'), Js('Maiava'), Js('Malaitai'), Js('Malemo'), Js('Manaia'), Js('Matautia'), Js('Maugatai'), Js('Maulalo'), Js('Multiauaopele'), Js('Naea'), Js('Nanai'), Js('Niko'), Js('Niu'), Js('Paea'), Js('Palamo'), Js('Papani'), Js('Pelesa'), Js('Perelini'), Js('Pule'), Js('Pulefaasisina'), Js('Safenu'), Js('Sale'), Js('Salesa'), Js('Saluni'), Js('Sapani'), Js('Sativaa'), Js('Savali'), Js('Savaliga'), Js('Savea'), Js('Seiuli'), Js('Seko'), Js('Seuava'), Js('Sifu'), Js('Silao'), Js('Siosifa'), Js('Siulai'), Js('Suega'), Js('Taalitua'), Js('Taito'), Js('Talatonu'), Js('Tamatoa'), Js('Tameifuna'), Js('Tanielu'), Js('Tau'), Js('Tauaalo'), Js('Taualai'), Js('Tauati'), Js('Taueu'), Js('Taupo'), Js('Tautu'), Js('Tele'), Js('Tilo'), Js('Timu'), Js('Toelau'), Js('Toleafoa'), Js("Tonumaipe'a"), Js('Tuala'), Js('Tufele'), Js('Tui'), Js('Tuiaa'), Js('Tuiasosopo'), Js('Tuigamala'), Js('Tuitama'), Js('Tupu'), Js('Tupua'), Js('Tuputala'), Js("Uta'i"), Js('Vailili'), Js('Vavau')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
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
samoanNames = var.to_python()
__all__ = ['uzbekNames']

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
    var.registers(['nm1', 'nm4', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Abdulaziz'), Js('Abdulghafur'), Js('Abdullah'), Js('Abdulqhafur'), Js('Abubakir'), Js('Ali'), Js('Alisher'), Js('Aminjon'), Js('Arslon'), Js('Ashur'), Js('Ataboy'), Js('Aziz'), Js('Bakir'), Js('Batir'), Js('Bekmirza'), Js('Dadajon'), Js('Davlat'), Js('Dehoan'), Js('Elyor'), Js('Erwat'), Js('Fattah'), Js('Ghafur'), Js('Ghani'), Js('Ghulam'), Js('Hakim'), Js('Hamra'), Js('Hasan'), Js('Hilol'), Js('Holi'), Js('Husan'), Js('Ilyas'), Js('Jora'), Js('Jura'), Js('Kamol'), Js('Karim'), Js('Khafiz'), Js('Khudayberdi'), Js('Kimsan'), Js('Kodir'), Js('Komil'), Js('Latif'), Js('Mahkam'), Js('Malik'), Js('Mamtqul'), Js('Mannon'), Js('Manzur'), Js('Mirzali'), Js('Muhiddin'), Js('Munavvar'), Js('Murtaza'), Js('Musa'), Js('Muzafar'), Js('Nabi'), Js('Narzuqul'), Js('Nasiv'), Js('Niyaz'), Js('Nurmat'), Js('Omar'), Js('Onar'), Js('Oqil'), Js('Orif'), Js('Otkir'), Js('Parpi'), Js('Pazzaq'), Js('Qasim'), Js('Qodir'), Js('Rahim'), Js('Rahmat'), Js('Ruslan'), Js('Rustam'), Js('Saidjahon'), Js('Salim'), Js('Sandjar'), Js('Sattar'), Js('Shakir'), Js('Sharif'), Js('Shavkat'), Js('Shodman'), Js('Shovruk'), Js('Shukrulla'), Js('Sodyq'), Js('Soli'), Js('Sulaymon'), Js('Surat'), Js('Tahir'), Js('Tesha'), Js('Timur'), Js('Tohta'), Js('Toshmat'), Js('Toychi'), Js('Tursan'), Js('Tursun'), Js('Ulfat'), Js('Umid'), Js('Usman'), Js('Usmon'), Js('Vali'), Js('Yarmat'), Js('Yoldash'), Js('Yulbas'), Js('Yunis'), Js('Yusuf'), Js('Zahid'), Js('Zakir'), Js('Zarif'), Js('Zokirjan')]))
    var.put('nm2', Js([Js('Adalat'), Js('Adolat'), Js('Anora'), Js('Aziza'), Js('Bahri'), Js('Bassar'), Js('Binafsha'), Js('Chinara'), Js('Dilbar'), Js('Diloram'), Js('Durdona'), Js('Elnura'), Js('Faroghat'), Js('Faroqhat'), Js('Fatima'), Js('Fayzikhon'), Js('Fazilat'), Js('Feruza'), Js('Gulchehra'), Js('Guldasta'), Js('Guli'), Js('Gulnara'), Js('Gulnora'), Js('Habiba'), Js('Hadicha'), Js('Hahbuba'), Js('Hakima'), Js('Hamra'), Js('Indira'), Js('Inoyat'), Js('Jamila'), Js('Khafiza'), Js('Khasiyat'), Js('Khayrikhon'), Js('Khoslyat'), Js('Kimsan'), Js('Komila'), Js('Latifa'), Js('Lola'), Js("Ma'rifat"), Js('Maghfirat'), Js('Malika'), Js('Malike'), Js('Manzura'), Js('Maqsuda'), Js('Mariyam'), Js('Mastura'), Js('Mehri'), Js("Mu'tabar"), Js('Muhabhat'), Js('Mukarrama'), Js('Munavvara'), Js('Murkhon'), Js('Muzayyana'), Js('Nafis'), Js('Nargiza'), Js('Nasiba'), Js('Nazira'), Js('Nazokat'), Js('Nigara'), Js('Nozanin'), Js('Olma'), Js('Ona'), Js('Onar'), Js('Oqila'), Js('Orifa'), Js('Oumri'), Js('Oundus'), Js('Oydin'), Js('Ozoda'), Js('Parizod'), Js('Parizoda'), Js('Puzvon'), Js('Qumri'), Js('Qumrinico'), Js('Qundus'), Js('Roziya'), Js('Sabira'), Js('Sadoqat'), Js('Salima'), Js('Sallma'), Js('Salomat'), Js('Sanobar'), Js('Shahlo'), Js('Shahnoza'), Js('Shakar'), Js('Shakarkhan'), Js('Shamsigul'), Js('Sharifa'), Js('Soliya'), Js('Tahmina'), Js('Tohta'), Js('Toti'), Js('Turdlya'), Js('Tursan'), Js('Tursunoy'), Js('Ulfat'), Js('Umida'), Js('Vasila'), Js('Yelena'), Js('Yulduz'), Js('Zahida'), Js('Zamira'), Js('Zarifa'), Js('Zarina'), Js('Zebi'), Js('Zulayho'), Js('Zulfiya')]))
    var.put('nm3', Js([Js('Abdulghafurov'), Js('Abdullayev'), Js('Abdulqhafurov'), Js('Abubakirov'), Js('Alimov'), Js('Alisherov'), Js('Aliyev'), Js('Aminjonov'), Js('Arslonov'), Js('Ashurov'), Js('Askarov'), Js('Ataboyev'), Js('Babakhozhayev'), Js('Bakirov'), Js('Batirov'), Js('Baymatov'), Js('Bazarov'), Js('Bekmirzayev'), Js('Berdiyev'), Js('Dadabayev'), Js('Dadajonov'), Js('Davlatov'), Js('Dehoanov'), Js('Elyorov'), Js('Ergashev'), Js('Ermatov'), Js('Erwatov'), Js('Fattayev'), Js('Fayziyev'), Js('Ghaffarov'), Js('Ghafurov'), Js('Ghaniyev'), Js('Ghulamov'), Js('Hakimov'), Js('Hamrayev'), Js('Hasanov'), Js('Haydarov'), Js('Hilolov'), Js('Holiyev'), Js('Husanov'), Js('Ilhamov'), Js('Ishanov'), Js('Jamalov'), Js('Jorayev'), Js('Jumayev'), Js('Jurayev'), Js('Kamalov'), Js('Kamolov'), Js('Karimov'), Js('Khudayberdiyev'), Js('Kimsanov'), Js('Kodirov'), Js('Komilov'), Js('Latifov'), Js('Lutfullayev'), Js('Mahkamov'), Js('Mahmudov'), Js('Malikov'), Js('Mamtqulov'), Js('Mannonov'), Js('Manzurov'), Js('Mirzaliyev'), Js('Muhiddinov'), Js('Munavvarov'), Js('Muradov'), Js('Murtazayev'), Js('Musayev'), Js('Muzafarov'), Js('Nabiyev'), Js('Narzuqulov'), Js('Negmatov'), Js('Nurmatov'), Js('Oalanoarov'), Js('Olichev'), Js('Olimov'), Js('Omarov'), Js('Onarov'), Js('Oodirov'), Js('Ooriyev'), Js('Oqilov'), Js('Otkirov'), Js('Pardayev'), Js('Parpiyev'), Js('Qasimov'), Js('Qodirov'), Js('Rahimov'), Js('Rahmatov'), Js('Ruslanov'), Js('Rustamov'), Js('Sabirov'), Js('Saidjahonov'), Js('Salimov'), Js('Sandjarov'), Js('Sattarov'), Js('Shakirov'), Js('Shavkatov'), Js('Shodmanov'), Js('Shovrukov'), Js('Shukrullayev'), Js('Shukurov'), Js('Soliyev'), Js('Sulaymonov'), Js('Suratov'), Js('Tahirov'), Js('Teshayev'), Js('Timurov'), Js('Tohtayev'), Js('Toshmatov'), Js('Toychiyev'), Js('Turdiyev'), Js('Tursanov'), Js('Tursunov'), Js('Ulfatov'), Js('Umidov'), Js('Usmanov'), Js('Usmonov'), Js('Vahidov'), Js('Valiyev'), Js('Yahyayev'), Js('Yakhshiyev'), Js('Yakubov'), Js('Yarmatov'), Js('Yodgarov'), Js('Yoldashev'), Js('Zakirov'), Js('Zikriyayev'), Js('Zokirjanov')]))
    var.put('nm4', Js([Js('Abdulghafurova'), Js('Abdullayeva'), Js('Abdulqhafurova'), Js('Abubakirova'), Js('Alimova'), Js('Alisherova'), Js('Aliyeva'), Js('Aminjonova'), Js('Arslonova'), Js('Ashurova'), Js('Askarova'), Js('Ataboyeva'), Js('Babakhozhayeva'), Js('Bakirova'), Js('Batirova'), Js('Baymatova'), Js('Bazarova'), Js('Bekmirzayeva'), Js('Berdiyeva'), Js('Dadabayeva'), Js('Dadajonova'), Js('Davlatova'), Js('Dehoanova'), Js('Elyorova'), Js('Ergasheva'), Js('Ermatova'), Js('Erwatova'), Js('Fattayeva'), Js('Fayziyeva'), Js('Ghaffarova'), Js('Ghafurova'), Js('Ghaniyeva'), Js('Ghulamova'), Js('Hakimova'), Js('Hamrayeva'), Js('Hasanova'), Js('Haydarova'), Js('Hilolova'), Js('Holiyeva'), Js('Husanova'), Js('Ilhamova'), Js('Ishanova'), Js('Jamalova'), Js('Jorayeva'), Js('Jumayeva'), Js('Jurayeva'), Js('Kamalova'), Js('Kamolova'), Js('Karimova'), Js('Khudayberdiyeva'), Js('Kimsanova'), Js('Kodirova'), Js('Komilova'), Js('Latifova'), Js('Lutfullayeva'), Js('Mahkamova'), Js('Mahmudova'), Js('Malikova'), Js('Mamtqulova'), Js('Mannonova'), Js('Manzurova'), Js('Mirzaliyeva'), Js('Muhiddinova'), Js('Munavvarova'), Js('Muradova'), Js('Murtazayeva'), Js('Musayeva'), Js('Muzafarova'), Js('Nabiyeva'), Js('Narzuqulova'), Js('Negmatova'), Js('Nurmatova'), Js('Oalanoarova'), Js('Olicheva'), Js('Olimova'), Js('Omarova'), Js('Onarova'), Js('Oodirova'), Js('Ooriyeva'), Js('Oqilova'), Js('Otkirova'), Js('Pardayeva'), Js('Parpiyeva'), Js('Qasimova'), Js('Qodirova'), Js('Rahimova'), Js('Rahmatova'), Js('Ruslanova'), Js('Rustamova'), Js('Sabirova'), Js('Saidjahonova'), Js('Salimova'), Js('Sandjarova'), Js('Sattarova'), Js('Shakirova'), Js('Shavkatova'), Js('Shodmanova'), Js('Shovrukova'), Js('Shukrullayeva'), Js('Shukurova'), Js('Soliyeva'), Js('Sulaymonova'), Js('Suratova'), Js('Tahirova'), Js('Teshayeva'), Js('Timurova'), Js('Tohtayeva'), Js('Toshmatova'), Js('Toychiyeva'), Js('Turdiyeva'), Js('Tursanova'), Js('Tursunova'), Js('Ulfatova'), Js('Umidova'), Js('Usmanova'), Js('Usmonova'), Js('Vahidova'), Js('Valiyeva'), Js('Yahyayeva'), Js('Yakhshiyeva'), Js('Yakubova'), Js('Yarmatova'), Js('Yodgarova'), Js('Yoldasheva'), Js('Zakirova'), Js('Zikriyayeva'), Js('Zokirjanova')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm4').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
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
uzbekNames = var.to_python()
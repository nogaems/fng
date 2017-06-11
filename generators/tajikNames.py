__all__ = ['tajikNames']

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
var.put('nm1', Js([Js('Anoushirvan'), Js('Arash'), Js('Ardavan'), Js('Ardshir'), Js('Armeen'), Js('Aryan'), Js('Arzhang'), Js('Ashkan'), Js('Atash'), Js('Awrang'), Js('Azad'), Js('Azada'), Js('Azarkhsh'), Js('Azerm'), Js('Babak'), Js('Bahman'), Js('Bahram'), Js('Bamdad'), Js('Behnam'), Js('Behrang'), Js('Behruz'), Js('Behzad'), Js('Buzurgmehr'), Js('Dara'), Js('Darab'), Js('Daryush'), Js('Dehqan'), Js('Esfandyar'), Js('Faramarz'), Js('Faraz'), Js('Fardad'), Js('Fardin'), Js('Farhad'), Js('Farhang'), Js('Fariad'), Js('Fariborz'), Js('Farrukh'), Js('Farrukhzad'), Js('Farshad'), Js('Farzad'), Js('Farzam'), Js('Farzann'), Js('Farzin'), Js('Feda'), Js('Firuz'), Js('Forood'), Js('Fraidun'), Js('Fruhar'), Js('Giv'), Js('Goudarz'), Js('Gulab'), Js('Gushtasb'), Js('Hamasa'), Js('Hoshang'), Js('Houshmand'), Js('Housyar'), Js('Human'), Js('Humayon'), Js('Hurmoz'), Js('Iraj'), Js('Jahandar'), Js('Jahangeer'), Js('Jahanshah'), Js('Jawid'), Js('Kaihan'), Js('Kaikhosrow'), Js('Kaiqubad'), Js('Kaiyan'), Js('Kambiz '), Js('Kamran'), Js('Kamshad'), Js('Kamyar'), Js('Kanishka'), Js('Kasra'), Js('Kavah'), Js('Kavoos'), Js('Khashyar'), Js('Khoram'), Js('Khuda Dad'), Js('Kia'), Js('Kianoosh'), Js('Kiumars'), Js('Kohyar'), Js('Kosha'), Js('Koshan'), Js('Kourash'), Js('Mahyar'), Js('Mani'), Js('Manuchehar'), Js('Mazdak'), Js('Mehrab'), Js('Mehrak'), Js('Mehran'), Js('Mehrang'), Js('Mehrdad'), Js('Mehrzad'), Js('Morad'), Js('Namdar'), Js('Namvar'), Js('Naraiman'), Js('Neda'), Js('Niyoosha'), Js('Noushzad'), Js('Omaid'), Js('Padshah'), Js('Paghahan'), Js('Pagzman'), Js('Paikan'), Js('Paiman'), Js('Parsa'), Js('Parwaaze'), Js('Payam'), Js('Pazhman'), Js('Pendar'), Js('Piruz'), Js('Poya'), Js('Qiomars'), Js('Qubad'), Js('Rastin'), Js('Rohina'), Js('Roozbeh'), Js('Roshan'), Js('Royan'), Js('Rozi'), Js('Rukhshan'), Js('Rustam'), Js('Salar'), Js('Sam'), Js('Saman'), Js('Sasan'), Js('Sepehr'), Js('Shadan'), Js('Shahbaz'), Js('Shaheen'), Js('Shahpur'), Js('Shahram'), Js('Shahrdad'), Js('Shahrukh'), Js('Shahryar'), Js('Shaya'), Js('Shayan'), Js('Shuhab'), Js('Siamak'), Js('Siamu'), Js('Siawash'), Js('Sina'), Js('Soroush'), Js('Sougand'), Js('Suhrab'), Js('Tahmaseb'), Js('Toktam'), Js('Tooraj'), Js('Tora'), Js('Toramana'), Js('Varshasb'), Js('Veda'), Js('Vishtasb'), Js('Yama'), Js('Zal'), Js('Zand '), Js('Zardusht'), Js('Khosrow')]))
var.put('nm2', Js([Js('Afareen'), Js('Afsana'), Js('Afsar'), Js('Afshan'), Js('Afsoon'), Js('Anahita'), Js('Anoosheh'), Js('Ara'), Js('Arezo'), Js('Arghavan'), Js('Armaghan'), Js('Asa'), Js('Asal'), Js('Ava'), Js('Avizeh'), Js('Awa'), Js('Azar'), Js('Azin'), Js('Bahar'), Js('Baharah'), Js('Baharak'), Js('Banafshah'), Js('Banou'), Js('Behnaz'), Js('Behrukh'), Js('Belour'), Js('Belourine'), Js('Bizhan'), Js('Boosah'), Js('Darya'), Js('Delaram'), Js('Delbar'), Js('Delkash'), Js('Delruba'), Js('Dorri'), Js('Farahnak'), Js('Farahnaz'), Js('Faranghis'), Js('Farhana'), Js('Farkhonda'), Js('Farrin'), Js('Farrukh'), Js('Farzaneh'), Js('Fila'), Js('Firoza'), Js('Forogh'), Js('Forozan'), Js('Forozenda'), Js('Freba'), Js('Freshta'), Js('Fruzan'), Js('Gawhar'), Js('Geesou'), Js('Ghoncheh'), Js('Giti'), Js('Golbahar'), Js('Gulgun'), Js('Gulnar'), Js('Gulnaz'), Js('Gulnessa'), Js('Gulpari'), Js('Gulshan'), Js('Gurdia'), Js('Hangahma'), Js('Hasti'), Js('Huma'), Js('Jahan Ara'), Js('Javaneh'), Js('Katayoun'), Js('Khandan'), Js('Khaterah'), Js('Khojasta'), Js('Khorsheed'), Js('Lala'), Js('Lila'), Js('Lily'), Js('Mahasti'), Js('Mahdokht'), Js('Mahnaz'), Js('Mahrukh'), Js('Mahsa'), Js('Mahtab'), Js('Mahwash'), Js('Manizha'), Js('Marjan'), Js('Marmar'), Js('Mastana'), Js('Mehrangiz'), Js('Mehrnaz'), Js('Mehrnoosh'), Js('Mehry'), Js('Mina'), Js('Minoo'), Js('Mitra'), Js('Mona'), Js('Murwarid'), Js('Muzghan'), Js('Muzhdah'), Js('Nahal'), Js('Najela'), Js('Nargis'), Js('Nasreen'), Js('Nastaran'), Js('Nava'), Js('Naz'), Js('Naz Gul'), Js('Nazaneen'), Js('Nazhin'), Js('Nazhla'), Js('Nazy'), Js('Neelab'), Js('Neelufar'), Js('Negar'), Js('Negeen'), Js('Negha'), Js('Niki'), Js('Nikoo'), Js('Nousafarin'), Js('Noushin'), Js('Padidah'), Js('Parand'), Js('Parastoo'), Js('Pareeya'), Js('Pari'), Js('Paricheher'), Js('Parirow'), Js('Parisa'), Js('Pariwash'), Js('Parwana'), Js('Parween'), Js('Paymaneh'), Js('Paywand'), Js('Poran Dokht'), Js('Rasa'), Js('Roudabeh'), Js('Rukhsana'), Js('Rukhshan'), Js('Saaman'), Js('Saghar'), Js('Sahar'), Js('Sahba'), Js('Sapedah'), Js('Seema'), Js('Setara'), Js('Shabnam'), Js('Shadan'), Js('Shahla'), Js('Shahnaz'), Js('Shahnoza'), Js('Shahrbano'), Js('Shahrnaz'), Js('Shahrzad'), Js('Shahzadah'), Js('Shameem'), Js('Shararah'), Js('Sheeftah'), Js('Sheela'), Js('Sheeva'), Js('Shervin'), Js('Shirin'), Js('Shirin Bano'), Js('Shogofa'), Js('Shokouh'), Js('Sholah'), Js('Simin'), Js('Soudabah'), Js('Souzan'), Js('Tahminah'), Js('Tanaz'), Js('Taneen'), Js('Tara'), Js('Tarana'), Js('Taranum'), Js('Yagana'), Js('Yakta'), Js('Yalda'), Js('Yasaman'), Js('Zarrin'), Js('Zarrin Dokht'), Js('Zarrina'), Js('Zeba'), Js('Zhalah'), Js('Zheela')]))
pass
pass


# Add lib to the module scope
tajikNames = var.to_python()
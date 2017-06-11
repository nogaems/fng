__all__ = ['trollNames']

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
var.put('nm1', Js([Js('Ditid'), Js('Quivilt'), Js('Mohanlal'), Js('Sollix'), Js('Equinus'), Js('Gamjee'), Js('Matuna'), Js('Kurzol'), Js('Erodjan'), Js('Alwan'), Js('Anje'), Js('Azibo'), Js('Ajin'), Js('Ekon'), Js('Erasto'), Js('Haijen'), Js('Hamedi'), Js('Hokima'), Js('Jaafan'), Js('Jabir'), Js('Jalai'), Js('Javyn'), Js('Jijel'), Js('Juma'), Js('Jumoke'), Js('Kaijin'), Js('Kazko'), Js('Maalik'), Js('Makas'), Js('Malak'), Js('Nyabingi'), Js('Rahjin'), Js('Rakash'), Js('Rashi'), Js('Razi'), Js('Reji'), Js('Rujabu'), Js('Rujin'), Js('Seji'), Js('Senwe'), Js('Seshi'), Js('Teshi'), Js('Tzane'), Js('Tzuljin'), Js('Voyambi'), Js('Vuzashi'), Js('Vuzembi'), Js('Yamike'), Js('Yavo'), Js('Yawan'), Js('Zaejin'), Js('Zallah'), Js('Zebajin'), Js('Zelaji'), Js('Zevrij'), Js('Zinjo'), Js('Zufem'), Js('Alzim'), Js('Ayagi'), Js('Ayargajin'), Js('Dorkuraz'), Js('Hakalai'), Js('Halasuwa'), Js('Hokajin'), Js('Hoodah'), Js('Hyptu'), Js('Jaryaya'), Js('Jayunya'), Js('Jinjin'), Js('Jojin'), Js('Kelraz'), Js('Kuroji'), Js('Lakjin'), Js('Laojin'), Js('Melkree'), Js('Mezilkree'), Js('Napokue'), Js('Nuenvan'), Js('Paikei'), Js('Rapshider'), Js('Rhazin'), Js('Shaktilar'), Js('Shengis'), Js('Sligo'), Js('Tanjin'), Js('Tazingo'), Js('Tedar'), Js('Trezzahn'), Js('Trolgar'), Js('Ttarmek'), Js('Ugoki'), Js('Vekuzz'), Js('Venjo'), Js('Vulzal'), Js('Wanjin'), Js('Wonjin'), Js('Xukundi'), Js('Yetu'), Js('Zengu'), Js('Zoljin'), Js('Zulabar'), Js('Zulbaljin'), Js('Zulgeteb'), Js('Zulkaz'), Js('Zulkis'), Js('Zulrajas'), Js('Zulyafi'), Js('Zunabar')]))
var.put('nm2', Js([Js('Gilta'), Js('Vitchen'), Js('Tirezi'), Js('Fefeya'), Js('Aradya'), Js('Nepita'), Js('Damari'), Js('Meenah'), Js('Kenaya'), Js('Vriska'), Js('Ajia'), Js('Aketa'), Js('Altoa'), Js('Aszea'), Js('Atae'), Js('Azra'), Js('Ecia'), Js('Ejie'), Js('Eleja'), Js('Esha'), Js('Illa'), Js('Kea'), Js('Keja'), Js('Kina'), Js('Kiya'), Js('Kizi'), Js('Moza'), Js('Oyana'), Js('Raca'), Js('Rasha'), Js('Seshia'), Js('Suja'), Js('Suli'), Js('Talisa'), Js('Tasiya'), Js('Tayo'), Js('Teja'), Js('Teza'), Js('Tezzi'), Js('Tizali'), Js('Xia'), Js('Yaci'), Js('Yajdna'), Js('Yashi'), Js('Yera'), Js('Yeree'), Js('Yesha'), Js('Yishi'), Js('Zara'), Js('Zashi'), Js('Zea'), Js('Zelea'), Js('Zesa'), Js('Zeti'), Js('Zola'), Js('Zoti'), Js('Zujia'), Js('Zyra'), Js('Alunja'), Js('Anji'), Js('Arany'), Js('Bajin'), Js('Baliaja'), Js('Benni'), Js('Bie'), Js('Boonoo'), Js('Bunjin'), Js('Csini'), Js('Feylin'), Js('Girisha'), Js('Hailith'), Js('Ithra'), Js('Javilla'), Js('Javinda'), Js('Jezemalu'), Js('Jinthaiya'), Js('Jiranty'), Js('Jozala'), Js('Jubukraa'), Js('Juljin'), Js('Kanjin'), Js('Katanja'), Js('Katzine'), Js('Khelynn'), Js('Khijazi'), Js('Khuwei'), Js('Kululu'), Js('Lujin'), Js('Makali'), Js('Mandula'), Js('Meimei'), Js('Melelea'), Js('Nelina'), Js('Prerrahar'), Js('Pujati'), Js('Rangi'), Js('Renjai'), Js('Renji'), Js('Ronjaty'), Js('Saedmara'), Js('Saonji'), Js('Segawa'), Js('Senzala'), Js('Shadrala'), Js('Shakawatha'), Js('Shaktila'), Js('Shamra'), Js('Sharimara'), Js('Shubre'), Js('Soniya'), Js('Sonja'), Js('Suliya'), Js('Sulynn'), Js('Titamor'), Js('Tsaijo'), Js('Usitutie'), Js('Valja'), Js('Vanjin'), Js('Venmara'), Js('Vinji'), Js('Vinjin'), Js('Vonjai'), Js('Vujii'), Js('Vulzala'), Js('Watu'), Js('Yuhai'), Js('Zalma'), Js('Zalmea'), Js('Zenma'), Js('Zhonya'), Js('Zhoumai'), Js('Ziataaman'), Js('Ziataima'), Js('Ziataja'), Js('Ziatajie'), Js('Ziatakraa'), Js('Zonraja'), Js('Zulja'), Js('Zulja'), Js('Zuljah'), Js('Zuljin'), Js('Zulkraa'), Js('Zulmara'), Js('Zulraja'), Js('Zulrea'), Js('Zulwatha')]))
pass
pass


# Add lib to the module scope
trollNames = var.to_python()
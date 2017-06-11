__all__ = ['akkadianNames']

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
    var.put('nm1', Js([Js('Appan-Il'), Js('Apuulluunideeszu'), Js('Ariistuun'), Js('Arishaka'), Js('Ataneedusu'), Js("Anti'iikusu"), Js('Aplaa'), Js("Ar'siuqqa"), Js('Arshaka'), Js("Attii'kusu"), Js('Baassiia'), Js('Balashi'), Js('Balathu'), Js('Bashaa'), Js('Burnaburiash'), Js('Dadanum'), Js("Dee'qiteesu"), Js('Deemeethresu'), Js('Deemethereesu'), Js('Deemethresi'), Js('Deemethresu'), Js('Deemuukratee'), Js('Demeetheresu'), Js('Demetheriia'), Js("Dii'duuresu"), Js('Diimeritia'), Js("Diipaa'ni"), Js('Diipanii'), Js('Diipatusu'), Js('Dipatusu'), Js('Dudu'), Js('Ea-nasir'), Js('Ekurzakir'), Js('Enshunu'), Js('Enusat'), Js('Gina'), Js('Hillalum'), Js('Hunzuu'), Js('Iaazipaa'), Js('Ibbi-Adad'), Js('Ikuppi-Adad'), Js('Ipqu-Annunitum'), Js('Ipqu-Aya'), Js('Ishme-Ea'), Js('Isiratuu'), Js('Issaruutunu'), Js('Kadashman-Enlil'), Js("Kiipluu'"), Js("Kiipluuu'"), Js('Kinaa'), Js('Kuri'), Js('Kurigalzu'), Js('Labashi'), Js('Laliya'), Js('Laqip'), Js('Ligish'), Js('Libluth'), Js('Manishtusu'), Js('Manishtushu'), Js('Manuiqapu'), Js('Mannuiqapi'), Js('Mannuiqapu'), Js('Naram-Sin'), Js('Nidintu-Bel'), Js('Nidintulugal'), Js('Niiqiarqusu'), Js('Niiqarquusu '), Js('Niiqquulamuusu'), Js('Nikanuur'), Js('Nikiiarqusu'), Js('Nigsummu'), Js('Nigsummulugal'), Js('Nigsummunu'), Js('Nutesh'), Js('Numunia'), Js('Nur-Ayya'), Js('Puzur-Ishtar'), Js('Rabi-Sillashu'), Js('Rihat'), Js('Rimush'), Js('Ripaa'), Js('Samsuiluna'), Js('Sargon'), Js('Seluku'), Js('Shamash-Andulli'), Js('Shamash-Nasir'), Js('Shar-kali-sharri'), Js('Shu-Turul'), Js('Sin-Nasir'), Js('Suusaandar'), Js('Tattannu'), Js('Timgiratee'), Js('Ubar'), Js('Ugurnaszir'), Js('Uktannu'), Js('Uppulu'), Js('Utuaa'), Js('Yahatti-Il'), Js('Zuuthusu')]))
    var.put('nm2', Js([Js('Adeeshuduggaat'), Js('Ahassunu'), Js('Ahati-waqrat'), Js('Ahatsunu'), Js('Alittum'), Js('Amata'), Js('Anagalmeshshu'), Js('Anagalshu'), Js('Arahunaa'), Js('Arwia'), Js('Ashlultum'), Js('Banunu'), Js('Belessunu'), Js('Beletsunu'), Js('Enheduana'), Js('Erishti-Aya'), Js('Ettu'), Js('Gashansunu'), Js('Gemegishkirihallat'), Js('Gemekaa'), Js('Gemeti'), Js('Humusi'), Js('Ia'), Js('Iltani'), Js('Ishtar-gamelat'), Js('Ku-Aya'), Js('Ku-Baba'), Js('Kullaa'), Js('Munawwirtum'), Js('Mushezibitu'), Js('Mushezibti'), Js('Nidintu'), Js('Ninsunu'), Js('Tabni-Ishtar'), Js('Ubalnu'), Js('Yadidatum'), Js('Zakiti')]))
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
akkadianNames = var.to_python()
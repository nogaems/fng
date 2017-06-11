__all__ = ['phoenicianNames']

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
    var.put('nm1', Js([Js('Abdastartus'), Js('Abdeshmun'), Js('Abdmelqart'), Js('Abdosir'), Js('Abibaal'), Js('Adad'), Js('Addir'), Js('Addonia'), Js('Aderbaal'), Js('Adohnes'), Js('Adon'), Js('Adones'), Js('Adonia'), Js('Adoniah'), Js('Adonias'), Js('Adonibaal'), Js('Adonis'), Js('Adonys'), Js('Ahinadab'), Js('Ahiram'), Js('Ahirom'), Js('Akbar'), Js('Amilcare'), Js('Anibal'), Js('Annaba'), Js('Annibale'), Js('Aqhat'), Js('Aradus'), Js('Arvad'), Js('Ashtartyaton'), Js('Ashtzaph'), Js('Astartus'), Js('Azmelqart'), Js('Baalhanno'), Js('Baalshillek'), Js('Baldassare'), Js('Baldo'), Js('Baltasar'), Js('Baltazar'), Js('Balthasar'), Js('Balthazar'), Js('Balthezar'), Js('Baltsar'), Js('Baltser'), Js('Balzer'), Js('Barekbaal'), Js('Batrun'), Js('Bedezorus'), Js('Beirut'), Js('Belshazzar'), Js('Berut'), Js('Bodashtart'), Js('Bodeshmun'), Js('Bodinelqart'), Js('Bodmelqart'), Js('BoldizsÃ¡r'), Js('Botrys'), Js('Byblos'), Js('Carthage'), Js('Danel'), Js('Donis'), Js('Eshmun'), Js('Eshmunamash'), Js('Eshmunazar'), Js('Gebal'), Js('Germelqart'), Js('Hailama'), Js('Hamilcar'), Js('Hammon'), Js('Hanibal'), Js('Hannibal'), Js('Hanno'), Js('Hasdrubal'), Js('Himilco'), Js('Hiram'), Js('Hyrum'), Js('Itthobaal'), Js('Jebel'), Js('Kanmi'), Js('Khilletzbaal'), Js('Maharbaal'), Js('Melqartpilles'), Js('Milkherem'), Js('Milkpilles'), Js('Milkyaton'), Js('Paltibaal'), Js('Philosir'), Js('Qarnaim'), Js('Resheph'), Js('Sakarbaal'), Js('Shamayim'), Js('Shemen'), Js('Sidon'), Js('Sikarbaal'), Js('Tabnit'), Js('Tammuz'), Js('Tyre'), Js('Ugarit'), Js('Utica'), Js('Yarikh'), Js('Yehawwielon'), Js('Yutpan'), Js('Zephon'), Js('Zidon'), Js('Zimrida')]))
    var.put('nm2', Js([Js('Adoncia'), Js('Adonia'), Js('Adoniah'), Js('Adonica'), Js('Adonna'), Js('Adonya'), Js('Adonyah'), Js('Alissa'), Js('Amatashtart'), Js('Amatbal'), Js('Amma'), Js('Amotmilqart'), Js('Anath'), Js('Arashtibal'), Js('Arisha'), Js('Arishat'), Js('Arishot'), Js('Arshut'), Js('Ashdanot'), Js('Ashdonbal'), Js('Asherah'), Js('Ashmonrabti'), Js('Ashtoreth'), Js('Astarte'), Js('Athirat'), Js('Azibal'), Js('Baalat'), Js('Barkitbal'), Js('Batnoam'), Js('Birkana'), Js('Birkanda'), Js('Bisha'), Js('Bitnima'), Js('Coriander'), Js('Coriender'), Js('Coryander'), Js('Coryender'), Js('Demna'), Js('Dido'), Js('Domina'), Js('Elissa'), Js('Emeshmoon'), Js('Imashmon'), Js('Imashtart'), Js('Izabel'), Js('Izavel'), Js('Jesibel'), Js('Jessabel'), Js('Jessebel'), Js('Jetzabel'), Js('Jez'), Js('Jezabel'), Js('Jezabella'), Js('Jezebel'), Js('Jezebela'), Js('Jezebele'), Js('Jezebelle'), Js('Jezibel'), Js('Melita'), Js('Mitunbaal'), Js('Muttunbaal'), Js('Nikkal'), Js('Pawly'), Js('Quarta'), Js('Septy'), Js('Shapash'), Js('Shiba'), Js('Sisa'), Js('Tanis'), Js('Tanit'), Js('Tanith'), Js('Tanitha'), Js('Tanithe'), Js('Tanni'), Js('Tanyih'), Js('Tanyth'), Js('Tanythe'), Js('Ummashtart'), Js('Yasha'), Js('Zibqet')]))
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
phoenicianNames = var.to_python()
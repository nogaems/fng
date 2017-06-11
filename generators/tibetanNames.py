__all__ = ['tibetanNames']

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
    var.put('nm1', Js([Js('Bhakto'), Js('Bhuchung'), Js('Bhuti'), Js('Chodag'), Js('Chodak'), Js('Choden'), Js('Chodrak'), Js('Choedon'), Js('Choegyal'), Js('Choejor'), Js('Choenyi'), Js('Choephel'), Js('Choezom'), Js('Chokey'), Js('Chokphel'), Js('Chokzay'), Js('Chonden'), Js('Chophel'), Js('Dakpa'), Js('Damchoe'), Js('Dawa'), Js('Dema'), Js('Dhadul'), Js('Dhakpa'), Js('Dhardon'), Js('Dhargay '), Js('Dhargey'), Js('Dhargye'), Js('Dharma'), Js('Dhundup'), Js('Dickey'), Js('Dolkar'), Js('Dolker'), Js('Dolma'), Js('Dorje'), Js('Dorjee'), Js('Duga'), Js('Gelek'), Js('Gephel'), Js('Gonpo'), Js('Gurmey'), Js('Gyalchok'), Js('Gyaltsen'), Js('Gyamtso'), Js('Gyatso'), Js('Gyurmey'), Js('Jamma'), Js('Jampa'), Js('Jamtso'), Js('Jamyang'), Js('Jangchup'), Js('Jinpa'), Js('Jorden'), Js('Jungney'), Js('Kalsang'), Js('Karma'), Js('Kechok'), Js('Kelden'), Js('Kelsang'), Js('Kesang'), Js('Khando'), Js('Khandro'), Js('Khedrup'), Js('Khetsun'), Js('Konchok'), Js('Kunchen'), Js('Kundang'), Js('Kunga'), Js('Legshey'), Js('Lhakpa'), Js('Lhamo'), Js('Lhawang'), Js('Lhundrup'), Js('Lhundup'), Js('Lobsang'), Js('Metok'), Js('Monlam'), Js('Namdak'), Js('Namdol'), Js('Namgyal'), Js('Namgyal Wangchuk'), Js('Ngawang'), Js('Ngodup'), Js('Ngonga'), Js('Norbu'), Js('Norzin'), Js('Nyandak'), Js('Nyima'), Js('Padma'), Js('Palden'), Js('Paldon'), Js('Paljor'), Js('Palkyi'), Js('Palmo'), Js('Passang'), Js('Pema'), Js('Pemba'), Js('Penpa'), Js('Phuntsok'), Js('Rabgyal'), Js('Rabten'), Js('Rabyang'), Js('Rangdol'), Js('Rapten'), Js('Richen'), Js('Rigsang'), Js('Rigzin'), Js('Rinchen'), Js('Samdup'), Js('Samten'), Js('Sangey'), Js('Sangmo'), Js('Sangyal'), Js('Sangye'), Js('Seldon'), Js('Shenlha Woekar'), Js('Sherab'), Js('Sherap'), Js('Sonam'), Js('Tamdin'), Js('Tashi'), Js('Tempa'), Js('Tenzin'), Js('Thekchen'), Js('Thokmay'), Js('Thubten'), Js('Tinley'), Js('Topden'), Js('Tsamchoe'), Js('Tselha'), Js('Tsering'), Js('Tseten'), Js('Tsewang'), Js('Tsomo'), Js('Tsultrim'), Js('Tsundue'), Js('Ugyen'), Js('Wangchen'), Js('Wangchuk'), Js('Wangdak'), Js('Wangdue'), Js('Wangdup'), Js('Wangmo'), Js('Wangyal'), Js('Woenang'), Js('Woeser'), Js('Woeten'), Js('Yama'), Js('Yangdon'), Js('Yangkey'), Js('Yangtso'), Js('Yangzom'), Js('Yeshi'), Js('Yonten'), Js('Youdon'), Js('Youdron'), Js('Yudron'), Js('Yungdrung'), Js('Zopa')]))
    var.put('nm2', Js([Js('Aukatsang'), Js('Bhutia'), Js('Bongpatsang'), Js('Chodron'), Js('Damdul'), Js('Dhanacktsang'), Js('Dhompa'), Js('Dorje'), Js('Drakpa'), Js('Drakthonpa'), Js('Dramuktsang'), Js('Drupa'), Js('Geymutsang'), Js('Gonpo'), Js('Gorkha'), Js('Gurung'), Js('Gyaktsen'), Js('Gyatso'), Js('Jigme'), Js('Jungne'), Js('Kalingpong'), Js('Karpo'), Js('Kyidtodpa'), Js('Ladakh'), Js('Lhamo'), Js('Lingpa'), Js('Lotsawa'), Js('Lukhangwa'), Js('Manriwa'), Js('Mingyur'), Js('Mipham'), Js('Monpa'), Js('Namdak'), Js('Nepali'), Js('Norbu'), Js('Nyima'), Js('Nyingpo'), Js('Pakshi'), Js('Palsang'), Js('Pandita'), Js('Repa'), Js('Sambhota'), Js('Sangpo'), Js('Shakabpa'), Js('Sherpa'), Js('Tamang'), Js('Tangpa'), Js('Tenzin'), Js('Thaye'), Js('Trengwa'), Js('Trungpa'), Js('Tsemo'), Js('Tsogyal'), Js('Wangpo'), Js('Yeshy')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('names', var.get('nm1').get(var.get('rnd')))
            else:
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
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
tibetanNames = var.to_python()
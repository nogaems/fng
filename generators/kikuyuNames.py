__all__ = ['kikuyuNames']

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
    var.put('nm1', Js([Js('Chege'), Js('Chomba'), Js('Ciugũ'), Js('Gĩchũki'), Js('Gĩchũrũ'), Js('Gĩcheha'), Js('Gĩchere'), Js('Gĩchikũ'), Js('Gĩchohi'), Js('Gĩchuhĩ'), Js('Gĩkonyo'), Js('Gĩtũma'), Js('Gĩtũra'), Js('Gĩtaũ'), Js('Gĩtahi'), Js('Gĩtari'), Js('Gĩthĩnji'), Js('Gĩthaiga'), Js('Gĩthire'), Js('Gĩtonga'), Js('Gĩtukũ'), Js('Gachũhĩ'), Js('Gachagua'), Js('Gachanja'), Js('Gachara'), Js('Gachii'), Js('Gakure'), Js('Gathaiya'), Js('Gathanja'), Js('Gathenya'), Js('Gathigira'), Js('Gathogo'), Js('Gathongo'), Js('Gathu'), Js('Gathua'), Js('Gathuuri'), Js('Gatimũ'), Js('Githendũ'), Js('Goko'), Js('Hinga'), Js('Irũngũ'), Js('Ireri'), Js('Kĩbachia'), Js('Kĩbakĩ'), Js('Kĩbunja'), Js('Kĩhĩa'), Js('Kĩhara'), Js('Kĩhiũ'), Js('Kĩhoro'), Js('Kĩhuna'), Js('Kĩmani'), Js('Kĩmotho'), Js('Kĩmunya'), Js('Kĩng’Ori'), Js('Kĩnuthia'), Js('Kĩnyanjui'), Js('Kĩnyua'), Js('Kĩoi'), Js('Kĩongo'), Js('Kĩrĩka'), Js('Kĩrĩma'), Js('Kĩragũ'), Js('Kũngũ'), Js('Kabirũ'), Js('Kabutha'), Js('Kago'), Js('Kagoci'), Js('Kagwa'), Js('Kahũthia'), Js('Kahara'), Js('Kahiĩ'), Js('Kairu'), Js('Kamande'), Js('Kamangĩ'), Js('Kamau'), Js('Kamotho'), Js('Kaniũ'), Js('Kanja'), Js('Karĩmi'), Js('Karũgũ'), Js('Karanja'), Js('Kariũki'), Js('Karungu'), Js('Kenyatta'), Js('Kibe'), Js('Kimane'), Js('Kimaru'), Js('Kimathi'), Js('Kinũthia'), Js('Kogĩ'), Js('Koinange'), Js('Kuria'), Js('Mĩchuki'), Js('Mũchene'), Js('Mũchoki'), Js('Mũciri'), Js('Mũgane'), Js('Mũgo'), Js('Mũhĩa'), Js('Mũhũri'), Js('Mũhoho'), Js('Mũhoro'), Js('Mũirũrĩ'), Js('Mũite'), Js('Mũkundi'), Js('Mũnene'), Js('Mũngai'), Js('Mũngania'), Js('Mũrĩgĩ'), Js('Mũrĩithi'), Js('Mũrĩmi'), Js('Mũrĩranja'), Js('Mũrĩu'), Js('Mũrũngarũ'), Js('Mũragũri'), Js('Mũrakaru'), Js('Mũraya'), Js('Mũrira'), Js('Mũtũng’Ũ'), Js('Mũtegi'), Js('Mũthĩnji'), Js('Mũthũi'), Js('Mũthũngũ'), Js('Mũtiga'), Js('Mũtugi'), Js('Mũya'), Js('Macharia'), Js('Mahĩhu'), Js('Maina'), Js('Maitho'), Js('Mathani'), Js('Mathenge'), Js('Matu'), Js('Mbĩra'), Js('Mbũgua'), Js('Mbũrũ'), Js('Mogo'), Js('Muriũki'), Js('Murigo'), Js('Mwagĩru'), Js('Mwai'), Js('Mwanĩki'), Js('Mwangi'), Js('Mwathi'), Js("Ndũn'Gũ"), Js('Ndegwa'), Js('Nderitũ'), Js('Ndiangui'), Js('Ndirangũ'), Js('Ngũgĩ'), Js('Ngũnjiri'), Js("Ng'Ang'A"), Js('Ngarĩ'), Js('Ngechũ'), Js('Ngengi'), Js('Ngichũ'), Js('Ngigĩ'), Js('Ngina'), Js('Nginyo'), Js('Ngure'), Js('Njũki'), Js('Njaũ'), Js('Njagĩ'), Js('Njaramba'), Js('Njau'), Js('Njenga'), Js('Njerũ'), Js('Njogu'), Js('Njoka'), Js('Njomo'), Js('Njonjo'), Js('Njoroge'), Js('Njuguna'), Js('Nyamu'), Js('Nyoike'), Js('Nyoro'), Js('Thairu'), Js('Theuri'), Js('Thuũ'), Js('Thuku'), Js('Wachira,'), Js('Wachiru'), Js('Wachiuri'), Js('Wachiuru'), Js('Wahome'), Js('Waigwa'), Js('Wainaina'), Js('Waita'), Js('Waititũ'), Js('Wakaritũ'), Js('Wamũgũnda'), Js('Wamahiũ'), Js('Wambũgũ'), Js('Wamiti'), Js('Wanderi'), Js('Wang’Ombe'), Js('Wang’Ondu'), Js("Wang'Ombe"), Js('Wanjohi'), Js('Wanyoike'), Js('Warũĩ'), Js('Warũirũ'), Js('Warari'), Js('Watene'), Js('Wawerũ')]))
    var.put('nm2', Js([Js('Gakuhĩ'), Js('Gathoni'), Js('Jata'), Js('Kanyi'), Js('Kioni'), Js('Mũkami'), Js('Mũkina'), Js('Mũmbi'), Js('Mũrĩnga'), Js('Mũringo'), Js('Mũrugi'), Js('Mũthoni'), Js('Magiri'), Js('Makena'), Js('Moombi'), Js('Mukami'), Js('Mukondi'), Js('Mumbi'), Js('Murigo'), Js('Murugi'), Js('Muthoni'), Js('Mwara'), Js('Mwihaki'), Js('Nũngari'), Js('Nduta'), Js('Ngĩna'), Js('Ng’Endo'), Js('Ngendo'), Js('Ngina'), Js('Njambi'), Js('Njeri'), Js('Njoki'), Js('Noni'), Js('Nyagũra'), Js('Nyagũthiĩ'), Js('Nyaguthii'), Js('Nyakio'), Js('Nyambugi'), Js('Nyambura'), Js('Nyawĩra'), Js('Nyawira'), Js('Nyokabi'), Js('Wacũ'), Js('Waceera'), Js('Waceke'), Js('Wacuka'), Js('Wagichugu'), Js('Wahu'), Js('Waihumbu'), Js('Wairimũ'), Js('Wairimu'), Js('Wairmu'), Js('Waithĩra'), Js('Waitherero'), Js('Waithira'), Js('Wakiuru'), Js('Wamũyũ'), Js('Wamaitha'), Js('Wambũi'), Js('Wambeere'), Js('Wambugua'), Js('Wambui'), Js('Wameru'), Js('Wamuhu'), Js('Wamuiru'), Js('Wamweru'), Js('Wandia'), Js('Wangũ'), Js('Wangũi'), Js('Wangai'), Js('Wangarĩ'), Js('Wangari'), Js('Wangeci'), Js('Wangera'), Js('Wangu'), Js('Wanjĩra'), Js('Wanja'), Js('Wanjeri'), Js('Wanjikũ'), Js('Wanjiku'), Js('Wanjirũ'), Js('Wanjira'), Js('Wanjiru'), Js('Wanyiri'), Js('Wanyora'), Js('Warĩnga'), Js('Warũgũrũ'), Js('Warigia'), Js('Wathira'), Js('Wawĩra'), Js('Wokabi')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm1').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm1').callprop('splice', var.get('rnd2'), Js(1.0))
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
kikuyuNames = var.to_python()
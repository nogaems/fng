__all__ = ['igboNames']

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
    var.put('nm1', Js([Js('Afamefula'), Js('Afamefuna'), Js('Agu'), Js('Akabueze'), Js('Akachi'), Js('Akubundu'), Js('Akuchi'), Js('Akumjeli'), Js('Amadi'), Js('Amazu'), Js('Azubuike'), Js('Belonwu'), Js('Beluchi'), Js('Buchi'), Js('Chee'), Js('Chi'), Js('Chibueze'), Js('Chibuike'), Js('Chibuzo'), Js('Chidea'), Js('Chidee'), Js('Chidey'), Js('Chidi'), Js('Chidie'), Js('Chidiebere'), Js('Chidiebube'), Js('Chidiegwu'), Js('Chidike'), Js('Chidubem'), Js('Chidy'), Js('Chiemeka'), Js('Chijindum'), Js('Chijioke'), Js('Chika'), Js('Chike'), Js('Chikelu'), Js('Chikere'), Js('Chima'), Js('Chimaijem'), Js('Chinasa'), Js('Chinaza'), Js('Chinedu'), Js('Chinelo'), Js('Chinese'), Js('Chineze'), Js('Chino'), Js('Chinou'), Js('Chinua'), Js('Chinuah'), Js('Chinwe'), Js('Chinweike'), Js('Chinwendu'), Js('Chinweuba'), Js('Chioke'), Js('Chioma'), Js('Chizoba'), Js('Chononso'), Js('Chuks'), Js('Chukwubuikem'), Js('Chukwudi'), Js('Chukwuemeka'), Js('Chukwuma'), Js('Chydea'), Js('Chydee'), Js('Chydey'), Js('Chydi'), Js('Chydie'), Js('Chydy'), Js('Chyke'), Js('Diji'), Js('Dike'), Js('Ebele'), Js('Ekene'), Js('Ekenedilichukwu'), Js('Ekwueme'), Js('Emeka'), Js('Enyinnaya'), Js('Fumnanya'), Js('Halim'), Js('Halimnye'), Js('Ibeabuchi'), Js('Ibezimako'), Js('Ifeanyichukwu'), Js('Ifeatu'), Js('Ijeawele'), Js('Ijendu'), Js('Ikem'), Js('Ikenna'), Js('Iweobiegbulam'), Js('Izuchukwu'), Js('Jaja'), Js('Jajah'), Js('Jamuike'), Js('Jel'), Js('Jelan'), Js('Jelanea'), Js('Jelanee'), Js('Jelaney'), Js('Jelani'), Js('Jelanie'), Js('Jelany'), Js('Jideofor'), Js('Jioke'), Js('Koofrey'), Js('Madou'), Js('Madu'), Js('Maduabuchim'), Js('Madue'), Js('Madukaife'), Js('Madukwe'), Js('Mazi'), Js('Mazzi'), Js('Munachiso'), Js('Ndidi'), Js('Ndulu'), Js('Ngozi'), Js('Nkechi'), Js('Nkemdilim'), Js('Nnamdi'), Js('Nwabudike'), Js('Nwankwo'), Js('Nweke'), Js('Nwoye'), Js('Obasea'), Js('Obasee'), Js('Obasey'), Js('Obasi'), Js('Obasie'), Js('Obasy'), Js('Obea'), Js('Obee'), Js('Obey'), Js('Obi'), Js('Obie'), Js('Obike'), Js('Oby'), Js('Obyke'), Js('Odion'), Js('Ogbonna'), Js('Ogbonnia'), Js('Okafo'), Js('Okechukwu'), Js('Okeke'), Js('Okeli'), Js('Okonkwo'), Js('Okorie'), Js('Okpara'), Js('Okparo'), Js('Okparra'), Js('Okparro'), Js('Oluchi'), Js('Onuchukwu'), Js('Onyekachi'), Js('Onyekachukwu'), Js('Orjea'), Js('Orjee'), Js('Orjey'), Js('Orji'), Js('Orjie'), Js('Orjy'), Js('Ozioma'), Js('Ozoemena'), Js('Somayina'), Js('Tobechukwu'), Js('Uche'), Js('Uchea'), Js('Uchechea'), Js('Uchechee'), Js('Uchechey'), Js('Uchechi'), Js('Uchechie'), Js('Uchechy'), Js('Uchee'), Js('Uchey'), Js('Uchi'), Js('Uchie'), Js('Uchy'), Js('Udegbulam'), Js('Udegbunam'), Js('Udo'), Js('Ugochukwu'), Js('Ugonna'), Js('Ugoorji'), Js('Uwaezuoke'), Js('Uzochi'), Js('Uzochukwu'), Js('Uzoma'), Js('Yobachukwu'), Js('Yobanna'), Js('Zebenjo'), Js('Zikoranaudodimma')]))
    var.put('nm2', Js([Js('Adaeze'), Js('Adaezennaya'), Js('Adamma'), Js('Adanma'), Js('Adanna'), Js('Adannaya'), Js('Adaobi'), Js('Adaoma'), Js('Adaora'), Js('Akachi'), Js('Akuchi'), Js('Akumjeli'), Js('Amachea'), Js('Amacheah'), Js('Amachee'), Js('Amachey'), Js('Amachi'), Js('Amachie'), Js('Amachy'), Js('Amachye'), Js('Amaka'), Js('Amaogechukwu'), Js('Amara'), Js('Amarachi'), Js('Amarachukwu'), Js('Anuli'), Js('Anulika'), Js('Chi'), Js('Chiamaka'), Js('Chibueze'), Js('Chibuifem'), Js('Chibuike'), Js('Chibuzo'), Js('Chichi'), Js('Chidea'), Js('Chideah'), Js('Chidee'), Js('Chidey'), Js('Chidi'), Js('Chidie'), Js('Chidiebere'), Js('Chidiebube'), Js('Chidiegwu'), Js('Chidimma'), Js('Chidinma'), Js('Chidy'), Js('Chijindum'), Js('Chika'), Js('Chikanso'), Js('Chike'), Js('Chikelu'), Js('Chikere'), Js('Chimaijem'), Js('Chinagorom'), Js('Chinaka'), Js('Chinasa'), Js('Chinaza'), Js('Chinecherem'), Js('Chinedu'), Js('Chineze'), Js('Chinonso'), Js('Chinwe'), Js('Chinweike'), Js('Chinwendu'), Js('Chinweuba'), Js('Chinyelu'), Js('Chinyere'), Js('Chioma'), Js('Chizoba'), Js('Chukwudi'), Js('Chukwuebuka'), Js('Daluchi'), Js('Daluchineke'), Js('Ebele'), Js('Ebuka'), Js('Echerem'), Js('Ekene'), Js('Ekenedilichukwu'), Js('Eshe'), Js('Fumnanya'), Js('Funanya'), Js('Gorom'), Js('Halim'), Js('Halimnye'), Js('Ifama'), Js('Ifamah'), Js('Ifamma'), Js('Ifammah'), Js('Ifenyinwa'), Js('Ifeoma'), Js('Ifunanya'), Js('Ijendu'), Js('Iruka'), Js('Iweobiegbulam'), Js('Kambiri'), Js('Maduabuchim'), Js('Madukaego'), Js('Mgbankwo'), Js('Mgbeke'), Js('Mgborie'), Js('Munachiso'), Js('Ndidi'), Js('Ngozi'), Js('Nkechi'), Js('Nkechinyere'), Js('Nkemdilim'), Js('Nkiru'), Js('Nkiruka'), Js('Nneka'), Js('Nnenna'), Js('Nnenne'), Js('Nwanneka'), Js('Odera'), Js('Ogechi'), Js('Ogechukwukama'), Js('Olisa'), Js('Oluchi'), Js('Onochie'), Js('Onuchukwu'), Js('Onyeka'), Js('Onyekachi'), Js('Onyekachukwu'), Js('Otuosoro'), Js('Ozioma'), Js('Uchena'), Js('Uchenah'), Js('Uchenna'), Js('Uchennah'), Js('Udo'), Js('Ula'), Js('Urenna'), Js('Urunwa'), Js('Uzoamaka'), Js('Uzochi'), Js('Uzochukwu'), Js('Uzoma'), Js('Yobachukwu'), Js('Yobanna'), Js('Zikoranaudodimma')]))
    var.put('nm3', Js([Js('Akachi'), Js('Akuchi'), Js('Akumjeli'), Js('Chi'), Js('Chibueze'), Js('Chibuike'), Js('Chibuzo'), Js('Chidi'), Js('Chidiebere'), Js('Chidiebube'), Js('Chidiegwu'), Js('Chijindum'), Js('Chika'), Js('Chike'), Js('Chikelu'), Js('Chikere'), Js('Chinasa'), Js('Chinaza'), Js('Chinedu'), Js('Chinwe'), Js('Chinweike'), Js('Chinwendu'), Js('Chinweuba'), Js('Chioma'), Js('Chizoba'), Js('Chononso'), Js('Ebele'), Js('Ekene'), Js('Ekenedilichukwu'), Js('Fumnanya'), Js('Halim'), Js('Halimnye'), Js('Ijendu'), Js('Iweobiegbulam'), Js('Maduabuchim'), Js('Munachiso'), Js('Ndidi'), Js('Ngozi'), Js('Nkechi'), Js('Nkemdilim'), Js('Oluchi'), Js('Onuchukwu'), Js('Onyekachi'), Js('Onyekachukwu'), Js('Ozioma'), Js('Udo'), Js('Uzochi'), Js('Uzochukwu'), Js('Uzoma'), Js('Yobachukwu'), Js('Yobanna'), Js('Zikoranaudodimma')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm1').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm1').get(var.get('rnd2'))))
                    var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
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
igboNames = var.to_python()
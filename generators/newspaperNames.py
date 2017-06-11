__all__ = ['newspaperNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Apex'), Js('Aurora'), Js('Avant-Garde'), Js('Banner'), Js('Beacon'), Js('Break of Day'), Js('Breakfast'), Js('Bulletin'), Js('Business'), Js('Capital'), Js('Capitol'), Js('Carpe Diem'), Js('Citizen'), Js('Community'), Js('Courier'), Js('Crack of Dawn'), Js('Daily'), Js('Daily Watch'), Js('Dawn'), Js('Dawning'), Js('Day Break'), Js('Daybreak'), Js('Daylight'), Js('Dayspring'), Js('Diem'), Js('Dispatch'), Js('Early'), Js('Early Bird'), Js('Eastern'), Js('Echo'), Js('Emerald'), Js('Emporium'), Js('Enterprise'), Js('Epoch'), Js('Era'), Js('Estate'), Js('Evening'), Js('Everyday'), Js('Explorer'), Js('Express'), Js('Eyewitness'), Js('First Light'), Js('Foreday'), Js('Foundation'), Js('Global'), Js('Headline'), Js('Heritage'), Js('Independent'), Js('Inside'), Js('Insider'), Js('Key'), Js('Leading'), Js('Legacy'), Js('Liberty'), Js('Life'), Js('Local'), Js('Local Voice'), Js('Lodestar'), Js('Metropolitan'), Js('Modest'), Js('Monday'), Js('Morn'), Js('Morning'), Js('Morning Star'), Js('Morning Watch'), Js('Morningtide'), Js('Morrow'), Js('National'), Js('New'), Js('Northern'), Js('Nova'), Js('Observer'), Js('Paragon'), Js('Patriot'), Js('Patron'), Js('Pinnacle'), Js('Pioneer'), Js('Plain'), Js('Prime'), Js('Public'), Js('Record'), Js('Relay'), Js('Saturday'), Js('Society'), Js('Southern'), Js('Standard'), Js('Star'), Js('State'), Js('Sun'), Js('Sunday'), Js('Sunrise'), Js('Sunup'), Js('Telegraph'), Js("Today's"), Js('Tribune'), Js('Vertex'), Js('Vista'), Js('Weekly'), Js('Western'), Js('Witness'), Js('World'), Js('Zenith')]))
    var.put('nm2', Js([Js('Account'), Js('Alliance'), Js('Apex'), Js('Aurora'), Js('Beacon'), Js('Breakfast'), Js('Bulletin'), Js('Business'), Js('Capital'), Js('Capitol'), Js('Carpe Diem'), Js('Chronicle'), Js('Chronicles'), Js('Citizen'), Js('Community'), Js('Connection'), Js('Courier'), Js('Day Break'), Js('Diem'), Js('Dispatch'), Js('Echo'), Js('Emerald'), Js('Emporium'), Js('Enquirer'), Js('Enterprise'), Js('Epoch'), Js('Era'), Js('Estate'), Js('Evening'), Js('Explorer'), Js('Express'), Js('Eyewitness'), Js('Gazette'), Js('Global'), Js('Globe'), Js('Headline'), Js('Herald'), Js('Heritage'), Js('Home'), Js('Independent'), Js('Inside'), Js('Insider'), Js('Journal'), Js('Leader'), Js('Ledger'), Js('Legacy'), Js('Liberty'), Js('Life'), Js('Local'), Js('Local Voice'), Js('Lodestar'), Js('Look'), Js('Look Back'), Js('Mail'), Js('Metropolitan'), Js('Morn'), Js('Morning Star'), Js('Morning Watch'), Js('Morningtide'), Js('Morrow'), Js('Narrative'), Js('National'), Js('Network'), Js('News'), Js('Nova'), Js('Observer'), Js('Outlook'), Js('Paragon'), Js('Patriot'), Js('Patron'), Js('Pinnacle'), Js('Pioneer'), Js('Prime'), Js('Record'), Js('Register'), Js('Relay'), Js('Report'), Js('Reporter'), Js('Review'), Js('Sentinel'), Js('Society'), Js('Standard'), Js('Star'), Js('Sun'), Js('Telegram'), Js('Telegraph'), Js('Time'), Js('Times'), Js('Tribune'), Js('Union'), Js('Unity'), Js('Vista'), Js('Witness'), Js('World'), Js('Zenith')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (((var.get('nm3').get(var.get('rnd2')).get('0')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm3').get(var.get('rnd2')).get('1')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                    var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm4').get(var.get('rnd2'))+Js(' '))+var.get('nm2').get(var.get('rnd'))))
                    var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm3', Js([Js([Js('The '), Js('Bulletin')]), Js([Js('The '), Js('Chronicle')]), Js([Js('The '), Js('Chronicles')]), Js([Js('The '), Js('Gazette')]), Js([Js('The '), Js('Herald')]), Js([Js('The '), Js('Inquirer')]), Js([Js('The '), Js('Journal')]), Js([Js('The '), Js('Mirror')]), Js([Js(''), Js('News')]), Js([Js(''), Js('News')]), Js([Js(''), Js('News')]), Js([Js('The '), Js('Observer')]), Js([Js('The '), Js('Post')]), Js([Js(''), Js('Press')]), Js([Js('The '), Js('Record')]), Js([Js(''), Js('Record')]), Js([Js('The '), Js('Register')]), Js([Js('The '), Js('Report')]), Js([Js('The '), Js('Reporter')]), Js([Js('The '), Js('Sentinel')]), Js([Js('The '), Js('Telegram')]), Js([Js(''), Js('Time')]), Js([Js(''), Js('Times')]), Js([Js('The '), Js('Time')]), Js([Js('The '), Js('Times')]), Js([Js(''), Js('Tribune')]), Js([Js('The '), Js('Tribune')])]))
var.put('nm4', Js([Js('Daily'), Js('Daily'), Js('Daily'), Js('Weekly'), Js('Morning'), Js('Evening')]))
pass
pass


# Add lib to the module scope
newspaperNames = var.to_python()
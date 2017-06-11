__all__ = ['khmerNames']

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
    var.put('nm1', Js([Js('Achariya'), Js('Akara'), Js('Amara'), Js('Anchaly'), Js('Arun'), Js('Atith'), Js('Bona'), Js('Bora'), Js('Boran'), Js('Borey'), Js('Bourey'), Js('Bunroeun'), Js('Chakara'), Js('Chakra'), Js('Chakriya'), Js('Chamroeun'), Js('Chankrisna'), Js('Chann'), Js('Chanthou'), Js('Chantou'), Js('Chantrea'), Js('Chanvatey'), Js('Chariya'), Js('Charya'), Js('Chea'), Js('Chhay'), Js('Chhaya'), Js('Dara'), Js('Darany'), Js('Davuth'), Js('Heng'), Js('Khemera'), Js('Kiri'), Js('Kosal'), Js('Kravann'), Js('Leap'), Js('Makara'), Js('Many'), Js('Mao'), Js('Mau'), Js('Meaker'), Js('Mittapheap'), Js('Montha'), Js('Mony'), Js('Munney'), Js('Munny'), Js('Narith'), Js('Nhean'), Js('Nimith'), Js('Nimol'), Js('Nisay'), Js('Noreaksey'), Js('Oudom'), Js('Peou'), Js('Phala'), Js('Pheakdei'), Js('Phirum'), Js('Phirun'), Js('Pich'), Js('Piseth'), Js('Pisey'), Js('Poeu'), Js('Ponleak'), Js('Ponleu'), Js('Ponlok'), Js('Prak'), Js('Pros'), Js('Puthyrith'), Js('Rachana'), Js('Rainsey'), Js('Raksmei'), Js('Rangsei'), Js('Rasmey'), Js('Rath'), Js('Rathana'), Js('Rathanak'), Js('Reasmey'), Js('Rith'), Js('Rithipol'), Js('Rithisak'), Js('Rithy'), Js('Roth'), Js('Rotha'), Js('Rothana'), Js('Rothanak'), Js('Rottana'), Js('Sakngea'), Js('Samang'), Js('Samay'), Js('Sambath'), Js('Samlain'), Js('Samnang'), Js('Samphy'), Js('Samrin'), Js('Sangha'), Js('Sann'), Js('Serey'), Js('Sokha'), Js('Sokhem'), Js('Sokhom'), Js('Sokun'), Js('Somnang'), Js('Sonith'), Js('Sopat'), Js('Sopath'), Js('Sophat'), Js('Sophea'), Js('Sopheaktra'), Js('Sopheap'), Js('Sopheara'), Js('Soriya'), Js('Sorya'), Js('Sotearith'), Js('Sotha'), Js('Sotharith'), Js('Sothea'), Js('Sothear'), Js('Sothiya'), Js('Sothy'), Js('Sourkea'), Js('Sov'), Js('Sovann'), Js('Sovanna'), Js('Sovannarith'), Js('Sros'), Js('Thom'), Js('Vannak'), Js('Veasna'), Js('Veha'), Js('Vibol'), Js('Vichear'), Js('Vichet'), Js('Vireak'), Js('Vireakboth'), Js('Visal'), Js('Viseth'), Js('Visna'), Js('Visoth'), Js('Visothirith'), Js('Vithara'), Js('Vithu')]))
    var.put('nm2', Js([Js('Achariya'), Js('Akara'), Js('Anchaly'), Js('Arunny'), Js('Ary'), Js('Bopha'), Js('Botum'), Js('Boupha'), Js('Chakriya'), Js('Champei'), Js('Chamroeun'), Js('Chan'), Js('Chankrisna'), Js('Chanlina'), Js('Chanmony'), Js('Channary'), Js('Chanthavy'), Js('Chanthou'), Js('Chantou'), Js('Chantrea'), Js('Chanvatey'), Js('Chariya'), Js('Charya'), Js('Chavy'), Js('Chaya'), Js('Chenda'), Js('Chhaya'), Js('Chhean'), Js('Chhorvin'), Js('Chhorvon'), Js('Chivy'), Js('Choum'), Js('Da'), Js('Daevy'), Js('Dara'), Js('Darareaksmey'), Js('Davi'), Js('Davy'), Js('Devi'), Js('Jorani'), Js('Kalianne'), Js('Kaliyan'), Js('Kaliyanei'), Js('Kalliyan'), Js('Kanleakhana'), Js('Kannareth'), Js('Kannitha'), Js('Kanya'), Js('Kesor'), Js('Khean'), Js('Kolab'), Js('Koliyan'), Js('Kolthida'), Js('Kravann'), Js('Kunthea'), Js('Leakena'), Js('Leap'), Js('Mach'), Js('Makara'), Js('Malis'), Js('Maly'), Js('Many'), Js('Mao'), Js('Mau'), Js('Mean'), Js('Mliss'), Js('Mony'), Js('Nakry'), Js('Narin'), Js('Nary'), Js('Nearidei'), Js('Neary'), Js('Nuon'), Js('Peou'), Js('Phally'), Js('Phary'), Js('Pheakdei'), Js('Pheakkley'), Js('Phhoung'), Js('Pich'), Js('Pisey'), Js('Poeu'), Js('Ponlok'), Js('Punthea'), Js('Putrea'), Js('Rachana'), Js('Rachany'), Js('Raksmei'), Js('Rangsei'), Js('Rasmey'), Js('Rath'), Js('Rathana'), Js('Reach'), Js('Reaksmey'), Js('Reasmey'), Js('Roth'), Js('Rotha'), Js('Rotha'), Js('Rothana'), Js('Rottana'), Js('Roumduol'), Js('Roumjong'), Js('Saley'), Js('Samphy'), Js('Sathea'), Js('Savady'), Js('Sawatdee'), Js('Seda'), Js('Serey'), Js('Setha'), Js('Seyha'), Js('Sikha'), Js('Sinuon'), Js('Sita'), Js('Sobin'), Js('Soboen'), Js('Socheat'), Js('Sok'), Js('Sokha'), Js('Sokhanya'), Js('Sokhom'), Js('Sombo'), Js('Sonisay'), Js('Sophal'), Js('Sophea'), Js('Sopheap'), Js('Sopheary'), Js('Sophon'), Js('Sophorn'), Js('Soportevy'), Js('Soriya'), Js('Soriya'), Js('Sorpheny'), Js('Sorya'), Js('Sotear'), Js('Sotear'), Js('Sotearith'), Js('Sothea'), Js('Sotheara'), Js('Sothy'), Js('Sourkea'), Js('Sovanara'), Js('Sovandary'), Js('Sovaneary'), Js('Sovann'), Js('Sovanna'), Js('Sovannary'), Js('Sraem'), Js('Srey'), Js('SreyPek'), Js('Sreymom'), Js('Sreynuon'), Js('Sreypich'), Js('Sros'), Js('Suorsdey'), Js('Taevy'), Js('Tevy'), Js('Thavary'), Js('Theary'), Js('Thida'), Js('Thom'), Js('Thyda'), Js('Tina'), Js('Toch'), Js('Touch'), Js('Vanna'), Js('Veasna'), Js('Veata'), Js('Vimean'), Js('Visal'), Js('Visna')]))
    var.put('nm3', Js([Js('Aang'), Js('Aek'), Js('Ang'), Js('Aok'), Js('Ben'), Js('Bun'), Js('Chak'), Js('Chan'), Js('Chea'), Js('Chen'), Js('Chey'), Js('Chhan'), Js('Chhay'), Js('Chhem'), Js('Chhet'), Js('Chhim'), Js('Chhit'), Js('Chhorn'), Js('Chhoub'), Js('Chim'), Js('Chin'), Js('Choem'), Js('Choeun'), Js('Din'), Js('Dith'), Js('Dul'), Js('Duong'), Js('Eam'), Js('Eav'), Js('Ek'), Js('Em'), Js('Heang'), Js('Ho'), Js('Hong'), Js('Hoy'), Js('Hu'), Js('Hun'), Js('Iam'), Js('Iem'), Js('Im'), Js('Iv'), Js('Jan'), Js('Jay'), Js('Jen'), Js('Jey'), Js('Jin'), Js('Keo'), Js('Khai'), Js('Khan'), Js('Khat'), Js('Khay'), Js('Khiev'), Js('Khin'), Js('Khlot'), Js('Khoun'), Js('Khun'), Js('Kim'), Js('Kong'), Js('Lim'), Js('Long'), Js('Lorn'), Js('Loun'), Js('Ma'), Js('Mak'), Js('Mao'), Js('Mean'), Js('Meang'), Js('Meas'), Js('Meng'), Js('Mok'), Js('Mon'), Js('Moul'), Js('Mul'), Js('Muoy'), Js('Muy'), Js('Neak'), Js('Nhek'), Js('Noung'), Js('Nourn'), Js('Nout'), Js('Ok'), Js('Om'), Js('On'), Js('Ong'), Js('Or'), Js('Ou'), Js('Ouch'), Js('Ouk'), Js('Pang'), Js('Pen'), Js('Phan'), Js('Phann'), Js('Pheng'), Js('Phon'), Js('Phy'), Js('Pok'), Js('Prak'), Js('Preap'), Js('Prum'), Js('Ros'), Js('Rous'), Js('Saluk'), Js('Sam'), Js('San'), Js('Sang'), Js('Sar'), Js('Sat'), Js('Say'), Js('Seang'), Js('Sen'), Js('Seng'), Js('Sieng'), Js('Sin'), Js('So'), Js('Sok'), Js('Sok '), Js('Som'), Js('Son'), Js('Song'), Js('Sor'), Js('Sorm'), Js('Soun'), Js('Su'), Js('Suy'), Js('Tang'), Js('Tat'), Js('Tep'), Js('Thith'), Js('Thy'), Js('Toch'), Js('Touch'), Js('Tum'), Js('Ty'), Js('Uch'), Js('Um'), Js('Ung'), Js('Uy'), Js('Vang'), Js('Voeum'), Js('Yim'), Js('Yos'), Js('Yous'), Js('Yu'), Js('Yun')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm1').get(var.get('rnd2'))))
            var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
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
khmerNames = var.to_python()
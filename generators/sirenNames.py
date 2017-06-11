__all__ = ['sirenNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aba'), Js('Aca'), Js('Acale'), Js('Ado'), Js('Adra'), Js('Aeleo'), Js('Aethe'), Js('Aethi'), Js('Agla'), Js('Aglao'), Js('Aiga'), Js('Ala'), Js('Alci'), Js('Ama'), Js('Amali'), Js('Amy'), Js('Ani'), Js('Ara'), Js('Aroa'), Js('Asi'), Js('Aste'), Js('Asteo'), Js('Ate'), Js('Boli'), Js('Bor'), Js('Cali'), Js('Calli'), Js('Calo'), Js('Caly'), Js('Cela'), Js('Cha'), Js('Ciri'), Js('Cla'), Js('Cly'), Js('Cora'), Js('Cori'), Js('Coro'), Js('Cria'), Js('Daei'), Js('Dana'), Js('Daph'), Js('Daphi'), Js('Dio'), Js('Dori'), Js('Dory'), Js('Echi'), Js('Echo'), Js('Eli'), Js('Elu'), Js('Ephe'), Js('Euphe'), Js('Eva'), Js('Evi'), Js('Gali'), Js('Hai'), Js('Heli'), Js('Hi'), Js('Hime'), Js('Ia'), Js('Iana'), Js('Iao'), Js('Ida'), Js('Idah'), Js('Ila'), Js('Ile'), Js('Ipha'), Js('Kahli'), Js('Kali'), Js('Kalli'), Js('Kela'), Js('Kimo'), Js('Kle'), Js('Kleo'), Js('Lame'), Js('Lami'), Js('Lao'), Js('Laome'), Js('Lari'), Js('Leu'), Js('Leuco'), Js('Li'), Js('Limo'), Js('Ma'), Js('Mai'), Js('Mali'), Js('Mary'), Js('Me'), Js('Meli'), Js('Meni'), Js('Meti'), Js('Metio'), Js('Mol'), Js('More'), Js('Mys'), Js('Nai'), Js('Nea'), Js('Neame'), Js('Neda'), Js('Neme'), Js('Nemen'), Js('Nephe'), Js('Neri'), Js('Nesa'), Js('Nona'), Js('Nysa'), Js('Ole'), Js('Ori'), Js('Pala'), Js('Palle'), Js('Par'), Js('Pasi'), Js('Pei'), Js('Peisi'), Js('Perei'), Js('Peri'), Js('Peti'), Js('Peto'), Js('Phali'), Js('Phe'), Js('Phero'), Js('Phi'), Js('Phia'), Js('Phio'), Js('Phri'), Js('Physa'), Js('Pi'), Js('Pire'), Js('Pisi'), Js('Porei'), Js('Rai'), Js('Rhae'), Js('Rhe'), Js('Rhene'), Js('Sabri'), Js('Sala'), Js('Salo'), Js('Sapha'), Js('Sava'), Js('Syli'), Js('Syna'), Js('Tania'), Js('Te'), Js('Tele'), Js('The'), Js('Thel'), Js('Thelxie'), Js('Themi'), Js('Thoni'), Js('Zeli')]))
var.put('nm2', Js([Js('cea'), Js('cia'), Js('cine'), Js('danea'), Js('deia'), Js('delia'), Js('della'), Js('dia'), Js('dise'), Js('doe'), Js('done'), Js('dora'), Js('dorise'), Js('ete'), Js('gale'), Js('geia'), Js('genia'), Js('gina'), Js('gonia'), Js('goria'), Js('kaia'), Js('kea'), Js('kharei'), Js('lacia'), Js('laeno'), Js('laira'), Js('lane'), Js('lato'), Js('lea'), Js('leia'), Js('lenia'), Js('leora'), Js('les'), Js('lia'), Js('liana'), Js('lina'), Js('linai'), Js('liphis'), Js('lira'), Js('lirea'), Js('liria'), Js('lis'), Js('lise'), Js('lodia'), Js('lopei'), Js('lophi'), Js('lyse'), Js('mea'), Js('mei'), Js('meia'), Js('meine'), Js('melle'), Js('mellia'), Js('mene'), Js('meni'), Js('menis'), Js('mia'), Js('milia'), Js('mine'), Js('mis'), Js('misa'), Js('misia'), Js('moni'), Js('naera'), Js('nara'), Js('nassa'), Js('nea'), Js('nei'), Js('neira'), Js('nele'), Js('nia'), Js('niassi'), Js('nilla'), Js('nise'), Js('nisse'), Js('noe'), Js('nohre'), Js('noire'), Js('nome'), Js('nope'), Js('nophe'), Js('nore'), Js('nos'), Js('pe'), Js('pea'), Js('peia'), Js('phaeia'), Js('phaia'), Js('phei'), Js('pheia'), Js('pheme'), Js('pheu'), Js('phia'), Js('phine'), Js('phise'), Js('phite'), Js('phonos'), Js('pise'), Js('rane'), Js('rea'), Js('reanes'), Js('recea'), Js('rei'), Js('reia'), Js('reino'), Js('reisis'), Js('relia'), Js('rephis'), Js('ria'), Js('rianne'), Js('riko'), Js('rila'), Js('riope'), Js('ris'), Js('rise'), Js('riye'), Js('rodia'), Js('ronei'), Js('ronis'), Js('rope'), Js('rose'), Js('sa'), Js('sea'), Js('seis'), Js('seise'), Js('sesis'), Js('sia'), Js('sine'), Js('siphe'), Js('sis'), Js('sise'), Js('tai'), Js('tea'), Js('teia'), Js('the'), Js('thea'), Js('thei'), Js('theis'), Js('thelia'), Js('thera'), Js('thilei'), Js('thise'), Js('thoe'), Js('thusa'), Js('thyia'), Js('thylia'), Js('tiax'), Js('xera'), Js('xiope')]))
var.put('nm3', Js([Js('Adra'), Js('Adre'), Js('Adrea'), Js('Adri'), Js('Adria'), Js('Adrie'), Js('Ae'), Js('Aega'), Js('Aere'), Js('Aeri'), Js('Aethe'), Js('Allu'), Js('Alu'), Js('Ama'), Js('Ana'), Js('Aqea'), Js('Aqia'), Js('Aqua'), Js('Aqui'), Js('Ari'), Js('Arie'), Js('Arri'), Js('Arrie'), Js('Assa'), Js('Aura'), Js('Ava'), Js('Aza'), Js('Bri'), Js('Calla'), Js('Chel'), Js('Chene'), Js('Cheri'), Js('Cora'), Js('Corae'), Js('Corde'), Js('Corea'), Js('Corra'), Js('Corrae'), Js('Dali'), Js('Dela'), Js('Delma'), Js('Delo'), Js('Dia'), Js('Dio'), Js('Do'), Js('Dorea'), Js('Doria'), Js('Dorie'), Js('Eathe'), Js('Echo'), Js('Eire'), Js('Fonta'), Js('Gene'), Js('Geni'), Js('Gine'), Js('Guine'), Js('Hali'), Js('Hy'), Js('Jenie'), Js('Jenni'), Js('Jeny'), Js('Kai'), Js('Ky'), Js('Lagu'), Js('Lai'), Js('Larai'), Js('Lorae'), Js('Lorai'), Js('Lore'), Js('Mari'), Js('Mary'), Js('Maya'), Js('Mello'), Js('Melo'), Js('Mere'), Js('Meri'), Js('Mira'), Js('Morga'), Js('Muri'), Js('Murie'), Js('Na'), Js('Nada'), Js('Nah'), Js('Nari'), Js('Nau'), Js('Nauti'), Js('Nerei'), Js('Neri'), Js('Noe'), Js('Oara'), Js('Oce'), Js('Ocea'), Js('Ora'), Js('Rae'), Js('Sere'), Js('Serei'), Js('She'), Js('Shei'), Js('Sire'), Js('Sirei'), Js('Tali'), Js('Talo'), Js('Tha'), Js('Thala'), Js('The'), Js('Thessa'), Js('Undi'), Js('Vivi'), Js('Vivia'), Js('Vivie'), Js('Ya'), Js('Zha')]))
var.put('nm4', Js([Js('bel'), Js('belle'), Js('ciane'), Js('da'), Js('dah'), Js('denah'), Js('dina'), Js('dine'), Js('fa'), Js('fer'), Js('gana'), Js('guna'), Js('gune'), Js('haneh'), Js('la'), Js('lea'), Js('lee'), Js('leh'), Js('lei'), Js('lena'), Js('lia'), Js('lila'), Js('lin'), Js('lina'), Js('lis'), Js('lise'), Js('lla'), Js('lle'), Js('lody'), Js('lora'), Js('lori'), Js('lura'), Js('lure'), Js('ly'), Js('lyn'), Js('ma'), Js('mala'), Js('mara'), Js('mare'), Js('me'), Js('meda'), Js('mere'), Js('mora'), Js('na'), Js('nah'), Js('ne'), Js('neh'), Js('nella'), Js('nelle'), Js('neva'), Js('ney'), Js('nia'), Js('nna'), Js('nne'), Js('noe'), Js('nora'), Js('nore'), Js('ny'), Js('ra'), Js('rah'), Js('rea'), Js('reida'), Js('rena'), Js('rene'), Js('renna'), Js('ria'), Js('rial'), Js('rian'), Js('riel'), Js('rien'), Js('rin'), Js('rina'), Js('rinda'), Js('rinia'), Js('ris'), Js('rissa'), Js('rith'), Js('roe'), Js('ros'), Js('sana'), Js('sea'), Js('shell'), Js('shi'), Js('ssa'), Js('sura'), Js('ta'), Js('thea'), Js('thia'), Js('tina'), Js('tune'), Js('va'), Js('ve'), Js('vere'), Js('via'), Js('viane'), Js('vianna'), Js('vien'), Js('wai'), Js('wen'), Js('xie')]))
pass
pass


# Add lib to the module scope
sirenNames = var.to_python()
__all__ = ['argonianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+Js(' '))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2')))+Js(' '))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+Js(' '))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Alex'), Js('Antigon'), Js('August'), Js('Calig'), Js('Claud'), Js('Demer'), Js('Dioclet'), Js('German'), Js('Her'), Js('Jul'), Js('Ner'), Js('Pil'), Js('Tib'), Js('Asu'), Js('Bun'), Js('Bus'), Js('Cha'), Js('Chi'), Js('Chu'), Js('Chu'), Js('Har'), Js('Hat'), Js('Hee'), Js('Hul'), Js('Huz'), Js('Ine'), Js('Ita'), Js('Mee'), Js('Mil'), Js('Nee'), Js('Oka'), Js('Pee'), Js('Ras'), Js('Ree'), Js('Ree'), Js('See'), Js('Ske'), Js('Tan'), Js('Tee'), Js('Tul'), Js('Uka'), Js('Ula'), Js('Uta'), Js('Wee'), Js('Wee'), Js('Sis'), Js('Yel'), Js('Amu'), Js('Dee'), Js('Gee'), Js('Jee'), Js('Mah'), Js('Otu'), Js('Paj'), Js('Ree'), Js('Sak'), Js('Sal'), Js('Tee'), Js('Tei'), Js('Ush'), Js('Wum'), Js('Yin'), Js('Dee'), Js('Der'), Js('Mad'), Js('Nee'), Js('Ush'), Js('Vee'), Js('Dee'), Js('She'), Js('Tsl'), Js('Asum'), Js('Buni'), Js('Bush'), Js('Chal'), Js('Chiw'), Js('Chul'), Js('Chun'), Js('Hara'), Js('Hath'), Js('Heed'), Js('Hule'), Js('Huze'), Js('Inee'), Js('Itan'), Js('Meer'), Js('Milo'), Js('Neet'), Js('Okaw'), Js('Peer'), Js('Rash'), Js('Reem'), Js('Rees'), Js('Seew'), Js('Skee'), Js('Tana'), Js('Teeg'), Js('Tul'), Js('Ukaw'), Js('Ula'), Js('Utad'), Js('Weel'), Js('Weer'), Js('Siss'), Js('Yeln'), Js('Amus'), Js('Deeh'), Js('Geel'), Js('Jeel'), Js('Mahe'), Js('Otum'), Js('Paje'), Js('Reen'), Js('Sake'), Js('Sali'), Js('Teek'), Js('Tein'), Js('Ushe'), Js('Wume'), Js('Yinz'), Js('Deek'), Js('Derk'), Js('Made'), Js('Neet'), Js('Usha'), Js('Veez'), Js('Deer'), Js('Sheh'), Js('Tsle')]))
var.put('nm2', Js([Js('meya'), Js('ish'), Js('heeus'), Js('lureel'), Js('wish'), Js('lz'), Js('na'), Js('an'), Js('hei'), Js('dul'), Js('eeya'), Js('ei'), Js('erei'), Js('neen'), Js('raz'), Js('os'), Js('tinei'), Js('wor'), Js('radeeh'), Js('ha'), Js('mukeeus'), Js('sa'), Js('wul'), Js('etul'), Js('an'), Js('gla'), Js('wei'), Js('deek'), Js('ltul'), Js('re'), Js('sithik'), Js('nicin'), Js('sei'), Js('haj'), Js('leesh'), Js('lius'), Js('ei'), Js('meel'), Js('een'), Js('num'), Js('eepa'), Js('iith'), Js('keeus'), Js('naava'), Js('eeja'), Js('eek'), Js("z'k"), Js('kus'), Js('keethus'), Js('esi'), Js('trenaza'), Js('are'), Js('zara'), Js('rkaza'), Js('hsi'), Js('eeixth'), Js('sh'), Js('eeus'), Js('ureel'), Js('ish'), Js("z'r"), Js("a'th"), Js('nee'), Js('ei'), Js('ul'), Js('eya'), Js('il'), Js('sehk'), Js('inei'), Js('adeeh'), Js('akees'), Js('ukeeus'), Js('at'), Js('ul'), Js('tul'), Js('nesh'), Js('la'), Js('ei'), Js('eek'), Js('tul'), Js('ithik'), Js('icin'), Js('ei'), Js('ius'), Js('ieth'), Js('eel'), Js('en'), Js('um'), Js('epa'), Js('ith'), Js('eeus'), Js('aava'), Js('eja'), Js('ek'), Js("k'r"), Js('us'), Js('eethus'), Js('si'), Js('renaza'), Js('ara'), Js('kaza'), Js("s'r"), Js('eixth'), Js('acles'), Js('andros'), Js('ate'), Js('erius'), Js('ian'), Js('iar'), Js('icus'), Js('ides'), Js('ios'), Js('ius'), Js('os'), Js('ula'), Js('us')]))
var.put('nm3', Js([Js('An'), Js('Bun'), Js('Bar'), Js('Dan'), Js('Effe'), Js('Eleedal'), Js('Gah'), Js('Gam'), Js('Geel'), Js('Haj'), Js('Han'), Js('Heem'), Js('Heir'), Js('Im'), Js('Jeelus'), Js('Jeer'), Js("J'Ram"), Js('Junal'), Js('Keerasa'), Js('Miun'), Js('Mush'), Js('Okan'), Js('Oleen'), Js('Olink'), Js('Reeh'), Js('Silm'), Js('Tee'), Js('Tim'), Js('Vistha'), Js('Wanan'), Js('Wih'), Js('Wud'), Js('Wuleen'), Js('Ah'), Js('Ajum'), Js('Beem'), Js('Dar'), Js('Deetum'), Js('Dreet'), Js('Er'), Js('Geem'), Js('Gin'), Js('Jee'), Js('Jeetum'), Js('Oleed'), Js('Pad'), Js('Tar'), Js('Tun'), Js('Weebam'), Js('Beem'), Js('Brand'), Js('Gulum'), Js('Ilas'), Js('Jaree'), Js('Talen'), Js('Teeba'), Js('Bah')]))
var.put('nm4', Js([Js('-Zaw'), Js('-Teemeeta'), Js('-Ru'), Js('-Tei'), Js('-Lei'), Js('-Julan'), Js('-Kur'), Js('-Lah'), Js('-Ei'), Js('-Tulm'), Js('-La'), Js('-Zish'), Js('-Kilaya'), Js('-Tei'), Js('-Maht'), Js('-Dar'), Js('-Lei'), Js('-Tan'), Js('-Gei'), Js('-Mere'), Js('-Shei'), Js('-Gei'), Js('-Nur'), Js('-Jah'), Js('-Dar'), Js('-Lan'), Js('-Jush'), Js('-Kai'), Js('-Dum'), Js('-Eius'), Js('-Neeus'), Js('-Shei'), Js('-Malz'), Js('-Kajin'), Js('-Kiurz'), Js('-Jee'), Js('-Ja'), Js('-Ju'), Js('-Lai'), Js('-Teeus'), Js('-Jasaiin'), Js('-Wulm'), Js('-Tah'), Js('-Ze'), Js('-Ei'), Js('-Ei'), Js('-Meena'), Js('-Zeeus'), Js('-Na'), Js('-Ja'), Js('-Shei'), Js('-Ei'), Js('-Tei'), Js('-Ra'), Js('-Jei'), Js('-Ei')]))
var.put('nm5', Js([Js('Ahah'), Js('Akis'), Js('Bana'), Js('Beek'), Js('Eute'), Js('Gilm'), Js('Gish'), Js('Hule'), Js('Kasa'), Js('Mila'), Js('Naku'), Js('Nees'), Js('Nura'), Js('Nush'), Js('Okur'), Js('Onas'), Js('Shat'), Js('Tash'), Js('Wush'), Js('Beel'), Js('Beew'), Js('Beje'), Js('Deet'), Js('Druj'), Js('Marz'), Js('Nume'), Js('Oche'), Js('Pash'), Js('Rana'), Js('Shal'), Js('Skal'), Js('Wits'), Js('Deej'), Js('Keer'), Js('Shah'), Js('Wuje'), Js('Aha'), Js('Aki'), Js('Ban'), Js('Bee'), Js('Eut'), Js('Gil'), Js('Gis'), Js('Hul'), Js('Kas'), Js('Mil'), Js('Nak'), Js('Nee'), Js('Nur'), Js('Nus'), Js('Oku'), Js('Ona'), Js('Sha'), Js('Tas'), Js('Wus'), Js('Bee'), Js('Bee'), Js('Bej'), Js('Dee'), Js('Dru'), Js('Mar'), Js('Num'), Js('Och'), Js('Pas'), Js('Ran'), Js('Sha'), Js('Ska'), Js('Wit'), Js('Dee'), Js('Kee'), Js('Sha'), Js('Wuj')]))
var.put('nm6', Js([Js('ht'), Js('sh'), Js('alz'), Js('katan'), Js('ei'), Js('mee'), Js('hee'), Js('ayee'), Js('ah'), Js('uma'), Js('sha'), Js('alg'), Js("h'r"), Js('resh'), Js('sha'), Js('talg'), Js('ha'), Js('ha'), Js('lei'), Js('wos'), Js('een'), Js('tsan'), Js('ja'), Js("z'r"), Js('een'), Js('eeva'), Js('ha'), Js('aye'), Js('leez'), Js('leel'), Js('seidutsei'), Js('ja'), Js('rava'), Js('hvee'), Js('eeta'), Js('tvee'), Js('haz'), Js('lz'), Js('atan'), Js('ila'), Js('hota'), Js('ma'), Js('ha'), Js('lg'), Js('ha'), Js('alg'), Js('aree'), Js('aza'), Js('ei'), Js('os'), Js('en'), Js('san'), Js('araje'), Js('en'), Js('eva'), Js('a'), Js('eez'), Js('eel'), Js('eedutsee'), Js('ayo'), Js('ava'), Js('vee'), Js('eta')]))
var.put('nm7', Js([Js('Ah'), Js('Am'), Js('An'), Js('Bur'), Js('Chanil'), Js('Cheesh'), Js('Dar'), Js('Deesh'), Js('El'), Js('Ereel'), Js('Gih'), Js('Hal'), Js('Jeed'), Js('Kal'), Js('Keel'), Js('Kud'), Js('Mach'), Js('Meeh'), Js('Meen'), Js('Mim'), Js('Muz'), Js('Nam'), Js('Olank'), Js('On'), Js('Seed'), Js('Seen'), Js('Sheer '), Js('Tar'), Js('Weedum'), Js('Erh'), Js('Amee'), Js('Aney'), Js('Bour'), Js('Cheenal'), Js('Chesoh'), Js('Dur'), Js('Deeth'), Js('En'), Js('Ereej'), Js('Ginh'), Js('Kahl'), Js('Jid'), Js('Kani'), Js('Kelo'), Js('Kudo'), Js('Meech'), Js('Meefh'), Js('Mereen'), Js('Meem'), Js('Mez'), Js('Nem'), Js('Olink'), Js('Oneer'), Js('Sedir'), Js('Tereen'), Js('Sheef '), Js('Thari'), Js('Wedum')]))
var.put('nm8', Js([Js('-Deesei'), Js('-Ei'), Js('-Ja'), Js('-Jeen'), Js('-La'), Js('-Lee'), Js('-Lei'), Js('-Liurz'), Js('-Lurasha'), Js('-Ma'), Js('-Meedish'), Js('-Meema'), Js('-Meena'), Js('-Meesei'), Js('-Meeus'), Js('-Mei'), Js('-Na'), Js('-Neeus'), Js('-Ra'), Js('-Raniur'), Js('-Rei'), Js('-Sa'), Js('-Wan'), Js('-Wazei'), Js('-Deese'), Js('-Eji'), Js('-Jazee'), Js('-Jereen'), Js('-Lari'), Js('-Leef'), Js('-Leith'), Js('-Liruz'), Js('-Lursha'), Js('-Maki'), Js('-Mideesh'), Js('-Meemar'), Js('-Menari'), Js('-Meseif'), Js('-Meefus'), Js('-Meik'), Js('-Nash'), Js('-Nevus'), Js('-Rafee'), Js('-Ranier'), Js('-Reij'), Js('-Kajee'), Js('-Wahn'), Js('-Wareih'), Js('-Deseith'), Js('-Eijar'), Js('-Jarlee'), Js('-Jeleen'), Js('-Lak'), Js('-Leehp'), Js('-Leish'), Js('-Lirzee'), Js('-Leesha'), Js('-Majee'), Js('-Meedish'), Js('-Mena'), Js('-Meeka'), Js('-Meei'), Js('-Neeus'), Js('-Slei'), Js('-Nha'), Js('-Nefeus'), Js('-Rajee'), Js('-Raneer'), Js('-Reiki'), Js('-Sakee'), Js('-Ran'), Js('-Razei')]))
var.put('nm9', Js([Js('Andro'), Js('Augus'), Js('Ca'), Js('Cae'), Js('Cali'), Js('Gal'), Js('Mag'), Js('Me'), Js('Ni'), Js('Per'), Js('Theo'), Js('Tiber'), Js('Xer'), Js('Andree'), Js('Augees'), Js('Caya'), Js('Caree'), Js('Calee'), Js('Geel'), Js('Nag'), Js('Meree'), Js('Nefe'), Js('Peri'), Js('Thefi'), Js('Tikeer'), Js('Xeir'), Js('Endore'), Js('Agius'), Js('Cas'), Js('Cay'), Js('Cani'), Js('Kay'), Js('Laf'), Js('Pe'), Js('Neeth'), Js('Pehr'), Js('Theer'), Js('Taier'), Js('Xem')]))
var.put('nm10', Js([Js('cles'), Js('des'), Js('dorus'), Js('gulus'), Js('lus'), Js('mean'), Js('mus'), Js('nes'), Js('sar'), Js('seus'), Js('sion'), Js('ssius'), Js('tus'), Js('calees'), Js('desh'), Js('dorees'), Js('goulus'), Js('lures'), Js('mareen'), Js('museeth'), Js('mesh'), Js('sareth'), Js('sesh'), Js('seene'), Js('seus'), Js('tius'), Js('clesh'), Js('daresh'), Js('deseer'), Js('galus'), Js('leesh'), Js('rean'), Js('marush'), Js('naresh'), Js('sareeth'), Js('teus'), Js('sifon'), Js('silus'), Js('thees')]))
pass
pass


# Add lib to the module scope
argonianNames = var.to_python()
__all__ = ['northEuropeTowns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(16.0)):
        try:
            if (var.get('i')<Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', (var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                            var.put('names', (var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2'))))
                        else:
                            if (var.get('i')<Js(10.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                                var.put('names', (var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2'))))
                            else:
                                if (var.get('i')<Js(12.0)):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                                    var.put('names', (var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2'))))
                                else:
                                    if (var.get('i')<Js(14.0)):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                                        var.put('names', (var.get('nm13').get(var.get('rnd'))+var.get('nm14').get(var.get('rnd2'))))
                                    else:
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                        var.put('names', (var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aal'), Js('Balle'), Js('Birke'), Js('Brønd'), Js('Es'), Js('Haders'), Js('Hel'), Js('Hol'), Js('Kol'), Js('Lyng'), Js('Nørre'), Js('Rød'), Js('Ring'), Js('Ros'), Js('Sønder'), Js('Silke'), Js('Svend'), Js('Tårn'), Js('Taa'), Js('Vi'), Js('Kors'), Js('Øster'), Js('Vester'), Js('Ege'), Js('Konge'), Js('Ul'), Js('Al'), Js('Ny'), Js('Lys'), Js('Avn'), Js('Bede'), Js('Binde'), Js('Bjørn'), Js('Blæs'), Js('Blå'), Js('Bred'), Js('Bøge'), Js('Dam'), Js('Dyb'), Js('Due'), Js('Drags'), Js('El'), Js('Engels'), Js('Ens'), Js('Favr'), Js('Flad'), Js('Flint'), Js('Fri'), Js('Fugle'), Js('Gammel'), Js('Grøn'), Js('Guld'), Js('Hal'), Js('Has'), Js('Hjorts'), Js('Hund'), Js('Hvid'), Js('Høj'), Js('Karls'), Js('Kirke'), Js('Knud'), Js('Krage'), Js('Kær'), Js('Lang'), Js('Lille'), Js('Mejl'), Js('Mose'), Js('Mølle'), Js('Neder'), Js('Over'), Js('Rand'), Js('Rød'), Js('Sand'), Js('Skjold'), Js('Smede'), Js('Stor'), Js('Strand'), Js('Tegl'), Js('Ting'), Js('Vej'), Js('Vind')]))
var.put('nm2', Js([Js('bæk'), Js('bjerg'), Js('borg'), Js('by'), Js('havn'), Js('holm'), Js('hus'), Js('kilde'), Js('lev'), Js('lund'), Js('rup'), Js('lev'), Js('sted'), Js('strup'), Js('trup'), Js('bro'), Js('hus'), Js('ager'), Js('skov'), Js('bøl'), Js('høj'), Js('gård'), Js('holt')]))
var.put('nm3', Js([Js('Ab'), Js('Ant'), Js('El'), Js('Haap'), Js('Jõge'), Js('Jõh'), Js('Kär'), Js('Kal'), Js('Kar'), Js('Keh'), Js('Kei'), Js('Ki'), Js('Kiviõ'), Js('Koht'), Js('Kun'), Js('Kure'), Js('Li'), Js('Lihu'), Js('Lok'), Js('Mõisa'), Js('Maar'), Js('Must'), Js('Nar'), Js('Ote'), Js('Pär'), Js('Põl'), Js('Pai'), Js('Pal'), Js('Rä'), Js('Räpi'), Js('Rak'), Js('Rap'), Js('Silla'), Js('Sin'), Js('Suur'), Js('Tõr'), Js('Tü'), Js('Ta'), Js('Tal'), Js('Tam'), Js('Tar'), Js('Võ'), Js('Võh'), Js('Val'), Js('Vil')]))
var.put('nm4', Js([Js('de'), Js('di'), Js('diski'), Js('duu'), Js('ga'), Js('geva'), Js('hula'), Js('ja'), Js('jandi'), Js('küla'), Js('la'), Js('lamäe'), Js('li'), Js('lin'), Js('lingi'), Js('linn'), Js('luoja'), Js('mäe'), Js('ma'), Js('me'), Js('mme'), Js('na'), Js('ngi'), Js('nu'), Js('pää'), Js('pa'), Js('pina'), Js('ra'), Js('ri'), Js('ru'), Js('sa'), Js('saare'), Js('salu'), Js('samaa'), Js('si'), Js('ski'), Js('ssaare'), Js('ssi'), Js('ste'), Js('suu'), Js('tu'), Js('va'), Js('vee'), Js('vere'), Js('viõli'), Js('vi')]))
var.put('nm5', Js([Js('Ääne'), Js('Ähtä'), Js('Ala'), Js('Hämeen'), Js('Ha'), Js('Haapa'), Js('Han'), Js('Harja'), Js('Hauki'), Js('Hei'), Js('Hel'), Js('Hui'), Js('Hy'), Js('Iisal'), Js('Ikaa'), Js('Ima'), Js('Jäm'), Js('Järven'), Js('Joen'), Js('Juan'), Js('Jyväs'), Js('Ka'), Js('Kaa'), Js('Kala'), Js('Kan'), Js('Kankaan'), Js('Kark'), Js('Kas'), Js('Kau'), Js('Kauha'), Js('Ke'), Js('Kemi'), Js('Kera'), Js('Keu'), Js('Ki'), Js('Kiure'), Js('Kok'), Js('Koke'), Js('Kot'), Js('Kou'), Js('Kuh'), Js('Kuo'), Js('Kuri'), Js('Kuu'), Js('La'), Js('Lah'), Js('Lai'), Js('Lappeen'), Js('Liek'), Js('Lo'), Js('Loh'), Js('Loi'), Js('Män'), Js('Mik'), Js('När'), Js('Naan'), Js('Ni'), Js('Nil'), Js('No'), Js('Nur'), Js('Ori'), Js('Orima'), Js('Ou'), Js('Outo'), Js('Pa'), Js('Pai'), Js('Par'), Js('Piek'), Js('Pietar'), Js('Pro'), Js('Pudas'), Js('Pyhä'), Js('Raase'), Js('Rai'), Js('Riihi'), Js('Rova'), Js('Saari'), Js('Sasta'), Js('Savon'), Js('Seinä'), Js('Siu'), Js('So'), Js('Suonen'), Js('Tam'), Js('Tor'), Js('Tur'), Js('Ul'), Js('Ussi'), Js('Uusikau'), Js('Valkea'), Js('Van'), Js('Var'), Js('Viita'), Js('Ylö'), Js('Yli')]))
var.put('nm6', Js([Js('hamina'), Js('hava'), Js('järvi'), Js('joki'), Js('kää'), Js('kano'), Js('kaupunki'), Js('keli'), Js('kia'), Js('kila'), Js('kinen'), Js('ko'), Js('kola'), Js('koski'), Js('ksa'), Js('kumpu'), Js('kylä'), Js('lepyy'), Js('linen'), Js('linna'), Js('mäki'), Js('mi'), Js('mina'), Js('ni'), Js('niemi'), Js('nkää'), Js('nola'), Js('ntio'), Js('pää'), Js('piö'), Js('pio'), Js('pori'), Js('pua'), Js('pudas'), Js('pula'), Js('punki'), Js('rainen'), Js('ranta'), Js('rava'), Js('ri'), Js('rina'), Js('ruu'), Js('sä'), Js('sämäki'), Js('saari'), Js('siä'), Js('sinki'), Js('ssa'), Js('suu'), Js('tali'), Js('tee'), Js('tila'), Js('tinen'), Js('tra'), Js('ttila'), Js('ttinen'), Js('vala'), Js('valta'), Js('vesi'), Js('vieska'), Js('viisa'), Js('voo'), Js('vus')]))
var.put('nm7', Js([Js('Álf'), Js('Árbæjar'), Js('Ísaf'), Js('Ólafs'), Js('Þórs'), Js('Þin'), Js('Þorláks'), Js('Ak'), Js('Aku'), Js('Bíldu'), Js('Búðar'), Js('Bakka'), Js('Bi'), Js('Blön'), Js('Bolungar'), Js('Borgar'), Js('Brúnah'), Js('Brautar'), Js('Breiðdals'), Js('Byggðak'), Js('Dal'), Js('Djúpi'), Js('Drang'), Js('Eglis'), Js('Eskif'), Js('Eyrar'), Js('Fjalla'), Js('Garða'), Js('Grím'), Js('Greni'), Js('Grinda'), Js('Grundar'), Js('Hó'), Js('Hól'), Js('Húsa'), Js('Haf'), Js('Hafnar'), Js('Helli'), Js('Hnífs'), Js('Hof'), Js('Hrí'), Js('Hraf'), Js('Hua'), Js('Hvamm'), Js('Hvan'), Js('Hvera'), Js('Hvols'), Js('Inn'), Js('Kópa'), Js('Kópas'), Js('Kefla'), Js('Krist'), Js('Lóns'), Js('Lauga'), Js('Laugar'), Js('Lit'), Js('Melah'), Js('Mosfells'), Js('Nesjah'), Js('Neskau'), Js('Nja'), Js('Patreks'), Js('Raufar'), Js('Reyk'), Js('Sól'), Js('Sand'), Js('Sauðár'), Js('Sel'), Js('Seltjar'), Js('Seyðis'), Js('Skaga'), Js('Stok'), Js('Stuk'), Js('Sval'), Js('Tálkna'), Js('Tjarna'), Js('Varmah'), Js('Vest'), Js('Vopna')]))
var.put('nm8', Js([Js('tanes'), Js('verfi'), Js('jarhverfi'), Js('fjörður'), Js('vík'), Js('höfn'), Js('nes'), Js('reyri'), Js('dalur'), Js('röst'), Js('duós'), Js('nesi'), Js('nes'), Js('líð'), Js('holt'), Js('jarni'), Js('vogur'), Js('snes'), Js('staðir'), Js('bakki'), Js('bær'), Js('byggð'), Js('ðir'), Js('ður'), Js('sey'), Js('verfi'), Js('nir'), Js('ganes'), Js('sandur'), Js('ssandur'), Js('dalur'), Js('sós'), Js('nagil'), Js('stangi'), Js('neyri'), Js('gerði'), Js('völlur'), Js('nes'), Js('sker'), Js('vogur'), Js('lavik'), Js('klaustur'), Js('reykir'), Js('rás'), Js('garás'), Js('vatn'), Js('sandur'), Js('verfi'), Js('firði'), Js('staður'), Js('lækur'), Js('höfn'), Js('hólar'), Js('holt'), Js('jahlíð'), Js('javík'), Js('heimar'), Js('vík'), Js('gerði'), Js('krókur'), Js('foss'), Js('narnes'), Js('strönd'), Js('seyri'), Js('hólmur'), Js('reyri'), Js('seyri'), Js('naeyjar')]))
var.put('nm9', Js([Js('Ai'), Js('Aiz'), Js('Ak'), Js('Akni'), Js('Alo'), Js('Alu'), Js('Aluk'), Js('Ba'), Js('Bal'), Js('Baus'), Js('Bro'), Js('Ce'), Js('Ces'), Js('Dag'), Js('Daugav'), Js('Do'), Js('Dur'), Js('Es'), Js('Gro'), Js('Gul'), Js('Ik'), Js('Iluk'), Js('Jaun'), Js('Jekab'), Js('Jel'), Js('Jur'), Js('Kan'), Js('Kar'), Js('Ke'), Js('Kras'), Js('Kul'), Js('Li'), Js('Lie'), Js('Liel'), Js('Ligat'), Js('Lim'), Js('Lu'), Js('Lud'), Js('Ma'), Js('Maz'), Js('Ol'), Js('Pavi'), Js('Pla'), Js('Prei'), Js('Prie'), Js('Rezek'), Js('Ri'), Js('Ru'), Js('Rujie'), Js('Sa'), Js('Sabi'), Js('Sal'), Js('Sala'), Js('Salac'), Js('Saul'), Js('Se'), Js('Si'), Js('Skrun'), Js('Smil'), Js('Stai'), Js('Sten'), Js('Stren'), Js('Su'), Js('Tal'), Js('Tu'), Js('Val'), Js('Valdemar'), Js('Van'), Js('Varak'), Js('Vents'), Js('Vi'), Js('Vie'), Js('Zi')]))
var.put('nm10', Js([Js('škile'), Js('baži'), Js('bana'), Js('bate'), Js('bazi'), Js('be'), Js('bele'), Js('bile'), Js('bina'), Js('ca'), Js('cele'), Js('ceni'), Js('cut'), Js('da'), Js('dava'), Js('dona'), Js('done'), Js('dus'), Js('gaži'), Js('ga'), Js('gava'), Js('gazilani'), Js('gda'), Js('griva'), Js('gulda'), Js('gums'), Js('ja'), Js('jiena'), Js('kile'), Js('kne'), Js('kraukle'), Js('ksne'), Js('kste'), Js('kule'), Js('kums'), Js('laca'), Js('laine'), Js('lava'), Js('li'), Js('loži'), Js('losta'), Js('lozi'), Js('lsi'), Js('lupe'), Js('lvi'), Js('mala'), Js('miera'), Js('naži'), Js('na'), Js('nas'), Js('nazi'), Js('nci'), Js('nda'), Js('nde'), Js('niste'), Js('paja'), Js('pils'), Js('pute'), Js('salaca'), Js('sava'), Js('sis'), Js('site'), Js('ska'), Js('skile'), Js('sne'), Js('sta'), Js('tene'), Js('tne'), Js('vaine'), Js('vani'), Js('vinas'), Js('za'), Js('zekne')]))
var.put('nm11', Js([Js('Šak'), Js('Šal'), Js('Šed'), Js('Šiaul'), Js('Šil'), Js('Šir'), Js('Šven'), Js('Žag'), Js('Žiež'), Js('Ak'), Js('Al'), Js('Anyk'), Js('Ario'), Js('Bal'), Js('Bir'), Js('Daug'), Js('Drus'), Js('Duk'), Js('Duset'), Js('Ežer'), Js('Eišis'), Js('Elek'), Js('Gar'), Js('Garg'), Js('Gel'), Js('Grig'), Js('Ignal'), Js('Jiez'), Js('Jon'), Js('Jur'), Js('Kaiš'), Js('Kal'), Js('Kaun'), Js('Kavar'), Js('Kaz'), Js('Kedain'), Js('Kel'), Js('Klai'), Js('Kret'), Js('Kudir'), Js('Kupiš'), Js('Kur'), Js('Kybar'), Js('Laz'), Js('Lent'), Js('Lin'), Js('Mažeik'), Js('Marij'), Js('Mol'), Js('Nauj'), Js('Ne'), Js('Nemen'), Js('Obel'), Js('Pab'), Js('Pag'), Js('Pak'), Js('Pal'), Js('Pan'), Js('Panem'), Js('Panev'), Js('Pas'), Js('Plun'), Js('Prie'), Js('Rad'), Js('Ramy'), Js('Rasein'), Js('Riet'), Js('Rokiš'), Js('Rudiš'), Js('Sal'), Js('Sed'), Js('Sim'), Js('Skaud'), Js('Skuod'), Js('Smal'), Js('Subac'), Js('Taur'), Js('Tel'), Js('Trak'), Js('Troš'), Js('Tytu'), Js('Už'), Js('Uk'), Js('Ut'), Js('Vabal'), Js('Var'), Js('Ven'), Js('Ver'), Js('Vie'), Js('Viek'), Js('Vies'), Js('Vil'), Js('Vir'), Js('Visa'), Js('Zara')]))
var.put('nm12', Js([Js('šciai'), Js('šenai'), Js('šiadorys'), Js('šiai'), Js('škelis'), Js('škes'), Js('škis'), Js('škunai'), Js('šniai'), Js('štas'), Js('štona'), Js('žai'), Js('ždai'), Js('žys'), Js('balis'), Js('barkas'), Js('brade'), Js('cine'), Js('cininkai'), Js('cioneliai'), Js('cionys'), Js('cius'), Js('da'), Js('das'), Js('delus'), Js('dijai'), Js('dorys'), Js('duva'), Js('gai'), Js('gala'), Js('gara'), Js('giai'), Js('ginas'), Js('jai'), Js('jis'), Js('joji'), Js('kai'), Js('kas'), Js('kiai'), Js('kija'), Js('kininkai'), Js('kis'), Js('kos'), Js('kruojis'), Js('kule'), Js('kuva'), Js('lale'), Js('lantai'), Js('liškis'), Js('liai'), Js('liava'), Js('lina'), Js('lis'), Js('lute'), Js('mariai'), Js('me'), Js('mene'), Js('merge'), Js('mune'), Js('na'), Js('nai'), Js('nas'), Js('neliai'), Js('nga'), Js('nge'), Js('niai'), Js('ninka'), Js('ninkai'), Js('ninkas'), Js('nius'), Js('nta'), Js('peda'), Js('pole'), Js('rage'), Js('relis'), Js('rena'), Js('rkas'), Js('rtai'), Js('sai'), Js('siejai'), Js('skas'), Js('skes'), Js('tai'), Js('tavas'), Js('tena'), Js('tinga'), Js('toji'), Js('tos'), Js('trenai'), Js('tus'), Js('va'), Js('valus'), Js('varija'), Js('varis'), Js('vas'), Js('vežys'), Js('venai'), Js('ventis'), Js('viškis'), Js('vile'), Js('viliškis'), Js('vintos'), Js('vis'), Js('zlu'), Js('znas')]))
var.put('nm13', Js([Js('Åkre'), Js('Åle'), Js('Åndal'), Js('Åsgård'), Js('Aren'), Js('As'), Js('Brønnøy'), Js('Bre'), Js('Brek'), Js('Brumund'), Js('Drø'), Js('Eger'), Js('El'), Js('Fager'), Js('Far'), Js('Finn'), Js('Flekke'), Js('Fos'), Js('Gjø'), Js('Grim'), Js('Høne'), Js('Hal'), Js('Hammer'), Js('Har'), Js('Hauge'), Js('Hokk'), Js('Holme'), Js('Holms'), Js('Honning'), Js('Hvit'), Js('Jørpe'), Js('Kirke'), Js('Kolve'), Js('Kongs'), Js('Koper'), Js('Lange'), Js('Lar'), Js('Leir'), Js('Lek'), Js('Lille'), Js('Lung'), Js('Man'), Js('Mol'), Js('Mos'), Js('Nam'), Js('Nar'), Js('Notod'), Js('Or'), Js('Os'), Js('Pors'), Js('Rju'), Js('Søg'), Js('Sand'), Js('Sande'), Js('Sarps'), Js('Seter'), Js('Skudenes'), Js('Sogn'), Js('Sort'), Js('Sta'), Js('Stat'), Js('Stein'), Js('Stjørdals'), Js('Tøns'), Js('Trom'), Js('Trond'), Js('Ulstein'), Js('Vad'), Js('Var'), Js('Vennes'), Js('Verdal')]))
var.put('nm14', Js([Js('bak'), Js('berg'), Js('bu'), Js('dal'), Js('den'), Js('fest'), Js('fjord'), Js('foss'), Js('grunn'), Js('halsen'), Js('hammer'), Js('hamn'), Js('heim'), Js('helle'), Js('jøen'), Js('kan'), Js('kanger'), Js('kenes'), Js('kim'), Js('kjer'), Js('land'), Js('nes'), Js('reid'), Js('ros'), Js('rum'), Js('søor'), Js('søra'), Js('sand'), Js('ske'), Js('sla'), Js('snes'), Js('sos'), Js('stad'), Js('strøm'), Js('strand'), Js('sund'), Js('våg'), Js('vanger'), Js('verg'), Js('vern'), Js('vik'), Js('vinger')]))
var.put('nm15', Js([Js('Ängel'), Js('Ål'), Js('Ö'), Js('Öre'), Js('Öst'), Js('Öster'), Js('Aling'), Js('Ar'), Js('Asker'), Js('Båt'), Js('Berg'), Js('Björn'), Js('Boll'), Js('Bor'), Js('Borg'), Js('Dag'), Js('Djurs'), Js('Ek'), Js('En'), Js('Eskil'), Js('Fager'), Js('Falken'), Js('Falster'), Js('Fin'), Js('Fol'), Js('Gamle'), Js('Gammal'), Js('Gothen'), Js('Grön'), Js('Gran'), Js('Härnö'), Js('Hässle'), Js('Höga'), Js('Hag'), Js('Halm'), Js('Hapar'), Js('Havs'), Js('Helsing'), Js('Hem'), Js('Hudiks'), Js('Husk'), Js('Jön'), Js('Karl'), Js('Karls'), Js('Kram'), Js('Kungs'), Js('Kväll'), Js('Lands'), Js('Lid'), Js('Lin'), Js('Lindes'), Js('Lud'), Js('Lyck'), Js('Lyse'), Js('Mar'), Js('Marie'), Js('Mjöl'), Js('Norr'), Js('Ny'), Js('Nynä'), Js('Oskar'), Js('Oxelö'), Js('Söder'), Js('Sölves'), Js('Sand'), Js('Sig'), Js('Simri'), Js('Skän'), Js('Ske'), Js('Skog'), Js('So'), Js('Stock'), Js('Ström'), Js('Sundby'), Js('Sunds'), Js('Tida'), Js('Tors'), Js('Träd'), Js('Udde'), Js('Ulrice'), Js('Upp'), Js('Väners'), Js('Väst'), Js('Väster'), Js('Vad'), Js('Vagn'), Js('Var'), Js('Vax'), Js('Vet'), Js('Vummer')]))
var.put('nm16', Js([Js('backa'), Js('berg'), Js('bo'), Js('borg'), Js('bro'), Js('burg'), Js('by'), Js('dal'), Js('fed'), Js('fors'), Js('gård'), Js('grund'), Js('hälla'), Js('härad'), Js('hättan'), Js('hall'), Js('hammar'), Js('hamn'), Js('holm'), Js('köping'), Js('kil'), Js('koga'), Js('krona'), Js('länge'), Js('land'), Js('landa'), Js('llefteå'), Js('näs'), Js('sås'), Js('sand'), Js('sele'), Js('shamn'), Js('sjö'), Js('stad'), Js('strand'), Js('stuna'), Js('sun'), Js('sund'), Js('tälje'), Js('torp'), Js('tuna'), Js('vall'), Js('valla'), Js('vik'), Js('viken')]))
pass
pass


# Add lib to the module scope
northEuropeTowns = var.to_python()
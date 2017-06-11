__all__ = ['asianTownsS']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'names15', 'names9', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names10', 'names13', 'names16', 'names14', 'names11', 'names3', 'names12', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(16.0)):
        try:
            if (var.get('i')<Js(2.0)):
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', (var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', (var.get('names3').get(var.get('rnd0'))+var.get('names4').get(var.get('rnd1'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                        var.put('names', (var.get('names5').get(var.get('rnd0'))+var.get('names6').get(var.get('rnd1'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                            var.put('names', (var.get('names7').get(var.get('rnd0'))+var.get('names8').get(var.get('rnd1'))))
                        else:
                            if (var.get('i')<Js(10.0)):
                                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names9').get('length'))))
                                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names10').get('length'))))
                                var.put('names', (var.get('names9').get(var.get('rnd0'))+var.get('names10').get(var.get('rnd1'))))
                            else:
                                if (var.get('i')<Js(12.0)):
                                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length'))))
                                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names12').get('length'))))
                                    var.put('names', (var.get('names11').get(var.get('rnd0'))+var.get('names12').get(var.get('rnd1'))))
                                else:
                                    if (var.get('i')<Js(14.0)):
                                        var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names13').get('length'))))
                                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names14').get('length'))))
                                        var.put('names', (var.get('names13').get(var.get('rnd0'))+var.get('names14').get(var.get('rnd1'))))
                                    else:
                                        var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names15').get('length'))))
                                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names16').get('length'))))
                                        var.put('names', (var.get('names15').get(var.get('rnd0'))+var.get('names16').get(var.get('rnd1'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Ab'), Js('Abed'), Js('Abre'), Js('Adi'), Js('Adram'), Js('Baba'), Js('Bad'), Js('Badur'), Js('Bago'), Js('Ba'), Js('Bal'), Js('Cah'), Js('Car'), Js('Cha'), Js('Chan'), Js('Dan'), Js('Danla'), Js('Da'), Js('Das'), Js('Do'), Js('Elya'), Js('Esh'), Js('Fa'), Js('Farma'), Js('Ganja'), Js('Gan'), Js('Gaw'), Js('Ghero'), Js('Ghu'), Js('Ha'), Js('Hey'), Js('Il'), Js('Jad'), Js('Jal'), Js('Jaw'), Js('Kah'), Js('Kal'), Js('Ka'), Js('Keli'), Js('Kora'), Js('Kulu'), Js('Lon'), Js('Ma'), Js('Mah'), Js('Muri'), Js('Nas'), Js('Naw'), Js('Nu'), Js('Om'), Js('Ota'), Js('Pala'), Js('Par'), Js('Quba'), Js('Qanda'), Js('Rakh'), Js('Rur'), Js('Sab'), Js('Sew'), Js('Shey'), Js('Takh')]))
var.put('names2', Js([Js('bahar'), Js('bar'), Js('botara'), Js('burgha'), Js('chaman'), Js('chaq'), Js('daha'), Js('dana'), Js('deh'), Js('dura'), Js('durzar'), Js('gan'), Js('gazi'), Js('ghez'), Js('ghisi'), Js('gorak'), Js('gozar'), Js('hari'), Js('jabad'), Js('jur'), Js('kata'), Js('khak'), Js('kharak'), Js('khel'), Js('khin'), Js('khlah'), Js('kul'), Js('kusta'), Js('laran'), Js('latabad'), Js('lur'), Js('mandan'), Js('mandi'), Js('mard'), Js('mazar'), Js('nadeh'), Js('najar'), Js('naqla'), Js('patan'), Js('qachi'), Js('qolak'), Js('qoli'), Js('rabad'), Js('ramzai'), Js('ran'), Js('rangi'), Js('raseh'), Js('ratan'), Js('rawan'), Js('rejan'), Js('rozar'), Js('ryd'), Js('sabad'), Js('sang'), Js('sarak'), Js('shan'), Js('suran'), Js('tabad'), Js('taken'), Js('tara')]))
var.put('names3', Js([Js('Ath'), Js('Ayu'), Js('Bat'), Js('Batta'), Js('Bhal'), Js('Bure'), Js('Cha'), Js('Chak'), Js('Chish'), Js('Dar'), Js('Dipal'), Js('Hafi'), Js('Jam'), Js('Kala'), Js('Kash'), Js('Kha'), Js('Khair'), Js('Khu'), Js('Khui'), Js('Khuz'), Js('Kula'), Js('Lar'), Js('Las'), Js('Latam'), Js('Man'), Js('Mas'), Js('Min'), Js('Miran'), Js('Mul'), Js('Nagar'), Js('Naro'), Js('Nush'), Js('Pas'), Js('Qaim'), Js('Qam'), Js('Raz'), Js('Risal'), Js('Sak'), Js('San'), Js('Shakar'), Js('Shar'), Js('Shikar'), Js('Si'), Js('Skar'), Js('Tang'), Js('Timer'), Js('Tur')]))
var.put('names4', Js([Js('bagh'), Js('bar'), Js('bat'), Js('bela'), Js('ber'), Js('bi'), Js('bia'), Js('chi'), Js('da'), Js('dar'), Js('dara'), Js('du'), Js('gai'), Js('gara'), Js('garh'), Js('ghar'), Js('gora'), Js('gram'), Js('kana'), Js('khela'), Js('ki'), Js('mak'), Js('man'), Js('more'), Js('muqam'), Js('ni'), Js('parkar'), Js('pur'), Js('ran'), Js('rand'), Js('ratta'), Js('rud'), Js('sehra'), Js('shab'), Js('shah'), Js('tan'), Js('tian'), Js('tung'), Js('wal'), Js('wala'), Js('wani'), Js('zabad')]))
var.put('names5', Js([Js('Ada'), Js('Ad'), Js('Ambe'), Js('Ba'), Js('Bal'), Js('Bar'), Js('Bhi'), Js('Byasa'), Js('Chat'), Js('Chhap'), Js('Chir'), Js('Dham'), Js('Dhu'), Js('Di'), Js('Dum'), Js('Farooq'), Js('Fateh'), Js('Fazil'), Js('Gad'), Js('Gopal'), Js('Gu'), Js('Guru'), Js('Han'), Js('Hazari'), Js('Haza'), Js('Jag'), Js('Jalan'), Js('Jan'), Js('Jhar'), Js('Kandu'), Js('Karim'), Js('Khaga'), Js('Kyatha'), Js('Lak'), Js('Lal'), Js('Ling'), Js('Luna'), Js('Madhe'), Js('Ma'), Js('Mahid'), Js('Malkan'), Js('Mangal'), Js('Musa'), Js('Nabaran'), Js('Nahar'), Js('Nar'), Js('Nela'), Js('?Nida'), Js('Pa'), Js('Periya'), Js('Piriya'), Js('Pukh'), Js('Rafi'), Js('Rajal'), Js('Raj'), Js('Revel'), Js('Rudra'), Js('Safi'), Js('Sag'), Js('Sher'), Js('Shish'), Js('Sila'), Js('Siva'), Js('Sundar'), Js('Tara'), Js('Tiru'), Js('Umar'), Js('Vanda'), Js('Vis'), Js('Wan')]))
var.put('names6', Js([Js('bag'), Js('bani'), Js('bri'), Js('desar'), Js('dhar'), Js('dhargat'), Js('doi'), Js('dukur'), Js('dwal'), Js('gadi'), Js('gam'), Js('ganj'), Js('gank'), Js('gaon'), Js('garh'), Js('garia'), Js('gat'), Js('ghati'), Js('giri'), Js('gudi'), Js('gundi'), Js('jogai'), Js('ka'), Js('kaner'), Js('khed'), Js('kheri'), Js('kulam'), Js('lagun'), Js('laj'), Js('langir'), Js('mangala'), Js('mia'), Js('miri'), Js('nagar'), Js('palle'), Js('pathar'), Js('pathur'), Js('patna'), Js('phu'), Js('pra'), Js('pur'), Js('pura'), Js('raon'), Js('rayan'), Js('ribag'), Js('si'), Js('sugur'), Js('tari'), Js('thampalle'), Js('tial'), Js('tra'), Js('vasi'), Js('vayoor'), Js('wada'), Js('wani'), Js('yar')]))
var.put('names7', Js([Js('Addalai'), Js('Amune'), Js('Arambe'), Js('Attara'), Js('Bakala'), Js('Bambara'), Js('Batti'), Js('Bo'), Js('Bodi'), Js('Buweli'), Js('Dambara'), Js('Dolos'), Js('Domati'), Js('Dunuke'), Js('Egoda'), Js('Elemal'), Js('Eta'), Js('Gan'), Js('Ge'), Js('Goda'), Js('Gunne'), Js('Hega'), Js('Hom'), Js('Hulu'), Js('Ilpe'), Js('Imbul'), Js('Ira'), Js('Jiwana'), Js('Kande'), Js('Karal'), Js('Khata'), Js('Lappa'), Js('Lini'), Js('Maliga'), Js('Mi'), Js('Miwa'), Js('Moraga'), Js('Na'), Js('Nika'), Js('Nuga'), Js('Ota'), Js('Owi'), Js('Paha'), Js('Pe'), Js('Pol'), Js('Puwak'), Js('Rada'), Js('Reki'), Js('Roti'), Js('Sela'), Js('Suriya'), Js('Taigaha'), Js('Tetta'), Js('Thikko'), Js('Thiray'), Js('Tora'), Js('Una'), Js('Uppo'), Js('Uru'), Js('Vadd'), Js('Vaka'), Js('Veera'), Js('Veppan'), Js('Ya'), Js('Yatima')]))
var.put('names8', Js([Js('bage'), Js('bawa'), Js('bepola'), Js('bura'), Js('caloa'), Js('chenai'), Js('dai'), Js('davan'), Js('diya'), Js('dura'), Js('gaginna'), Js('gaha'), Js('galla'), Js('gama'), Js('ganga'), Js('gatenna'), Js('ginna'), Js('goda'), Js('golla'), Js('hala'), Js('handa'), Js('hilla'), Js('kada'), Js('kamam'), Js('karai'), Js('kewatta'), Js('kodai'), Js('kotuwa'), Js('kuda'), Js('kumbura'), Js('landa'), Js('lawa'), Js('lena'), Js('likada'), Js('liyada'), Js('mada'), Js('madu'), Js('mulla'), Js('mure'), Js('nagama'), Js('pana'), Js('pitiya'), Js('pola'), Js('ragama'), Js('rai'), Js('rawa'), Js('ruppa'), Js('sa'), Js('sulla'), Js('tagaha'), Js('tale'), Js('tembe'), Js('tenna'), Js('tipe'), Js('tivu'), Js('tiya'), Js('tiyawa'), Js('tota'), Js('tura'), Js('wala'), Js('wana'), Js('watta'), Js('watura'), Js('wela'), Js('wella'), Js('wewa'), Js('yada'), Js('yawa')]))
var.put('names9', Js([Js('Amara'), Js('Bandi'), Js('Bane'), Js('Bhakta'), Js('Bir'), Js('Birat'), Js('Chain'), Js('Chau'), Js('Chit'), Js('Da'), Js('Dha'), Js('Gai'), Js('Gaida'), Js('Gho'), Js('Gor'), Js('Gula'), Js('Ina'), Js('Janak'), Js('Jit'), Js('Ka'), Js('Kama'), Js('Kapil'), Js('Khand'), Js('Kirti'), Js('Kohal'), Js('Lalit'), Js('Man'), Js('Mechi'), Js('Nara'), Js('Pa'), Js('Po'), Js('Pyu'), Js('Raja'), Js('Ram'), Js('Ratna'), Js('Sankhar'), Js('Sanphe'), Js('Taple'), Js('Tri'), Js('Urla')]))
var.put('names10', Js([Js('bagar'), Js('bari'), Js('dakot'), Js('gadhi'), Js('ganj'), Js('gar'), Js('gram'), Js('hari'), Js('jung'), Js('kha'), Js('khara'), Js('kot'), Js('lamai'), Js('mai'), Js('mak'), Js('nagar'), Js('nepa'), Js('pa'), Js('pur'), Js('rahi'), Js('ran'), Js('riya'), Js('ruwa'), Js('tara'), Js('tari'), Js('thali'), Js('than'), Js('vastu'), Js('wan'), Js('yan'), Js('yuga')]))
var.put('names11', Js([Js('Ak'), Js('Ba'), Js('Baghe'), Js('Ban'), Js('Bandar'), Js('Bar'), Js('Bari'), Js('Chand'), Js('Chau'), Js('Chaumu'), Js('Chitta'), Js('Co'), Js('Fe'), Js('Gai'), Js('Gopal'), Js('Jamal'), Js('Jhalo'), Js('Jhe'), Js('Jhenai'), Js('Kha'), Js('Khagra'), Js('Lak'), Js('Lakshmi'), Js('Lalmo'), Js('Lalmoni'), Js('Ma'), Js('Munshi'), Js('Na'), Js('Nao'), Js('Nar'), Js('Narsing'), Js('Netro'), Js('Pab'), Js('Patau'), Js('Raj'), Js('Ran'), Js('Sand'), Js('Shat'), Js('Sul'), Js('Tan'), Js('Tha'), Js('Thakur')]))
var.put('names12', Js([Js('ban'), Js('bandha'), Js('chhari'), Js('dah'), Js('di'), Js('gail'), Js('ganj'), Js('gaon'), Js('gong'), Js('guna'), Js('gunia'), Js('gura'), Js('hani'), Js('hat'), Js('haura'), Js('het'), Js('kati'), Js('khali'), Js('khira'), Js('kona'), Js('lokati'), Js('milla'), Js('mipur'), Js('muhani'), Js('na'), Js('naidah'), Js('ni'), Js('nirhat'), Js('pur'), Js('rail'), Js('sal'), Js('sam'), Js('shahi'), Js('singdi'), Js('wip')]))
var.put('names13', Js([Js('Dhidh'), Js('Eydha'), Js('Far'), Js('Farukol'), Js('Feli'), Js('Fevah'), Js('Funa'), Js('Hinna'), Js('Hitha'), Js('Hulhu'), Js('Kuda'), Js('Kudahu'), Js('Kulhu'), Js('Kulhudhuf'), Js('Ma'), Js('Magoo'), Js('Mana'), Js('Maro'), Js('Mi'), Js('Mu'), Js('Nai'), Js('Nolhi'), Js('Nolhiva'), Js('Nolhivaran'), Js('Thi'), Js('Thinda'), Js('Ungoo'), Js('Vey'), Js('Veyman'), Js('Vili'), Js('Villi'), Js('Villin')]))
var.put('names14', Js([Js('badhoo'), Js('dhoo'), Js('dhuffushi'), Js('du'), Js('faaru'), Js('faru'), Js('funadhoo'), Js('fushi'), Js('gili'), Js('goodhoo'), Js('huffushi'), Js('hufunadhoo'), Js('humale'), Js('huvadhoo'), Js('la'), Js('male'), Js('mandhoo'), Js('mandoo'), Js('meedhoo'), Js('mulah'), Js('n'), Js('nadhoo'), Js('navaru'), Js('ranfaru'), Js('roshi'), Js('ru'), Js('shi'), Js('vadhoo'), Js('varanfaru'), Js('varu')]))
var.put('names15', Js([Js('Ba'), Js('Bar'), Js('Cha'), Js('Che'), Js('Chung'), Js('Dam'), Js('Dip'), Js('Don'), Js('Ga'), Js('Gom'), Js('Gye'), Js('Ha'), Js('Hara'), Js('Hati'), Js('Ka'), Js('Kam'), Js('Kang'), Js('Ken'), Js('Ki'), Js('Kiso'), Js('Lame'), Js('Lhe'), Js('Lob'), Js('Mao'), Js('Mon'), Js('Nai'), Js('Nak'), Js('Ouna'), Js('Pa'), Js('Phi'), Js('Phisu'), Js('Pin'), Js('Pinso'), Js('Ri'), Js('Rung'), Js('Sak'), Js('Sam'), Js('Sar'), Js('Sha'), Js('Shin'), Js('Shing'), Js('Ta'), Js('Tari'), Js('Thim'), Js('Thun'), Js('Tosu'), Js('Tsha'), Js('Tshal'), Js('Tshalu'), Js('Ya')]))
var.put('names16', Js([Js('be'), Js('bling'), Js('cha'), Js('chap'), Js('cho'), Js('chu'), Js('dada'), Js('dang'), Js('ganka'), Js('gaon'), Js('gar'), Js('gha'), Js('hong'), Js('ka'), Js('kar'), Js('kha'), Js('laika'), Js('lang'), Js('lunang'), Js('maito'), Js('manu'), Js('nakha'), Js('nang'), Js('nig'), Js('pang'), Js('par'), Js('pe'), Js('pero'), Js('phu'), Js('ripe'), Js('sang'), Js('sar'), Js('shong'), Js('sila'), Js('sona'), Js('soperi'), Js('tang'), Js('teng'), Js('tola'), Js('tsa'), Js('tsang'), Js('tse'), Js('tu'), Js('zyung')]))
pass
pass


# Add lib to the module scope
asianTownsS = var.to_python()
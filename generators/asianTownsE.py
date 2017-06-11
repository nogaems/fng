__all__ = ['asianTownsE']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', (var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', (var.get('names3').get(var.get('rnd0'))+var.get('names4').get(var.get('rnd1'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                        var.put('names', (var.get('names5').get(var.get('rnd0'))+var.get('names6').get(var.get('rnd1'))))
                    else:
                        var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                        var.put('names', (var.get('names7').get(var.get('rnd0'))+var.get('names8').get(var.get('rnd1'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Arida'), Js('Asa'), Js('Bira'), Js('En'), Js('Fuji'), Js('Funa'), Js('Furu'), Js('Hashi'), Js('Haya'), Js('Hon'), Js('Horo'), Js('Iwa'), Js('Jami'), Js('Kamisu'), Js('Ken'), Js('Kiko'), Js('Kimo'), Js('Kiyo'), Js('Kuma'), Js('Kumi'), Js('Kuri'), Js('Kuro'), Js('Kuzu'), Js('Matsu'), Js('Mina'), Js('Miya'), Js('Mutsu'), Js('Naga'), Js('Naka'), Js('Nakashi'), Js('Nara'), Js('Oku'), Js('Ran'), Js('Shako'), Js('Shi'), Js('Shima'), Js('Shin'), Js('Shinto'), Js('Shira'), Js('Sou'), Js('Taka'), Js('Tate'), Js('Tawa'), Js('Tawara'), Js('Tou'), Js('Ura'), Js('Wata'), Js('Ya'), Js('Yaha'), Js('Yaku'), Js('Yama'), Js('Yoko'), Js('Yuga')]))
var.put('names2', Js([Js('betsu'), Js('biro'), Js('buchi'), Js('daka'), Js('furano'), Js('gata'), Js('gawa'), Js('haba'), Js('hama'), Js('hidaka'), Js('homa'), Js('horo'), Js('kami'), Js('kanai'), Js('kawa'), Js('kita'), Js('konai'), Js('koshi'), Js('kotan'), Js('kumo'), Js('maki'), Js('mamoto'), Js('matsunai'), Js('moto'), Js('nagawa'), Js('nai'), Js('nobe'), Js('nokawa'), Js('nouchi'), Js('raha'), Js('ramoto'), Js('rano'), Js('raoi'), Js('saki'), Js('sato'), Js('shibetsu'), Js('shihoro'), Js('shina'), Js('shiri'), Js('sunai'), Js('tama'), Js('tari'), Js('tori'), Js('toro'), Js('tsukawa'), Js('wara'), Js('yako'), Js('yama'), Js('zaki'), Js('zawa')]))
var.put('names3', Js([Js('Bao'), Js('Chang'), Js('Dan'), Js('Dong'), Js('Feng'), Js('Fu'), Js('Guang'), Js('Gui'), Js('Hang'), Js('Heng'), Js('Jiang'), Js('Jiao'), Js('Jin'), Js('Kara'), Js('Liao'), Js('Mei'), Js('Mian'), Js('Mudan'), Js('Nan'), Js('Pan'), Js('Ping'), Js('Qi'), Js('Qin'), Js('Qing'), Js('Qu'), Js('Quan'), Js('Shan'), Js('Shang'), Js('Shao'), Js('Shi'), Js('Shizui'), Js('Su'), Js('Tai'), Js('Tang'), Js('Teng'), Js('Tong'), Js('Xian'), Js('Xiang'), Js('Xin'), Js('Xu'), Js('Xuan'), Js('Yuan'), Js('Yue'), Js('Zhao'), Js('Zhen'), Js('Zhong'), Js('Zhou'), Js('Zoa')]))
var.put('names4', Js([Js('chang'), Js('cheng'), Js('chong'), Js('chun'), Js('dao'), Js('dong'), Js('ging'), Js('gong'), Js('guan'), Js('hai'), Js('har'), Js('hou'), Js('hua'), Js('jiang'), Js('jing'), Js('liang'), Js('may'), Js('men'), Js('ping'), Js('qihar'), Js('qiu'), Js('ramay'), Js('rao'), Js('shan'), Js('shu'), Js('shui'), Js('tong'), Js('tou'), Js('wei'), Js('xiang'), Js('xing'), Js('yang'), Js('ying'), Js('yuan'), Js('zhou'), Js('zihua'), Js('zou'), Js('zuishan')]))
var.put('names5', Js([Js('Altan'), Js('Ba'), Js('Baat'), Js('Baga'), Js('Baruun'), Js('Batt'), Js('Bayan'), Js('Bi'), Js('Bu'), Js('Bul'), Js('Bulan'), Js('Buut'), Js('Chand'), Js('Choi'), Js('Chu'), Js('Chuluun'), Js('Dar'), Js('Del'), Js('Dulaan'), Js('Er'), Js('Erdene'), Js('Ga'), Js('Gurvan'), Js('Guu'), Js('Han'), Js('Jan'), Js('Jar'), Js('Jav'), Js('Kha'), Js('Khair'), Js('Khar'), Js('Kher'), Js('Kherlen'), Js('Khon'), Js('Khot'), Js('Khu'), Js('Khyal'), Js('Khyar'), Js('Mal'), Js('Man'), Js('Na'), Js('Naran'), Js('Nogoon'), Js('Nom'), Js('On'), Js('Or'), Js('Sa'), Js('Sai'), Js('Sal'), Js('Shar'), Js('Sharyn'), Js('Shi'), Js('Shine'), Js('Tai'), Js('Taria'), Js('Tsen'), Js('Ulaan'), Js('Zuun')]))
var.put('names6', Js([Js('bayan'), Js('bulag'), Js('chivlin'), Js('dene'), Js('ga'), Js('gaa'), Js('gai'), Js('galan'), Js('galant'), Js('galjuut'), Js('gana'), Js('ganuur'), Js('gas'), Js('gat'), Js('ger'), Js('gol'), Js('gon'), Js('gor'), Js('horoot'), Js('jinst'), Js('kh'), Js('khaan'), Js('khan'), Js('khangai'), Js('khet'), Js('khir'), Js('khit'), Js('khlant'), Js('khon'), Js('khorin'), Js('lan'), Js('lig'), Js('lin'), Js('liun'), Js('luut'), Js('mandal'), Js('mani'), Js('nuur'), Js('raat'), Js('ran'), Js('ryngol'), Js('sagaan'), Js('sai'), Js('sengel'), Js('serleg'), Js('shaat'), Js('shir'), Js('sogt'), Js('tai'), Js('teeg'), Js('tont'), Js('tooroi'), Js('tsogt'), Js('turuun'), Js('vi'), Js('yant')]))
var.put('names7', Js([Js('An'), Js('Bor'), Js('Cheo'), Js('Chun'), Js('Chung'), Js('Cong'), Js('Dang'), Js('Dong'), Js('Gang'), Js('Gim'), Js('Gwa'), Js('Gwang'), Js('Gyeong'), Js('Gyer'), Js('Hae'), Js('Ham'), Js('Hoer'), Js('Hui'), Js('Hye'), Js('Ik'), Js('Je'), Js('Jeon'), Js('Jin'), Js('Kae'), Js('Kang'), Js('Kim'), Js('Ku'), Js('Man'), Js('Mung'), Js('Na'), Js('Nam'), Js('Non'), Js('Po'), Js('Pyong'), Js('Ra'), Js('Sam'), Js('Sari'), Js('Seo'), Js('Sin'), Js('Sinui'), Js('Sok'), Js('Sun'), Js('Tae'), Js('Tan'), Js('Tok'), Js('Ui'), Js('Won'), Js('Yang'), Js('Yeo')]))
var.put('names8', Js([Js('baek'), Js('chaek'), Js('cheok'), Js('cheon'), Js('cho'), Js('chon'), Js('dong'), Js('geup'), Js('gye'), Js('hae'), Js('hung'), Js('je'), Js('jin'), Js('ju'), Js('nan'), Js('neung'), Js('po'), Js('san'), Js('seong'), Js('song'), Js('su'), Js('wang'), Js('won'), Js('yeong'), Js('yong')]))
pass
pass


# Add lib to the module scope
asianTownsE = var.to_python()
__all__ = ['loatianNames']

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
    var.put('nm1', Js([Js('Akamu'), Js('Analu'), Js('Aulii'), Js('Bane'), Js('Bane '), Js('Havika'), Js('Ikaika'), Js('Kahoku'), Js('Kai'), Js('Kaili'), Js('Kaipo'), Js('Kalani'), Js('Kale'), Js('Kale '), Js('Kalei'), Js('Kanoa'), Js('Kapono'), Js('Kawaii'), Js('Keahi'), Js('Keanu'), Js('Kelii'), Js('Keoki'), Js('Keola'), Js('Keon'), Js('Keona'), Js('Keowynn'), Js('Kimo'), Js('Kimo '), Js('Koa'), Js('Konala'), Js('Kye'), Js('Kye '), Js('Lae'), Js('Lani'), Js('Leilani'), Js('Liko'), Js('Lilo'), Js('Loe'), Js('Maiele'), Js('Maik'), Js('Makaio'), Js('Makan'), Js('Makan '), Js('Makani'), Js('Malo'), Js('Malo '), Js('Mauli'), Js('Meka'), Js('Mele'), Js('Moana'), Js('Moke'), Js('Mya'), Js('Noi'), Js('Oke'), Js('Palani'), Js('Paxathipatai'), Js('Pekelo'), Js('Phetdum'), Js('Phonesavanh'), Js('Saravan'), Js('Sathanalat'), Js('Sengprachanh'), Js('Sommai'), Js('Somphone'), Js('Songkram'), Js('Sonxai'), Js('Teyvada'), Js('Ulani'), Js('Wongduan'), Js('Xaisomboun')]))
    var.put('nm2', Js([Js('Aelan'), Js('Ailani'), Js('Akela'), Js('Alaina'), Js('Alamea'), Js('Alana'), Js('Alani'), Js('Alanna'), Js('Alaula'), Js('Aleka'), Js('Alika'), Js('Alli'), Js('Allyn'), Js('Aloha'), Js('Alohi'), Js('Alohilani'), Js('Alona'), Js('Alun'), Js('Alyn'), Js('Anani'), Js('Ani'), Js('Aolani'), Js('Aolha'), Js('Aulani'), Js('Aulii'), Js('Bane'), Js('Bounmy'), Js('Chansouda'), Js('Chanthadeth'), Js('Dorit'), Js('Edena'), Js('Gladi'), Js('Haimi'), Js('Haleah'), Js('Haleigha'), Js('Halia'), Js('Hina'), Js('Inoke'), Js('Iokina'), Js('Iolana'), Js('Iolani'), Js('Ipo'), Js('Iwalani'), Js('Jeanitha'), Js('Kai'), Js('Kaiah'), Js('Kailani'), Js('Kailea'), Js('Kaili'), Js('Kalaina'), Js('Kalama'), Js('Kalani'), Js('Kalea'), Js('Kaleah'), Js('Kalei'), Js('Kaleigh'), Js('Kaleikaumaka'), Js('Kalena'), Js('Kalia'), Js('Kalina'), Js('Kaloni'), Js('Kamea'), Js('Kawailani'), Js('Kawena'), Js('Keahi'), Js('Keala'), Js('Keanu'), Js('Keiki'), Js('Keilana'), Js('Keili'), Js('Kekiokolanee'), Js('Kekona'), Js('Keola'), Js('Ketsada'), Js('Khampheng'), Js('Kiana'), Js('Kiele'), Js('Kieli'), Js('Kina'), Js('Kinipela'), Js('Konane'), Js('Lae'), Js('Lahela'), Js('Laina'), Js('Lanai'), Js('Lani'), Js('Lanikai'), Js('Laya'), Js('Leigha'), Js('Leilana'), Js('Leilana '), Js('Leilani'), Js('Leilanie'), Js('Liliha'), Js('Lilo'), Js('Loe'), Js('Lokelani'), Js('Lulani'), Js('Mahina'), Js('Maik'), Js('Maile'), Js('Makaio'), Js('Makala'), Js('Makana'), Js('Makani'), Js('Makelina'), Js('Makenna'), Js('Malana'), Js('Maleah'), Js('Malia'), Js('Malu'), Js('Mauli'), Js('Mei'), Js('Milani'), Js('Mily'), Js('Moana'), Js('Moanna'), Js('Moke'), Js('Mya'), Js('Nalani'), Js('Nalanie'), Js('Nani'), Js('Napua'), Js('Noelani'), Js('Noma'), Js('Okalani'), Js('Oke'), Js('Okelani'), Js('Okilani'), Js('Oliana'), Js('Olina'), Js('Onaona'), Js('Palila'), Js('Peni'), Js('Phetmany'), Js('Phetsavanh'), Js('Pilialoha'), Js('Pilis'), Js('Pualani'), Js('Roselani'), Js('Saengvone'), Js('Sasilvia'), Js('Sathit'), Js('Somphone'), Js('Soukchanda'), Js('Sousida'), Js('Suke'), Js('Ulani'), Js('Ululani'), Js('Wanika')]))
    var.put('nm3', Js([Js('Bokeo'), Js('Bouphavanh'), Js('Bouvanaat'), Js('Champasack'), Js('Champasak'), Js('Chanthanane'), Js('Chanthavong\t '), Js('Chanthavong'), Js('Chanthraphone'), Js('Cheruene'), Js('Douangmala'), Js('Douangvily'), Js('Genevong'), Js('Inthisane'), Js('Kaewdara'), Js('Keobounphanh'), Js('Keobunta'), Js('Keomany'), Js('Keopraseuth'), Js('Keothavong'), Js('Kethavongsa'), Js('Ketthavong'), Js('Khamchanh'), Js('Khamsomphou'), Js('Khamvongsouk'), Js('Khanthavong'), Js('Khotpanya'), Js('Khouphongsy'), Js('Kittiphan'), Js('Kommandam'), Js('Kouanchao'), Js('Lengsavad'), Js('Louangrath\t '), Js('Malaythong'), Js('Manwilaivong'), Js('Menorath'), Js('Ornpaeng'), Js('Oudomphonh'), Js('Pakdimounivong'), Js('Phanivong'), Js('Phankham'), Js('Phaophanit'), Js('Phengsavath'), Js('Phetphommasouk'), Js('Phommajack'), Js('Phommasane'), Js('Phommathep'), Js('Phomsouvanh'), Js('Phomvihane'), Js('Phothisarath'), Js('Phoumsavanh'), Js('Phoutthasinh'), Js('Phrasavath'), Js('Rattanavongsa'), Js('Saenbouthalath'), Js('Saengsavang'), Js('Saengsouriya'), Js('Saenthavisouk'), Js('Savang'), Js('Sayasone'), Js('Sayavong'), Js('Saysamongdy'), Js('Saysanasy'), Js('Seeha'), Js('Sengprachanh'), Js('Sengtavisouk'), Js('Siharath '), Js('Simnouansai'), Js('Siphandon'), Js('Sisoulith'), Js('Siyavong'), Js('Somphonpadee'), Js('Somphousiharath'), Js('Sonexarth'), Js('Souksanh'), Js('Soulignavong'), Js('Southavilay'), Js('Souvannaphouma'), Js('Syrypanha'), Js('Syvongsa'), Js('Tayvihane'), Js('Thammasith'), Js('Thammavong'), Js('Thammavong '), Js('Thammavongsa'), Js('Thepsenavong'), Js('Thiamphasone'), Js('Thonemany'), Js('Vatthana'), Js('Viravongs'), Js('Vongphachanh'), Js('Vongphakdy'), Js('Vongsamphanh'), Js('Vongsay'), Js('Vongvichit'), Js('Vongvilay'), Js('Vorachith'), Js('Xiengboree')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
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
loatianNames = var.to_python()
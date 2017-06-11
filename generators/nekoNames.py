__all__ = ['nekoNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            if (var.get('rnd7')<Js(35.0)):
                var.put('rnd8', Js(0.0))
            else:
                while PyJsStrictEq(var.get('rnd8'),Js(0.0)):
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', var.get('nm2').get(var.get('rnd')))
                else:
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((((var.get('nm4').get(var.get('rnd4'))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+var.get('nm5').get(var.get('rnd9')))+var.get('nm10').get(var.get('rnd10'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    if (var.get('i')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', var.get('nm3').get(var.get('rnd')))
                    else:
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('names', ((((((var.get('nm4').get(var.get('rnd4'))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+var.get('nm5').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10'))))
                else:
                    if (var.get('i')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('names', var.get('nm1').get(var.get('rnd')))
                    else:
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', ((((((var.get('nm4').get(var.get('rnd4'))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+var.get('nm5').get(var.get('rnd9')))+var.get('nm9').get(var.get('rnd10'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aiko'), Js('Aki'), Js('Akihiko'), Js('Akihiro'), Js('Akiko'), Js('Akina'), Js('Akira'), Js('Anda'), Js('Aneko'), Js('Aoi'), Js('Ayame'), Js('Bento'), Js('Chika'), Js('Chiko'), Js('Chiyo'), Js('Cho'), Js('Dai'), Js('Daiki'), Js('Daisuke'), Js('Domo'), Js('Eriko'), Js('Gin'), Js('Haiku'), Js('Hana'), Js('Haru'), Js('Haruki'), Js('Haruko'), Js('Hideki'), Js('Hideo'), Js('Hikaru'), Js('Hiro'), Js('Hiroki'), Js('Hiroshi'), Js('Hisa'), Js('Hisashi'), Js('Hisoka'), Js('Honcho'), Js('Hoshi'), Js('Hoshiko'), Js('Ichiro'), Js('Isamu'), Js('Isao'), Js('Jiro'), Js('Judo'), Js('Jun'), Js('Juro'), Js('Kabuki'), Js('Kaede'), Js('Kameko'), Js('Katsumi'), Js('Katsuo'), Js('Katsuro'), Js('Keiji'), Js('Keiko'), Js('Ken'), Js('Kenji'), Js('Kin'), Js('Kioko'), Js('Kioshi'), Js('Ko'), Js('Kobe'), Js('Kohaku'), Js('Koji'), Js('Koto'), Js('Kou'), Js('Kumiko'), Js('Kuro'), Js('Kyo'), Js('Kyoko'), Js('Leiko'), Js('Madoka'), Js('Maeko'), Js('Makoto'), Js('Masa'), Js('Masaaki'), Js('Masaki'), Js('Masi'), Js('Masumi'), Js('Masuru'), Js('Matsui'), Js('Michiko'), Js('Michio'), Js('Minoru'), Js('Mitsuo'), Js('Mitsuru'), Js('Nami'), Js('Nao'), Js('Naoki'), Js('Nariko'), Js('Natsuko'), Js('Nikki'), Js('Nobu'), Js('Nori'), Js('Noriko'), Js('Norio'), Js('Nyoko'), Js('Oki'), Js('Orino'), Js('Ran'), Js('Rei'), Js('Ryu'), Js('Sachi'), Js('Sachiko'), Js('Sake'), Js('Sakura'), Js('Satu'), Js('Shig'), Js('Shika'), Js('Shin'), Js('Shina'), Js('Shino'), Js('Shiro'), Js('Sho'), Js('Suki'), Js('Sumi'), Js('Sumo'), Js('Suzu'), Js('Taiki'), Js('Taiko'), Js('Taji'), Js('Taka'), Js('Takara'), Js('Tamae'), Js('Toshi'), Js('Yoshi'), Js('Yukio')]))
var.put('nm2', Js([Js('Aiko'), Js('Aimi'), Js('Aio'), Js('Akane'), Js('Aki'), Js('Akina'), Js('Akira'), Js('Amaya'), Js('Ame'), Js('Aoi'), Js('Aozora'), Js('Asa'), Js('Asami'), Js('Aya'), Js('Ayaka'), Js('Chi'), Js('Chie'), Js('Chika'), Js('Chikako'), Js('Chiyo'), Js('Cho'), Js('Choji'), Js('Dai'), Js('Eiko'), Js('Emi'), Js('Emiko'), Js('Eri'), Js('Fujiko'), Js('Fuyu'), Js('Ginkgo'), Js('Haiku'), Js('Hana'), Js('Hanako'), Js('Haru'), Js('Haruki'), Js('Haruko'), Js('Hideko'), Js('Hikari'), Js('Hikaru'), Js('Hiro'), Js('Hiromi'), Js('Hisanori'), Js('Hisoka'), Js('Hitomi'), Js('Hoshi'), Js('Hoshinka'), Js('Hotaru'), Js('Junko'), Js('Kabuki'), Js('Kaede'), Js('Kameko'), Js('Kaori'), Js('Kasumi'), Js('Katsu'), Js('Kazumi'), Js('Kei'), Js('Keiko'), Js('Kimi'), Js('Kimiko'), Js('Kioko'), Js('Kiyoshi'), Js('Ko'), Js('Kohaku'), Js('Kohana'), Js('Koko'), Js('Kou'), Js('Kuro'), Js('Kyo'), Js('Kyoko'), Js('Leiko'), Js('Madoka'), Js('Mai'), Js('Maiya'), Js('Masa'), Js('Masako'), Js('Masami'), Js('Masumi'), Js('Mi'), Js('Michi'), Js('Michiko'), Js('Midori'), Js('Mika'), Js('Miki'), Js('Miku'), Js('Misuki'), Js('Mitsuru'), Js('Miyoshi'), Js('Miyuki'), Js('Moe'), Js('Momo'), Js('Momoe'), Js('Moriko'), Js('Name'), Js('Nami'), Js('Naoki'), Js('Naoko'), Js('Naomi'), Js('Nari'), Js('Nariko'), Js('Natsu'), Js('Natsumi'), Js('Neka'), Js('Nobu'), Js('Nori'), Js('Noriko'), Js('Oki'), Js('Rei'), Js('Reiko'), Js('Riko'), Js('Rin'), Js('Ryoko'), Js('Saki'), Js('Sakura'), Js('Sayomi'), Js('Sayuri'), Js('Shig'), Js('Shinju'), Js('Shiori'), Js('Shizumi'), Js('Shoji'), Js('Sora'), Js('Suki'), Js('Sumiko'), Js('Susumu'), Js('Suzaku'), Js('Suzu'), Js('Tamika'), Js('Tanaka'), Js('Tokiwa'), Js('Tora'), Js('Toshiko'), Js('Tsuki'), Js('Tsukiko'), Js('Umeko'), Js('Usagi'), Js('Yoi'), Js('Yoki'), Js('Yoko'), Js('Yori'), Js('Yoshie'), Js('Yuki'), Js('Yukiko'), Js('Yumi'), Js('Yumiko'), Js('Yuri'), Js('Yuuki'), Js('Zakuro')]))
var.put('nm3', Js([Js('Aiko'), Js('Aki'), Js('Akira'), Js('Aoi'), Js('Asa'), Js('Ayame'), Js('Chi'), Js('Chie'), Js('Chikako'), Js('Dai'), Js('Daiki'), Js('Domo'), Js('Eiko'), Js('Eri'), Js('Fuyu'), Js('Haiku'), Js('Haru'), Js('Haruki'), Js('Haruko'), Js('Hikari'), Js('Hikaru'), Js('Hiro'), Js('Hiroki'), Js('Hisoka'), Js('Honcho'), Js('Hoshi'), Js('Hotaru'), Js('Isamu'), Js('Jun'), Js('Junko'), Js('Kabuki'), Js('Kaede'), Js('Kameko'), Js('Katsu'), Js('Katsumi'), Js('Kei'), Js('Keiko'), Js('Ken'), Js('Kin'), Js('Kio'), Js('Kioko'), Js('Kioshi'), Js('Ko'), Js('Kohaku'), Js('Kohana'), Js('Koko'), Js('Kou'), Js('Kyo'), Js('Kyoko'), Js('Leiko'), Js('Madoka'), Js('Maeko'), Js('Mai'), Js('Makoto'), Js('Masa'), Js('Masaaki'), Js('Masako'), Js('Masumi'), Js('Masuru'), Js('Matsui'), Js('Michi'), Js('Mika'), Js('Minoru'), Js('Mitsuru'), Js('Miyoshi'), Js('Momo'), Js('Nami'), Js('Nao'), Js('Naoki'), Js('Naoko'), Js('Nari'), Js('Nariko'), Js('Natsu'), Js('Nobu'), Js('Nori'), Js('Oki'), Js('Rei'), Js('Reiko'), Js('Rin'), Js('Ryoko'), Js('Saki'), Js('Shig'), Js('Shin'), Js('Sho'), Js('Sora'), Js('Suzaku'), Js('Taiki'), Js('Tanaka'), Js('Tora'), Js('Toshi'), Js('Usagi'), Js('Yoi'), Js('Yoko'), Js('Yori'), Js('Yoshi'), Js('Yuki'), Js('Yukiko'), Js('Yukio'), Js('Yumi'), Js('Yumiko')]))
var.put('nm4', Js([Js('ch'), Js('c'), Js('f'), Js('g'), Js('h'), Js('k'), Js('m'), Js('n'), Js('pr'), Js('r'), Js('s'), Js('sh'), Js('th'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ia'), Js('au'), Js('iau'), Js('aa'), Js('ee'), Js('ie'), Js('y'), Js('y')]))
var.put('nm6', Js([Js('ch'), Js('c'), Js('f'), Js('fr'), Js('cr'), Js('k'), Js('ks'), Js('cs'), Js('kr'), Js('m'), Js('mm'), Js('mn'), Js('ms'), Js('mz'), Js('kz'), Js('n'), Js('nm'), Js('ns'), Js('nz'), Js('nx'), Js('nch'), Js('mch'), Js('pr'), Js('gr'), Js('s'), Js('ss'), Js('sh'), Js('sz'), Js('shr'), Js('sr'), Js('th'), Js('tr'), Js('t'), Js('x'), Js('z'), Js('zz'), Js('zs'), Js('zr'), Js('c'), Js('f'), Js('k'), Js('m'), Js('n'), Js('s'), Js('t'), Js('x'), Js('z'), Js('c'), Js('f'), Js('k'), Js('m'), Js('n'), Js('s'), Js('t'), Js('x'), Js('z')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ia'), Js('au'), Js('iau'), Js('aa'), Js('ee'), Js('ie'), Js('y'), Js('y')]))
var.put('nm8', Js([Js(''), Js('ch'), Js('c'), Js('f'), Js('fr'), Js('cr'), Js('k'), Js('ks'), Js('cs'), Js('kr'), Js('m'), Js('mm'), Js('mn'), Js('ms'), Js('mz'), Js('kz'), Js('n'), Js('nm'), Js('ns'), Js('nz'), Js('nx'), Js('nch'), Js('mch'), Js('pr'), Js('gr'), Js('s'), Js('ss'), Js('sh'), Js('sz'), Js('shr'), Js('sr'), Js('th'), Js('tr'), Js('t'), Js('x'), Js('z'), Js('zz'), Js('zs'), Js('zr'), Js('c'), Js('f'), Js('k'), Js('m'), Js('n'), Js('s'), Js('t'), Js('x'), Js('z'), Js('c'), Js('f'), Js('k'), Js('m'), Js('n'), Js('s'), Js('t'), Js('x'), Js('z')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('x'), Js('z')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('th'), Js('h'), Js('s'), Js('ss'), Js('sh')]))
var.put('nm11', Js([Js('s'), Js('ss'), Js('sh'), Js('z'), Js('h'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
nekoNames = var.to_python()
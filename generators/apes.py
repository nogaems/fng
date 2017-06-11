__all__ = ['apes']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Akamaru'), Js('Alfalfa'), Js('Alien'), Js('Alphonso'), Js('Alvin'), Js('Aokuro'), Js('Aono'), Js('Avalanche'), Js('BananaHammock'), Js('BananaPunch'), Js('Bananas'), Js('Bananerz'), Js('Banjo'), Js('Bannanas'), Js('Banzai'), Js('Barnaby'), Js('Belvedere'), Js('Beppo'), Js('BigPete'), Js('BigSteve'), Js('Bleach'), Js('Bobo'), Js('Bones'), Js('Bonkbek'), Js('Bonkers'), Js('Bonzo'), Js('Boots'), Js('Brass'), Js('BrassMonkey'), Js('Bubbles'), Js('Business'), Js('Butters'), Js('Cedric'), Js('Chappal'), Js('Chawworra'), Js('Cheruurrik'), Js('Chimes'), Js('Chimp'), Js('ChimpCharlie'), Js('Chipmunkey'), Js('Chubaka'), Js('Chuckapoo'), Js('ChunkyMonkey'), Js('ChunkyMunkey'), Js('Claw'), Js('Clide'), Js('Clyde'), Js('Cooter'), Js('Corky'), Js('Cornelious'), Js('Cornelius'), Js('Cosmo'), Js('Couch'), Js('Darwin'), Js('Dejen'), Js('Dookie'), Js('Duffy'), Js('Eggo'), Js('Elgon'), Js('Elmer'), Js('FecalFlinger'), Js('Fidget'), Js('Fido'), Js('FirstMate'), Js('Fivel'), Js('Fleabag'), Js('Fred'), Js('Fredrick'), Js('Frowrakich'), Js('Fujioka'), Js('Funky'), Js('FunkyMonkey'), Js('FuriousJorge'), Js('Gaspode'), Js('George'), Js('Gerbil'), Js('Gigantor'), Js('Giggles'), Js('Gilley'), Js('Gilligan'), Js('Ginhon'), Js('Gordon'), Js('Gorilladin'), Js('Grapeape'), Js('Grawahrr'), Js('Grease'), Js('Grillya'), Js('Grums'), Js('Guantichosd'), Js('Hanatoyo'), Js('Harahon'), Js('HearNoEvil'), Js('Herashorr'), Js('Ichimura'), Js('Iflingpoo'), Js('Igawa'), Js('Igby'), Js('Infernape'), Js('Iwaharu'), Js('Iwato'), Js('Jaccuka'), Js('Jade'), Js('JarJar'), Js('Jello'), Js('Jim'), Js('Jimmy'), Js('Jingles'), Js('JoJo'), Js('Juice'), Js('Jumana'), Js('Justin'), Js('Kachrarc'), Js('Kahlua'), Js('Kamiyama'), Js('Kar'), Js('Katie'), Js('Kawakita'), Js('Kenhira'), Js('Kep'), Js('KingKong'), Js('Kinue'), Js('Kitaka'), Js('Klepto'), Js('Knuckles'), Js('Koko'), Js('Kong'), Js('KungFuPoo'), Js('Linus'), Js('Lochanhakk'), Js('Lockjaw'), Js('Lokaap'), Js('Lucas'), Js('Lugnut'), Js('Lunatic'), Js('Magilla'), Js('Mankey'), Js('Marley'), Js('Maruikei'), Js('Matsumura'), Js('Matsuoo'), Js('Moco'), Js('Mojo'), Js('MojoJojo'), Js('Momo'), Js('Monkey'), Js('MonkeyBone'), Js('MonkeysUncle'), Js('Montgomery'), Js('Moptop'), Js('Morida'), Js('Morikami'), Js('Morikawa'), Js('Morishima'), Js('Moroto'), Js('Morruuna'), Js('Motewnawr'), Js('MrNilsson'), Js('Mugsy'), Js('Munky'), Js('Murdock'), Js('Murny'), Js('Nabe'), Js('Noelle'), Js('Noharu'), Js('Noken'), Js('Nokin'), Js('Nostradamus'), Js('NutJob'), Js('Nyrka'), Js('Ohoh'), Js('Omori'), Js('Onu'), Js('Ooga'), Js('OptimusPrimal'), Js('Pancakes'), Js('Pansy'), Js('Peaches'), Js('Pewner'), Js('Pickles'), Js('Pimple'), Js('PooFlinger'), Js('Pootapult'), Js('Popeye'), Js('Poppa'), Js('Predator'), Js('Primeape'), Js('Rafiki'), Js('Reyrrrwacca'), Js('Roobarb'), Js('Ruxpin'), Js('Sakakei'), Js('Sakamori'), Js('Sakanaka'), Js('Sakiko'), Js('Sakizaki'), Js('Sarah'), Js('Sawa'), Js('Sebastian'), Js('SeeNoEvil'), Js('Seymour'), Js('Sinclair'), Js('Situation'), Js('Slingshot'), Js('Spank'), Js('Spanks'), Js('SpeakNoEvil'), Js('Suzu'), Js('Suzukin'), Js('Takakei'), Js('Takazawa'), Js('Tater'), Js('Tbone'), Js('TheSituation'), Js('Thunder'), Js('Thunderstomp'), Js('Tim'), Js('Timmy'), Js('Tiny'), Js('TinyTim'), Js('Tipster'), Js('Tizzy'), Js('Tooter'), Js('Tremor'), Js('Truffles'), Js('Truk'), Js('TrunkMonkey'), Js('Tulip'), Js('Turdis'), Js('Tygarr'), Js('Tyrock'), Js('Ueshima'), Js('Utcharrakk'), Js('Waffles'), Js('Wilbur'), Js('Wingnut'), Js('Worrawrowr'), Js('Yama'), Js('Yamakami'), Js('Zach'), Js('Zawabashi'), Js('Zawaoo'), Js('Zimba'), Js('Zippy'), Js('iFlingPoo'), Js('iPoo')]))
pass
pass


# Add lib to the module scope
apes = var.to_python()
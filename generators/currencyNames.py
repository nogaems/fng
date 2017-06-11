__all__ = ['currencyNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                if (var.get('i')<Js(2.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm6').get(var.get('rnd6'))+Js(' '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', var.get('nm7').get(var.get('rnd')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', ((var.get('nm8').get(var.get('rnd'))+Js(' '))+var.get('nm9').get(var.get('rnd2'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('names', ((var.get('nm8').get(var.get('rnd'))+Js(' '))+var.get('nm10').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('boa'), Js('c'), Js('cha'), Js('ching'), Js('de'), Js('der'), Js('ding'), Js('do'), Js('doba'), Js('fa'), Js('geni'), Js('ham'), Js('k'), Js('kel'), Js('la'), Js('lar'), Js('le'), Js('ling'), Js('moni'), Js('na'), Js('nar'), Js('nat'), Js('ne'), Js('nea'), Js('ni'), Js('nia'), Js('ning'), Js('pee'), Js('pi'), Js('pia'), Js('pira'), Js('ra'), Js('ram'), Js('rani'), Js('ri'), Js('rin'), Js('rint'), Js('ro'), Js('runa'), Js('sar'), Js('si'), Js('so'), Js('taca'), Js('tas'), Js('tos'), Js('ty'), Js('ya'), Js('za'), Js('zal')]))
var.put('nm6', Js([Js('Alliance'), Js('Allied'), Js('Amber'), Js('Ancestral'), Js('Black'), Js('Blood'), Js('Bloodbound'), Js('Blue'), Js('Bronze'), Js('Castle'), Js('Celestial'), Js('Chrono'), Js('Coalition'), Js('Commonwealth'), Js('Confederate'), Js('Constellation'), Js('Copper'), Js('Crescent'), Js('Crimson'), Js('Crown'), Js('Crystal'), Js('Diamond'), Js('Division'), Js('Dominion'), Js('Dwarven'), Js('Earth'), Js('Earthian'), Js('Electric'), Js('Elemental'), Js('Elvish'), Js('Emerald'), Js('Emperor'), Js('Empire'), Js('Ethereal'), Js('Federal'), Js('Free World'), Js('Freedom'), Js('Galactic'), Js('Ghost'), Js('Glory'), Js('Gnomish'), Js('Gold'), Js('Golden'), Js('Gothic'), Js('Honor'), Js('Intergalactic'), Js('Interstellar'), Js('Jade'), Js("King's"), Js('Lunar'), Js('Mystic'), Js('New'), Js('New Earth'), Js('New Order'), Js('Obsidian'), Js('Orcish'), Js('Phantom'), Js('Phoenix'), Js('Platinum'), Js('Presidential'), Js('Raven'), Js('Republic'), Js('Royal'), Js('Sanguine'), Js('Serpent'), Js('Silver'), Js('Solar'), Js('Sovereign'), Js('Space'), Js('Spectral'), Js('Supremacy'), Js('Syndicate'), Js('Tin'), Js('Trade Federation'), Js("Trader's"), Js('Tribe'), Js('Union'), Js('Utopian'), Js('Virtual'), Js('White'), Js("World League's"), Js('World Union')]))
var.put('nm7', Js([Js('Air Coins'), Js('Air Dollars'), Js('Behavior Credits'), Js('Belt Buckles'), Js('Bits'), Js('Black Gold'), Js('Black Pennies'), Js('Blings'), Js('Blossoms'), Js('Blue Orbs'), Js('Bolts'), Js('Bottle Caps'), Js('Buckles'), Js('Bullets'), Js('Chips'), Js('Chronocoins'), Js('Chronocredits'), Js('Chronodollars'), Js('Chronos'), Js('Chronus'), Js('Claws'), Js('Coins'), Js('Constellation Coins'), Js('Constellation Gold'), Js('Constellatoin Credits'), Js('Copper'), Js('Credits'), Js('Creds'), Js('Crescents'), Js('Crowns'), Js('Crystals'), Js('Cubes'), Js('Cuts'), Js('Diamonds'), Js('Dominions'), Js('Eagle Eyes'), Js('Earth Coins'), Js('Earthians'), Js('Emeralds'), Js('Empire Gold'), Js('Eyes'), Js('Feathers'), Js('Federal Credits'), Js('Federal Gold'), Js('Free World Coins'), Js('Free World Credits'), Js('Freedom Credits'), Js('Galactic Coins'), Js('Galactic Credit'), Js('Galactic Gold'), Js('Gems'), Js('Gold'), Js('Gold Coins'), Js('Gold Crowns'), Js('Gold Pieces'), Js('Golden Pennies'), Js('Grains'), Js('Influence Points'), Js('Intergalactic Coins'), Js('Intergalactic Gold'), Js('Interstellar Credits'), Js('Interstellar Gold'), Js('Jewels'), Js('Marks'), Js('Nectar'), Js('New Coins'), Js('New Dollars'), Js('New Earth Coins'), Js('New Earth Credit'), Js('New Earths'), Js('New Order Credit'), Js('Novas'), Js('Orbs'), Js('Pebbles'), Js('Pennies'), Js('Petals'), Js('Platinum'), Js('Quills'), Js('Raven Claws'), Js('Republic Dollars'), Js('Rubies'), Js('Seeds'), Js('Shells'), Js('Shinies'), Js('Silver'), Js('Silver Eyes'), Js('Silver Pieces'), Js('Solars'), Js('Souls'), Js('Space Bucks'), Js('Space Dollars'), Js('Space Gold'), Js('Sparkles'), Js('Talons'), Js('Teeth'), Js('Tokens'), Js('Utopis'), Js('White Gold'), Js('White Orbs'), Js('Widgets')]))
var.put('nm8', Js([Js('Alliance'), Js('Allied'), Js('Ancestral'), Js('Astral'), Js('Black'), Js('Blood'), Js('Bloodbound'), Js('Blue'), Js('Castle'), Js('Celestial'), Js('Chrono'), Js('Coalition'), Js('Commonwealth'), Js('Confederate'), Js('Constellation'), Js('Crescent'), Js('Crimson'), Js('Crown'), Js('Division'), Js('Dominion'), Js('Dragon'), Js('Dwarven'), Js('Earth'), Js('Earthian'), Js('Electric'), Js('Elemental'), Js('Elvish'), Js('Emperor'), Js('Empire'), Js('Ethereal'), Js('Federal'), Js('Forest'), Js('Free World'), Js('Freedom'), Js('Galactic'), Js('Ghost'), Js('Glory'), Js('Gnomish'), Js('Gothic'), Js('Honor'), Js('Intergalactic'), Js('Interstellar'), Js("King's"), Js('Lion'), Js('Lionheart'), Js('Lunar'), Js('Mountain'), Js('Mystic'), Js('New'), Js('New Earth'), Js('New Order'), Js('Nova'), Js('Obsidian'), Js('Ocean'), Js('Orcish'), Js('Phantom'), Js('Phoenix'), Js('Presidential'), Js('Raven'), Js('Republic'), Js('River'), Js('Royal'), Js('Sanguine'), Js('Sea'), Js('Seafarer'), Js('Serpent'), Js('Solar'), Js('Sovereign'), Js('Space'), Js('Spectral'), Js('Supremacy'), Js('Syndicate'), Js('Trade Federation'), Js("Trader's"), Js('Tribe'), Js('Union'), Js('Utopian'), Js('Virtual'), Js('Volcanic'), Js('White'), Js("World League's"), Js('World Union')]))
var.put('nm9', Js([Js('Cash'), Js('Chips'), Js('Coins'), Js('Coins'), Js('Copper'), Js('Copper'), Js('Credits'), Js('Credits'), Js('Dime'), Js('Dime'), Js('Dollars'), Js('Doubloons'), Js('Gold'), Js('Gold'), Js('Pennies'), Js('Pieces'), Js('Silver'), Js('Silver'), Js('Tender'), Js('Tokens')]))
var.put('nm10', Js([Js('Abazi'), Js('Apsar'), Js('Aureus'), Js('Austral'), Js('Balboa'), Js('Birr'), Js('Cedi'), Js('Dalasi'), Js('Daler'), Js('Daric'), Js('Denarius'), Js('Dinar'), Js('Dobra'), Js('Dollar'), Js('Drachma'), Js('Dram'), Js('Ducat'), Js('Ekwele'), Js('Elymais'), Js('Escudo'), Js('Euro'), Js('Florin'), Js('Follis'), Js('Franc'), Js('Gourde'), Js('Guarani'), Js('Guilder'), Js('Hekte'), Js('Hwan'), Js('Inti'), Js('Keping'), Js('Kina'), Js('Koruna'), Js('Krone'), Js('Kuna'), Js('Kwacha'), Js('Kwanza'), Js('Kyat'), Js('Lari'), Js('Lempira'), Js('Leone'), Js('Leu'), Js('Lev'), Js('Lilangeni'), Js('Lira'), Js('Litas'), Js('Loti'), Js('Manat'), Js('Mark'), Js('Metica'), Js('Mon'), Js('Nakfa'), Js('Pataca'), Js('Peseta'), Js('Peso'), Js('Pound'), Js('Prutah'), Js('Pula'), Js('Qirsh'), Js('Quetzal'), Js('Rand'), Js('Real'), Js('Rial'), Js('Riel'), Js('Ringgit'), Js('Riyal'), Js('Ruble'), Js('Rufiyaa'), Js('Rupee'), Js('Rupiah'), Js('Shekel'), Js('Sheqel'), Js('Shilling'), Js('Sigloi'), Js('Sol'), Js('Solidus'), Js('Som'), Js('Somoni'), Js('Stater'), Js('Syli'), Js('Tael'), Js('Taka'), Js('Talent'), Js('Tenge'), Js('Tolar'), Js('Tremissis'), Js('Trite'), Js('Vatu'), Js('Won'), Js('Xu'), Js('Yen'), Js('Yuan'), Js('Zaire'), Js('Zuz')]))
pass
pass


# Add lib to the module scope
currencyNames = var.to_python()
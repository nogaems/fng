__all__ = ['dwarfNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js('Ara'), Js('Alfo'), Js('Bari'), Js('Be'), Js('Bo'), Js('Bha'), Js('Bu'), Js('Ba'), Js('Bra'), Js('Bro'), Js('Brou'), Js('Bru'), Js('Da'), Js('Dalo'), Js('Dare'), Js('De'), Js('Dhu'), Js('Dho'), Js('Do'), Js('Dora'), Js('Dwo'), Js('Dou'), Js('Duri'), Js('Du'), Js('El'), Js('Eri'), Js('Fi'), Js('Fo'), Js('Fo'), Js('Ga'), Js('Gi'), Js('Gla'), Js('Glori'), Js('Go'), Js('Gra'), Js('Gro'), Js('Groo'), Js('Gru'), Js('Grou'), Js('Ha'), Js('Ha'), Js('He'), Js('He'), Js('Ho'), Js('Hou'), Js('Hu'), Js('Ja'), Js('Jo'), Js('Ka'), Js('Khe'), Js('Khu'), Js('Khou'), Js('Ko'), Js('Ku'), Js('Ki'), Js('Kra'), Js('Kro'), Js('Lo'), Js('Lu'), Js('Lo'), Js('Ma'), Js('Mo'), Js('Mu'), Js('Na'), Js('No'), Js('Nu'), Js('Nora'), Js('Nura'), Js('Ne'), Js('No'), Js('O'), Js('Ori'), Js('Rei'), Js('Ra'), Js('Ru'), Js('Sa'), Js('Si'), Js('Sna'), Js('Sko'), Js('Ska'), Js('Stro'), Js('The'), Js('Thi'), Js('Tho'), Js('Thra'), Js('Tha'), Js('Tore'), Js('Tha'), Js('Thra'), Js('Thro'), Js('Thu'), Js('Tu'), Js('U'), Js('Umi'), Js('Va'), Js('Vo'), Js('Whu'), Js('We'), Js('Wera'), Js('Yu'), Js('Yo'), Js('Ya')]))
var.put('nm2', Js([Js('b'), Js('br'), Js('dd'), Js('d'), Js('dr'), Js('dm'), Js('dgr'), Js('f'), Js('fr'), Js('gr'), Js('gg'), Js('gh'), Js('gn'), Js('k'), Js('kh'), Js('kgr'), Js('kdr'), Js('kk'), Js('kh'), Js('kr'), Js('l'), Js('lg'), Js('lgr'), Js('ldr'), Js('lm'), Js('md'), Js('mn'), Js('m'), Js('mm'), Js('mr'), Js('n'), Js('nd'), Js('ndr'), Js('ngr'), Js('nm'), Js('r'), Js('rr'), Js('rgr'), Js('rdr'), Js('rb'), Js('rg'), Js('rn'), Js('rh'), Js('rd'), Js('rm'), Js('rs'), Js('rf'), Js('s'), Js('ss'), Js('sdr'), Js('sgr'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('tm'), Js('th'), Js('tdr'), Js('tgr'), Js('v'), Js('vr'), Js('z'), Js('zm'), Js('zn'), Js('zz')]))
var.put('nm3', Js([Js('ac'), Js('aic'), Js('aec'), Js('ec'), Js('eac'), Js('ic'), Js('oc'), Js('oic'), Js('ouc'), Js('ack'), Js('aeck'), Js('eck'), Js('eack'), Js('ick'), Js('ock'), Js('oick'), Js('ouck'), Js('uck'), Js('uc'), Js('ad'), Js('aed'), Js('ed'), Js('ead'), Js('id'), Js('od'), Js('oid'), Js('oud'), Js('ud'), Js('uid'), Js('ag'), Js('aeg'), Js('eg'), Js('eag'), Js('ig'), Js('og'), Js('oug'), Js('ug'), Js('ak'), Js('aek'), Js('ek'), Js('eak'), Js('ik'), Js('ok'), Js('oki'), Js('uk'), Js('uik'), Js('ouk'), Js('uki'), Js('al'), Js('ael'), Js('el'), Js('eal'), Js('il'), Js('ol'), Js('oli'), Js('olin'), Js('olim'), Js('olir'), Js('oul'), Js('ul'), Js('uli'), Js('ulim'), Js('ulir'), Js('uil'), Js('am'), Js('ami'), Js('amli'), Js('amri'), Js('aem'), Js('em'), Js('eam'), Js('im'), Js('om'), Js('omli'), Js('omri'), Js('omi'), Js('oum'), Js('um'), Js('umi'), Js('umir'), Js('umin'), Js('umli'), Js('umlir'), Js('umlin'), Js('umri'), Js('an'), Js('aen'), Js('en'), Js('ean'), Js('in'), Js('on'), Js('onlim'), Js('onlir'), Js('oun'), Js('un'), Js('unli'), Js('unri'), Js('ar'), Js('arlum'), Js('arlun'), Js('arlug'), Js('arlig'), Js('aer'), Js('er'), Js('erlum'), Js('erlun'), Js('erlug'), Js('erlig'), Js('ear'), Js('ir'), Js('irlum'), Js('irlun'), Js('or'), Js('orli'), Js('orlim'), Js('orlum'), Js('orlun'), Js('orlig'), Js('orlug'), Js('oir'), Js('our'), Js('ur'), Js('uri'), Js('urim'), Js('urum'), Js('us'), Js('as'), Js('ous'), Js('aes'), Js('eas'), Js('at'), Js('atir'), Js('atum'), Js('atin'), Js('aet'), Js('et'), Js('eat'), Js('it'), Js('ot'), Js('otir'), Js('atin'), Js('otum'), Js('out'), Js('ut'), Js('ath'), Js('aeth'), Js('eth'), Js('eath'), Js('ith'), Js('oth'), Js('outh'), Js('uth')]))
var.put('nm4', Js([Js('A'), Js('Ara'), Js('Alfo'), Js('Bari'), Js('Be'), Js('Bo'), Js('Bha'), Js('Bu'), Js('Ba'), Js('Bra'), Js('Bro'), Js('Brou'), Js('Bru'), Js('Da'), Js('Dalo'), Js('Dare'), Js('De'), Js('Dhu'), Js('Dho'), Js('Do'), Js('Dora'), Js('Dwo'), Js('Dou'), Js('Duri'), Js('Du'), Js('El'), Js('Eri'), Js('Fi'), Js('Fo'), Js('Fo'), Js('Ga'), Js('Gi'), Js('Gla'), Js('Glori'), Js('Go'), Js('Gra'), Js('Gro'), Js('Groo'), Js('Gru'), Js('Grou'), Js('Ha'), Js('Ha'), Js('He'), Js('He'), Js('Ho'), Js('Hou'), Js('Hu'), Js('Ja'), Js('Jo'), Js('Ka'), Js('Khe'), Js('Khu'), Js('Khou'), Js('Ko'), Js('Ku'), Js('Ki'), Js('Kra'), Js('Kro'), Js('Lo'), Js('Lu'), Js('Lo'), Js('Ma'), Js('Mo'), Js('Mu'), Js('Na'), Js('No'), Js('Nu'), Js('Nora'), Js('Nura'), Js('Ne'), Js('No'), Js('O'), Js('Ori'), Js('Rei'), Js('Ra'), Js('Ru'), Js('Sa'), Js('Si'), Js('Sna'), Js('Sko'), Js('Ska'), Js('Stro'), Js('The'), Js('Thi'), Js('Tho'), Js('Thra'), Js('Tha'), Js('Tore'), Js('Tha'), Js('Thra'), Js('Thro'), Js('Thu'), Js('Tu'), Js('U'), Js('Umi'), Js('Va'), Js('Vo'), Js('Whu'), Js('We'), Js('Wera'), Js('Yu'), Js('Yo'), Js('Ya')]))
var.put('nm5', Js([Js('b'), Js('br'), Js('dd'), Js('d'), Js('dr'), Js('dm'), Js('dgr'), Js('dw'), Js('f'), Js('fr'), Js('gr'), Js('gg'), Js('gh'), Js('gn'), Js('k'), Js('kh'), Js('kgr'), Js('kdr'), Js('kk'), Js('kw'), Js('kh'), Js('kr'), Js('l'), Js('lg'), Js('lgr'), Js('ldr'), Js('lm'), Js('md'), Js('mw'), Js('mn'), Js('m'), Js('mm'), Js('mr'), Js('n'), Js('nd'), Js('ndr'), Js('nw'), Js('ngr'), Js('nm'), Js('r'), Js('rr'), Js('rgr'), Js('rdr'), Js('rb'), Js('rg'), Js('rn'), Js('rh'), Js('rd'), Js('rm'), Js('rs'), Js('rf'), Js('s'), Js('ss'), Js('sdr'), Js('sgr'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('tm'), Js('th'), Js('tdr'), Js('tgr'), Js('v'), Js('vr'), Js('w'), Js('z'), Js('zm'), Js('zn'), Js('zz')]))
var.put('nm6', Js([Js('abelle'), Js('aebelle'), Js('ebelle'), Js('ibelle'), Js('obelle'), Js('ubelle'), Js('alyn'), Js('aelyn'), Js('elyn'), Js('ealyn'), Js('ilyn'), Js('olyn'), Js('oulyn'), Js('ulyn'), Js('uilyn'), Js('alynn'), Js('aelynn'), Js('elynn'), Js('ealynn'), Js('ilynn'), Js('olynn'), Js('oulynn'), Js('ulynn'), Js('uilynn'), Js('abelyn'), Js('aebelyn'), Js('ebelyn'), Js('eabelyn'), Js('ibelyn'), Js('obelyn'), Js('oubelyn'), Js('ubelyn'), Js('uibelyn'), Js('abelynn'), Js('aebelynn'), Js('ebelynn'), Js('eabelynn'), Js('ibelynn'), Js('obelynn'), Js('oubelynn'), Js('ubelynn'), Js('uibelyn'), Js('anelyn'), Js('aenelyn'), Js('enelyn'), Js('eanelyn'), Js('inelyn'), Js('onelyn'), Js('ounelyn'), Js('unelyn'), Js('uinelyn'), Js('anelynn'), Js('aenelynn'), Js('enelynn'), Js('eanelynn'), Js('inelynn'), Js('onelynn'), Js('ounelynn'), Js('unelynn'), Js('uinelynn'), Js('agit'), Js('aegit'), Js('egit'), Js('eagit'), Js('igit'), Js('ogit'), Js('ugit'), Js('uigit'), Js('agith'), Js('aegith'), Js('egith'), Js('eagith'), Js('igith'), Js('ogith'), Js('ugith'), Js('uigith'), Js('irgit'), Js('irgith'), Js('uirgit'), Js('uirgith'), Js('airgit'), Js('airgith'), Js('arika'), Js('aerika'), Js('erika'), Js('earika'), Js('irika'), Js('orika'), Js('urika'), Js('atain'), Js('aetain'), Js('etain'), Js('eatain'), Js('itain'), Js('otain'), Js('utain'), Js('ataine'), Js('aetaine'), Js('etaine'), Js('eataine'), Js('itaine'), Js('otaine'), Js('utaine'), Js('ahilda'), Js('aehilda'), Js('ehilda'), Js('eahilda'), Js('ohilda'), Js('ihilda'), Js('uhilda'), Js('ahulda'), Js('aehulda'), Js('ehulda'), Js('eahulda'), Js('ohulda'), Js('ihulda'), Js('uhulda'), Js('agar'), Js('aegar'), Js('egar'), Js('eagar'), Js('igar'), Js('ogar'), Js('ugar'), Js('agaer'), Js('egaer'), Js('igaer'), Js('ogaer'), Js('ugaer'), Js('atrud'), Js('aetrud'), Js('etrud'), Js('eatrud'), Js('itrud'), Js('otrud'), Js('utrud'), Js('atrude'), Js('aetrude'), Js('etrude'), Js('eatrude'), Js('itrude'), Js('otrude'), Js('utrude'), Js('ada'), Js('aeda'), Js('eda'), Js('eada'), Js('ida'), Js('oda'), Js('uda'), Js('alda'), Js('aelda'), Js('elda'), Js('ealda'), Js('ilda'), Js('olda'), Js('oulda'), Js('ulda'), Js('alin'), Js('aelin'), Js('elin'), Js('ealin'), Js('ilin'), Js('olin'), Js('oulin'), Js('ulin'), Js('aline'), Js('aeline'), Js('eline'), Js('ealine'), Js('iline'), Js('oline'), Js('ouline'), Js('uline'), Js('atalin'), Js('aetalin'), Js('etalin'), Js('eatalin'), Js('italin'), Js('otalin'), Js('outalin'), Js('utalin'), Js('atalyn'), Js('aetalyn'), Js('etalyn'), Js('eatalyn'), Js('italyn'), Js('otalyn'), Js('outalyn'), Js('utalyn'), Js('atelin'), Js('aetelin'), Js('etelin'), Js('eatelin'), Js('itelin'), Js('otelin'), Js('outelin'), Js('utelin'), Js('atelyn'), Js('aetelyn'), Js('etelyn'), Js('eatelyn'), Js('itelyn'), Js('otelyn'), Js('outelyn'), Js('utelyn'), Js('angrid'), Js('aengrid'), Js('engrid'), Js('eangrid'), Js('ingrid'), Js('ongrid'), Js('oungrid'), Js('ungrid'), Js('ani'), Js('aeni'), Js('eni'), Js('eani'), Js('ini'), Js('oni'), Js('ouni'), Js('uni'), Js('ana'), Js('aena'), Js('ena'), Js('eana'), Js('ina'), Js('ona'), Js('ouna'), Js('una'), Js('alsia'), Js('aelsia'), Js('elsia'), Js('ealsia'), Js('ilsia'), Js('olsia'), Js('oulsia'), Js('ulsia'), Js('ala'), Js('aela'), Js('ela'), Js('eala'), Js('ila'), Js('ola'), Js('oula'), Js('ula'), Js('abella'), Js('aebella'), Js('ebella'), Js('eabella'), Js('ibella'), Js('obella'), Js('oubella'), Js('ubella'), Js('abela'), Js('aebela'), Js('ebela'), Js('eabela'), Js('ibela'), Js('obela'), Js('oubela'), Js('ubela'), Js('astr'), Js('aestr'), Js('estr'), Js('eastr'), Js('istr'), Js('ostr'), Js('oustr'), Js('ustr'), Js('abo'), Js('aebo'), Js('ebo'), Js('eabo'), Js('ibo'), Js('obo'), Js('oubo'), Js('ubo'), Js('abena'), Js('aebena'), Js('ebena'), Js('eabena'), Js('ibena'), Js('obena'), Js('oubena'), Js('ubena'), Js('abera'), Js('aebera'), Js('ebera'), Js('eabera'), Js('ibera'), Js('obera'), Js('oubera'), Js('ubera'), Js('adeth'), Js('aedeth'), Js('edeth'), Js('eadeth'), Js('ideth'), Js('odeth'), Js('oudeth'), Js('udeth'), Js('adrid'), Js('aedrid'), Js('edrid'), Js('eadrid'), Js('idrid'), Js('odrid'), Js('oudrid'), Js('udrid'), Js('abyrn'), Js('aebyrn'), Js('ebyrn'), Js('eabyrn'), Js('ibyrn'), Js('obyrn'), Js('oubyrn'), Js('ubyrn'), Js('agrett'), Js('aegrett'), Js('egrett'), Js('eagrett'), Js('igrett'), Js('ogrett'), Js('ougrett'), Js('ugrett'), Js('agret'), Js('aegret'), Js('egret'), Js('eagret'), Js('igret'), Js('ogret'), Js('ougret'), Js('ugret'), Js('asli'), Js('aesli'), Js('esli'), Js('easli'), Js('isli'), Js('osli'), Js('ousli'), Js('usli'), Js('ahilda'), Js('aehilda'), Js('ehilda'), Js('eahilda'), Js('ihilda'), Js('ohilda'), Js('ouhilda'), Js('uhilda'), Js('ahilde'), Js('aehilde'), Js('ehilde'), Js('eahilde'), Js('ihilde'), Js('ohilde'), Js('ouhilde'), Js('uhilde'), Js('aginn'), Js('aeginn'), Js('eginn'), Js('eaginn'), Js('iginn'), Js('oginn'), Js('ouginn'), Js('uginn'), Js('amora'), Js('aemora'), Js('emora'), Js('eamora'), Js('imora'), Js('omora'), Js('oumora'), Js('umora'), Js('alydd'), Js('aelydd'), Js('elydd'), Js('ealydd'), Js('ilydd'), Js('olydd'), Js('oulydd'), Js('ulydd'), Js('akara'), Js('aekara'), Js('ekara'), Js('eakara'), Js('ikara'), Js('okara'), Js('oukara'), Js('ukara'), Js('aren'), Js('aeren'), Js('eren'), Js('earen'), Js('iren'), Js('oren'), Js('ouren'), Js('uren'), Js('arra'), Js('aerra'), Js('erra'), Js('earra'), Js('irra'), Js('orra'), Js('ourra'), Js('urra'), Js('are'), Js('aere'), Js('ere'), Js('eare'), Js('ire'), Js('ore'), Js('oure'), Js('ure'), Js('awynn'), Js('aewynn'), Js('ewynn'), Js('eawynn'), Js('iwynn'), Js('owynn'), Js('ouwynn'), Js('uwynn'), Js('atryd'), Js('aetryd'), Js('etryd'), Js('eatryd'), Js('itryd'), Js('otryd'), Js('outryd'), Js('utryd'), Js('athra'), Js('aethra'), Js('ethra'), Js('eathra'), Js('ithra'), Js('othra'), Js('outhra'), Js('uthra'), Js('aserd'), Js('aeserd'), Js('eserd'), Js('easerd'), Js('iserd'), Js('oserd'), Js('ouserd'), Js('userd'), Js('tryd')]))
var.put('nm7', Js([Js('Ale'), Js('Amber'), Js('Anvil'), Js('Ash'), Js('Axe'), Js('Barbed'), Js('Barrel'), Js('Battle'), Js('Beast'), Js('Bone'), Js('Beryl'), Js('Bitter'), Js('Black'), Js('Blazing'), Js('Blessed'), Js('Blood'), Js('Blunt'), Js('Bone'), Js('Bottle'), Js('Boulder'), Js('Brew'), Js('Brick'), Js('Bright'), Js('Bristle'), Js('Broad'), Js('Bronze'), Js('Brown'), Js('Cave'), Js('Cask'), Js('Chain'), Js('Crag'), Js('Chaos'), Js('Coal'), Js('Coin'), Js('Copper'), Js('Dark'), Js('Deep'), Js('Dim'), Js('Dragon'), Js('Drake'), Js('Dusk'), Js('Earth'), Js('Ember'), Js('Fiery'), Js('Flint'), Js('Flask'), Js('Flint'), Js('Flat'), Js('Forge'), Js('Frost'), Js('Giant'), Js('Gold'), Js('Golden'), Js('Granite'), Js('Gravel'), Js('Gray'), Js('Great'), Js('Grey'), Js('Grim'), Js('Grumble'), Js('Hammer'), Js('Hard'), Js('Heavy'), Js('Hill'), Js('Honor'), Js('Horn'), Js('Ice'), Js('Ingot'), Js('Iron'), Js('Jade'), Js('Keg'), Js('Kobold'), Js('Krag'), Js('Lead'), Js('Large'), Js('Lava'), Js('Leather'), Js('Light'), Js('Long'), Js('Marble'), Js('Magma'), Js('Merry'), Js('Metal'), Js('Mithril'), Js('Mine'), Js('Mountain'), Js('Mud'), Js('Night'), Js('Noble'), Js('Oak'), Js('Oaken'), Js('Onyx'), Js('Opal'), Js('Ore'), Js('Orc'), Js('Plate'), Js('Pebble'), Js('Red'), Js('Rune'), Js('Ruby'), Js('Sapphire'), Js('Shadow'), Js('Shatter'), Js('Smelt'), Js('Silver'), Js('Snow'), Js('Steel'), Js('Storm'), Js('Strong'), Js('Troll'), Js('Thunder'), Js('Twilight'), Js('Treasure'), Js('Under'), Js('War'), Js('Warm'), Js('Whit'), Js('Wind'), Js('Wold'), Js('Wraith'), Js('Wyvern')]))
var.put('nm8', Js([Js('arm'), Js('armour'), Js('axe'), Js('back'), Js('bane'), Js('beard'), Js('basher'), Js('belly'), Js('belt'), Js('bender'), Js('blade'), Js('born'), Js('bow'), Js('braid'), Js('braids'), Js('branch'), Js('brand'), Js('breaker'), Js('brew'), Js('brewer'), Js('bringer'), Js('brow'), Js('buckle'), Js('buster'), Js('chest'), Js('chin'), Js('cloak'), Js('coat'), Js('delver'), Js('digger'), Js('foot'), Js('fall'), Js('fury'), Js('finger'), Js('flayer'), Js('feet'), Js('forge'), Js('forged'), Js('grog'), Js('grip'), Js('guard'), Js('gut'), Js('granite'), Js('hand'), Js('head'), Js('heart'), Js('helm'), Js('hide'), Js('hood'), Js('horn'), Js('jaw'), Js('mace'), Js('mail'), Js('maker'), Js('mantle'), Js('mane'), Js('master'), Js('maul'), Js('miner'), Js('pike'), Js('rock'), Js('river'), Js('shield'), Js('shaper'), Js('sword'), Js('shoulder'), Js('stone'), Js('spine'), Js('sunder'), Js('thane'), Js('toe'), Js('tank'), Js('view')]))
pass
pass


# Add lib to the module scope
dwarfNames = var.to_python()
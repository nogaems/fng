__all__ = ['scottishNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen', 'names2', 'namesMale', 'namesFemale'])
@Js
def PyJsHoisted_nameGen_(firstNames, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'firstNames':firstNames}, var)
    var.registers(['names1', 'firstNames', 'result'])
    var.put('names1', var.get('firstNames'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd1'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('namesMale', Js([Js('Adaidh'), Js('Adhamh'), Js('Àdhamh'), Js('Ailbeart'), Js('Ailean'), Js('Ailig'), Js('Ailpean'), Js('Ailpein'), Js('Aindrea'), Js('Aindreas'), Js('Alasdair'), Js('Amhladh'), Js('Amhlaibh'), Js('Amhlaidh'), Js('Amhlaigh'), Js('Angaidh'), Js('Anndra'), Js('Anndrais'), Js('Aodh'), Js('Aonghas'), Js('Aonghus'), Js('Arailt'), Js('Artair'), Js('Artur'), Js('Asgall'), Js('Àaron'), Js('Baltair'), Js('Bearnard'), Js('Beathan'), Js('Beistean'), Js('Benneit'), Js('Bhaltair'), Js('Bhatair'), Js('Brian'), Js('Cailean'), Js('Calum'), Js('Caomhainn'), Js('Cathal'), Js('Ciaran'), Js('Cliamain'), Js('Coinneach'), Js('Colla'), Js('Colum Cille'), Js('Comhnall'), Js('Conall'), Js('Conn'), Js('Cormac'), Js('Cormag'), Js('Crìsdean'), Js('Cuithbeart'), Js('Daibhidh'), Js('Dàibhidh'), Js('Daidh'), Js('Daniel'), Js('Deorsa'), Js('Deòrsa'), Js('Diarmad'), Js('Domhnall'), Js('Dòmhnall'), Js('Domhnull'), Js('Dòmhnull'), Js('Donaidh'), Js('Donnchadh'), Js('Dubh'), Js('Dubh-shìth'), Js('Dubhghall'), Js('Dànaidh'), Js('Dùghall'), Js('Dùghlas'), Js('Eachann'), Js('Eacharn'), Js('Eairdsidh'), Js('Ealar'), Js('Eanraig'), Js('Eanruig'), Js('Eideard'), Js('Eirdsidh'), Js('Ellair'), Js('Eoghann'), Js('Eòghann'), Js('Eumann'), Js('Eòghan'), Js('Eòin'), Js('Eòsaph'), Js('Faolan'), Js('Fearchar'), Js('Fearghas'), Js('Filib'), Js('Fionn'), Js('Fionnghall'), Js('Fionnghan'), Js('Fionnlagh'), Js('Frang'), Js('Frangan'), Js('Frangean'), Js('Friseal'), Js('Gill-easbuig'), Js('Gilleasbuig'), Js('Gill-Eathain'), Js('Gill-Eòin'), Js('Gill-Iosa'), Js('Gillìosa'), Js('Gille-Aindreis'), Js('Gille-Brìdhde'), Js('Gille-Caluim'), Js('Gille-Crìosd'), Js('Gilleasbaig'), Js('Gillebeart'), Js('Gillebrìde'), Js('Goiridh'), Js('Goraidh'), Js('Grannd'), Js('Greum'), Js('Griogair'), Js('Guaidre'), Js('Gòrdan'), Js('Harailt'), Js('Horas'), Js('Hùisdean'), Js('Iagan'), Js('Iain'), Js('Ianatan'), Js('Iomhair'), Js('Iomhar'), Js('Isaac'), Js('Iàcob'), Js('Iòna'), Js('Iòsaph'), Js('Labhrann'), Js('Labhruinn'), Js('Lachlann'), Js('Laomann'), Js('Luthais'), Js('Lùcas'), Js('Maoilios'), Js('Maol-Chaluim'), Js('Maol-Domhnuich'), Js('Maol-Dòmhnuich'), Js('Maol-Iosa'), Js('Maol-Moire'), Js('Maoldònaich'), Js('Maolmhuire'), Js('Maolruibh'), Js('Marc'), Js('Marcas'), Js('Martainn'), Js('Màrtainn'), Js('Mata'), Js('Micheil'), Js('Mhoirbheinn'), Js('Morgan'), Js('Muireach'), Js('Munga'), Js('Mungan'), Js('Murchadh'), Js('Mànas'), Js('Mànus'), Js('Mìcheal'), Js('Mìcheil'), Js('Neacal'), Js('Neachdainn'), Js('Niall'), Js('Niallghus'), Js('Oilbhreis'), Js('Oisean'), Js('Padean'), Js('Padruig'), Js('Para'), Js('Peadair'), Js('Peadar'), Js('Peadaran'), Js('Peadrus'), Js('Prainnseas'), Js('Pàdair'), Js('Pàdraig'), Js('Pàdruig'), Js('Pàl'), Js('Pàra'), Js('Pàrlan'), Js('Pòl'), Js('Raghnall'), Js('Raibeart'), Js('Raonull'), Js('Ringean'), Js('Risteard'), Js('Rob'), Js('Roibeart'), Js('Ruairidh'), Js('Ruaraidh'), Js('Ruiseart'), Js('Ràild'), Js('Sachairi'), Js('Samuel'), Js('Sandaidh'), Js('Seaghdh'), Js('Seathan'), Js('Seoc'), Js('Seocan'), Js('Seonaidh'), Js('Seoras'), Js('Seumas'), Js('Seòras'), Js('Seòsaidh'), Js('Sgàire'), Js('Sim'), Js('Simidh'), Js('Solamh'), Js('Somhairle'), Js('Steaphan'), Js('Stiùbhard'), Js('Stiùbhart'), Js('Sìm'), Js('Sìomon'), Js('Tadhg'), Js('Tamhas'), Js('Taog'), Js('Tasgall'), Js('Tearlach'), Js('Teàrlach'), Js('Tiobaid'), Js('Tomag'), Js('Tomaidh'), Js('Torcadall'), Js('Torcall'), Js('Torcull'), Js('Tormod'), Js('Tormoid'), Js('Tàmhas'), Js('Tòmachan'), Js('Tòmas'), Js('Uailean'), Js('Ualan'), Js('Ualraig'), Js('Uarraig'), Js('Uilleachan'), Js('Uilleam'), Js('Uisdean'), Js('Ùisdean')]))
var.put('namesFemale', Js([Js('Ailios'), Js('Ailis'), Js('Aimil'), Js('Aingealag'), Js('Anabla'), Js('Anna'), Js('Aoife'), Js('Barabal'), Js('Baraball'), Js('Barabla'), Js('Bearnas'), Js('Beasag'), Js('Beathag'), Js('Beileag'), Js('Beitidh'), Js('Beitiris'), Js('Beitris'), Js('Bhioctoria'), Js('Brighde'), Js('Brìghde'), Js('Brìde'), Js('Cairistiòna'), Js('Cairistìne'), Js('Cairistìona'), Js('Caitir'), Js('Caitlin'), Js('Caitrìona'), Js('Calaminag'), Js('Catrìona'), Js('Ceana'), Js('Ceit'), Js('Ceiteag'), Js('Ceitidh'), Js('Ciorsdan'), Js('Ciorstag'), Js('Ciorstaidh'), Js('Ciorstan'), Js('Cotrìona'), Js('Criosaidh'), Js('Curstag'), Js('Curstaidh'), Js('Deirdre'), Js('Deòiridh'), Js('Deònaidh'), Js('Dior-bhorgàil'), Js('Diorbhail'), Js('Dior-bhail'), Js('Dior-bhàil'), Js('Dìorbhail'), Js('Doileag'), Js('Doilidh'), Js('Doirin'), Js('Dolag'), Js('Ealasaid'), Js('Eamhair'), Js('Eilidh'), Js('Eimhir'), Js('Eiric'), Js('Eithrig'), Js('Eubh'), Js('Eubha'), Js('Èibhlin'), Js('Fionnaghal'), Js('Fionninghua'), Js('Fionnuala'), Js('Floireans'), Js('Flòraidh'), Js('Frangag'), Js('Giorsail'), Js('Giorsal'), Js('Gormall'), Js('Gormlaith'), Js('Isbeil'), Js('Iseabail'), Js('Iseabal'), Js('Leagsaidh'), Js('Leitis'), Js('Lili'), Js('Liùsaidh'), Js('Lucrais'), Js('Lìosa'), Js('Magaidh'), Js('Maighread'), Js('Mairead'), Js('Mairearad'), Js('Malamhìn'), Js('Malmhìn'), Js('Marsail'), Js('Marsaili'), Js('Marta'), Js('Milread'), Js('Moibeal'), Js('Moire'), Js('Moireach'), Js('Muire'), Js('Muireall'), Js('Màili'), Js('Màiri'), Js('Mòr'), Js('Mòrag'), Js('Nansaidh'), Js('Oighrig'), Js('Olibhia'), Js('Peanaidh'), Js('Peigi'), Js('Raghnaid'), Js('Raodhailt'), Js('Raonaid'), Js('Raonaild'), Js('Rut'), Js('Seasaìdh'), Js('Seonag'), Js('Seònaid'), Js('Simeag'), Js('Siubhan'), Js('Siùbhan'), Js('Siùsaidh'), Js('Siùsan'), Js('Sorcha'), Js('Stineag'), Js('Sìle'), Js('Sìleas'), Js('Sìlis'), Js('Sìne'), Js('Sìneag'), Js('Sìonag'), Js('Teasag'), Js('Teàrlag'), Js('Ùna'), Js('Una')]))
var.put('names2', Js([Js('Ìomharach'), Js('Aileanach'), Js('Ailpeanach'), Js('Allanach'), Js('Ambarsan'), Js('Andarsan'), Js('Anndrasdan'), Js('Arasgain'), Js('Bànach'), Js('Bòid'), Js('Bòideach'), Js('Baran'), Js('Barrach'), Js('Beitean'), Js('Bhàsa'), Js('Bhodhsa'), Js('Blàr'), Js('Blàrach'), Js('Blacach'), Js('Bochanan'), Js('Boid'), Js('Bràigheach'), Js('Brùn'), Js('Breac'), Js('Breathnach'), Js('Brothaigh'), Js('Bruis'), Js('Brus'), Js('Buideach'), Js('Buidheach'), Js('Buids'), Js('Buiseid'), Js('Càidh'), Js('Cèamp'), Js('Cèampach'), Js('Còmhan'), Js('Cailbhin'), Js('Caileanach'), Js('Caimbeul'), Js('Caimbeulach'), Js('Camran'), Js('Camshron'), Js('Camshronach'), Js('Cananach'), Js('Canonach'), Js('Caoidheach'), Js('Caolaisdean'), Js('Catach'), Js('Catan'), Js('Catanach'), Js('Ceallach'), Js('Ceanadach'), Js('Ceannaideach'), Js('Cearrach'), Js('Ceiteach'), Js('Ciar'), Js('Ciarach'), Js('Ciogach'), Js('Coineagan'), Js('Crannach'), Js('Creag'), Js('Creagach'), Js('Criatharach'), Js('Cuimeanach'), Js('Cuimein'), Js('Cuimeineach'), Js('Dòmhnallach'), Js('Dòmhnullach'), Js('Dùbhghlas'), Js('Dùghallach'), Js('Dùghlas'), Js('Dùghlasach'), Js('Dalais'), Js('Deòir'), Js('Deòireach'), Js('Druimeanach'), Js('Druimein'), Js('Druimeineach'), Js('Druiminn'), Js('Dubh'), Js('Dubhach'), Js('Dunaid'), Js('Dunaidh'), Js('Eabarcrombaigh'), Js('Fòlais'), Js('Fearghasdan'), Js('Fionnlasdan'), Js('Flimean'), Js('Foirbeis'), Js('Foirbeiseach'), Js('Forsàidh'), Js('Friseal'), Js('Frisealach'), Js('Gòrdan'), Js('Gòrdanach'), Js('Gall'), Js('Gallach'), Js('Geadais'), Js('Geadasach'), Js('Gearailteach'), Js('Gilios'), Js("Gill'Iosa"), Js('GillAndrais'), Js('GillEasbaig'), Js('GillEasbuig'), Js('GilleChrìost'), Js('GilleChriosd'), Js('Giobsan'), Js('Glas'), Js('Gobha'), Js('Grannd'), Js('Grannda'), Js('Granndach'), Js('Greum'), Js('Greumach'), Js('Griogal'), Js('Griogalach'), Js('Griogarach'), Js('Guaire'), Js('Guinne'), Js('Gunnach'), Js('Gutraidh'), Js('Lìos'), Js('Lìosach'), Js('Lùtair'), Js('Latharnach'), Js('Lathurna'), Js('Leòideach'), Js('Leamhanach'), Js('Leamhnach'), Js('Lobhdain'), Js('Loganach'), Js('Loudain'), Js('Màrnach'), Js('Màrr'), Js('Màrtainn'), Js('Mèinn'), Js('Mèinnearach'), Js('MacÀdaidh'), Js('MacÀdhaimh'), Js('MacÀidh'), Js('MacÌomhair'), Js('MacÌosaig'), Js('MacÙisdein'), Js("Mac'Ill'Anndrais"), Js("Mac'Ill'Eathainn"), Js("Mac'Ill'Fhinnein"), Js("Mac'Ill'Fhinntain"), Js("Mac'Ill'Fhionndaig"), Js("Mac'Ill'Iosa"), Js("Mac'Ill'Oig"), Js("Mac'Ille na Brataich"), Js("Mac'IlleBhàin"), Js("Mac'IlleBhreac"), Js("Mac'IlleBhuidh"), Js("Mac'IlleChiar"), Js("Mac'IlleDhuibh"), Js("Mac'IlleMhìcheil"), Js("Mac'IlleMhòire"), Js("Mac'IlleNaoimh"), Js("Mac'IlleRiabhaich"), Js("Mac'IlleRuaidh"), Js("Mac'Uirigh"), Js('MacAbhra'), Js('MacAbhsalain'), Js('MacAdaidh'), Js('MacAdhaimh'), Js('MacAididh'), Js('MacAilein'), Js('MacAilpein'), Js('MacAlasdair'), Js('MacAmbrais'), Js('MacAmhalghaidh'), Js('MacAmhlaidh'), Js('MacAmhlaigh'), Js('MacAnndaidh'), Js('MacAnndra'), Js('MacAnndrais'), Js('MacAodhagain'), Js('MacAoidh'), Js('MacAoidhein'), Js('MacAomalain'), Js('MacAonghais'), Js('MacAra'), Js('MacArtain'), Js('MacArtair'), Js('MacAsgaidh'), Js('MacAsgaill'), Js('MacAsgain'), Js('MacBeatha'), Js('MacBeathag'), Js('MacBhàididh'), Js('MacBhàtair'), Js('MacBharrais'), Js('MacBheatha'), Js('MacBheathaig'), Js('MacBheathain'), Js('MacBhigein'), Js('MacBhiocair'), Js('MacBhlàthain'), Js('MacBhrìghdeinn'), Js('MacBhradain'), Js('MacBhraonaigh'), Js('MacCàba'), Js('MacCòiseam'), Js('MacCòmhain'), Js('MacCòmhghan'), Js('MacCùga'), Js('MacCaibe'), Js('MacCailein'), Js('MacCain'), Js('MacCaisgein'), Js('MacCalmain'), Js('MacCaluim'), Js('MacCaog'), Js('MacCaoig'), Js('MacCardaidh'), Js('MacCarmaig'), Js('MacCathachaidh'), Js('MacCathail'), Js('MacCathain'), Js('MacCathasaigh'), Js('MacCathbhaidh'), Js('MacCathbharra'), Js('MacCeallaig'), Js('MacCeallaigh'), Js('MacCeallair'), Js('MacCearnaigh'), Js('MacCearraich'), Js('MacCeasain'), Js('MacChoinnich'), Js('MacCianain'), Js('MacCiarain'), Js('MacCinidh'), Js('MacCiomalain'), Js('MacCionadha'), Js('MacClambroch'), Js('MacCnaimhin'), Js('MacCnusachainn'), Js('MacCodrum'), Js('MacCoinnich'), Js('MacCoinnigh'), Js('MacColla'), Js('MacComhainn'), Js('MacConaill'), Js('MacConnain'), Js('MacCorcadail'), Js('MacCormaig'), Js('MacCosgraigh'), Js('MacCrìsdein'), Js('MacCròin'), Js('MacCrain'), Js('MacCreamhain'), Js('MacCriomain'), Js('MacCrithein'), Js('MacCrosain'), Js('MacCruimein'), Js('MacCuaig'), Js('MacCuidhein'), Js('MacCuilcein'), Js('MacCuinn'), Js('MacCuinnleis'), Js('MacCuirc'), Js('MacCuithein'), Js('MacCullach'), Js('MacCullaich'), Js('MacCumasgaigh'), Js('MacCumhais'), Js('MacCuthais'), Js('MacDhàibhidh'), Js('MacDhòmhnaill'), Js('MacDhùghaill'), Js('MacDhùnShléibhe'), Js('MacDheòrsa'), Js('MacDhiarmaid'), Js('MacDhonnchaidh'), Js('MacDhrostain'), Js('MacDhubhShìth'), Js('MacDhubhaich'), Js('MacDhubhaig'), Js('MacDhubhthaich'), Js('MacDhuibh'), Js('MacDhunlèibhe'), Js('MacDiarmaid'), Js('MacEòghainn'), Js('MacEachaidh'), Js('MacEachainn'), Js('MacEachairn'), Js('MacEacharna'), Js('MacEalair'), Js('MacEalar'), Js('MacEamailinn'), Js('MacEanain'), Js('MacEanraig'), Js('MacFhearchair'), Js('MacFhearghail'), Js('MacFhearghais'), Js('MacFhilib'), Js('MacFhiongain'), Js('MacFhionghain'), Js('MacFhionghuin'), Js('MacFhionnlaigh'), Js('MacFhitheachain'), Js('MacFhlaithbheartaich'), Js('MacFhraing'), Js('MacFhraingein'), Js('MacFigeinn'), Js('MacFrìdeinn'), Js('MacFuirigh'), Js('MacGairbheith'), Js('MacGaradh'), Js('MacGhearailt'), Js('MacGhille'), Js("MacGill'Eòin"), Js("MacGill'Earnain"), Js("MacGill'Easbaig"), Js("MacGill'Fhaolagain"), Js("MacGill'Fhiontag"), Js("MacGill'Oig"), Js("MacGill'Onaidh"), Js('MacGill-Eain'), Js('MacGillIosa'), Js('MacGille'), Js('MacGilleBhàin'), Js('MacGilleBhràth'), Js('MacGilleBhrìghde'), Js('MacGilleBhreac'), Js('MacGilleChaluim'), Js('MacGilleChrìosd'), Js('MacGilleDhonaghart'), Js('MacGilleDhuibh'), Js('MacGilleFhialain'), Js('MacGilleGhlais'), Js('MacGilleMhartainn'), Js('MacGilleRiabhaich'), Js('MacGilleSeathanaich'), Js('MacGilleathain'), Js('MacGiobain'), Js('MacGlaisein'), Js('MacGobhainn'), Js('MacGoraidh'), Js('MacGriogair'), Js('MacGuaire'), Js('MacGumaraid'), Js('MacIain'), Js('MacIllÌmheir'), Js('MacIllÌosa'), Js("MacIll'Éidich"), Js("MacIll'Eòin"), Js("MacIll'Fhaolain"), Js("MacIll'Fhialain"), Js("MacIll'Fhinnein"), Js("MacIll'Fhionndaig"), Js("MacIll'osa"), Js('MacIllAnndrais'), Js('MacIllAodhagain'), Js('MacIllDheòra'), Js('MacIllEarnain'), Js('MacIllEasbaig'), Js('MacIllEathain'), Js('MacIllFhaolagain'), Js('MacIllFheargain'), Js('MacIllFhionndain'), Js('MacIllIanain'), Js('MacIllIomchadha'), Js('MacIllOnchon'), Js('MacIllOnfhaidh'), Js('MacIllUidhir'), Js('MacIlleBhàin'), Js('MacIlleBheathain'), Js('MacIlleBhlàthain'), Js('MacIlleBhràth'), Js('MacIlleBhrìghde'), Js('MacIlleBhris'), Js('MacIlleBhuidhe'), Js('MacIlleChaluim'), Js('MacIlleChatain'), Js('MacIlleChathbhaidh'), Js('MacIlleChiar'), Js('MacIlleChiarain'), Js('MacIlleChomhghain'), Js('MacIlleChonaill'), Js('MacIlleChrìosd'), Js('MacIlleChruim'), Js('MacIlleDhòmhnaich'), Js('MacIlleDhonaghart'), Js('MacIlleDhubhthaich'), Js('MacIlleDhuibh'), Js('MacIlleDhuinn'), Js('MacIlleGhlais'), Js('MacIlleGhuinnein'), Js('MacIlleGhuirm'), Js('MacIlleMhàrtainn'), Js('MacIlleMhìcheil'), Js('MacIlleMhaoil'), Js('MacIlleMhearnaig'), Js('MacIlleMhoire'), Js('MacIlleNaoimh'), Js('MacIllePhàdraig'), Js('MacIllePheadair'), Js('MacIlleRiabhaich'), Js('MacIlleRuaidh'), Js('MacIlleSheathain'), Js('MacIlleSheathanaich'), Js('MacIlleSheathnaich'), Js('MacIlleThòmhais'), Js('MacIomhair'), Js('MacIonmhainn'), Js('MacIosaig'), Js('MacLùcaidh'), Js('MacLùcais'), Js('MacLabhrainn'), Js('MacLabhruinn'), Js('MacLachlainn'), Js('MacLagain'), Js('MacLamraich'), Js('MacLaomainn'), Js('MacLathagain'), Js('MacLeòid'), Js('MacLeòir'), Js('MacLianain'), Js('MacLiuthar'), Js('MacLothaidh'), Js('MacLughaidh'), Js('MacLuinge'), Js('MacLuirg'), Js('MacLulaich'), Js('MacMhànais'), Js('MacMhàrtainn'), Js('MacMhèinn'), Js('MacMhìcheil'), Js('MacMhòrdha'), Js('MacMhaighstir'), Js('MacMhanachain'), Js('MacMhannain'), Js('MacMhaoilein'), Js('MacMhaoirn'), Js('MacMhaolÌosa'), Js('MacMhaolBheatha'), Js('MacMhaolChaluim'), Js('MacMhaolDòmhnaich'), Js('MacMhaolagain'), Js('MacMhaolain'), Js('MacMharais'), Js('MacMharcais'), Js('MacMhata'), Js('MacMhatha'), Js('MacMhathain'), Js('MacMhiadhchain'), Js('MacMhoirein'), Js('MacMhorgain'), Js('MacMhuircheartaich'), Js('MacMhuirich'), Js('MacMhunna'), Js('MacMhurardaich'), Js('MacMhurchaidh'), Js('MacNèill'), Js('MacNìll'), Js('MacNaois'), Js('MacNaomhain'), Js('MacNeacail'), Js('MacNeachdain'), Js('MacNeis'), Js('MacNia'), Js('MacNiallghais'), Js('MacNiallghuis'), Js('MacNiocail'), Js('MacNobaill'), Js('MacPhàdraig'), Js('MacPhàic'), Js('MacPhàidein'), Js('MacPhàil'), Js('MacPhàrlain'), Js('MacPhòil'), Js('MacPhaid'), Js('MacPhaidein'), Js('MacPhail'), Js('MacPhairce'), Js('MacPheadair'), Js('MacPheadarain'), Js('MacPheadrais'), Js('MacPheidearain'), Js('MacPhilip'), Js('MacRàild'), Js('MacRìdeinn'), Js('MacRìgh'), Js('MacRabaidh'), Js('MacRaghnaill'), Js('MacRaibeirt'), Js('MacRaoimhin'), Js('MacRaoiridh'), Js('MacRaonaill'), Js('MacRath'), Js('MacRiada'), Js('MacRiocaird'), Js('MacRisnidh'), Js('MacRob'), Js('MacRobaidh'), Js('MacRoibeirt'), Js('MacRoithridh'), Js('MacRuairidh'), Js('MacRusachainn'), Js('MacShìm'), Js('MacShanndaidh'), Js('MacSheòrais'), Js('MacSheòrsa'), Js('MacShealbhaigh'), Js('MacShimidh'), Js('MacShithich'), Js('MacShitrig'), Js('MacShomhairle'), Js('MacShuibhne'), Js('MacSiridh'), Js('MacSporain'), Js('MacSuain'), Js('MacSual'), Js('MacThàmhais'), Js('MacThòmais'), Js('MacThaidhg'), Js('MacTheàrlaich'), Js('MacThom'), Js('MacThomaidh'), Js('MacThorcadail'), Js('MacThorcaill'), Js('MacTiridh'), Js('MacTuirc'), Js('MacUalraig'), Js('MacUaraig'), Js('MacUchtraigh'), Js('MacUilleim'), Js('MacUirigh'), Js('MacUisdein'), Js('MacUrardaidh'), Js('MacUrardaigh'), Js('MacUrchadain'), Js('MacUrchaidh'), Js('MacUsbaig'), Js('Maoileanach'), Js('MaolIosa'), Js('Maolanach'), Js('Matasan'), Js('Mathanach'), Js('Matharnach'), Js('Mawr, Maor'), Js('Moireach'), Js('Moireasdan'), Js('Moireasdanach'), Js('Morgan'), Js('Morganach'), Js('Munna'), Js('Niocalsan'), Js("O'Brolchain"), Js("O'Cain"), Js("O'Luingeachain"), Js('Padarsan'), Js('Paorach'), Js('Peadarsan'), Js('Peucag'), Js('Peutan'), Js('Preas'), Js('Puidreach'), Js('Ròs'), Js('Ròsach'), Js('Rathais'), Js('Robasan'), Js('Robasdan'), Js('Roid'), Js('Roideach'), Js('Ros'), Js('Rosach'), Js('Rothach'), Js('Ruadh'), Js('Ruiseal'), Js('Sùdrach'), Js('Sailcirc'), Js('Salmond'), Js('Seadh'), Js('Seadhg'), Js('Seagha'), Js('Seaghach'), Js('Seathanach'), Js('Sgèin'), Js('Sginnearach'), Js('Sgot'), Js('Singleir'), Js('Siosal'), Js('Siosalach'), Js('Smios'), Js('Stiùbhart'), Js('Stiùbhartach'), Js('Sutharlainn'), Js('Sutharlan'), Js('Suthurlanach'), Js('Tàileach'), Js('Tàillear'), Js('Talmhach'), Js('Tod'), Js('Todt'), Js('Tolmach'), Js('Tuairnear'), Js('Tulach'), Js('Ualas'), Js('Umphraidh'), Js('Urchadainn'), Js('Urchardan')]))
pass
pass


# Add lib to the module scope
scottishNames = var.to_python()
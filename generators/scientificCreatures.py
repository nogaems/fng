__all__ = ['scientificCreatures']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Acanthuridae'), Js('Achatina'), Js('Achatinoidea'), Js('Acinonyx'), Js('Actinidia'), Js('Aegypius'), Js('Aepyceros'), Js('Ailuropoda'), Js('Ailurus'), Js('Ajaja'), Js('Alcelaphinae'), Js('Alces'), Js('Alligator'), Js('Alopex'), Js('Alouatta'), Js('Ambystoma'), Js('Amphiprioninae'), Js('Anas'), Js('Anguis'), Js('Anisoptera'), Js('Anthozoa'), Js('Apatura'), Js('Apis'), Js('Apodemus'), Js('Aptenodytes'), Js('Arachnocampa'), Js('Arctictis'), Js('Arctocephalinae'), Js('Ardeidae'), Js('Arini'), Js('Arvicola'), Js('Astrochelys'), Js('Atelerix'), Js('Balaenoptera'), Js('Balsenoptera'), Js('Barbus'), Js('Betta'), Js('Bison'), Js('Blattaria'), Js('Bombina'), Js('Bombus'), Js('Bos'), Js('Brachypelma'), Js('Brachyura'), Js('Branta'), Js('Bubalus'), Js('Bubo'), Js('Bufo'), Js('Buteo'), Js('Cacajao'), Js('Caelifera'), Js('Caimaninae'), Js('Callithrix'), Js('Camelus'), Js('Canis'), Js('Canus'), Js('Capra'), Js('Caracal'), Js('Carcharhinus'), Js('Carcharodon'), Js('Caridea'), Js('Castor'), Js('Casuarius'), Js('Caudata'), Js('Cavia'), Js('Cebus'), Js('Cephalopterus'), Js('Ceratophrys'), Js('Ceratotherium'), Js('Cerura'), Js('Cetorhinus'), Js('Cettia'), Js('Chaetodontidae'), Js('Chamaeleonidae'), Js('Chelonioidea'), Js('Chelydridae'), Js('Chilopoda'), Js('Chinchilla'), Js('Chiroptera'), Js('Chlamydosaurus'), Js('Chlamyphorus'), Js('Chlorocebus'), Js('Choeropsis'), Js('Choloepus'), Js('Cichlidae'), Js('Cirripedia'), Js('Civettictis'), Js('Cnidaria'), Js('Coccinellidae'), Js('Coleoptera'), Js('Connochaetes'), Js('Coraciiformes'), Js('Coturnix'), Js('Crocodylus'), Js('Crocuta'), Js('Cryptoprocta'), Js('Cuon'), Js('Cygnus'), Js('Dasyatis'), Js('Dasypodidae'), Js('Dasyurus'), Js('Daubentonia'), Js('Delphinus'), Js('Demospongiae'), Js('Dendrobatidae'), Js('Dendrobranchiata'), Js('Dermaptera'), Js('Desmodontinae'), Js('Dicerorhinus'), Js('Diceros'), Js('Didelphis'), Js('Diomedeidae'), Js('Diplopoda'), Js('Diptera'), Js('Dracaena'), Js('Dromaius'), Js('Dugong'), Js('Dynastes'), Js('Echinoidea'), Js('Electrophorus'), Js('Elephantulus'), Js('Elephas'), Js('Eleutherodactylus'), Js('Emydidae'), Js('Enhydra'), Js('Ephemeroptera'), Js('Equus'), Js('Erethizon'), Js('Erithacus'), Js('Erythrocebus'), Js('Esox'), Js('Eudyptes'), Js('Eudyptula'), Js('Euptilotis'), Js('Falconiforme'), Js('Felis'), Js('Formicidae'), Js('Fratercula'), Js('Fregata'), Js('Funambulus'), Js('Galeocerdo'), Js('Gallinula'), Js('Gallus'), Js('Gavia'), Js('Gavialis'), Js('Gekkonidae'), Js('Geochelone'), Js('Gerbillinae'), Js('Gerridae'), Js('Ginglymostoma'), Js('Giraffa'), Js('Gliridae'), Js('Gopherus'), Js('Gorilla'), Js('Gruidae'), Js('Gulo'), Js('Gynnidomorpha'), Js('Halichoerus'), Js('Helarctos'), Js('Heleioporus'), Js('Heloderma'), Js('Helogale'), Js('Hemigalus'), Js('Heterodontus'), Js('Hieraatus'), Js('Hippocampus'), Js('Hippopotamus'), Js('Holothuroidea'), Js('Homo'), Js('Hydrochoerus'), Js('Hydrodamalis'), Js('Hydrurga'), Js('Hyla'), Js('Hylobatidae'), Js('Hymenoptera'), Js('Iguana'), Js('Indri'), Js('Insecta'), Js('Isoptera'), Js('Labridae'), Js('Lacerta'), Js('Lacertilia'), Js('Lagenorhynchus'), Js('Lagothrix'), Js('Lama'), Js('Larva'), Js('Latrodectus'), Js('Lemmus'), Js('Lemur'), Js('Leontopithecus'), Js('Leopardus'), Js('Lepisosteidae'), Js('Leptailurus'), Js('Lepus'), Js('Limulidae'), Js('Lissotriton'), Js('Litoria'), Js('Lopholithodes'), Js('Loxodonta'), Js('Lucanidae'), Js('Luscinia'), Js('Lutra'), Js('Lycaon'), Js('Lynx'), Js('Macaca'), Js('Macropus'), Js('Mammuthus'), Js('Mandrillus'), Js('Manta'), Js('Megadyptes'), Js('Megaptera'), Js('Meleagris'), Js('Melopsittacus'), Js('Mephitis'), Js('Merops'), Js('Mesobatrachia'), Js('Mesocricetus'), Js('Metynnis'), Js('Microcebus'), Js('Mirounga'), Js('Moloch'), Js('Muraenidae'), Js('Mustela'), Js('Myrmecobius'), Js('Myrmecophaga'), Js('Nandinia'), Js('Nasalis'), Js('Nasua'), Js('Nectophryne'), Js('Neofelis'), Js('Nephropidae'), Js('Numididae'), Js('Nyctereutes'), Js('Ochotona'), Js('Octopus'), Js('Odobenus'), Js('Odocoileus'), Js('Okapia'), Js('Oniscidea'), Js('Ophisaurus'), Js('Orcinus'), Js('Oriolus'), Js('Ornithorhynchus'), Js('Oryctolagus'), Js('Osteolaemus'), Js('Ostreidae'), Js('Otariidae'), Js('Ovis'), Js('Paguma'), Js('Paguroidea'), Js('Pan'), Js('Panthera'), Js('Papilionoidea'), Js('Papio'), Js('Paracheirodon'), Js('Paradisaeidae'), Js('Paradoxurus'), Js('Paralichthys'), Js('Passeridae'), Js('Pavo'), Js('Pecari'), Js('Pelecanus'), Js('Pelophylax'), Js('Perameles'), Js('Phacochoerus'), Js('Phaethon'), Js('Phalanger'), Js('Phalangeriforme'), Js('Pharomachrus'), Js('Phascolarctos'), Js('Phasianus'), Js('Phasmatodea'), Js('Phoca'), Js('Phoenicopterus'), Js('Phycodurus'), Js('Physeter'), Js('Physignathus'), Js('Pica'), Js('Picidae'), Js('Platanistoidea'), Js('Poecilia'), Js('Pogona'), Js('Pomacanthidae'), Js('Pongo'), Js('Prionailurus'), Js('Pristella'), Js('Procavia'), Js('Procyon'), Js('Proteus'), Js('Protoreaster'), Js('Pseudoryx'), Js('Psittacine'), Js('Pterois'), Js('Pteromyini'), Js('Pygocentrus'), Js('Pygoscelis'), Js('Ramphastos'), Js('Rana'), Js('Rangifer'), Js('Raphus'), Js('Rattus'), Js('Recurvirostra'), Js('Rhincodon'), Js('Rhinoceros'), Js('Rhinocerotidae'), Js('Rhinoderma'), Js('Rupicapra'), Js('Saguinus'), Js('Saimiri'), Js('Sarcophilus'), Js('Sciuridae'), Js('Scorpaenidae'), Js('Scorpiones'), Js('Sepiida'), Js('Serpentes'), Js('Setonix'), Js('Siluriformes'), Js('Simia'), Js('Smilodon'), Js('Spermophilus'), Js('Spheniscus'), Js('Sphenodon'), Js('Sphyraena'), Js('Sphyrna'), Js('Squalus'), Js('Stegostoma'), Js('Strigops'), Js('Strix'), Js('Struthio'), Js('Sula'), Js('Suricata'), Js('Sus'), Js('Symphysodon'), Js('Syncerus'), Js('Tachyglossus'), Js('Talpidae'), Js('Tamias'), Js('Tapirus'), Js('Tarsius'), Js('Taxidea'), Js('Tetraodontidae'), Js('Tetraoninae'), Js('Teuthida'), Js('Threskiornithidae'), Js('Thylogale'), Js('Tragelaphus'), Js('Tremarctos'), Js('Trichechus'), Js('Tridacna'), Js('Trochilidae'), Js('Troglodytes'), Js('Tursiops'), Js('Tyto'), Js('Urochordata'), Js('Uroplatus'), Js('Ursidae'), Js('Ursus'), Js('Varanus'), Js('Vespa'), Js('Viverra'), Js('Vombatus'), Js('Vulpes'), Js('Xenopus')]))
var.put('nm2', Js([Js('Abelii'), Js('Acanthias'), Js('Aculeatus'), Js('Acutorostrata'), Js('Adeliae'), Js('Aegagrus'), Js('Afra'), Js('Africana'), Js('Africanus'), Js('Agassizii'), Js('Agilis'), Js('Ajaja'), Js('Alba'), Js('Albiventris'), Js('Alces'), Js('Alisman'), Js('Alpinus'), Js('Altaica'), Js('Aluco'), Js('Amblyrhynchos'), Js('Americanus'), Js('Amoyensis'), Js('Amphibius'), Js('Anatinus'), Js('Anguinus'), Js('Antarcticus'), Js('Antipodes'), Js('Arctica'), Js('Arcticus'), Js('Arctos'), Js('Argenteus'), Js('Aries'), Js('Asinus'), Js('Atratus'), Js('Auratus'), Js('Aurelia'), Js('Aureus'), Js('Axelrodi'), Js('Bactrianus'), Js('Barbus'), Js('Bengalensis'), Js('Berengei'), Js('Bicolor'), Js('Bicornis'), Js('Binotata'), Js('Binturong'), Js('Birostris'), Js('Bison'), Js('Borneensis'), Js('Brachyurus'), Js('Bubalis'), Js('Bufo'), Js('Buteo'), Js('Caballus'), Js('Caffer'), Js('Camelopardalis'), Js('Camelus'), Js('Canadensis'), Js('Capensis'), Js('Capucinus'), Js('Caracal'), Js('Carcharias'), Js('Catesbeiana'), Js('Catta'), Js('Centroura'), Js('Chrysocome'), Js('Chrysolophus'), Js('Cinereus'), Js('Cirratum'), Js('Civetta'), Js('Colchicus'), Js('Concolor'), Js('Corbetti'), Js('Coturnix'), Js('Cristatus'), Js('Crocuta'), Js('Cucullatus'), Js('Cuniculus'), Js('Cuvier'), Js('Cyclotis'), Js('Darwinii'), Js('Deliciosa'), Js('Delphis'), Js('Demersus'), Js('Derbyanus'), Js('Diehli'), Js('Dingo'), Js('Diphone'), Js('Domesticus'), Js('Dorsaum'), Js('Dromedarius'), Js('Dugon'), Js('Electricus'), Js('Elegans'), Js('Eques'), Js('Equus'), Js('Erminea'), Js('Esculentus'), Js('Europaeus'), Js('Eurycerus'), Js('Falconeri'), Js('Familiaris'), Js('Fasciatum'), Js('Fasciatus'), Js('Fascicularis'), Js('Ferox'), Js('Forsteri'), Js('Fragilis'), Js('Francisci'), Js('Fulgens'), Js('Fulica'), Js('Furo'), Js('Fuscata'), Js('Gallus'), Js('Gangeticus'), Js('Geoffroyi'), Js('Gigantea'), Js('Giganteus'), Js('Gigas'), Js('Glama'), Js('Gorilla'), Js('Graueri'), Js('Grevyi'), Js('Grunniens'), Js('Grypus'), Js('Guianensis'), Js('Gulo'), Js('Habroptilus'), Js('Harrisii'), Js('Hercules'), Js('Hermaphroditus'), Js('Hircus'), Js('Hoffmani'), Js('Horriblis'), Js('Horridus'), Js('Humboldti'), Js('Hydrochaeris'), Js('Iberia'), Js('Iguana'), Js('Immer'), Js('Imperator'), Js('Indicus'), Js('Indri'), Js('Iris'), Js('Jacksoni'), Js('Johnstoni'), Js('Jubatus'), Js('Kingii'), Js('Komodoensis'), Js('Laevis'), Js('Lagopus'), Js('Lagotricha'), Js('Lanigera'), Js('Larvata'), Js('Larvatus'), Js('Latrans'), Js('Lemmus'), Js('Leo'), Js('Leptonyx'), Js('Lessonae'), Js('Leucas'), Js('Liberiensis'), Js('Lotor'), Js('Luminosa'), Js('Lupus'), Js('Lutris'), Js('Lynx'), Js('Macrocephalus'), Js('Maculatus'), Js('Magarhynchos'), Js('Magellanicus'), Js('Malayanus'), Js('Manatu'), Js('Mandarinia'), Js('Mandtii'), Js('Marinus'), Js('Maritimus'), Js('Maxillaris'), Js('Maximus'), Js('Melampus'), Js('Melanoleuca'), Js('Mendiculus'), Js('Mephitis'), Js('Mexicanum'), Js('Midas'), Js('Minor'), Js('Monachus'), Js('Mule'), Js('Murinus'), Js('Musculus'), Js('Nasua'), Js('Nasuta'), Js('Nattereri'), Js('Neanderthalensis'), Js('Nebouxii'), Js('Nebulosa'), Js('Nghetinhensis'), Js('Nigra'), Js('Nivalis'), Js('Nodosus'), Js('Novaeangliae'), Js('Novaehollandiae'), Js('Obscurus'), Js('Occidentalis'), Js('Oedipus'), Js('Onca'), Js('Orca'), Js('Orientalis'), Js('Oriolus'), Js('Ornata'), Js('Ornatus'), Js('Palmarum'), Js('Paniscus'), Js('Papua'), Js('Pardalis'), Js('Pardus'), Js('Parvula'), Js('Patagonicus'), Js('Patas'), Js('Physalus'), Js('Pica'), Js('Pictus'), Js('Platyrhynchos'), Js('Populator'), Js('Porcellus'), Js('Primigenius'), Js('Procyonoides'), Js('Punctatus'), Js('Putorius'), Js('Pygerythrus'), Js('Pygmaea'), Js('Pygmaeus'), Js('Quagga'), Js('Radiata'), Js('Rattus'), Js('Reticulata'), Js('Richardsonii'), Js('Ridibundus'), Js('Robustus'), Js('Rosalia'), Js('Rosmarus'), Js('Rubecula'), Js('Rufus'), Js('Rupicapra'), Js('Sapiens'), Js('Scandiacus'), Js('Schlegeli'), Js('Scrofa'), Js('Scyphozoa'), Js('Serval'), Js('Simum'), Js('Smithi'), Js('Sondaicus'), Js('Sphinx'), Js('Spilogaster'), Js('Splendens'), Js('Strepsiceros'), Js('Striatus'), Js('Sulfuratus'), Js('Sumatrae'), Js('Sumatranus'), Js('Sumatrensis'), Js('Suricatta'), Js('Suspectum'), Js('Sylvaticus'), Js('Tajacu'), Js('Tangalunga'), Js('Tarandus'), Js('Taurinus'), Js('Taurus'), Js('Taxus'), Js('Temporaria'), Js('Tetraspis'), Js('Tibetanus'), Js('Tigrinum'), Js('Tigris'), Js('Toco'), Js('Tridactyla'), Js('Troglodytes'), Js('Truncatus'), Js('Typus'), Js('Undulatus'), Js('Unicornis'), Js('Ursinus'), Js('Vinula'), Js('Virginiana'), Js('Vitticeps'), Js('Vitulina'), Js('Viverrinus'), Js('Volitans'), Js('Vulgaris'), Js('Vulpes'), Js('Zebra'), Js('Zerda'), Js('Zygaena')]))
var.put('nm3', Js([Js('Acanth'), Js('Ach'), Js('Achat'), Js('Acin'), Js('Act'), Js('Aeg'), Js('Aepyc'), Js('Ail'), Js('Ailur'), Js('Aj'), Js('Al'), Js('Alc'), Js('Alcel'), Js('All'), Js('Amb'), Js('Amphipr'), Js('An'), Js('Ang'), Js('Anis'), Js('Anth'), Js('Ap'), Js('Apat'), Js('Apod'), Js('Apten'), Js('Ar'), Js('Arachn'), Js('Arct'), Js('Arctoc'), Js('Ard'), Js('Arv'), Js('Astr'), Js('Atel'), Js('Balaen'), Js('Balsen'), Js('Barb'), Js('Bett'), Js('Bis'), Js('Blatt'), Js('Bomb'), Js('Bos'), Js('Br'), Js('Brach'), Js('Bub'), Js('Buf'), Js('But'), Js('Cac'), Js('Cael'), Js('Caim'), Js('Call'), Js('Cam'), Js('Can'), Js('Capr'), Js('Car'), Js('Carch'), Js('Cas'), Js('Cast'), Js('Caud'), Js('Cav'), Js('Ceb'), Js('Cephal'), Js('Cer'), Js('Cerat'), Js('Cet'), Js('Cett'), Js('Chaetod'), Js('Chamael'), Js('Chel'), Js('Chelon'), Js('Chil'), Js('Chinch'), Js('Chiropt'), Js('Chlam'), Js('Chlamyd'), Js('Chlor'), Js('Choer'), Js('Chol'), Js('Cichl'), Js('Cirr'), Js('Civett'), Js('Cnid'), Js('Coccin'), Js('Coleopt'), Js('Connoch'), Js('Corac'), Js('Cot'), Js('Croc'), Js('Crocod'), Js('Crypt'), Js('Cuon'), Js('Cygn'), Js('Das'), Js('Dasyp'), Js('Daubent'), Js('Delph'), Js('Demosp'), Js('Dendrob'), Js('Dendrobr'), Js('Derm'), Js('Desmod'), Js('Dic'), Js('Dicer'), Js('Did'), Js('Diom'), Js('Dipl'), Js('Dipt'), Js('Drac'), Js('Drom'), Js('Dug'), Js('Dyn'), Js('Echin'), Js('Electr'), Js('Eleph'), Js('Eleuther'), Js('Emyd'), Js('Enh'), Js('Ephem'), Js('Eq'), Js('Ereth'), Js('Erith'), Js('Erythr'), Js('Es'), Js('Eud'), Js('Eupt'), Js('Falcon'), Js('Fel'), Js('Formic'), Js('Frat'), Js('Freg'), Js('Fun'), Js('Galeoc'), Js('Gall'), Js('Gallin'), Js('Gav'), Js('Gekkon'), Js('Geoch'), Js('Gerb'), Js('Gerr'), Js('Ginglym'), Js('Gir'), Js('Glir'), Js('Goph'), Js('Gor'), Js('Gruid'), Js('Gul'), Js('Gynnid'), Js('Halich'), Js('Hel'), Js('Heleiop'), Js('Helod'), Js('Helog'), Js('Hemig'), Js('Heter'), Js('Hier'), Js('Hipp'), Js('Hippop'), Js('Holoth'), Js('Hom'), Js('Hydr'), Js('Hydrod'), Js('Hyl'), Js('Hylob'), Js('Hymen'), Js('Iguan'), Js('Indr'), Js('Ins'), Js('Isopt'), Js('Labr'), Js('Lac'), Js('Lacert'), Js('Lag'), Js('Lagenorh'), Js('Lam'), Js('Larv'), Js('Latr'), Js('Lem'), Js('Lemm'), Js('Leontop'), Js('Leop'), Js('Lep'), Js('Lepis'), Js('Lept'), Js('Limul'), Js('Liss'), Js('Lit'), Js('Lophol'), Js('Loxod'), Js('Lucan'), Js('Lusc'), Js('Lutr'), Js('Lyc'), Js('Lynx'), Js('Mac'), Js('Macr'), Js('Mammuth'), Js('Mandr'), Js('Mant'), Js('Megad'), Js('Megapt'), Js('Meleagr'), Js('Melops'), Js('Meph'), Js('Mer'), Js('Mesobatr'), Js('Mesocr'), Js('Met'), Js('Microc'), Js('Mir'), Js('Mol'), Js('Muraen'), Js('Must'), Js('Myrmec'), Js('Nand'), Js('Nas'), Js('Nectophr'), Js('Neof'), Js('Nephr'), Js('Numid'), Js('Nycter'), Js('Ochot'), Js('Octop'), Js('Odob'), Js('Odoc'), Js('Okap'), Js('Onisc'), Js('Ophis'), Js('Orc'), Js('Oriol'), Js('Ornithorh'), Js('Oryct'), Js('Osteol'), Js('Ostr'), Js('Otar'), Js('Ov'), Js('Pag'), Js('Pagur'), Js('Pan'), Js('Panth'), Js('Pap'), Js('Papilion'), Js('Parach'), Js('Paradis'), Js('Paradox'), Js('Paral'), Js('Pass'), Js('Pav'), Js('Pec'), Js('Pelec'), Js('Peloph'), Js('Peram'), Js('Phacoch'), Js('Phaeth'), Js('Phal'), Js('Phalanger'), Js('Pharom'), Js('Phas'), Js('Phascol'), Js('Phasmat'), Js('Phoc'), Js('Phoenic'), Js('Phycod'), Js('Phys'), Js('Physign'), Js('Pic'), Js('Platan'), Js('Poec'), Js('Pog'), Js('Pomac'), Js('Pong'), Js('Prion'), Js('Prist'), Js('Proc'), Js('Prot'), Js('Protor'), Js('Pseud'), Js('Psitt'), Js('Pter'), Js('Pterom'), Js('Pygoc'), Js('Pygosc'), Js('Ramph'), Js('Ran'), Js('Rang'), Js('Raph'), Js('Ratt'), Js('Recurv'), Js('Rhinc'), Js('Rhinoc'), Js('Rhinocer'), Js('Rhinod'), Js('Rupic'), Js('Sag'), Js('Saim'), Js('Sarcoph'), Js('Sciur'), Js('Scorp'), Js('Sep'), Js('Serp'), Js('Set'), Js('Silurif'), Js('Sim'), Js('Smil'), Js('Spermoph'), Js('Sph'), Js('Sphen'), Js('Sphyr'), Js('Squal'), Js('Stegost'), Js('Strig'), Js('Strix'), Js('Struth'), Js('Sul'), Js('Suric'), Js('Sus'), Js('Symph'), Js('Sync'), Js('Tachyg'), Js('Talp'), Js('Tam'), Js('Tap'), Js('Tars'), Js('Tax'), Js('Tetraod'), Js('Tetraon'), Js('Teuth'), Js('Threskiorn'), Js('Thyl'), Js('Tragel'), Js('Trem'), Js('Trich'), Js('Trid'), Js('Troch'), Js('Trogl'), Js('Turs'), Js('Tyt'), Js('Uroch'), Js('Uropl'), Js('Urs'), Js('Var'), Js('Vesp'), Js('Viv'), Js('Vomb'), Js('Vulp'), Js('Xenop')]))
var.put('nm4', Js([Js('aatus'), Js('aca'), Js('acal'), Js('achia'), Js('achrus'), Js('acine'), Js('acna'), Js('acus'), Js('ae'), Js('aeidae'), Js('aemus'), Js('aena'), Js('aenidae'), Js('aetes'), Js('affa'), Js('ailurus'), Js('aius'), Js('aja'), Js('ajao'), Js('ale'), Js('alis'), Js('alus'), Js('amalis'), Js('ambulus'), Js('anchiata'), Js('anger'), Js('aninae'), Js('anta'), Js('anthidae'), Js('antulus'), Js('anus'), Js('aon'), Js('aphinae'), Js('aphus'), Js('apra'), Js('aptera'), Js('arctos'), Js('ardus'), Js('arhinus'), Js('ari'), Js('aria'), Js('arodon'), Js('as'), Js('astes'), Js('astos'), Js('ata'), Js('athus'), Js('atidae'), Js('atina'), Js('atus'), Js('aurus'), Js('avia'), Js('easter'), Js('ebus'), Js('echus'), Js('ecta'), Js('edeidae'), Js('eidae'), Js('eirodon'), Js('ela'), Js('eles'), Js('elis'), Js('ella'), Js('ellidae'), Js('elone'), Js('elphis'), Js('elus'), Js('emus'), Js('entes'), Js('entrus'), Js('enus'), Js('eo'), Js('eonidae'), Js('ephalinae'), Js('era'), Js('ercula'), Js('erdo'), Js('eridae'), Js('erix'), Js('erma'), Js('eroptera'), Js('eros'), Js('erra'), Js('erta'), Js('erus'), Js('es'), Js('eter'), Js('eus'), Js('eutes'), Js('ia'), Js('ialis'), Js('ianus'), Js('ias'), Js('icetus'), Js('ichthys'), Js('icola'), Js('ictis'), Js('ida'), Js('idae'), Js('idea'), Js('ifer'), Js('ifera'), Js('iforme'), Js('igator'), Js('iida'), Js('iidae'), Js('iiformes'), Js('ilia'), Js('ilidae'), Js('illa'), Js('illinae'), Js('illus'), Js('ilotis'), Js('ilus'), Js('ina'), Js('inae'), Js('ini'), Js('inia'), Js('inidia'), Js('inoidea'), Js('inus'), Js('io'), Js('ioidea'), Js('iones'), Js('ioninae'), Js('iops'), Js('ipedia'), Js('iri'), Js('irostra'), Js('irus'), Js('is'), Js('iscus'), Js('istoidea'), Js('ithecus'), Js('ithidae'), Js('ithodes'), Js('ithrix'), Js('itis'), Js('ittacus'), Js('ius'), Js('izon'), Js('lossus'), Js('o'), Js('obius'), Js('ocampa'), Js('ocampus'), Js('ocebus'), Js('och'), Js('ochelys'), Js('ochoerus'), Js('odactylus'), Js('odea'), Js('odectus'), Js('odidae'), Js('odon'), Js('odontus'), Js('odytes'), Js('oepus'), Js('oerus'), Js('ogale'), Js('oidea'), Js('oileus'), Js('ois'), Js('olagus'), Js('oma'), Js('omorpha'), Js('on'), Js('ona'), Js('ong'), Js('ongiae'), Js('onia'), Js('onix'), Js('onta'), Js('ontidae'), Js('ontinae'), Js('onyx'), Js('opex'), Js('ophaga'), Js('ophorus'), Js('ophrys'), Js('opidae'), Js('opoda'), Js('oprocta'), Js('ops'), Js('opsis'), Js('optera'), Js('opterus'), Js('opus'), Js('or'), Js('ordata'), Js('orhinus'), Js('oria'), Js('ormes'), Js('orus'), Js('oryx'), Js('osaurus'), Js('osteidae'), Js('ostoma'), Js('otamus'), Js('otherium'), Js('othrix'), Js('otidae'), Js('otriton'), Js('ouatta'), Js('ounga'), Js('ox'), Js('ozoa'), Js('ua'), Js('uarius'), Js('uinus'), Js('uis'), Js('ula'), Js('uma'), Js('ur'), Js('ura'), Js('urga'), Js('uridae'), Js('urnix'), Js('uroidea'), Js('urus'), Js('us'), Js('uta'), Js('uus'), Js('yatis'), Js('ydra'), Js('ydridae'), Js('yini'), Js('ylax'), Js('ylus'), Js('ynchus'), Js('yne'), Js('ynnis'), Js('yon'), Js('ypelma'), Js('yphorus'), Js('ypius'), Js('yptes'), Js('yptula'), Js('yrna'), Js('ysodon'), Js('ystoma'), Js('yura'), Js('yurus')]))
var.put('nm5', Js([Js('Abel'), Js('Acanth'), Js('Acul'), Js('Acutor'), Js('Adel'), Js('Aeg'), Js('Afr'), Js('Agass'), Js('Agil'), Js('Aj'), Js('Al'), Js('Alb'), Js('Albiv'), Js('Alc'), Js('Alism'), Js('Alp'), Js('Alt'), Js('Amblyrh'), Js('Amoyens'), Js('Amphib'), Js('Anat'), Js('Ang'), Js('Antip'), Js('Ar'), Js('Arct'), Js('Arg'), Js('As'), Js('Atr'), Js('Aur'), Js('Axelr'), Js('Bactr'), Js('Barb'), Js('Bengal'), Js('Ber'), Js('Bic'), Js('Bin'), Js('Bint'), Js('Bir'), Js('Bison'), Js('Born'), Js('Brach'), Js('Bub'), Js('Buf'), Js('But'), Js('Cab'), Js('Caff'), Js('Camel'), Js('Camelop'), Js('Cap'), Js('Capuc'), Js('Car'), Js('Carch'), Js('Catesb'), Js('Catt'), Js('Centr'), Js('Chrys'), Js('Cin'), Js('Cirr'), Js('Civ'), Js('Colch'), Js('Conc'), Js('Corb'), Js('Cot'), Js('Crist'), Js('Croc'), Js('Cucull'), Js('Cunic'), Js('Cuv'), Js('Cycl'), Js('Darw'), Js('Delic'), Js('Delph'), Js('Dem'), Js('Derb'), Js('Diehl'), Js('Ding'), Js('Diph'), Js('Domest'), Js('Dors'), Js('Dromed'), Js('Dug'), Js('Electr'), Js('Eleg'), Js('Eq'), Js('Erm'), Js('Escul'), Js('Europ'), Js('Euryc'), Js('Falcon'), Js('Famil'), Js('Fasc'), Js('Fascic'), Js('Fer'), Js('Forst'), Js('Frag'), Js('Franc'), Js('Ful'), Js('Fulg'), Js('Fur'), Js('Fusc'), Js('Gall'), Js('Ganget'), Js('Geoffr'), Js('Gig'), Js('Gigant'), Js('Glam'), Js('Gor'), Js('Grauer'), Js('Grev'), Js('Grunn'), Js('Gryp'), Js('Guian'), Js('Gul'), Js('Habropt'), Js('Harr'), Js('Herc'), Js('Herm'), Js('Hirc'), Js('Hoffm'), Js('Horr'), Js('Humb'), Js('Hydroch'), Js('Ib'), Js('Iguan'), Js('Imm'), Js('Imper'), Js('Ind'), Js('Indr'), Js('Ir'), Js('Jacks'), Js('Johnst'), Js('Jub'), Js('King'), Js('Komod'), Js('Laev'), Js('Lag'), Js('Lagotr'), Js('Lanig'), Js('Larv'), Js('Latr'), Js('Lemm'), Js('Lept'), Js('Less'), Js('Leuc'), Js('Liber'), Js('Lot'), Js('Lum'), Js('Lup'), Js('Lutr'), Js('Lynx'), Js('Ma'), Js('Macroc'), Js('Macul'), Js('Magarh'), Js('Magell'), Js('Mal'), Js('Man'), Js('Mand'), Js('Mandt'), Js('Mar'), Js('Maxill'), Js('Maxim'), Js('Mel'), Js('Melan'), Js('Mend'), Js('Meph'), Js('Mid'), Js('Min'), Js('Monach'), Js('Mul'), Js('Mur'), Js('Muscul'), Js('Nas'), Js('Natt'), Js('Neb'), Js('Nghetinh'), Js('Niv'), Js('Nod'), Js('Novaeangl'), Js('Obscur'), Js('Occid'), Js('Oedip'), Js('Onc'), Js('Or'), Js('Orc'), Js('Orn'), Js('Palm'), Js('Pan'), Js('Pap'), Js('Pard'), Js('Parv'), Js('Pat'), Js('Patag'), Js('Phys'), Js('Pic'), Js('Pict'), Js('Platyrh'), Js('Popul'), Js('Porc'), Js('Prim'), Js('Procyon'), Js('Punct'), Js('Put'), Js('Pyger'), Js('Pygm'), Js('Quagg'), Js('Radiat'), Js('Ratt'), Js('Retic'), Js('Ridib'), Js('Robust'), Js('Ros'), Js('Rosm'), Js('Rubec'), Js('Ruf'), Js('Rupic'), Js('Sap'), Js('Scand'), Js('Scr'), Js('Scyph'), Js('Serv'), Js('Sim'), Js('Sond'), Js('Sph'), Js('Spilog'), Js('Splend'), Js('Str'), Js('Streps'), Js('Sulfur'), Js('Sum'), Js('Sumatr'), Js('Suric'), Js('Susp'), Js('Sylv'), Js('Taj'), Js('Tang'), Js('Tar'), Js('Taur'), Js('Tax'), Js('Tempor'), Js('Tetr'), Js('Tibet'), Js('Tigr'), Js('Toc'), Js('Trid'), Js('Trogl'), Js('Trunc'), Js('Typ'), Js('Undul'), Js('Unic'), Js('Ursin'), Js('Vin'), Js('Vitt'), Js('Vitul'), Js('Viverr'), Js('Volit'), Js('Vulg'), Js('Vulp'), Js('Zebr'), Js('Zerd'), Js('Zyg')]))
var.put('nm6', Js([Js('acal'), Js('actyla'), Js('acu'), Js('aea'), Js('aena'), Js('aeris'), Js('aeus'), Js('agrus'), Js('aica'), Js('aicus'), Js('aja'), Js('al'), Js('alia'), Js('alis'), Js('allus'), Js('alunga'), Js('alus'), Js('ampus'), Js('an'), Js('andus'), Js('ani'), Js('anicus'), Js('ans'), Js('anus'), Js('apra'), Js('ardalis'), Js('aria'), Js('arias'), Js('arinia'), Js('aris'), Js('arius'), Js('arum'), Js('arus'), Js('as'), Js('aspis'), Js('aster'), Js('ata'), Js('aticus'), Js('ator'), Js('atrae'), Js('atta'), Js('atu'), Js('atum'), Js('atus'), Js('aum'), Js('ayanus'), Js('ea'), Js('eatus'), Js('ectum'), Js('eensis'), Js('eiana'), Js('elia'), Js('ellus'), Js('engei'), Js('ens'), Js('ensis'), Js('entalis'), Js('enteus'), Js('entris'), Js('entus'), Js('eo'), Js('ephalus'), Js('er'), Js('era'), Js('ereri'), Js('ereus'), Js('eri'), Js('eria'), Js('ersus'), Js('erus'), Js('es'), Js('etta'), Js('etti'), Js('eus'), Js('iacus'), Js('iae'), Js('ianus'), Js('iaris'), Js('ias'), Js('iatum'), Js('iatus'), Js('iblis'), Js('ica'), Js('iceps'), Js('iceros'), Js('icha'), Js('iculus'), Js('icus'), Js('idus'), Js('iens'), Js('iensis'), Js('ier'), Js('ies'), Js('igenius'), Js('ii'), Js('ilis'), Js('illa'), Js('ilus'), Js('ina'), Js('inea'), Js('inii'), Js('inosa'), Js('inum'), Js('inus'), Js('inx'), Js('iol'), Js('iosa'), Js('is'), Js('isci'), Js('iscus'), Js('isii'), Js('itimus'), Js('itis'), Js('ius'), Js('izii'), Js('o'), Js('ocome'), Js('odes'), Js('odi'), Js('oditus'), Js('odytes'), Js('oensis'), Js('ofa'), Js('oides'), Js('oldti'), Js('oleuca'), Js('olophus'), Js('olor'), Js('on'), Js('onae'), Js('one'), Js('oni'), Js('onicus'), Js('onii'), Js('onyx'), Js('opus'), Js('or'), Js('orius'), Js('ornis'), Js('os'), Js('ostrata'), Js('ostris'), Js('osus'), Js('otata'), Js('otis'), Js('oura'), Js('ouxii'), Js('ox'), Js('oyi'), Js('ozoa'), Js('ua'), Js('uco'), Js('ues'), Js('uinus'), Js('ula'), Js('ularis'), Js('ulata'), Js('ules'), Js('ulosa'), Js('ulus'), Js('um'), Js('undus'), Js('urnix'), Js('urong'), Js('us'), Js('uta'), Js('uus'), Js('yanus'), Js('yi'), Js('ynchos'), Js('ythrus'), Js('yurus')]))
pass
pass


# Add lib to the module scope
scientificCreatures = var.to_python()
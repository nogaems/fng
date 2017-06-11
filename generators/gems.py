__all__ = ['gems']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', (((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('Adamantine'), Js('Amaranth'), Js('Amber'), Js('Amethyst'), Js('Apricot'), Js('Aquamarine'), Js('Azure'), Js('Baby blue'), Js('Beige'), Js('Black'), Js('Blue'), Js('Blue-green'), Js('Blue-violet'), Js('Blush'), Js('Brilliance'), Js('Brilliant'), Js('Bronze'), Js('Brown'), Js('Burgundy'), Js('Byzantium'), Js('Carmine'), Js('Cerise'), Js('Cerulean'), Js('Champagne'), Js('Chartreuse green'), Js('Chocolate'), Js('Cobalt blue'), Js('Coffee'), Js('Copper'), Js('Coral'), Js('Crimson'), Js('Crystalline'), Js('Cyan'), Js('Dazzling'), Js('Desert sand'), Js('Electric blue'), Js('Emerald'), Js('Erin'), Js('Facet'), Js('Flashing'), Js('Gilty'), Js('Gleaming'), Js('Glinting'), Js('Glinty'), Js('Glittering'), Js('Gold'), Js('Gray'), Js('Green'), Js('Harlequin'), Js('Indigo'), Js('Ivory'), Js('Jade'), Js('Jungle green'), Js('Lavender'), Js('Lemon'), Js('Lilac'), Js('Lime'), Js('Magenta'), Js('Magenta rose'), Js('Maroon'), Js('Mauve'), Js('Multifaceted'), Js('Navy blue'), Js('Ocher'), Js('Olive'), Js('Orange'), Js('Orange-red'), Js('Orchid'), Js('Peach'), Js('Pear'), Js('Periwinkle'), Js('Persian blue'), Js('Pink'), Js('Plum'), Js('Prussian blue'), Js('Puce'), Js('Purple'), Js('Raspberry'), Js('Red'), Js('Red-violet'), Js('Rose'), Js('Salmon'), Js('Sangria'), Js('Sapphire'), Js('Scarlet'), Js('Scintillant'), Js('Scintillating'), Js('Silver'), Js('Slate gray'), Js('Sparkling'), Js('Spring bud'), Js('Spring green'), Js('Tan'), Js('Taupe'), Js('Teal'), Js('Turquoise'), Js('Twinkling'), Js('Violet'), Js('Viridian'), Js('White'), Js('Yellow')]))
var.put('nm2', Js([Js('Abe'), Js('Abel'), Js('Aben'), Js('Aber'), Js('Abh'), Js('Abhu'), Js('Abs'), Js('Absw'), Js('Aca'), Js('Acan'), Js('Ach'), Js('Achr'), Js('Act'), Js('Acti'), Js('Acu'), Js('Acum'), Js('Ada'), Js('Adam'), Js('Ade'), Js('Adel'), Js('Adm'), Js('Admo'), Js('Aeg'), Js('Aegi'), Js('Aen'), Js('Aeni'), Js('Aer'), Js('Aeri'), Js('Aeru'), Js('Aes'), Js('Aesc'), Js('Afg'), Js('Afgh'), Js('Afw'), Js('Afwi'), Js('Aga'), Js('Agar'), Js('Agat'), Js('Agr'), Js('Agre'), Js('Agri'), Js('Agu'), Js('Agui'), Js('Ahe'), Js('Ahey'), Js('Ahl'), Js('Ahlf'), Js('Aik'), Js('Aiki'), Js('Ajo'), Js('Ajoi'), Js('Aka'), Js('Akag'), Js('Akat'), Js('Akd'), Js('Akda'), Js('Ake'), Js('Aker'), Js('Aks'), Js('Aksa'), Js('Ala'), Js('Alab'), Js('Alam'), Js('Alar'), Js('Alb'), Js('Albi'), Js('Ald'), Js('Alde'), Js('Ale'), Js('Alex'), Js('Alf'), Js('Alfo'), Js('Alg'), Js('Algo'), Js('Ali'), Js('Alie'), Js('All'), Js('Alla'), Js('Alli'), Js('Allo'), Js('Alm'), Js('Alma'), Js('Als'), Js('Alst'), Js('Alt'), Js('Alta'), Js('Alu'), Js('Alum'), Js('Alun'), Js('Ama'), Js('Amaz'), Js('Amb'), Js('Ambe'), Js('Ambl'), Js('Ame'), Js('Ameg'), Js('Amet'), Js('Amm'), Js('Ammo'), Js('Amo'), Js('Amos'), Js('Amp'), Js('Amph'), Js('Ana'), Js('Anal'), Js('Anap'), Js('Anat'), Js('And'), Js('Anda'), Js('Ande'), Js('Andr'), Js('Ang'), Js('Angl'), Js('Anh'), Js('Anhy'), Js('Ank'), Js('Anke'), Js('Ann'), Js('Anna'), Js('Ano'), Js('Anor'), Js('Ant'), Js('Anth'), Js('Anti'), Js('Antl'), Js('Anto'), Js('Any'), Js('Anyo'), Js('Apa'), Js('Apat'), Js('Apo'), Js('Apop'), Js('Aqu'), Js('Aqua'), Js('Ara'), Js('Arag'), Js('Arc'), Js('Arch'), Js('Arct'), Js('Arcu'), Js('Arf'), Js('Arfv'), Js('Arg'), Js('Arge'), Js('Argu'), Js('Arm'), Js('Arma'), Js('Ars'), Js('Arse'), Js('Art'), Js('Arth'), Js('Arti'), Js('Artr'), Js('Asb'), Js('Asbe'), Js('Ash'), Js('Ashb'), Js('Asi'), Js('Asis'), Js('Ast'), Js('Astr'), Js('Ata'), Js('Atac'), Js('Ath'), Js('Athe'), Js('Aub'), Js('Aube'), Js('Aug'), Js('Auge'), Js('Augi'), Js('Aur'), Js('Auri'), Js('Auro'), Js('Aut'), Js('Autu'), Js('Ava'), Js('Aval'), Js('Ave'), Js('Aven'), Js('Axi'), Js('Axin'), Js('Azu'), Js('Azur'), Js('Bab'), Js('Babi'), Js('Bad'), Js('Badd'), Js('Bao'), Js('Baot'), Js('Bar'), Js('Bari'), Js('Bars'), Js('Bary'), Js('Bas'), Js('Bast'), Js('Bau'), Js('Baux'), Js('Baz'), Js('Bazz'), Js('Bec'), Js('Beck'), Js('Ben'), Js('Beni'), Js('Bens'), Js('Bent'), Js('Ber'), Js('Berr'), Js('Bert'), Js('Bery'), Js('Bio'), Js('Biot'), Js('Bir'), Js('Birn'), Js('Bis'), Js('Bism'), Js('Bix'), Js('Bixb'), Js('Blo'), Js('Blod'), Js('Bloo'), Js('Blos'), Js('Bob'), Js('Bobf'), Js('Boe'), Js('Boeh'), Js('Bor'), Js('Bora'), Js('Born'), Js('Bot'), Js('Botr'), Js('Bou'), Js('Boul'), Js('Bour'), Js('Bow'), Js('Bowe'), Js('Bra'), Js('Bram'), Js('Bras'), Js('Brau'), Js('Braz'), Js('Bre'), Js('Brei'), Js('Brew'), Js('Bri'), Js('Bria'), Js('Bro'), Js('Broc'), Js('Brom'), Js('Bron'), Js('Broo'), Js('Bru'), Js('Bruc'), Js('Brus'), Js('Bud'), Js('Budd'), Js('Bue'), Js('Buer'), Js('Buk'), Js('Buko'), Js('Bul'), Js('Bult'), Js('Byt'), Js('Byto'), Js('Cab'), Js('Cabr'), Js('Cad'), Js('Cadm'), Js('Caf'), Js('Cafe'), Js('Cal'), Js('Cala'), Js('Calc'), Js('Cald'), Js('Cale'), Js('Cali'), Js('Can'), Js('Canc'), Js('Canf'), Js('Car'), Js('Carn'), Js('Caro'), Js('Carr'), Js('Cary'), Js('Cas'), Js('Cass'), Js('Cav'), Js('Cava'), Js('Cel'), Js('Cela'), Js('Cele'), Js('Cels'), Js('Cem'), Js('Ceme'), Js('Cer'), Js('Ceri'), Js('Ceru'), Js('Ces'), Js('Cesb'), Js('Cey'), Js('Ceyl'), Js('Cha'), Js('Chab'), Js('Chal'), Js('Chao'), Js('Chap'), Js('Char'), Js('Chi'), Js('Chil'), Js('Chl'), Js('Chlo'), Js('Cho'), Js('Chon'), Js('Chr'), Js('Chro'), Js('Chry'), Js('Cin'), Js('Cinn'), Js('Cit'), Js('Citr'), Js('Cla'), Js('Clar'), Js('Cle'), Js('Clev'), Js('Cli'), Js('Clin'), Js('Cob'), Js('Coba'), Js('Coe'), Js('Coes'), Js('Cof'), Js('Coff'), Js('Col'), Js('Cole'), Js('Coll'), Js('Colo'), Js('Colt'), Js('Colu'), Js('Com'), Js('Comb'), Js('Con'), Js('Conc'), Js('Conn'), Js('Coo'), Js('Coop'), Js('Cop'), Js('Copa'), Js('Copi'), Js('Copp'), Js('Cor'), Js('Cora'), Js('Cord'), Js('Coru'), Js('Cov'), Js('Cove'), Js('Cre'), Js('Cree'), Js('Cri'), Js('Cris'), Js('Cro'), Js('Croc'), Js('Cron'), Js('Croo'), Js('Cros'), Js('Cry'), Js('Cryo'), Js('Cum'), Js('Cumb'), Js('Cumm'), Js('Cup'), Js('Cupr'), Js('Cya'), Js('Cyan'), Js('Cyl'), Js('Cyli'), Js('Cym'), Js('Cymo'), Js('Cyp'), Js('Cypr'), Js('Dan'), Js('Danb'), Js('Dat'), Js('Dato'), Js('Dav'), Js('Davi'), Js('Daw'), Js('Daws'), Js('Del'), Js('Dele'), Js('Delv'), Js('Dem'), Js('Dema'), Js('Des'), Js('Desc'), Js('Dia'), Js('Diab'), Js('Diad'), Js('Diam'), Js('Dias'), Js('Diat'), Js('Dic'), Js('Dick'), Js('Dig'), Js('Dige'), Js('Dio'), Js('Diop'), Js('Dju'), Js('Djur'), Js('Dol'), Js('Doll'), Js('Dolo'), Js('Dom'), Js('Dome'), Js('Dra'), Js('Drav'), Js('Dum'), Js('Dumo'), Js('Edi'), Js('Edin'), Js('Eka'), Js('Ekan'), Js('Elb'), Js('Elba'), Js('Els'), Js('Elsm'), Js('Eme'), Js('Emer'), Js('Emp'), Js('Empr'), Js('Ena'), Js('Enar'), Js('Ens'), Js('Enst'), Js('Eos'), Js('Eosp'), Js('Epi'), Js('Epid'), Js('Eps'), Js('Epso'), Js('Ery'), Js('Eryt'), Js('Esp'), Js('Espe'), Js('Ett'), Js('Ettr'), Js('Euc'), Js('Euch'), Js('Eucl'), Js('Eucr'), Js('Eud'), Js('Eudi'), Js('Eux'), Js('Euxe'), Js('Fab'), Js('Fabi'), Js('Fas'), Js('Fass'), Js('Fay'), Js('Faya'), Js('Fel'), Js('Feld'), Js('Fer'), Js('Ferb'), Js('Ferg'), Js('Fero'), Js('Ferr'), Js('Fic'), Js('Fich'), Js('Flu'), Js('Fluo'), Js('For'), Js('Forn'), Js('Fors'), Js('Fou'), Js('Foug'), Js('Fra'), Js('Fran'), Js('Fre'), Js('Frei'), Js('Fres'), Js('Fuk'), Js('Fuku'), Js('Gad'), Js('Gado'), Js('Gah'), Js('Gahn'), Js('Gal'), Js('Gala'), Js('Gale'), Js('Gar'), Js('Garn'), Js('Gat'), Js('Gate'), Js('Gay'), Js('Gayl'), Js('Ged'), Js('Geda'), Js('Geh'), Js('Gehl'), Js('Gei'), Js('Geig'), Js('Geo'), Js('Geoc'), Js('Geor'), Js('Ger'), Js('Germ'), Js('Gers'), Js('Gib'), Js('Gibb'), Js('Gis'), Js('Gism'), Js('Gla'), Js('Glau'), Js('Gle'), Js('Gles'), Js('Gme'), Js('Gmel'), Js('Goe'), Js('Goet'), Js('Gol'), Js('Gold'), Js('Gos'), Js('Gosh'), Js('Gosl'), Js('Gra'), Js('Graf'), Js('Grap'), Js('Gre'), Js('Gree'), Js('Grei'), Js('Gro'), Js('Gros'), Js('Gru'), Js('Grun'), Js('Gum'), Js('Gumm'), Js('Gun'), Js('Gunn'), Js('Gyp'), Js('Gyps'), Js('Hac'), Js('Hack'), Js('Hag'), Js('Hagg'), Js('Hai'), Js('Haid'), Js('Hal'), Js('Hali'), Js('Hall'), Js('Halo'), Js('Han'), Js('Hank'), Js('Hap'), Js('Hapk'), Js('Har'), Js('Hard'), Js('Harm'), Js('Hau'), Js('Haue'), Js('Haus'), Js('Hauy'), Js('Haw'), Js('Hawl'), Js('Hax'), Js('Haxo'), Js('Haz'), Js('Haze'), Js('Hea'), Js('Heaz'), Js('Hec'), Js('Hect'), Js('Hed'), Js('Hede'), Js('Hel'), Js('Heli'), Js('Hell'), Js('Hem'), Js('Hema'), Js('Hemi'), Js('Her'), Js('Herb'), Js('Herd'), Js('Hes'), Js('Hess'), Js('Heu'), Js('Heul'), Js('Hib'), Js('Hibo'), Js('Hid'), Js('Hidd'), Js('Hil'), Js('Hilg'), Js('His'), Js('Hisi'), Js('Hol'), Js('Holm'), Js('Hom'), Js('Homi'), Js('Hop'), Js('Hope'), Js('Hor'), Js('Horn'), Js('How'), Js('Howl'), Js('Hue'), Js('Huem'), Js('Hum'), Js('Humi'), Js('Hut'), Js('Hutc'), Js('Hya'), Js('Hyal'), Js('Hyd'), Js('Hydr'), Js('Hyp'), Js('Hype'), Js('Ido'), Js('Idoc'), Js('Idr'), Js('Idri'), Js('Ika'), Js('Ikai'), Js('Ill'), Js('Illi'), Js('Ilm'), Js('Ilme'), Js('Ilv'), Js('Ilva'), Js('Inc'), Js('Incl'), Js('Ind'), Js('Indi'), Js('Iny'), Js('Inyo'), Js('Iod'), Js('Ioda'), Js('Iol'), Js('Ioli'), Js('Jac'), Js('Jaco'), Js('Jad'), Js('Jada'), Js('Jade'), Js('Jam'), Js('Jame'), Js('Jar'), Js('Jaro'), Js('Jas'), Js('Jasp'), Js('Jef'), Js('Jeff'), Js('Jen'), Js('Jenn'), Js('Jer'), Js('Jerr'), Js('Jun'), Js('Juni'), Js('Juo'), Js('Juon'), Js('Jur'), Js('Jurb'), Js('Kaa'), Js('Kaat'), Js('Kad'), Js('Kady'), Js('Kai'), Js('Kain'), Js('Kal'), Js('Kali'), Js('Kals'), Js('Kam'), Js('Kama'), Js('Kamb'), Js('Kamp'), Js('Kan'), Js('Kank'), Js('Kao'), Js('Kaol'), Js('Kas'), Js('Kass'), Js('Kei'), Js('Keil'), Js('Ker'), Js('Kerm'), Js('Kern'), Js('Kero'), Js('Kie'), Js('Kies'), Js('Kin'), Js('Kino'), Js('Kne'), Js('Kneb'), Js('Kno'), Js('Knor'), Js('Kob'), Js('Kobe'), Js('Kog'), Js('Koga'), Js('Kol'), Js('Kolb'), Js('Kor'), Js('Korn'), Js('Kra'), Js('Kran'), Js('Krat'), Js('Kre'), Js('Krem'), Js('Kren'), Js('Kuk'), Js('Kukh'), Js('Kun'), Js('Kunz'), Js('Kut'), Js('Kutn'), Js('Kya'), Js('Kyan'), Js('Lab'), Js('Labr'), Js('Lan'), Js('Lana'), Js('Lang'), Js('Lans'), Js('Lant'), Js('Lap'), Js('Lapi'), Js('Lar'), Js('Lari'), Js('Lau'), Js('Laum'), Js('Laur'), Js('Law'), Js('Laws'), Js('Laz'), Js('Lazu'), Js('Lea'), Js('Lead'), Js('Lec'), Js('Lech'), Js('Leg'), Js('Legr'), Js('Lep'), Js('Lepi'), Js('Leu'), Js('Leuc'), Js('Lev'), Js('Levy'), Js('Lib'), Js('Libe'), Js('Lid'), Js('Lidd'), Js('Lig'), Js('Lign'), Js('Lim'), Js('Limo'), Js('Lin'), Js('Lina'), Js('Lip'), Js('Lips'), Js('Lir'), Js('Liro'), Js('Lit'), Js('Lith'), Js('Liv'), Js('Livi'), Js('Liz'), Js('Liza'), Js('Lod'), Js('Lode'), Js('Lol'), Js('Loll'), Js('Lon'), Js('Lons'), Js('Lop'), Js('Lopa'), Js('Lope'), Js('Lor'), Js('Lora'), Js('Lore'), Js('Lub'), Js('Lubl'), Js('Lud'), Js('Ludw'), Js('Lyo'), Js('Lyon'), Js('Mac'), Js('Macd'), Js('Mack'), Js('Mag'), Js('Magh'), Js('Magn'), Js('Maj'), Js('Majo'), Js('Mal'), Js('Mala'), Js('Man'), Js('Mang'), Js('Mar'), Js('Marc'), Js('Marg'), Js('Mari'), Js('Mas'), Js('Masc'), Js('Mass'), Js('Mat'), Js('Matl'), Js('Mck'), Js('Mcke'), Js('Mee'), Js('Meer'), Js('Mei'), Js('Meio'), Js('Mel'), Js('Mela'), Js('Meli'), Js('Melo'), Js('Men'), Js('Mend'), Js('Mene'), Js('Meni'), Js('Mer'), Js('Merc'), Js('Mes'), Js('Meso'), Js('Mess'), Js('Met'), Js('Meta'), Js('Mia'), Js('Miar'), Js('Mic'), Js('Mica'), Js('Micr'), Js('Mil'), Js('Milk'), Js('Mill'), Js('Mim'), Js('Mime'), Js('Min'), Js('Mini'), Js('Mir'), Js('Mira'), Js('Mix'), Js('Mixi'), Js('Mog'), Js('Moga'), Js('Moh'), Js('Mohi'), Js('Moi'), Js('Mois'), Js('Mol'), Js('Moly'), Js('Mon'), Js('Mona'), Js('Mono'), Js('Mont'), Js('Moo'), Js('Mool'), Js('Moon'), Js('Mor'), Js('Mord'), Js('Morg'), Js('Mot'), Js('Mott'), Js('Motu'), Js('Mul'), Js('Mull'), Js('Mur'), Js('Murd'), Js('Mus'), Js('Musc'), Js('Nab'), Js('Nabe'), Js('Nac'), Js('Nacr'), Js('Nag'), Js('Nagy'), Js('Nah'), Js('Nahc'), Js('Nat'), Js('Nati'), Js('Natr'), Js('Nek'), Js('Nekr'), Js('Nel'), Js('Nele'), Js('Nen'), Js('Nena'), Js('Nep'), Js('Neph'), Js('Nept'), Js('Nic'), Js('Nick'), Js('Nie'), Js('Nied'), Js('Nin'), Js('Nini'), Js('Nio'), Js('Niob'), Js('Nis'), Js('Niss'), Js('Nit'), Js('Nitr'), Js('Non'), Js('Nont'), Js('Nor'), Js('Norm'), Js('Nos'), Js('Nose'), Js('Nsu'), Js('Nsut'), Js('Nye'), Js('Nyer'), Js('Olg'), Js('Olgi'), Js('Oli'), Js('Olig'), Js('Oliv'), Js('Omp'), Js('Omph'), Js('Ony'), Js('Onyx'), Js('Opa'), Js('Opal'), Js('Ord'), Js('Ordo'), Js('Ore'), Js('Oreg'), Js('Orp'), Js('Orpi'), Js('Ort'), Js('Orth'), Js('Osa'), Js('Osar'), Js('Osm'), Js('Osmi'), Js('Osu'), Js('Osum'), Js('Ota'), Js('Otav'), Js('Ott'), Js('Ottr'), Js('Ove'), Js('Over'), Js('Pai'), Js('Pain'), Js('Pal'), Js('Pala'), Js('Pall'), Js('Paly'), Js('Pan'), Js('Pang'), Js('Pap'), Js('Papa'), Js('Par'), Js('Para'), Js('Pari'), Js('Part'), Js('Pas'), Js('Pasc'), Js('Pea'), Js('Pear'), Js('Pec'), Js('Peco'), Js('Pect'), Js('Pen'), Js('Pent'), Js('Per'), Js('Peri'), Js('Perl'), Js('Pero'), Js('Pet'), Js('Peta'), Js('Petz'), Js('Pez'), Js('Pezz'), Js('Pha'), Js('Phar'), Js('Phe'), Js('Phen'), Js('Phi'), Js('Phil'), Js('Phl'), Js('Phlo'), Js('Pho'), Js('Phoe'), Js('Phos'), Js('Pig'), Js('Pige'), Js('Pit'), Js('Pitc'), Js('Pla'), Js('Plag'), Js('Plat'), Js('Ple'), Js('Ples'), Js('Pol'), Js('Pola'), Js('Poll'), Js('Poly'), Js('Pot'), Js('Pota'), Js('Pou'), Js('Poud'), Js('Pow'), Js('Powe'), Js('Pra'), Js('Pras'), Js('Pre'), Js('Preh'), Js('Pro'), Js('Prou'), Js('Psi'), Js('Psil'), Js('Pum'), Js('Pumi'), Js('Pump'), Js('Pur'), Js('Purp'), Js('Pyr'), Js('Pyra'), Js('Pyri'), Js('Pyro'), Js('Pyrr'), Js('Qua'), Js('Quah'), Js('Quar'), Js('Que'), Js('Quen'), Js('Ram'), Js('Ramb'), Js('Ramm'), Js('Rap'), Js('Rapi'), Js('Ras'), Js('Rasp'), Js('Rea'), Js('Real'), Js('Rei'), Js('Reis'), Js('Ren'), Js('Reni'), Js('Rhe'), Js('Rhen'), Js('Rho'), Js('Rhod'), Js('Rhom'), Js('Ric'), Js('Rick'), Js('Rie'), Js('Rieb'), Js('Rob'), Js('Robe'), Js('Roc'), Js('Rock'), Js('Rom'), Js('Roma'), Js('Ros'), Js('Rosa'), Js('Rosc'), Js('Rose'), Js('Rou'), Js('Roum'), Js('Rout'), Js('Rub'), Js('Rube'), Js('Ruby'), Js('Rui'), Js('Ruiz'), Js('Rut'), Js('Ruth'), Js('Ruti'), Js('Ryn'), Js('Ryne'), Js('Sab'), Js('Saba'), Js('Sabi'), Js('Saf'), Js('Saff'), Js('Sal'), Js('Sali'), Js('Sam'), Js('Sama'), Js('Sams'), Js('San'), Js('Sanb'), Js('Sane'), Js('Sani'), Js('Sant'), Js('Sap'), Js('Sapo'), Js('Sapp'), Js('Sar'), Js('Sard'), Js('Sark'), Js('Sas'), Js('Sass'), Js('Sat'), Js('Sati'), Js('Sau'), Js('Sauc'), Js('Sca'), Js('Scap'), Js('Sch'), Js('Sche'), Js('Scho'), Js('Schr'), Js('Schw'), Js('Sco'), Js('Scol'), Js('Scor'), Js('Sea'), Js('Seam'), Js('See'), Js('Seel'), Js('Seg'), Js('Sege'), Js('Sek'), Js('Seka'), Js('Sel'), Js('Sele'), Js('Seli'), Js('Sell'), Js('Sen'), Js('Sena'), Js('Sep'), Js('Sepi'), Js('Ser'), Js('Sera'), Js('Serp'), Js('Sha'), Js('Shat'), Js('Shi'), Js('Shig'), Js('Shu'), Js('Shun'), Js('Sid'), Js('Side'), Js('Sie'), Js('Sieg'), Js('Sil'), Js('Sili'), Js('Sill'), Js('Silv'), Js('Sim'), Js('Sime'), Js('Simo'), Js('Sin'), Js('Sink'), Js('Sku'), Js('Skut'), Js('Sma'), Js('Smal'), Js('Sme'), Js('Smec'), Js('Smi'), Js('Smit'), Js('Smo'), Js('Smok'), Js('Soa'), Js('Soap'), Js('Sod'), Js('Soda'), Js('Son'), Js('Sono'), Js('Spe'), Js('Spec'), Js('Sper'), Js('Spes'), Js('Sph'), Js('Spha'), Js('Sphe'), Js('Spi'), Js('Spin'), Js('Spo'), Js('Spod'), Js('Spu'), Js('Spur'), Js('Sta'), Js('Stan'), Js('Stau'), Js('Ste'), Js('Stea'), Js('Step'), Js('Sti'), Js('Stib'), Js('Stic'), Js('Stil'), Js('Sto'), Js('Stol'), Js('Str'), Js('Stro'), Js('Stru'), Js('Stu'), Js('Stud'), Js('Sug'), Js('Sugi'), Js('Sul'), Js('Sulf'), Js('Sun'), Js('Suns'), Js('Sur'), Js('Surs'), Js('Sus'), Js('Suss'), Js('Syl'), Js('Sylv'), Js('Tac'), Js('Tach'), Js('Tae'), Js('Taen'), Js('Tal'), Js('Talc'), Js('Tan'), Js('Tant'), Js('Tanz'), Js('Tar'), Js('Tara'), Js('Tarb'), Js('Tas'), Js('Tash'), Js('Tau'), Js('Taus'), Js('Tea'), Js('Teal'), Js('Tel'), Js('Tell'), Js('Tem'), Js('Tema'), Js('Ten'), Js('Tenn'), Js('Teno'), Js('Tep'), Js('Teph'), Js('Ter'), Js('Terl'), Js('Teru'), Js('Tet'), Js('Tetr'), Js('Tha'), Js('Thau'), Js('The'), Js('Then'), Js('Tho'), Js('Thom'), Js('Thor'), Js('Thu'), Js('Thul'), Js('Tie'), Js('Tiem'), Js('Tig'), Js('Tige'), Js('Tin'), Js('Tinc'), Js('Tit'), Js('Tita'), Js('Tob'), Js('Tobe'), Js('Tod'), Js('Todo'), Js('Tok'), Js('Toky'), Js('Top'), Js('Topa'), Js('Tor'), Js('Torb'), Js('Tou'), Js('Tour'), Js('Tra'), Js('Trav'), Js('Tre'), Js('Trem'), Js('Trev'), Js('Tri'), Js('Trid'), Js('Trip'), Js('Tro'), Js('Tron'), Js('Tsa'), Js('Tsav'), Js('Tsc'), Js('Tsch'), Js('Tug'), Js('Tugt'), Js('Tun'), Js('Tung'), Js('Tur'), Js('Turq'), Js('Tus'), Js('Tusi'), Js('Tyr'), Js('Tyro'), Js('Tyu'), Js('Tyuy'), Js('Uch'), Js('Uchu'), Js('Ukl'), Js('Uklo'), Js('Ule'), Js('Ulex'), Js('Ull'), Js('Ullm'), Js('Ult'), Js('Ultr'), Js('Ulv'), Js('Ulvo'), Js('Uma'), Js('Uman'), Js('Umb'), Js('Umbe'), Js('Umbi'), Js('Una'), Js('Unak'), Js('Upa'), Js('Upal'), Js('Ura'), Js('Ural'), Js('Uran'), Js('Uva'), Js('Uvar'), Js('Vae'), Js('Vaes'), Js('Val'), Js('Vale'), Js('Van'), Js('Vana'), Js('Var'), Js('Vari'), Js('Vat'), Js('Vate'), Js('Vau'), Js('Vauq'), Js('Vaux'), Js('Ver'), Js('Verd'), Js('Verm'), Js('Ves'), Js('Vesu'), Js('Vil'), Js('Vill'), Js('Vio'), Js('Viol'), Js('Viv'), Js('Vivi'), Js('Vol'), Js('Volb'), Js('Wad'), Js('Wag'), Js('Wagn'), Js('War'), Js('Ward'), Js('Wari'), Js('Warw'), Js('Was'), Js('Wass'), Js('Wav'), Js('Wave'), Js('Wed'), Js('Wedd'), Js('Wei'), Js('Weil'), Js('Weis'), Js('Wel'), Js('Welo'), Js('Whe'), Js('Whew'), Js('Whi'), Js('Whit'), Js('Wil'), Js('Will'), Js('Wilu'), Js('Wit'), Js('With'), Js('Wol'), Js('Wolf'), Js('Woll'), Js('Wul'), Js('Wulf'), Js('Wur'), Js('Wurt'), Js('Wya'), Js('Wyar'), Js('Xen'), Js('Xeno'), Js('Xif'), Js('Xife'), Js('Xon'), Js('Xono'), Js('Ytt'), Js('Yttr'), Js('Zab'), Js('Zabu'), Js('Zac'), Js('Zacc'), Js('Zah'), Js('Zahe'), Js('Zaj'), Js('Zaja'), Js('Zak'), Js('Zakh'), Js('Zan'), Js('Zana'), Js('Zar'), Js('Zara'), Js('Zek'), Js('Zekt'), Js('Zeo'), Js('Zeol'), Js('Zha'), Js('Zhan'), Js('Zhar'), Js('Zho'), Js('Zhon'), Js('Zie'), Js('Zies'), Js('Zim'), Js('Zimb'), Js('Zin'), Js('Zina'), Js('Zinc'), Js('Zink'), Js('Zinn'), Js('Zip'), Js('Zipp'), Js('Zir'), Js('Zirc'), Js('Zirk'), Js('Zoi'), Js('Zois'), Js('Zul'), Js('Zult'), Js('Zun'), Js('Zuny')]))
var.put('nm3', Js([Js('a'), Js('abar'), Js('abergite'), Js('abilite'), Js('abogdanite'), Js('abweite'), Js('achite'), Js('achrysotile'), Js('acinnabarite'), Js('acite'), Js('acolite'), Js('acyite'), Js('adinite'), Js('adite'), Js('adium'), Js('adkevichite'), Js('adonite'), Js('adorite'), Js('adymite'), Js('agamite'), Js('agite'), Js('agnaite'), Js('agnite'), Js('agoite'), Js('agonite'), Js('ahedrite'), Js('aiba'), Js('aite'), Js('akiite'), Js('akite'), Js('al'), Js('alaite'), Js('alcolite'), Js('alconite'), Js('ald'), Js('aldaite'), Js('alerite'), Js('alite'), Js('allite'), Js('alsite'), Js('altite'), Js('alusite'), Js('alyte'), Js('amarine'), Js('amite'), Js('amunite'), Js('an'), Js('andine'), Js('andite'), Js('andrite'), Js('anechite'), Js('aneite'), Js('angerite'), Js('aninaite'), Js('anite'), Js('ankasite'), Js('annite'), Js('anocolumbite'), Js('anotantalite'), Js('anowodginite'), Js('ansite'), Js('antite'), Js('antoid'), Js('anvesuvianite'), Js('apacaite'), Js('apite'), Js('ardite'), Js('arealgar'), Js('arenkoite'), Js('arge'), Js('argyrite'), Js('aritasite'), Js('arite'), Js('arkite'), Js('arkoite'), Js('armontite'), Js('arovite'), Js('arskite'), Js('artite'), Js('asclarkite'), Js('ase'), Js('aseite'), Js('asite'), Js('asovite'), Js('assite'), Js('assium'), Js('aster'), Js('astonite'), Js('atelierite'), Js('atierite'), Js('atine'), Js('atite'), Js('atorbernite'), Js('auxite'), Js('averite'), Js('ax'), Js('axite'), Js('az'), Js('azite'), Js('azziite'), Js('babweite'), Js('baldaite'), Js('bandite'), Js('banite'), Js('basite'), Js('baster'), Js('bazite'), Js('bbiite'), Js('bdenite'), Js('beckite'), Js('beinite'), Js('beite'), Js('belite'), Js('bergite'), Js('berite'), Js('berlandite'), Js('bernite'), Js('bertsmithite'), Js('bilite'), Js('bisite'), Js('bite'), Js('blende'), Js('bnite'), Js('boclase'), Js('bogdanite'), Js('boleite'), Js('bornite'), Js('borthite'), Js('bronite'), Js('bsite'), Js('burite'), Js('burtonite'), Js('buttite'), Js('byite'), Js('c'), Js('cagnaite'), Js('cagnite'), Js('calconite'), Js('camite'), Js('canthite'), Js('casite'), Js('cate'), Js('cchacuaite'), Js('cedony'), Js('ch pearl'), Js('chalcite'), Js('chantite'), Js('chblende'), Js('chikhite'), Js('chilite'), Js('chinsonite'), Js('chite'), Js('chlore'), Js('chrysotile'), Js('chtite'), Js('chynite'), Js('cidolite'), Js('cinnabarite'), Js('cite'), Js('cite '), Js('ckeite'), Js('clase'), Js('clasite'), Js('clipscombite'), Js('cloizite'), Js('cobotryogen'), Js('cochroite'), Js('cochromite'), Js('cocite'), Js('codot'), Js('coelite'), Js('coite'), Js('colite'), Js('combite'), Js('con'), Js('conite'), Js('conolite'), Js('cophane'), Js('cophanite'), Js('cophoenicite'), Js('cophyllite'), Js('copyrite'), Js('covite'), Js('crase'), Js('crinite'), Js('cronite'), Js('ctite'), Js('ctrolite'), Js('cupride'), Js('cury'), Js('cyite'), Js('d'), Js('daleite'), Js('dcreekite'), Js('deleyite'), Js('dellite'), Js('denite'), Js('derite'), Js('dermayrite'), Js('deroite'), Js('dhillite'), Js('dicoatite'), Js('dierite'), Js('dine'), Js('dingerite'), Js('dingtonite'), Js('dinite'), Js('dite'), Js('dium'), Js('dkevichite'), Js('dochite'), Js('dochrosite'), Js('docrocite'), Js('dolite'), Js('donaldite'), Js('donite'), Js('donyx'), Js('dorffite'), Js('dot'), Js('dote'), Js('dozite'), Js('drenite'), Js('dretteite'), Js('drite'), Js('drodite'), Js('dspar'), Js('dspathoid'), Js('dstone'), Js('dtite'), Js('dumene'), Js('dymite'), Js('dystonite'), Js('e'), Js('ean'), Js('ecite'), Js('eckite'), Js('edite'), Js('edonite'), Js('edsonite'), Js('eelite'), Js('eghinite'), Js('ehouseite'), Js('eibersite'), Js('eite'), Js('el'), Js('eldite'), Js('elerite'), Js('eleyite'), Js('elian'), Js('eline'), Js('elite'), Js('ellite'), Js('ellyite'), Js('elsbergite'), Js('elveyite'), Js('emanite'), Js('emite'), Js('ena'), Js('enbergite'), Js('ene'), Js('eneite'), Js('engite'), Js('enic'), Js('enicochroite'), Js('enite'), Js('enium'), Js('enockite'), Js('enoclasite'), Js('enopyrite'), Js('enovite'), Js('entine'), Js('entinite'), Js('entite'), Js('enzenite'), Js('eolite'), Js('eonite'), Js('epite'), Js('er'), Js('ereite'), Js('ereye'), Js('erfordine'), Js('ergite'), Js('ergusonite'), Js('erite'), Js('erlandite'), Js('ermanite'), Js('ermayrite'), Js('ermigite'), Js('ermorite'), Js('ernite'), Js('erocobaltite'), Js('eroite'), Js('erotil'), Js('ersite'), Js('ersonite'), Js('ersthene'), Js('ertine'), Js('ertite'), Js('ertmannite'), Js('ertsite'), Js('ertsmithite'), Js('ertyite'), Js('erupine'), Js('esia'), Js('esine'), Js('esioferrite'), Js('esite'), Js('eslebenite'), Js('esonite'), Js('essite'), Js('estine'), Js('estone'), Js('estos'), Js('et'), Js('ethenite'), Js('etite'), Js('ettite'), Js('exite'), Js('eyite'), Js('eykite'), Js('ezite'), Js('feldite'), Js('fenite'), Js('fergusonite'), Js('fersonite'), Js('fieldite'), Js('finite'), Js('fite'), Js('florite'), Js('fonteinite'), Js('fordite'), Js('fornite'), Js('framite'), Js('ftonite'), Js('fur'), Js('gaite'), Js('gamite'), Js('ganeite'), Js('ganite'), Js('ganocolumbite'), Js('ganotantalite'), Js('ganvesuvianite'), Js('gar'), Js('gardite'), Js('garitasite'), Js('garite'), Js('gbeinite'), Js('genite'), Js('gerite'), Js('gerobinsonite'), Js('gertyite'), Js('ggite'), Js('ghengite'), Js('ghinite'), Js('ghuacerite'), Js('gioclase'), Js('gite'), Js('gmannite'), Js('gmatite'), Js('goclase'), Js('goite'), Js('gonite'), Js('gopite'), Js('gorite'), Js('gorskite'), Js('gstite'), Js('gtonite'), Js('guite'), Js('gusonite'), Js('gyrite'), Js('h pearl'), Js('hacite'), Js('halite'), Js('hanite'), Js('hantite'), Js('harenkoite'), Js('harge'), Js('harovite'), Js('hatelierite'), Js('hauite'), Js('hblende'), Js('heite'), Js('heline'), Js('hemite'), Js('henite'), Js('henium'), Js('herfordine'), Js('herite'), Js('hermigite'), Js('hibole'), Js('hierite'), Js('hillite'), Js('hinite'), Js('hinsonite'), Js('hiophilite'), Js('hire'), Js('hirine'), Js('hite'), Js('hmarine'), Js('hmite'), Js('hnite'), Js('hochrysotile'), Js('hoclase'), Js('hog'), Js('hophyllite'), Js('horite'), Js('hotite'), Js('houseite'), Js('hrite'), Js('hroite'), Js('hsonite'), Js('htelite'), Js('htite'), Js('hurite'), Js('hwater pearl'), Js('hydrocalcite'), Js('hyhydrite'), Js('hylite'), Js('hyllite'), Js('hynite'), Js('hyst'), Js('ialaite'), Js('ialite'), Js('ialyte'), Js('ian'), Js('ianite'), Js('iapite'), Js('iaumite'), Js('iba'), Js('ibergite'), Js('ibole'), Js('icate'), Js('icellite'), Js('ichalcite'), Js('icite'), Js('ickite'), Js('iclase'), Js('icoatite'), Js('icolite'), Js('icot'), Js('icrete'), Js('iculite'), Js('icupride'), Js('idcreekite'), Js('idine'), Js('idite'), Js('idocrocite'), Js('idolite'), Js('idot'), Js('ieite'), Js('ieldite'), Js('ierite'), Js('ieslebenite'), Js('ifornite'), Js('igerite'), Js('igite'), Js('igmannite'), Js('igmatite'), Js('igorite'), Js('ihydrite'), Js('iite'), Js('ikahnite'), Js('ilarite'), Js('ile'), Js('ilianite'), Js('ilite'), Js('illite'), Js('imanite'), Js('imar'), Js('iment'), Js('imony'), Js('imorphite'), Js('inaite'), Js('inawite'), Js('indrite'), Js('ine'), Js('ingerite'), Js('ingite'), Js('ingstonite'), Js('ingtonite'), Js('inguaite'), Js('inierite'), Js('ininite'), Js('inite'), Js('inium'), Js('inolite'), Js('insite'), Js('inspar'), Js('inum'), Js('ioclase'), Js('iodor'), Js('iolite'), Js('ionite'), Js('iophilite'), Js('iotite'), Js('iotrope'), Js('iposite'), Js('irine'), Js('is'), Js('iscite'), Js('isite'), Js('itaenite'), Js('ite'), Js('ite '), Js('iterite'), Js('ithauptite'), Js('itoite'), Js('ium'), Js('ive'), Js('iz'), Js('izawaite'), Js('k'), Js('kahnite'), Js('kankasite'), Js('kardite'), Js('keite'), Js('kel'), Js('keline'), Js('kelite'), Js('kenite'), Js('kerite'), Js('kesite'), Js('khawthorneite'), Js('kinawite'), Js('kinite'), Js('kite'), Js('klinite'), Js('kmanite'), Js('koreaite'), Js('ksite'), Js('ky'), Js('l'), Js('lacolloite'), Js('ladium'), Js('laite'), Js('landite'), Js('langerite'), Js('larite'), Js('lase'), Js('laseite'), Js('lastonite'), Js('lbite'), Js('lcanthite'), Js('lcedony'), Js('lcite'), Js('lcocite'), Js('lcolite'), Js('lcopyrite'), Js('ldrenite'), Js('le'), Js('lecite'), Js('leite'), Js('lemite'), Js('lenite'), Js('lerite'), Js('lesite'), Js('lewoodite'), Js('leyite'), Js('lgar'), Js('lhauite'), Js('li'), Js('liaumite'), Js('ligerite'), Js('limanite'), Js('ling'), Js('lingite'), Js('linguaite'), Js('linite'), Js('linsite'), Js('lipscombite'), Js('lipsite'), Js('lite'), Js('llacolloite'), Js('lleite'), Js('llipsite'), Js('llite'), Js('llonite'), Js('lockite'), Js('loidite'), Js('loizite'), Js('lomelane'), Js('lonite'), Js('looite'), Js('lophane'), Js('lorite'), Js('loysite'), Js('lsite'), Js('lsonite'), Js('ltite'), Js('lucite'), Js('lurite'), Js('lurium'), Js('lurobismuthite'), Js('lusion'), Js('lusite'), Js('lussite'), Js('lveyite'), Js('lybite'), Js('lyerite'), Js('lygonite'), Js('lzite'), Js('m'), Js('macosiderite'), Js('maline'), Js('mallite'), Js('mandite'), Js('manite'), Js('mannite'), Js('mar'), Js('margyrite'), Js('marine'), Js('masclarkite'), Js('masite'), Js('mbite'), Js('mboclase'), Js('mellite'), Js('melsbergite'), Js('ment'), Js('mersite'), Js('mesite'), Js('meyerite'), Js('miculite'), Js('milite'), Js('mingtonite'), Js('minite'), Js('minium'), Js('mite'), Js('mium'), Js('mmallite'), Js('molite'), Js('mond'), Js('mondine'), Js('montite'), Js('mony'), Js('moreite'), Js('morillonite'), Js('morphite'), Js('mosite'), Js('motome'), Js('mquistite'), Js('msenolite'), Js('msite'), Js('mulite'), Js('muth'), Js('muthinite'), Js('na'), Js('nabar'), Js('nacite'), Js('naite'), Js('nakiite'), Js('nakite'), Js('nallite'), Js('nantite'), Js('nardite'), Js('nasite'), Js('nathyite'), Js('nbergite'), Js('nblende'), Js('nckeite'), Js('ndine'), Js('ndite'), Js('ndrite'), Js('ndrodite'), Js('ndum'), Js('ne'), Js('nechite'), Js('neite'), Js('nel'), Js('nelian'), Js('nellite'), Js('nerite'), Js('nerupine'), Js('nesia'), Js('nesioferrite'), Js('nesite'), Js('nessite'), Js('net'), Js('netite'), Js('nezite'), Js('ngerite'), Js('nghengite'), Js('nghuacerite'), Js('ngite'), Js('ngstonite'), Js('ngtonite'), Js('nic'), Js('nicochroite'), Js('nierite'), Js('niite'), Js('ninaite'), Js('ningite'), Js('ninite'), Js('nite'), Js('nium'), Js('nkhawthorneite'), Js('nklinite'), Js('nnerite'), Js('nniite'), Js('nnite'), Js('nochrysotile'), Js('nockite'), Js('noclase'), Js('noclasite'), Js('nogen'), Js('nohedrite'), Js('nohorite'), Js('nohumite'), Js('nolite'), Js('nonite'), Js('nophane'), Js('nopilite'), Js('noptilolite'), Js('nopyrite'), Js('notite'), Js('notrichite'), Js('novite'), Js('nowodginite'), Js('nozoisite'), Js('nsite'), Js('nskovite'), Js('nspar'), Js('nstedtite'), Js('nstone'), Js('nthite'), Js('ntianite'), Js('ntienite'), Js('ntinite'), Js('ntite'), Js('ntoid'), Js('ntonite'), Js('nturine'), Js('ntzite'), Js('nwaldite'), Js('nzenite'), Js('nzite'), Js('o'), Js('obbiite'), Js('obotryogen'), Js('obsite'), Js('ocerite'), Js('ochite'), Js('ochlore'), Js('ochromite'), Js('ochrosite'), Js('ochrysotile'), Js('ochvilite'), Js('ockite'), Js('oclase'), Js('oclasite'), Js('ocline'), Js('ocolumbite'), Js('oconite'), Js('odite'), Js('odonite'), Js('odor'), Js('odstone'), Js('oeite'), Js('oelite'), Js('oepite'), Js('og'), Js('oganite'), Js('ogen'), Js('ogopite'), Js('ogrossular'), Js('ohedrite'), Js('ohorite'), Js('ohortonolite'), Js('ohumite'), Js('ohydrocalcite'), Js('oite'), Js('okesite'), Js('okite'), Js('oleite'), Js('olinite'), Js('olite'), Js('ollite'), Js('olusite'), Js('omagnesite'), Js('omelane'), Js('omeyerite'), Js('omite'), Js('omium'), Js('omorphite'), Js('on'), Js('onaldite'), Js('ond'), Js('ondine'), Js('onellite'), Js('onezite'), Js('onite'), Js('onolite'), Js('onskovite'), Js('ontianite'), Js('ontite'), Js('onyx'), Js('ooite'), Js('ope'), Js('opericlase'), Js('ophane'), Js('ophanite'), Js('ophilite'), Js('ophoenicite'), Js('ophyllite'), Js('opilite'), Js('optilolite'), Js('oradoite'), Js('orapatite'), Js('orargyrite'), Js('orastrolite'), Js('orcaphite'), Js('oreite'), Js('oriate'), Js('orichterite'), Js('orite'), Js('oritoid'), Js('orl'), Js('ornite'), Js('orokite'), Js('orsite'), Js('orspar'), Js('orthite'), Js('ortierite'), Js('osewichite'), Js('osite'), Js('ospinel'), Js('ostibite'), Js('otantalite'), Js('ote'), Js('otime'), Js('otite'), Js('otlite'), Js('otome'), Js('otrichite'), Js('otrope'), Js('ottaite'), Js('ovite'), Js('ovskite'), Js('ovskyite'), Js('ownite'), Js('oxene'), Js('oxferroite'), Js('oxyhyte'), Js('oxylapatite'), Js('oysite'), Js('ozincite'), Js('ozite'), Js('ozoisite'), Js('ozonite'), Js('pacaite'), Js('paite'), Js('pe'), Js('peite'), Js('pellyite'), Js('pentine'), Js('per'), Js('perite'), Js('pfite'), Js('phane'), Js('phanite'), Js('phire'), Js('phirine'), Js('phite'), Js('phophyllite'), Js('phorite'), Js('phylite'), Js('phyllite'), Js('pite'), Js('plite'), Js('ploidite'), Js('pmanite'), Js('polite'), Js('pore'), Js('posite'), Js('pside'), Js('pstone'), Js('ptase'), Js('puhyite'), Js('purite'), Js('quelinite'), Js('quistite'), Js('quoise'), Js('r'), Js('radite'), Js('radoite'), Js('radorite'), Js('radymite'), Js('rahedrite'), Js('rald'), Js('ramarine'), Js('ramite'), Js('randite'), Js('rapatite'), Js('rargyrite'), Js('rase'), Js('rasovite'), Js('rastrolite'), Js('ratine'), Js('rcaphite'), Js('rchikhite'), Js('rdite'), Js('re'), Js('realgar'), Js('reibersite'), Js('relite'), Js('rereite'), Js('ressite'), Js('retteite'), Js('reye'), Js('rgerite'), Js('rgerobinsonite'), Js('rgite'), Js('rgyrite'), Js('rhotite'), Js('rialite'), Js('rianite'), Js('riate'), Js('richterite'), Js('ricrete'), Js('rierite'), Js('rihydrite'), Js('riite'), Js('rine'), Js('ringite'), Js('rinite'), Js('rite'), Js('ritoid'), Js('rizawaite'), Js('rkeite'), Js('rkite'), Js('rkoite'), Js('rl'), Js('rleite'), Js('rmacosiderite'), Js('rmaline'), Js('rmanite'), Js('rmontite'), Js('rmorite'), Js('rnathyite'), Js('rnonite'), Js('ro'), Js('rocerite'), Js('rocline'), Js('rocobaltite'), Js('rocolumbite'), Js('rodite'), Js('roeite'), Js('rogrossular'), Js('rohortonolite'), Js('roite'), Js('rokite'), Js('rolite'), Js('rollite'), Js('romagnesite'), Js('ron'), Js('ronite'), Js('ropericlase'), Js('rophilite'), Js('rophyllite'), Js('rotantalite'), Js('rotil'), Js('rovite'), Js('roxylapatite'), Js('rozincite'), Js('rringite'), Js('rrite'), Js('rrylite'), Js('rschaum'), Js('rsite'), Js('rskite'), Js('rsonite'), Js('rspar'), Js('rsthene'), Js('rthite'), Js('rthoclase'), Js('rtierite'), Js('rtite'), Js('rtsite'), Js('rtveitite'), Js('rtz'), Js('ry'), Js('rygibbsite'), Js('ryite'), Js('rylite'), Js('ryogen'), Js('ryptite'), Js('rzalite'), Js('s'), Js('saite'), Js('sanite'), Js('sartite'), Js('sassite'), Js('schaum'), Js('scite'), Js('scombite'), Js('sdaleite'), Js('sdorffite'), Js('selite'), Js('senolite'), Js('seolite'), Js('serite'), Js('sewichite'), Js('sexite'), Js('sfordite'), Js('sgenite'), Js('shite'), Js('shwater pearl'), Js('sian'), Js('sicot'), Js('side'), Js('silite'), Js('sine'), Js('siolite'), Js('site'), Js('siterite'), Js('sling'), Js('smannite'), Js('soberyl'), Js('socolla'), Js('solite'), Js('sonite'), Js('soprase'), Js('sotile'), Js('spar'), Js('spathoid'), Js('sphophyllite'), Js('sphorite'), Js('spinel'), Js('spore'), Js('ssanite'), Js('ssartite'), Js('ssite'), Js('ssium'), Js('ssular'), Js('stedtite'), Js('sterite'), Js('stibite'), Js('stine'), Js('stite'), Js('stobalite'), Js('stone'), Js('stonite'), Js('stos'), Js('stowite'), Js('sular'), Js('sum'), Js('taenite'), Js('tagonite'), Js('talite'), Js('tan'), Js('tanite'), Js('tase'), Js('tatite'), Js('te'), Js('telite'), Js('terite'), Js('terudite'), Js('tfonteinite'), Js('thanite'), Js('thauptite'), Js('theite'), Js('thenite'), Js('thierite'), Js('thite'), Js('thoclase'), Js('thrite'), Js('thsonite'), Js('thyst'), Js('tialaite'), Js('ticellite'), Js('tienite'), Js('tierite'), Js('time'), Js('tinum'), Js('tite'), Js('tlandite'), Js('tlite'), Js('tlockite'), Js('tmorillonite'), Js('tnasite'), Js('tobalite'), Js('tocalcite'), Js('tochvilite'), Js('toite'), Js('tolite'), Js('tomite'), Js('tone'), Js('tonite'), Js('torbernite'), Js('toreite'), Js('torite'), Js('towite'), Js('tramite'), Js('trandite'), Js('trichite'), Js('trine'), Js('trolite'), Js('tronite'), Js('tterudite'), Js('ttite'), Js('ttuckite'), Js('tuckite'), Js('tunite'), Js('tupite'), Js('turine'), Js('tveitite'), Js('tz'), Js('tzerite'), Js('tzite'), Js('uberite'), Js('ubisite'), Js('ucchacuaite'), Js('uchilite'), Js('ucite'), Js('ucochroite'), Js('ucodot'), Js('uconite'), Js('ucophane'), Js('uelinite'), Js('uggite'), Js('ugite'), Js('uhyite'), Js('uite'), Js('ukoreaite'), Js('uli'), Js('ulite'), Js('um'), Js('umasite'), Js('umbite'), Js('umene'), Js('undum'), Js('unite'), Js('uoise'), Js('upite'), Js('ur'), Js('urite'), Js('urium'), Js('urmbachite'), Js('urobismuthite'), Js('urolite'), Js('urtonite'), Js('ury'), Js('usion'), Js('usonite'), Js('ussite'), Js('ustite'), Js('uth'), Js('uthinite'), Js('utite'), Js('uttite'), Js('uvianite'), Js('uvite'), Js('uyelite'), Js('vanite'), Js('vauxite'), Js('ve'), Js('vedsonite'), Js('veite'), Js('venite'), Js('ver'), Js('verite'), Js('vertine'), Js('vianite'), Js('vine'), Js('vite'), Js('vorite'), Js('vskite'), Js('vskyite'), Js('waldite'), Js('wellite'), Js('wertmannite'), Js('wickite'), Js('wigite'), Js('wnite'), Js('wsterite'), Js('wurmbachite'), Js('x'), Js('xandrite'), Js('xene'), Js('xferroite'), Js('xite'), Js('xyhyte'), Js('y'), Js('yagite'), Js('yamunite'), Js('ybasite'), Js('ybdenite'), Js('ybite'), Js('ycrase'), Js('ydrite'), Js('ydymite'), Js('yelite'), Js('yerite'), Js('ygibbsite'), Js('ygonite'), Js('ygorskite'), Js('yhalite'), Js('yhydrite'), Js('yite'), Js('ykite'), Js('yl'), Js('ylite'), Js('yllonite'), Js('ymite'), Js('yne'), Js('yogen'), Js('yoite'), Js('yopilite'), Js('yptite'), Js('yrelite'), Js('ysoberyl'), Js('ysocolla'), Js('ysoprase'), Js('ysotile'), Js('ystonite'), Js('yte'), Js('ytocalcite'), Js('z'), Js('zalite'), Js('zanite'), Js('zerite'), Js('zilianite'), Js('zite'), Js('zlewoodite'), Js('zonite'), Js('zottaite'), Js('zziite')]))
pass
pass


# Add lib to the module scope
gems = var.to_python()
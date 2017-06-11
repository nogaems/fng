__all__ = ['englishRenaissance']

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
    var.put('nm1', Js([Js('Abraham'), Js('Adam'), Js('Adrian'), Js('Aelfward'), Js('Aelnod'), Js('Aelric'), Js('Ailwin'), Js('Akeman'), Js('Alan'), Js('Alexander'), Js('Alfred'), Js('Alfsige'), Js('Algar'), Js('Allen'), Js('Ambrose'), Js('Andrew'), Js('Ansketel'), Js('Ansketil'), Js('Anthony'), Js('Arnold'), Js('Arthur'), Js('Asketel'), Js('Asketil'), Js('Aslac'), Js('Athelstan'), Js('Attwell'), Js('Augustin'), Js('Avery'), Js('Baldwin'), Js('Barnaby'), Js('Bartholomew'), Js('Benedict'), Js('Bernard'), Js('Bertram'), Js('Brian'), Js('Brictric'), Js('Charles'), Js('Christopher'), Js('Conan'), Js('Constantin'), Js('Cornelius'), Js('Cuthbert'), Js('Daniel'), Js('David'), Js('Denis'), Js('Diggory'), Js('Drogo'), Js('Edmund'), Js('Edric'), Js('Edward'), Js('Elgar'), Js('Elric'), Js('Elyas'), Js('Eustace'), Js('Francis'), Js('Fulk'), Js('Fulke'), Js('Gabriel'), Js('Gamel'), Js('Gawain'), Js('Gawaine'), Js('Geoffrey'), Js('George'), Js('Gerard'), Js('Gilbert'), Js('Giles'), Js('Godfrey'), Js('Godric'), Js('Godwin'), Js('Gregory'), Js('Griffin'), Js('Guy'), Js('Hamo'), Js('Harald'), Js('Henry'), Js('Herebert'), Js('Hervey'), Js('Hugh'), Js('Humphrey'), Js('Isaac'), Js('Ivo'), Js('Jacob'), Js('James'), Js('Jasper'), Js('Jerome'), Js('Jodoc'), Js('John'), Js('Jordan'), Js('Josce'), Js('Joscelin'), Js('Joseph'), Js('Joyce'), Js('Jukel'), Js('Julian'), Js('Lambert'), Js('Lancelot'), Js('Laurence'), Js('Lawrence'), Js('Lefwald'), Js('Lefwin'), Js('Leofing'), Js('Leofric'), Js('Leofstan'), Js('Leomer'), Js('Leonard'), Js('Lewin'), Js('Ludovic'), Js('Luke'), Js('Mark'), Js('Marmaduke'), Js('Martin'), Js('Mathias'), Js('Matthew'), Js('Maurice'), Js('Maximillian'), Js('Merewin'), Js('Michael'), Js('Miles'), Js('Nathaniel'), Js('Nicholas'), Js('Nicolas'), Js('Nigel'), Js('Norman'), Js('Odbert'), Js('Odo'), Js('Oliver'), Js('Osbert'), Js('Osgood'), Js('Oswyn'), Js('Pascoe'), Js('Patrick'), Js('Percival'), Js('Peter'), Js('Philip'), Js('Philips'), Js('Piers'), Js('Ralph'), Js('Randall'), Js('Reginald'), Js('Reynold'), Js('Richard'), Js('Robert'), Js('Roger'), Js('Rolf'), Js('Rollo'), Js('Rowland'), Js('Saewulf'), Js('Sampson'), Js('Samuel'), Js('Sayer'), Js('Seman'), Js('Semer'), Js('Sewel'), Js('Sigor'), Js('Sigric'), Js('Silvester'), Js('Simon'), Js('Siward'), Js('Solomon'), Js('Stannard'), Js('Stephen'), Js('Swain'), Js('Swithin'), Js('Tedric'), Js('Thomas'), Js('Thori'), Js('Thorkel'), Js('Thurstan'), Js('Thurston'), Js('Tobias'), Js('Toka'), Js('Tori'), Js('Torkel'), Js('Turbert'), Js('Ulf'), Js('Ulfi'), Js('Ulfketel'), Js('Ulric'), Js('Urian'), Js('Valentine'), Js('Vivian'), Js('Waldo'), Js('Walter'), Js('Warin'), Js('Wicing'), Js('William'), Js('Wulfgar'), Js('Wulfgeat'), Js('Wulfstan'), Js('Wulfwin'), Js('Wulsi')]))
    var.put('nm2', Js([Js('Acelina'), Js('Adeline'), Js('Agatha'), Js('Agnes'), Js('Ailith'), Js('Albreda'), Js('Aldreda'), Js('Alfleta'), Js('Alice'), Js('Aliva'), Js('Alviva'), Js('Amice'), Js('Amy'), Js('Angrebod'), Js('Ann'), Js('Anne'), Js('Audrey'), Js('Avice'), Js('Avis'), Js('Barbara'), Js('Basilia'), Js('Beatrice'), Js('Beatrix'), Js('Bettrys'), Js('Blanche'), Js('Bothild'), Js('Bricteva'), Js('Bridget'), Js('Cassandra'), Js('Catherine'), Js('Cecilia'), Js('Cecily'), Js('Charity'), Js('Christian'), Js('Christiana'), Js('Christina'), Js('Clarissa'), Js('Clemence'), Js('Clementia'), Js('Constance'), Js('Crystobell'), Js('Cwenhild'), Js('Denise'), Js('Dorothy'), Js('Dyonisia'), Js('Earngith'), Js('Edith'), Js('Ediva'), Js('Egidia'), Js('Elena'), Js('Elinor'), Js('Elisabeth'), Js('Elizabeth'), Js('Ellen'), Js('Emeline'), Js('Emma'), Js('Engelise'), Js('Enota'), Js('Eulalia'), Js('Euphemia'), Js('Eve'), Js('Felicia'), Js('Fleur'), Js('Florence'), Js('Fortune'), Js('Frances'), Js('Frideswide'), Js('Genevieve'), Js('Gillian'), Js('Gilot'), Js('Godith'), Js('Goditha'), Js('Godiva'), Js('Godlefe'), Js('Godusa'), Js('Golde'), Js('Grace'), Js('Griselda'), Js('Gudrun'), Js('Gunnilda'), Js('Gunnora'), Js('Hannah'), Js('Hawisia'), Js('Helen'), Js('Helewis'), Js('Hilda'), Js('Ida'), Js('Idonea'), Js('Ingaret'), Js('Ingrid'), Js('Isabel'), Js('Iseult'), Js('Ismay'), Js('Ismenia'), Js('Isolde'), Js('Iva'), Js('Ivette'), Js('Jane'), Js('Janet'), Js('Jenefer'), Js('Joan'), Js('Josian'), Js('Joy'), Js('Joyce'), Js('Joycelin'), Js('Judith'), Js('Julian'), Js('Kynburgh'), Js('Laura'), Js('Lavinia'), Js('Leofe'), Js('Lettice'), Js('Lina'), Js('Livitha'), Js('Love'), Js('Lovechild'), Js('Loveday'), Js('Lucy'), Js('Mabel'), Js('Magisend'), Js('Margaret'), Js('Margery'), Js('Maria'), Js('Marion'), Js('Marjorie'), Js('Martha'), Js('Mary'), Js('Mathilda'), Js('Mathilde'), Js('Maud'), Js('Mawa'), Js('Milda'), Js('Mildburgh'), Js('Mildred'), Js('Millicent'), Js('Muriel'), Js('Nicola'), Js('Nota'), Js('Odelina'), Js('Olivia'), Js('Orabella'), Js('Parnell'), Js('Patience'), Js('Pavia'), Js('Petronella'), Js('Petronelle'), Js('Petronille'), Js('Philippa'), Js('Pleasance'), Js('Preciosa'), Js('Protasia'), Js('Rachel'), Js('Ragenhild'), Js('Rebecca'), Js('Regina'), Js('Richenda'), Js('Rimilde'), Js('Rosamund'), Js('Rose'), Js('Ruth'), Js('Sabine'), Js('Saegifu'), Js('Saelova'), Js('Sarah'), Js('Sarra'), Js('Scientia'), Js('Seberga'), Js('Sedehana'), Js('Sephare'), Js('Sibilla'), Js('Sigrith'), Js('Stanburgh'), Js('Stanilde'), Js('Susan'), Js('Susanna'), Js('Susannah'), Js('Sybil'), Js('Theda'), Js('Thomasin'), Js('Thomasine'), Js('Thomazin'), Js('Tiecia'), Js('Tiffany'), Js('Torilda'), Js('Tovilda'), Js('Truda'), Js('Turgiva'), Js('Ursula'), Js('Wakerilda'), Js('Wenthelen'), Js('Werthiva'), Js('Whyburgh'), Js('Wilamin'), Js('Wilmot'), Js('Winifred'), Js('Wulfhild'), Js('Ysopa')]))
    var.put('nm3', Js([Js('Abell'), Js('Abery'), Js('Acworth'), Js('Adams'), Js('Addicock'), Js('Alard'), Js('Albyn'), Js('Aldebourne'), Js('Alfraye'), Js('Alikok'), Js('Alington'), Js('Alleine'), Js('Amcottes'), Js('Amondesham'), Js('Andrews'), Js('Annesley'), Js('Ansty'), Js('Archer'), Js('Ardalle'), Js('Arderne'), Js('Argentein'), Js('Arnold'), Js('Arthur'), Js('Asger'), Js('Ashenhurst'), Js('Ashtor'), Js('Askew'), Js('Asplyn'), Js('Assheby'), Js('Assheton'), Js('Astley'), Js('Atherton'), Js('Atkinson'), Js('Atlee'), Js('Attilburgh'), Js('Aubrey'), Js('Audeley'), Js('Auldyngton'), Js('Aumberden'), Js('Ayde'), Js('Ayleward'), Js('Aylmer'), Js('Aynesworth'), Js('Ayshecombe'), Js('Babham'), Js('Babyngton'), Js('Bacon'), Js('Badby'), Js('Bailey'), Js('Baker'), Js('Balam'), Js('Baldwin'), Js('Ballard'), Js('Ballett'), Js('Bamard'), Js('Barantyn'), Js('Barber'), Js('Bardolf'), Js('Baret'), Js('Barfoot'), Js('Barker'), Js('Barnes'), Js('Barre'), Js('Barrentyne'), Js('Barstaple'), Js('Bartelot'), Js('Barton'), Js('Basset'), Js('Batherst'), Js('Battersby'), Js('Battyl'), Js('Baynton'), Js('Beauchamp'), Js('Beaumont'), Js('Beaurepaire'), Js('Bedell'), Js('Bedgbery'), Js('Bedingfeld'), Js('Beel'), Js('Beer'), Js('Bekyngham'), Js('Bell'), Js('Bende'), Js('Bennet'), Js('Benthey'), Js('Berdwell'), Js('Berecraft'), Js('Beresford'), Js('Berkhead'), Js('Bernard'), Js('Bernewelt'), Js('Berney'), Js('Berry'), Js('Berwyk'), Js('Best'), Js('Beton'), Js('Bettesthorne'), Js('Bewforest'), Js('Bewley'), Js('Bexley'), Js('Bigley'), Js('Bilingford'), Js('Bischoptree'), Js('Bishop'), Js('Bladwell'), Js('Blakeley'), Js('Blakewell'), Js('Blaknall'), Js('Blakwall'), Js('Blakwell'), Js('Blenerhayset'), Js('Blexham'), Js('Blodwell'), Js('Blome'), Js('Blondell'), Js('Blount'), Js('Blundell'), Js('Boddinham'), Js('Bohan'), Js('Boote'), Js('Boothe'), Js('Borell'), Js('Borrow'), Js('Bosby'), Js('Bost'), Js('Bostock'), Js('Boston'), Js('Boteler'), Js('Bothy'), Js('Bouldre'), Js('Bourne'), Js('Boville'), Js('Bowcer'), Js('Bowett'), Js('Bownell'), Js('Bowthe'), Js('Bowyar'), Js('Bradbridge'), Js('Bradshawe'), Js('Bradstane'), Js('Bradston'), Js('Bramfield'), Js('Brampton'), Js('Branche'), Js('Branwhait'), Js('Brassie'), Js('Braunstone'), Js('Bray'), Js('Brayles'), Js('Brecknock'), Js('Bredham'), Js('Brent'), Js('Bret'), Js('Brewse'), Js('Brewster'), Js('Brewys'), Js('Bridgeman'), Js('Briggs'), Js('Brinckhurst'), Js('Brocksby'), Js('Brodeway'), Js('Brodnax'), Js('Brokhill'), Js('Brome'), Js('Brook'), Js('Brougham'), Js('Broughton'), Js('Brouncker'), Js('Browet'), Js('Brown'), Js('Brownflet'), Js('Brownyng'), Js('Brudenell'), Js('Bryan'), Js('Bryn'), Js('Brystowe'), Js('Bulkeley'), Js('Bulstrode'), Js('Burgess'), Js('Burgh'), Js('Burghehyll'), Js('Burgoyn'), Js('Burlton'), Js('Burnell'), Js('Burton'), Js('Buryngton'), Js('Bushbury'), Js('Bushe'), Js('Buslingthorpe'), Js('Butler'), Js('Byfield'), Js('Byllyng'), Js('Byngham'), Js('Byrde'), Js('Byschoppeson'), Js('Caley'), Js('Callthorp'), Js('Campeden'), Js('Canon'), Js('Canteys'), Js('Cantilupe'), Js('Carbonall'), Js('Cardiff'), Js('Carew'), Js('Carlyll'), Js('Carter'), Js('Cary'), Js('Caseberde'), Js('Cassy'), Js('Castell'), Js('Castletown'), Js('Catesby'), Js('Cavell'), Js('Caxaton'), Js('Cely'), Js('Chamburleyn'), Js('Champneys'), Js('Chanceler'), Js('Chancey'), Js('Chapman'), Js('Charlis'), Js('Chase'), Js('Chatwyn'), Js('Chauncey'), Js('Chaundeler'), Js('Cheberell'), Js('Chechester'), Js('Cheddar'), Js('Chelde'), Js('Chelseye'), Js('Chernocke'), Js('Chester'), Js('Chetwoode'), Js('Cheyne'), Js('Child'), Js('Chowne'), Js('Chudderle'), Js('Churmound'), Js('Chylton'), Js('Chyrche'), Js('Claimond'), Js('Clarell'), Js('Clark'), Js('Clavell'), Js('Claybrook'), Js('Cleffort'), Js('Clement'), Js('Clerk'), Js('Clifton'), Js('Clitherow'), Js('Clopton'), Js('Clyfford'), Js('Cobbe'), Js('Cobham'), Js('Coblegh'), Js('Cockayne'), Js('Cod'), Js('Codington'), Js('Coffyn'), Js('Coggeshall'), Js('Colard'), Js('Colby'), Js('Cole'), Js('Colkins'), Js('Colmer'), Js('Colt'), Js('Complyn'), Js('Compton'), Js('Conquest'), Js('Cooke'), Js('Coorthopp'), Js('Copinger'), Js('Corbett'), Js('Corby'), Js('Cossale'), Js('Cosworth'), Js('Cosyngton'), Js('Cotton'), Js('Coulthurst'), Js('Courtenay'), Js('Covert'), Js('Cowill'), Js('Cox'), Js('Crane'), Js('Cranford'), Js('Crawley'), Js('Crekett'), Js('Cressy'), Js('Crispe'), Js('Cristemas'), Js('Crocker'), Js('Crugge'), Js('Cryppys'), Js('Cuddon'), Js('Culpeper'), Js('Cunnyngham'), Js('Curson'), Js('Curteys'), Js('Daelyngridge'), Js('Dagworth'), Js('Dale'), Js('Dalison'), Js('Damsell'), Js('Danet'), Js('Danvers'), Js('Darcy'), Js('Darley'), Js('Daubernoun'), Js('Daunce'), Js('Daundelyon'), Js('Dauntesay'), Js('Davers'), Js('Davy'), Js('Dawne'), Js('Day'), Js('Deacons'), Js('Delabere'), Js('Delamere'), Js('Dely'), Js('Demoke'), Js('Dencourt'), Js('Dene'), Js('Denton'), Js('Denys'), Js('Dericote'), Js('Dering'), Js('Deryngton'), Js('Desford'), Js('Digby'), Js('Dixton'), Js('Doddle'), Js('Dogmersfield'), Js('Donnet'), Js('Doreward'), Js('Dormer'), Js('Dove'), Js('Dow'), Js('Downer'), Js('Draper'), Js('Draw'), Js('Drayton'), Js('Driland'), Js('Dryden'), Js('Dunch'), Js('Duncombe'), Js('Dunham'), Js('Duredent'), Js('Dusteby'), Js('Dye'), Js('Dygenys'), Js('Dyneley'), Js('Dynham'), Js('Echyngham'), Js('Edgar'), Js('Edgcomb'), Js('Edgerley'), Js('Edwards'), Js('Egerton'), Js('Eggerley'), Js('Eglisfelde'), Js('Eldysley'), Js('Elmebrigge'), Js('Elyot'), Js('Elys'), Js('Emerson'), Js('Engeham'), Js('Engleford'), Js('Englysche'), Js('Epworth'), Js('Erewaker'), Js('Ermyn'), Js('Ertham'), Js('Esmund'), Js('Estbury'), Js('Estney'), Js('Estone'), Js('Etton'), Js('Everard'), Js('Everdon'), Js('Evrenden'), Js('Evyngar'), Js('Eyer'), Js('Eyston'), Js('Fabyan'), Js('Faldo'), Js('Fane'), Js('Faryndon'), Js('Faylare'), Js('Fayneman'), Js('Felbrigg'), Js('Feld'), Js('Fenton'), Js('Ferrer'), Js('Feversham'), Js('Ffrewyll'), Js('Fienley'), Js('Finch'), Js('Fitton'), Js('Fitzgeffrey'), Js('Fitzherbert'), Js('Fitzlewis'), Js('Fitzralph'), Js('Fitzwarym'), Js('Fitzwilliyam'), Js('Fleet'), Js('Fleming'), Js('Fletewoode'), Js('Flexney'), Js('Flower'), Js('Fodde'), Js('Fogg'), Js('Foliot'), Js('Foljambe'), Js('Follywolle'), Js('Folon'), Js('Folsham'), Js('Forde'), Js('Fortescue'), Js('Fortey'), Js('Fowler'), Js('Fox'), Js('Francey'), Js('Frankeleyn'), Js('Fraunces'), Js('Freer'), Js('Freville'), Js('Frilende'), Js('Frilleck'), Js('Frogenhall'), Js('Fromond'), Js('Froste'), Js('Frowseloure'), Js('Frye'), Js('Fryth'), Js('Fulburne'), Js('Fulmer'), Js('Funteyn'), Js('Furnace'), Js('Fynderne'), Js('Fyneux'), Js('Fysher'), Js('Gage'), Js('Galey'), Js('Garard'), Js('Gardyner'), Js('Gare'), Js('Garneys'), Js('Garret'), Js('Gascoigne'), Js('Gasper'), Js('Gavell'), Js('Gaynesford'), Js('Geddyng'), Js('Geffray'), Js('George'), Js('Gerard'), Js('Gerville'), Js('Geste'), Js('Gibbs'), Js('Gifford'), Js('Gilbert'), Js('Ginter'), Js('Glenham'), Js('Glennon'), Js('Glover'), Js('Goberd'), Js('Goddam'), Js('Godfrey'), Js('Golde'), Js('Golding'), Js('Goldwell'), Js('Gomersall'), Js('Gomfrey'), Js('Gonson'), Js('Good'), Js('Goodenouth'), Js('Goodere'), Js('Goodluck'), Js('Goodnestone'), Js('Goodryke'), Js('Goodryngton'), Js('Goodwyn'), Js('Goring'), Js('Gorney'), Js('Gorste'), Js('Gosebourne'), Js('Grafton'), Js('Greenway'), Js('Grene'), Js('Grenefeld'), Js('Greville'), Js('Grey'), Js('Grobbam'), Js('Grofhurst'), Js('Groston'), Js('Grove'), Js('Grymbalde'), Js('Guildeforde'), Js('Gyll'), Js('Gysborne'), Js('Gyttyns'), Js('Hache'), Js('Hackeman'), Js('Haddock'), Js('Haddon'), Js('Hadresham'), Js('Hakebourne'), Js('Hale'), Js('Hall'), Js('Halley'), Js('Halshan'), Js('Hambard'), Js('Hammer'), Js('Hamond'), Js('Hampden'), Js('Hancock'), Js('Hansart'), Js('Harbird'), Js('Harbotle'), Js('Harcourt'), Js('Hardy'), Js('Harewell'), Js('Hargreve'), Js('Harlakinden'), Js('Harleston'), Js('Harley'), Js('Harpeden'), Js('Harper'), Js('Harris'), Js('Harryses'), Js('Harte'), Js('Harwood'), Js('Hasard'), Js('Hatteclyff'), Js('Haukesworth'), Js('Hawkins'), Js('Hawtrey'), Js('Haye'), Js('Hayes'), Js('Hayton'), Js('Helme'), Js('Henshawe'), Js('Herleston'), Js('Heron'), Js('Hertcombe'), Js('Herwy'), Js('Hewes'), Js('Heydon'), Js('Heywood'), Js('Heyworth'), Js('Hicchecok'), Js('Higate'), Js('Higden'), Js('Hille'), Js('Hoare'), Js('Hobart'), Js('Hobert'), Js('Hodgeson'), Js('Holbrook'), Js('Holcot'), Js('Holes'), Js('Holland'), Js('Holsey'), Js('Holt'), Js('Holton'), Js('Hopton'), Js('Horman'), Js('Hornebolt'), Js('Hornley'), Js('Horsey'), Js('Horthall'), Js('Horton'), Js('Hosteler'), Js('Hotham'), Js('Howard'), Js('Huchenson'), Js('Huddleston'), Js('Hugeford'), Js('Hunden'), Js('Hungate'), Js('Hunston'), Js('Hurst'), Js('Hussey'), Js('Hyde'), Js('Hyenson'), Js('Hylderley'), Js('Hyll'), Js('Inwood'), Js('Isley'), Js('Jackmann'), Js('Jackson'), Js('James'), Js('Janner'), Js('Jarman'), Js('Jay'), Js('Jendring'), Js('Jenney'), Js('Johnson'), Js('Jordan'), Js('Joslyne'), Js('Joulon'), Js('Jowchet'), Js('Kekilpenny'), Js('Kellett'), Js('Kelly'), Js('Kemp'), Js('Kent'), Js('Keriell'), Js('Kesteven'), Js('Key'), Js('Kidwelly'), Js('Killigrew'), Js('Kinge'), Js('Knevynton'), Js('Knighton'), Js('Knody'), Js('Knoyll'), Js('Knyvet'), Js('Kottow'), Js('Kydwelly'), Js('Kyllyngworth'), Js('Kyrkeby'), Js('Kytson'), Js('Lacy'), Js('Laken'), Js('Lamber'), Js('Lambton'), Js('Langeton'), Js('Langham'), Js('Langstone'), Js('Lappage'), Js('Latham'), Js('Latton'), Js('Launceleyn'), Js('Lave'), Js('Lawnder'), Js('Leeche'), Js('Leeds'), Js('Lehenard'), Js('Leigh'), Js('Leighlin'), Js('Leman'), Js('Lenton'), Js('Lestrange'), Js('Letterford'), Js('Leventhorpe'), Js('Leverer'), Js('Leveson'), Js('Lewys'), Js('Leynham'), Js('Leynthall'), Js('Lichefield'), Js('Livesey'), Js('Lloyd'), Js('Lockton'), Js('Lodyngton'), Js('Lond'), Js('London'), Js('Long'), Js('Longton'), Js('Lovell'), Js('Loveney'), Js('Loveryk'), Js('Lowe'), Js('Lowthe'), Js('Lucy'), Js('Ludsthorp'), Js('Luke'), Js('Lumbarde'), Js('Lupton'), Js('Lyfelde'), Js('Lymsey'), Js('Lynde'), Js('Lyon'), Js('Lyrypine'), Js('Lysle'), Js('Lytcott'), Js('Lyttleburye'), Js('Lytton'), Js('Lyveryche'), Js('Makepiece'), Js('Malemayns'), Js('Malster'), Js('Maltoun'), Js('Malyns'), Js('Manfield'), Js('Manston'), Js('Mapilton'), Js('Marcheford'), Js('Mareys'), Js('Markeley'), Js('Marsham'), Js('Marten'), Js('Mason'), Js('Massyngberde'), Js('Maudit'), Js('Mauntell'), Js('Maycot'), Js('Maydestone'), Js('Mayne'), Js('Maynwaring'), Js('Mede'), Js('Medeley'), Js('Merden'), Js('Mereworth'), Js('Merstun'), Js('Merton'), Js('Metcalf'), Js('Michelgrove'), Js('Millys'), Js('Milsent'), Js('Moland'), Js('Molyngton'), Js('Molyns'), Js('Monde'), Js('Montacute'), Js('Montagu'), Js('Moore'), Js('More'), Js('Morecote'), Js('Morley'), Js('Mortymer'), Js('Moryet'), Js('Morys'), Js('Motesfont'), Js('Mowfurth'), Js('Mugge'), Js('Mullens'), Js('Muston'), Js('Myddilton'), Js('Myllet'), Js('Mylner'), Js('Narbrige'), Js('Nash'), Js('Neceham'), Js('Nele'), Js('Nevinson'), Js('Newdegate'), Js('Newman'), Js('Noke'), Js('Norbury'), Js('Norden'), Js('Norrys'), Js('North'), Js('Northwoode'), Js('Norton'), Js('Norwich'), Js('Norwood'), Js('Notfelde'), Js('Notyngham'), Js('Nysell'), Js('Obson'), Js('Oke'), Js('Oken'), Js('Oliver'), Js('Olyngworthe'), Js('Osborne'), Js('Osteler'), Js('Osyllbury'), Js('Outlawe'), Js('Oxenbrigg'), Js('Page'), Js('Pagge'), Js('Palmer'), Js('Panshawe'), Js('Papley'), Js('Parker'), Js('Parret'), Js('Parris'), Js('Parsons'), Js('Paston'), Js('Pattesley'), Js('Payne'), Js('Peacok'), Js('Pecke'), Js('Peckham'), Js('Peele'), Js('Pekham'), Js('Peletoot'), Js('Peltie'), Js('Pemberton'), Js('Pen'), Js('Penhallick'), Js('Pennebrygg'), Js('Perchehay'), Js('Perot'), Js('Perryvalle'), Js('Petham'), Js('Petley'), Js('Pettit'), Js('Pettwoode'), Js('Peyton'), Js('Phelip'), Js('Philips'), Js('Playters'), Js('Plessi'), Js('Plymmyswoode'), Js('Poffe'), Js('Pole'), Js('Polsted'), Js('Polton'), Js('Porter'), Js('Portyngton'), Js('Potter'), Js('Poulet'), Js('Pownder'), Js('Pratt'), Js('Pray'), Js('Prelatte'), Js('Prophete'), Js('Prowd'), Js('Purlles'), Js('Pursglove'), Js('Purvoche'), Js('Pygott'), Js('Pylet'), Js('Pynnoke'), Js('Pynty'), Js('Quintin'), Js('Radley'), Js('Rampston'), Js('Ramsey'), Js('Ratcliff'), Js('Rawlyn'), Js('Rawson'), Js('Raynsford'), Js('Rede'), Js('Redman'), Js('Reeve'), Js('Reynes'), Js('Reynesford'), Js('Richeman'), Js('Rikhill'), Js('Risley'), Js('Roberts'), Js('Robertson'), Js('Robins'), Js('Robynson'), Js('Rochester'), Js('Rochforth'), Js('Roland'), Js('Rolleston'), Js('Rondel'), Js('Ront'), Js('Roper'), Js('Rotheley'), Js('Rous'), Js('Rowdon'), Js('Rowe'), Js('Rowlatt'), Js('Rowley'), Js('Rudhall'), Js('Rufford'), Js('Ruggenale'), Js('Ruggeweyn'), Js('Rusche'), Js('Russell'), Js('Ryall'), Js('Rykeworth'), Js('Rynger'), Js('Ryppringham'), Js('Sacheverell'), Js('Sackville'), Js('Sadler'), Js('Salford'), Js('Salle'), Js('Salter'), Js('Saltonstall'), Js('Sampson'), Js('Samuell'), Js('Sanburne'), Js('Sandes'), Js('Saunders'), Js('Saunterton'), Js('Savill'), Js('Sayer'), Js('Saynsbery'), Js('Scarclyf'), Js('Scollfyld'), Js('Scot'), Js('Scrogs'), Js('Scrope'), Js('Sedley'), Js('Sedlow'), Js('Seger'), Js('Selwyn'), Js('Sencler'), Js('Sentjohn'), Js('Serche'), Js('Sever'), Js('Seymour'), Js('Seyntaubyn'), Js('Seys'), Js('Sharman'), Js('Shawe'), Js('Sheffeld'), Js('Sheraton'), Js('Sherbourne'), Js('Sherman'), Js('Shevington'), Js('Shingleton'), Js('Shipwash'), Js('Shiveley'), Js('Shorditch'), Js('Shosmyth'), Js('Shotbolt'), Js('Shylton'), Js('Sibill'), Js('Silvester'), Js('Skipwith'), Js('Sleford'), Js('Slyfield'), Js('Smith'), Js('Snayth'), Js('Snell'), Js('Snelling'), Js('Sotton'), Js('Sparrow'), Js('Spebynton'), Js('Speir'), Js('Spelman'), Js('Spencer'), Js('Spetyll'), Js('Spicer'), Js('Sprottle'), Js('Sprunt'), Js('Stace'), Js('Stanbury'), Js('Standon'), Js('Stanley'), Js('Stanwix'), Js('Staple'), Js('Staunton'), Js('Staverton'), Js('Stepney'), Js('Stevyn'), Js('Stocks'), Js('Stodeley'), Js('Stoke'), Js('Stokerton'), Js('Stokes'), Js('Stokey'), Js('Stokton'), Js('Stone'), Js('Stoner'), Js('Stoughton'), Js('Strachleigh'), Js('Strader'), Js('Strangewayes'), Js('Strelley'), Js('Strete'), Js('Stubbe'), Js('Styles'), Js('Stylle'), Js('Styward'), Js('Sulyard'), Js('Sumner'), Js('Swan'), Js('Swetecok'), Js('Swetenham'), Js('Switte'), Js('Symeon'), Js('Symons'), Js('Tabard'), Js('Tame'), Js('Taylor'), Js('Tedcastle'), Js('Theobauld'), Js('Thomas'), Js('Thornburgh'), Js('Thorne'), Js('Thornton'), Js('Thorp'), Js('Throkmorton'), Js('Thursby'), Js('Tibborde'), Js('Tilghman'), Js('Tiploft'), Js('Topsfield'), Js('Torryngton'), Js('Tothyll'), Js('Town'), Js('Tregonwell'), Js('Treningham'), Js('Trenowyth'), Js('Trevet'), Js('Trumpington'), Js('Tubney'), Js('Turner'), Js('Twarby'), Js('Tweedye'), Js('Tyndall'), Js('Tyrell'), Js('Ufford'), Js('Underhill'), Js('Unton'), Js('Upton'), Js('Urswic'), Js('Vass'), Js('Vaughan'), Js('Vawdrey'), Js('Veldon'), Js('Verney'), Js('Vernon'), Js('Vinter'), Js('Wade'), Js('Wadham'), Js('Wake'), Js('Waldegrave'), Js('Waldeley'), Js('Walden'), Js('Walford'), Js('Walkden'), Js('Walker'), Js('Wallace'), Js('Walley'), Js('Walrond'), Js('Walsch'), Js('Waltham'), Js('Walton'), Js('Wanteley'), Js('Wappelode'), Js('Warbulton'), Js('Warde'), Js('Wardeby'), Js('Wardrieu'), Js('Wardyworth'), Js('Warner'), Js('Warren'), Js('Wayte'), Js('Webb'), Js('Weekes'), Js('Welbek'), Js('Welby'), Js('Wellins'), Js('Wenman'), Js('Wensley'), Js('West'), Js('Westbrook'), Js('Westlake'), Js('Weston'), Js('Wetherden'), Js('Wexcombe'), Js('Whalley'), Js('White'), Js('Whitewood'), Js('Whowood'), Js('Whytton'), Js('Whytyng'), Js('Wightman'), Js('Wilkins'), Js('Willardsey'), Js('Williams'), Js('Willmer'), Js('Willys'), Js('Wilson'), Js('Windham'), Js('Wingfield'), Js('Wiseman'), Js('Wolrond'), Js('Wolstonton'), Js('Woodbrygge'), Js('Woode'), Js('Woodeward'), Js('Worsley'), Js('Wotton'), Js('Wreke'), Js('Wrenne'), Js('Wright'), Js('Wulvedon'), Js('Wyard'), Js('Wyatt'), Js('Wyddowsoun'), Js('Wyghtham'), Js('Wylcotes'), Js('Wylde'), Js('Wylmot'), Js('Wymer'), Js('Wyncall'), Js('Wynston'), Js('Wynstryngham'), Js('Wynter'), Js('Wythinghall'), Js('Wyvil'), Js('Yate'), Js('Yaxley'), Js('Yden'), Js('Yelverton'), Js('Yerde'), Js('York'), Js('Yornold'), Js('Young'), Js('la Barre'), Js('la Hale'), Js('la Penne'), Js('le Bone')]))
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
englishRenaissance = var.to_python()
__all__ = ['spanishRenaissance']

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
    var.put('nm1', Js([Js('Çino'), Js('Agostin'), Js('Agustín'), Js('Agustin'), Js('Alex'), Js('Alexandre'), Js('Alfonso'), Js('Alixandre'), Js('Almerique'), Js('Almeyque'), Js('Alonsico'), Js('Alonso'), Js('Alsen'), Js('Alsonso'), Js('Altar'), Js('Alvar'), Js('Alvaro'), Js('Ambrosio'), Js('Andres'), Js('Anrique'), Js('Anselmo'), Js('Antón'), Js('Anton'), Js('Antonio'), Js('Arias'), Js('Arnao'), Js('Audres'), Js('Baltasar'), Js('Bartolo'), Js('Bartolomé'), Js('Bartolome'), Js('Bea'), Js('Beltrán'), Js('Beltrané'), Js('Benito'), Js('Bernal'), Js('Bernaldino'), Js('Bernardino'), Js('Biçent'), Js('Bicençio'), Js('Bitores'), Js('Blas'), Js('Blasco'), Js('Blay'), Js('Borredan'), Js('Braçayda'), Js('Brahen'), Js('Carlos'), Js('Castañon'), Js('Christoval'), Js('Cornieles'), Js('Cosme'), Js('Cristóbal'), Js('Cristobal'), Js('Cristoval'), Js('Damián'), Js('Damian'), Js('Diego'), Js('Dieguito'), Js('Domingo'), Js('Donis'), Js('Duran'), Js('Enrique'), Js('Enrrique'), Js('Escobar'), Js('Esqivel'), Js('Estevan'), Js('Ettor'), Js('Fadrique'), Js('Felipe'), Js('Fernado'), Js('Fernan'), Js('Fernand'), Js('Fernandico'), Js('Fernando'), Js('Fernendo'), Js('Ferrand'), Js('Ferrer'), Js('Ferrnando'), Js('Françisco'), Js('Francisco'), Js('Fransisco'), Js('Frenando'), Js('Fulgencio'), Js('Gabriel'), Js('Galla'), Js('Garçi'), Js('Garçia'), Js('Garçilaso'), Js('Garaçia'), Js('García'), Js('Garcia'), Js('Gascon'), Js('Gaspar'), Js('Gavriel'), Js('Gemini'), Js('Gerónimo'), Js('Geronimo'), Js('Gil'), Js('Gilete'), Js('Gironimo'), Js('Golarte'), Js('Gomes'), Js('Gomez'), Js('Gonçalo'), Js('Gonzalo'), Js('Graviel'), Js('Guillén'), Js('Guillen'), Js('Gutierre'), Js('Gutirre'), Js('Henrrique'), Js('Hernando'), Js('Hortuñño'), Js('Hortun'), Js('Iñigo'), Js('Jacobo'), Js('Jaime'), Js('Janucho'), Js('Jayme'), Js('Jcan'), Js('Joanes'), Js('Johan'), Js('Johanes'), Js('Jorge'), Js('José'), Js('Juan'), Js('Juancho'), Js('Juanes'), Js('Juanico'), Js('Juanito'), Js('Julian'), Js('Jullian'), Js('Julliau'), Js('Ladron'), Js('Larnaz'), Js('Leon'), Js('Llorençe'), Js('Llorenço'), Js('Llorenco'), Js('Llorente'), Js('Lono'), Js('Lop'), Js('Lope'), Js('Lorenço'), Js('Lorenzo'), Js('Lucas'), Js('Lucon'), Js('Luis'), Js('Luys'), Js('Machin'), Js('Manrrique'), Js('Manuel'), Js('Marçal'), Js('Marmolejo'), Js('Martín'), Js('Martin'), Js('Mateo'), Js('Men'), Js('Menaute'), Js('Mendo'), Js('Micael'), Js('Miguel'), Js('Millan'), Js('Monferriz'), Js('Muli'), Js('Nadal'), Js('Nicolás'), Js('Nicolao'), Js('Nicolas'), Js('Nofre'), Js('Nuño'), Js('Nuflo'), Js('Nufro'), Js('Ochoa'), Js('Onorato'), Js('Ontañon'), Js('Pablo'), Js('Pascual'), Js('Patro'), Js('Pedro'), Js('Pequeni'), Js('Pequi'), Js('Per'), Js('Perico'), Js('Pero'), Js('Perucho'), Js('Porico'), Js('Ramiro'), Js('Ramon'), Js('Ramonet'), Js('Remero'), Js('Remon'), Js('Rodrigo'), Js('Ruberte'), Js('Ruy'), Js('Sabastian'), Js('Salazar'), Js('Salvador'), Js('Sancho'), Js('Sansón'), Js('Savastian'), Js('Sebastian'), Js('Simon'), Js('Suero'), Js('Tello'), Js('Timoteo'), Js('Tomás'), Js('Tomas'), Js('Toribio'), Js('Tristán'), Js('Valeriano'), Js('Velasco'), Js('Vernaldino'), Js('Viçente'), Js('Vinçente'), Js('Ximen'), Js('Ximon'), Js('Yñigo'), Js('Ydalla')]))
    var.put('nm2', Js([Js('Çeçilia'), Js('Abdona'), Js('Ageda'), Js('Agnes'), Js('Agueda'), Js('Aguilona'), Js('Alatara'), Js('Alba'), Js('Aldomara'), Js('Aldonça'), Js('Aldonsa'), Js('Aldorisa'), Js('Alfonsa'), Js('Alfresina'), Js('Almenara'), Js('Alvira'), Js('Ana'), Js('Andarina'), Js('Andolça'), Js('Andrea'), Js('Angel'), Js('Angela'), Js('Angelina'), Js('Anna'), Js('Anthona'), Js('Antona'), Js('Antonia'), Js('Argeda'), Js('Aularia'), Js('Baltasara'), Js('Barbera'), Js('Barbola'), Js('Beatriç'), Js('Beatris'), Js('Beatriu'), Js('Beatriz'), Js('Berarda'), Js('Berthomeua'), Js('Blanca'), Js('Blanqua'), Js('Blanquina'), Js('Brianda'), Js('Brigida'), Js('Burguera'), Js('Calamoya'), Js('Castellana'), Js('Castelleta'), Js('Catalana'), Js('Catalina'), Js('Catalyna'), Js('Catelina'), Js('Caterina'), Js('Catherina'), Js('Ceçilia'), Js('Cetina'), Js('Clara'), Js('Constança'), Js('Constanza'), Js('Costança'), Js('Costanza'), Js('Crespa'), Js('Cristina'), Js('Dalfina'), Js('Damiana'), Js('Damiata'), Js('Diomar'), Js('Dionisa'), Js('Egipciana'), Js('Eguala'), Js('Elbira'), Js('Elena'), Js('Elionor'), Js('Eluira'), Js('Elvira'), Js('Elvyra'), Js('Eularia'), Js('Fatima'), Js('Featris'), Js('Floriana'), Js('Florinda'), Js('Foresa'), Js('Françisca'), Js('Françisquita'), Js('Francesca'), Js('Francina'), Js('Francisca'), Js('Gaceta'), Js('Gentil'), Js('Geronima'), Js('Ginovisa'), Js('Gostança'), Js('Graçia'), Js('Gracia'), Js('Gregoria'), Js('Guinella'), Js('Guiomar'), Js('Guyomar'), Js('Hieronima'), Js('Hieronyma'), Js('Iheronima'), Js('Inés'), Js('Ines'), Js('Isabel'), Js('Isabelica'), Js('Jerónima'), Js('Joana'), Js('Johana'), Js('Jona'), Js('Juana'), Js('Juanica'), Js('Julia'), Js('Juliana'), Js('Leal'), Js('Leonor'), Js('Loçia'), Js('Lopisa'), Js('Loreta'), Js('Luïsa'), Js('Lucia'), Js('Lucrecia'), Js('Luisa'), Js('Luysa'), Js('Luzia'), Js('Maçana'), Js('Madelena'), Js('Magdalena'), Js('Magdelena'), Js('Maior'), Js('Mancia'), Js('María'), Js('Margalida'), Js('Margarida'), Js('Margarina'), Js('Margarita'), Js('Mari'), Js('Maria'), Js('Mariana'), Js('Marina'), Js('Marquesa'), Js('Martina'), Js('Mayor'), Js('Melchora'), Js('Mençia'), Js('Mencía'), Js('Mencia'), Js('Merina'), Js('Miata'), Js('Miquela'), Js('Nofra'), Js('Ofrecina'), Js('Olall'), Js('Orastriosa'), Js('Palacesa'), Js('Patronilla'), Js('Pelejana'), Js('Quiteria'), Js('Ricla'), Js('Sancha'), Js('Scolana'), Js('Sentiu'), Js('Sicilia'), Js('Sperança'), Js('Stefania'), Js('Susana'), Js('Tareisa'), Js('Tareza'), Js('Teresa'), Js('Tereysa'), Js('Theresa'), Js('Thomasa'), Js('Toda'), Js('Tonixqua'), Js('Urgellesa'), Js('Ursola'), Js('Ursula'), Js('Valentina'), Js('Viana'), Js('Vicenta'), Js('Violant'), Js('Violante'), Js('Ynés'), Js('Ynes'), Js('Yolant'), Js('Ypola'), Js('Ysabel'), Js('Ysabet')]))
    var.put('nm3', Js([Js('Çafra'), Js('Çahera'), Js('Çapata'), Js('Çatico'), Js('Çenturion'), Js('Çeron'), Js('Çorrilla'), Js('Abril'), Js('Aguado'), Js('Alcaçar'), Js('Alcon'), Js('Alexandre'), Js('Almayda'), Js('Alonso'), Js('Alvares'), Js('Alvarez'), Js('Aragones'), Js('Arias'), Js('Ayere'), Js('Aznariz'), Js('Bárba'), Js('Badelas'), Js('Bajas'), Js('Balboa'), Js('Bamonte'), Js('Banbela'), Js('Banegas'), Js('Barbero'), Js('Barril'), Js('Baylín'), Js('Bernal'), Js('Bertino Sans'), Js('Bogado'), Js('Bota'), Js('Brasa'), Js('Bretanzos'), Js('Briçianos'), Js('Brusa'), Js('Cañero'), Js('Cabrero'), Js('Cacho'), Js('Calabaças'), Js('Calahorra'), Js('Calante'), Js('Calderon'), Js('Caminante'), Js('Cano'), Js('Cardoso'), Js('Carperon'), Js('Carral'), Js('Carrasco'), Js('Carreño'), Js('Carrillo'), Js('Cascon'), Js('Casteles'), Js('Castellano'), Js('Castellon'), Js('Catala'), Js('Catarribera'), Js('Cavallero'), Js('Cenisçeros'), Js('Chacon'), Js('Chanta'), Js('Cherino'), Js('Cintero'), Js('Cocon'), Js('Cola'), Js('Coll'), Js('Collaço'), Js('Colmenares'), Js('Colon'), Js('Comete'), Js('Conchada'), Js('Correa'), Js('Corredor'), Js('Cortes'), Js('Corvacho'), Js('Cotado'), Js('Covarrubias'), Js('Cuello'), Js('Damian'), Js('Deça'), Js('Dey'), Js('Dias'), Js('Diez'), Js('Dominguez'), Js('Dominico'), Js('Donant'), Js('Donayre'), Js('Donis'), Js('Duran'), Js('Enrriquez'), Js('Escalante'), Js('Escalera'), Js('Estevan'), Js('Estevez'), Js('Fajardo'), Js('Fernandes'), Js('Ferrer'), Js('Florentin'), Js('Flores'), Js('Fogaça'), Js('Fonte Poutein'), Js('Fontesar'), Js('Forentin'), Js('Gajardo'), Js('Galas'), Js('Galiano'), Js('Galindo'), Js('Galvan'), Js('Galves'), Js('Garavito'), Js('Garcia'), Js('Garnica'), Js('Garrido'), Js('Gaytan'), Js('Gil'), Js('Gimenez'), Js('Girán'), Js('Giraldino'), Js('Girao'), Js('Gomes'), Js('Gonçales'), Js('Gonzales'), Js('Gramaja'), Js('Grand'), Js('Guerrero'), Js('Guerrey'), Js('Gutierres'), Js('Hernandez'), Js('Herrero'), Js('Hordoñez'), Js('Hortiz'), Js('Hortolano'), Js('Hortuño'), Js('Hurtado'), Js('Jimenez'), Js('Julian'), Js('Justeniano'), Js('Lascaris'), Js('Llorens'), Js('Lopes'), Js('Lopez'), Js('Lorenço'), Js('Loriguero'), Js('Lucas'), Js('Lusicori'), Js('Maça'), Js('Maderuelo'), Js('Madraso'), Js('Mafaraxas'), Js('Maldonado'), Js('Malon'), Js('Manrrique1'), Js('Manuel'), Js('Marañon'), Js('Marques'), Js('Marroqui'), Js('Martil'), Js('Martin'), Js('Martinez'), Js('Mata'), Js('Mato'), Js('Mendez'), Js('Mexía'), Js('Mexica'), Js('Mirones'), Js('Mondexar'), Js('Mondragon'), Js('Montero'), Js('Mora'), Js('Moya'), Js('Muños'), Js('Murcia'), Js('Natalez'), Js('Navaroo'), Js('Nuñes'), Js('Nuñez'), Js('Nuño'), Js('Oleylas'), Js('Oller'), Js('Onte'), Js('Ordas'), Js('Ordoñes'), Js('Orejón'), Js('Orenes'), Js('Ortelano'), Js('Osorio'), Js('Ospital'), Js('Ozalla'), Js('Pacheco'), Js('Palafox'), Js('Palomino'), Js('Pardo'), Js('Patudo'), Js('Patyño'), Js('Pedrosa'), Js('Pellicer'), Js('Peres'), Js('Pereyra'), Js('Piero'), Js('Pimentel'), Js('Pina'), Js('Pinedo'), Js('Pinto'), Js('Piquier'), Js('Ponçe'), Js('Porras'), Js('Preto'), Js('Quadrado'), Js('Quexada'), Js('Quicedo'), Js('Raçoso'), Js('Rache'), Js('Rachen'), Js('Ram'), Js('Ramires'), Js('Ramirez'), Js('Rancha'), Js('Raso'), Js('Rejón'), Js('Roche'), Js('Rodrigues'), Js('Rodriguez'), Js('Roman'), Js('Romano'), Js('Romero'), Js('Rosa'), Js('Rosil'), Js('Ruberto'), Js('Ruis'), Js('Ruyz'), Js('Sabastian'), Js('Salazar'), Js('Sanches'), Js('Sanchez'), Js('Sandin'), Js('Sandino'), Js('Santos'), Js('Saravia'), Js('Sariñena'), Js('Sarmiento'), Js('Sarria'), Js('Sebastian'), Js('Serra'), Js('Serrano'), Js('Sesto'), Js('Seve'), Js('Situ'), Js('Soler'), Js('Sorje'), Js('Sosa'), Js('Suares'), Js('Suarez'), Js('Symilor'), Js('Tasina'), Js('Telles'), Js('Texen'), Js('Texera'), Js('Texil'), Js('Tinoco'), Js('Torrero'), Js('Toxenes'), Js('Tuñon'), Js('Vaca'), Js('Vaes'), Js('Valdés'), Js('Valera'), Js('Vanegas'), Js('Varela'), Js('Vazques'), Js('Vela'), Js('Velasco'), Js('Velasques'), Js('Velazquez'), Js('Velez'), Js('Vello'), Js('Venegas'), Js('Vera'), Js('Vida'), Js('Villagras'), Js('Villanova'), Js('Ximenes'), Js('Ximon'), Js('Yanes'), Js('Ybañes'), Js('Yebera'), Js('Ynfante'), Js('Yniguis'), Js('de Çafra'), Js('de Çalaga'), Js('de Çaldibar'), Js('de Çamora'), Js('de Çana'), Js('de Çapata'), Js('de Çarate'), Js('de Çavallos'), Js('de Çebolleros'), Js('de Çigales'), Js('de Çiruela'), Js('de Çisneros'), Js('de Çuñiga'), Js('de Çuaçola'), Js('de Çulvaga'), Js('de Çumel'), Js('de Çuyvi'), Js('de Aça'), Js('de Açarga'), Js('de Acosta'), Js('de Acuña'), Js('de Aguayo'), Js('de Aguero'), Js('de Aguilar'), Js('de Aguilera'), Js('de Aguirre'), Js('de Ahumanda'), Js('de Alçaga'), Js('de Alacon'), Js('de Alagon'), Js('de Alarçio'), Js('de Alarcon'), Js('de Albear'), Js('de Albion'), Js('de Albiz'), Js('de Albuaçeri'), Js('de Alcalá'), Js('de Alcala'), Js('de Alcaraz'), Js('de Alconchel'), Js('de Alderete'), Js('de Alfaro'), Js('de Alixandria'), Js('de Almaçan'), Js('de Almendara'), Js('de Almería'), Js('de Alsedo'), Js('de Alva'), Js('de Alzado'), Js('de Alzedo'), Js('de Ampudia'), Js('de Amusco'), Js('de Anchieta'), Js('de Andia'), Js('de Andino'), Js('de Anglada'), Js('de Angulo'), Js('de Arçe'), Js('de Arçeo'), Js('de Ara'), Js('de Aragon'), Js('de Aramayo'), Js('de Arana'), Js('de Aranda'), Js('de Araoz'), Js('de Araso'), Js('de Arbuete'), Js('de Arena'), Js('de Arenas'), Js('de Arevalo'), Js('de Argote'), Js('de Arroyo'), Js('de Arteaga'), Js('de Artiaga'), Js('de Artieta'), Js('de Arzco'), Js('de Arze'), Js('de Asconiça'), Js('de Astorga'), Js('de Astudillo'), Js('de Auilera'), Js('de Avalos'), Js('de Avila'), Js('de Ayala'), Js('de Ayon'), Js('de Azcona'), Js('de Azpetia'), Js('de Badajoz'), Js('de Baeça'), Js('de Baena'), Js('de Bagida'), Js('de Balbuena'), Js('de Baldivia'), Js('de Balparda'), Js('de Barçelona'), Js('de Barrasa'), Js('de Barreda'), Js('de Barrientos'), Js('de Baylen'), Js('de Bazan'), Js('de Benavides'), Js('de Beneja'), Js('de Bergara'), Js('de Bermeo'), Js('de Bernuda'), Js('de Betanzos'), Js('de Beydatar'), Js('de Bilbao'), Js('de Bilbau'), Js('de Binçiguerra'), Js('de Biosca'), Js('de Biruiesca'), Js('de Bitoria'), Js('de Bobadilla'), Js('de Bolaños'), Js('de Bonal'), Js('de Bonaval'), Js('de Bort'), Js('de Bozmediano'), Js('de Brihuega'), Js('de Briones'), Js('de Buenaventura'), Js('de Buendía'), Js('de Burgos'), Js('de Bustamante'), Js('de Buytrago'), Js('de Cárdenas'), Js('de Cañado'), Js('de Cañete'), Js('de Cañizares'), Js('de Cabmillas'), Js('de Cabra'), Js('de Caceres'), Js('de Caderroa'), Js('de Calátayud'), Js('de Calatrava'), Js('de Camarma'), Js('de Camiña'), Js('de Cantlapiedra'), Js('de Cardenas'), Js('de Cardona'), Js('de Carmona'), Js('de Carrión'), Js('de Carvajal'), Js('de Casanueva'), Js('de Castil'), Js('de Castilla'), Js('de Castro'), Js('de Castylblanco'), Js('de Catres'), Js('de Cea'), Js('de Cepeda'), Js('de Cespedes'), Js('de Chandiano'), Js('de Cieça'), Js('de Cobraçes'), Js('de Colmenares'), Js('de Comendador'), Js('de Conchillos'), Js('de Contreras'), Js('de Corcoles'), Js('de Cordoba'), Js('de Coria'), Js('de Corrales'), Js('de Coslada'), Js('de Costana'), Js('de Cotes'), Js('de Covarruvias'), Js('de Cuellar'), Js('de Cuenca'), Js('de Cuero'), Js('de Cueto'), Js('de Cueva'), Js('de Cuevas Rubias'), Js('de Deça'), Js('de Dicastillo'), Js('de Dueñas'), Js('de Escalona'), Js('de Escobar'), Js('de Espinosa'), Js('de Estremos'), Js('de Ferrada'), Js('de Fez'), Js('de Figueredo'), Js('de Figueroa'), Js('de Flores'), Js('de Fonseca'), Js('de Frimonet'), Js('de Gadea'), Js('de Galves'), Js('de Gamarra'), Js('de Gaona'), Js('de Gareta'), Js('de Gasta'), Js('de Godoy'), Js('de Goire'), Js('de Gomiel'), Js('de Gordón'), Js('de Graçia'), Js('de Greda'), Js('de Grizio'), Js('de Guadalajara'), Js('de Guadalupe'), Js('de Guarda'), Js('de Gudiel'), Js('de Guevara'), Js('de Guzman'), Js('de Hermita'), Js('de Hermosilla'), Js('de Herrera'), Js('de Hervas'), Js('de Hivia'), Js('de Hontañon'), Js('de Hontiveros'), Js('de Horduña'), Js('de Hortega'), Js('de Huerta'), Js('de Jaen'), Js('de Joara'), Js('de Junio'), Js('de Landa'), Js('de Lara'), Js('de Lares'), Js('de Larringa'), Js('de Layan'), Js('de Leon'), Js('de Lerma'), Js('de Leyva'), Js('de Lezcano'), Js('de Liaño'), Js('de Libe'), Js('de Limonsin'), Js('de Lire'), Js('de Lisón'), Js('de Llarena'), Js('de Luna'), Js('de Lunar'), Js('de Lupián'), Js('de Luque'), Js('de Luson'), Js('de Luxan'), Js('de Luz'), Js('de Maderuelo'), Js('de Madrid'), Js('de Madrigal'), Js('de Maella'), Js('de Mahuleon'), Js('de Maldonado'), Js('de Mallea'), Js('de Manjeras'), Js('de Mansilla'), Js('de Marchena'), Js('de Marmol'), Js('de Mata'), Js('de Matienço'), Js('de Mayorga'), Js('de Mayrena'), Js('de Medina'), Js('de Medrano'), Js('de Mena'), Js('de Menata'), Js('de Mendoça'), Js('de Meneses'), Js('de Mercado'), Js('de Merlo'), Js('de Merodio'), Js('de Mesa'), Js('de Miera'), Js('de Miranda'), Js('de Moço'), Js('de Mobellar'), Js('de Molina'), Js('de Molino'), Js('de Montaluan'), Js('de Montalvo'), Js('de Monterroso'), Js('de Montoya'), Js('de Mora'), Js('de Morales'), Js('de Moscoso'), Js('de Mosquera'), Js('de Moxica'), Js('de Moya'), Js('de Muriel'), Js('de Murio'), Js('de Muxica'), Js('de Naçabal'), Js('de Nabarres'), Js('de Najara'), Js('de Narbona'), Js('de Narraces'), Js('de Navarra'), Js('de Navarrete'), Js('de Oñate'), Js('de Obregon'), Js('de Ocaña'), Js('de Ochavino'), Js('de Olano'), Js('de Olea de Reynoso'), Js('de Olivares'), Js('de Olso'), Js('de Oquellas'), Js('de Orozco'), Js('de Ortega'), Js('de Oviedo'), Js('de Ovierna'), Js('de Padila'), Js('de Padilla'), Js('de Palaçios'), Js('de Palencia'), Js('de Palfox'), Js('de Palia'), Js('de Pallares'), Js('de Palma'), Js('de Panea'), Js('de Parada'), Js('de Paredes'), Js('de Pareja'), Js('de Pasan'), Js('de Pavia'), Js('de Paz'), Js('de Peñafiel'), Js('de Peñalosa'), Js('de Peñaranda'), Js('de Pedrosa'), Js('de Peraça'), Js('de Perales'), Js('de Peralta'), Js('de Perea'), Js('de Pereda'), Js('de Pernia'), Js('de Peteral'), Js('de Piedrayta'), Js('de Pina'), Js('de Pinedo'), Js('de Pisa'), Js('de Pliego'), Js('de Porras'), Js('de Portillo'), Js('de Porto'), Js('de Portugal'), Js('de Presano'), Js('de Puertos'), Js('de Pulgar'), Js('de Quedan'), Js('de Quesada'), Js('de Quevedo'), Js('de Quincoçes'), Js('de Quintana'), Js('de Quintanilla'), Js('de Quintela'), Js('de Quiroga'), Js('de Quiros'), Js('de Quixada'), Js('de Rada'), Js('de Rapariegos'), Js('de Raya'), Js('de Rebina'), Js('de Rebolledo'), Js('de Rey'), Js('de Riba'), Js('de Ribafrecha'), Js('de Ribas Altas'), Js('de Ribera'), Js('de Ribero'), Js('de Riero'), Js('de Rio'), Js('de Rivera'), Js('de Robledo'), Js('de Robles'), Js('de Robredo'), Js('de Robres'), Js('de Rogorraga'), Js('de Rojas'), Js('de Ronda'), Js('de Rosales'), Js('de Rueda'), Js('de Rutia'), Js('de Saabedra'), Js('de Sahagund'), Js('de Salamanca'), Js('de Salares'), Js('de Salas'), Js('de Salazar'), Js('de Salcedo'), Js('de Salinas'), Js('de Salmeron'), Js('de Salonia'), Js('de Salsedo'), Js('de Salvatierra'), Js('de San Blab'), Js('de Sant Biçente'), Js('de Sant Martin'), Js('de Sant Miguel'), Js('de Sant Payo'), Js('de Sant Pedro'), Js('de Sant Roman'), Js('de Santa Ana'), Js('de Santa Cruz'), Js('de Santa Fe'), Js('de Santa Maria'), Js('de Santangel'), Js('de Santillan'), Js('de Santillana'), Js('de Santo Domingo'), Js('de Saravia'), Js('de Sarmiento'), Js('de Sarvia'), Js('de Segovia'), Js('de Segura'), Js('de Sepulveda'), Js('de Sequeda'), Js('de Sese'), Js('de Setiel'), Js('de Sevilla'), Js('de Silva'), Js('de Solares'), Js('de Somonte'), Js('de Sonseca'), Js('de Soria'), Js('de Sosa'), Js('de Soto'), Js('de Sotomayor'), Js('de Sylva'), Js('de Tabares'), Js('de Tagle'), Js('de Talavera'), Js('de Tamayo'), Js('de Taran'), Js('de Tavira'), Js('de Teba'), Js('de Teran'), Js('de Terrazo'), Js('de Texeda'), Js('de Tiedra'), Js('de Titosa'), Js('de Tobar'), Js('de Toledo'), Js('de Tolosa'), Js('de Toquemada'), Js('de Toranço'), Js('de Tordesillas'), Js('de Toro'), Js('de Torre'), Js('de Torreblanca'), Js('de Torrellas'), Js('de Torres'), Js('de Torrijos'), Js('de Tovar'), Js('de Tresana'), Js('de Tresano'), Js('de Tresfuentes'), Js('de Trueva'), Js('de Ugarte'), Js('de Ulloa'), Js('de Ureña'), Js('de Ure'), Js('de Urive'), Js('de Urueña'), Js('de Vaca'), Js('de Valbuena'), Js('de Valdenebro'), Js('de Valdes'), Js('de Valdevieso'), Js('de Valençia'), Js('de Valençihuela'), Js('de Valera'), Js('de Vallego'), Js('de Vallejo'), Js('de Vallesteros'), Js('de Vallodolid'), Js('de Valmeseda'), Js('de Valterra'), Js('de Vaquida'), Js('de Vargas'), Js('de Vascuñana'), Js('de Vega'), Js('de Vegil'), Js('de Velasco'), Js('de Velasquillo'), Js('de Verdesoto'), Js('de Vergara'), Js('de Vic'), Js('de Villa'), Js('de Villacorta'), Js('de Villafrecha'), Js('de Villafuerte'), Js('de Villalpando'), Js('de Villalva'), Js('de Villamanan'), Js('de Villamartin'), Js('de Villandrando'), Js('de Villaneuva'), Js('de Villaquiran'), Js('de Villar'), Js('de Villarrubia'), Js('de Villasante'), Js('de Villaseca'), Js('de Villaverde'), Js('de Villegas'), Js('de Villela'), Js('de Villoria'), Js('de Vio'), Js('de Vique'), Js('de Vire'), Js('de Vittoria'), Js('de Vizcargui'), Js('de Xea'), Js('de Xerez'), Js('de Yaques'), Js('de Yepes'), Js('de Yera'), Js('de Yeres'), Js('de Yllon'), Js('de Ynuricaço'), Js('de Yra'), Js('de Yscar'), Js('de Ysla'), Js('de Ytorrica'), Js('de Zeniçeros'), Js('de la Aguila'), Js('de la Bastida'), Js('de la Carrera'), Js('de la Cava'), Js('de la Cerda'), Js('de la Concha'), Js('de la Corte'), Js('de la Cueva'), Js('de la Escalera'), Js('de la Forsa'), Js('de la Fuente'), Js('de la Hera'), Js('de la Hoz'), Js('de la Huerta'), Js('de la Lança'), Js('de la Mar'), Js('de la Nata'), Js('de la Parra'), Js('de la Peña'), Js('de la Puente'), Js('de la Reina'), Js('de la Riba'), Js('de la Roelas'), Js('de la Rua'), Js('de la Sara'), Js('de la Serna'), Js('de la Torre'), Js('de la Vega'), Js('de la Vorda'), Js('de las Andas'), Js('de las Cuevas'), Js('de las Heras'), Js('de las Osas'), Js('de las Quintanillas'), Js('de los Abcades'), Js('de los Santos'), Js('del Almendral'), Js('del Campo'), Js('del Castellar'), Js('del Castillo'), Js('del Corral'), Js('del Cotrob'), Js('del Espinar'), Js('del Grano'), Js('del Lunar'), Js('del Nero'), Js('del Oyo'), Js('del Peral'), Js('del Rey'), Js('del Rincon'), Js('del Salto'), Js('del Tienplo'), Js('del Valle')]))
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
spanishRenaissance = var.to_python()
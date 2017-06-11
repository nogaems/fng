__all__ = ['argentinianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abran'), Js('Adan'), Js('Adelio'), Js('Adrían'), Js('Adriano'), Js('Agustín'), Js('Agustin'), Js('Alano'), Js('Alanzo'), Js('Alarico'), Js('Alba'), Js('Alberto'), Js('Aldo'), Js('Alejandro'), Js('Alfonso'), Js('Alfredo'), Js('Ali'), Js('Alonso'), Js('Alonzo'), Js('Aluino'), Js('Alvar'), Js('Alvaro'), Js('Alvino'), Js('Amadeo'), Js('Amado'), Js('Ambrosio'), Js('Amoldo'), Js('Anastasio'), Js('Anbessa'), Js('Andrés'), Js('Andreo'), Js('Andres'), Js('Angel'), Js('Angelino'), Js('Angelito'), Js('Angelo'), Js('Anibal'), Js('Anselmo'), Js('Anton'), Js('Antonio'), Js('Aquila'), Js('Aquilino'), Js('Archibaldo'), Js('Arlo'), Js('Armando'), Js('Arnaldo'), Js('Arnoldo'), Js('Arturo'), Js('Ascanio'), Js('Atahualpa'), Js('Atila'), Js('Augusto'), Js('Aureliano'), Js('Aurelio'), Js('Aurelius'), Js('Baltasar'), Js('Barto'), Js('Bartoli'), Js('Bartolo'), Js('Bartolome'), Js('Bartolomeo'), Js('Basilio'), Js('Bautista'), Js('Beinvenido'), Js('Beltran'), Js('Bemabe'), Js('Bembe'), Js('Benedicto'), Js('Benjamín'), Js('Bernardino'), Js('Bernardo'), Js('Berto'), Js('Blanco'), Js('Blas'), Js('Bonifacio'), Js('Bonifaco'), Js('Buinton'), Js('Calvino'), Js('Carlomagno'), Js('Carlos'), Js('Casimiro'), Js('Casta'), Js('Cayetano'), Js('Cedro'), Js('Cesar'), Js('Cesario'), Js('Cesaro'), Js('Chan'), Js('Chano'), Js('Charro'), Js('Chavez'), Js('Chayo'), Js('Che'), Js('Chico'), Js('Ciceron'), Js('Cid'), Js('Cidro'), Js('Cipriano'), Js('Cirilo'), Js('Ciro'), Js('Cisco'), Js('Claudio'), Js('Clodoveo'), Js('Conrado'), Js('Constantino'), Js('Cornelio'), Js('Cortez'), Js('Cris'), Js('Cristian'), Js('Cristiano'), Js('Cristobal'), Js('Cristofer'), Js('Cristofor'), Js('Criston'), Js('Cristos'), Js('Cristoval'), Js('Cruz'), Js('Cuartio'), Js('Cuarto'), Js('Curcio'), Js('Currito'), Js('Curro'), Js('Dacio'), Js('Damario'), Js('Damián'), Js('Damian'), Js('Daniel'), Js('Danilo'), Js('Dantae'), Js('Dante'), Js('Dantel'), Js('Darío'), Js('Dario'), Js('Daunte'), Js('David'), Js('Delmar'), Js('Demario'), Js('Diego'), Js('Domingo'), Js('Eduardo'), Js('Edwardo'), Js('Efrain'), Js('Elia'), Js('Elias'), Js('Elija'), Js('Eloy'), Js('Eluney'), Js('Elvio'), Js('Emanuel'), Js('Emesto'), Js('Emiliano'), Js('Emilio'), Js('Eneas'), Js('Enrique'), Js('Enrrique'), Js('Enzo'), Js('Erasmo'), Js('Ernesto'), Js('Eron'), Js('Esequiel'), Js('Estanislao'), Js('Esteban'), Js('Estefan'), Js('Estevan'), Js('Estevon'), Js('Eugenio'), Js('Evarado'), Js('Everardo'), Js('Ezequiel'), Js('Fabián'), Js('Fabio'), Js('Fabricio'), Js('Facundo'), Js('Fadrique'), Js('Fanuco'), Js('Faro'), Js('Faron'), Js('Faustino'), Js('Fausto'), Js('Federico'), Js('Feliciano'), Js('Felipe'), Js('Felippe'), Js('Felix'), Js('Feo'), Js('Fermín'), Js('Fermin'), Js('Fernán'), Js('Fernando'), Js('Fidel'), Js('Fidele'), Js('Flavio'), Js('Florencio'), Js('Florentino'), Js('Florinio'), Js('Fraco'), Js('Francisco'), Js('Franco'), Js('Frasco'), Js('Frascuelo'), Js('Frederico'), Js('Fresco'), Js('Frisco'), Js('Gabino'), Js('Gabriel'), Js('Gabrio'), Js('Galeno'), Js('Galtero'), Js('Garcia'), Js('Gaspar'), Js('Gaspard'), Js('Gastón'), Js('Generosb'), Js('Geraldo'), Js('Gerardo'), Js('German'), Js('Gervasio'), Js('Gervaso'), Js('Gezane'), Js('Gil'), Js('Gilberto'), Js('Gillermo'), Js('Ginebra'), Js('Ginessa'), Js('Gitana'), Js('Godalupe'), Js('Godfredo'), Js('Godofredo'), Js('Gonzalo'), Js('Gorane'), Js('Gotzone'), Js('Gracia'), Js('Graciana'), Js('Gregoria'), Js('Gregorio'), Js('Guadalupe'), Js('Gualterio'), Js('Guido'), Js('Guillelmina'), Js('Guillermo'), Js('Gustava'), Js('Gustavo'), Js('Héctor'), Js('Hector'), Js('Henriqua'), Js('Heriberto'), Js('Hermosa'), Js('Hernán'), Js('Hernan'), Js('Hernandez'), Js('Hernando'), Js('Hidalgo'), Js('Hilario'), Js('Hipolito'), Js('Horado'), Js('Hortencia'), Js('Hugo'), Js('Humberto'), Js('Iago'), Js('Idoia'), Js('Idurre'), Js('Ignacia'), Js('Ignacio'), Js('Ignado'), Js('Ignazio'), Js('Igone'), Js('Ikerne'), Js('Ileanna'), Js('Iliana'), Js('Jairo'), Js('Isidoro'), Js('Iván'), Js('Javier'), Js('Javiero'), Js('Jax'), Js('Jerardo'), Js('Jeremías'), Js('Jeremias'), Js('Jerico'), Js('Jerold'), Js('Jeronimo'), Js('Jerrald'), Js('Jerrold'), Js('Jesus'), Js('Joaquín'), Js('Joaquin'), Js('Jonas'), Js('Jorge'), Js('José'), Js('José Luis'), Js('José María'), Js('Jose'), Js('Joselito'), Js('Josias'), Js('Josue'), Js('Juan'), Js('Juan Bautista'), Js('Juan Carlos'), Js('Juan Cruz'), Js('Juan Domingo'), Js('Juan José'), Js('Juan Manuel'), Js('Juan Martín'), Js('Juan Pablo'), Js('Juan Pedro'), Js('Juanito'), Js('Julián'), Js('Julian'), Js('Juliano'), Js('Julio'), Js('Julio César'), Js('Justino'), Js('Justo'), Js('Kemen'), Js('Ladislao'), Js('Lalo'), Js('Lautaro'), Js('Lazaro'), Js('León'), Js('Leandro'), Js('Leon'), Js('Leonardo'), Js('Leonel'), Js('Leonides'), Js('Leopoldo'), Js('Lia'), Js('Lisandro'), Js('Lobo'), Js('Lonzo'), Js('Lorenzo'), Js('Lucas'), Js('Lucero'), Js('Luciano'), Js('Lucila'), Js('Lucio'), Js('Luis'), Js('Macario'), Js('Macerio'), Js('Mannie'), Js('Mano'), Js('Manolito'), Js('Manolo'), Js('Manuel'), Js('Manuelo'), Js('Marcelo'), Js('Marco'), Js('Marcos'), Js('Mariano'), Js('Mario'), Js('Marquez'), Js('Martín'), Js('Martin'), Js('Martinez'), Js('Martino'), Js('Matías'), Js('Mateo'), Js('Matias'), Js('Matro'), Js('Maureo'), Js('Mauricio'), Js('Mauro'), Js('Maximiliano'), Js('Maximo'), Js('Miguel'), Js('Milagro'), Js('Milton'), Js('Mio'), Js('Moises'), Js('Montae'), Js('Montay'), Js('Monte'), Js('Montego'), Js('Montel'), Js('Montenegro'), Js('Montes'), Js('Montez'), Js('Montrel'), Js('Montrell'), Js('Montrelle'), Js('Néstor'), Js('Nahuel'), Js('Naldo'), Js('Natal'), Js('Natalio'), Js('Natanael'), Js('Nataniel'), Js('Navarro'), Js('Nehuen'), Js('Nemesio'), Js('Neron'), Js('Nesto'), Js('Nestor'), Js('Neto'), Js('Nevada'), Js('Nicanor'), Js('Nicolás'), Js('Nicolas'), Js('Niguel'), Js('Noe'), Js('Norberto'), Js('Normando'), Js('Oliverio'), Js('Oliverios'), Js('Omar'), Js('Onofre'), Js('Orlan'), Js('Orland'), Js('Orlando'), Js('Orlin'), Js('Orlondo'), Js('Oro'), Js('Oscar'), Js('Osvaldo'), Js('Ovidio'), Js('Pablo'), Js('Pacho'), Js('Paco'), Js('Pacorro'), Js('Palben'), Js('Pancho'), Js('Pascual'), Js('Pasqual'), Js('Patricio'), Js('Patricio'), Js('Patrido'), Js('Paz'), Js('Pedro'), Js('Pepe'), Js('Pirro'), Js('Placido'), Js('Platon'), Js('Porfirio'), Js('Porfiro'), Js('Primeiro'), Js('Prospero'), Js('Pueblo'), Js('Quin'), Js('Quinto'), Js('Quito'), Js('Raúl'), Js('Rafael'), Js('Rafe'), Js('Rai'), Js('Raimundo'), Js('Ramirez'), Js('Ramiro'), Js('Ramon'), Js('Ramone'), Js('Raul'), Js('Raulo'), Js('Rayman'), Js('Raymon'), Js('Renaldo'), Js('Renato'), Js('Reno'), Js('Rey'), Js('Reyes'), Js('Reynaldo'), Js('Reynardo'), Js('Ricardo'), Js('Richie'), Js('Rico'), Js('Rio'), Js('Ritchie'), Js('Roano'), Js('Roberto'), Js('Rodas'), Js('Roderigo'), Js('Rodolfo'), Js('Rodrigo'), Js('Rogelio'), Js('Roldan'), Js('Roman'), Js('Romano'), Js('Romeo'), Js('Ronaldo'), Js('Roque'), Js('Rosario'), Js('Ruben'), Js('Rufio'), Js('Rufo'), Js('Sabino'), Js('Sal'), Js('Salbatore'), Js('Salomon'), Js('Salvador'), Js('Salvadore'), Js('Salvatore'), Js('Salvino'), Js('Samuel'), Js('Sancho'), Js('Sandro'), Js('Santiago'), Js('Santino'), Js('Santo'), Js('Santos'), Js('Saturnin'), Js('Saul'), Js('Sebastián'), Js('Sebastian'), Js('Sebastiano'), Js('Segundo'), Js('Sein'), Js('Senon'), Js('Serafin'), Js('Sergio'), Js('Severo'), Js('Silverio'), Js('Silvino'), Js('Silvio'), Js('Simón'), Js('Socorro'), Js('Sol'), Js('Stefano'), Js('Suelita'), Js('Tabor'), Js('Tadeo'), Js('Tajo'), Js('Taurino'), Js('Tauro'), Js('Tavio'), Js('Tejano'), Js('Teo'), Js('Teodor'), Js('Teodoro'), Js('Terciero'), Js('Teyo'), Js('Thiago'), Js('Tiago'), Js('Timo'), Js('Timoteo'), Js('Tito'), Js('Tobias'), Js('Toli'), Js('Tomás'), Js('Tomas'), Js('Tonio'), Js('Toro'), Js('Tulio'), Js('Turi'), Js('Ulises'), Js('Ulrich'), Js('Urbano'), Js('Víctor'), Js('Valentin'), Js('Veto'), Js('Vicente'), Js('Victor'), Js('Victoriano'), Js('Victorino'), Js('Victorio'), Js('Victoro'), Js('Vidal'), Js('Videl'), Js('Vincente'), Js('Virgilio'), Js('Wenceslao'), Js('Yaguatí')]))
var.put('nm2', Js([Js('Ámbar'), Js('Ángeles'), Js('Abadora'), Js('Abril'), Js('Adriana'), Js('Agostina'), Js('Ailin'), Js('Alén'), Js('Alegra'), Js('Alejandra'), Js('Alelí'), Js('Alessa'), Js('Alicia'), Js('Alina'), Js('Alma'), Js('Amaike'), Js('Amakáik '), Js('Amancay'), Js('Amanda'), Js('Ana'), Js('Ana Lía'), Js('Ana Laura'), Js('Anabela'), Js('Anahí'), Js('Analía'), Js('Analisa'), Js('Anamaría'), Js('Andrea'), Js('Antonella'), Js('Araceli'), Js('Arcadia'), Js('Arcelia'), Js('Arcilla'), Js('Arella'), Js('Aricela'), Js('Ariela'), Js('Armanda'), Js('Armena'), Js('Artemisia'), Js('Artura'), Js('Ascencion'), Js('Asianah '), Js('Asuncion'), Js('Atalaya'), Js('Athalia'), Js('Aura'), Js('Aurelia'), Js('Aureliana'), Js('Aurkena'), Js('Aurkene'), Js('Aurora'), Js('Ayelén'), Js('Azucena'), Js('Azul'), Js('Azura'), Js('Beatrisa'), Js('Beatriz'), Js('Belen'), Js('Belgis'), Js('Belicia'), Js('Belinda'), Js('Belita'), Js('Bella'), Js('Benigna'), Js('Benita'), Js('Berenice'), Js('Bernicia'), Js('Berta'), Js('Bertha'), Js('Betiana'), Js('Bibiana'), Js('Bienvenida'), Js('Blanca'), Js('Blandina'), Js('Blasa'), Js('Bonita'), Js('Brandye '), Js('Brigida'), Js('Brigidia'), Js('Brisa'), Js('Brisha'), Js('Brisia'), Js('Brissa'), Js('Briza'), Js('Bryssa'), Js('Buena'), Js('Calandria'), Js('Calida'), Js('Calvina'), Js('Camila'), Js('Candela'), Js('Candelaria'), Js('Candi'), Js('Candida'), Js('Candie'), Js('Cari'), Js('Carilla'), Js('Carisa'), Js('Carla'), Js('Carleigha '), Js('Carletta'), Js('Carlita'), Js('Carlota'), Js('Carlotta'), Js('Carmela'), Js('Carmelita'), Js('Carmen'), Js('Carmencita'), Js('Carmina'), Js('Carminda'), Js('Carmita'), Js('Carola'), Js('Carolina'), Js('Carona'), Js('Carrola'), Js('Casandra'), Js('Casey'), Js('Cassandra '), Js('Casta'), Js('Catalin'), Js('Catalina'), Js('Catarina'), Js('Cayetana'), Js('Cecilia'), Js('Ceibo'), Js('Celerina'), Js('Celesta'), Js('Celeste'), Js('Celestina'), Js('Cenobia'), Js('Ceri'), Js('Ceria'), Js('Cesara'), Js('Chalina'), Js('Chamayra '), Js('Charo'), Js('Chavela'), Js('Chavelle'), Js('Chaya'), Js('Cheena '), Js('Chela'), Js('Chica'), Js('Chiquita'), Js('Chrisanna'), Js('Chrisanne'), Js('Christina'), Js('Chrysann'), Js('Cielo'), Js('Cierra'), Js('Cionnaye '), Js('Cipriana'), Js('Cira'), Js('Ciri'), Js('Clara'), Js('Clareta'), Js('Clarinda'), Js('Clarisa'), Js('Clarissa'), Js('Claudia'), Js('Clementina'), Js('Clodovea'), Js('Coco'), Js('Coleta'), Js('Concepcion'), Js('Concetta'), Js('Conchetta'), Js('Conshita'), Js('Consolacion'), Js('Consolata'), Js('Constantia'), Js('Constanza'), Js('Consuela'), Js('Consuelo'), Js('Coraly '), Js('Corazana'), Js('Corazon'), Js('Crisann'), Js('Crisanna'), Js('Crista'), Js('Cristina'), Js('Cristine'), Js('Crotilda'), Js('Cyntia'), Js('Dalila'), Js('Damita'), Js('Dana'), Js('Dani'), Js('Daniela'), Js('Danita'), Js('Daria'), Js('Dayami '), Js('Dayanara '), Js('Deiene'), Js('Deikun'), Js('Deina'), Js('Delcine'), Js('Delfina'), Js('Delma'), Js('Delmar'), Js('Delmara'), Js('Delphia'), Js('Denisa'), Js('Desideria'), Js('Destina'), Js('Devera'), Js('Dia'), Js('Diega'), Js('Digna'), Js('Dina'), Js('Dinora'), Js('Dionis'), Js('Dionisa'), Js('Dita'), Js('Dolores'), Js('Dolorita'), Js('Domenica'), Js('Dominga'), Js('Dominica'), Js('Dona'), Js('Dora'), Js('Dorbeta'), Js('Dorinda'), Js('Dorotea'), Js('Dreena'), Js('Drina Duena'), Js('Dukine'), Js('Dukinea'), Js('Dulce'), Js('Dulcea'), Js('Dulcina'), Js('Dulcinea'), Js('Dulcinia'), Js('Earlena'), Js('Earlene'), Js('Earlina'), Js('Edenia'), Js('Edita'), Js('Elba'), Js('Elbertina'), Js('Eldora'), Js('Eleadora'), Js('Eleanora'), Js('Eleena'), Js('Elena'), Js('Eleonora'), Js('Eliana'), Js('Elina'), Js('Elisa'), Js('Eliza'), Js('Elizabeth'), Js('Ella'), Js('Elodia'), Js('Eloisa'), Js('Elsa'), Js('Elvera'), Js('Elvia'), Js('Elvira'), Js('Elvita'), Js('Ema'), Js('Emerald'), Js('Emesta'), Js('Emilia'), Js('Emilie'), Js('Emily '), Js('Encarnacion'), Js('Engracia'), Js('Enrica'), Js('Enriqua'), Js('Enriqueta'), Js('Erendira'), Js('Erendiria'), Js('Erlene'), Js('Erlina'), Js('Ernesta'), Js('Eskama'), Js('Esma'), Js('Esmeralda'), Js('Esmerelda'), Js('Esperanza'), Js('Estebana'), Js('Estefana'), Js('Estefani'), Js('Estefania'), Js('Estefany'), Js('Estela'), Js('Estelita'), Js('Estella'), Js('Estelle '), Js('Estephanie'), Js('Ester'), Js('Esteva'), Js('Estralita'), Js('Estrella'), Js('Estrellita'), Js('Eufemia'), Js('Eugenia'), Js('Eva'), Js('Eva-Yolanda'), Js('Evalisse '), Js('Evangelina'), Js('Evelin'), Js('Evita'), Js('Exaltacion'), Js('Ezmeralda'), Js('Fabiana'), Js('Fabiola'), Js('Faqueza'), Js('Fausta'), Js('Faustina'), Js('Felicita'), Js('Felicitas'), Js('Felisa'), Js('Fermina'), Js('Fernanda'), Js('Fidelia'), Js('Fidelina'), Js('Filipa'), Js('Fiorela'), Js('Flaca'), Js('Flor'), Js('Floramaria'), Js('Florencia'), Js('Florentina'), Js('Florida'), Js('Florinia'), Js('Florita'), Js('Fonda'), Js('Fortuna'), Js('Francisca'), Js('Freira'), Js('Frescura'), Js('Fresia'), Js('Gabriela'), Js('Gabriella'), Js('Gala'), Js('Galena'), Js('Galenia'), Js('Garabina'), Js('Garabine'), Js('Garaitz'), Js('Garbina'), Js('Garbine'), Js('Gaspara'), Js('Geavonna'), Js('Gechina'), Js('Generosa'), Js('Genevalisse '), Js('Gertrudes'), Js('Gertrudis'), Js('Gezana'), Js('Gloria'), Js('Graciela'), Js('Grazia'), Js('Grizelda'), Js('Guadalupe'), Js('Guanina '), Js('Guillermina'), Js('Guliana'), Js('Helena'), Js('Heriberto '), Js('Huilén'), Js('Idalyz '), Js('Iliana'), Js('Iluminada'), Js('Imelda'), Js('Immaculada'), Js('Inés'), Js('Ines'), Js('Inez'), Js('Inocencia'), Js('Inoceneia'), Js('Inocenta'), Js('Iratze'), Js('Irene'), Js('Irma'), Js('Irune'), Js('Irupé'), Js('Isabel'), Js('Isabela'), Js('Isabella'), Js('Isi'), Js('Isidora'), Js('Itatí'), Js('Itsaso'), Js('Itxaro'), Js('Ivelisse '), Js('Ivette'), Js('Ivonne'), Js('Izar'), Js('Izarra'), Js('Izarre'), Js('Izazkun'), Js('JaJuan '), Js('Jacarandá'), Js('Jacinta'), Js('Jade'), Js('Jaione'), Js('Jakinda'), Js('Janisa '), Js('Jasone'), Js('Javier '), Js('Javiera'), Js('Jerrely '), Js('Jesenia '), Js('Jesusa'), Js('Jimena'), Js('Joaquina'), Js('Jolie'), Js('Jomayra '), Js('Jordana'), Js('Jorgelina'), Js('Josefa'), Js('Josefina'), Js('Josune'), Js('Jovana'), Js('Jovanna'), Js('Jovena'), Js('Jovina'), Js('Jovita'), Js('Juana'), Js('Juandalynn'), Js('Juanetta'), Js('Juanisha'), Js('Juanita'), Js('Judith '), Js('Julia'), Js('Juliana'), Js('Julieta'), Js('Julina'), Js('Karelma '), Js('Karina'), Js('Karmen'), Js('Katia'), Js('Katya'), Js('Kemena'), Js('Kemina'), Js('Kesara'), Js('Kesare'), Js('Kiki'), Js('Kita'), Js('Kristina'), Js('LaCienega'), Js('Ladonna'), Js('Lala'), Js('Lali'), Js('Lalia'), Js('Laline '), Js('Lalla'), Js('Lana'), Js('Landa'), Js('Landrada'), Js('Lara'), Js('Lareina'), Js('Larunda'), Js('Laura'), Js('Laurana'), Js('Laurencia'), Js('Laurinda'), Js('Laurita'), Js('Lavina'), Js('Lea'), Js('Leahonia'), Js('Leala'), Js('Leandra'), Js('Legarre'), Js('Leila'), Js('Leira'), Js('Lela'), Js('Lenora'), Js('Leonor'), Js('Leonora'), Js('Lera'), Js('Leticia'), Js('Letitia'), Js('Letizia'), Js('Levina'), Js('Leya'), Js('Lia'), Js('Liana'), Js('Lihuén'), Js('Lilen'), Js('Lilia'), Js('Liliana'), Js('Linda'), Js('Llesenia'), Js('Lluvia'), Js('Lola'), Js('Loleta'), Js('Lolita'), Js('Lolitta'), Js('Lora'), Js('Lorda'), Js('Lore'), Js('Lorena'), Js('Loretta'), Js('Lourdes'), Js('Louredes'), Js('Lucía'), Js('Lucena'), Js('Luciana'), Js('Lucila'), Js('Lucita'), Js('Lucrecia'), Js('Ludmila'), Js('Luella'), Js('Luisa'), Js('Luiza'), Js('Luján'), Js('Luna'), Js('Lupe'), Js('Lupita'), Js('Lur'), Js('Luvenia'), Js('Luvina'), Js('Luz'), Js('Mónica'), Js('Madalena'), Js('Madalynn'), Js('Madeira'), Js('Madelynn'), Js('Madena'), Js('Madia'), Js('Madina'), Js('Madre'), Js('Madrona'), Js('Maela '), Js('Mafalda'), Js('Magalys '), Js('Magdalen'), Js('Magdalena'), Js('Magdalene'), Js('Mailen'), Js('Maite'), Js('Maitea'), Js('Maja'), Js('Malaya'), Js('Malena'), Js('Malia'), Js('Malita'), Js('Mallorie '), Js('Malvina'), Js('Manda'), Js('Manoela'), Js('Manuela'), Js('María'), Js('María Belén'), Js('María Cecilia'), Js('María Celeste'), Js('María Fátima'), Js('María Itatí'), Js('María Marta'), Js('María Pilar'), Js('María del Carmen'), Js('María del Luján'), Js('María del Mar'), Js('María del Rosario'), Js('Marcela'), Js('Marelys '), Js('Margarita'), Js('Maria'), Js('Mariana'), Js('Marianela'), Js('Marianella'), Js('Maribel'), Js('Maricel'), Js('Maricela'), Js('Maricelia'), Js('Maricella'), Js('Maricruz'), Js('Mariela'), Js('Marietta'), Js('Marilu'), Js('Mariquita'), Js('Marisa '), Js('Marisela'), Js('Marisol'), Js('Maritza '), Js('Marlina'), Js('Marquilla'), Js('Marta'), Js('Martha'), Js('Martina'), Js('Materia'), Js('Matia'), Js('Maxima'), Js('Maya'), Js('Mayra-Liz '), Js('Melisenda'), Js('Melita'), Js('Melosa'), Js('Melosia'), Js('Mendi'), Js('Mercedes'), Js('Micaela'), Js('Michaela'), Js('Michelle'), Js('Migdalia '), Js('Mikaela'), Js('Milagritos'), Js('Milagro'), Js('Milagros'), Js('Milagrosa'), Js('Mimi'), Js('Mirabel'), Js('Miranda'), Js('Mirari'), Js('Mireya'), Js('Mirta'), Js('Modesta'), Js('Modeste'), Js('Molara'), Js('Monaique '), Js('Monica'), Js('Monita'), Js('Mora'), Js('Morisa'), Js('Morissa'), Js('Moya'), Js('Muriel'), Js('Myra'), Js('Naiara'), Js('Nailea'), Js('Nalda'), Js('Nana'), Js('Narcisa'), Js('Natacha'), Js('Natalia'), Js('Natividad'), Js('Nautica '), Js('Neiva'), Js('Nekana'), Js('Nekane'), Js('Nelia'), Js('Nelida'), Js('Nerea'), Js('Nerita'), Js('Neta'), Js('Neva'), Js('Nevada'), Js('Nicanora'), Js('Nieve'), Js('Nina'), Js('Nita'), Js('Nixzaliz '), Js('Noelia'), Js('Noemi'), Js('Norma '), Js('Novia'), Js('Odanda'), Js('Ofelia'), Js('Oihane'), Js('Olademis'), Js('Olinda'), Js('Oliveria'), Js('Olivia'), Js('Ora'), Js('Orquidia'), Js('Osana'), Js('Pía'), Js('Pabla'), Js('Paciencia'), Js('Palba'), Js('Palma'), Js('Palmira'), Js('Paloma'), Js('Paola'), Js('Paquita'), Js('Pasha'), Js('Pastora'), Js('Patricia'), Js('Paula'), Js('Paulita'), Js('Paz'), Js('Pedra'), Js('Pepita'), Js('Perfecta'), Js('Pia'), Js('Pilar'), Js('Pitina'), Js('Placenta'), Js('Placida'), Js('Presencia'), Js('Presta'), Js('Primavera'), Js('Prudencia'), Js('Puebla'), Js('Pura'), Js('Pureza'), Js('Purisima'), Js('Querida'), Js('Quinta'), Js('Raimunda'), Js('Raina'), Js('Ramira'), Js('Ramona'), Js('Raquel'), Js('Regina'), Js('Reia'), Js('Reina'), Js('Remedios'), Js('Renata'), Js('Reya'), Js('Reyna'), Js('Ria'), Js('Rica'), Js('Ricarda'), Js('Rio'), Js('Rita'), Js('Roana'), Js('Roberta'), Js('Rocio'), Js('Roderiga'), Js('Roja'), Js('Roldana'), Js('Romana'), Js('Romina'), Js('RosIyn'), Js('Rosa'), Js('Rosalia'), Js('Rosalind'), Js('Rosalinda'), Js('Rosalinde'), Js('Rosaline'), Js('Rosalyn'), Js('Rosamar'), Js('Rosamaria'), Js('Rosario'), Js('Rosemarie'), Js('Roz'), Js('Rufa'), Js('Rufina'), Js('Sabana'), Js('Sabina'), Js('Sabrina'), Js('Salbatora'), Js('Salma'), Js('Salvadora'), Js('Samanta'), Js('Sancha'), Js('Sancia'), Js('Sara'), Js('Sarita'), Js('Saturnina'), Js('Savanna'), Js('Savannah'), Js('Segunda'), Js('Seina'), Js('Senalda'), Js('Senona'), Js('Serafina'), Js('Serena'), Js('Sevilla'), Js('Shoshana'), Js('Sierra'), Js('Silvana'), Js('Silvia'), Js('Silvina'), Js('Simona'), Js('Socorro'), Js('Sofía'), Js('Sofia'), Js('Sol'), Js('Solana'), Js('Solange'), Js('Soledad'), Js('Soledada'), Js('Solymar'), Js('Sonora'), Js('Stella Maris'), Js('Suelita'), Js('Susana'), Js('Suyai'), Js('Suzelly'), Js('Tabora'), Js('Tamara'), Js('Tanis'), Js('Tea'), Js('Tejana'), Js('Telma'), Js('Teodora'), Js('Terceira'), Js('Teresa'), Js('Teresita'), Js('Thaimy '), Js('Thalia'), Js('Tia'), Js('Tierra'), Js('Tranquilla'), Js('Trella'), Js('Tulia'), Js('Ula'), Js('Uma'), Js('Ursulina'), Js('Usoa'), Js('Valencia'), Js('Valentina'), Js('Valeria'), Js('Vanesa'), Js('Ventana'), Js('Ventura'), Js('Verónica'), Js('Verda'), Js('Verdad'), Js('Veronica'), Js('Veta'), Js('Vicenta'), Js('Victoria'), Js('Vina'), Js('Violeta'), Js('Vionaika '), Js('Virginia'), Js('Viridiana'), Js('Vittoria'), Js('Viviana'), Js('Waleska '), Js('Wanda'), Js('Xalbadora'), Js('Xalvadora'), Js('Xaviera'), Js('Xenia'), Js('Xevera'), Js('Xeveria'), Js('Xiomara'), Js('Xiomarys '), Js('Xochitl'), Js('Xuxa'), Js('Yadra'), Js('Yaineris '), Js('Yaira '), Js('Yajaira'), Js('Yanamaria'), Js('Yaneisy'), Js('Yanely'), Js('Yanire '), Js('Yara'), Js('Yara '), Js('Yashira'), Js('Yedid'), Js('Yelina '), Js('Yesenia'), Js('Yizel'), Js('Yoana'), Js('Yolanda'), Js('Yonaidys '), Js('Yosdalkis '), Js('Yumaris'), Js('Yuricema '), Js('Yvonne'), Js('Zaira'), Js('Zamora'), Js('Zandra'), Js('Zaneta'), Js('Zanetta'), Js('Zanita'), Js('Zapopa'), Js('Zarita'), Js('Zaviera'), Js('Zita'), Js('Zuleika'), Js('Zumac'), Js('Zurina'), Js('Zurine')]))
var.put('nm3', Js([Js('Álvarez'), Js('Ávila'), Js('Acosta'), Js('Acuña'), Js('Acuna'), Js('Agüero'), Js('Aguilar'), Js('Aguirre'), Js('Al Sadd'), Js('Albarez'), Js('Alonso'), Js('Alvarez'), Js('Angelo'), Js('Arce'), Js('Arcuri'), Js('Arias'), Js('Auriemma'), Js('Autino'), Js('Avelardez'), Js('Baggio'), Js('Baresi'), Js('Barrios'), Js('Baumann'), Js('Belasio'), Js('Bellucci'), Js('Benítez'), Js('Beneventi'), Js('Benitez'), Js('Beuchene'), Js('Bianchi'), Js('Blanco'), Js('Boedo'), Js('Bogatzian'), Js('Boni'), Js('Borroni'), Js('Bravo'), Js('Bregmann'), Js('Bruno'), Js('Buccho'), Js('Bullrich'), Js('Cáceres'), Js('Córdoba'), Js('Cabrera'), Js('Caceres'), Js('Calvo'), Js('Campos'), Js('Capon'), Js('Cardozo'), Js('Carrizo'), Js('Castiglione'), Js('Castillo'), Js('Castro'), Js('Chávez'), Js('Cocci'), Js('Cohen'), Js('Colombo'), Js('Conti'), Js('Cordero'), Js('Coronel'), Js('Correa'), Js('Costa'), Js('Cruz'), Js('Díaz'), Js("D'Onofrio"), Js('Davide'), Js('De Luca'), Js('De Marco'), Js('De la Cruz'), Js('DeRose'), Js('Delgado'), Js('Dellucci'), Js('Devia'), Js('Di Donato'), Js('Di Natale'), Js('Di Stefano'), Js('Diaz'), Js('Domínguez'), Js('Dominguez'), Js('Duarte'), Js('Dukaroff'), Js('Echeverria'), Js('Endrizzi'), Js('Escobar'), Js('Esposito'), Js('Falcone'), Js('Fallaci'), Js('Fanucci'), Js('Farías'), Js('Feimann'), Js('Fernández'), Js('Fernandez'), Js('Ferrari'), Js('Ferreyra'), Js('Ferri'), Js('Fetuccini'), Js('Figueroa'), Js('Fiorentino'), Js('Flores'), Js('Folliero'), Js('Franco'), Js('French'), Js('Gómez'), Js('Gallo'), Js('García'), Js('Garcia'), Js('Gashi'), Js('Genovese'), Js('Genz'), Js('Gershkovich'), Js('Gil'), Js('Giménez'), Js('Gimenez'), Js('Giordano'), Js('Godoy'), Js('Gomez'), Js('González'), Js('Gonzalez'), Js('Gonzalezs'), Js('Greco'), Js('Grimoldi'), Js('Gutiérrez'), Js('Gutierrez'), Js('Guzmán'), Js('Guzman'), Js('Halder'), Js('Hernández'), Js('Hernandez'), Js('Herrera'), Js('Hirigoyen'), Js('Hoffman'), Js('Iadanza'), Js('Ibáñez'), Js('Ibañez'), Js('Ibanez'), Js('Iglesias'), Js('Juárez'), Js('Juarez'), Js('Kämpfer'), Js('Kirchner'), Js('López'), Js('Lacroze'), Js('Lavezzi'), Js('Ledesma'), Js('Leguizamón'), Js('Leiva'), Js('Lettiere'), Js('Li Fonti'), Js('Lo Duca'), Js('Loggia'), Js('Lombardi'), Js('Lombardo'), Js('Longo'), Js('Lopez'), Js('Lorenzo'), Js('Lori'), Js('Lousteau'), Js('Lucciano'), Js('Lucero'), Js('Luna'), Js('Méndez'), Js('Maidana'), Js('Malavia'), Js('Maldonado'), Js('Mancini'), Js('Manfrin'), Js('Manna'), Js('Mansilla'), Js('Marcelo'), Js('March'), Js('Marchesi'), Js('Marino'), Js('Martín'), Js('Martínez'), Js('Martin'), Js('Martinez'), Js('Mazzanti'), Js('Mazzi'), Js('Medina'), Js('Mele'), Js('Mendez'), Js('Mendoza'), Js('Milani'), Js('Milano'), Js('Miniati'), Js('Miranda'), Js('Molina'), Js('Monaldo'), Js('Montenegro'), Js('Morales'), Js('Moreau'), Js('Moreno'), Js('Moretti'), Js('Mosconi'), Js('Moyano'), Js('Muñoz'), Js('Munoz'), Js('Núñez'), Js('Núnez'), Js('Nair'), Js('Napolitano'), Js('Narzecian'), Js('Navarro'), Js('Nuñez'), Js('Nucci'), Js('Nunez'), Js('Ojeda'), Js('Olivera'), Js('Olleros'), Js('Onio'), Js('Ortíz'), Js('Ortiz'), Js('Otero'), Js('Páez'), Js('Pérez'), Js('Pagnotto'), Js('Palazzo'), Js('Palermo'), Js('Panicucci'), Js('Paz'), Js('Pazarella'), Js('Pellegrini'), Js('Peralta'), Js('Pereira'), Js('Pereyra'), Js('Perez'), Js('Pestalozzi'), Js('Piazza'), Js('Piccio'), Js('Pinto'), Js('Pirozzi'), Js('Pisani'), Js('Pisano'), Js('Ponce'), Js('Prieto'), Js('Pugliesi'), Js('Quiroga'), Js('Ríos'), Js('Ramírez'), Js('Ramirez'), Js('Ramos'), Js('Rey'), Js('Ricci'), Js('Rios'), Js('Rivas'), Js('Rivera'), Js('Rivero'), Js('Rizzo'), Js('Roca'), Js('Rodríguez'), Js('Rodriguez'), Js('Rojas'), Js('Roldán'), Js('Romano'), Js('Romero'), Js('Rossi'), Js('Rousse'), Js('Ruiz'), Js('Russo'), Js('Sánchez'), Js('Sabbatini'), Js('Sabella'), Js('Sagese'), Js('Sal'), Js('Sanchez'), Js('Santos'), Js('Scalabrini'), Js('Schiavone'), Js('Schmidt'), Js('Siciliano'), Js('Silva'), Js('Simone'), Js('Soria'), Js('Sosa'), Js('Soto'), Js('Suárez'), Js('Suarez'), Js('Tarella'), Js('Tocci'), Js('Toledo'), Js('Torres'), Js('Toscani'), Js('Toscano'), Js('Trevisan'), Js('Trevisani'), Js('Udinese'), Js('Udinesi'), Js('Urquiza'), Js('Vásquez'), Js('Vázquez'), Js('Valdéz'), Js('Varela'), Js('Vargas'), Js('Vazquez'), Js('Vecoli'), Js('Vega'), Js('Vera'), Js('Vidal'), Js('Villalba'), Js('Villar'), Js('Von Brocken'), Js('Zetticci'), Js('Zito')]))
pass
pass


# Add lib to the module scope
argentinianNames = var.to_python()
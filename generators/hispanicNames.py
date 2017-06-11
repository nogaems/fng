__all__ = ['hispanicNames']

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
var.put('nm1', Js([Js('Álvaro'), Js('Ángel'), Js('Édgar'), Js('Óliver'), Js('Óscar'), Js('Aarón'), Js('Aaron'), Js('Abel'), Js('Abraham'), Js('Abram'), Js('Adán'), Js('Adrián'), Js('Agustín'), Js('Alan'), Js('Alberto'), Js('Alejandro'), Js('Alex'), Js('Alexander'), Js('Alexis'), Js('Alfonso'), Js('Alfredo'), Js('Alonso'), Js('Alonzo'), Js('Andrés'), Js('Angel'), Js('Anthony'), Js('Antonio'), Js('Armando'), Js('Arturo'), Js('Axel'), Js('Bautista'), Js('Benito'), Js('Benjamín'), Js('Bernabé'), Js('Bruno'), Js('César'), Js('Camilo'), Js('Carlos'), Js('Carmelo'), Js('Christian'), Js('Christopher'), Js('Cristóbal'), Js('Cristian'), Js('Dídac'), Js('Damián'), Js('Daniel'), Js('Dante'), Js('David'), Js('Diego'), Js('Diego Alejandro'), Js('Domingo'), Js('Dylan'), Js('Edmundo'), Js('Eduardo'), Js('Efraim'), Js('Efrain'), Js('Elías'), Js('Eliseo'), Js('Emanuel'), Js('Emiliano'), Js('Emilio'), Js('Emmanuel'), Js('Enrique'), Js('Erick'), Js('Ernesto'), Js('Esteban'), Js('Estefania'), Js('Eustacio'), Js('Ezequiel'), Js('Fabián'), Js('Facundo'), Js('Felipe'), Js('Felix'), Js('Fernando'), Js('Francisco'), Js('Franco'), Js('Gabriel'), Js('Gael'), Js('Gerardo'), Js('Gonzalo'), Js('Guillermo'), Js('Gustavo'), Js('Héctor'), Js('Hector'), Js('Hugo'), Js('Ian'), Js('Ignacio'), Js('Iker'), Js('Inhué'), Js('Isaías'), Js('Isaac'), Js('Isidoro'), Js('Ismael'), Js('Israel'), Js('Iván'), Js('Ivan'), Js('Jacobo'), Js('Jaime'), Js('Jairo'), Js('Javier'), Js('Jerónimo'), Js('Jeremías'), Js('Jesús'), Js('Jesus'), Js('Joaquín'), Js('Joaquin'), Js('Joel'), Js('Jonatán'), Js('Jonathan'), Js('Jorge'), Js('José'), Js('Jose'), Js('Joshua'), Js('Josué'), Js('Juan'), Js('Juan Andrés'), Js('Juan David'), Js('Juan Diego'), Js('Juan Esteban'), Js('Juan José'), Js('Juan Manuel'), Js('Juan Martín'), Js('Juan Pablo'), Js('Juan Sebastián'), Js('Juanita'), Js('Julián'), Js('Julian'), Js('Julio'), Js('Justin'), Js('Kevin'), Js('Kimberly'), Js('Lautaro'), Js('Leonardo'), Js('Lorenzo'), Js('Luca'), Js('Lucas'), Js('Lucho'), Js('Lucián'), Js('Luciano'), Js('Luis'), Js('Luz'), Js('Máximo'), Js('Macos'), Js('Manuel'), Js('Marco'), Js('Marcos'), Js('Mariano'), Js('Mario'), Js('Martín'), Js('Martin'), Js('Matías'), Js('Mateo'), Js('Matthew'), Js('Mauricio'), Js('Max'), Js('Maximiliano'), Js('Miguel'), Js('Miguel Ángel'), Js('Milagros'), Js('Moises'), Js('Nico'), Js('Nicolás'), Js('Orlando'), Js('Oscar'), Js('Paúl'), Js('Pablo'), Js('Pascual'), Js('Patricio'), Js('Pedro'), Js('Primitivo'), Js('Raúl'), Js('Rafael'), Js('Ramón'), Js('Ramon'), Js('Raul'), Js('Ricardo'), Js('Rigoberto'), Js('Roberto'), Js('Rodrigo'), Js('Rolando'), Js('Román'), Js('Rubén'), Js('Saúl'), Js('Salvador'), Js('Samuel'), Js('Santiago'), Js('Santino'), Js('Sebastián'), Js('Sebastian'), Js('Serafín'), Js('Sergio'), Js('Simón'), Js('Stefano'), Js('Thiago'), Js('Tobías'), Js('Tomás'), Js('Tomas'), Js('Umberto'), Js('Víctor'), Js('Valentín'), Js('Valentino'), Js('Vicente'), Js('Xavier'), Js('Zacarías')]))
var.put('nm2', Js([Js('Ángela'), Js('Ángeles'), Js('Abigail'), Js('Abril'), Js('Ada'), Js('Adoración'), Js('Adriana'), Js('Agustina'), Js('Aitana'), Js('Alana'), Js('Alba'), Js('Albina'), Js('Alejandra'), Js('Alessandra'), Js('Alexa'), Js('Alexandría'), Js('Alexandra'), Js('Alexia'), Js('Alexis'), Js('Alicia'), Js('Alina'), Js('Allison'), Js('Alma'), Js('Amanda'), Js('Amaya'), Js('Amelia'), Js('Ana'), Js('Ana María'), Js('Ana Paula'), Js('Ana Sofía'), Js('Ana Sofia'), Js('Andrea'), Js('Angélica'), Js('Angela'), Js('Angelina'), Js('Antonella'), Js('Antonia'), Js('Araceli'), Js('Ariadna'), Js('Ariana'), Js('Ashley'), Js('Asia'), Js('Asunción'), Js('Aurora'), Js('Bárbara'), Js('Bella'), Js('Bianca'), Js('Brenda'), Js('Briana'), Js('Brisa'), Js('Camila'), Js('Candela'), Js('Carina'), Js('Carla'), Js('Carmen'), Js('Carolina'), Js('Catalina'), Js('Catarina'), Js('Cecilia'), Js('Celeste'), Js('Clara'), Js('Claudia'), Js('Concepción'), Js('Constanza'), Js('Consuela'), Js('Covadonga'), Js('Cristina'), Js('Débora'), Js('Daniela'), Js('Daniella'), Js('Delfina'), Js('Diana'), Js('Doria'), Js('Dulce'), Js('Eduarda'), Js('Elena'), Js('Eliana'), Js('Elisa'), Js('Elisabet'), Js('Elisenda'), Js('Elizabeth'), Js('Elsa'), Js('Emanuella'), Js('Emilia'), Js('Emily'), Js('Emma'), Js('Encarnación'), Js('Engracia'), Js('Esmeralda'), Js('Esperanza'), Js('Estela'), Js('Estrella'), Js('Eva'), Js('Evangelina'), Js('Fátima'), Js('Fabiana'), Js('Fatima'), Js('Felipa'), Js('Fernanda'), Js('Florencia'), Js('Frida'), Js('Génesis'), Js('Gabriela'), Js('Giuliana'), Js('Gloria'), Js('Graciela'), Js('Guadalupe'), Js('Hermosa'), Js('Ines'), Js('Inmaculada'), Js('Irene'), Js('Iris'), Js('Isabel'), Js('Isabela'), Js('Isabella'), Js('Isaias'), Js('Isidora'), Js('Ivanna'), Js('Jauna'), Js('Jazmín'), Js('Jimena'), Js('Josefa'), Js('Josefina'), Js('Juana'), Js('Juanita'), Js('Julia'), Js('Juliana'), Js('Julieta'), Js('Lía'), Js('Laura'), Js('Laura Sofía'), Js('Leila'), Js('Lila'), Js('Lilian'), Js('Liliana'), Js('Linda'), Js('Lola'), Js('Luana'), Js('Lucía'), Js('Lucia'), Js('Luciana'), Js('Luisa'), Js('Luna'), Js('Mía'), Js('Mónica'), Js('Magdalena'), Js('Maite'), Js('Malena'), Js('Manuela'), Js('María'), Js('María Alejandra'), Js('María Camila'), Js('María Fernanda'), Js('María José'), Js('María Paula'), Js('Marcela'), Js('Margarita'), Js('Maria'), Js('Maria José'), Js('Mariana'), Js('Mariangel'), Js('Marina'), Js('Marisa'), Js('Marisol'), Js('Marta'), Js('Martina'), Js('Maya'), Js('Melanie'), Js('Melina'), Js('Melissa'), Js('Mercedes'), Js('Mia'), Js('Micaela'), Js('Michelle'), Js('Miranda'), Js('Miriam'), Js('Monserrat'), Js('Montserrat'), Js('Morena'), Js('Naomí'), Js('Natalia'), Js('Natalie'), Js('Nazarena'), Js('Nazaret'), Js('Nicole'), Js('Nina'), Js('Noé'), Js('Nora'), Js('Octavia'), Js('Olivia'), Js('Paloma'), Js('Paola'), Js('Pastora'), Js('Patricia'), Js('Paula'), Js('Paulin'), Js('Paulina'), Js('Paz'), Js('Penélope'), Js('Perla'), Js('Pilar'), Js('Priscila'), Js('Rafaela'), Js('Raquel'), Js('Rebeca'), Js('Regina'), Js('Renata'), Js('Rene'), Js('Romina'), Js('Rosa'), Js('Rosario'), Js('Rubi'), Js('Sabrina'), Js('Salomé'), Js('Samantha'), Js('Sandra'), Js('Sara'), Js('Sara Sofía'), Js('Selena'), Js('Serena'), Js('Silvana'), Js('Sofía'), Js('Sofia'), Js('Soledad'), Js('Sophie'), Js('Stephanie'), Js('Susana'), Js('Talía'), Js('Tatiana'), Js('Teresa'), Js('Tia'), Js('Valentina'), Js('Valeria'), Js('Valerie'), Js('Valery'), Js('Vanessa'), Js('Verónica'), Js('Veronica'), Js('Victoria'), Js('Violeta'), Js('Virginia'), Js('Vivian'), Js('Viviana'), Js('Ximena'), Js('Ximena/Jimena'), Js('Yesenia'), Js('Yolanda'), Js('Yvonne'), Js('Zarina'), Js('Zoe')]))
var.put('nm3', Js([Js('Águila'), Js('Abasto'), Js('Abellán'), Js('Agramonte'), Js('Aguayo'), Js('Aguinaldo'), Js('Alarcón'), Js('Alcabú'), Js('Alcocer'), Js('Alemán'), Js('Alguacil'), Js('Alvarado'), Js('Amengual'), Js('Andino'), Js('Andrade'), Js('Aparicio'), Js('Arboleda'), Js('Arias'), Js('Arnal'), Js('Arrabal'), Js('Atenas'), Js('Barrios'), Js('Barrueco'), Js('Beldad'), Js('Berganza'), Js('Berrocal'), Js('Bienvenida'), Js('Botín'), Js('Céspedes'), Js('Cabal'), Js('Cadaval'), Js('Cambeiro'), Js('Campos'), Js('Capmany'), Js('Carballal'), Js('Carballar'), Js('Carballo'), Js('Carita'), Js('Carvallo'), Js('Casaus'), Js('Cazalla'), Js('Chicote'), Js('Cicerón'), Js('Collazo'), Js('Coronil'), Js('Correa'), Js('Cortés'), Js('Costa'), Js('Cotilla'), Js('Covarrubias'), Js('Curbelo'), Js('Dávalos'), Js('Dengra'), Js('Elvira'), Js('Encarnación'), Js('Escribano'), Js('Espiga'), Js('Espina'), Js('Espinar'), Js('Feijoo'), Js('Fernán'), Js('Fernandino'), Js('Ferrant'), Js('Figueroa'), Js('Fonseca'), Js('Fontirroig'), Js('Fraga'), Js('Franco'), Js('Freixa'), Js('Gálvez'), Js('Galán'), Js('Gallo'), Js('Gaona'), Js('Gaos'), Js('García'), Js('Garrido'), Js('Gayoso'), Js('Gilabert'), Js('Gisbert'), Js('González'), Js('Graciani'), Js('Guillén'), Js('Gutiérrez'), Js('Hurtado'), Js('Illescas'), Js('Indiano'), Js('Japón'), Js('Juderías'), Js('López'), Js('Lacasa'), Js('Laguna'), Js('Lain'), Js('Leguizamo'), Js('Leoz'), Js('Llacer'), Js('Luque'), Js('Madrid'), Js('Magrina'), Js('Mancebo'), Js('Manzanares'), Js('Manzanedo'), Js('Mariano'), Js('Maroto'), Js('Martí'), Js('Martínez'), Js('Mastache'), Js('Mina'), Js('Miralles'), Js('Molina'), Js('Montenegro'), Js('Montes'), Js('Montreal'), Js('Morillo'), Js('Morterero'), Js('Moruga'), Js('Moya'), Js('Muñoz'), Js('Murillo'), Js('Navarro'), Js('Noboa'), Js('Nores'), Js('Obregón'), Js('Ocampo'), Js('Ordóñez'), Js('Palacio'), Js('Palau'), Js('París'), Js('Pardo'), Js('Pareja'), Js('Piñón'), Js('Pinto'), Js('Pliego'), Js('Pomar'), Js('Pousa'), Js('Pozo'), Js('Prats'), Js('Puig'), Js('Quesada'), Js('Rasgado'), Js('Reyes'), Js('Rodríguez'), Js('Romero'), Js('Ros'), Js('Rouco'), Js('Rubio'), Js('Ruiz'), Js('Sáenz'), Js('Sáez'), Js('Sánchez'), Js('Saavedra'), Js('Saelices'), Js('Sainz'), Js('San Martín'), Js('Sancho'), Js('Santángel'), Js('Sanz'), Js('Sarmiento'), Js('Secada'), Js('Seco'), Js('Semprún'), Js('Tafalla'), Js('Tamayo'), Js('Tasis'), Js('Tassis'), Js('Tejedor'), Js('Tenorio'), Js('Ureña'), Js('Valerio'), Js('Varela'), Js('Velázquez'), Js('Venegas'), Js('Vera'), Js('Villa'), Js('Villacrés'), Js('Xirau'), Js('Yepes'), Js('Zoido'), Js('Zorita'), Js('de la Cavallería'), Js('de la Cruz'), Js('del Pozo')]))
pass
pass


# Add lib to the module scope
hispanicNames = var.to_python()
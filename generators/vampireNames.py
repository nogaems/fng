__all__ = ['vampireNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Quelii'), Js('Zintius'), Js('Fertuitus'), Js('Dorlus'), Js('Versum'), Js('Zegrath'), Js('Sebastian'), Js('Christoph'), Js('Kristoph'), Js('Thaddeus'), Js('Abel'), Js('Abraham'), Js('Acheron'), Js('Adam'), Js('Adrian'), Js('Alaric'), Js('Alec'), Js('Aleister'), Js('Aleron'), Js('Alexander'), Js('Alfred'), Js('Aliester'), Js('Angel'), Js('Angelus'), Js('Anton'), Js('Arad'), Js('Aramastus'), Js('Archibald'), Js('Armand'), Js('Arnold'), Js('Arthur'), Js('Asa'), Js('Ascelin'), Js('Asema'), Js('Asmodeus'), Js('Astaroth'), Js('Astrophel'), Js('Athanasius'), Js('Auberon'), Js('Aubrey'), Js('Aurel'), Js('Azerrad'), Js('Azriel'), Js('Balthazar'), Js('Barnabas'), Js('Bartholomew'), Js('Benedict'), Js('Benjamin'), Js('Bertram'), Js('Bjorn'), Js('Blayze'), Js('Boris'), Js('Brander'), Js('Brandyn'), Js('Brendan'), Js('Bryce'), Js('Byron'), Js('Cadell'), Js('Cadogan'), Js('Caedmon'), Js('Cain'), Js('Caleb'), Js('Cassius'), Js('Cazimir'), Js('Christian'), Js('Church'), Js('Ciaran'), Js('Ciro'), Js('Clarence'), Js('Cleon'), Js('Cole'), Js('Colin'), Js('Constantine'), Js('Corbett'), Js('Corbin'), Js('Creighton'), Js('Cynfael'), Js('Cyprian'), Js('Cyran'), Js("D'Arcy"), Js('Daire'), Js('Damascus'), Js('Damian'), Js('Damien'), Js('Damon'), Js('Danag'), Js('Daniel'), Js('Dante'), Js('Darick'), Js('Darius'), Js('Darren'), Js('Darrien'), Js('Davon'), Js('Davorin'), Js('Demetrius'), Js('Demidicus'), Js('Demitri'), Js('Desmond'), Js('Deverell'), Js('Devin'), Js('Dimitri'), Js('Dommik'), Js('Donovan'), Js('Dorian'), Js('Doru'), Js('Dragon'), Js('Dragos'), Js('Drake'), Js('Draven'), Js('Dregan'), Js('Dreven'), Js('Duncan'), Js('Duradel'), Js('Echo'), Js('Edmund'), Js('Edward'), Js('Edwin'), Js('Eldon'), Js('Elijah'), Js('Elwin'), Js('Emery'), Js('Emil'), Js('Enoch'), Js('Eoghan'), Js('Eoin'), Js('Erasmus'), Js('Etienne'), Js('Everild'), Js('Ezekiel'), Js('Ezra'), Js('Fabian'), Js('Fane'), Js('Florin'), Js('Francis'), Js('Frank'), Js('Frederick'), Js('Frey'), Js('Gabe'), Js('Gabriel'), Js('Gadiel'), Js('Gair'), Js('Gale'), Js('Gareth'), Js('Garrett'), Js('Garroway'), Js('Garth'), Js('Gattas'), Js('Gawain'), Js('Gdalicanu'), Js('Gethin'), Js('Ghislaine'), Js('Gilbert'), Js('Godfrey'), Js('Gossom'), Js('Gregory'), Js('Griffin'), Js('Grimbald'), Js('Griswold'), Js('Hacan'), Js('Hale'), Js('Hannibal'), Js('Harland'), Js('Harold'), Js('Heathcliffe'), Js('Hendrik'), Js('Henry'), Js('Heskel'), Js('Holstein'), Js('Horace'), Js('Horatio'), Js('Hunter'), Js('Iancu'), Js('Ichabod'), Js('Idris'), Js('Ingram'), Js('Isaac'), Js('Isaiah'), Js('Ishmael'), Js('Jacob'), Js('Jael'), Js('Jagger'), Js('Jairus'), Js('James'), Js('Jarlath'), Js('Jarlen'), Js('Jasper'), Js('Jedediah'), Js('Jeffrey'), Js('Jeremy'), Js('Jett'), Js('Jonas'), Js('Jonathan'), Js('Jorin'), Js('Joseph'), Js('Joshua'), Js('Julian'), Js('Julien'), Js('Julius'), Js('Justin'), Js('Kalon'), Js('Kane'), Js('Kapral'), Js('Karpov'), Js('Kayne'), Js('Kazimir'), Js('Keenan'), Js('Keir'), Js('Keiran'), Js('Kellam'), Js('Kern'), Js('Khalid'), Js('Killian'), Js('Kirnon'), Js('Klyn'), Js('Kozani'), Js('Kragen'), Js('Kristopher'), Js('Lafayette'), Js('Lance'), Js('Lancelot'), Js('Lauden'), Js('Laurent'), Js('Lawrence'), Js('Lazarus'), Js('Leander'), Js('Leandro'), Js('Lennix'), Js('Leon'), Js('Leopold'), Js('Lestat'), Js('Liam'), Js('Lionel'), Js('London'), Js('Lothaire'), Js('Louis'), Js('Lucas'), Js('Lucian'), Js('Lucien'), Js('Luther'), Js('Lycidas'), Js('Lysander'), Js('Mabon'), Js('Maggard'), Js('Maggart'), Js('Magna'), Js('Magnus'), Js('Malachi'), Js('Malik'), Js('Marcel'), Js('Marcellus'), Js('Marcus'), Js('Marius'), Js('Martel'), Js('Mathias'), Js('Maxius'), Js('Maxwell'), Js('Melchior'), Js('Merle'), Js('Merlin'), Js('Moldark'), Js('Mordecai'), Js('Mordred'), Js('Morgan'), Js('Mortas'), Js('Mullo'), Js('Nathan'), Js('Nathaniel'), Js('Neculai'), Js('Nehemiah'), Js('Nelo'), Js('Niall'), Js('Nicholas'), Js('Nicodemus'), Js('Nicolai'), Js('Nicu'), Js('Nikolas'), Js('Niles'), Js('Nodin'), Js('Norrix'), Js('Nostro'), Js('Obediah'), Js('Oberon'), Js('Obsidian'), Js('Octavian'), Js('Odolff'), Js('Oliver'), Js('Orien'), Js('Orion'), Js('Orsova'), Js('Owen'), Js('Ozul'), Js('Paine'), Js('Perseus'), Js('Peter'), Js('Phaeron'), Js('Phelan'), Js('Phoenix'), Js('Qadir'), Js('Quillan'), Js('Quillon'), Js('Quinn'), Js('Radomir'), Js('Radu'), Js('Randal'), Js('Ransley'), Js('Raoul'), Js('Raphael'), Js('Rapheal'), Js('Raymond'), Js('Remus'), Js('Renwick'), Js('Reyes'), Js('Rhain'), Js('Rhazien'), Js('Richard'), Js('Riordan'), Js('Riskel'), Js('Roderick'), Js('Roman'), Js('Rufus'), Js('Rune'), Js('Ruse'), Js('Saber'), Js('Sabien'), Js('Salem'), Js('Samuel'), Js('Sandor'), Js('Santiago'), Js('Saxon'), Js('Seain'), Js('Sebastian'), Js('Seskel'), Js('Seth'), Js('Severn'), Js('Seymour'), Js('Silas'), Js('Silvan'), Js('Simon'), Js('Sin'), Js('Sirius'), Js('Sliske'), Js('Solomon'), Js('Soran'), Js('Spencer'), Js('Spike'), Js('Star'), Js('Stelian'), Js('Sterling'), Js('Strix'), Js('Sullivan'), Js('Sun'), Js('Tallon'), Js('Talon'), Js('Tama'), Js('Taos'), Js('Tearle'), Js('Theron'), Js('Thomas'), Js('Thorin'), Js('Thorne'), Js('Tobias'), Js('Treznor'), Js('Ulfred'), Js('Ulysses'), Js('Urien'), Js('Valentine'), Js('Valerian'), Js('Vance'), Js('Vasile'), Js('Vernon'), Js('Victor'), Js('Viktor'), Js('Vincent'), Js('Virgil'), Js('Viscardi'), Js('Vlad'), Js('Vladimir'), Js('Vorigan'), Js('Waldron'), Js('Walter'), Js('Warren'), Js('Wilfred'), Js('William'), Js('Wolf'), Js('Wolfram'), Js('Xanthus'), Js('Xavier'), Js('Xenos'), Js('Ywain'), Js('Zachaeus'), Js('Zachariah'), Js('Zadicus'), Js('Zadimus'), Js('Zaff'), Js('Zane'), Js('Zaros'), Js('Zeidan'), Js('Zeke'), Js('Zoltan')]))
var.put('nm2', Js([Js('Deyja'), Js('Abby'), Js('Abigale'), Js('Ada'), Js('Adriana'), Js('Adrienne'), Js('Aerin'), Js('Aisling'), Js('Akasha'), Js('Aleron'), Js('Alessandra'), Js('Alexandra'), Js('Alexandria'), Js('Alice'), Js('Alvira'), Js('Amalia'), Js('Amaris'), Js('Amber'), Js('Amelia'), Js('Amelie'), Js('Ana'), Js('Anastasia'), Js('Angelica'), Js('Angelika'), Js('Angelina'), Js('Angelique'), Js('Antoinette'), Js('Arabella'), Js('Arachne'), Js('Arora'), Js('Artemia'), Js('Asphodel'), Js('Athena'), Js('Aubrey'), Js('Aurelia'), Js('Aurora'), Js('Austra'), Js('Autumn'), Js('Babylon'), Js('Badriyah'), Js('Baptista'), Js('Beatrice'), Js('Beatrix'), Js('Becca'), Js('Bella'), Js('Belladonna'), Js('Bellatrix'), Js('Bernia'), Js('Bianca'), Js('Bijou'), Js('Branwen'), Js('Briallen'), Js('Brienne'), Js('Brigid'), Js('Buffy'), Js('Caera'), Js('Calamity'), Js('Calantha'), Js('Calista'), Js('Callidora'), Js('Calliope'), Js('Carmilla'), Js('Caroline'), Js('Cassandra'), Js('Cassara'), Js('Ceiridwen'), Js('Celeste'), Js('Celosia'), Js('Chandra'), Js('Chantrea'), Js('Charity'), Js('Charlotte'), Js('Chaseleigh'), Js('Chastity'), Js('Circe'), Js('Claire'), Js('Clara'), Js('Claudia'), Js('Clementine'), Js('Constantia'), Js('Cordelia'), Js('Crimson'), Js('Cristina'), Js('Daniela'), Js('Danika'), Js('Daria'), Js('Darian'), Js('Darla'), Js('Dawn'), Js('December'), Js('Deidre'), Js('Delia'), Js('Deliliah'), Js('Demelza'), Js('Demetria'), Js('Denisa'), Js('Desdemona'), Js('Destiny'), Js('Dominique'), Js('Dru'), Js('Druilla'), Js('Drusilla'), Js('Ebony'), Js('Echo'), Js('Edana'), Js('Eden'), Js('Eirisse'), Js('Eirlys'), Js('Eldia'), Js('Eleanor'), Js('Electra'), Js('Elena'), Js('Elenor'), Js('Elisabeta'), Js('Elissa'), Js('Elizabeth'), Js('Ellanora'), Js('Ellanore'), Js('Ellena'), Js('Ellie'), Js('Elvira'), Js('Emberlynn'), Js('Emerande'), Js('Emilia'), Js('Emily'), Js('Emma'), Js('Emmanuelle'), Js('Emmeranne'), Js('Ennata'), Js('Eranthe'), Js('Erylis'), Js('Esmeralda'), Js('Esmeralde'), Js('Esther'), Js('Estrella'), Js('Ethelinda'), Js('Eunice'), Js('Eva'), Js('Evangeline'), Js('Eventide'), Js('Fae'), Js('Faine'), Js('Faith'), Js('Faline'), Js('Fanchon'), Js('Fawn'), Js('Felicia'), Js('Fern'), Js('Feronia'), Js('Fleurdelice'), Js('Florence'), Js('Fortune'), Js('Gabriela'), Js('Gabrielle'), Js('Galexialyn'), Js('Garnette'), Js('Genevieve'), Js('Gertrude'), Js('Grace'), Js('Gretchen'), Js('Griselda'), Js('Guinevere'), Js('Gwendoline'), Js('Gwendydd'), Js('Haera'), Js('Hagar'), Js('Hazelmere'), Js('Hecate'), Js('Hegna'), Js('Helana'), Js('Helen'), Js('Helena'), Js('Helga'), Js('Henrietta'), Js('Herma'), Js('Hesperia'), Js('Hestia'), Js('Hilda'), Js('Hildegarde'), Js('Ianira'), Js('Ianthe'), Js('Ileana'), Js('Illythia'), Js('Indigo'), Js('Iolana'), Js('Iolanthe'), Js('Iona'), Js('Ione'), Js('Irene'), Js('Irina'), Js('Isabella'), Js('Isadora'), Js('Isis'), Js('Isolabella'), Js('Ivory'), Js('Ivy'), Js('Izora'), Js('Jacqueline'), Js('Jade'), Js('Jane'), Js('Janet'), Js('Jett'), Js('Jevera'), Js('Jillian'), Js('Jocasta'), Js('Joliette'), Js('Joscelyn'), Js('Josephine'), Js('Julia'), Js('Julianna'), Js('Julienne'), Js('Juliet'), Js('Kafara'), Js('Kairos'), Js('Kala'), Js('Kali'), Js('Kalonice'), Js('Kamra'), Js('Karlene'), Js('Kat'), Js('Katherine'), Js('Kathryx'), Js('Katrina'), Js('Kavita'), Js('Kenia'), Js('Ketura'), Js('Khalida'), Js('Kiara'), Js('Kismet'), Js('Kolfinna'), Js('Krista'), Js('Kristian'), Js('Kynthia'), Js('Lahmia'), Js('Lamia'), Js('Lamya'), Js('Lavinia'), Js('Layla'), Js('Leandra'), Js('Lechsinska'), Js('Lenora'), Js('Lenore'), Js('Leontine'), Js('Leora'), Js('Lethia'), Js('Levana'), Js('Lien'), Js('Lilah'), Js('Liliana'), Js('Lilith'), Js('Lisa'), Js('Lisha'), Js('Loredana'), Js('Lorelei'), Js('Loren'), Js('Lorraine'), Js('Lucia'), Js('Lucilla'), Js('Lucinda'), Js('Lucretia'), Js('Lucy'), Js('Lullaby'), Js('Luna'), Js('Lupe'), Js('Lycoris'), Js('Lyllith'), Js('Lynede'), Js('Lynexia'), Js('Lyra'), Js('Lysa'), Js('Madeline'), Js('Madison'), Js('Maeve'), Js('Magda'), Js('Magdalena'), Js('Magdelena'), Js('Magena'), Js('Mallory'), Js('Margaret'), Js('Maria'), Js('Mariana'), Js('Marianne'), Js('Marta'), Js('Matilda'), Js('Mehira'), Js('Melantha'), Js('Mercedes'), Js('Mercy'), Js('Meredith'), Js('Merle'), Js('Mildred'), Js('Minerva'), Js('Mira'), Js('Misty'), Js('Monique'), Js('Mora'), Js('Morgan'), Js('Morrisey'), Js('Morticia'), Js('Morwenna'), Js('Musette'), Js('Myth'), Js('Myvanwy'), Js('Naida'), Js('Narcisa'), Js('Natalia'), Js('Nebula'), Js('Neferata'), Js('Nessa'), Js('Nevada'), Js('Nezera'), Js('Niamh'), Js('Nichole'), Js('Nicole'), Js('Nicolette'), Js('Nirvana'), Js('Nisha'), Js('Nissa'), Js('Nokomis'), Js('Nora'), Js('Nyx'), Js('Oana'), Js('Odile'), Js('Opal'), Js('Ophelia'), Js('Ordelia'), Js('Orenda'), Js('Osanna'), Js('Pandora'), Js('Parthena'), Js('Permelia'), Js('Persephone'), Js('Petra'), Js('Phaelyn'), Js('Phaidra'), Js('Philomena'), Js('Phoenix'), Js('Pixie'), Js('Poison'), Js('Prudence'), Js('Psyche'), Js('Purity'), Js('Pythea'), Js('Qadira'), Js('Quintella'), Js('Radella'), Js('Raelinn'), Js('Ramona'), Js('Raphaelle'), Js('Raven'), Js('Ravette'), Js('Rebecca'), Js('Renee'), Js('Renita'), Js('Rhapsody'), Js('Rhiannon'), Js('Rhodanthe'), Js('Riah'), Js('River'), Js('Rosalie'), Js('Rosalyn'), Js('Rowena'), Js('Ruby'), Js('Sabina'), Js('Sabrione'), Js('Samantha'), Js('Sapphira'), Js('Sapphire'), Js('Sarah'), Js('SarahAnn'), Js('Scarlett'), Js('Seiran'), Js('Selena'), Js('Selene'), Js('Selina'), Js('Senna'), Js('Seraphine'), Js('Seren'), Js('Sierra'), Js('Silvana'), Js('Silver'), Js('Silvia'), Js('Simone'), Js('Sky'), Js('Skylar'), Js('Sorcha'), Js('Sorina'), Js('Star'), Js('Stefania'), Js('Stella'), Js('Sylvia'), Js('Tabitha'), Js('Tanith'), Js('Tatiana'), Js('Tempesta'), Js('Tereza'), Js('Tessa'), Js('Thalia'), Js('Thelma'), Js('Thessalia'), Js('Thora'), Js('Thordis'), Js('Tiana'), Js('Tierney'), Js('Timandra'), Js('Tizane'), Js('Topaz'), Js('Tourmaline'), Js('Trista'), Js('Turaya'), Js('Ulva'), Js('Urania'), Js('Ursula'), Js('Ursulette'), Js('Ursuline'), Js('Valaine'), Js('Valenthia'), Js('Valentina'), Js('Valeria'), Js('Valerie'), Js('Vanessa'), Js('Vanita'), Js('Vanity'), Js('Vasilisa'), Js('Velika'), Js('Velorina'), Js('Velvet'), Js('Venette'), Js('Venus'), Js('Vesper'), Js('Vespera'), Js('Victoire'), Js('Victoria'), Js('Viessa'), Js('Viktoria'), Js('Violet'), Js('Violeta'), Js('Wanette'), Js('Wilhelmina'), Js('Willow'), Js('Wilma'), Js('Winnifred'), Js('Wren'), Js('Xanthe'), Js('Xaverie'), Js('Xena'), Js('Xylia'), Js('Yolanthe'), Js('Ysabelle'), Js('Yvonne'), Js('Zabrina'), Js('Zada'), Js('Zafrina'), Js('Zakira'), Js('Zaleria'), Js('Zara'), Js('Zella'), Js('Zephirah'), Js('Zetta'), Js('Zola')]))
pass
pass


# Add lib to the module scope
vampireNames = var.to_python()
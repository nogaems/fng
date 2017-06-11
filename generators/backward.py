__all__ = ['backward']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
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
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abbie - Eibba'), Js('Abigail - Liagiba'), Js('Abram - Marba'), Js('Acceber - Rebecca'), Js('Acinom - Monica'), Js('Adair - Riada'), Js('Adaj - Jada'), Js('Adam - Mada'), Js('Adela - Aleda'), Js('Adelaide - Edialeda'), Js('Adia - Aida'), Js('Adiel - Leida'), Js('Adnerb - Brenda'), Js('Adrea - Aerda'), Js('Adrian - Nairda'), Js('Agnes - Senga'), Js('Ahsila - Alisha'), Js('Aicats - Stacia'), Js('Aida - Adia'), Js('Aidan - Nadia'), Js('Aidualc - Claudia'), Js('Ailuj - Julia'), Js('Aiphos - Sophia'), Js('Airam - Maria'), Js('Airotciv - Victoria'), Js('Aivilo - Olivia'), Js('Ajani - Inaja'), Js('Alan - Nala'), Js('Alani - Inala'), Js('Alec - Cela'), Js('Alex - Xela'), Js('Alexi - Ixela'), Js('Ali - Ila'), Js('Allebasi - Isabella'), Js('Allen - Nella'), Js('Ameer - Reema'), Js('Amin - Nima'), Js('Amir - Rima'), Js('Amirah - Harima'), Js('Amla - Alma'), Js('Amme - Emma'), Js('Anaili - Iliana'), Js('Anali - Ilana'), Js('Angie - Eigna'), Js('Ani - Ina'), Js('Annika - Akinna'), Js('Arabrab - Barbara'), Js('Arden - Nedra'), Js('Ardnas - Sandra'), Js('Ares - Sera'), Js('Ari - Ira'), Js('Ariadne - Endaria'), Js('Aric - Cira'), Js('Arica - Acira'), Js('Ariel - Leira'), Js('Arik - Kira'), Js('Ariyah - Hayira'), Js('Aron - Nora'), Js('Arrec - Cerra'), Js('Ashley - Yelhsa'), Js('Ashley - Yelsha'), Js('Assenav - Vanessa'), Js('Assilem - Melissa'), Js('Aven - Neva'), Js('Avi - Iva'), Js('Axel - Lexa'), Js('Ayah - Haya'), Js('Aydan - Nadya'), Js('Aylie - Eliya'), Js('Azure - Ezura'), Js('Billy - Yllib'), Js('Boris - Sirob'), Js('Brin - Nirb'), Js('Byron - Noryb'), Js('Caleb - Belac'), Js('Callie - Eillac'), Js('Cameron - Noremac'), Js('Carlos - Solrac'), Js('Carol - Lorac'), Js('Carrie - Eirrac'), Js('Carter - Retrac'), Js('Casey - Yesac'), Js('Cecile - Elicec'), Js('Chris - Sirch'), Js('Cierra - Arreic'), Js('Cindy - Ydnic'), Js('Cohen - Nehoc'), Js('Cole - Eloc'), Js('Coleman - Nameloc'), Js('Colin - Niloc'), Js('Colleen - Neelloc'), Js('Cora - Aroc'), Js('Cory - Yroc'), Js('Crie - Eric'), Js('Damon - Nomad'), Js('Dan - Nad'), Js('Dana - Anad'), Js('Daniel - Leinad'), Js('Danielle - Elleinad'), Js('Darla - Alrad'), Js('Darren - Nerrad'), Js('Dave - Evad'), Js('David - Divad'), Js('Dean - Naed'), Js('Delia - Ailed'), Js('Deraj - Jared'), Js('Derek - Kered'), Js('Derfla - Alfred'), Js('Devin - Nived'), Js('Diana - Anaid'), Js('Divad - David'), Js('Dlanor - Ronald'), Js('Dnomyar - Raymond'), Js('Dolores - Serolod'), Js('Donna - Annod'), Js('Dora - Arod'), Js('Doyle - Elyod'), Js('Droffilc - Clifford'), Js('Duncan - Nacnud'), Js('Dustin - Nitsud'), Js('Dylan - Nalyd'), Js('Ecnerwal - Lawrence'), Js('Ecynaj - Janyce'), Js('Edward - Drawde'), Js('Eibbed - Debbie'), Js('Eilatan - Natalie'), Js('Eileen - Neelie'), Js('Eilsel - Leslie'), Js('Eiram - Marie'), Js('Eirloav - Valorie'), Js('Eirrehs - Sherrie'), Js('Eissej - Jessie'), Js('Elaine - Eniale'), Js('Eleanor - Ronaele'), Js('Eliza - Azile'), Js('Ella - Alle'), Js('Ellen - Nelle'), Js('Ellis - Sille'), Js('Elohc - Chole'), Js('Elohcin - Nichole'), Js('Emily - Ylime'), Js('Emma - Amme'), Js('Emmalyn - Nylamme'), Js('Emmet - Temme'), Js('Enaj - Jane'), Js('Enegue - Eugene'), Js('Ener - Rene'), Js('Eniledam - Madeline'), Js('Enilorac - Caroline'), Js('Enilrae - Earline'), Js('Ennaoj - Joanne'), Js('Ennazus - Suzanne'), Js('Eric - Cire'), Js('Eric-Cire'), Js('Erica - Acire'), Js('Ettolrahc - Charlotte'), Js('Eva - Ave'), Js('Evangeline - Enilegnave'), Js('Evelyn - Nyleve'), Js('Evilo - Olive'), Js('Eyak - Kaye'), Js('Fallon - Nollaf'), Js('Fanny - Ynnaf'), Js('Farrah - Harraf'), Js('Felix - Xilef'), Js('Flor - Rolf'), Js('Flora - Arolf'), Js('Floyd - Dyolf'), Js('Freida - Adierf'), Js('Gabriella - Alleirbag'), Js('Gary - Yrag'), Js('Gem - Meg'), Js('Giles - Selig'), Js('Gillian - Naillig'), Js('Greg - Gerg'), Js('Hacim - Micah'), Js('Haela - Aleah'), Js('Haidan - Nadiah'), Js('Haidran - Nadriah'), Js('Hairam - Mariah'), Js('Haley - Yelah'), Js('Halie - Eilah'), Js('Haon - Noah'), Js('Haras - Sarah'), Js('Harobed - Deborah'), Js('Harold - Dlorah'), Js('Haron - Norah'), Js('Harry - Yrrah'), Js('Harvey - Yevrah'), Js('Hayes - Seyah'), Js('Hazel - Lezah'), Js('Henry - Yrneh'), Js('Hpesoj - Joseph'), Js('Htebazile - Elizabeth'), Js('Htennek - Kenneth'), Js('Hunter - Retnuh'), Js('Ida - Adi'), Js('Iman - Nami'), Js('Imogene - Enegomi'), Js('Iort - Tori'), Js('Ira - Ari'), Js('Iris - Siri'), Js('Irving - Gnivri'), Js('Isaac - Caasi'), Js('Isabel - Lebasi'), Js('Ised - Desi'), Js('Issac - Cassi'), Js('Ivan - Navi'), Js('Jamal - Lamaj'), Js('Jan - Naj'), Js('Jared - Deraj'), Js('Jason - Nosaj'), Js('Jesse - Essej'), Js('Jordan - Nadroj'), Js('Kaasi - Isaak'), Js('Kara - Arak'), Js('Karen - Narek'), Js('Kassie - Eissak'), Js('Kate - Etak'), Js('Katerina - Aniretak'), Js('Katie - Eitak'), Js('Kavon - Novak'), Js('Kayla - Alyak'), Js('Kcirtap - Patrick'), Js('Kcuhc - Chuck'), Js('Kelly - Yellek'), Js('Kendall - Lladnek'), Js('Kevin - Nivek'), Js('Kim - Mik'), Js('Kram - Mark'), Js('Kris - Sirk'), Js('Kyle - Elyk'), Js('Lamaj - Jamal'), Js('Larc - Carl'), Js('Larry - Yrral'), Js('Laup - Paul'), Js('Laura - Arual'), Js('Lauren - Nerual'), Js('Layla - Alyal'), Js('Leahcim - Michael'), Js('Lehcar - Rachel'), Js('Leinad - Daniel'), Js('Leira - Ariel'), Js('Leonard - Dranoel'), Js('Lestor - Rotsel'), Js('Lexa - Axel'), Js('Lezah - Hazel'), Js('Lila - Alil'), Js('Lina - Anil'), Js('Linda - Adnil'), Js('Lisa - Asil'), Js('Llib - Bill'), Js('Lorna - Anrol'), Js('Lowell - Llewol'), Js('Luanne - Ennaul'), Js('Lucas - Sacul'), Js('Luke - Ekul'), Js('Lydia - Aidyl'), Js('Mac - Cam'), Js('Madeline-Eniledam'), Js('Mailliw - William'), Js('Mallory - Yrollam'), Js('Mara - Aram'), Js('Margaret - Teragram'), Js('Maria - Airam'), Js('Marion - Noiram'), Js('Marsha - Ahsram'), Js('Martha - Ahtram'), Js('Matthias - Saihttam'), Js('Max - Xam'), Js('Melora - Arolem'), Js('Miah - Haim'), Js('Mika - Akim'), Js('Mikah - Hakim'), Js('Miles - Selim'), Js('Millie - Eillim'), Js('Milly - Yllim'), Js('Milo - Olim'), Js('Miranda - Adnarim'), Js('Misha - Ahsim'), Js('Missy - Yssim'), Js('Moira - Ariom'), Js('Nadia - Aidan'), Js('Naed - Dean'), Js('Nagol - Logan'), Js('Naima - Amian'), Js('Nairb - Brian'), Js('Naj - Jan'), Js('Nala - Alan'), Js('Naleac - Caelan'), Js('Nalla - Allan'), Js('Naomi - Imoan'), Js('Nasoj - Josan'), Js('Nasus - Susan'), Js('Natasha - Ahsatan'), Js('Nate - Etan'), Js('Nathe - Ethan'), Js('Nav - Van'), Js('Naya - Ayan'), Js('Nedac - Caden'), Js('Nedaj - Jaden'), Js('Nedyaj - Jayden'), Js('Nedyarb - Brayden'), Js('Neelia - Aileen'), Js('Nehpets - Stephen'), Js('Nelaj - Jalen'), Js('Nelg - Glen'), Js('Nell - Llen'), Js('Nerys - Syren'), Js('Netsirk - Kristen'), Js('Nevah - Haven'), Js('Neville - Elliven'), Js('Newo - Owen'), Js('Nibot - Tobin'), Js('Nikki - Ikkin'), Js('Nire - Erin'), Js('Nitsuj - Justin'), Js('Noa - Aon'), Js('Noah - Haon'), Js('Noah - Hoan'), Js('Nodlehs - Sheldon'), Js('Nodnarb - Brandon'), Js('Noel - Leon'), Js('Nola - Alon'), Js('Noryb - Byron'), Js('Nosidam - Madison'), Js('Nosidda - Addison'), Js('Nosilla - Allison'), Js('Noskcaj - Jackson'), Js('Nosredna - Anderson'), Js('Nova - Avon'), Js('Nya - Ayn'), Js('Nylava - Avalyn'), Js('Nyleve - Evelyn'), Js('Olivia - Aivilo'), Js('Om - Mo'), Js('Opal - Lapo'), Js('Oprah - Harpo'), Js('Orimar - Ramiro'), Js('Owen - Newo'), Js('Paula - Aluap'), Js('Penny - Ynnep'), Js('Peyton - Notyep'), Js('Phelix - Xilehp'), Js('Piper - Repip'), Js('Ramaj - Jamar'), Js('Ramon - Nomar'), Js('Rauol-Louar'), Js('Reese - Eseer'), Js('Refinnej - Jennifer'), Js('Regue - Euger'), Js('Rehtra - Arther'), Js('Retep - Peter'), Js('Retnuh - Hunter'), Js('Revilo - Oliver'), Js('Rhie - Eihr'), Js('Rita - Atir'), Js('Rob - Bor'), Js('Robert - Trebor'), Js('Roberta - Atrebor'), Js('Robin - Nibor'), Js('Roger - Regor'), Js('Rolyat - Taylor'), Js('Roman - Namor'), Js('Ronald - Dlanor'), Js('Rosa - Asor'), Js('Rosalie - Eilasor'), Js('Rosalyn - Nylasor'), Js('Ruby - Ybur'), Js('Ruhtra - Arthur'), Js('Russell - Llessur'), Js('Ryan - Nayr'), Js('Ryne - Enyr'), Js('Sabrina - Anirbas'), Js('Sadie - Eidas'), Js('Sally - Yllas'), Js('Sarah - Haras'), Js('Sasha - Ahsas'), Js('Sawyer - Reywas'), Js('Sean - Naes'), Js('Selena - Aneles'), Js('Selim - Miles'), Js('Selma - Amles'), Js('Selrahc - Charles'), Js('Semaj - James'), Js('Siana - Anais'), Js('Silas - Salis'), Js('Sillyph - Phyllis'), Js('Sinned - Dennis'), Js('Siri - Iris'), Js('Sito - Otis'), Js('Sivart - Travis'), Js('Socram - Marcos'), Js('Stanley - Yelnats'), Js('Steven - Nevets'), Js('Stuart - Trauts'), Js('Susan - Nasus'), Js('Susie - Eisus'), Js('Sven - Nevs'), Js('Sylvia - Aivlys'), Js('Tamara - Aramat'), Js('Tara - Arat'), Js('Tenaj - Janet'), Js('Terbor - Robert'), Js('Terri - Irret'), Js('Tessa - Asset'), Js('Tiana - Anait'), Js('Tiffany - Ynaffit'), Js('Tilly - Yllit'), Js('Tnilc - Clint'), Js('Tommy - Ymmot'), Js('Tori - Irot'), Js('Tracy - Ycart'), Js('Trauts - Stuart'), Js('Trevor - Rovert'), Js('Troy - Yort'), Js('Tsenre - Ernest'), Js('Ttocs - Scott'), Js('Velma - Amlev'), Js('Veronica - Acinorev'), Js('Virgil - Ligriv'), Js('Vivian - Naiviv'), Js('Wehtam - Mathew'), Js('Werdan - Andrew'), Js('Werdna - Andrew'), Js('Xela - Alex'), Js('Yar - Ray'), Js('Ybbor - Robby'), Js('Ycart - Tracy'), Js('Ydurt - Trudy'), Js('Yenaled - Delaney'), Js('Yenetruoc - Courteney'), Js('Yerffej - Jeffrey'), Js('Yhtorod - Dorothy'), Js('Ylrebmik - Kimberly'), Js('Ynitsed - Destiny'), Js('Ynnej - Jenny'), Js('Yor - Roy'), Js('Yret - Tery'), Js('Yrloav - Valory'), Js('Yrret - Terry'), Js('Zaid - Diaz'), Js('Zeni - Inez'), Js('Zil - Liz'), Js('Zoey - Yeoz')]))
pass
pass


# Add lib to the module scope
backward = var.to_python()
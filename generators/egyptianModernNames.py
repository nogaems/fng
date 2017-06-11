__all__ = ['egyptianModernNames']

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
var.put('nm1', Js([Js('Abasi'), Js('Abdalla'), Js('Abdelrahman'), Js('Achraf'), Js('Adel'), Js('Adham'), Js('Ahmad'), Js('Ahmed'), Js('Alaa'), Js('Ali'), Js('Aly'), Js('Amir'), Js('Amr'), Js('Anwar'), Js('Ari'), Js('Ashraf'), Js('Assem'), Js('Athouman'), Js('Aymn'), Js('Barika'), Js('Bassam'), Js('Bassel'), Js('Bebi'), Js('Bebti'), Js('Bedario'), Js('Boody'), Js('Chaths'), Js('Chatuluka'), Js('Chibale'), Js('Chigaru'), Js('Chisisi'), Js('Darwishi'), Js('David'), Js('Desire'), Js('Dodi'), Js('Dodo'), Js('Dods'), Js('Gahiji'), Js('Garai'), Js('Gyasi'), Js('Haisam'), Js('Haji'), Js('Hamadi'), Js('Hamed'), Js('Hanbal'), Js('Hanif'), Js('Hany'), Js('Hassan'), Js('Hatem'), Js('Haytham'), Js('Hesso'), Js('Hosni'), Js('Hossam'), Js('Husani'), Js('Hussein'), Js('Ishaq'), Js('Islam'), Js('Isma'), Js('Ismael'), Js('Issa'), Js('Kafele'), Js('Kamuzu'), Js('Kaphiri'), Js('Kareem'), Js('Karim'), Js('Kasiya'), Js('Kasto'), Js('Khaled'), Js('Kontar'), Js('Louai'), Js('Madu'), Js('Maged'), Js('Mahmoud'), Js('Male'), Js('Mamdoh'), Js('Mando'), Js('Manu'), Js('Marwan'), Js('Masud'), Js('Mazen'), Js('Medo'), Js('Mero'), Js('Mido'), Js('Mina'), Js('Mody'), Js('Mohab'), Js('Mohammed'), Js('Momo'), Js('Monim'), Js('Moustafa'), Js('Muhanad'), Js('Mustafa'), Js('Nader'), Js('Nafty'), Js('Nassor'), Js('Nino'), Js('Nizsm'), Js('Nour'), Js('Nuru'), Js('Odion'), Js('Omar'), Js('Osahar'), Js('Osaze'), Js('Osman'), Js('Ossama'), Js('Psamtic'), Js('Qeb'), Js('Quasshie'), Js('Radames'), Js('Raffy'), Js('Ragab'), Js('Reda'), Js('Redore'), Js('Romuald'), Js('Sadiki'), Js('Samir'), Js('Seif'), Js('Selim'), Js('Shaaban'), Js('Shakir'), Js('Sharky'), Js('Teremun'), Js('Thabit'), Js('Tsekani'), Js('Ubaid'), Js('Ufa'), Js('Usi'), Js('Wael'), Js('Waleed'), Js('Wessam')]))
var.put('nm2', Js([Js('Aaliyah'), Js('Abby'), Js('Alia'), Js('Aliaa'), Js('Alima'), Js('Amal'), Js('Ameera'), Js('Amina'), Js('Amirah'), Js('Anan'), Js('Andra'), Js('Arwa'), Js('Asmaa'), Js('Aya'), Js('Ayah'), Js('Babes'), Js('Babu'), Js('Baniti'), Js('Bassam'), Js('Bassant'), Js('Bassma'), Js('Boombaa'), Js('Chavi'), Js('Dalia'), Js('Deena'), Js('Dendera'), Js('Dina'), Js('Donya'), Js('Ehsan'), Js('Farida'), Js('Fatma'), Js('Femi'), Js('Galela'), Js('Gameela'), Js('Habiba'), Js('Hafsah'), Js('Hana'), Js('Hanaa'), Js('Haqikah'), Js('Heba'), Js('Houda'), Js('Ife'), Js('Iman'), Js('Isis'), Js('Jehan'), Js('Kaikara'), Js('Kakra'), Js('Kamilah'), Js('Karima'), Js('Kiara'), Js('Lapis'), Js('Mai'), Js('Maibe'), Js('Malak'), Js('Manar'), Js('Maria'), Js('Mariah'), Js('Mariam'), Js('Marwa'), Js('Masika'), Js('Mayar'), Js('Menna'), Js('Meroo'), Js('Mert'), Js('Mesi'), Js('Mi-Soon'), Js('Miria'), Js('Mona'), Js('Monifa'), Js('Monique'), Js('Mosi'), Js('Moushira'), Js('Muminah'), Js('Myrrh'), Js('Nabirye'), Js('Nada'), Js('Nadeen'), Js('Nadia'), Js('Nadine'), Js('Nagwa'), Js('Naima'), Js('Nannosa'), Js('Nehad'), Js('Nerin'), Js('Nero'), Js('Nesma'), Js('Nihad'), Js('Nile'), Js('Noha'), Js('Nona'), Js('Norhan'), Js('Nourane'), Js('Nubia'), Js('Ode'), Js('Olabisis'), Js('Olufemi'), Js('Omorose'), Js('Oseye'), Js('Panya'), Js('Pili'), Js('Quibailah'), Js('Rabiah'), Js('Rana'), Js('Raneem'), Js('Rania'), Js('Rasha'), Js('Razan'), Js('Reem'), Js('Rehema'), Js('Sabah'), Js('Safa'), Js('Sagira'), Js('Sahirah'), Js('Salama'), Js('Sally'), Js('Salma'), Js('Salwa'), Js('Samah'), Js('Samar'), Js('Samia'), Js('Sanie'), Js('Sanura'), Js('Sara'), Js('Sarah'), Js('Selki'), Js('Shadya'), Js('Shafira'), Js('Shahirah'), Js('Shaimaa'), Js('Shani'), Js('Shesho'), Js('Siti'), Js('Sohaila'), Js('Sohair'), Js('Somaya'), Js('Souhila'), Js('Suhaila'), Js('Tabia'), Js('Taheya'), Js('Tale'), Js('Talibah'), Js('Tania'), Js('Tauret'), Js('Theoris'), Js('Umayma'), Js('Urbi'), Js('Walaa'), Js('Walidah'), Js('Weam'), Js('Yasmeen'), Js('Yasmin'), Js('Yasmine'), Js('Zalika')]))
var.put('nm3', Js([Js('Abadi'), Js('Abboud'), Js('Al Sadat'), Js('Almasi'), Js('Amari'), Js('Antar'), Js('Antoun'), Js('Arian'), Js('Asfour'), Js('Asghar'), Js('Asker'), Js('Assaf'), Js('Aswad'), Js('Atiyeh'), Js('Attia'), Js('Awad'), Js('Ba'), Js('Baba'), Js('Bahar'), Js('Basara'), Js('Bata'), Js('Baz'), Js('Bazzi'), Js('Bishara'), Js('Bitar'), Js('Botros'), Js('Boulos'), Js('Boutros'), Js('Cham'), Js('Dagher'), Js('Daher'), Js('Deeb'), Js('El Sadat'), Js('Essa'), Js('Fakhoury'), Js('Gaber'), Js('Ganem'), Js('Ganim'), Js('Gerges'), Js('Ghanem'), Js('Ghannam'), Js('Guirguis'), Js('Hadad'), Js('Haddad'), Js('Haik'), Js('Hajjar'), Js('Hakimi'), Js('Halabi'), Js('Hanania'), Js('Handal'), Js('Harb'), Js('Isa'), Js('Issa'), Js('Kalb'), Js('Kanaan'), Js('Kassab'), Js('Kassis'), Js('Kattan'), Js('Khouri'), Js('Khoury'), Js('Kouri'), Js('Koury'), Js('Maalouf'), Js('Maloof'), Js('Malouf'), Js('Mansour'), Js('Maroun'), Js('Masih'), Js('Mifsud'), Js('Mikhail'), Js('Moghadam'), Js('Morcos'), Js('Mubarak'), Js('Mustafa'), Js('Nader'), Js('Nahas'), Js('Naifeh'), Js('Najjar'), Js('Naser'), Js('Nassar'), Js('Nazari'), Js('Quraishi'), Js('Qureshi'), Js('Rahal'), Js('Sabbag'), Js('Sabbagh'), Js('Safar'), Js('Said'), Js('Salib'), Js('Saliba'), Js('Samaha'), Js('Sarkis'), Js('Sarraf'), Js('Sayegh'), Js('Seif'), Js('Shadid'), Js('Shalhoub'), Js('Shammas'), Js('Shamon'), Js('Shamoon'), Js('Shamoun'), Js('Sleiman'), Js('Srour'), Js('Tahan'), Js('Tannous'), Js('Toma'), Js('Totah'), Js('Touma'), Js('Tuma'), Js('Wasem'), Js('Zogby')]))
pass
pass


# Add lib to the module scope
egyptianModernNames = var.to_python()
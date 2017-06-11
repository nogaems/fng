__all__ = ['hausaNames']

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
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Abashe'), Js('Abdul'), Js('Adamu'), Js('Ahmedu'), Js('Ali'), Js('Alkali'), Js('Aminu'), Js('Amir'), Js('Audu'), Js('Babangida'), Js('Bakano'), Js('Balarabe'), Js('Barmani'), Js('Bashir'), Js('Bature'), Js('Bello'), Js('Bilal'), Js('Bulu'), Js('Danasabe'), Js('Danjuma'), Js('Danladi'), Js('Danlami'), Js('Daren'), Js("Fa'izu"), Js('Faisal'), Js('Faizu'), Js('Faruq'), Js('Finn'), Js("Fu'ad"), Js('Fuad'), Js('Gambo'), Js('Genet'), Js('Guban'), Js('Gure'), Js('Haben'), Js('Habib'), Js('Hadi'), Js('Hafiz'), Js('Hajari'), Js('Hamzah'), Js('Hassan'), Js('Hirsi'), Js('Huso'), Js('Hussain'), Js('Hussein'), Js('Ibeamaka'), Js('Ibrahim'), Js('Idris'), Js('Ife'), Js('Imam'), Js('Isa'), Js('Ismaila'), Js('Ja'), Js('Jabilo'), Js('Jabulani'), Js('Jafaru'), Js('Jalil'), Js('Jamal'), Js('Jibril'), Js('Junaidu'), Js('Kamil'), Js('Kareem'), Js('Katungi'), Js('Khairi'), Js('Khalifah'), Js('Kiho'), Js('Kijana'), Js('Kimoni'), Js('Kinfe'), Js('Kione'), Js('Kirabo'), Js('Kiros'), Js('Kitoko'), Js('Koda'), Js('Kojo'), Js('Kupakwashe'), Js('Kuron'), Js('Kwame'), Js('Madaki'), Js('Mahdi'), Js('Mahmud'), Js('Malomo'), Js('Mansa'), Js('Mansur'), Js('Mariatu'), Js('Mashaka'), Js('Messina'), Js('Mhina'), Js('Mikaili'), Js('Milandu'), Js('Morathi'), Js('Muhktar'), Js('Muhsin'), Js('Mukasa'), Js('Musa'), Js('Musawenkosi'), Js('Musoke'), Js('Mustafa'), Js('Nabil'), Js('Nabulung'), Js('Naiser'), Js('Nakima'), Js('Nalo'), Js('Nasir'), Js('Natine'), Js('Nikeese'), Js('Nyack'), Js('Nyako'), Js('Nyoka'), Js('Oafe'), Js('Oba'), Js('Obiajulu'), Js('Ochen'), Js('Odion'), Js('Okal'), Js('Okapi'), Js('Okoth'), Js('Ola'), Js('Omayma'), Js('Oni'), Js('Onika'), Js('Oringo'), Js('Otieno'), Js('Oto'), Js('Paki'), Js('Panyin'), Js('Paulo'), Js('Pemba'), Js('Phomello'), Js('Polo'), Js('Rabia'), Js('Rach'), Js('Rafiki'), Js('Rahid'), Js('Raimi'), Js('Ramses'), Js('Ranyshia'), Js('Rasheed'), Js('Rashidi'), Js('Razi'), Js('Reth'), Js('Roho'), Js('Runako'), Js('Russom'), Js('Ruzna'), Js('Sabola'), Js('Sadiki'), Js('Safina'), Js('Sahansan'), Js('Saidi'), Js('Salim'), Js('Sarda'), Js('Sarki'), Js('Seghen'), Js('Sekai'), Js('Selas'), Js('Shagari'), Js('Shehu'), Js('Tahir'), Js('Umar'), Js('Umaru'), Js('Usman'), Js('Yakubu'), Js('Yohance'), Js('Yohanna'), Js('Yusuf')]))
    var.put('nm2', Js([Js("A'isha"), Js('Adia'), Js('Aishatu'), Js('Aminah'), Js('Arria'), Js('Arziki'), Js('Asabe'), Js("Asma'u"), Js('Assibi'), Js('Atikah'), Js('Auta'), Js('Bahijjah'), Js('Balaraba'), Js('Baturiya'), Js('Cof'), Js('Coffee'), Js('Coffi'), Js('Coffie'), Js('Colee'), Js('Coley'), Js('Colie'), Js('Danuwa'), Js('Daurama'), Js('Delu'), Js('Dura'), Js('Durah'), Js('Durrah'), Js("Fa'idah"), Js("Fa'iqah"), Js("Fa'izah"), Js('Fara'), Js('Faraa'), Js('Fari'), Js('Farih'), Js('Farra'), Js('Farry'), Js('Fatima'), Js('Fatimah'), Js('Fatuma'), Js('Fayola'), Js('Femi'), Js('Finesse'), Js('Finn'), Js('Gaddo'), Js('Gambo'), Js('Gerda'), Js('Gimbya'), Js('Gobad'), Js('Gogo'), Js('Gzifa'), Js('Habiba'), Js('Habibah'), Js('Habika'), Js('Hada'), Js('Hafsah'), Js('Halimah'), Js('Hamidah'), Js('Hanna'), Js('Hassana'), Js('Hazika'), Js('Hola'), Js('Hova'), Js('Husiana'), Js('Huso'), Js('Hussaina'), Js('Ice'), Js('Ifama'), Js('Ifeoma'), Js('Ifiok'), Js('Ifrah'), Js('Ijaba'), Js('Iman'), Js('Ina'), Js('Iverem'), Js('Iyangura'), Js('Izefia'), Js('Izza'), Js('Jabulela'), Js('Jaha'), Js('Jahzara'), Js('Jamilah'), Js('Jummai'), Js('Kaka'), Js('Keyara'), Js('Khadija'), Js('Khadijah'), Js('Khamees'), Js('Khamisa'), Js('Khari'), Js('Khatiti'), Js('Kia'), Js('Kianga'), Js('Kibibi'), Js('Kiden'), Js('Kifle'), Js('Kiho'), Js('Kijana'), Js('Kima'), Js('Kimmy'), Js('Kinfe'), Js('Kione'), Js('Kirabo'), Js('Kiros'), Js('Kisser'), Js('Kitoko'), Js('Koda'), Js('Koko'), Js('Kubra'), Js('Kuron'), Js('Kwesi'), Js('Kya'), Js('Ladi'), Js('Lami'), Js('Lantana'), Js('Laraba'), Js('Larai'), Js('Latifah'), Js('Lawanna'), Js('Layla'), Js('Lehana'), Js('Lina'), Js('Lisha'), Js('Lubabah'), Js('Maimuna'), Js('Malomo'), Js('Mandze'), Js('Manica'), Js('Mansa'), Js('Mansurah'), Js('Mapenzi'), Js('Mardea'), Js('Mariama'), Js('Mariatu'), Js('Marka'), Js('Markabo'), Js('Maryam'), Js('Mashaka'), Js('Massassi'), Js('Mawunyaga'), Js('Meria'), Js('Messina'), Js('Mhina'), Js('Mikaili'), Js('Milandu'), Js('Miniya'), Js('Miyanda'), Js('Monifa'), Js('Montsho'), Js('Muna'), Js('Musoke'), Js('Mutia'), Js('Myeisha'), Js("Na'imah"), Js('Nabilah'), Js('Nadifa'), Js('Nadira'), Js('Nafisa'), Js('Nafisah'), Js('Nafuna'), Js('Nagesa'), Js('Nailah'), Js('Naiser'), Js('Naja'), Js('Najja'), Js('Naki'), Js('Nakima'), Js('Nala'), Js('Naliaka'), Js('Nalo'), Js('Namazzi'), Js('Nana'), Js('Nangila'), Js('Nantale'), Js('Nasha'), Js('Nashwa'), Js('Nasiche'), Js('Natine'), Js('Nazi'), Js('Ndila'), Js('Neema'), Js('Nehanda'), Js('Neliah'), Js('Nia'), Js('Nini'), Js('Njemile'), Js('Nkechi'), Js('Nuru'), Js('Nyack'), Js('Nyaga'), Js('Nyako'), Js('Nyeki'), Js('Nyoka'), Js('Okimma'), Js('Oafe'), Js('Oba'), Js('Obax'), Js('Okal'), Js('Okapi'), Js('Okoth'), Js('Ola'), Js('Olayinka'), Js('Olisa'), Js('Onaedo'), Js('Oni'), Js('Ontibile'), Js('Orma'), Js('Pangi'), Js('Panya'), Js('Panyin'), Js('Pemba'), Js('Phenyo'), Js('Qwara'), Js('Raashida'), Js("Rabi'ah"), Js('Rabia'), Js('Rach'), Js('Radhiya'), Js('Rafiki'), Js('Rahmah'), Js('Ramla'), Js('Raniesha'), Js('Rashidah'), Js('Raziya'), Js('Rehema'), Js('Rena'), Js('Renah'), Js('Renna'), Js('Ruqayyah'), Js('Saada'), Js('Sade'), Js('Sadiki'), Js('Sadio'), Js('Safara'), Js('Safia'), Js('Safina'), Js('Safiyah'), Js('Saida'), Js('Saidah'), Js('Saidi'), Js('Sakinah'), Js('Salama'), Js('Salihah'), Js('Salimah'), Js('Samirah'), Js('Sanura'), Js('Sarama'), Js('Saran'), Js('Sarda'), Js('Sarki'), Js('Sauda'), Js('Seghen'), Js('Sekai'), Js('Selam'), Js('Selamawit'), Js('Selas'), Js('Semira'), Js('Shukriyah'), Js('Sumayyah'), Js('Talatu'), Js('Tani'), Js('Zahrah'), Js('Zainab'), Js('Zakiyyah'), Js('Zaytun'), Js('Zorra'), Js('Zubaydah')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
hausaNames = var.to_python()
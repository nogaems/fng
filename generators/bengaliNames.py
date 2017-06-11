__all__ = ['bengaliNames']

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
    var.put('nm1', Js([Js('Aalok'), Js('Aashish'), Js('Aashutosh'), Js('Abhijeet'), Js('Abhijit'), Js('Abhik'), Js('Abhimanuya'), Js('Abhimanya'), Js('Abhirup'), Js('Abhoy'), Js('Abhra'), Js('Achintya'), Js('Adler'), Js('Aghor'), Js('Ajeet'), Js('Ajit'), Js('Ajoy'), Js('Akhil'), Js('Akshay'), Js('Akshaya'), Js('Akshya'), Js('Alok'), Js('Alokendra'), Js('Amal'), Js('Amar'), Js('Amit'), Js('Amitaabh'), Js('Amitabh'), Js('Amitabha'), Js('Amitava'), Js('Amiya'), Js('Amolik'), Js('Ananda'), Js('Anik'), Js('Anil'), Js('Aniq'), Js('Anirudha'), Js('Anirvan'), Js('Anjuman'), Js('Anmol'), Js('Anoop'), Js('Anshumaan'), Js('Anshuman'), Js('Anupam'), Js('Anuraag'), Js('Anurag'), Js('Apoorva'), Js('Apurba'), Js('Apurva'), Js('Ardhendu'), Js('Arjun'), Js('Arka'), Js('Arnab'), Js('Arpan'), Js('Arun'), Js('Asheesh'), Js('Ashish'), Js('Ashok'), Js('Ashutosh'), Js('Asis'), Js('Asok'), Js('Asotosa'), Js('Aswinikumar'), Js('Atul'), Js('Baadal'), Js('Badal'), Js('Baldeb'), Js('Balendra'), Js('Balinder'), Js('Bankimchandra'), Js('Banshi'), Js('Banshidhar'), Js('Banshilal'), Js('Bansi'), Js('Bansidhar'), Js('Bansilal'), Js('Basant'), Js('Basil'), Js('Benoy'), Js('Bharat'), Js('Bhashkar'), Js('Bhaskor'), Js('Bhavani'), Js('Bhola'), Js('Bholanath'), Js('Bhoopendra'), Js('Bhubaneswar'), Js('Bhudeb'), Js('Bihari'), Js('Biharilal'), Js('Biju'), Js('Bimal'), Js('Biman'), Js('Binod'), Js('Bipin'), Js('Birendra'), Js('Birendramohan'), Js('Bishnu'), Js('Bishwa'), Js('Bishwanath'), Js('Biswajeet'), Js('Bitan'), Js('Brajamohan'), Js('Brajmohan'), Js('Brijamohan'), Js('Brijmohan'), Js('Buddhadeb'), Js('Chaaruchandra'), Js('Chaitan'), Js('Chakradhar'), Js('Chakrapaani'), Js('Chaman'), Js('Chamanlal'), Js('Champabati'), Js('Champavati'), Js('Chandan'), Js('Chandra'), Js('Chandrabhan'), Js('Chandrachur'), Js('Chandragupt'), Js('Chandrahaas'), Js('Chandrakiran'), Js('Chandrakishore'), Js('Chandrakumar'), Js('Chandramauli'), Js('Chandramohan'), Js('Chandran'), Js('Chandranath'), Js('Chandraprakaash'), Js('Chandraprakash'), Js('Chandrashekar'), Js('Chandrashekhar'), Js('Chandravadan'), Js('Charuchandra'), Js('Chaten'), Js('Chayan'), Js('Chetan'), Js('Chinmay'), Js('Chintan'), Js('Chirakumar'), Js('Chittaranjan'), Js('Deb'), Js('Debabrata'), Js('Debashis'), Js('Debashish'), Js('Debendra'), Js('Debendranath'), Js('Deepak'), Js('Deepankar'), Js('Deependra'), Js('Deependu'), Js('Deepesh'), Js('Deeptendu'), Js('Deeptimay'), Js('Deeptimoy'), Js('Dev Kumar'), Js('Devadas'), Js('Devakumar'), Js('Devdas'), Js('Deveedaas'), Js('Deveeprasad'), Js('Devendranath'), Js('Devesh'), Js('Devidaas'), Js('Devidas'), Js('Deviprasad'), Js('Dheerandra'), Js('Dheerendra'), Js('Dhir'), Js('Dhirendra'), Js('Dhirendro'), Js('Dinabandhu'), Js('Dinesh'), Js('Dipankar'), Js('Dipen'), Js('Dipendra'), Js('Dipesh'), Js('Diptendu'), Js('Dwaraka'), Js('Dwarakaa'), Js('Dwarka'), Js('Dwarka Nath'), Js('Dwarkanath'), Js('Dwijendra'), Js('Dwijendralal'), Js('Dwijendranath'), Js('Dwijesh'), Js('Eekalabya'), Js('Ekalavya'), Js('Ekambar'), Js('Eknath'), Js('Faalgun'), Js('Falgu'), Js('Falgun'), Js('Fanibhusan'), Js('Fanish'), Js('Gadhar'), Js('Gagan'), Js('Gajendra'), Js('Gajendranath'), Js('Ganesh'), Js('Gangesh'), Js('Gaurav'), Js('Gaureeshankar'), Js('Gaurinandan'), Js('Gaurishankar'), Js('Gautam'), Js('Gautama'), Js('Girish'), Js('Gobardhan'), Js('Gobinda'), Js('Gopaal'), Js('Gopal'), Js('Gopalgobinda'), Js('Gopichand'), Js('Gour'), Js('Gourab'), Js('Gourinandan'), Js('Gourishankar'), Js('Goutam'), Js('Guru'), Js('Gurupada'), Js('Hari'), Js('Harihar'), Js('Harit'), Js('Harsh'), Js('Harsha'), Js('Hem'), Js('Hemanga'), Js('Hemchandra'), Js('Heramba'), Js('Herambwa'), Js('Himadri'), Js('Himaghana'), Js('Himanish'), Js('Hiran'), Js('Hiranmay'), Js('Hiranmaya'), Js('Hrishab'), Js('Hrishabh'), Js('Indra'), Js('Indrajit'), Js('Indranil'), Js('Indrashis'), Js('Indrashish'), Js('Ishwar'), Js('Jagadish'), Js('Jagadisha'), Js('Jagannath'), Js('Jagat'), Js('Jagdish'), Js('Jaidev'), Js('Jaladhar'), Js('Jatindra'), Js('Jatindranath'), Js('Jay'), Js('Jayanta'), Js('Jayashish'), Js('Jaydeb'), Js('Joy'), Js('Kailash'), Js('Kamal'), Js('Lalit'), Js('Malay'), Js('Mihir'), Js('Milan'), Js('Mithun'), Js('Nayan'), Js('Nikhil'), Js('Pabok'), Js('Parth'), Js('Partho'), Js('Phanish'), Js('Pranab'), Js('Pranav'), Js('Ramesh'), Js('Rishabh'), Js('Roshan'), Js('Sanjay'), Js('Satyajeet'), Js('Satyajit'), Js('Satyen'), Js('Shaan'), Js('Shantanu'), Js('Shisheer'), Js('Shishir'), Js('Shubhang'), Js('Sisir'), Js('Som'), Js('Som Nath'), Js('Somu'), Js('Sonu'), Js('Subhash'), Js('Sudeep'), Js('Sudip'), Js('Suresh'), Js('Swapnil'), Js('Tapas'), Js('Utpal'), Js('Vikrant'), Js('Vinod'), Js('Virendra'), Js('Vishwajeet'), Js('Vishwajit'), Js('Vishwanath'), Js('Vivek')]))
    var.put('nm2', Js([Js('Aishwarya'), Js('Aiswarya'), Js('Ajanta'), Js('Ali'), Js('Amala'), Js('Amla'), Js('Amodita'), Js('Amolika'), Js('Amrita'), Js('Amritambu'), Js('Amrusha'), Js('Anasooya'), Js('Anasuya'), Js('Anindita'), Js('Anjali'), Js('Ankolika'), Js('Anmolika'), Js('Annapoorna'), Js('Annapurna'), Js('Anshula'), Js('Anupama'), Js('Anuradha'), Js('Anurupa'), Js('Anusuya'), Js('Aparajita'), Js('Aparijita'), Js('Aparna'), Js('Archana'), Js('Arpita'), Js('Aruna'), Js('Arundhati'), Js('Arunima'), Js('Aswini'), Js('Atreyee'), Js('Atreyi'), Js('Ayanna'), Js('Baijayanti'), Js('Bakul'), Js('Bandana'), Js('Bani'), Js('Bansari'), Js('Banshari'), Js('Barnali'), Js('Barsha'), Js('Baruna'), Js('Baruni'), Js('Bhaarati'), Js('Bhaavana'), Js('Bhabani'), Js('Bharati'), Js('Bhavana'), Js('Bhavini'), Js('Bhavna'), Js('Bhoomika'), Js('Bhumika'), Js('Bibha'), Js('Bibhuti'), Js('Bijoya'), Js('Bimala'), Js('Bimla'), Js('Bindu'), Js('Binita'), Js('Binodini'), Js('Bipasha'), Js('Bithika'), Js('Bratati'), Js('Brinda'), Js('Chaitali'), Js('Chakrika'), Js('Chameli'), Js('Chamelia'), Js('Champa'), Js('Chanchala'), Js('Chandi'), Js('Chandira'), Js('Chandra'), Js('Chandrabali'), Js('Chandrakala'), Js('Chandrakanta'), Js('Chandrani'), Js('Chandrima'), Js('Charu'), Js('Charvi'), Js('Chitra'), Js('Chitralekha'), Js('Daevi'), Js('Damayanti'), Js('Damyanti'), Js('Darpana'), Js('Debi'), Js('Deepa'), Js('Deepali'), Js('Deeptimayee'), Js('Deeptimoyee'), Js('Devi'), Js('Dhara'), Js('Dhriti'), Js('Dipali'), Js('Divya'), Js('Doyel'), Js('Drishti'), Js('Dristi'), Js('Durba'), Js('Durga'), Js('Durva'), Js('Eenakshi'), Js('Eesha'), Js('Ekantika'), Js('Ekaparana'), Js('Ekata'), Js('Ekavali'), Js('Ekta'), Js('Ektaa'), Js('Esha'), Js('Falguni'), Js('Fullara'), Js('Gargi'), Js('Geet'), Js('Geeta'), Js('Geetanjali'), Js('Gitanjali'), Js('Himani'), Js('Jagruti'), Js('Jaya'), Js('Jyoti'), Js('Kajol'), Js('Kalpana'), Js('Kanan'), Js('Kanchan'), Js('Kanchana'), Js('Kanika'), Js('Karuna'), Js('Kasturi'), Js('Kishori'), Js('Komal'), Js('Komali'), Js('Kshipra'), Js('Laboni'), Js('Lalima'), Js('Lalita'), Js('Leena'), Js('Lekha'), Js('Manali'), Js('Mausami'), Js('Minaxi'), Js('Mishti'), Js('Nalini'), Js('Nandita'), Js('Nilima'), Js('Oormila'), Js('Paromita'), Js('Pauravi'), Js('Phalguni'), Js('Prachi'), Js('Prafula'), Js('Prafulla'), Js('Prakruti'), Js('Pratima'), Js('Promita'), Js('Pushpa'), Js('Puspa'), Js('Rachana'), Js('Rachna'), Js('Rajani'), Js('Ramaa'), Js('Rani'), Js('Ruma'), Js('Saheli'), Js('Sahira'), Js('Samali'), Js('Sangeeta'), Js('Sangita'), Js('Sarita'), Js('Sarmila'), Js('Shefali'), Js('Shila'), Js('Shipra'), Js('Shomili'), Js('Subhashini'), Js('Suparna'), Js('Suravi'), Js('Sushma'), Js('Sushmita'), Js('Swati'), Js('Taneesha'), Js('Tara'), Js('Trisha'), Js('Trishana'), Js('Ujjwala'), Js('Ujwala'), Js('Upasana'), Js('Urmila'), Js('Usha'), Js('Vandana'), Js('Vanita'), Js('Varsha'), Js('Varuna'), Js('Varuni'), Js('Vibhuti'), Js('Vijaya'), Js('Vinita'), Js('Vipasha'), Js('Vrishti'), Js('Yamini'), Js('Yamuna')]))
    var.put('nm3', Js([Js('Abed'), Js('Abhedananda'), Js('Acharya'), Js('Acharyya'), Js('Adhikari'), Js('Aich'), Js('Alam'), Js('Alim'), Js('Asad'), Js('Asharaful'), Js('Azam'), Js('Babaji'), Js('Bachchan'), Js('Bachchu'), Js('Bagchi'), Js('Baidya'), Js('Baij'), Js('Bakshi'), Js('Banarje'), Js('Bandopadhyay'), Js('Bandyopadhyay'), Js('Banerjee'), Js('Bardhan'), Js('Barkat'), Js('Barua'), Js('Basak'), Js('Basu'), Js('Begum'), Js('Bhaduri'), Js('Bhanja'), Js('Bharadwaj'), Js('Bhattacharya'), Js('Bhattacharyya'), Js('Bhonda'), Js('Bhowmick'), Js('Bhuiyan'), Js('Bisharad'), Js('Biswas'), Js('Boral'), Js('Bose'), Js('Brahmachari'), Js('Brahmananda'), Js('Brata'), Js('Buksh'), Js('Chakrabarti'), Js('Chakrabarty'), Js('Chakraborty'), Js('Chakravarty'), Js('Chakravorty'), Js('Chakrobarty'), Js('Chandra'), Js('Chatterjee'), Js('Chattopadhyay'), Js('Chaudhuri'), Js('Chinmoy'), Js('Choudhry'), Js('Choudhury'), Js('Chowdhury'), Js('Chowdury'), Js('Dabaji'), Js('Dam'), Js('Das'), Js('Dasgupta'), Js('Datta'), Js('Debnath'), Js('Debroy'), Js('Devi'), Js('Dey'), Js('Dinda'), Js('Dutt'), Js('Dutta'), Js('Gain'), Js('Gangopadhyay'), Js('Ganguli'), Js('Ganguly'), Js('Gayen'), Js('Ghani'), Js('Ghatak'), Js('Ghose'), Js('Ghosemajumder'), Js('Ghosh'), Js('Ghoshal'), Js('Giri'), Js('Goswami'), Js('Guha'), Js('Guhathakurta'), Js('Gupta'), Js('Hamid'), Js('Haque'), Js('Hazra'), Js('Hore'), Js('Hossain'), Js('Huq'), Js('Jain'), Js('Jatin'), Js('Joyanto'), Js('Kabir'), Js('Kalyanpur'), Js('Kar'), Js('Karim'), Js('Karmakar'), Js('Khan'), Js('Khanum'), Js('Khuro'), Js('Kivaraj'), Js('Kotal'), Js('Kriplani'), Js('Kumar'), Js('Lahiri'), Js('Latif'), Js('Lohani'), Js('MAmun'), Js('Magsaysay'), Js('Mahalanabis'), Js('Mahalanobis'), Js('Maharaj'), Js('Mahasaya'), Js('Mahmud'), Js('Maitra'), Js('Maity'), Js('Maji'), Js('Majumdar'), Js('Majumder'), Js('Malakar'), Js('Mallick'), Js('Mandal'), Js('Manwar'), Js('Matri'), Js('Mazumdar'), Js('Mazumder'), Js('Miah'), Js('Mirza'), Js('Mitra'), Js('Mokammel'), Js('Momen'), Js('Mondal'), Js('Muhkerjee'), Js('Mukerjea'), Js('Mukerji'), Js('Mukharji'), Js('Mukherjee'), Js('Mukherji'), Js('Mukhopadhyay'), Js('Mukhopdadhyay'), Js('Mullick'), Js('Munindra'), Js('Murshid'), Js('Musa'), Js('Nabi'), Js('Nag'), Js('Nagari'), Js('Nagchaudhuri'), Js('Naidu'), Js('Nandi'), Js('Nandy'), Js('Nasrin'), Js('Nazimuddin'), Js('Niyogi'), Js('Ojha'), Js('Osmani'), Js('Pal'), Js('Panja'), Js('Paramahamsa'), Js('Parveen'), Js('Phonte'), Js('PrabhupÄ�da'), Js('Pramanick'), Js('Pramanik'), Js('Pyne'), Js('Qamar'), Js('Quadir'), Js('Raha'), Js('Rahaman'), Js('Rahman'), Js('Rai'), Js('Raihan'), Js('Rakib'), Js('Rani'), Js('Ranjan'), Js('Rashmoni'), Js('Ray'), Js('Raychaudhuri'), Js('Roy'), Js('Sagnik'), Js('Saha'), Js('Salimullah'), Js('Samad'), Js('Sana'), Js('Sanu'), Js('Sanyal'), Js('Sarasvati'), Js('Saraswat'), Js('Sarkar'), Js('Sasmal'), Js('Sastri'), Js('Satyananda'), Js('Sayeed'), Js('Sekhar'), Js('Sen'), Js('Sengupta'), Js('Sett'), Js('Shahidullah'), Js('Shaikh'), Js('Shankar'), Js('Sharma'), Js('Shastri'), Js('Shekhar'), Js('Shome'), Js('Shonku'), Js('Sikdar'), Js('Sil'), Js('Singh'), Js('Sinha'), Js('Siraj'), Js('Sircar'), Js('Sobhan'), Js('Som'), Js('Sorcar'), Js('Suhrawardy'), Js('Sumon'), Js('Tagore'), Js('Talukdar'), Js('Thakur'), Js('Thakurta'), Js('Uddin'), Js('Vibhushan'), Js('Vidyabhusan'), Js('Vidyasagar'), Js('Vivekananda'), Js('Waddedar'), Js('Yagnik'), Js('Yunus'), Js('Zia')]))
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
bengaliNames = var.to_python()
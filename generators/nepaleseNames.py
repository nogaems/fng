__all__ = ['nepaleseNames']

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
var.put('nm1', Js([Js('Aadarsh'), Js('Aadesh'), Js('Aadi'), Js('Aaditey'), Js('Aaditya'), Js('Aakaash'), Js('Aakarshan'), Js('Aakash'), Js('Aalok'), Js('Aamod'), Js('Aanand'), Js('Aananda'), Js('Aastik'), Js('Abhay'), Js('Abhaya'), Js('Abhijeet'), Js('Abhijit'), Js('Abhiman'), Js('Abhimanyu'), Js('Abhinabhas'), Js('Abhinav'), Js('Abhinava'), Js('Abhishek'), Js('Achyut'), Js('Achyuta'), Js('Adesh'), Js('Adhiraj'), Js('Adinath'), Js('Agni'), Js('Ajay'), Js('Ajaya'), Js('Ajeet'), Js('Ajendra'), Js('Ajit'), Js('Akaash'), Js('Akash'), Js('Akhilesh'), Js('Akshay'), Js('Akshaya'), Js('Alaap'), Js('Alok'), Js('Amalesh'), Js('Amar'), Js('Ambar'), Js('Amber'), Js('Amir'), Js('Amitabh'), Js('Amod'), Js('Amrit'), Js('Anand'), Js('Anant'), Js('Ananta'), Js('Anil'), Js('Anjani'), Js('Anjay'), Js('Ankit'), Js('Anniruddha'), Js('Anoj'), Js('Anuj'), Js('Anup'), Js('Anuraag'), Js('Anurag'), Js('Arjun'), Js('Arun'), Js('Ashok'), Js('Ashutosh'), Js('Atul'), Js('Atulya'), Js('Avaneesh'), Js('Avanish'), Js('Ayush'), Js('Babu'), Js('Baburam'), Js('Badal'), Js('Badri'), Js('Badrinath'), Js('Bahadur'), Js('Baikuntha'), Js('Bajra'), Js('Balaraj'), Js('Balbir'), Js('Baldev'), Js('Balgopal'), Js('Balgovind'), Js('Balkrishan'), Js('Balmohan'), Js('Balraj'), Js('Balram'), Js('Balwant'), Js('Bandhu'), Js('Barun'), Js('Basant'), Js('Basistha'), Js('Basudev'), Js('Bhagwan'), Js('Bhairab'), Js('Bhairav'), Js('Bhakti'), Js('Bhanu'), Js('Bharadwaj'), Js('Bharat'), Js('Bhaskar'), Js('Bhavesh'), Js('Bhim'), Js('Bhupendra'), Js('Bhuwan'), Js('Bhuwaneshwar'), Js('Bibek'), Js('Bibhaakar'), Js('Bidur'), Js('Bijay'), Js('Bijendra'), Js('Bijanyendra'), Js('Bikash'), Js('Bikesh'), Js('Bikram'), Js('Bimal'), Js('Binay'), Js('Binaya'), Js('Bindeshwor'), Js('Binit'), Js('Binod'), Js('Bipin'), Js('Biplav'), Js('Biraj'), Js('Birbal'), Js('Birendra'), Js('Bishal'), Js('Bishwa'), Js('Bishwambhar'), Js('Bishweshwar'), Js('Biswa'), Js('Biswajit'), Js('Bodhan'), Js('Brajesh'), Js('Bramha'), Js('Brijesh'), Js('Brijmohan'), Js('Buddha'), Js('Byas'), Js('Chakra'), Js('Chakrapani'), Js('Chanakya'), Js('Chandan'), Js('Chandeshwor'), Js('Chandra'), Js('Chandrashekhar'), Js('Chetan'), Js('Chintamani'), Js('Chintan'), Js('Chirag'), Js('Chiranjeev'), Js('Chiranjibi'), Js('Chittaranjan'), Js('Chudamani'), Js('Damodar'), Js('Danbir'), Js('Danvir'), Js('Dasharath'), Js('Daya'), Js('Dayanand'), Js('Debendra'), Js('Deenabandhu'), Js('Deepak'), Js('Deepiti'), Js('Devdas'), Js('Devendra'), Js('Dhan'), Js('Dhana'), Js('Dhananjay'), Js('Dharanidhar'), Js('Dharma'), Js('Dharmalal'), Js('Dharmendra'), Js('Dheer'), Js('Dheerendra'), Js('Dhir'), Js('Dhiren'), Js('Dhirendra'), Js('Dhruba'), Js('Dhyaneshwar'), Js('Digambar'), Js('Dilaram'), Js('Dileep'), Js('Dilip'), Js('Dinakar'), Js('Dinesh'), Js('Dipak'), Js('Dipendra'), Js('Dipesh'), Js('Divaj'), Js('Divakar'), Js('Diwakar'), Js('Durgesh'), Js('Ekalavya'), Js('Ekaraj'), Js('Fanindra'), Js('Fanishwar'), Js('Gagan'), Js('Gajendra'), Js('Ganapati'), Js('Ganesh'), Js('Gangadhar'), Js('Gaurav'), Js('Gautam'), Js('Ghanashyam'), Js('Giridhar'), Js('Girija'), Js('Giriraj'), Js('Gokul'), Js('Gopal'), Js('Gopi'), Js('Gourishankar'), Js('Govinda'), Js('Gunaratna'), Js('Gurudutt'), Js('Gyan'), Js('Gyanedra'), Js('Gyaneshwar'), Js('Hanuman'), Js('Hari'), Js('Harigopal'), Js('Harihar'), Js('Harinarayan'), Js('Harish'), Js('Hasan'), Js('Hem'), Js('Hemachandra'), Js('Hemant'), Js('Himal'), Js('Himanshu'), Js('Hitesh'), Js('Hridaya'), Js('Hridayesh'), Js('Iman'), Js('Indra'), Js('Indrajeet'), Js('Indrajit'), Js('Ishwar'), Js('Jagadeep'), Js('Jagadish'), Js('Jagajeet'), Js('Jagannath'), Js('Jagat'), Js('Jagdish'), Js('Janak'), Js('Janardan'), Js('Jaswant'), Js('Jaya'), Js('Jayadev'), Js('Jayant'), Js('Jayanta'), Js('Jeevan'), Js('Jibachh'), Js('Jitendra'), Js('Jivan'), Js('Jiwan'), Js('Kabi'), Js('Kabir'), Js('Kaila'), Js('Kailash'), Js('Kalyan'), Js('Kamadev'), Js('Kamal'), Js('Kamlesh'), Js('Kanchha'), Js('Kapil'), Js('Karna'), Js('Kashyap'), Js('Kasindra'), Js('Kaushal'), Js('Kaushik'), Js('Kavi'), Js('Kedar'), Js('Kesar'), Js('Keshab'), Js('Keshav'), Js('Khagendra'), Js('Khem'), Js('Kiran'), Js('Kishor'), Js('Kishore'), Js('Kripal'), Js('Kris'), Js('Kuber'), Js('Kuldeep'), Js('Kumar'), Js('Kundan'), Js('Lakshman'), Js('Lalan'), Js('Lalit'), Js('Lokesh'), Js('Loknath'), Js('Madan'), Js('Madhav'), Js('Madhukar'), Js('Madhur'), Js('Madhusudan'), Js('Mahadev'), Js('Mahant'), Js('Mahavir'), Js('Mahendra'), Js('Mahesh'), Js('Maheshwar'), Js('Maila'), Js('Mandeep'), Js('Mangal'), Js('Mangesh'), Js('Manish'), Js('Manjeet'), Js('Manjit'), Js('Manjul'), Js('Manmohan'), Js('Manohar'), Js('Manoj'), Js('Milan'), Js('Mithilesh'), Js('Mithun'), Js('Mohan'), Js('Mohit'), Js('Mrigendra'), Js('Mukesh'), Js('Mukta'), Js('Mukti'), Js('Murali'), Js('Nabin'), Js('Nagendra'), Js('Nakul'), Js('Nandakishor'), Js('Nandan'), Js('Nandlal'), Js('Narahari'), Js('Narayan'), Js('Narendra'), Js('Naresh'), Js('Natwar'), Js('Naveen'), Js('Navin'), Js('Nawal'), Js('Neelambar'), Js('Neeraj'), Js('Niketan'), Js('Nikhil'), Js('Nikhilesh'), Js('Niraj'), Js('Niranjan'), Js('Nirbhaya'), Js('Nirmal'), Js('Nischal'), Js('Nishant'), Js('Nishanta'), Js('Nuraj'), Js('Om'), Js('Omkar'), Js('Omprakash'), Js('Paaras'), Js('Pankaj'), Js('Parakram'), Js('Paramananda'), Js('Parameshwar'), Js('Paras'), Js('Parbat'), Js('Parvat'), Js('Parvesh'), Js('Parwesh'), Js('Pasang'), Js('Pavan'), Js('Pawan'), Js('Phanindra'), Js('Phanishwar'), Js('Pitambar'), Js('Poonyeah'), Js('Poorna'), Js('Prabal'), Js('Prabhakar'), Js('Prabhat'), Js('Prabhu'), Js('Prabin'), Js('Prabuddha'), Js('Pradeep'), Js('Pradip'), Js('Prahalad'), Js('Prajeet'), Js('Prajit'), Js('Prakash'), Js('Pramesh'), Js('Pramod'), Js('Prasad'), Js('Prashant'), Js('Pratap'), Js('Pratik'), Js('Praval'), Js('Praveen'), Js('Pravin'), Js('Prawal'), Js('Prayag'), Js('Prem'), Js('Pritam'), Js('Prithivi'), Js('Prithvi'), Js('Puneet'), Js('Punit'), Js('Purna'), Js('Purushottam'), Js('Pushkar'), Js('Rabi'), Js('Rabin'), Js('Rabindra'), Js('Raghab'), Js('Raghav'), Js('Raghu'), Js('Rahul'), Js('Raj'), Js('Raja'), Js('Rajan'), Js('Rajaram'), Js('Rajeev'), Js('Rajendra'), Js('Rajesh'), Js('Rajiv'), Js('Rajkumar'), Js('Raju'), Js('Rajyeshwar'), Js('Rakesh'), Js('Ram'), Js('Raman'), Js('Ramchandra'), Js('Ramesh'), Js('Rameshwar'), Js('Ramkrishna'), Js('Randhir'), Js('Ranjan'), Js('Ranjeet'), Js('Ranjit'), Js('Rashmi'), Js('Ratna'), Js('Ravi'), Js('Ravikiran'), Js('Ravindra'), Js('Resham'), Js('Rijan'), Js('Rijendra'), Js('Rishabh'), Js('Rishav'), Js('Rishi'), Js('Rishikesh'), Js('Rohan'), Js('Rohit'), Js('Roopak'), Js('Roshan'), Js('Rudra'), Js('Rupak'), Js('Rushav'), Js('Sabin'), Js('Sachin'), Js('Sachindra'), Js('Sagar'), Js('Sahadev'), Js('Sameer'), Js('Samir'), Js('Samrat'), Js('Sandeep'), Js('Sanjay'), Js('Sanjeev'), Js('Sanjiv'), Js('Santosh'), Js('Sarbagya'), Js('Sarbodaya'), Js('Satindra'), Js('Satish'), Js('Satyajit'), Js('Satyanarayan'), Js('Satyendra'), Js('Saubhagya'), Js('Saurabh'), Js('Saurav'), Js('Shaan'), Js('Shahid'), Js('Shailen'), Js('Shailendra'), Js('Shailesh'), Js('Shakti'), Js('Shambhu'), Js('Shamsher'), Js('Shankar'), Js('Shashank'), Js('Shashi'), Js('Shekhar'), Js('Shridhar'), Js('Shrikanta'), Js('Shrikrishna'), Js('Shyam'), Js('Shyamal'), Js('Shyamsundar'), Js('Siddhanta'), Js('Siddhartha'), Js('Sikendra'), Js('Sitaram'), Js('Sohan'), Js('Sridhar'), Js('Subas'), Js('Subhas'), Js('Subhash'), Js('Subhodha'), Js('Subodh'), Js('Sudeep'), Js('Sudhakar'), Js('Sudheer'), Js('Sudhir'), Js('Sudip'), Js('Suman'), Js('Sumesh'), Js('Sundar'), Js('Sundip'), Js('Sunil'), Js('Suraj'), Js('Suren'), Js('Surendra'), Js('Suresh'), Js('Surya'), Js('Susan'), Js('Sushil'), Js('Swagat'), Js('Swarup'), Js('Swayambhu'), Js('Tej'), Js('Thaila'), Js('Tilak'), Js('Tirtha'), Js('Tribhuvan'), Js('Trilochan'), Js('Trilok'), Js('Tsering'), Js('Tushar'), Js('Udit'), Js('Ujwal'), Js('Umesh'), Js('Upendra'), Js('Uttam'), Js('Vajra'), Js('Varun'), Js('Vasant'), Js('Vasishtha'), Js('Vasudev'), Js('Ved'), Js('Vikesh'), Js('Vikram'), Js('Vimal'), Js('Vinay'), Js('Vineet'), Js('Vipin'), Js('Vishal'), Js('Vyas'), Js('Yadab'), Js('Yadav'), Js('Yadunath'), Js('Yagya'), Js('Yam'), Js('Yogendra'), Js('Yogesh'), Js('Yuvaraj')]))
var.put('nm2', Js([Js('Aadi'), Js('Aakanksha'), Js('Aalaap'), Js('Aanchal'), Js('Aaradhana'), Js('Aarati'), Js('Aashika'), Js('Aayusha'), Js('Aayushma'), Js('Adesha'), Js('Adhipa'), Js('Agni'), Js('Aishwarya'), Js('Ajaya'), Js('Ajeeta'), Js('Alisa'), Js('Alisha'), Js('Ambika'), Js('Ameeri'), Js('Ameeta'), Js('Amira'), Js('Amiree'), Js('Amiri'), Js('Amita'), Js('Amla'), Js('Amrabati'), Js('Amreeta'), Js('Amrita'), Js('Amriti'), Js('Amshu'), Js('Amulyaa'), Js('Ananta'), Js('Anila'), Js('Anita'), Js('Anjala'), Js('Anjalee'), Js('Anjali'), Js('Anjanee'), Js('Anjani'), Js('Anju'), Js('Anjula'), Js('Ankita'), Js('Ankur'), Js('Anmol'), Js('Anshu'), Js('Anu'), Js('Anuja'), Js('Anupa'), Js('Anupam'), Js('Anushka'), Js('Apeksha'), Js('Arati'), Js('Archana'), Js('Arpan'), Js('Aruna'), Js('Arunee'), Js('Aruni'), Js('Aruradha'), Js('Atithee'), Js('Atithi'), Js('Atreya'), Js('Atulya'), Js('Ayusha'), Js('Balaji'), Js('Bandana'), Js('Barsha'), Js('Baruna'), Js('Basanta'), Js('Bechani'), Js('Beena'), Js('Beendu'), Js('Bhagirathi'), Js('Bhakti'), Js('Bharata'), Js('Bhavana'), Js('Bhawana'), Js('Bhoomi'), Js('Bhumeeja'), Js('Bhumi'), Js('Bhumija'), Js('Bhuwaneshwori'), Js('Bichitra'), Js('Bihaani'), Js('Bihanee'), Js('Bihani'), Js('Bijaya'), Js('Bijena'), Js('Bimala'), Js('Bina'), Js('Binaya'), Js('Bindu'), Js('Bindusar'), Js('Binita'), Js('Bipana'), Js('Bishala'), Js('Bishnu'), Js('Buddhimaya'), Js('Chaman'), Js('Chameli'), Js('Champa'), Js('Chanda'), Js('Chandan'), Js('Chandra'), Js('Chandrakala'), Js('Chandramaya'), Js('Chetana'), Js('Chhhaya'), Js('Chhinmaya'), Js('Chitra'), Js('Daksheena'), Js('Dakshina'), Js('Damini'), Js('Darpan'), Js('Daya'), Js('Debika'), Js('Deeksha'), Js('Deepa'), Js('Deepaka'), Js('Deepshikha'), Js('Deepsikha'), Js('Deepti'), Js('Deveeka'), Js('Devika'), Js('Dhan'), Js('Dhana'), Js('Dhanju'), Js('Dhankumari'), Js('Dhanmaya'), Js('Dhatri'), Js('Dhyanee'), Js('Dhyani'), Js('Dibya'), Js('Dikchha'), Js('Diksha'), Js('Dipa'), Js('Dipaka'), Js('Dipshika'), Js('Dipshikha'), Js('Divya'), Js('Diya'), Js('Dularee'), Js('Dulari'), Js('Durga'), Js('Dwarika'), Js('Falguni'), Js('Fulkumari'), Js('Ganga'), Js('Garima'), Js('Gauri'), Js('Geet'), Js('Geeta'), Js('Gireeja'), Js('Girija'), Js('Git'), Js('Gita'), Js('Goma'), Js('Gopee'), Js('Gopeeka'), Js('Gopi'), Js('Gopika'), Js('Grishma'), Js('Gulab'), Js('Gunaratna'), Js('Gunjan'), Js('Gyani'), Js('Gyanu'), Js('Hans'), Js('Harsa'), Js('Harsha'), Js('Hasana'), Js('Hasmi'), Js('Heena'), Js('Heera'), Js('Hema'), Js('Hemanta'), Js('Himaghna'), Js('Himal'), Js('Himani'), Js('Hina'), Js('Hira'), Js('Hiranya'), Js('Indra'), Js('Indrakala'), Js('Indraneel'), Js('Isha'), Js('Ishan'), Js('Ishika'), Js('Ishwari'), Js('Iswari'), Js('Jamuna'), Js('Janaki'), Js('Janu'), Js('Jaya'), Js('Jayanta'), Js('Jayantee'), Js('Jayanti'), Js('Jeevan'), Js('Jeevani'), Js('Jeeya'), Js('Jessica'), Js('Jethi'), Js('Jibachhi'), Js('Jibani'), Js('Jinat'), Js('Jivan'), Js('Jiya'), Js('Junu'), Js('Jyotee'), Js('Jyoti'), Js('Jyotshna'), Js('Kabeeta'), Js('Kabita'), Js('Kaili'), Js('Kali'), Js('Kalpana'), Js('Kalyani'), Js('Kamala'), Js('Kamaleshwori'), Js('Kamana'), Js('Kamini'), Js('Kanchan'), Js('Kanchhi'), Js('Kanti'), Js('Kareesma'), Js('Karisma'), Js('Karuna'), Js('Kasis'), Js('Kaushika'), Js('Kaushilya'), Js('Kausiki'), Js('Keeran'), Js('Kesari'), Js('Khusbhu'), Js('Kiran'), Js('Kirti'), Js('Komal'), Js('Kopeela'), Js('Kopila'), Js('Kripa'), Js('Krisha'), Js('Krishna'), Js('Kritee'), Js('Kriti'), Js('Kumari'), Js('Kumati'), Js('Kumud'), Js('Kusum'), Js('Kusunti'), Js('Kuwari'), Js('Lagan'), Js('Laila'), Js('Lalita'), Js('Laxmi'), Js('Leela'), Js('Lila'), Js('Lina'), Js('Lochan'), Js('Loleeta'), Js('Lolita'), Js('Madhu'), Js('Madhuri'), Js('Madhurima'), Js('Mahadevi'), Js('Maheshwari'), Js('Maili'), Js('Maina'), Js('Mainabati'), Js('Maiya'), Js('Mallika'), Js('Mamata'), Js('Mangita'), Js('Mani'), Js('Manila'), Js('Manisa'), Js('Manisha'), Js('Manjeeta'), Js('Manjita'), Js('Manju'), Js('Manjul'), Js('Manjula'), Js('Mankumari'), Js('Manmaya'), Js('Manu'), Js('Mathura'), Js('Maya'), Js('Mayabati'), Js('Mayur'), Js('Mayushi'), Js('Meenku'), Js('Meera'), Js('Meet'), Js('Meeta'), Js('Menka'), Js('Menku'), Js('Menuka'), Js('Milan'), Js('Minku'), Js('Mira'), Js('Mit'), Js('Mita'), Js('Mithila'), Js('Mitra'), Js('Mohani'), Js('Mohita'), Js('Motee'), Js('Moti'), Js('Mukta'), Js('Mukti'), Js('Muna'), Js('Muni'), Js('Murali'), Js('Murtee'), Js('Murti'), Js('Muzur'), Js('Nabina'), Js('Nabita'), Js('Nageena'), Js('Nagina'), Js('Naina'), Js('Nanda'), Js('Nandan'), Js('Nandanee'), Js('Nandani'), Js('Nanu'), Js('Narayani'), Js('Naveena'), Js('Navina'), Js('Neehal'), Js('Neehar'), Js('Neel'), Js('Neelam'), Js('Neena'), Js('Neera'), Js('Nihal'), Js('Nihar'), Js('Nikeeta'), Js('Niketan'), Js('Nikita'), Js('Nilam'), Js('Nina'), Js('Nipun'), Js('Nira'), Js('Nirmala'), Js('Nirupam'), Js('Nisha'), Js('Nishita'), Js('Nripa'), Js('Pabitra'), Js('Padma'), Js('Padmabati'), Js('Palash'), Js('Pallavee'), Js('Pallavi'), Js('Parbati'), Js('Pareejat'), Js('Parijat'), Js('Parimal'), Js('Partha'), Js('Parvati'), Js('Pavitra'), Js('Peenkee'), Js('Peenki'), Js('Phalguni'), Js('Phani'), Js('Pinki'), Js('Poojana'), Js('Prabha'), Js('Prabina'), Js('Pragya'), Js('Prajeeta'), Js('Prajita'), Js('Prakritee'), Js('Prakriti'), Js('Prameela'), Js('Pramila'), Js('Prasana'), Js('Prasata'), Js('Pratiksha'), Js('Praveena'), Js('Pravina'), Js('Preeti'), Js('Preeya'), Js('Preeyanka'), Js('Prema'), Js('Premkumari'), Js('Prenana'), Js('Prithivi'), Js('Prithvi'), Js('Priti'), Js('Priya'), Js('Priyanka'), Js('Puja'), Js('Punam'), Js('Puneeta'), Js('Punita'), Js('Punya'), Js('Purnima'), Js('Puspa'), Js('Putali'), Js('Rabina'), Js('Rachana'), Js('Radha'), Js('Radheeka'), Js('Radhika'), Js('Ragini'), Js('Raina'), Js('Rajani'), Js('Rajeshwori'), Js('Rajmati'), Js('Raksha'), Js('Ram kumari'), Js('Rama'), Js('Ramabati'), Js('Ramaiya'), Js('Ramani'), Js('Rameela'), Js('Rameeta'), Js('Ramila'), Js('Ramita'), Js('Rampyari'), Js('Ranamaya'), Js('Rang'), Js('Rangoli'), Js('Rani'), Js('Ranjan'), Js('Ranjana'), Js('Ranjeeta'), Js('Ranjita'), Js('Ranju'), Js('Raseela'), Js('Rashmi'), Js('Rasila'), Js('Rasmi'), Js('Ratna'), Js('Ratree'), Js('Ratri'), Js('Ravina'), Js('Reena'), Js('Reenkee'), Js('Reenki'), Js('Reenku'), Js('Reeta'), Js('Reeti'), Js('Reetu'), Js('Reeya'), Js('Rejeena'), Js('Rejina'), Js('Rekha'), Js('Renu'), Js('Renuka'), Js('Resami'), Js('Reshami'), Js('Richa'), Js('Riddhi'), Js('Rina'), Js('Rinki'), Js('Rinku'), Js('Rishi'), Js('Rishika'), Js('Rita'), Js('Riti'), Js('Ritu'), Js('Riya'), Js('Rohita'), Js('Rojeena'), Js('Rojina'), Js('Roma'), Js('Roshani'), Js('Roshni'), Js('Rosnee'), Js('Rudra'), Js('Rupa'), Js('Sabeena'), Js('Sabeeta'), Js('Sabina'), Js('Sabita'), Js('Sabitree'), Js('Sabitri'), Js('Sacheta'), Js('Sachina'), Js('Sachita'), Js('Sadhana'), Js('Safala'), Js('Safari'), Js('Sailaja'), Js('Saili'), Js('Sajal'), Js('Sajana'), Js('Sajeeta'), Js('Sajita'), Js('Sakshi'), Js('Samana'), Js('Sameera'), Js('Samira'), Js('Sancheeta'), Js('Sanchita'), Js('Sangeeta'), Js('Sangin'), Js('Sangita'), Js('Sanjana'), Js('Sanjeela'), Js('Sanjeeta'), Js('Sanjibnee'), Js('Sanjila'), Js('Sanjita'), Js('Sanjivni'), Js('Sanju'), Js('Santa'), Js('Santoshi'), Js('Sanumaya'), Js('Sapana'), Js('Sarala'), Js('Sarang'), Js('Saraswati'), Js('Sareena'), Js('Sareeta'), Js('Sarina'), Js('Sarita'), Js('Sarmeela'), Js('Sarmila'), Js('Saroja'), Js('Sarupa'), Js('Saubhagya'), Js('Saumya'), Js('Sauvagya'), Js('Seeya'), Js('Seti'), Js('Shakti'), Js('Shamita'), Js('Shanta'), Js('Shantee'), Js('Shanti'), Js('Shashi'), Js('Shasikala'), Js('Shesha'), Js('Shikha'), Js('Shiksha'), Js('Shital'), Js('Shitala'), Js('Shova'), Js('Shreya'), Js('Shreyashi'), Js('Shrisha'), Js('Shristi'), Js('Shubha'), Js('Shushila'), Js('Siddha'), Js('Siddhi'), Js('Siddhika'), Js('Simran'), Js('Sita'), Js('Siya'), Js('Sila'), Js('Sova'), Js('Sreejana'), Js('Srijana'), Js('Subhadra'), Js('Subheksha'), Js('Sudha'), Js('Sujaya'), Js('Sujeeta'), Js('Sujita'), Js('Sukanta'), Js('Sukriti'), Js('Sukumaya'), Js('Sulekha'), Js('Sulochana'), Js('Suman'), Js('Sumeeta'), Js('Sumita'), Js('Suneela'), Js('Suneeta'), Js('Sunila'), Js('Sunita'), Js('Suntali'), Js('Supreeya'), Js('Supriya'), Js('Surabi'), Js('Suravee'), Js('Suravi'), Js('Sureeta'), Js('Surita'), Js('Surya'), Js('Suryaa'), Js('Susheela'), Js('Sushila'), Js('Susila'), Js('Suskriti'), Js('Susma'), Js('Suveksha'), Js('Swapan'), Js('Swapnil'), Js('Swechchha'), Js('Sweksha'), Js('Swornim'), Js('Swornima'), Js('Tanuja'), Js('Tanushree'), Js('Tara'), Js('Taranee'), Js('Tarini'), Js('Teeka'), Js('Teja'), Js('Thaili'), Js('Thuli'), Js('Tika'), Js('Tulasi'), Js('Tulsi'), Js('Udaya'), Js('Udayaa'), Js('Ujjali'), Js('Ujwali'), Js('Uma'), Js('Umanga'), Js('Urbasi'), Js('Urmila'), Js('Uru'), Js('Utsav'), Js('Varuna'), Js('Vasanta'), Js('Vasava'), Js('Vimala'), Js('Vinaya'), Js('Vineeta'), Js('Vumeeja'), Js('Vumija'), Js('Yami')]))
var.put('nm3', Js([Js('Acharya'), Js('Adhikari'), Js('Adhikary'), Js('Agarwal'), Js('Agasti'), Js('Agrahari'), Js('Agrawal'), Js('Amatya'), Js('Ansari'), Js('Aryal'), Js('Awale'), Js('Awasthi'), Js('Bachhar'), Js('Badal'), Js('Bade'), Js('Bagale'), Js('Bahadur'), Js('Baidhya'), Js('Baidya'), Js('Bajagain'), Js('Bajgain'), Js('Bajimaya'), Js('Bajracharya'), Js('Bal'), Js('Bamrel'), Js('Bandyopadhyay'), Js('Banepali'), Js('Baniya'), Js('Banjade'), Js('Banjara'), Js('Bansal'), Js('Banskota'), Js('Banstola'), Js('Barakoti'), Js('Baral'), Js('Baruwal'), Js('Basnet'), Js('Basnyat'), Js('Bastakoti'), Js('Bastakoty'), Js('Bastola'), Js('Basukala'), Js('Basyal'), Js('Bataju'), Js('Batas'), Js('Belbase'), Js('Benjankar'), Js('Bhagat'), Js('Bhandari'), Js('Bhansali'), Js('Bhattachan'), Js('Bhattacharya'), Js('Bhetwal'), Js('Bhujail'), Js('Bhujel'), Js('Bhurtel'), Js('Bhusal'), Js('Bhutia'), Js('Bijukchhe'), Js('Bimb'), Js('Bisht'), Js('Bist'), Js('Bista'), Js('Bogati'), Js('Bohara'), Js('Bohra'), Js('Budathoki'), Js('Buddhacharya'), Js('Budhathoki'), Js('Byanjanakar'), Js('Byanjankar'), Js('Byanju'), Js('Chalise'), Js('Chalisey'), Js('Chamling'), Js('Chamrel'), Js('Chand'), Js('Chanda'), Js('Chapagain'), Js('Chapai'), Js('Chapain'), Js('Chataut'), Js('Chaudhari'), Js('Chaudhary'), Js('Chaudhuri'), Js('Chaulagain'), Js('Chitrakar'), Js('Choudhary'), Js('Choulagai'), Js('Dahal'), Js('Dangi'), Js('Dangol'), Js('Danuwar'), Js('Darji'), Js('Darlami'), Js('Dawadi'), Js('Deuja'), Js('Devaki'), Js('Devkota'), Js('Dhakal'), Js('Dhakwa'), Js('Dhamala'), Js('Dhami'), Js('Dharel'), Js('Dhewajoo'), Js('Dhimal'), Js('Dhital'), Js('Dhundup'), Js('Dhungana'), Js('Dhungel'), Js('Dolma'), Js('Dongol'), Js('Dulal'), Js('Dutta'), Js('Gadal'), Js('Gadtaula'), Js('Gaire'), Js('Gajmer'), Js('Gajurel'), Js('Gartaula'), Js('Gauchan'), Js('Gaudel'), Js('Gaundel'), Js('Gautam'), Js('Gazmer'), Js('Ghale'), Js('Ghimire'), Js('Ghorasaini'), Js('Giri'), Js('Gnawali'), Js('Gnyawali'), Js('Golchha'), Js('Gorkhali'), Js('Goudel'), Js('Gubhaju'), Js('Gupta'), Js('Guragai'), Js('Guragain'), Js('Gurung'), Js('Guruwacharya'), Js('Gyanwali'), Js('Gyawali'), Js('Hamal'), Js('Himanshu'), Js('Humagain'), Js('Hyoju'), Js('Jamarkattel'), Js('Jha'), Js('Jhapali'), Js('Jirel'), Js('Kandel'), Js('Kanel'), Js('Kansakar'), Js('Kantha'), Js('Kapali'), Js('Kaphle'), Js('Karkee'), Js('Karki'), Js('Karmacharya'), Js('Karn'), Js('Karna'), Js('Kasaju'), Js('Kashyap'), Js('Kattel'), Js('Kayastha'), Js('Keshari'), Js('Khadgi'), Js('Khadka'), Js('Khakurel'), Js('Khan'), Js('Khanal'), Js('Kharel'), Js('Khatioda'), Js('Khatiwada'), Js('Khetan'), Js('Khwaounju'), Js('Khwaunju'), Js('Koirala'), Js('Kolachapati'), Js('Kshatriya'), Js('Kshetri'), Js('Kunwar'), Js('Kunwer'), Js('Lawoti'), Js('Lekhak'), Js('Limbu'), Js('Luitail'), Js('Luitel'), Js('Madhikarmi'), Js('Magar'), Js('Maharjan'), Js('Mahat'), Js('Mahato'), Js('Mahto'), Js('Mainali'), Js('Malakar'), Js('Mali'), Js('Malla'), Js('Manandhar'), Js('Mandal'), Js('Marasini'), Js('Maskay'), Js('Maske'), Js('Maskey'), Js('Massali'), Js('Mathema'), Js('Mishra'), Js('Misra'), Js('Mitra'), Js('Modi'), Js('Moktan'), Js('Mukhia'), Js('Mulepati'), Js('Mulmi'), Js('Munakarmi'), Js('Munankarmi'), Js('Nagargoje'), Js('Nagarkoti'), Js('Nakarmi'), Js('Naulakha'), Js('Nayaju'), Js('Nayak'), Js('Nemkul'), Js('Neopane'), Js('Neupane'), Js('Nihure'), Js('Niraula'), Js('Niroula'), Js('Niyogi'), Js('Nyachhyon'), Js('Nyachyoo'), Js('Nyaupane'), Js('Ojha'), Js('Oli'), Js('Pageni'), Js('Pahadi'), Js('Pahari'), Js('Palikhe'), Js('Palikhey'), Js('Panday'), Js('Pande'), Js('Pandey'), Js('Pandeya'), Js('Pandit'), Js('Pangeni'), Js('Pant'), Js('Panta'), Js('Panth'), Js('Pantha'), Js('Panthee'), Js('Panthi'), Js('Parajuli'), Js('Pariyar'), Js('Parsai'), Js('Patel'), Js('Pathak'), Js('Paudel'), Js('Paudyal'), Js('Phuyal'), Js('Piya'), Js('Poddar'), Js('Pokharel'), Js('Pokhrel'), Js('Portel'), Js('Poudel'), Js('Poudyal'), Js('Pradhan'), Js('Pradhanang'), Js('Pradhananga'), Js('Prajapati'), Js('Prasai'), Js('Prasain'), Js('Pudasaini'), Js('Pun'), Js('Puri'), Js('Pyakurel'), Js('Pyakuryal'), Js('Rai'), Js('Rajak'), Js('Rajaure'), Js('Rajbanshi'), Js('Rajbhandari'), Js('Rajkarnikar'), Js('Rana'), Js('Ranjan'), Js('Ranjeet'), Js('Ranjit'), Js('Ranjitkar'), Js('Rasaili'), Js('Rasaily'), Js('Rauniyar'), Js('Raut'), Js('Rautela'), Js('Raval'), Js('Rawal'), Js('Rawat'), Js('Rayamajhi'), Js('Regmi'), Js('Rijal'), Js('Rimal'), Js('Risal'), Js('Rishal'), Js('Rizal'), Js('Roka'), Js('Rumba'), Js('Sadaula'), Js('Sahani'), Js('Sainju'), Js('Salike'), Js('Sapkota'), Js('Satyal'), Js('Sedhain'), Js('Shah'), Js('Sherpa'), Js('Shahi'), Js('Shakya'), Js('Sharma'), Js('Sherchan'), Js('Sherchand'), Js('Sherpa'), Js('Shilakar'), Js('Shilpakar'), Js('Shiwakoti'), Js('Shreesh'), Js('Shrestha'), Js('Shresthacharya'), Js('Shukla'), Js('Sigdel'), Js('Sijapati'), Js('Silpakar'), Js('Silwal'), Js('Sindhuliya'), Js('Singh'), Js('Sinha'), Js('Sinjali'), Js('Sinkhada'), Js('Sitaula'), Js('Sitoula'), Js('Siwakoti'), Js('Sodhi'), Js('Sonar'), Js('Sthapit'), Js('Subba'), Js('Subedee'), Js('Subedi'), Js('Subedy'), Js('Sunuwar'), Js('Sunwar'), Js('Suwal'), Js('Syangden'), Js('Syangjali'), Js('Tamang'), Js('Tamarkar'), Js('Tammrakar'), Js('Tamrakar'), Js('Tandukar'), Js('Thakur'), Js('Thakuri'), Js('Thami'), Js('Thapa'), Js('Thapalia'), Js('Thapaliya'), Js('Timalsina'), Js('Timilshina'), Js('Timilsina'), Js('Timsina'), Js('Tripathee'), Js('Tripathi'), Js('Tripathy'), Js('Tsering'), Js('Tshering'), Js('Tuladhar'), Js('Tumbahangphe'), Js('Tumbahangphey'), Js('Upadhayay'), Js('Upadhya'), Js('Upadhyay'), Js('Upadhyaya'), Js('Upreti'), Js('Uprety'), Js('Vaidya'), Js('Vaishnav'), Js('Vajracharya'), Js('Verma'), Js('Vidyadhar'), Js('Wagle'), Js('Waiba'), Js('Wasti'), Js('Wosti'), Js('Yadav'), Js('Yogi'), Js('Yonjan'), Js('Yonzon')]))
pass
pass


# Add lib to the module scope
nepaleseNames = var.to_python()
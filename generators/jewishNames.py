__all__ = ['jewishNames']

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
var.put('nm1', Js([Js('Chaim'), Js('Eliyohu'), Js('Mordechai'), Js('Boruch'), Js('Yitzchok'), Js('Yaakov'), Js('Avrohom'), Js('Moshe'), Js('Meir'), Js('Dovid'), Js('Ahron'), Js('Shlomo'), Js('Yehuda'), Js('Avishay'), Js('Gal'), Js('Don'), Js('Yeruchum'), Js('Akiva'), Js('Yonatan'), Js('Shmuel'), Js('Yesochor'), Js('Aaron'), Js('Abarron'), Js('Abba'), Js('Abe'), Js('Abel'), Js('Abell'), Js('Abijah'), Js('Abimelech'), Js('Abir'), Js('Abiram'), Js('Abisha'), Js('Able'), Js('Abner'), Js('Abraham'), Js('Abram'), Js('Abramo'), Js('Absolom'), Js('Adam'), Js('Adar'), Js('Addai'), Js('Addam'), Js('Aden'), Js('Aderet'), Js('Adin'), Js('Adir'), Js('Adiv'), Js('Adlai'), Js('Adlai'), Js('Adley'), Js('Adli'), Js('Admon'), Js('Adniel'), Js('Adon'), Js('Adonai'), Js('Adriel'), Js('Adriyel'), Js('Ager'), Js('Ahab'), Js('Ahsalom'), Js('Aitan'), Js('Akiba'), Js('Akim'), Js('Akiva'), Js('Aksel'), Js('Akub'), Js('Alijah'), Js('Alim'), Js('Alivia'), Js('Alon'), Js('Alter'), Js('Alva'), Js('Alvah'), Js('Alvan'), Js('Amasa'), Js('Amichai'), Js('Amiel'), Js('Amikam'), Js('Amir'), Js('Amiram'), Js('Amita'), Js('Amiti'), Js('Ammi'), Js('Ammitai'), Js('Amnon'), Js('Amon'), Js('Amos'), Js('Amram'), Js('Aram'), Js('Ardon'), Js('Ari'), Js('Arie'), Js('Ariel'), Js('Arion'), Js('Arlan'), Js('Arland'), Js('Arlando'), Js('Arlen'), Js('Arlin'), Js('Armen'), Js('Armin'), Js('Armon'), Js('Arnan'), Js('Aron'), Js('Arvad'), Js('Arye'), Js('Aryeh'), Js('Asa'), Js('Asaf'), Js('Asaph'), Js('Asher'), Js('Ashur'), Js('Avi'), Js('Avichai'), Js('Avidan'), Js('Avidan'), Js('Avidor'), Js('Aviel'), Js('Avigdor'), Js('Avimelech'), Js('Avinoam'), Js('Aviram'), Js('Avisha'), Js('Avishai'), Js('Avital'), Js('Avner'), Js('Avniel'), Js('Avraham'), Js('Avsalom'), Js('Avshalom'), Js('Axel'), Js('Azaria'), Js('Azarious'), Js('Azaryah'), Js('Azaryahu'), Js('Azriel'), Js('Bama'), Js('Barak'), Js('Baram'), Js('Barnabas'), Js('Barnabe'), Js('Barnaby'), Js('Baron'), Js('Barrak'), Js('Bart'), Js('Bartel'), Js('Barth'), Js('Bartholomew'), Js('Bartley'), Js('Baruch'), Js('Bela'), Js('Ben'), Js('Benedictson'), Js('Beniamino'), Js('Benjamin'), Js('Benjy'), Js('Benkamin'), Js('Benny'), Js('Benoni'), Js('Benroy'), Js('Benson'), Js('Benson'), Js('Benzion'), Js('Berakhiah'), Js('Betzalel'), Js('Binah'), Js('Binyamin'), Js('Boas'), Js('Boaz'), Js('Bogdan'), Js('Bohdan'), Js('Cain'), Js('Cale'), Js('Caleb'), Js('Carmel'), Js('Carmelo'), Js('Carmi'), Js('Carmine'), Js('Chagai'), Js('Chaim'), Js('Chanan'), Js('Chanoch'), Js('Chaviv'), Js('Chavivi'), Js('Chayim'), Js('Che'), Js('Chepe'), Js('Chiram'), Js('Choni'), Js('Dabi'), Js('Dagan'), Js('Dagon'), Js('Dalit'), Js('Dan'), Js('Dane'), Js('Danel'), Js('Danell'), Js('Dani'), Js('Daniel'), Js('Daniele'), Js('Danil'), Js('Danila'), Js('Dann'), Js('Dannie'), Js('Dannon'), Js('Danny'), Js('Dantrell'), Js('Danyl'), Js('Dar'), Js('Dave'), Js('Davi'), Js('David'), Js('Davin'), Js('Deen'), Js('Deron'), Js('Dor'), Js('Doren'), Js('Dov'), Js('Dovev'), Js('Eban'), Js('Eben'), Js('Ebenezer'), Js('Eder'), Js('Efraim'), Js(' Efran'), Js('Efrat'), Js('Efrayim'), Js('Efrem'), Js('Efren'), Js('Efron'), Js('EIlis'), Js('Eitan'), Js('Elam'), Js('Elan'), Js('Elazar'), Js('Elazaro'), Js('Eleazar'), Js('Elhanan'), Js('Eli'), Js('Elias'), Js('Eliezer'), Js('Elihu'), Js('Elijah'), Js('Eliot'), Js('Eliseo'), Js('Elishama'), Js('Elisheba'), Js('Elisheva'), Js('Eljah'), Js('Elkanah'), Js('Elliott'), Js('Elrad'), Js('Ely'), Js('Emanuel'), Js('Emmanuel'), Js('Enoch'), Js('Ephram'), Js('Ephrem'), Js('Ephron'), Js('Eran'), Js('Eri'), Js('Eron'), Js('Errapel'), Js('Esau'), Js('Esdras'), Js('Eshkol'), Js('Esra'), Js('Etan'), Js('Ethan'), Js('Evelyn'), Js('Eyal'), Js('Eyou'), Js('Ezechiel'), Js('Ezekiel'), Js('Ezra'), Js('Ezrah'), Js('Feivel'), Js('Foma'), Js('Gabai'), Js('Gabe'), Js('Gabi'), Js('Gabor'), Js('Gabrian'), Js('Gabriel'), Js('Gabriele'), Js('Gabrielo'), Js('Gal'), Js('Gali'), Js('Gamaliel'), Js('Ganit'), Js('Gavi'), Js('Gavriel'), Js('Gedaliah'), Js('Gedalya'), Js('Gedalyahu'), Js('Gedeon'), Js('Geremia'), Js('Gersham'), Js('Gershom'), Js('Giacomo'), Js('Gian'), Js('Giannes'), Js('Gideon'), Js('Gil'), Js('Gilead'), Js('Gili'), Js('Gilli'), Js('Gilon'), Js('Giovanni'), Js('Gur'), Js('Guri'), Js('Gurion'), Js('Guy'), Js('Habib'), Js('Hadar'), Js('Ham'), Js('Hanan'), Js('Hannibal'), Js('Harel'), Js('Harmon'), Js('Harrell'), Js('Harrod'), Js('Hayyim'), Js('Heber'), Js('Heman'), Js('Herschel'), Js('Hershel'), Js('Hezekiah'), Js('Hieremias'), Js('Hiram'), Js('Hod'), Js('Honi'), Js('Hosea'), Js('Hyman'), Js('Iakovos'), Js('Ian'), Js('Iaokim'), Js('Ichabod'), Js('Ike'), Js('Ilias'), Js('Illias'), Js('Imanol'), Js('Ioan'), Js('Ionnes'), Js('Iosep'), Js('Ioseph'), Js('Iov'), Js('Ira'), Js('Iram'), Js('Isaac'), Js('Isaakios'), Js('Isaiah'), Js('Isaias'), Js('Iseabail'), Js('Ishmael'), Js('Isiah'), Js('Ismael'), Js('Ismail'), Js('Israel'), Js('Isreal'), Js('Itai'), Js('Ittamar'), Js('Ivrit'), Js('Ixaka'), Js('Izaak'), Js('Izreal'), Js('Izzy'), Js('Jaap'), Js('Jabin'), Js('Jacan'), Js('Jack'), Js('Jacob'), Js('Jacob'), Js('Jacobe'), Js('Jacot'), Js('Jaden'), Js('Jader'), Js('Jadon'), Js('Jaedon'), Js('Jael'), Js('Jaira'), Js('Jairus'), Js('Jake'), Js('Jakeem'), Js('Jakome'), Js('James'), Js('Jamian'), Js('Jamie'), Js('Jamiel'), Js('Jamin'), Js('Jamon'), Js('Jan'), Js('Jancsi'), Js('Jani'), Js('Janie'), Js('Jankia'), Js('Janko'), Js('Jannes'), Js('Janos'), Js('Jantje'), Js('Japhet'), Js('Japheth'), Js('Jaques'), Js('Jarah'), Js('Jared'), Js('Jariath'), Js('Jaron'), Js('Jarrett'), Js('Jasper'), Js('Javan'), Js('Javen'), Js('Jaydon'), Js('Jaymin'), Js('Jeb'), Js('Jebediah'), Js('Jed'), Js('Jedadiah'), Js('Jedaiah'), Js('Jedd'), Js('Jedediah'), Js('Jedi'), Js('Jediah'), Js('Jedidiah'), Js('Jehoichin'), Js('Jehu'), Js('Jem'), Js(' Jenda'), Js('Jephtah'), Js('Jerad'), Js('Jerah'), Js('Jered'), Js('Jeremi'), Js('Jeremiah'), Js('Jeremias'), Js('Jeremie'), Js('Jeremy'), Js('Jeriah'), Js('Jerod'), Js('Jerrah'), Js('Jerrick'), Js('Jerrod'), Js('Jesiah'), Js('Jess'), Js('Jesse'), Js('Jessey'), Js('Jessie'), Js('Jessy'), Js('Jesus'), Js('Jethro'), Js('Jim'), Js('Jimmy'), Js('Joachim'), Js('Job'), Js('Jobe'), Js('Joby'), Js('Jocheved'), Js('Jock'), Js('Joe'), Js('Joed'), Js('Joel'), Js('Joen'), Js('Joey'), Js('Johan'), Js('John'), Js('Johnathan'), Js('Johnathon'), Js('Johnny'), Js('Jokin'), Js('Jomar'), Js('Jon'), Js('Jonah'), Js('Jonam'), Js('Jonas'), Js('Jonatan'), Js('Jonathan'), Js('Jonathon'), Js('Jonny'), Js('Joop'), Js('Joosef'), Js('Jopie'), Js('Jorah'), Js('Joram'), Js('Jordain'), Js('Jordan'), Js('Jordell'), Js('Jordi'), Js('Jordy'), Js('Jore'), Js('Jori'), Js('Jorie'), Js('Jorim'), Js('Jory'), Js('Joseba'), Js('Josef'), Js('Joseph'), Js('Josephus'), Js('Josh'), Js('Joshua'), Js('Joshwa'), Js('Josiah'), Js('Josias'), Js('Joss'), Js('Josu'), Js('Josue'), Js('Jotham'), Js('Jourdaine'), Js('Jourdon'), Js('Jov'), Js('Joziah'), Js('Jubal'), Js('Jubal'), Js('Jud'), Js('Jud'), Js('Judah'), Js('Judas'), Js('Judd'), Js('Jude'), Js('Juha'), Js('Jukka'), Js('Junien'), Js('Jurre'), Js('Jussi'), Js('Kalb'), Js('Kaleb'), Js('Kaniel'), Js('Karmel'), Js('Kedem'), Js('Kenaz'), Js('Kobe'), Js('Kuper'), Js('Laban'), Js('Lapidos'), Js('Lapidoth'), Js('Lavan'), Js('Lazar'), Js('Lazarus'), Js('Lazzaro'), Js('Leb'), Js('Lemuel'), Js('Lev'), Js('Levey'), Js('Levi'), Js('Lewi'), Js('Lot'), Js('Machau'), Js('Machum'), Js('Mads'), Js('Mai'), Js('Maichail'), Js('Makis'), Js('Mal'), Js('Malachi'), Js('Malachy'), Js('Manasses'), Js('Manuel'), Js('Marnin'), Js('Matai'), Js('Mate'), Js('Mathe'), Js('Mathew'), Js('Mathews'), Js('Matt'), Js('Matthew'), Js('Matthias'), Js('Matthieu'), Js('Mattias'), Js('Matyas'), Js('Matz'), Js('Mayir'), Js('Meilseoir'), Js('Meir'), Js('Melchoir'), Js('Menachem'), Js('Menassah'), Js('Mendel'), Js('Meyer'), Js('Micah'), Js('Michael'), Js('Michel'), Js('Michon'), Js('Mihaly'), Js('Mika'), Js('Mikael'), Js('Mike'), Js('Mikel'), Js('Mikhail'), Js('Mikhalis'), Js('Mikhos'), Js('Mikkel'), Js('Miron'), Js('Misi'), Js('Miska'), Js('Mitchell'), Js('Moeshe'), Js('Mordecai'), Js('Mordechai'), Js('Moses'), Js('Moshe'), Js('Mosheh'), Js('Myron'), Js('Naaman'), Js('Nachman'), Js('Nadav'), Js('Nadiv'), Js('Naftali'), Js('Naftalie'), Js('Nahum'), Js('Nat'), Js('Natanael'), Js('Nate'), Js('Nathan'), Js('Nathanael'), Js('Nathanial'), Js('Nathaniel'), Js('Nechemya'), Js('Nehemiah'), Js('Nethanel'), Js('Nimrod'), Js('Nissim'), Js('Noach'), Js('Noah'), Js('Noam'), Js('Noe'), Js('Nuri'), Js('Obediah'), Js('Oded'), Js('Ofer'), Js('Omar'), Js(' Omeet'), Js('Omet'), Js('Omri'), Js('Oren'), Js('Ori'), Js('Orin'), Js('Oris'), Js('Ornice'), Js('Osip'), Js('Ovadiah'), Js('Ovadya'), Js('Oved'), Js('Ovid'), Js('Ozi'), Js('Ozzi'), Js('Ozzie'), Js('Paltel'), Js('Palti'), Js('Paz'), Js('Pesach'), Js('Pessach'), Js('Phineas'), Js('Raanan'), Js('Radwan'), Js('Rafael'), Js('Rafal'), Js('Rafe'), Js('Ranen'), Js('Rani'), Js('Ranit'), Js('Ranon'), Js('Raphael'), Js('Ravid'), Js('Rechavia'), Js('Reuben'), Js('Reuhen'), Js('Ron'), Js('Roni'), Js('Rouvin'), Js("R'phael"), Js('Ruben'), Js('Rueban'), Js('Saadya'), Js('Sakeri'), Js('Salamon'), Js('Samoel'), Js('Sampson'), Js('Samson'), Js('Samuel'), Js('Sanson'), Js('Sasson'), Js('Saul'), Js('Schmaiah'), Js('Schmuel'), Js('Seanan'), Js('Senen'), Js('Seosamh'), Js('Seosaph'), Js('Serafim'), Js('Serafin'), Js('Seraphim'), Js('Set'), Js('Seth'), Js('Shaan'), Js('Shadrach'), Js('Shane'), Js('Shelomo'), Js('Shem'), Js('Shet'), Js('Shilo'), Js('Shiloh'), Js('Shimshon'), Js('Shlomo'), Js('Shubha'), Js('Simao'), Js('Simcha'), Js('Simen'), Js('Simeon'), Js('Simon'), Js('Simson'), Js('Sinai'), Js('Sinon'), Js('Siomon'), Js('Sivan'), Js('Sol'), Js('Solomon'), Js('Symeon'), Js('Taaveti'), Js('Taavi'), Js('Tab'), Js('Tabor'), Js('Talmai'), Js('Tamas'), Js('Taneli'), Js('Tapani'), Js('Teppo'), Js('Thaddeus'), Js('Thoma'), Js('Thomas'), Js('Tobiah'), Js('Tobias'), Js('Tobin'), Js('Tohy'), Js('Tomas'), Js('Tomek'), Js('Tovi'), Js('Tsidhqiyah'), Js('Tutyahu'), Js('Tuvya'), Js('Tuvya'), Js('Tzadok'), Js('Tzefanyah'), Js('Tzefanyahu'), Js('Tzion'), Js('Tziyon'), Js('Tzuriel'), Js('Tzvi'), Js('Uri'), Js('Uriah'), Js('Uriel'), Js('Uzziah'), Js('Uzziel'), Js('Vaschel'), Js('Venamin'), Js('Veniamin'), Js('Venjamin'), Js('Ximen'), Js('Ximon'), Js('Ximun'), Js('Yaakov'), Js('Yadid'), Js('Yagil'), Js('Yago'), Js('Yair'), Js('Yakov'), Js('Yanis'), Js('Yannis'), Js('Yaphet'), Js('Yardane'), Js('Yarema'), Js('Yaremka'), Js('Yaron'), Js('Yavin'), Js('Yedidiah'), Js('Yedidyah'), Js('Yeeshai'), Js('Yehoash'), Js('Yehonadov'), Js('Yehoshua'), Js('Yehuda'), Js('Yehudah'), Js('Yehudi'), Js('Yerachmiel'), Js('Yered'), Js('Yerik'), Js('Yerucham'), Js('Yeshaya'), Js('Yiftach'), Js('Yigil'), Js('Yigol'), Js('Yisreal'), Js('Yissachar'), Js('Yitro'), Js('Yitzchak'), Js('Yoel'), Js('Yonah'), Js('Yosef'), Js('Yosefu'), Js('Yusef'), Js('Yuval'), Js('Zacchaeus'), Js('Zach'), Js('Zachaios'), Js('Zachariah'), Js('Zacharias'), Js('Zachary'), Js('Zachely'), Js('Zack'), Js('Zadok'), Js('Zalman'), Js('Zamir'), Js('Zan'), Js('Zane'), Js('Zani'), Js('Zarad'), Js('Zared'), Js('Zavad'), Js('Zayit'), Js('Zebediah'), Js('Zebulon'), Js('Zebulun'), Js('Zechariah'), Js('Zed'), Js('Zedekiah'), Js('Zeke'), Js('Zephan'), Js('Zephaniah'), Js('Zevulun'), Js('Zimra'), Js('Ziv'), Js('Zohar'), Js('Zubin'), Js('Zuriel')]))
var.put('nm2', Js([Js('Chaya'), Js('Baila'), Js('Chava'), Js('Shira'), Js('Leah'), Js('Shifra'), Js('Meira'), Js('Hadassah'), Js('Chedva'), Js('Aviva'), Js('Rochel'), Js('Rivkah'), Js('Sara'), Js('Nechama'), Js('Elisheva'), Js('Avigayil'), Js('Bluma'), Js('Shoshana'), Js('Miriam'), Js('Adina'), Js('Deena'), Js('Abigail'), Js('Abirit'), Js('Ada'), Js('Adar'), Js('Adi'), Js('Adina'), Js('Adiva'), Js('Adva'), Js('Agam'), Js('Agamit'), Js('Ahava'), Js('Ahuda'), Js('Ahuva'), Js('Alice'), Js('Alina'), Js('Aliza'), Js('Alma'), Js('Alona'), Js('Alonit'), Js('Aluma'), Js('Alumit'), Js('Amalia'), Js('Amira'), Js('Anat'), Js('Anna'), Js('Ariel'), Js('Ariela'), Js('Ariella'), Js('Ateret'), Js('Aviah'), Js('Aviam'), Js('Aviel'), Js('Aviella'), Js('Avigail'), Js('Avior'), Js('Avital'), Js('Aviv'), Js('Aviva'), Js('Avivit'), Js('Aya'), Js('Ayala'), Js('Ayelet'), Js('Bat Sheva'), Js('Bat-Chen'), Js('Batel'), Js('Batya'), Js('Bina'), Js('Bracha'), Js('Bruria'), Js('Carmel'), Js('Carmela'), Js('Carmit'), Js('Chagit'), Js('Chamutal'), Js('Chanit'), Js('Chasidah'), Js('Chava'), Js('Chavatzelet'), Js('Chaviva'), Js('Chaya'), Js('Chedva'), Js('Cheli'), Js('Chemda'), Js('Chofit'), Js('Cochava'), Js('Dafna'), Js('Dalia'), Js('Dalit'), Js('Dana'), Js('Daniel'), Js('Daniela'), Js('Daniella'), Js('Danit'), Js('Daria'), Js('Dasha'), Js('Dganit'), Js('Diana'), Js('Dikla'), Js('Dina'), Js('Dlila'), Js('Dora'), Js('Dorin'), Js('Dorit'), Js('Drora'), Js('Drorit'), Js('Dvorah'), Js('Eden'), Js('Edna'), Js('Efrat'), Js('Eina'), Js('Einat'), Js('Einav'), Js('Ela'), Js('Eliana'), Js('Elinor'), Js('Eliora'), Js('Elisheva'), Js('Eliza'), Js('Elizabeth'), Js('Ella'), Js('Elmaz'), Js('Emily'), Js('Emma'), Js('Emuna'), Js('Estee'), Js('Esther'), Js('Etti'), Js('Eva'), Js('Fanni'), Js('Fanya'), Js('Frida'), Js('Fruma'), Js('Gabi'), Js('Gabriel'), Js('Gabriela'), Js('Gal'), Js('Gali'), Js('Galia'), Js('Galila'), Js('Galina'), Js('Galit'), Js('Ganit'), Js('Gavriel'), Js('Gaya'), Js('Gazit'), Js('Gefen'), Js('Geula'), Js('Gil'), Js('Gili'), Js('Gilla'), Js('Gillat'), Js('Golda'), Js('Gurit'), Js('Hadar'), Js('Hadas'), Js('Hadasa'), Js('Hannah'), Js('Hela'), Js('Hila'), Js('Hilla'), Js('Hodaya'), Js('Idit'), Js('Ilana'), Js('Ilanit'), Js('Inbal'), Js('Inbar'), Js('Inna'), Js('Irena'), Js('Irina'), Js('Iris'), Js('Irit'), Js('Isabel'), Js('Israela'), Js('Izabella'), Js('Kalanit'), Js('Karin'), Js('Karina'), Js('Karmelita'), Js('Karmia'), Js('Karmina'), Js('Karmit'), Js('Keren'), Js('Kineret'), Js('Larissa'), Js('Laura'), Js('Lea'), Js('Lee'), Js('Lee-El'), Js('Levana'), Js('Levia'), Js('Lia'), Js('Liat'), Js('Lihi'), Js('Lilach'), Js('Lilit'), Js('Lily'), Js('Limor'), Js('Lin'), Js('Linor'), Js('Linoy'), Js('Lior'), Js('Liora'), Js('Lital'), Js('Livnat'), Js('Liza'), Js('Mai'), Js('Mali'), Js('Malka'), Js('Margalit'), Js('Maria'), Js('Mariana'), Js('Marina'), Js('Mary'), Js('Masha'), Js('Maya'), Js('Mazal'), Js('Mazal-Tov'), Js('Meira'), Js('Meirav'), Js('Meital'), Js('Michaela'), Js('Michal'), Js('Mika'), Js('Miki'), Js('Mira'), Js('Miri'), Js('Miriam'), Js('Mirit'), Js('Miryam'), Js("Na'ama"), Js("Na'omi"), Js('Natali'), Js('Natalia'), Js('Nava'), Js('Nechama'), Js('Nelly'), Js('Neora'), Js('Neta'), Js('Netali'), Js('Nicol'), Js('Nili'), Js('Nira'), Js('Nirit'), Js('Nitzan'), Js('Nitzana'), Js('Nitzanit'), Js('Noa'), Js('Noga'), Js('Noy'), Js('Noya'), Js('Nurit'), Js('Odaya'), Js('Odelia'), Js('Ofek'), Js('Ofir'), Js('Ofira'), Js('Ofra'), Js('Opal'), Js('Or'), Js('Orah'), Js('Oranit'), Js('Orian'), Js('Orit'), Js('Orli'), Js('Orna'), Js('Ortal'), Js('Oshra'), Js('Oshrat'), Js('Oshrit'), Js('Osnat'), Js('Paz'), Js('Pazit'), Js('Perla'), Js('Pnina'), Js("Ra'aya"), Js('Rachel'), Js('Racheli'), Js('Rakefet'), Js('Ravit'), Js('Rebecca'), Js('Reuya'), Js('Revital'), Js('Riki'), Js('Rina'), Js('Rinat'), Js('Rita'), Js('Riva'), Js('Rivka'), Js('Rona'), Js('Roni'), Js('Ronit'), Js('Roza'), Js('Ruchama'), Js('Ruma'), Js('Rut'), Js('Rutti'), Js('Sagit'), Js('Sara'), Js('Sarit'), Js('Sgula'), Js('Shakked'), Js('Sharon'), Js('Sharona'), Js('Shelly'), Js('Sherry'), Js('Shifra'), Js('Shimrit'), Js('Shir'), Js('Shira'), Js('Shirel'), Js('Shiri'), Js('Shirit'), Js('Shirli'), Js('Shlomit'), Js('Shoshana'), Js('Shoshi'), Js('Shoval'), Js('Shula'), Js('Shulamit'), Js('Shuli'), Js('Sigal'), Js('Sigalit'), Js('Simona'), Js('Smadar'), Js('Sofia'), Js('Sonia'), Js('Stav'), Js('Stella'), Js("T'chiya"), Js('Tal'), Js('Tali'), Js('Talia'), Js('Talma'), Js('Talya'), Js('Tamar'), Js('Tamara'), Js('Tammi'), Js('Tania'), Js('Tatiana'), Js('Tehila'), Js('Tikva'), Js('Tina'), Js('Tova'), Js('Tzilla'), Js('Tziona'), Js('Tzippi'), Js('Tzippora'), Js('Tzofia'), Js('Tzofit'), Js('Tzuf'), Js('Tzufit'), Js('Tzvia'), Js('Varda'), Js('Vardit'), Js('Vered'), Js('Veronica'), Js('Victoria'), Js("Ya'ara"), Js("Ya'arit"), Js("Ya'el"), Js("Ya'ela"), Js('Yafa'), Js('Yafit'), Js('Yahel'), Js('Yam'), Js('Yamit'), Js('Yana'), Js('Yanina'), Js('Yarden'), Js('Yardena'), Js('Yasmin'), Js('Yehudit'), Js('Yifat'), Js('Yocheved'), Js('Yona'), Js('Yonat'), Js('Yonit'), Js('Yulia'), Js('Zahava'), Js('Zehava'), Js('Zehavit'), Js('Zimra'), Js('Ziva'), Js('Zmira'), Js('Zohara'), Js('Zoheret')]))
var.put('nm3', Js([Js('Abraham'), Js('Abrams'), Js('Abramsky'), Js('Abramson'), Js('Adler'), Js('Aharoni'), Js('Aidallbery'), Js('Almog'), Js('Alter'), Js('Altman'), Js('Altmann'), Js('Angel'), Js('Apfel'), Js('Argov'), Js('Aronsfeld'), Js('Aronthal'), Js('Ascher'), Js('Asher'), Js('Auerbach'), Js('Bach'), Js('Backer'), Js('Baeck'), Js('Bakstansky'), Js('Baline'), Js('Ballin'), Js('Balsam'), Js('Bamberger'), Js('Barak'), Js('Barak'), Js('Barnato'), Js('Basch'), Js('Bash'), Js('Bashevis'), Js('Basin'), Js('Baskin'), Js('Baum'), Js('Baumberger'), Js('Bayme'), Js('Beck'), Js('Becker'), Js('Beer'), Js('Beit'), Js('Ben'), Js('Ben-Shahar'), Js('Benisch'), Js('Benski'), Js('Berkovic'), Js('Berlin'), Js('Berlinger'), Js('Bettman'), Js('Bezalel'), Js('Blomstein'), Js('Bloom'), Js('Blum'), Js('Blumenfeld'), Js('Bomberg'), Js('Borach'), Js('Braff'), Js('Brann'), Js('Brasch'), Js('Brenner'), Js('Breuer'), Js('Brodetsky'), Js('Bruck'), Js('Buchler'), Js('Cantor'), Js('Cassel'), Js('Chagall'), Js('Chertok'), Js('Chicherin'), Js('Cohen'), Js('Cohen'), Js('Cowen'), Js('Daiches'), Js('Danielovitch'), Js('Datz'), Js('Davidson'), Js('Dayan'), Js('Demsky'), Js('Deronda'), Js('Deutsch'), Js('Diamond'), Js('Dienesman'), Js('Dobias'), Js('Dresner'), Js('Dreyfuss'), Js('Duchan'), Js('Duchen'), Js('Duchin'), Js('Dukes'), Js('Duzy'), Js('Eban'), Js('Ehrenburg'), Js('Einhorn'), Js('Einstein'), Js('Eisen'), Js('Eisner'), Js('Emanuel'), Js('Endelman'), Js('Epstein'), Js('Erlich'), Js('Eshel'), Js('Eshkol'), Js('Farber'), Js('Federman'), Js('Feinstein'), Js('Feldshuh'), Js('Fersht'), Js('Fiedler'), Js('Filipowski'), Js('Finestein'), Js('Fishman'), Js('Fleischer'), Js('Fleischmann'), Js('Fraenkel'), Js('Frank'), Js('Frankau'), Js('Frankel'), Js('Frankfurter'), Js('Franklin'), Js('Friedlander'), Js('Friedman'), Js('Gadi'), Js('Ganani'), Js('Garbacz'), Js('Garfinkle'), Js('Gartner'), Js('Gaster'), Js('Geiger'), Js('Gerber'), Js('Gerlis'), Js('Gertler'), Js('Gestetner'), Js('Ginsberg'), Js('Gluckstein'), Js('Golan'), Js('Gold'), Js('Goldberg'), Js('Goldberg'), Js('Goldbloom'), Js('Goldman'), Js('Goldschmidt'), Js('Goldsmid'), Js('Golembo'), Js('Gollancz'), Js('Goni'), Js('Goodman'), Js('Gottesdiener'), Js('Gottesman'), Js('Gould'), Js('Goulston'), Js('Graetz'), Js('Grajek'), Js('Greenberg'), Js('Gretz'), Js('Grois'), Js('Gross'), Js('Grossman'), Js('Grossman'), Js('Grunwald'), Js('Gryn'), Js('Haber'), Js('Hadar'), Js('Halevi'), Js('Halevy'), Js('Hamutal'), Js('Har-Zahav'), Js('Harel'), Js('Harpaz'), Js('Hart'), Js('Hartog'), Js('Hefetz'), Js('Heilbron'), Js('Helfgott'), Js('Henriques'), Js('Hershon'), Js('Herzl'), Js('Hillman'), Js('Hirschell'), Js('Hirst'), Js('Hodesmann'), Js('Homa'), Js('Horovitz'), Js('Horowitz'), Js('Hurwitz'), Js('Hyamson'), Js('Isaac'), Js('Isaacs'), Js('Isaacson'), Js('Isaaman'), Js('Ish-Shalom'), Js('Iskowitch'), Js('Itzik'), Js('Jacob'), Js('Jacobovits'), Js('Jacobowitz'), Js('Jacobs'), Js('Jacobsen'), Js('Jacobson'), Js('Jakubowicz'), Js('Janner'), Js('Jerayesh'), Js('Jessel'), Js('Josephs'), Js('Jung'), Js('Kabotinsky'), Js('Kadish'), Js('Kafni'), Js('Kagan'), Js('Kahan'), Js('Kahn'), Js('Kalish'), Js('Kandelcukier'), Js('Kantor'), Js('Kantor'), Js('Kantorowitsch'), Js('Kaplan'), Js('Katz'), Js('Kedar'), Js('Kempinski'), Js('Kershen'), Js('Kobler'), Js('Kohnstamm'), Js('Kollek'), Js('Kosmin'), Js('Kostiner'), Js('Kramer'), Js('Kraushaar'), Js('Krausz'), Js('Krickstein'), Js('Kupner'), Js('Kuttab'), Js('Kolmel'), Js('Lachman'), Js('Lahrheim'), Js('Landau'), Js('Landeshut'), Js('Lasker'), Js('Laski'), Js('Latchman'), Js('Lawson'), Js('Lebzelter'), Js('Lehmann'), Js('Lehrer'), Js('Lerner'), Js('Levenberg'), Js('Leverson'), Js('Levi'), Js('Levin'), Js('Levine'), Js('Levinsky'), Js('Levinson'), Js('Levinstein'), Js('Levitansky'), Js('Levitch'), Js('Levitsky'), Js('Levitt'), Js('Levy'), Js('Liberman'), Js('Lichtman'), Js('Lieberman'), Js('Liebermann'), Js('Lipman'), Js('Liss'), Js('Littauer'), Js('Litvinov'), Js('Livshin'), Js('Loewe'), Js('Lotner'), Js('Luxemburg'), Js('Lyons'), Js('Lowy'), Js('Maccoby'), Js('Machuv'), Js('Malbim'), Js('Mandebaum'), Js('Manis'), Js('Manischewitz'), Js('Mankowitz'), Js('Mannes'), Js('Margolin'), Js('Margolis'), Js('Marks'), Js('Mattuck'), Js('Matusevitch'), Js('Matz'), Js('Maxse'), Js('Mayer'), Js('Mazar'), Js('Meir'), Js('Meir'), Js('Meldola'), Js('Mendel'), Js('Mendelson'), Js('Mendenhall'), Js('Meninsky'), Js('Merton'), Js('Metz'), Js('Mocatta'), Js('Mohilewer'), Js('Monash'), Js('Mond'), Js('Montagu'), Js('Montefiore'), Js('Morgenthau'), Js('Moses'), Js('Mowshowitch'), Js('Munk'), Js('Myer'), Js('Myers'), Js('Nachum'), Js('Nenbauer'), Js('Neuberger'), Js('Neumegen'), Js('Novokovichi'), Js('Oded'), Js('Okin'), Js('Okun'), Js('Ophir'), Js('Paliakov'), Js('Pazy'), Js('Pekarsky'), Js('Peres'), Js('Perlman'), Js('Persky'), Js('Pick'), Js('Pinero'), Js('Pinsker'), Js('Pinsky'), Js('Piratin'), Js('Pirbright'), Js('Poliakov'), Js('Pollack'), Js('Pomerantz'), Js('Posner'), Js('Poupko'), Js('Prag'), Js('Prais'), Js('Rabbinowitz'), Js('Rabin'), Js('Rabinowicz'), Js('Ran'), Js('Reinhartz'), Js('Reinharz'), Js('Reiss'), Js('Resnick'), Js('Reuben'), Js('Rivkin'), Js('Rocker'), Js('Romach'), Js('Rose'), Js('Rosen'), Js('Rosenbaum'), Js('Rosenberg'), Js('Rosenberg'), Js('Rosenstein'), Js('Rosenthal'), Js('Roth'), Js('Rothenstein'), Js('Rothschild'), Js('Rothstein'), Js('Rubin'), Js('Rubinstein'), Js('Sachar'), Js('Sacher'), Js('Salbstein'), Js('Salomons'), Js('Saltman'), Js('Saltzmann'), Js('Samuel'), Js('Samuels'), Js('Sandler'), Js('Sarasohn'), Js('Sarkin'), Js('Sarlin'), Js('Sassoon'), Js('Sayar'), Js('Schach'), Js('Schalit'), Js('Schapiro'), Js('Schechter'), Js('Schecter'), Js('Schiff'), Js('Schiller'), Js('Schlesinger'), Js('Schmool'), Js('Schneider'), Js('Schonfeld'), Js('Schuster'), Js('Schwab'), Js('Sebag'), Js('Segal'), Js('Segal'), Js('Segalowitch'), Js('Semon'), Js('Shahar'), Js('Shalit'), Js('Shameel'), Js('Shapiro'), Js('Sharansky'), Js('Sharett'), Js('Sharot'), Js('Sherman'), Js('Shiloh'), Js('Shimoni'), Js('Shimshelewitz'), Js('Shine'), Js('Shkolnik'), Js('Shmerkin'), Js('Shoshan'), Js('Shub'), Js('Shulman'), Js('Sieff'), Js('Silberstein'), Js('Singer'), Js('Singer'), Js('Sklare'), Js('Smashnova'), Js('Sokolov'), Js('Somper'), Js('Spector'), Js('Speyer'), Js('Spiegel'), Js('Spiro'), Js('Spiro'), Js('Spitzer'), Js('Starkman'), Js('Stein'), Js('Steinberg'), Js('Steiner'), Js('Stephany'), Js('Stern'), Js('Sternberg'), Js('Stiebel'), Js('Straus'), Js('Susser'), Js('Sutro'), Js('Sylvester'), Js('Szinessy'), Js('Theodores'), Js('Trachtenberg'), Js('Trumpelder'), Js('Tschkenow'), Js('Twersky'), Js('Tzon'), Js('Uki'), Js('Ussishkin'), Js('Vinchevsky'), Js('Wakstok'), Js('Waley'), Js('Wallach'), Js('Wandsworth'), Js('Wassermann'), Js('Watterman'), Js('Weber'), Js('Wechsler'), Js('Weidenseld'), Js('Weil'), Js('Weizman'), Js('Weizmann'), Js('Wiener'), Js('Wiezman'), Js('Wigram'), Js('Wirth'), Js('Wolf'), Js('Wolmark'), Js('Woolf'), Js('Worms'), Js('Yadin'), Js('Yakobovitch'), Js('Yedidyah'), Js('Yoelsen'), Js('Yoffey'), Js('Zahavy'), Js('Zalkind'), Js('Zangwill'), Js('Zedner'), Js('Zeev'), Js('Zeiman'), Js('Zlato'), Js('Zoegell'), Js('Zundel')]))
pass
pass


# Add lib to the module scope
jewishNames = var.to_python()
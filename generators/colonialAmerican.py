__all__ = ['colonialAmerican']

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
    var.put('nm1', Js([Js('Abel'), Js('Abiel'), Js('Abijah'), Js('Abimael'), Js('Abner'), Js('Abraham'), Js('Absalom'), Js('Adonijah'), Js('Ajax'), Js('Alden'), Js('Amias'), Js('Amiel'), Js('Ammiras'), Js('Amos'), Js('Amzi'), Js('Ansel'), Js('Archibald'), Js('Asa'), Js('Asahel'), Js('Azariah'), Js('Balthasar'), Js('Barnabas'), Js('Bartholomew'), Js('Bazel'), Js('Benajah'), Js('Boaz'), Js('Chauncey'), Js('Christopher'), Js('Clement'), Js('Comfort'), Js('Constant'), Js('Cotton'), Js('Cyrus'), Js('Degory'), Js('Duncan'), Js('Ebenezer'), Js('Edward'), Js('Elbert'), Js('Eleazar'), Js('Eleazer'), Js('Eli'), Js('Eliab'), Js('Eliakim'), Js('Elias'), Js('Elihu'), Js('Elijah'), Js('Eliphalet'), Js('Elisha'), Js('Emanuel'), Js('Emory'), Js('Enoch'), Js('Enos'), Js('Ephraim'), Js('Experience'), Js('Ezekiel'), Js('Francis'), Js('Garvan'), Js('Gawen'), Js('Gerrard'), Js('Gideon\t'), Js('Gideon'), Js('Giles'), Js('Hannibal'), Js('Henry'), Js('Hercules'), Js('Hezekiah'), Js('Hiram'), Js('Holmes'), Js('Homer'), Js('Horatio'), Js('Hosea'), Js('Increase'), Js('Isaac'), Js('Isaiah'), Js('Isham'), Js('Israel'), Js('Jabez'), Js('James'), Js('Jared'), Js('Jasper'), Js('Jedidiah'), Js('Jehu'), Js('Jeremiah'), Js('Jethro'), Js('Job'), Js('John'), Js('Jonas'), Js('Josiah'), Js('Jothan'), Js('Kenelm'), Js('Lazarus'), Js('Lemuel'), Js('Levi'), Js('Linus'), Js('Love'), Js('Matthias'), Js('Micajah'), Js('Miles'), Js('Moses'), Js('Myles'), Js('Nehemiah'), Js('Noble'), Js('Obadiah'), Js('Oceanus'), Js('Philo'), Js('Philomon'), Js('Phineas'), Js('Prosperity'), Js('Reason'), Js('Resolved'), Js('Richard'), Js('Robert'), Js('Rufus'), Js('Salmon'), Js('Sampson'), Js('Samuel'), Js('Seth'), Js('Silas'), Js('Simon'), Js('Solomon'), Js('Thaddeus'), Js('Theophilus'), Js('Thomas'), Js('Truth'), Js('William'), Js('Wrestling'), Js('Zaccheus'), Js('Zachariah'), Js('Zadock'), Js('Zadok'), Js('Zebulon'), Js('Zephaniah'), Js('Zophar')]))
    var.put('nm2', Js([Js('Abigail'), Js('Abitha'), Js('Alice'), Js('Amity'), Js('Ann'), Js('Anne'), Js('Aphra'), Js('Aurinda'), Js('Azuba'), Js('Candace'), Js('Catherine'), Js('Charity'), Js('Charlotte'), Js('Chastity'), Js('Clarity'), Js('Comfort'), Js('Constance'), Js('Cornelia'), Js('Damarus'), Js('Deliverance'), Js('Desire'), Js('Dorcas'), Js('Dorothy'), Js('Edith'), Js('Eleanor'), Js('Electa'), Js('Eliza'), Js('Elizabeth'), Js('Ellen'), Js('Emeline'), Js('Ester'), Js('Esther'), Js('Experience'), Js('Fanny'), Js('Felicity'), Js('Fidelity'), Js('Georgine'), Js('Grace'), Js('Harriet'), Js('Hecuba'), Js('Helen'), Js('Henrietta'), Js('Hephzibah'), Js('Hepzibah'), Js('Hester'), Js('Humility'), Js('Increase'), Js('Isabella'), Js('Jane'), Js('Joan'), Js('Joy'), Js('Judith'), Js('Katherine'), Js('Keturah'), Js('Keziah'), Js('Lydia'), Js('Mahala'), Js('Martha'), Js('Mary'), Js('Mercy'), Js('Modesty'), Js('Patience'), Js('Phila'), Js('Phoebe'), Js('Piety'), Js('Primrose'), Js('Priscilla'), Js('Prosperity'), Js('Prudence'), Js('Reason'), Js('Rebekah'), Js('Remember'), Js('Rosanna'), Js('Rose'), Js('Sarah'), Js('Selah'), Js('Silence'), Js('Susanna'), Js('Tabitha'), Js('Temperance'), Js('Thankfull'), Js('Theodosia'), Js('Truth'), Js('Verity'), Js('Virginia'), Js('Zipporah')]))
    var.put('nm3', Js([Js('Adair'), Js('Adams'), Js('Aigar'), Js('Alexander'), Js('Allen'), Js('Alloways'), Js('Amos'), Js('Anderson'), Js('Andrews'), Js('Atkins'), Js('Attyte'), Js('Badders'), Js('Bailey'), Js('Baird'), Js('Barnard'), Js('Barnet'), Js('Barnett'), Js('Barton'), Js('Bean'), Js('Bennett'), Js('Best'), Js('Bohannon'), Js('Bohnanon'), Js('Bond'), Js('Bourne'), Js('Bowles'), Js('Boyd'), Js('Bradley'), Js('Bradshaw'), Js('Brady'), Js('Brannon'), Js('Brown'), Js('Buchannon'), Js('Caldwell'), Js('Camble'), Js('Carson'), Js('Chamberlain'), Js('Chambers'), Js('Channel'), Js('Clark'), Js('Clement'), Js('Clements'), Js('Collins'), Js('Cooper'), Js('Cord'), Js('Cornelius'), Js('Couzens'), Js('Cowan'), Js('Cowgil'), Js('Cowgill'), Js('Crawford'), Js('Cresswell'), Js('Criswel'), Js('Crockett'), Js('Cromey'), Js('Crummey'), Js('Cunningham'), Js('Curley'), Js('Davison'), Js('Dickson'), Js('Dinsmore'), Js('Dixon'), Js('Dodson'), Js('Donald'), Js('Donnell'), Js('Doran'), Js('Doras'), Js('Duncan'), Js('Dunlap'), Js('Eastburn'), Js('Eaton'), Js('Ebaugh'), Js('Edgar'), Js('Edmiston'), Js('Edmundson'), Js('Elder'), Js('Emenheiser'), Js('Emmitt'), Js('Erwin'), Js('Ewing'), Js('Fansant'), Js('Farr'), Js('Feit'), Js('Foster'), Js('Fulton'), Js('Galbraith'), Js('Gale'), Js('Gest'), Js('Gibson'), Js('Gillcrest'), Js('Glasgow'), Js('Gordon'), Js('Gorley'), Js('Graham'), Js('Graydon'), Js('Griffith'), Js('Grove'), Js('Growden'), Js('Hair'), Js('Hall'), Js('Hamilton'), Js('Hartman'), Js('Hawkins'), Js('Hershey'), Js('Hill'), Js('Hopkins'), Js('Hughey'), Js('Irwin'), Js('Jarret'), Js('Jarrett'), Js('John'), Js('Johnston'), Js('Jones'), Js('Jordan'), Js('Kenly'), Js('Kennard'), Js('Kersey'), Js('Kilgore'), Js('Kimble'), Js('Kincaid'), Js('Kinnard'), Js('Kirk'), Js('Kisiner'), Js('Lanius'), Js('Lawson'), Js('Leeper'), Js('Lewden'), Js('Ligget'), Js('Liggett'), Js('Liggit'), Js('Lineboro'), Js('Litten'), Js('Livingston'), Js('Lukey'), Js('Mackey'), Js('Major'), Js('Manifold'), Js('Mantle'), Js('Mare'), Js('Marlin'), Js('Martin'), Js('Mason'), Js('Matthews'), Js('McCalla'), Js('McCalmont'), Js('McCanless'), Js('McCaskey'), Js('McClelland'), Js('McClemont'), Js('McConnal'), Js('McConnel'), Js('McCord'), Js('McCourtney'), Js('McCoy'), Js('McCullough'), Js('McCurdy'), Js('McDaniel'), Js('McFadden'), Js('McGee'), Js('McMullen'), Js('McNamee'), Js('McPherson'), Js('Means'), Js('Mears'), Js('Miller'), Js('Milligen'), Js('Millikan'), Js('Milliken'), Js('Mitchell'), Js('Moffett'), Js('Montgomery'), Js('Morgan'), Js('Morris'), Js('Morrison '), Js('Munn'), Js('Murphy'), Js('Murray'), Js('Neiper'), Js('Nichol'), Js('Nichols'), Js('Nickle'), Js('Oâ€™Brian'), Js('Obrian'), Js('Oliver'), Js('Onion'), Js('Osborn'), Js('PERKINGS'), Js('Paine'), Js('Parker'), Js('Patterson'), Js('Payne'), Js('Pedan'), Js('Pennel'), Js('Perkins'), Js('Peters'), Js('Pickart'), Js('Pierson'), Js('Poole'), Js('Power'), Js('Price'), Js('Purdy'), Js('Pymer'), Js('Quigly'), Js('Ramsey'), Js('Redman'), Js('Reed'), Js('Richardson'), Js('Robinson'), Js('Rogers'), Js('Roland'), Js('Ross'), Js('Rouse'), Js('Rowan'), Js('Sample'), Js('Schotts'), Js('Scott'), Js('Scotts'), Js('Semple'), Js('Siddall'), Js('Sinclair'), Js('Sinkler'), Js('Smille'), Js('Smith'), Js('Snyder'), Js('Stalsworth'), Js('Stedman'), Js('Steel'), Js('Sterret'), Js('Sterrett'), Js('Stevenson'), Js('Stewart'), Js('Suitor'), Js('Switzer'), Js('Taggert'), Js('Taylor'), Js('Templeton'), Js('Thompson'), Js('Tomkin'), Js('Toule'), Js('Traverse'), Js('Vansant'), Js('Wallace'), Js('Watt'), Js('Webb'), Js('Wentz'), Js('West'), Js('White'), Js('Whiteford'), Js('Whitelock'), Js('Wiley'), Js('Williams'), Js('Williamson'), Js('Wilson'), Js('Wise'), Js('Woodbury')]))
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
colonialAmerican = var.to_python()
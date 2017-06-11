__all__ = ['teutonicNames']

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
    var.put('nm1', Js([Js('Adalard'), Js('Adolf'), Js('Aeilmar'), Js('Aelgar'), Js('Aelmar'), Js('Alberich'), Js('Albert'), Js('Albrecht'), Js('Ambrosius'), Js('Amery'), Js('Andreas'), Js('Anno'), Js('Anselm'), Js('Anthonius'), Js('Aric'), Js('Arnoldt'), Js('Augustin'), Js('Ayllmer'), Js('Aylmar'), Js('Baldewin'), Js('Balthazar'), Js('Bartholomeus'), Js('Bernhart'), Js('Bernt'), Js('Berthold'), Js('Bertram'), Js('Brainard'), Js('Bruno'), Js('Burchard'), Js('Caspar'), Js('Cavell'), Js('Cenred'), Js('Christian'), Js('Christof'), Js('Crosby'), Js('Curd'), Js('Dedrick'), Js('Dedrik'), Js('Dellwin'), Js('Delwyn'), Js('Dickson'), Js('Dietborg'), Js('Dieter'), Js('Dietleb'), Js('Dietmar'), Js('Dietrich'), Js('Dwijaraj'), Js('Eberhard'), Js('Eckart'), Js('Eckehart'), Js('Edolie'), Js('Egbart'), Js('Ehrhart'), Js('Eldon'), Js('Elgar'), Js('Ellard'), Js('Ellary'), Js('Elldrich'), Js('Ellgar'), Js('Elmar'), Js('Engelbrecht'), Js('Engelhard'), Js('Erasmus'), Js('Erwin'), Js('Ethmer'), Js('Eusebius'), Js('Friedrich'), Js('Fritjof'), Js('Fyodor'), Js('Gabriel'), Js('Garryk'), Js('Gebhard'), Js('Georg'), Js('Gerbert'), Js('Gerebert'), Js('Gerhard'), Js('Gernand'), Js('Getz'), Js('Gifford'), Js('Goswyn'), Js('Gottfried'), Js('Gotthard'), Js('Gottschalk'), Js('Gregor'), Js('Gumbrecht'), Js('Gunther'), Js('Hank'), Js('Hannus'), Js('Hans'), Js('Harm'), Js('Hartmann'), Js('Hartmut'), Js('Hartwig'), Js('Hasso'), Js('Heidenreich'), Js('Heinrich'), Js('Heintz'), Js('Helferich'), Js('Helmut'), Js('Henning'), Js('Herberto'), Js('Heribert'), Js('Herman'), Js('Hermann'), Js('Herolt'), Js('Hildebrand'), Js('Howard'), Js('Hoyer'), Js('Hugo'), Js('Jacob'), Js('Jens'), Js('Joachim'), Js('Jobst'), Js('Johann'), Js('Johannes'), Js('Jonas'), Js('Jorg'), Js('Karl'), Js('Kilian'), Js('Klaus'), Js('Kolman'), Js('Konrad'), Js('Kuno'), Js('Kunz'), Js('Leonhard'), Js('Leopold'), Js('Linhart'), Js('Lorencz'), Js('Lothar'), Js('Ludolf'), Js('Ludwig'), Js('Luitpold'), Js('Lukas'), Js('Lutold'), Js('Manfred'), Js('Mangold'), Js('Markus'), Js('Markward'), Js('Matthias'), Js('Maximilian'), Js('Medwin'), Js('Meinhard'), Js('Mertin'), Js('Michael'), Js('Nikolaus'), Js('Nirnay'), Js('Notker'), Js('Onnan'), Js('Ortwin'), Js('Osgood'), Js('Oswynn'), Js('Ota'), Js('Oto'), Js('Otomars'), Js('Otto'), Js('Packston'), Js('Paul'), Js('Peter'), Js('Petermann'), Js('Petrus'), Js('Philipp'), Js('Reimar'), Js('Reinhard'), Js('Reinhold'), Js('Remshel'), Js('Rendel'), Js('Richmond'), Js('Riechard'), Js('Robin'), Js('Ross'), Js('Rudeger'), Js('Rudolf'), Js('Ruprecht'), Js('Ryner'), Js('Ryngware'), Js('Sacharias'), Js('Sander'), Js('Sebastian'), Js('Segenand'), Js('Siedler'), Js('Siegfried'), Js('Sieghard'), Js('Sigismund'), Js('Stefan'), Js('Sweder'), Js('Symon'), Js('Syvand'), Js('Teoderich'), Js('Thomas'), Js('Til'), Js('Tilman'), Js('Tirell'), Js('Torbert'), Js('Ulrich'), Js('Veit'), Js('Vincenz'), Js('Vollprecht'), Js('Walther'), Js('Welf'), Js('Wendel'), Js('Wennemar'), Js('Wenzel'), Js('Werner'), Js('Wilhelm'), Js('Willekin'), Js('Winrich'), Js('Wolff'), Js('Wolfgang'), Js('Wolfhart'), Js('Wolfram'), Js('Wolter')]))
    var.put('nm2', Js([Js('Acelin'), Js('Ada'), Js('Adala'), Js('Adalheidis'), Js('Adelinda'), Js('Adelma'), Js('Ailna'), Js('Aldea'), Js('Alfonsa'), Js('Aloysia'), Js('Amahna'), Js('Amelinda'), Js('Athala'), Js('Auberta'), Js('Awatif'), Js('Baudilia'), Js('Belinda'), Js('Bertilda'), Js('Blanda'), Js('Braulia'), Js('Brunhild'), Js('Brunhilda'), Js('Carla'), Js('Carlen'), Js('Dalmira'), Js('Della'), Js('Edelmira'), Js('Edgarda'), Js('Edith'), Js('Edolina'), Js('Edwige'), Js('Edyta'), Js('Elberta'), Js('Elcira'), Js('Elfreda'), Js('Elfredda'), Js('Elfrida'), Js('Ellois'), Js('Elmena'), Js('Elmina'), Js('Emna'), Js('Ethmer'), Js('Etta'), Js('Farica'), Js('Fritjof'), Js('Geraldine'), Js('Gertrude'), Js('Gilen'), Js('Gundelina'), Js('Haldis'), Js('Hedwig'), Js('Heilwidis'), Js('Helewidis'), Js('Henka'), Js('Henriette'), Js('Hilda'), Js('Hildegard'), Js('Hildegarde'), Js('Ingrid'), Js('Isold'), Js('Kelly'), Js('Lulu'), Js('Magan'), Js('Minka'), Js('Nettie'), Js('Orinda'), Js('Rimilda'), Js('Rimilde'), Js('Rosalind'), Js('Tille'), Js('Verena'), Js('Walburga'), Js('Waltraud'), Js('Willa'), Js('Xiomara'), Js('Yvette')]))
    var.put('nm3', Js([Js('Albe'), Js('Becker'), Js('Beckow'), Js('Beheim'), Js('Bentim'), Js('Blankenberg'), Js('Bock'), Js('Borg'), Js('Brant'), Js('Bresch'), Js('Brunau'), Js('Buchsenmeister'), Js('Burhamer'), Js('Christiani'), Js('Clare'), Js('Cracht'), Js('Crampitcz'), Js('Dedekind'), Js('Dobeneck'), Js('Dusemer'), Js('Ebner'), Js('Echter'), Js('Eck'), Js('Engel'), Js('Erlach'), Js('Fischart'), Js('Flemyng'), Js('Folz'), Js('Freytag'), Js('Gans'), Js('Gattersleben'), Js('Geiler'), Js('Glasow'), Js('Glazenap'), Js('Hartfust'), Js('Haselbach'), Js('Hasenkamp'), Js('Hatenik'), Js('Heinke'), Js('Heydebreke'), Js('Hitvelt'), Js('Hold'), Js('Hubener'), Js('Hund'), Js('Jordan'), Js('Junge'), Js('Kaldenborn'), Js('Keseling'), Js('Kirskorbes'), Js('Knoffe'), Js('Knorre'), Js('Konig'), Js('Kreuder'), Js('Krouwel'), Js('Kuchmeister'), Js('Kuhschmalz'), Js('Kuwal'), Js('Lander'), Js('Langmann'), Js('Langes'), Js('Lepper'), Js('Leyskewange'), Js('Liechtenauer'), Js('Linke'), Js('Lohner'), Js('Lode'), Js('Mankebeke'), Js('Matzke'), Js('Merklin'), Js('Mewsing'), Js('Multscher'), Js('Munzmeister'), Js('Murner'), Js('Ockenghem'), Js('Nagel'), Js('Nothaft'), Js('Oberstolz'), Js('Ochmann'), Js('Pacher'), Js('Papstein'), Js('Pettickh'), Js('Pferdesdorf'), Js('Pilgrim'), Js('Pleydenwurff'), Js('Probst'), Js('Pruse'), Js('Puschmann'), Js('Quade'), Js('Rabensteyner'), Js('Recke'), Js('Reffle'), Js('Regnart'), Js('Rehwinkel'), Js('Reuss'), Js('Rieschach'), Js('Rigler'), Js('Ritter'), Js('Roder'), Js('Rogga'), Js('Rotenburg'), Js('Rulman'), Js('Runge'), Js('Ruperti'), Js('Ruppel'), Js('Rymann'), Js('Rymenhower'), Js('Sauer'), Js('Scharpenberg'), Js('Schabe'), Js('Schede'), Js('Schenk'), Js('Shenkendorf'), Js('Schindekopf'), Js('Schippen'), Js('Slesiger'), Js('Schliderer'), Js('Schlungel'), Js('Schoneck'), Js('Schonewelt'), Js('Schutte'), Js('Schreiner'), Js('Schurburg'), Js('Sefeler'), Js('Seuse'), Js('Slick'), Js('Spreng'), Js('Stadler'), Js('Stagel'), Js('Stangenwalt'), Js('Stegelitz'), Js('Steinhowel'), Js('Sterbeke'), Js('Stolpmann'), Js('Stolte'), Js('Stoss'), Js('Schutzbar'), Js('Suderman'), Js('Tanke'), Js('Tauler'), Js('ten Hove'), Js('Terrax'), Js('Tiergart'), Js('Tolke'), Js('Tork'), Js('Trunczman'), Js('Tyn'), Js('Uxkull'), Js('Vetter'), Js('Vinke'), Js('Volz'), Js('vom Felde'), Js('vom Thawer'), Js('vom Walde'), Js('vom Wege'), Js('von Ast'), Js('von Balk'), Js('von Baysen'), Js('von Borke'), Js('von Beffart'), Js('von Bodem'), Js('von Buk'), Js('von Burgeln'), Js('von Cleyn'), Js('von Dellwig'), Js('von Depenbroich'), Js('von Dewis'), Js('von Duden'), Js('von Elner'), Js('von Eltz'), Js('von Eyll'), Js('von Felben'), Js('von Feuchtwangen'), Js('von Fischenich'), Js('von Galen'), Js('von Gelstorp'), Js('von Hausen'), Js('von Hechenreyt'), Js('von Hirkin'), Js('von Kendenich'), Js('von Keppel'), Js('von Kerpen'), Js('von Ketze'), Js('von Ketteler'), Js('von Kittlitz'), Js('von Kinnitz'), Js('von Krixen'), Js('von Kottwitz'), Js('von Langen'), Js('von Lessen'), Js('von Manteufel'), Js('von Mewe'), Js('von Meylen'), Js('von Montebur'), Js('von Mossig'), Js('von Querfurt'), Js('von Orle'), Js('von Orseln'), Js('von Orsbecke'), Js('von Osterna '), Js('von Otleve'), Js('von Oushem'), Js('von Kellenyn'), Js('von Kreytz'), Js('von Pelland'), Js('von Polenszik'), Js('von Posteyn'), Js('von Radam'), Js('von Reve'), Js('von Roghiten'), Js('von Rusdorf '), Js('von Sagan'), Js('von Sayn'), Js('von Schlieben'), Js('von Sheebe'), Js('von Steffen'), Js('von Stein'), Js('von Streifen'), Js('von Sydow'), Js('von Swayne'), Js('von Tauer'), Js('von Tiefen'), Js('von Tunna'), Js('von Vechta'), Js('von Vischenyk'), Js('von Wedel'), Js('von Weida'), Js('von Werth'), Js('von Worbeke'), Js('von der Beke'), Js('von der Dube'), Js('von der Horst'), Js('von der Kemnate'), Js('von der Linde'), Js('von der Marwitcz'), Js('von der Weyse'), Js('Vochs'), Js('Wald'), Js('Walpot'), Js('Wargel'), Js('Warnemann'), Js('Weinmuth'), Js('Wegleben'), Js('Westfal'), Js('Wickram'), Js('Wilke'), Js('Windeck'), Js('Wittenwiler'), Js('Witz'), Js('Wolthus'), Js('Worm'), Js('Zedeler'), Js('Zenger'), Js('Zevelt'), Js('Zollner')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
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
teutonicNames = var.to_python()
__all__ = ['oldHighGerman']

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
var.put('nm1', Js([Js('Adalbero'), Js('Adelbrand'), Js('Adelgis'), Js('Adelhard'), Js('Adelhelm'), Js('Adolar'), Js('Adolf'), Js('Aimar'), Js('Alberich'), Js('Albert'), Js('Aldo'), Js('Alida'), Js('Alram'), Js('Altmann'), Js('Alwin'), Js('Anselm'), Js('Archibald'), Js('Aristeo'), Js('Arnfried'), Js('Arnold'), Js('Arnulf'), Js('Arwin'), Js('Aschwin'), Js('Askan'), Js('Astolfo'), Js('Baldwin'), Js('Bernard'), Js('Bernfried'), Js('Bernger'), Js('Bernward'), Js('Bert'), Js('Berthold'), Js('Bertrad'), Js('Bertram'), Js('Bertrand'), Js('Bodo'), Js('Bodobert'), Js('Bruno'), Js('Burkhard'), Js('Clodomiro'), Js('Conrad'), Js('Curt'), Js('Dagobert'), Js('Dankmar'), Js('Dankrad'), Js('Degenhard'), Js('Deion'), Js('Detlev'), Js('Dieter'), Js('Dietgard'), Js('Dietger'), Js('Diethard'), Js('Dietmar'), Js('Dietrich'), Js('Ebbo'), Js('Eckbert'), Js('Eckhard'), Js('Egmont'), Js('Egon'), Js('Eike'), Js('Elmer'), Js('Elric'), Js('Emmerich'), Js('Engelbert'), Js('Erfried'), Js('Erhard'), Js('Ernest'), Js('Erwin'), Js('Everard'), Js('Ewald'), Js('Falko'), Js('Farald'), Js('Filibert'), Js('Folke'), Js('Frank'), Js('Frederick'), Js('Friedbert'), Js('Friedger'), Js('Friedhelm'), Js('Friedwart'), Js('Friso'), Js('Günther'), Js('Gangolf'), Js('Gaston'), Js('Gebhard'), Js('Gerald'), Js('Gerard'), Js('Gerfried'), Js('Gerlach'), Js('Gernot'), Js('Gerolf'), Js('Gerwig'), Js('Gerwin'), Js('Gilbert'), Js('Giselher'), Js('Gismondo'), Js('Godfrey'), Js('Gonzalo'), Js('Goswin'), Js('Gotthard'), Js('Gottlieb'), Js('Gottschalk'), Js('Grimwald'), Js('Guerino'), Js('Guido'), Js('Gundolf'), Js('Guntbert'), Js('Gunthard'), Js('Guntram'), Js('Hadebrand'), Js('Hademar'), Js('Hagen'), Js('Harald'), Js('Hartbert'), Js('Hartmann'), Js('Hartmut'), Js('Hartwig'), Js('Hartwin'), Js('Hasso'), Js('Hatto'), Js('Heimo'), Js('Heimrad'), Js('Helferich'), Js('Helmer'), Js('Helmut'), Js('Henry'), Js('Herbert'), Js('Hermann'), Js('Herwig'), Js('Hildebrand'), Js('Hildemar'), Js('Hilger'), Js('Horst'), Js('Hubert'), Js('Hugo'), Js('Humbert'), Js('Hunfried'), Js('Ingbert'), Js('Ingmar'), Js('Ingo'), Js('Ingolf'), Js('Isebrand'), Js('Isenbert'), Js('Ivo'), Js('Kai'), Js('Karl'), Js('Kléber'), Js('Korbinian'), Js('Kraft'), Js('Kunibald'), Js('Kunibert'), Js('Kuno'), Js('Lambert'), Js('Lando'), Js('Landolf'), Js('Landrich'), Js('Lanfrank'), Js('Laurin'), Js('Leonhard'), Js('Leopold'), Js('Liebhard'), Js('Liebwin'), Js('Lothar'), Js('Lubin'), Js('Ludger'), Js('Ludolf'), Js('Ludwig'), Js('Luitwin'), Js('Luther'), Js('Major'), Js('Malte'), Js('Manegold'), Js('Manfred'), Js('Markolf'), Js('Markward'), Js('Meinhard'), Js('Meinolf'), Js('Meinrad'), Js('Mombert'), Js('Neidhard'), Js('Norbert'), Js('Norman'), Js('Notker'), Js('Oddone'), Js('Oliver'), Js('Ortwin'), Js('Oswald'), Js('Ottfried'), Js('Ottmar'), Js('Otto'), Js('Ottokar'), Js('Otwin'), Js('Raban'), Js('Ralf'), Js('Randolf'), Js('Raymond'), Js('Rayner'), Js('Reimar'), Js('Reingard'), Js('Reinhard'), Js('Reinhold'), Js('Rembert'), Js('Richard'), Js('Richmut'), Js('Rigoberto'), Js('Roald'), Js('Robert'), Js('Rocco'), Js('Roderick'), Js('Roger'), Js('Roland'), Js('Romarich'), Js('Romuald'), Js('Rudolf'), Js('Sachso'), Js('Siegbald'), Js('Siegbert'), Js('Sieger'), Js('Siegfried'), Js('Sieghard'), Js('Siegmar'), Js('Siegmund'), Js('Siegward'), Js('Theobald'), Js('Thijmen'), Js('Thilo'), Js('Till'), Js('Ubaldo'), Js('Ulrich'), Js('Volkbert'), Js('Volker'), Js('Volkhard'), Js('Volkmar'), Js('Waldemar'), Js('Walfried'), Js('Walo'), Js('Walter'), Js('Waltram'), Js('Wedekind'), Js('Wendelin'), Js('Werner'), Js('Wieland'), Js('Wigand'), Js('Wigbert'), Js('Wighard'), Js('Wigmar'), Js('Wilburg'), Js('Wilfried'), Js('Wilhard'), Js('William'), Js('Willibald'), Js('Willibert'), Js('Wilmar'), Js('Winand'), Js('Winfried'), Js('Witold'), Js('Wolf'), Js('Wolfgang'), Js('Wolfhard'), Js('Wolfram'), Js('Wunibald'), Js('Zelindo')]))
var.put('nm2', Js([Js('Abelarda'), Js('Adalgisa'), Js('Adela'), Js('Adelgunde'), Js('Adelheid'), Js('Adelhelma'), Js('Adelinde'), Js('Adolfa'), Js('Alberta'), Js('Alda'), Js('Aldona'), Js('Alido'), Js('Almut'), Js('Alrun'), Js('Alwine'), Js('Amalberga'), Js('Anselma'), Js('Arda'), Js('Aristea'), Js('Arnhild'), Js('Arnolda'), Js('Asgard'), Js('Aubrey'), Js('Belinda'), Js('Bernharde'), Js('Berta'), Js('Berthild'), Js('Bertille'), Js('Bertrada'), Js('Bliktrud'), Js('Bruna'), Js('Brunhilde'), Js('Burghild'), Js('Burglinde'), Js('Carla'), Js('Charlotte'), Js('Cressida'), Js('Diemut'), Js('Diethild'), Js('Dietlinde'), Js('Diomira'), Js('Ebba'), Js('Edelgard'), Js('Edeltraud'), Js('Ehrentraud'), Js('Eike'), Js('Elfrun'), Js('Elma'), Js('Eloise'), Js('Elva'), Js('Emery'), Js('Engel'), Js('Engla'), Js('Ernesta'), Js('Everarda'), Js('Filiberta'), Js('Franka'), Js('Frauke'), Js('Frederika'), Js('Friedegund'), Js('Geraldine'), Js('Gerburg'), Js('Gerharde'), Js('Gerhild'), Js('Gerlinde'), Js('Gertrud'), Js('Gerwine'), Js('Gilberta'), Js('Gisela'), Js('Gotlinde'), Js('Griselda'), Js('Gudrun'), Js('Guerina'), Js('Gunda'), Js('Gundelinde'), Js('Gunthilde'), Js('Hedwig'), Js('Heilburg'), Js('Heilgard'), Js('Heilwig'), Js('Helmgard'), Js('Helmtraud'), Js('Hemma'), Js('Henrietta'), Js('Herlinde'), Js('Hermine'), Js('Herta'), Js('Hildburg'), Js('Hildegard'), Js('Hildegunde'), Js('Hildrun'), Js('Hiltrud'), Js('Huberta'), Js('Huguette'), Js('Hulda'), Js('Ida'), Js('Inge'), Js('Ingfried'), Js('Irma'), Js('Irmgard'), Js('Irmhild'), Js('Irmlinde'), Js('Irmtraud'), Js('Ishilde'), Js('Kai'), Js('Kaja'), Js('Kirsa'), Js('Klothilde'), Js('Konrada'), Js('Kriemhild'), Js('Kunigunde'), Js('Lamberta'), Js('Landriche'), Js('Leonarda'), Js('Leopoldine'), Js('Liebgard'), Js('Liebtrud'), Js('Linda'), Js('Linde'), Js('Lioba'), Js('Livina'), Js('Loreley'), Js('Louise'), Js('Ludgera'), Js('Ludwina'), Js('Luitgard'), Js('Margund'), Js('Mathilde'), Js('Merlind'), Js('Miltrud'), Js('Norgard'), Js('Nortrud'), Js('Notburga'), Js('Ortraud'), Js('Ortrun'), Js('Ostara'), Js('Ottilia'), Js('Radegundis'), Js('Raina'), Js('Ramona'), Js('Randi'), Js('Reinhild'), Js('Reinhilde'), Js('Riccarda'), Js('Richmute'), Js('Roberta'), Js('Rochelle'), Js('Rodina'), Js('Rolanda'), Js('Romilda'), Js('Rosalinde'), Js('Rosamunde'), Js('Roswitha'), Js('Rotraud'), Js('Runhild'), Js('Saskia'), Js('Schwanhilde'), Js('Sieghilde'), Js('Sieglinde'), Js('Sigune'), Js('Sunna'), Js('Sunnhild'), Js('Thusnelda'), Js('Ubalda'), Js('Ulrike'), Js('Ute'), Js('Veerle'), Js('Walpurga'), Js('Waltraud'), Js('Wanda'), Js('Wendelgard'), Js('Wendelina'), Js('Wigberta'), Js('Wigburg'), Js('Wilfriede'), Js('Wilhelma'), Js('Wiltrud'), Js('Yvonne')]))
pass
pass


# Add lib to the module scope
oldHighGerman = var.to_python()
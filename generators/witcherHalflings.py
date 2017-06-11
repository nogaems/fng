__all__ = ['witcherHalflings']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abbo'), Js('Aega'), Js('Ageric'), Js('Aigulf'), Js('Amand'), Js('Andwise'), Js('Anno'), Js('Arnold'), Js('Arnor'), Js('Arnoul'), Js('Arnulf'), Js('Basso'), Js('Baudry'), Js('Bauto'), Js('Bavo'), Js('Benild'), Js('Berchar'), Js('Bernard'), Js('Berno'), Js('Bero'), Js('Bertin'), Js('Bertram'), Js('Besso'), Js('Bildad'), Js('Blanco'), Js('Bodo'), Js('Bosco'), Js('Boso'), Js('Bovo'), Js('Brice'), Js('Briffo'), Js('Brocard'), Js('Bruno'), Js('Bucca'), Js('Bungo'), Js('Cerdic'), Js('Cheldric'), Js('Chlodwig'), Js('Chlotar'), Js('Clodio'), Js('Clovis'), Js('Conrad'), Js('Corbus'), Js('Cotman'), Js('Cottar'), Js('Crassus'), Js('Crispus'), Js('Dado'), Js('Dalfin'), Js('Deagol'), Js('Dodo'), Js('Drogo'), Js('Drogon'), Js('Dudo'), Js('Dudon'), Js('Durand'), Js('Ebbo'), Js('Einhard'), Js('Elfstan'), Js('Emmon'), Js('Erard'), Js('Erling'), Js('Euric'), Js('Evrard'), Js('Falco'), Js('Faro'), Js('Flambard'), Js('Flavus'), Js('Folco'), Js('Folmar'), Js('Fosco'), Js('Fulbert'), Js('Fulrad'), Js('Gerbert'), Js('Gereon'), Js('Gerold'), Js('Gilbert'), Js('Giso'), Js('Godun'), Js('Griffo'), Js('Grimald'), Js('Grimbald'), Js('Gruffo'), Js('Gunthar'), Js('Guntram'), Js('Hagen'), Js('Halfred'), Js('Hamfast'), Js('Harding'), Js('Hartmut'), Js('Hartnid'), Js('Hending'), Js('Hobson'), Js('Holfast'), Js('Holman'), Js('Hubert'), Js('Huebald'), Js('Hugo'), Js('Humbert'), Js('Hunald'), Js('Jago'), Js('Lambert'), Js('Largo'), Js('Laudus'), Js('Ledger'), Js('Leger'), Js('Leufred'), Js('Longo'), Js('Lothar'), Js('Madoc'), Js('Magnus'), Js('Marco'), Js('Marcoul'), Js('Marcus'), Js('Marroc'), Js('Medard'), Js('Merry'), Js('Milo'), Js('Minto'), Js('Moro'), Js('Mosco'), Js('Nithard'), Js('Norbert'), Js('Notger'), Js('Odger'), Js('Olo'), Js('Otker'), Js('Otto'), Js('Otton'), Js('Pepin'), Js('Pippin'), Js('Polo'), Js('Porro'), Js('Posco'), Js('Rathar'), Js('Rathier'), Js('Razo'), Js('Remi'), Js('Richer'), Js('Robin'), Js('Robur'), Js('Rollo'), Js('Rufus'), Js('Sadoc'), Js('Sago'), Js('Samson'), Js('Sichar'), Js('Sunno'), Js('Taurin'), Js('Thierry'), Js('Timba'), Js('Tobas'), Js('Tobold'), Js('Togo'), Js('Tolman'), Js('Turpin'), Js('Vigo'), Js('Vigor'), Js('Wazo'), Js('Wibert')]))
var.put('nm2', Js([Js('Abigail'), Js('Adallinda'), Js('Adda'), Js('Adele'), Js('Alexandra'), Js('Alexis'), Js('Alia'), Js('Alicia'), Js('Allison'), Js('Alura'), Js('Alyssa'), Js('Amalda'), Js('Amanda'), Js('Amaranth'), Js('Amber'), Js('Amethyst'), Js('Amy'), Js('Andrea'), Js('Angela'), Js('Angelica'), Js('Anna'), Js('Arabella'), Js('Aregund'), Js('Athalia'), Js('Aude'), Js('Audovera'), Js('Autumn'), Js('Basina'), Js('Begga'), Js('Belba'), Js('Belinda'), Js('Belladonna'), Js('Berenga'), Js('Beretrude'), Js('Bertha'), Js('Berthe'), Js('Bertrada'), Js('Berylla'), Js('Blesinde'), Js('Camelia'), Js('Cara'), Js('Caramella'), Js('Caroline'), Js('Cassandra'), Js('Catherine'), Js('Celendine'), Js('Chelsea'), Js('Cheryl'), Js('Cheyenne'), Js('Christina'), Js('Clotilde'), Js('Cora'), Js('Cori'), Js('Daisy'), Js('Delaney'), Js('Deuteria'), Js('Diamanda'), Js('Diamond'), Js('Diana'), Js('Dina'), Js('Donna'), Js('Donnamira'), Js('Dora'), Js('Elanor'), Js('Ellie'), Js('Emma'), Js('Engelberga'), Js('Engelberge'), Js('Erica'), Js('Erin'), Js('Fara'), Js('Fiona'), Js('Genofeva'), Js('Gerda'), Js('Gilly'), Js('Gisela'), Js('Gloriana'), Js('Grimalda'), Js('Haley'), Js('Hatilde'), Js('Herleva'), Js('Hilda'), Js('Hildeburg'), Js('Hildegard'), Js('Hildegarde'), Js('Hildegund'), Js('Hiltrude'), Js('Hodierna'), Js('Ingeltrude'), Js('Ingitrude'), Js('Ingoberg'), Js('Iridian'), Js('Jasmine'), Js('Jemima'), Js('Jessamine'), Js('Jessica'), Js('Julia'), Js('Kayla'), Js('Keena'), Js('Keira'), Js('Kymma'), Js('Lalia'), Js('Laura'), Js('Lauren'), Js('Lavinia'), Js('Leesha'), Js('Lenora'), Js('Lily'), Js('Linda'), Js('Madelgarde'), Js('Malva'), Js('Maria'), Js('Marigold'), Js('Matilda'), Js('Melba'), Js('Melissa'), Js('Menegilda'), Js('Mentha'), Js('Merofled'), Js('Mirabella'), Js('Miranda'), Js('Moira'), Js('Myrna'), Js('Myrtle'), Js('Neela'), Js('Nina'), Js('Nora'), Js('Oda'), Js('Olivia'), Js('Paige'), Js('Prima'), Js('Primrose'), Js('Primula'), Js('Prisca'), Js('Regina'), Js('Rhoda'), Js('Rosa'), Js('Rosamund'), Js('Rosamunda'), Js('Rose'), Js('Roslyn'), Js('Rotrude'), Js('Rowan'), Js('Rylee'), Js('Salvia'), Js('Sarai'), Js('Selina'), Js('Semolina'), Js('Shanna'), Js('Suri'), Js('Tara'), Js('Taryn'), Js('Tavia'), Js('Theodora')]))
var.put('nm3', Js([Js('Adel'), Js('Alt'), Js('And'), Js('Ans'), Js('Arm'), Js('Balden'), Js('Berk'), Js('Biber'), Js('Bil'), Js('Blum'), Js('Bottom'), Js('Boulder'), Js('Brace'), Js('Bramble'), Js('Brand'), Js('Brod'), Js('Cull'), Js('Dew'), Js('Edel'), Js('Eisen'), Js('Fair'), Js('Fallo'), Js('Far'), Js('Fass'), Js('Fein'), Js('Finna'), Js('Flor'), Js('Gal'), Js('Gam'), Js('Gell'), Js('Hal'), Js('Ham'), Js('Hand'), Js('Har'), Js('Hard'), Js('Hay'), Js('Hilde'), Js('Hoch'), Js('Hof'), Js('Hog'), Js('Knot'), Js('Korn'), Js('Land'), Js('Lehm'), Js('Lowen'), Js('Mug'), Js('Neu'), Js('Old'), Js('Rei'), Js('Rosen'), Js('Roth'), Js('Stritt'), Js('Tol'), Js('Vander'), Js('Wahr'), Js('Weg'), Js('Weide'), Js('Wein'), Js('Weis'), Js('Whit')]))
var.put('nm4', Js([Js('bach'), Js('bairn'), Js('bald'), Js('baum'), Js('beck'), Js('berg'), Js('berry'), Js('bottom'), Js('brand'), Js('buck'), Js('buhr'), Js('burg'), Js('burrow'), Js('der'), Js('fast'), Js('fel'), Js('feld'), Js('felt'), Js('foot'), Js('gard'), Js('gart'), Js('gund'), Js('ham'), Js('hand'), Js('hang'), Js('hard'), Js('haupt'), Js('haus'), Js('heimer'), Js('hell'), Js('hill'), Js('kranz'), Js('lein'), Js('lich'), Js('ling'), Js('man'), Js('meier'), Js('ming'), Js('mond'), Js('red'), Js('ric'), Js('rich'), Js('ring'), Js('roth'), Js('stein'), Js('stock'), Js('thal'), Js('thorn'), Js('thran'), Js('tram'), Js('veldt'), Js('ville'), Js('wald'), Js('ward'), Js('wend'), Js('wich'), Js('wise'), Js('wort'), Js('yegg'), Js('zel')]))
pass
pass


# Add lib to the module scope
witcherHalflings = var.to_python()
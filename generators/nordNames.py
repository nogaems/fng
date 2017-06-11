__all__ = ['nordNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                if (var.get('i')<Js(4.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', (((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+Js(' '))+var.get('nm9').get(var.get('rnd7'))))
                    else:
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', (((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+Js(' '))+var.get('nm10').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('i')<Js(4.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm9').get(var.get('rnd7'))))
                    else:
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm10').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd8')))+var.get('nm3').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abb'), Js('Abba'), Js('Ada'), Js('Adal'), Js('Add'), Js('Addi'), Js('Addv'), Js('Adr'), Js('Adri'), Js('Aen'), Js('Aena'), Js('Aev'), Js('Aeva'), Js('Aga'), Js('Agar'), Js('Agm'), Js('Agma'), Js('Agn'), Js('Agna'), Js('Agni'), Js('Aka'), Js('Akar'), Js('Al'), Js('Ald'), Js('Aldi'), Js('Alf'), Js('Alfa'), Js('Alfb'), Js('Alfh'), Js('Alg'), Js('Algo'), Js('All'), Js('Alld'), Js('Alo'), Js('Alof'), Js('Alv'), Js('Alvo'), Js('Alvr'), Js('And'), Js('Ande'), Js('Andr'), Js('Andu'), Js('Ang'), Js('Angr'), Js('Angv'), Js('Arc'), Js('Arct'), Js('Are'), Js('Area'), Js('Arg'), Js('Argi'), Js('Ark'), Js('Arkm'), Js('Arn'), Js('Arnb'), Js('Arng'), Js('Arns'), Js('Arr'), Js('Arra'), Js('Asb'), Js('Asbj'), Js('Asg'), Js('Asge'), Js('Asl'), Js('Aslf'), Js('Ass'), Js('Assu'), Js('Ata'), Js('Atar'), Js('Aud'), Js('Audm'), Js('Ave'), Js('Aven'), Js('Avu'), Js('Avul'), Js('Bad'), Js('Badn'), Js('Bal'), Js('Balb'), Js('Bald'), Js('Balf'), Js('Balg'), Js('Bali'), Js('Balm'), Js('Bar'), Js('Bari'), Js('Bas'), Js('Basl'), Js('Bass'), Js('Bat'), Js('Bath'), Js('Bato'), Js('Bed'), Js('Bedr'), Js('Bei'), Js('Bein'), Js('Beir'), Js('Bel'), Js('Belr'), Js('Ben'), Js('Benk'), Js('Beno'), Js('Ber'), Js('Bers'), Js('Bir'), Js('Birk'), Js('Bit'), Js('Bitt'), Js('Bj'), Js('Bja'), Js('Bjad'), Js('Bjal'), Js('Bjo'), Js('Bjor'), Js('Bol'), Js('Bolg'), Js('Boll'), Js('Bolu'), Js('Bor'), Js('Borg'), Js('Borm'), Js('Borr'), Js('Borv'), Js('Bot'), Js('Botr'), Js('Bott'), Js('Bra'), Js('Bran'), Js('Bre'), Js('Bref'), Js('Bri'), Js('Brie'), Js('Bril'), Js('Brir'), Js('Bro'), Js('Bron'), Js('Bru'), Js('Brun'), Js('Brur'), Js('Bry'), Js('Bryn'), Js('Bul'), Js('Bulf'), Js('Bur'), Js('Burd'), Js('Cal'), Js('Cald'), Js('Car'), Js('Cars'), Js('Chr'), Js('Chri'), Js('Cri'), Js('Cris'), Js('Dag'), Js('Dagl'), Js('Dagu'), Js('Dat'), Js('Dath'), Js('Den'), Js('Deng'), Js('Deo'), Js('Deor'), Js('Der'), Js('Dere'), Js('Dero'), Js('Dra'), Js('Drah'), Js('Dre'), Js('Dren'), Js('Dry'), Js('Dryn'), Js('Eif'), Js('Eifi'), Js('Eim'), Js('Eima'), Js('Ein'), Js('Eina'), Js('Eit'), Js('Eita'), Js('Eld'), Js('Eldj'), Js('Eldr'), Js('Elg'), Js('Elgr'), Js('Elm'), Js('Elmu'), Js('Emb'), Js('Embr'), Js('Eng'), Js('Enga'), Js('Enn'), Js('Ennb'), Js('Eor'), Js('Eorl'), Js('Er'), Js('Erg'), Js('Ergn'), Js('Eri'), Js('Eric'), Js('Erik'), Js('Erl'), Js('Erle'), Js('Erli'), Js('Esb'), Js('Esbe'), Js('Faf'), Js('Fafn'), Js('Fal'), Js('Falk'), Js('Fan'), Js('Fana'), Js('Far'), Js('Fare'), Js('Fark'), Js('Fel'), Js('Fell'), Js('Fen'), Js('Fenr'), Js('Fil'), Js('Filn'), Js('Fjo'), Js('Fjol'), Js('Fjor'), Js('Fjot'), Js('Fjr'), Js('Fjro'), Js('For'), Js('Fors'), Js('Fra'), Js('Frak'), Js('Fral'), Js('Fri'), Js('Frik'), Js('Fro'), Js('Frod'), Js('Frof'), Js('Frok'), Js('Fror'), Js('Frot'), Js('Gal'), Js('Galm'), Js('Galt'), Js('Gar'), Js('Gard'), Js('Gart'), Js('Garu'), Js('Gau'), Js('Gaul'), Js('Gei'), Js('Geil'), Js('Geim'), Js('Geir'), Js('Gel'), Js('Gell'), Js('Ges'), Js('Gest'), Js('Gir'), Js('Girg'), Js('Gis'), Js('Gisl'), Js('Giss'), Js('Gja'), Js('Gjak'), Js('Gjal'), Js('Gju'), Js('Gjuk'), Js('Glo'), Js('Glot'), Js('God'), Js('Godr'), Js('Gog'), Js('Gogr'), Js('Gol'), Js('Goll'), Js('Gon'), Js('Gonn'), Js('Gor'), Js('Gorm'), Js('Gort'), Js('Gra'), Js('Gral'), Js('Grar'), Js('Gre'), Js('Greg'), Js('Gri'), Js('Grim'), Js('Gris'), Js('Grj'), Js('Grjo'), Js('Gro'), Js('Grom'), Js('Gud'), Js('Gudl'), Js('Guk'), Js('Guki'), Js('Gun'), Js('Gund'), Js('Gunm'), Js('Gunn'), Js('Gur'), Js('Guri'), Js('Gut'), Js('Guth'), Js('Haa'), Js('Haak'), Js('Had'), Js('Hadr'), Js('Hadv'), Js('Hae'), Js('Haen'), Js('Haes'), Js('Haf'), Js('Hafi'), Js('Hafn'), Js('Hag'), Js('Hagr'), Js('Haj'), Js('Hajv'), Js('Hak'), Js('Haka'), Js('Hakn'), Js('Hako'), Js('Hal'), Js('Halb'), Js('Hall'), Js('Haln'), Js('Halo'), Js('Halu'), Js('Ham'), Js('Hami'), Js('Haml'), Js('Hamv'), Js('Han'), Js('Hans'), Js('Har'), Js('Hara'), Js('Harg'), Js('Hark'), Js('Harl'), Js('Harr'), Js('Hav'), Js('Havi'), Js('Hed'), Js('Hedd'), Js('Hef'), Js('Hefa'), Js('Hei'), Js('Heid'), Js('Heif'), Js('Heim'), Js('Hein'), Js('Hel'), Js('Helv'), Js('Hem'), Js('Hemm'), Js('Hen'), Js('Henr'), Js('Her'), Js('Hera'), Js('Herd'), Js('Herm'), Js('Hern'), Js('Hew'), Js('Hewn'), Js('Hig'), Js('Higi'), Js('Hil'), Js('Hild'), Js('Hir'), Js('Hirn'), Js('His'), Js('Hisi'), Js('Hja'), Js('Hjal'), Js('Hjar'), Js('Hjo'), Js('Hjol'), Js('Hjor'), Js('Hjr'), Js('Hjro'), Js('Hla'), Js('Hlar'), Js('Hlo'), Js('Hlof'), Js('Hlog'), Js('Hlor'), Js('Hoa'), Js('Hoag'), Js('Hod'), Js('Hodl'), Js('Hof'), Js('Hofg'), Js('Hog'), Js('Hogn'), Js('Hok'), Js('Hoki'), Js('Hol'), Js('Holg'), Js('Holm'), Js('Hon'), Js('Honm'), Js('Hont'), Js('Hor'), Js('Horg'), Js('Hori'), Js('Hork'), Js('Horm'), Js('Hors'), Js('Hos'), Js('Hosg'), Js('Hra'), Js('Hrar'), Js('Hre'), Js('Hrei'), Js('Hri'), Js('Hrid'), Js('Hris'), Js('Hro'), Js('Hroa'), Js('Hrod'), Js('Hrog'), Js('Hroi'), Js('Hrol'), Js('Hron'), Js('Hror'), Js('Hrot'), Js('Hru'), Js('Hrun'), Js('Hul'), Js('Hulg'), Js('Hun'), Js('Hunr'), Js('Hur'), Js('Hurg'), Js('Hurn'), Js('Huro'), Js('Hyl'), Js('Hylf'), Js('Idl'), Js('Idla'), Js('Ido'), Js('Idol'), Js('Igm'), Js('Igmu'), Js('Ing'), Js('Ingj'), Js('Ingm'), Js('Irl'), Js('Irlo'), Js('Irn'), Js('Irns'), Js('Irr'), Js('Irro'), Js('Ist'), Js('Ista'), Js('Istl'), Js('Ita'), Js('Itar'), Js('Ive'), Js('Iver'), Js('Jal'), Js('Jalm'), Js('Jay'), Js('Jayr'), Js('Jee'), Js('Jeek'), Js('Jen'), Js('Jens'), Js('Jer'), Js('Jerv'), Js('Jes'), Js('Jesp'), Js('Jod'), Js('Jof'), Js('Jofn'), Js('Joft'), Js('Jol'), Js('Jolf'), Js('Jolg'), Js('Joll'), Js('Jon'), Js('Jond'), Js('Jor'), Js('Jorc'), Js('Jorg'), Js('Jori'), Js('Jorl'), Js('Jorn'), Js('Joru'), Js('Jur'), Js('Jurg'), Js('Jyr'), Js('Jyri'), Js('Kai'), Js('Kal'), Js('Kalt'), Js('Kar'), Js('Karl'), Js('Kars'), Js('Kel'), Js('Keld'), Js('Kib'), Js('Kibe'), Js('Kj'), Js('Kja'), Js('Kjar'), Js('Kje'), Js('Kjel'), Js('Kjo'), Js('Kjor'), Js('Kle'), Js('Klep'), Js('Kli'), Js('Klim'), Js('Klu'), Js('Kluw'), Js('Knj'), Js('Knja'), Js('Knu'), Js('Knud'), Js('Knur'), Js('Kod'), Js('Kodl'), Js('Kodr'), Js('Kol'), Js('Koli'), Js('Kor'), Js('Kori'), Js('Kors'), Js('Kot'), Js('Kott'), Js('Kra'), Js('Kral'), Js('Kun'), Js('Kunt'), Js('Kus'), Js('Kust'), Js('Kuv'), Js('Kuva'), Js('Kve'), Js('Kven'), Js('Kyr'), Js('Kyrn'), Js('Lar'), Js('Lars'), Js('Lart'), Js('Las'), Js('Lass'), Js('Lei'), Js('Leif'), Js('Leig'), Js('Lem'), Js('Lemk'), Js('Len'), Js('Lenn'), Js('Lle'), Js('Llew'), Js('Loa'), Js('Loat'), Js('Lod'), Js('Lodi'), Js('Lodv'), Js('Log'), Js('Logr'), Js('Logv'), Js('Lok'), Js('Lokh'), Js('Loki'), Js('Lon'), Js('Lond'), Js('Lor'), Js('Lore'), Js('Lork'), Js('Loro'), Js('Lort'), Js('Lun'), Js('Lund'), Js('Lyg'), Js('Lygr'), Js('Lyn'), Js('Lync'), Js('Lyno'), Js('Mae'), Js('Maer'), Js('Maj'), Js('Majn'), Js('Mal'), Js('Malt'), Js('Man'), Js('Manh'), Js('Mant'), Js('Manw'), Js('Mar'), Js('Mark'), Js('Mat'), Js('Math'), Js('Mau'), Js('Maul'), Js('Mek'), Js('Meks'), Js('Men'), Js('Mend'), Js('Menr'), Js('Mer'), Js('Merk'), Js('Met'), Js('Meti'), Js('Mik'), Js('Mika'), Js('Mikr'), Js('Mir'), Js('Mira'), Js('Mog'), Js('Moge'), Js('Moj'), Js('Mol'), Js('Molg'), Js('Mra'), Js('Mral'), Js('Mry'), Js('Mryf'), Js('Msi'), Js('Msir'), Js('Nar'), Js('Narf'), Js('Ned'), Js('Nedd'), Js('Nel'), Js('Nelk'), Js('Nels'), Js('New'), Js('Newh'), Js('Nie'), Js('Niel'), Js('Nil'), Js('Nils'), Js('Nod'), Js('Nodu'), Js('Nor'), Js('Norr'), Js('Nys'), Js('Nyst'), Js('Oda'), Js('Odar'), Js('Odf'), Js('Odfe'), Js('Odm'), Js('Odmi'), Js('Oen'), Js('Oeng'), Js('Ogm'), Js('Ogmu'), Js('Ola'), Js('Olaf'), Js('Olav'), Js('Olf'), Js('Olfa'), Js('Olfr'), Js('Oll'), Js('Ollr'), Js('Olm'), Js('Olmg'), Js('Ong'), Js('Onga'), Js('Onm'), Js('Onmi'), Js('Onmu'), Js('Org'), Js('Orgn'), Js('Orm'), Js('Ormv'), Js('Ort'), Js('Orth'), Js('Orti'), Js('Osl'), Js('Osla'), Js('Pac'), Js('Pact'), Js('Pel'), Js('Pelf'), Js('Rad'), Js('Radd'), Js('Rae'), Js('Raer'), Js('Raf'), Js('Rafl'), Js('Rag'), Js('Ragn'), Js('Rak'), Js('Rako'), Js('Ral'), Js('Ralo'), Js('Ram'), Js('Ramt'), Js('Ran'), Js('Ranm'), Js('Rar'), Js('Rarg'), Js('Reg'), Js('Regn'), Js('Rei'), Js('Rein'), Js('Reis'), Js('Rev'), Js('Reve'), Js('Rho'), Js('Rhor'), Js('Rig'), Js('Rige'), Js('Rigm'), Js('Ris'), Js('Riss'), Js('Roe'), Js('Roet'), Js('Rog'), Js('Roge'), Js('Rogg'), Js('Rol'), Js('Rolf'), Js('Rolg'), Js('Roli'), Js('Ror'), Js('Rori'), Js('Rorl'), Js('Run'), Js('Rund'), Js('Rus'), Js('Rust'), Js('Sab'), Js('Sabj'), Js('Sae'), Js('Saer'), Js('Saet'), Js('Sar'), Js('Sarn'), Js('Sat'), Js('Satt'), Js('Sav'), Js('Sava'), Js('Sib'), Js('Sibb'), Js('Sid'), Js('Sidd'), Js('Sif'), Js('Sifk'), Js('Sifn'), Js('Sig'), Js('Siga'), Js('Sigd'), Js('Sigu'), Js('Sigv'), Js('Sil'), Js('Sild'), Js('Sin'), Js('Sind'), Js('Sinm'), Js('Sir'), Js('Sirg'), Js('Sirk'), Js('Sit'), Js('Sitt'), Js('Sja'), Js('Sjar'), Js('Sjo'), Js('Sjor'), Js('Ska'), Js('Skag'), Js('Skal'), Js('Skar'), Js('Ske'), Js('Skeg'), Js('Skj'), Js('Skjo'), Js('Sko'), Js('Skor'), Js('Sku'), Js('Skul'), Js('Sla'), Js('Slaf'), Js('Sna'), Js('Snad'), Js('Snar'), Js('Sne'), Js('Sned'), Js('Sni'), Js('Snil'), Js('Sno'), Js('Snor'), Js('Sog'), Js('Sogr'), Js('Sol'), Js('Sola'), Js('Sold'), Js('Sor'), Js('Sork'), Js('Sorr'), Js('Sta'), Js('Stal'), Js('Star'), Js('Ste'), Js('Stei'), Js('Sten'), Js('Sti'), Js('Stig'), Js('Sto'), Js('Stor'), Js('Str'), Js('Stro'), Js('Sty'), Js('Styr'), Js('Sul'), Js('Sulv'), Js('Sva'), Js('Svak'), Js('Sve'), Js('Sven'), Js('Svo'), Js('Svog'), Js('Swy'), Js('Swyk'), Js('Tal'), Js('Tals'), Js('Ter'), Js('Terr'), Js('Tha'), Js('Thad'), Js('Thae'), Js('Thal'), Js('Thar'), Js('Thi'), Js('Thia'), Js('Thj'), Js('Thjo'), Js('Tho'), Js('Thon'), Js('Thor'), Js('Thr'), Js('Thro'), Js('Thru'), Js('Thry'), Js('Thu'), Js('Thur'), Js('Tol'), Js('Tola'), Js('Tolf'), Js('Tolg'), Js('Tor'), Js('Tora'), Js('Torb'), Js('Toro'), Js('Tors'), Js('Torv'), Js('Tory'), Js('Tov'), Js('Tove'), Js('Tri'), Js('Tril'), Js('Tsu'), Js('Tsun'), Js('Tul'), Js('Tulv'), Js('Tym'), Js('Tymv'), Js('Tys'), Js('Tysn'), Js('Uch'), Js('Uche'), Js('Ulf'), Js('Ulfa'), Js('Ulfb'), Js('Ulfg'), Js('Ulfr'), Js('Ulr'), Js('Und'), Js('Undv'), Js('Unm'), Js('Unmi'), Js('Urf'), Js('Urfi'), Js('Url'), Js('Urla'), Js('Val'), Js('Vald'), Js('Valg'), Js('Valu'), Js('Van'), Js('Vani'), Js('Vek'), Js('Veke'), Js('Vel'), Js('Velf'), Js('Ver'), Js('Vern'), Js('Vid'), Js('Vidg'), Js('Vidi'), Js('Vidk'), Js('Vidr'), Js('Vig'), Js('Vigg'), Js('Vign'), Js('Vil'), Js('Vilk'), Js('Vilo'), Js('Vip'), Js('Vipi'), Js('Vir'), Js('Virg'), Js('Virk'), Js('Vol'), Js('Volk'), Js('Von'), Js('Vong'), Js('Vor'), Js('Vors'), Js('Vra'), Js('Vrag'), Js('Vul'), Js('Vulw'), Js('Vun'), Js('Vund'), Js('Wil'), Js('Wilh'), Js('Wilm'), Js('Wra'), Js('Wrat'), Js('Wul'), Js('Wulf'), Js('Wuu'), Js('Wuun'), Js('Ylg'), Js('Ylga'), Js('Yng'), Js('Yngl'), Js('Yngn'), Js('Yngo'), Js('Yngv'), Js('Yrs'), Js('Yrsa'), Js('Ysg'), Js('Ysgr'), Js('Ysm'), Js('Ysmi'), Js('Yus'), Js('Yust')]))
var.put('nm2', Js([Js('a'), Js('aak'), Js('aar'), Js('ach'), Js('ad'), Js('admir'), Js('ae'), Js('ael'), Js('aer'), Js('af'), Js('aflod'), Js('ak'), Js('akr'), Js('al'), Js('ald'), Js('aldr'), Js('alf'), Js('allod'), Js('ami'), Js('amor'), Js('an'), Js('and'), Js('ar'), Js('arald'), Js('ard'), Js('arel'), Js('arinn'), Js('arn'), Js('arr'), Js('arth'), Js('as'), Js('atar'), Js('atr'), Js('aug'), Js('aul'), Js('avar'), Js('bal'), Js('bald'), Js('barn'), Js('berth'), Js('bi'), Js('bjof'), Js('bjorn'), Js('brand'), Js('brir'), Js('bus'), Js('ch'), Js('ck'), Js('ct'), Js('dall'), Js('dan'), Js('dar'), Js('dbrir'), Js('del'), Js('demar'), Js('der'), Js('dgeir'), Js('dheim'), Js('di'), Js('dic'), Js('dimar'), Js('ding'), Js('dir'), Js('dis'), Js('dlar'), Js('dmir'), Js('dmund'), Js('dnar'), Js('dor'), Js('dr'), Js('drir'), Js('dulf'), Js('dur'), Js('e'), Js('ed'), Js('edil'), Js('ehl'), Js('eif'), Js('eim'), Js('eir'), Js('ek'), Js('el'), Js('eld'), Js('elf'), Js('elheim'), Js('ell'), Js('ellyn'), Js('elm'), Js('emar'), Js('en'), Js('endr'), Js('engar'), Js('enor'), Js('ens'), Js('enz'), Js('er'), Js('erd'), Js('ern'), Js('ers'), Js('erth'), Js('es'), Js('eskr'), Js('far'), Js('fdir'), Js('ferth'), Js('ff'), Js('fgar'), Js('fi'), Js('fing'), Js('fknir'), Js('fmare'), Js('fnir'), Js('fred'), Js('frek'), Js('fring'), Js('fur'), Js('fwiil'), Js('fyg'), Js('gal'), Js('gan'), Js('gar'), Js('garel'), Js('garth'), Js('gas'), Js('ge'), Js('geir'), Js('gelf'), Js('gen'), Js('ger'), Js('gerd'), Js('gg'), Js('ggar'), Js('ggi'), Js('ggr'), Js('gheid'), Js('gi'), Js('gny'), Js('gor'), Js('gr'), Js('grim'), Js('grir'), Js('grod'), Js('grom'), Js('gruuf'), Js('gul'), Js('gun'), Js('gunn'), Js('guri'), Js('gvar'), Js('gvild'), Js('gvir'), Js('gvor'), Js('h'), Js('har'), Js('hardt'), Js('hedil'), Js('heim'), Js('helm'), Js('hff'), Js('hies'), Js('hild'), Js('hjar'), Js('hjolf'), Js('hl'), Js('hman'), Js('hmar'), Js('hmund'), Js('hor'), Js('horgh'), Js('hrum'), Js('i'), Js('iand'), Js('ianus'), Js('iarco'), Js('ic'), Js('id'), Js('ies'), Js('ig'), Js('ik'), Js('il'), Js('ild'), Js('ilius'), Js('ilstein'), Js('im'), Js('imar'), Js('imir'), Js('imk'), Js('imund'), Js('in'), Js('ing'), Js('inn'), Js('ir'), Js('irod'), Js('irrid'), Js('is'), Js('ismod'), Js('ister'), Js('it'), Js('jaldr'), Js('jar'), Js('jof'), Js('jolf'), Js('jolfr'), Js('jorg'), Js('jorn'), Js('kar'), Js('kas'), Js('ke'), Js('ki'), Js('kil'), Js('kir'), Js('kjorg'), Js('kmar'), Js('kmir'), Js('kmund'), Js('knir'), Js('knolf'), Js('kon'), Js('kr'), Js('kum'), Js('kun'), Js('kur'), Js('kus'), Js('kvar'), Js('kvild'), Js('kvir'), Js('kyllian'), Js('laf'), Js('lak'), Js('lam'), Js('lar'), Js('laug'), Js('ld'), Js('ldan'), Js('ldar'), Js('ldir'), Js('ldr'), Js('ldur'), Js('leid'), Js('leif'), Js('len'), Js('lf'), Js('lfar'), Js('lfdir'), Js('lfi'), Js('li'), Js('lin'), Js('ling'), Js('lir'), Js('lismod'), Js('lius'), Js('lki'), Js('ll'), Js('lling'), Js('llod'), Js('lmer'), Js('lmir'), Js('lnach'), Js('lnar'), Js('lod'), Js('lof'), Js('lring'), Js('ls'), Js('lstein'), Js('lti'), Js('lund'), Js('lvald'), Js('lvar'), Js('lvaror'), Js('man'), Js('mar'), Js('mare'), Js('mdall'), Js('mek'), Js('mer'), Js('meskr'), Js('mgar'), Js('mi'), Js('ming'), Js('mir'), Js('mk'), Js('mm'), Js('mmek'), Js('moor'), Js('mor'), Js('mskr'), Js('mund'), Js('muth'), Js('mvar'), Js('nach'), Js('nal'), Js('nar'), Js('navar'), Js('nd'), Js('ndar'), Js('ndi'), Js('ndir'), Js('ndr'), Js('ne'), Js('nel'), Js('neld'), Js('nen'), Js('ner'), Js('nferth'), Js('nfid'), Js('nfing'), Js('ng'), Js('ngar'), Js('ngheid'), Js('ngr'), Js('ngrim'), Js('ngvor'), Js('nhardt'), Js('nhild'), Js('ni'), Js('nil'), Js('ning'), Js('nir'), Js('njar'), Js('njolf'), Js('njolfr'), Js('nl'), Js('nlen'), Js('nnen'), Js('nnir'), Js('nolf'), Js('nolfr'), Js('non'), Js('nr'), Js('nrich'), Js('nrod'), Js('ns'), Js('nskar'), Js('ntus'), Js('nunn'), Js('nvar'), Js('nwulf'), Js('ny'), Js('nz'), Js('oct'), Js('od'), Js('of'), Js('oit'), Js('oke'), Js('oknolf'), Js('okvar'), Js('ol'), Js('old'), Js('oldr'), Js('olf'), Js('ollod'), Js('om'), Js('omgar'), Js('on'), Js('ondir'), Js('oor'), Js('or'), Js('orgh'), Js('ormr'), Js('orn'), Js('oslod'), Js('ot'), Js('otgaror'), Js('ou'), Js('per'), Js('ppr'), Js('pr'), Js('ra'), Js('rad'), Js('rae'), Js('raflod'), Js('rald'), Js('rallod'), Js('ramor'), Js('rand'), Js('rbald'), Js('rbjorn'), Js('rd'), Js('rdan'), Js('red'), Js('reid'), Js('rek'), Js('relheim'), Js('renor'), Js('rfyg'), Js('rgal'), Js('rgar'), Js('rgeir'), Js('rguri'), Js('ri'), Js('ric'), Js('rich'), Js('rid'), Js('rig'), Js('rik'), Js('rim'), Js('ring'), Js('rinn'), Js('rir'), Js('rkmar'), Js('rknir'), Js('rlaf'), Js('rlak'), Js('rlam'), Js('rleid'), Js('rlund'), Js('rm'), Js('rmar'), Js('rmir'), Js('rmoor'), Js('rmund'), Js('rn'), Js('rnfid'), Js('rnolfr'), Js('rnskar'), Js('ro'), Js('rod'), Js('rolf'), Js('rom'), Js('roor'), Js('rormr'), Js('rr'), Js('rreid'), Js('rri'), Js('rrid'), Js('rrod'), Js('rs'), Js('rsten'), Js('rth'), Js('rul'), Js('rum'), Js('runn'), Js('ruuf'), Js('rvar'), Js('ry'), Js('rygg'), Js('ryr'), Js('se'), Js('sen'), Js('sgar'), Js('si'), Js('sianus'), Js('sim'), Js('sing'), Js('skar'), Js('skr'), Js('slod'), Js('smar'), Js('snr'), Js('ss'), Js('ssen'), Js('sskar'), Js('st'), Js('staag'), Js('stag'), Js('star'), Js('stein'), Js('sten'), Js('ster'), Js('str'), Js('stus'), Js('sur'), Js('svar'), Js('taag'), Js('tag'), Js('tar'), Js('te'), Js('ten'), Js('tgaror'), Js('th'), Js('thar'), Js('theim'), Js('thjar'), Js('thjolf'), Js('thmund'), Js('thor'), Js('ti'), Js('tiarco'), Js('tir'), Js('tleif'), Js('tneld'), Js('tr'), Js('treid'), Js('tring'), Js('trom'), Js('tur'), Js('tus'), Js('u'), Js('ud'), Js('uk'), Js('ul'), Js('ulf'), Js('um'), Js('un'), Js('und'), Js('undr'), Js('unn'), Js('ur'), Js('urd'), Js('urs'), Js('us'), Js('uth'), Js('vaar'), Js('vald'), Js('var'), Js('vard'), Js('varor'), Js('varr'), Js('vatr'), Js('vaul'), Js('veld'), Js('vid'), Js('vild'), Js('vir'), Js('vur'), Js('we'), Js('wellyn'), Js('wiil'), Js('wulf'), Js('ygg'), Js('yllian'), Js('ynn'), Js('yr'), Js('ald'), Js('an'), Js('ar'), Js('arik'), Js('arke'), Js('arne'), Js('eld'), Js('en'), Js('ens'), Js('er'), Js('ik'), Js('is'), Js('orn')]))
var.put('nm3', Js([Js('sen'), Js('ssen'), Js('son'), Js('sson')]))
var.put('nm4', Js([Js('Abe'), Js('Abel'), Js('Adi'), Js('Adis'), Js('Aeg'), Js('Aegi'), Js('Ael'), Js('Aela'), Js('Aer'), Js('Aeri'), Js('Aet'), Js('Aeta'), Js('Aga'), Js('Agat'), Js('Agn'), Js('Agna'), Js('Agne'), Js('Agni'), Js('Ald'), Js('Aldi'), Js('Ale'), Js('Alea'), Js('Alf'), Js('Alfh'), Js('Alg'), Js('Alga'), Js('Alv'), Js('Alva'), Js('Alvi'), Js('Ang'), Js('Angi'), Js('Ani'), Js('Anis'), Js('Anj'), Js('Anja'), Js('Ann'), Js('Anne'), Js('Ans'), Js('Ansk'), Js('Arg'), Js('Argi'), Js('Ari'), Js('Ast'), Js('Asta'), Js('Astr'), Js('Aum'), Js('Aums'), Js('Bar'), Js('Barr'), Js('Bei'), Js('Beit'), Js('Ber'), Js('Bera'), Js('Berg'), Js('Bet'), Js('Betr'), Js('Bir'), Js('Birn'), Js('Bja'), Js('Bjar'), Js('Bod'), Js('Bodi'), Js('Bol'), Js('Bolf'), Js('Bot'), Js('Boti'), Js('Bra'), Js('Bras'), Js('Bre'), Js('Brey'), Js('Bri'), Js('Brin'), Js('Brit'), Js('Bry'), Js('Bryl'), Js('Buj'), Js('Bujo'), Js('Dag'), Js('Dagn'), Js('Dan'), Js('Dani'), Js('Dor'), Js('Dort'), Js('Dri'), Js('Drif'), Js('Edi'), Js('Edit'), Js('Edl'), Js('Edla'), Js('Eig'), Js('Eigm'), Js('Eir'), Js('Eiri'), Js('Eiru'), Js('Eis'), Js('Eisa'), Js('Ekk'), Js('Ekkh'), Js('Eld'), Js('Elda'), Js('Eli'), Js('Elis'), Js('Els'), Js('Else'), Js('Emf'), Js('Emfr'), Js('Erd'), Js('Erdi'), Js('Eri'), Js('Eris'), Js('Ern'), Js('Erna'), Js('Eve'), Js('Evet'), Js('Eyd'), Js('Eydi'), Js('Eyj'), Js('Eyja'), Js('Fai'), Js('Faid'), Js('Fan'), Js('Fana'), Js('Fas'), Js('Fast'), Js('Fin'), Js('Finn'), Js('Fjo'), Js('Fjol'), Js('Fjor'), Js('Fjot'), Js('Fra'), Js('Frab'), Js('Fral'), Js('Fre'), Js('Frea'), Js('Fred'), Js('Frei'), Js('Frey'), Js('Fri'), Js('Frid'), Js('Fril'), Js('Fro'), Js('Froa'), Js('Frod'), Js('Fru'), Js('Fruk'), Js('Fry'), Js('Fryf'), Js('Frys'), Js('Fur'), Js('Fura'), Js('Ger'), Js('Gerd'), Js('Gis'), Js('Gisl'), Js('Gor'), Js('Gorm'), Js('Gre'), Js('Grei'), Js('Grel'), Js('Grer'), Js('Gret'), Js('Grey'), Js('Gro'), Js('Gros'), Js('Gwe'), Js('Gwen'), Js('Hae'), Js('Hael'), Js('Haem'), Js('Haf'), Js('Hafj'), Js('Ham'), Js('Hama'), Js('Har'), Js('Hara'), Js('Hed'), Js('Hedd'), Js('Hef'), Js('Hefi'), Js('Hel'), Js('Hela'), Js('Helg'), Js('Her'), Js('Herk'), Js('Herm'), Js('Hert'), Js('Hes'), Js('Hest'), Js('Hid'), Js('Hida'), Js('Hil'), Js('Hild'), Js('Hill'), Js('Hilu'), Js('Hjo'), Js('Hjol'), Js('Hjor'), Js('Hjot'), Js('Hod'), Js('Hodd'), Js('Hol'), Js('Holm'), Js('Hor'), Js('Hors'), Js('Hre'), Js('Href'), Js('Hrei'), Js('Hro'), Js('Hroa'), Js('Hrok'), Js('Hror'), Js('Huk'), Js('Huki'), Js('Hul'), Js('Huld'), Js('Hyr'), Js('Hyri'), Js('Idd'), Js('Iddr'), Js('Ign'), Js('Igna'), Js('Ilf'), Js('Ilfh'), Js('Ill'), Js('Illd'), Js('Ims'), Js('Imsi'), Js('Ing'), Js('Inge'), Js('Ingj'), Js('Ingo'), Js('Ingr'), Js('Ingu'), Js('Ion'), Js('Iona'), Js('Irg'), Js('Irgn'), Js('Isg'), Js('Isge'), Js('Jal'), Js('Jala'), Js('Jen'), Js('Jens'), Js('Jof'), Js('Jofr'), Js('Jol'), Js('Jold'), Js('Jor'), Js('Jora'), Js('Jord'), Js('Kar'), Js('Kat'), Js('Katl'), Js('Katr'), Js('Kil'), Js('Kili'), Js('Kir'), Js('Kirs'), Js('Kjo'), Js('Kjol'), Js('Kol'), Js('Kolf'), Js('Lai'), Js('Lail'), Js('Lam'), Js('Lami'), Js('Lie'), Js('Lies'), Js('Lil'), Js('Lill'), Js('Lis'), Js('Lisa'), Js('Lisb'), Js('Lyd'), Js('Lydi'), Js('Lyn'), Js('Lynl'), Js('Mab'), Js('Mabj'), Js('Mac'), Js('Maca'), Js('Mack'), Js('Mae'), Js('Maev'), Js('Mal'), Js('Male'), Js('Mar'), Js('Mare'), Js('Marg'), Js('Mat'), Js('Matl'), Js('Mav'), Js('Mave'), Js('Mer'), Js('Mere'), Js('Mert'), Js('Met'), Js('Mett'), Js('Min'), Js('Mine'), Js('Mjo'), Js('Mjol'), Js('Mor'), Js('Morw'), Js('Nar'), Js('Narr'), Js('Net'), Js('Nett'), Js('Nil'), Js('Nils'), Js('Nja'), Js('Njad'), Js('Nur'), Js('Nura'), Js('Nurn'), Js('Odd'), Js('Oddn'), Js('Ola'), Js('Olav'), Js('Old'), Js('Olda'), Js('Olf'), Js('Olfe'), Js('Olfi'), Js('Ond'), Js('Ondi'), Js('Ori'), Js('Orie'), Js('Orl'), Js('Orla'), Js('Pet'), Js('Petr'), Js('Rak'), Js('Rake'), Js('Ran'), Js('Rang'), Js('Rey'), Js('Reyd'), Js('Rig'), Js('Rige'), Js('Rigm'), Js('Rik'), Js('Rikk'), Js('Rin'), Js('Ring'), Js('Ris'), Js('Risi'), Js('Ron'), Js('Rona'), Js('Ros'), Js('Rost'), Js('Ruk'), Js('Ruki'), Js('Run'), Js('Runa'), Js('Sap'), Js('Sapp'), Js('Ser'), Js('Sera'), Js('Sig'), Js('Sign'), Js('Sigr'), Js('Sil'), Js('Sild'), Js('Sir'), Js('Siri'), Js('Sis'), Js('Siss'), Js('Skj'), Js('Skjo'), Js('Sof'), Js('Sofi'), Js('Son'), Js('Soni'), Js('Sonj'), Js('Sor'), Js('Sorl'), Js('Sot'), Js('Sott'), Js('Sus'), Js('Susa'), Js('Sva'), Js('Svan'), Js('Svar'), Js('Sve'), Js('Sven'), Js('Swa'), Js('Swan'), Js('Syl'), Js('Sylg'), Js('Tek'), Js('Tekl'), Js('Tem'), Js('Temb'), Js('Tha'), Js('Thae'), Js('Thal'), Js('Thr'), Js('Thre'), Js('Thu'), Js('Thun'), Js('Til'), Js('Tild'), Js('Tilm'), Js('Tor'), Js('Torm'), Js('Tov'), Js('Tova'), Js('Ulf'), Js('Ulfr'), Js('Ulr'), Js('Ulri'), Js('Una'), Js('Urs'), Js('Ursi'), Js('Uth'), Js('Uthg'), Js('Val'), Js('Vale'), Js('Vib'), Js('Vibe'), Js('Vig'), Js('Vigd'), Js('Vor'), Js('Vori'), Js('Ygf'), Js('Ygfa'), Js('Yrs'), Js('Yrsa'), Js('Yso'), Js('Ysol')]))
var.put('nm5', Js([Js('a'), Js('aa'), Js('aarn'), Js('al'), Js('alla'), Js('an'), Js('ana'), Js('anna'), Js('ar'), Js('ara'), Js('ard'), Js('ari'), Js('arte'), Js('ba'), Js('bbi'), Js('bet'), Js('bi'), Js('ca'), Js('da'), Js('de'), Js('di'), Js('dil'), Js('ding'), Js('dis'), Js('dir'), Js('do'), Js('dolyn'), Js('dreid'), Js('drika'), Js('dur'), Js('dvild'), Js('e'), Js('eigr'), Js('eke'), Js('eki'), Js('ekke'), Js('el'), Js('ela'), Js('ella'), Js('en'), Js('ena'), Js('ene'), Js('erd'), Js('erica'), Js('eror'), Js('estris'), Js('et'), Js('ete'), Js('ette'), Js('evi'), Js('fa'), Js('finna'), Js('fna'), Js('fnhild'), Js('frida'), Js('frodi'), Js('ga'), Js('garte'), Js('geira'), Js('gela'), Js('gerd'), Js('geth'), Js('gi'), Js('gird'), Js('gja'), Js('gljot'), Js('greir'), Js('gret'), Js('gritte'), Js('gvild'), Js('he'), Js('hi'), Js('hild'), Js('hilde'), Js('hire'), Js('hvir'), Js('i'), Js('ia'), Js('ica'), Js('id'), Js('ida'), Js('ide'), Js('idil'), Js('ie'), Js('if'), Js('igr'), Js('ika'), Js('il'), Js('ild'), Js('ilde'), Js('ilief'), Js('in'), Js('ina'), Js('ine'), Js('ing'), Js('inna'), Js('ior'), Js('ir'), Js('ird'), Js('irek'), Js('is'), Js('ith'), Js('ja'), Js('jaarn'), Js('jard'), Js('je'), Js('jorg'), Js('ka'), Js('ke'), Js('ki'), Js('kja'), Js('kke'), Js('kning'), Js('la'), Js('laith'), Js('lara'), Js('ld'), Js('lda'), Js('lestris'), Js('levi'), Js('lfrodi'), Js('lga'), Js('lgeth'), Js('li'), Js('lia'), Js('lief'), Js('ling'), Js('lith'), Js('ljot'), Js('lka'), Js('ll'), Js('lla'), Js('lod'), Js('logi'), Js('lone'), Js('lver'), Js('ly'), Js('ma'), Js('mgeira'), Js('mir'), Js('mlaith'), Js('mor'), Js('mund'), Js('na'), Js('nd'), Js('ndolyn'), Js('ne'), Js('ng'), Js('nhild'), Js('nhilde'), Js('nhvir'), Js('nir'), Js('nja'), Js('nmund'), Js('nna'), Js('ny'), Js('o'), Js('od'), Js('okning'), Js('old'), Js('one'), Js('or'), Js('org'), Js('orta'), Js('phire'), Js('ra'), Js('rdis'), Js('red'), Js('reid'), Js('reir'), Js('rek'), Js('ret'), Js('ri'), Js('ria'), Js('rica'), Js('rid'), Js('rida'), Js('rika'), Js('rine'), Js('rior'), Js('ritte'), Js('ror'), Js('rta'), Js('rtur'), Js('run'), Js('sa'), Js('se'), Js('sel'), Js('si'), Js('sif'), Js('sine'), Js('ski'), Js('sl'), Js('sla'), Js('ssa'), Js('sta'), Js('steir'), Js('sten'), Js('ta'), Js('te'), Js('teir'), Js('ten'), Js('th'), Js('the'), Js('tild'), Js('tilde'), Js('tla'), Js('tlogi'), Js('tra'), Js('tred'), Js('tta'), Js('tte'), Js('tur'), Js('uki'), Js('un'), Js('und'), Js('ur'), Js('va'), Js('ver'), Js('vild'), Js('wen'), Js('y'), Js('ya'), Js('ydis'), Js('yf')]))
var.put('nm6', Js([Js('sdottir'), Js('dottir')]))
var.put('nm7', Js([Js('Anvil'), Js('Arrow'), Js('Autumn'), Js('Axe'), Js('Banner'), Js('Bear'), Js('Bellow'), Js('Black'), Js('Blue'), Js('Boar'), Js('Bog'), Js('Bold'), Js('Boulder'), Js('Brandy'), Js('Brittle'), Js('Broken'), Js('Bronze'), Js('Cabbage'), Js('Cairn'), Js('Cloud'), Js('Copper'), Js('Corundum'), Js('Crag'), Js('Crossed'), Js('Dark'), Js('Dead'), Js('Death'), Js('Deep'), Js('Doom'), Js('Double'), Js('Dragon'), Js('Drunk'), Js('Drunken'), Js('Dwarf'), Js('Early'), Js('Ebon'), Js('Elf'), Js('Ember'), Js('Fair'), Js('Far'), Js('Fiery'), Js('Fine'), Js('Fire'), Js('Flame'), Js('Flat'), Js('Fog'), Js('Fork'), Js('Free'), Js('Frozen'), Js('Geode'), Js('Ghost'), Js('God'), Js('Gold'), Js('Golden'), Js('Gray'), Js('Green'), Js('Grey'), Js('Hairy'), Js('Hammer'), Js('Hand'), Js('Hard'), Js('Head'), Js('Heart'), Js('Hearth'), Js('Hoarse'), Js('Home'), Js('Honey'), Js('Horse'), Js('Ice'), Js('Iron'), Js('Knot'), Js('Law'), Js('Little'), Js('Lonely'), Js('Long'), Js('Lute'), Js('Maiden'), Js('Milk'), Js('Nail'), Js('Night'), Js('Oaken'), Js('Oath'), Js('Once'), Js('Orc'), Js('Poor'), Js('Pure'), Js('Raven'), Js('Red'), Js('Rich'), Js('Rock'), Js('Round'), Js('Sable'), Js('Salt'), Js('Salty'), Js('Scar'), Js('Secret'), Js('Seven'), Js('Shade'), Js('Shadow'), Js('Shallow'), Js('Short'), Js('Silver'), Js('Smiling'), Js('Snow'), Js('Soul'), Js('Spring'), Js('Star'), Js('Steel'), Js('Stone'), Js('Storm'), Js('Stout'), Js('Strong'), Js('Summer'), Js('Sun'), Js('Swift'), Js('Thrice'), Js('Triple'), Js('Troll'), Js('Twice'), Js('Two'), Js('War'), Js('Wave'), Js('Wet'), Js('Whetted'), Js('White'), Js('Wide'), Js('Wild'), Js('Wind'), Js('Wine'), Js('Winter'), Js('Wolf'), Js('Worm')]))
var.put('nm8', Js([Js('-Anvil'), Js('-Arm'), Js('-Back'), Js('-Bandit'), Js('-Bane'), Js('-Bear'), Js('-Beard'), Js('-Bearer'), Js('-Blade'), Js('-Blood'), Js('-Brand'), Js('-Breaker'), Js('-Breeks'), Js('-Champion'), Js('-Child'), Js('-Chucker'), Js('-Cloak'), Js('-Colossus'), Js('-Crusher'), Js('-Daggers'), Js('-Dawn'), Js('-Defender'), Js('-Drinker'), Js('-Drums'), Js('-Eater'), Js('-Eye'), Js('-Eyes'), Js('-Face'), Js('-Fang'), Js('-Feet'), Js('-Finger'), Js('-Fingers'), Js('-Fire'), Js('-Fist'), Js('-Foot'), Js('-Free'), Js('-Fur'), Js('-Gale'), Js('-Giver'), Js('-Gobler'), Js('-Gut'), Js('-Hair'), Js('-Hammers'), Js('-Hand'), Js('-Hater'), Js('-Head'), Js('-Healer'), Js('-Heart'), Js('-Helm'), Js('-Hewer'), Js('-Hilt'), Js('-Honored'), Js('-Hull'), Js('-Hunter'), Js('-Jumper'), Js('-Killed'), Js('-Killer'), Js('-Knee'), Js('-Leg'), Js('-Legs'), Js('-Liar'), Js('-Light'), Js('-Loom'), Js('-Lute'), Js('-Maiden'), Js('-Master'), Js('-Mouth'), Js('-Mug'), Js('-Nail'), Js('-Nose'), Js('-Outlaw'), Js('-Pierced'), Js('-Plank'), Js('-Pommel'), Js('-Raed'), Js('-Robber'), Js('-Runner'), Js('-Sage'), Js('-Sailer'), Js('-Sayer'), Js('-Seeker'), Js('-Shaper'), Js('-Shield'), Js('-Shifter'), Js('-Shoal'), Js('-Singer'), Js('-Skeever'), Js('-Skinner'), Js('-Smasher'), Js('-Smith'), Js('-Song'), Js('-Sot'), Js('-Spear'), Js('-Spring'), Js('-Stone'), Js('-Strider'), Js('-Sung'), Js('-Sword'), Js('-Swords'), Js('-Tamer'), Js('-Thief'), Js('-Toe'), Js('-Toes'), Js('-Tongue'), Js('-Tooth'), Js('-Torn'), Js('-Trotter'), Js('-Veins'), Js('-Versed'), Js('-Victim'), Js('-Voice'), Js('-Wand'), Js('-Wave'), Js('-Wife'), Js('-Winter'), Js('-Wish'), Js('-Wrecker'), Js('-Scourge'), Js('-Rival'), Js('-Torment'), Js('-Seer'), Js('-Mage'), Js('-Guard')]))
var.put('nm9', Js([Js('Bearclaw'), Js('Blackthorn'), Js('Bloodmouth'), Js('Braggart'), Js('Broken'), Js('Builder'), Js('Bulwark'), Js('Burly'), Js('Buxom'), Js('Colossus'), Js('Cook'), Js('Craven'), Js('Crow'), Js('Curse-Bringer'), Js('Dreamer'), Js('Easterner'), Js('Ebonhand'), Js('Elfkiller'), Js('Farseer'), Js('Flayer'), Js('Fleetfoot'), Js('Greycloak'), Js('Haggard'), Js('Halfhand'), Js('Harrier'), Js('Helmbolg'), Js('Highlander'), Js('Hollowleg'), Js('Ironhand'), Js('Ironkettle'), Js('Laggard'), Js('Lioness'), Js('Long'), Js('Maulhand'), Js('Merkiller'), Js('Nightingale'), Js('Northerner'), Js('Outcast'), Js('Outlaw'), Js('Peacock'), Js('Ravencrone'), Js('Roarer'), Js('Rockbreaker'), Js('Singer'), Js('Six Fingers'), Js('Slayer'), Js('Smith'), Js('Starkad'), Js('Stone'), Js('Stonearm'), Js('Stormcloak'), Js('Stout'), Js('Strong'), Js('Sword-Maiden'), Js('Tallowhand'), Js('Thrallmaster'), Js('Trollsbane'), Js('Walker'), Js('Wanderer'), Js('Warlock'), Js('White'), Js('Whitemane'), Js('Windcaller'), Js('Windrime'), Js('Woodcutter'), Js('Wulfharth'), Js('of Stuhn'), Js('of the Isles'), Js('of the Piercing Eyes'), Js('of the River'), Js('the Bearclaw'), Js('the Blackthorn'), Js('the Blind'), Js('the Bloodmouth'), Js('the Bloody'), Js('the Bold'), Js('the Braggart'), Js('the Broken'), Js('the Builder'), Js('the Bulwark'), Js('the Burly'), Js('the Buxom'), Js('the Calm'), Js('the Candle'), Js('the Cautious'), Js('the Clerk'), Js('the Colossus'), Js('the Contemptible'), Js('the Cook'), Js('the Craven'), Js('the Crow'), Js('the Curse-Bringer'), Js('the Deaf'), Js('the Dreamer'), Js('the Easterner'), Js('the Ebonhand'), Js('the Elfkiller'), Js('the Fair'), Js('the Farseer'), Js('the Fat'), Js('the Fearless'), Js('the Fearsome'), Js('the Feeble'), Js('the Flayer'), Js('the Fleet'), Js('the Frenzied'), Js('the Gentle'), Js('the Giant'), Js('the Gifted'), Js('the Greater'), Js('the Greycloak'), Js('the Haggard'), Js('the Halfhand'), Js('the Halt'), Js('the Harrier'), Js('the Heavy'), Js('the Helmbolg'), Js('the Highlander'), Js('the Hollowleg'), Js('the Huntress'), Js('the Innocent'), Js('the Intrepid'), Js('the Ironhand'), Js('the Ironkettle'), Js('the Kind'), Js('the Knife'), Js('the Laggard'), Js('the Large'), Js('the Lean'), Js('the Lioness'), Js('the Long'), Js('the Long-Sighted'), Js('the Man'), Js('the Maulhand'), Js('the Merkiller'), Js('the Mumbling'), Js('the Naughty'), Js('the Nightingale'), Js('the Northerner'), Js('the Nose'), Js('the Old'), Js('the Outcast'), Js('the Outlaw'), Js('the Peacock'), Js('the Pickled'), Js('the Portly'), Js('the Quiet'), Js('the Rascal'), Js('the Raven'), Js('the Ravencrone'), Js('the Roarer'), Js('the Rockbreaker'), Js('the Rotted'), Js('the Scribe'), Js('the Seal'), Js('the Singer'), Js('the Slayer'), Js('the Smiler'), Js('the Smith'), Js('the Steady'), Js('the Stone'), Js('the Stonearm'), Js('the Stormcloak'), Js('the Stout'), Js('the Strange'), Js('the Strong'), Js('the Sufficient'), Js('the Sweltering'), Js('the Sword-Maiden'), Js('the Tall'), Js('the Tallowhand'), Js('the Thrallmaster'), Js('the Tiny'), Js('the Tongue'), Js('the Trollsbane'), Js('the Ugly'), Js('the Unbroken'), Js('the Unending'), Js('the Unfaithful'), Js('the Unliving'), Js('the Unlucky'), Js('the Unmentioned'), Js('the Unminded'), Js('the Unrestful'), Js('the Unseen'), Js('the Unwavering'), Js('the Unworthy'), Js('the Walker'), Js('the Wanderer'), Js('the Warlock'), Js('the White'), Js('the Whitemane'), Js('the Wicked'), Js('the Wide'), Js('the Wild'), Js('the Willful'), Js('the Windcaller'), Js('the Windrime'), Js('the Withdrawn'), Js('the Woodcutter'), Js('the World-Weary'), Js('the Worm'), Js('the Yellow'), Js('the Younger')]))
var.put('nm10', Js([Js('Ahl'), Js('Al'), Js('Alf'), Js('Alr'), Js('Arg'), Js('As'), Js('Asg'), Js('Bj'), Js('Bjo'), Js('Dj'), Js('Ehr'), Js('Engm'), Js('Enr'), Js('Er'), Js('Fanr'), Js('Fenar'), Js('Fenr'), Js('Fj'), Js('Gj'), Js('Hahr'), Js('Har'), Js('Her'), Js('Ingm'), Js('Ingr'), Js('Jarg'), Js('Jorg'), Js('Jurg'), Js('Kj'), Js('Mj'), Js('Mjor'), Js('Moj'), Js('Sar'), Js('Sohr'), Js('Sor'), Js('Tarb'), Js('Torb'), Js('Torv'), Js('Ulfr'), Js('Ulr')]))
var.put('nm11', Js([Js('aeld'), Js('aen'), Js('ahr'), Js('ahrik'), Js('ald'), Js('alde'), Js('alder'), Js('an'), Js('ander'), Js('aner'), Js('ans'), Js('ar'), Js('arde'), Js('arik'), Js('arike'), Js('arke'), Js('arme'), Js('arn'), Js('arne'), Js('arok'), Js('ehr'), Js('eld'), Js('en'), Js('enr'), Js('ens'), Js('ensve'), Js('er'), Js('ervon'), Js('ifk'), Js('ik'), Js('ikver'), Js('is'), Js('isor'), Js('isver'), Js('orin'), Js('orke'), Js('orn'), Js('orne')]))
pass
pass


# Add lib to the module scope
nordNames = var.to_python()
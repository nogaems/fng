__all__ = ['slovakNames']

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
    var.registers(['nm1', 'nm4', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Ľuboš'), Js('Ľubomír'), Js('Šimon'), Js('Štefan'), Js('Žigmund'), Js('Adam'), Js('Aleš'), Js('Alexander'), Js('Alexej'), Js('Alojz'), Js('Andrej'), Js('Augustín'), Js('Aurel'), Js('Bartolomej'), Js('Benjamín '), Js('Blažej'), Js('Bohumír'), Js('Bohumil'), Js('Bohuslav'), Js('Branislav'), Js('Branko'), Js('Bronislav'), Js('Ctirad'), Js('Cyril'), Js('Dávid'), Js('Dalibor'), Js('Dalimil'), Js('Daniel'), Js('Denis'), Js('Dionýz'), Js('Dominik'), Js('Drahoslav'), Js('Dušan'), Js('Eduard'), Js('Erik'), Js('Eugen'), Js('Filip'), Js('Gabriel'), Js('Gregor'), Js('Havel'), Js('Henrich'), Js('Imrich'), Js('Ivan'), Js('Ján'), Js('Július'), Js('Jakub'), Js('Janko'), Js('Jaroslav'), Js('Jonáš'), Js('Jozef'), Js('Juraj'), Js('Kajetán'), Js('Kamil'), Js('Karol'), Js('Kazimír'), Js('Klement'), Js('Koloman'), Js('Konrád'), Js('Kornel'), Js('Krištof'), Js('Ladislav'), Js('Lukáš'), Js('Marcel'), Js('Marek'), Js('Marián'), Js('Martin'), Js('Matúš'), Js('Matej'), Js('Maximilián'), Js('Metod'), Js('Michal'), Js('Mikuláš'), Js('Milan'), Js('Miloš'), Js('Miloslav'), Js('Mirek'), Js('Miroslav'), Js('Oldrich'), Js('Oliver'), Js('Ondrej'), Js('Patrik'), Js('Pavol'), Js('Peter'), Js('Radovan'), Js('René'), Js('Riško'), Js('Rišo'), Js('Richard'), Js('Robert'), Js('Roman'), Js('Samuel'), Js('Silvester'), Js('Slavomír'), Js('Stanislav'), Js('Tadeáš'), Js('Teodor'), Js('Tibor'), Js('Timotej'), Js('Tomáš'), Js('Václav'), Js('Vít'), Js('Valentín'), Js('Vavrinec'), Js('Vendelín'), Js('Viktor'), Js('Viliam'), Js('Vincent'), Js('Vladan'), Js('Vladimír'), Js('Vladislav'), Js('Vlado'), Js('Vojtech'), Js('Vratislav'), Js('Zdenko'), Js('Zdeno')]))
    var.put('nm2', Js([Js('Štefánia'), Js('Žofia'), Js('Adriana'), Js('Agnesa'), Js('Alžbeta'), Js('Albína'), Js('Alena'), Js('Alexandra'), Js('Alica'), Js('Alojzia'), Js('Amália'), Js('Anastázia'), Js('Andrea'), Js('Angela'), Js('Angelika'), Js('Anna'), Js('Antónia'), Js('Apolena'), Js('Barbora'), Js('Beáta'), Js('Blanka'), Js('Božena'), Js('Braňka'), Js('Branislava'), Js('Bronislava'), Js('Cecília'), Js('Dagmar'), Js('Dana'), Js('Danica'), Js('Daniela'), Js('Danka'), Js('Darina'), Js('Denisa'), Js('Dominika'), Js('Dorota'), Js('Dušana'), Js('Edita'), Js('Elena'), Js('Eliška'), Js('Emília'), Js('Ema'), Js('Estera'), Js('Eulália'), Js('Eva'), Js('Gabriela'), Js('Gertrúda'), Js('Hana'), Js('Hedviga'), Js('Helena'), Js('Imriška'), Js('Iva'), Js('Ivana'), Js('Ivanka'), Js('Iveta'), Js('Ivka'), Js('Ivona'), Js('Júlia'), Js('Jana'), Js('Janka'), Js('Jarmila'), Js('Jaroslava'), Js('Jela'), Js('Jolana'), Js('Jozefína'), Js('Judita'), Js('Justína'), Js('Kamila'), Js('Katarína'), Js('Katka'), Js('Klára'), Js('Klaudia'), Js('Kristína'), Js('Lýdia'), Js('Ladislava'), Js('Lenka'), Js('Linda'), Js('Luba'), Js('Lubica'), Js('Lucia'), Js('Mária'), Js('Margita'), Js('Marianna'), Js('Marika'), Js('Markéta'), Js('Marta'), Js('Martina'), Js('Melánia'), Js('Michaela'), Js('Miroslava'), Js('Monika'), Js('Nadežda'), Js('Natália'), Js('Nela'), Js('Nikola'), Js('Nina'), Js('Olívia'), Js('Olga'), Js('Patka'), Js('Patrícia'), Js('Paulína'), Js('Petra'), Js('Petronela'), Js('Renáta'), Js('Romana'), Js('Sára'), Js('Silvia'), Js('Simona'), Js('Soňa'), Js('Sofia'), Js('Stanislava'), Js('Svetlana'), Js('Tamara'), Js('Tatiana'), Js('Terézia'), Js('Valéria'), Js('Valentína'), Js('Vanda'), Js('Vanesa'), Js('Veronika'), Js('Viktória'), Js('Vilma'), Js('Vladimíra'), Js('Zita'), Js('Zlata'), Js('Zlatica'), Js('Zorka'), Js('Zuza'), Js('Zuzana'), Js('Zuzanka'), Js('Zuzka')]))
    var.put('nm3', Js([Js('Čížik'), Js('Čiernik'), Js('Čierny'), Js('Řezník'), Js('Šťastný'), Js('Široký'), Js('Bača'), Js('Baník'), Js('Bartoš'), Js('Biely'), Js('Biskup'), Js('Bosko'), Js('Chren'), Js('Chrobák'), Js('Cibuľka'), Js('Cuda'), Js('Dobrovodský'), Js('Doležal'), Js('Dolina'), Js('Hodža'), Js('Holič'), Js('Holub'), Js('Hornick'), Js('Hornik'), Js('Ján'), Js('Jahoda'), Js('Jankovic'), Js('Jelen'), Js('Kľúčiar'), Js('Kočiš'), Js('Kocur'), Js('Kolar'), Js('Koleno'), Js('Komár'), Js('Koreň'), Js('Kostra'), Js('Kováč'), Js('Kovac'), Js('Kráľ'), Js('Križ'), Js('Kuchár'), Js('Láska'), Js('Mäsiar'), Js('Malý'), Js('Maliar'), Js('Malina'), Js('Mečiar'), Js('Medvedík'), Js('Medved'), Js('Mlynár'), Js('Mokrý'), Js('Mráz'), Js('Nedved'), Js('Novák'), Js('Otčenáš'), Js('Pekár'), Js('Pokorny'), Js('Rybár'), Js('Skalicky'), Js('Sklenár'), Js('Slaný'), Js('Slavik'), Js('Smutný'), Js('Strnad'), Js('Suchý'), Js('Surový'), Js('Tesar'), Js('Tesarik'), Js('Tichý'), Js('Zima')]))
    var.put('nm4', Js([Js('Čiliaká'), Js('Čiliaková'), Js('Šafařiková'), Js('Šafiřiká'), Js('Bartá'), Js('Bartková'), Js('Bellá'), Js('Bellová'), Js('Bláhá'), Js('Bláhová'), Js('Bottá'), Js('Bottoca'), Js('Chlebovcá'), Js('Chlebovcová'), Js('Cudová'), Js('Grgasá'), Js('Grgasová'), Js('Hodžová'), Js('Hrljacá'), Js('Hrljacová'), Js('Jánošíká'), Js('Jánošíková'), Js('Jilemničká'), Js('Jillemničková'), Js('Kočišová'), Js('Koleničká'), Js('Koleničková'), Js('Kollará'), Js('Kollarová'), Js('Kostrová'), Js('Kováčová'), Js('Kráľová'), Js('Lucáčá'), Js("Lucáčov'"), Js('Mišurá'), Js('Mišurová'), Js('Novomedská'), Js('Novomedsková'), Js('Orszaghá'), Js('Orszaghova'), Js('Paučulá'), Js('Paučuloá'), Js('Pivovarčá'), Js('Pivovarčová'), Js('Razusá'), Js('Razusová'), Js('Repká'), Js('Repková'), Js('Smreká'), Js('Smreková'), Js('Turošíká'), Js('Turošíkova'), Js('Urbaná'), Js('Urbanová'), Js('Vajanská'), Js('Vajanskvá'), Js('Záhorecá'), Js('Záhorecová')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm4').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
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
slovakNames = var.to_python()
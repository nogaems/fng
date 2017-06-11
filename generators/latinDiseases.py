__all__ = ['latinDiseases']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'nm3', 'result', 'nm4'])
    var.put('nm1', Js([Js([Js('Abscessus'), Js('Abscess')]), Js([Js('Accessio'), Js('Seizure')]), Js([Js('Agonia'), Js('Cramps')]), Js([Js('Ambustio'), Js('Burn')]), Js([Js('Aneurisma'), Js('Aneurysm')]), Js([Js('Angina'), Js('Chest pain')]), Js([Js('Apoplexia'), Js('Stroke')]), Js([Js('Asthenia'), Js('Atrophy')]), Js([Js('Ataxia'), Js('Ataxia')]), Js([Js('Atrophia'), Js('Atrophy')]), Js([Js('Calculus'), Js('Stones')]), Js([Js('Cancrum'), Js('Canker')]), Js([Js('Carbunculus'), Js('Carbuncle')]), Js([Js('Carcinoma'), Js('Cancer')]), Js([Js('Catarrhus'), Js('Catarrh')]), Js([Js('Cholerica'), Js('Cholera')]), Js([Js('Chorea'), Js('Dance')]), Js([Js('Colica'), Js('Colic')]), Js([Js('Commotio'), Js('Concussion')]), Js([Js('Contracture'), Js('Stricture')]), Js([Js('Contuses'), Js('Bruised')]), Js([Js('Contusio'), Js('Contusion')]), Js([Js('Convulsio'), Js('Convulsion')]), Js([Js('Convulsionis'), Js('Convulsions')]), Js([Js('Crampus'), Js('Cramps')]), Js([Js('Debilitas'), Js('Weakness')]), Js([Js('Dolor'), Js('Pain')]), Js([Js('Ecclampsia'), Js('Convulsions')]), Js([Js('Exhaustio'), Js('Exhaustion')]), Js([Js('Explosio'), Js('Explosion')]), Js([Js('Fatuitas'), Js('Idiocy')]), Js([Js('Febris'), Js('Fever')]), Js([Js('Fracture'), Js('Fracture')]), Js([Js('Fulmen'), Js('Lightning')]), Js([Js('Galbanus'), Js('Jaundice')]), Js([Js('Gangraena'), Js('Gangrene')]), Js([Js('Gelatio'), Js('Frost')]), Js([Js('Glarea'), Js('Gravel')]), Js([Js('Haemorrhagia'), Js('Hemorrhage')]), Js([Js('Haemorrhois'), Js('Hemorrhoids')]), Js([Js('Hydrocephalus'), Js('Hydrocephalus')]), Js([Js('Hydropisis'), Js('Dropsis')]), Js([Js('Hydrops'), Js('Dropsis')]), Js([Js('Ictus'), Js('Trauma')]), Js([Js('Ignis'), Js('Burning')]), Js([Js('Infectio'), Js('Infection')]), Js([Js('Infirmus'), Js('Weak')]), Js([Js('Inflammatio'), Js('Inflammation')]), Js([Js('Intessusceptio'), Js('Intussusception')]), Js([Js('Lepra'), Js('Leprosy')]), Js([Js('Marasmus'), Js('Weakness')]), Js([Js('Mollities'), Js('Softening')]), Js([Js('Morbilli'), Js('Measles')]), Js([Js('Morbus'), Js('Disease')]), Js([Js('Mors'), Js('Death')]), Js([Js('Myelitis'), Js('Paraplegia')]), Js([Js('Noctis'), Js('of the Night')]), Js([Js('Noma'), Js('Canker')]), Js([Js('Obitus'), Js('Death')]), Js([Js('Obstructiones'), Js('Obstruction')]), Js([Js('Otitis'), Js('Inflammation')]), Js([Js('Peritus'), Js('Deceased')]), Js([Js('Perniciose'), Js('Pernicious')]), Js([Js('Pestis'), Js('Plague')]), Js([Js('Phthisis'), Js('Consumption')]), Js([Js('Plaga'), Js('Plague')]), Js([Js('Pleuritis'), Js('Pleuritis')]), Js([Js('Privatio'), Js('Priviation')]), Js([Js('Rheumatismus'), Js('Rheumatism')]), Js([Js('Scophulosis'), Js('Scrofula')]), Js([Js('Scorbutus'), Js('Scurvy')]), Js([Js('Senilis'), Js('Weakness')]), Js([Js('Spasmus'), Js('Spasms')]), Js([Js('Tussis'), Js('Cough')]), Js([Js('Ulcus'), Js('Ulcer')]), Js([Js('Venenatio'), Js('Poisoning')]), Js([Js('Vermis'), Js('Worms')]), Js([Js('Vitium'), Js('Disease')])]))
    var.put('nm2', Js([Js([Js('Abdmonis'), Js('Abdominal')]), Js([Js('Abdominalis'), Js('Abdominal')]), Js([Js('Acerbus'), Js('Sharp')]), Js([Js('Agita'), Js('Shaking')]), Js([Js('Alvus'), Js('Belly')]), Js([Js('Articulorum'), Js('Joint')]), Js([Js('Bracium'), Js('Arm')]), Js([Js('Caput'), Js('Head')]), Js([Js('Cerebralis'), Js('Cerebrum')]), Js([Js('Cerebri'), Js('Brain')]), Js([Js('Cerebri'), Js('Cerebral')]), Js([Js('Clarus'), Js('Clear')]), Js([Js('Collum'), Js('Neck')]), Js([Js('Cordis'), Js('Heart')]), Js([Js('Coxa'), Js('Hip')]), Js([Js('Cutis'), Js('Skin')]), Js([Js('Dentes'), Js('Teeth')]), Js([Js('Dextra'), Js('Right')]), Js([Js('Epiglottidis'), Js('Eppiglotis')]), Js([Js('Flava'), Js('Yellow')]), Js([Js('Flores'), Js('Flower')]), Js([Js('Folia'), Js('Leaf')]), Js([Js('Frigor'), Js('Cold')]), Js([Js('Fuscus'), Js('Brown')]), Js([Js('Fuscus'), Js('Dark')]), Js([Js('Glottidis'), Js('Glottis')]), Js([Js('Hectica'), Js('Hectic')]), Js([Js('Hirudo'), Js('Leech')]), Js([Js('Ilii'), Js('Ilium')]), Js([Js('Incisum'), Js('Cut')]), Js([Js('Incognita'), Js('Unidentified')]), Js([Js('Infantilis'), Js('Infantile')]), Js([Js('Inflammatoria'), Js('Inflammatory')]), Js([Js('Intermittens'), Js('Intermittent')]), Js([Js('Jecoris'), Js('Liver')]), Js([Js('Laceratum'), Js('Lacerated')]), Js([Js('Laryngea'), Js('Larynx')]), Js([Js('Luteus'), Js('Yellow')]), Js([Js('Magnus'), Js('Mighty')]), Js([Js('Membranacea'), Js('Membrane')]), Js([Js('Motus'), Js('Locomotion')]), Js([Js('Nervosa'), Js('Nervous')]), Js([Js('Niger'), Js('Black')]), Js([Js('Molle'), Js('Soft')]), Js([Js('Mollis'), Js('Soft')]), Js([Js('Os'), Js('Mouth')]), Js([Js('Ovarii'), Js('Ovarian')]), Js([Js('Pancreatis'), Js('Pancreas')]), Js([Js('Pectus'), Js('Breast')]), Js([Js('Pedicularis'), Js('Louse')]), Js([Js('Pes'), Js('Foot')]), Js([Js('Petechialis'), Js('Spotted')]), Js([Js('Prostata'), Js('Prostate')]), Js([Js('Puerperalis'), Js('Puerperal')]), Js([Js('Pulmonum'), Js('Lung')]), Js([Js('Punctum'), Js('Stabbed')]), Js([Js('Putrida'), Js('Rotten')]), Js([Js('Remittens'), Js('Remittent')]), Js([Js('Rheumatica'), Js('Rheumatic')]), Js([Js('Rubra'), Js('Scarlet')]), Js([Js('Rumen'), Js('Throat')]), Js([Js('Siccus'), Js('Dry')]), Js([Js('Spissus'), Js('Dense')]), Js([Js('Sacer'), Js('Sacred')]), Js([Js('Senilis'), Js('Dry')]), Js([Js('Vulnus'), Js('Wounded')]), Js([Js('Ustus'), Js('Burnt')]), Js([Js('Sinistra'), Js('Left')]), Js([Js('Tonsillaris'), Js('Tonsils')]), Js([Js('Ulna'), Js('Arm')]), Js([Js('Ulna'), Js('Elbow')]), Js([Js('Uteri'), Js('Uterus')]), Js([Js('Ventriculi'), Js('Stomach')]), Js([Js('Verminosa'), Js('Verminous')]), Js([Js('Astuosa'), Js('Hot')]), Js([Js('Aquaticum'), Js('Aquatic')]), Js([Js('Arenosum'), Js('Sandy')]), Js([Js('Candidulum'), Js('Shining')]), Js([Js('Cavum'), Js('Hollow')]), Js([Js('Cerritum'), Js('Frantic')])]))
    var.put('nm3', Js([Js('Ab'), Js('Absce'), Js('Acce'), Js('Ago'), Js('Am'), Js('Ambu'), Js('Aneu'), Js('Angi'), Js('Apo'), Js('As'), Js('Asthe'), Js('Atro'), Js('Ca'), Js('Cal'), Js('Calcu'), Js('Can'), Js('Car'), Js('Carbu'), Js('Cata'), Js('Cho'), Js('Chole'), Js('Co'), Js('Coli'), Js('Commo'), Js('Con'), Js('Contra'), Js('Contu'), Js('Convu'), Js('Cra'), Js('Cram'), Js('Debi'), Js('Do'), Js('Eccla'), Js('Ex'), Js('Explo'), Js('Fa'), Js('Fatui'), Js('Fe'), Js('Fi'), Js('Fra'), Js('Ga'), Js('Gal'), Js('Galba'), Js('Gela'), Js('Gla'), Js('Haemo'), Js('Hy'), Js('Hydro'), Js('In'), Js('Infe'), Js('InfiInfla'), Js('Inte'), Js('Intes'), Js('Le'), Js('Ma'), Js('Mara'), Js('Molli'), Js('Mor'), Js('Morbi'), Js('Mye'), Js('Noc'), Js('Peri'), Js('Perni'), Js('Pes'), Js('Phthi'), Js('Pla'), Js('Pleu'), Js('Pri'), Js('Priva'), Js('Rheu'), Js('Sco'), Js('Scophu'), Js('Scor'), Js('Se'), Js('Seni'), Js('Spa'), Js('Spas'), Js('Tu'), Js('Ve'), Js('Vene'), Js('Ver'), Js('Vi')]))
    var.put('nm4', Js([Js('banus'), Js('bus'), Js('cinoma'), Js('ciose'), Js('crum'), Js('culus'), Js('cus'), Js('drops'), Js('fectio'), Js('firmus'), Js('ga'), Js('gina'), Js('graena'), Js('hagia'), Js('li'), Js('lica'), Js('lis'), Js('litas'), Js('lities'), Js('litis'), Js('lor'), Js('losis'), Js('lus'), Js('ma'), Js('matio'), Js('men'), Js('mis'), Js('motio'), Js('mus'), Js('natio'), Js('nia'), Js('nis'), Js('noma'), Js('nus'), Js('phalus'), Js('phia'), Js('pisis'), Js('plexia'), Js('pus'), Js('ra'), Js('rea'), Js('rhagia'), Js('rhus'), Js('rica'), Js('ris'), Js('risma'), Js('ritis'), Js('sceptio'), Js('ses'), Js('sia'), Js('sio'), Js('sionis'), Js('sis'), Js('sus'), Js('tas'), Js('ties'), Js('tio'), Js('tiones'), Js('tis'), Js('tismus'), Js('tium'), Js('ture'), Js('tus'), Js('tuses'), Js('vatio'), Js('xia')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((((((var.get('nm1').get(var.get('rnd')).get('0')+Js(' '))+var.get('nm2').get(var.get('rnd2')).get('0'))+Js(' ('))+var.get('nm2').get(var.get('rnd2')).get('1'))+Js(' '))+var.get('nm1').get(var.get('rnd')).get('1'))+Js(')')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                while PyJsStrictEq(var.get('rnd'),var.get('rnd3')):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                while PyJsStrictEq(var.get('rnd2'),var.get('rnd4')):
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
                var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm3').callprop('splice', var.get('rnd3'), Js(1.0))
                var.get('nm4').callprop('splice', var.get('rnd2'), Js(1.0))
                var.get('nm4').callprop('splice', var.get('rnd4'), Js(1.0))
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
latinDiseases = var.to_python()
__all__ = ['diseaseNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aggressive'), Js('Agitated'), Js('Agony'), Js('Aggressive'), Js('Ancient'), Js('Angel'), Js('Angry'), Js('Animated'), Js('Anxious'), Js('Arachnid'), Js('Autumn'), Js('Avian'), Js('Bacterial'), Js('Banshee'), Js('Beer'), Js('Black'), Js('Boar'), Js('Brain'), Js('Brittle'), Js('Buzzing'), Js('Canine'), Js('Cat'), Js('Cave'), Js('Chicken'), Js('Chilling'), Js('Cold'), Js('Collapsing'), Js('Contagious'), Js('Cow'), Js('Crazy'), Js('Creeping'), Js('Crippling'), Js('Crumbling'), Js('Crying'), Js('Crystal'), Js('Curable'), Js('Deadly'), Js("Death's"), Js('Deathbell'), Js('Decaying'), Js('Delirious'), Js('Demon'), Js('Desert'), Js('Desolation'), Js('Deteriorating'), Js("Devil's"), Js('Dog'), Js('Dragon'), Js('Dream'), Js('Dreaming'), Js('Duck'), Js('Dwarf'), Js('Dying'), Js('Elastic'), Js('Elephant'), Js('Enlarged'), Js('Ethereal'), Js('Exhausting'), Js('Explosive'), Js('Fading'), Js('Failing'), Js('Fall'), Js('Falling'), Js('Fatal'), Js('Feline'), Js('Fickle'), Js('Fiery'), Js("Fisherman's"), Js('Flower'), Js('Forceful'), Js('Forest'), Js('Frenzied'), Js('Frost'), Js('Frozen'), Js('Ghastly'), Js('Ghost'), Js('Goblin'), Js('Golden'), Js('Goose'), Js('Grave'), Js('Green'), Js('Growing'), Js('Guttural'), Js('Happy'), Js('Harmless'), Js("Heaven's"), Js('Hell'), Js('Hellish'), Js('Hiccup'), Js('Hopeless'), Js('Horse'), Js('Hostile'), Js('Hot'), Js('Humming'), Js('Hyper'), Js('Icy'), Js('Immobilizing'), Js('Impossible'), Js('Incurable'), Js('Intense'), Js('Iron'), Js('Ironbark'), Js('Island'), Js('Jumping'), Js('Jungle'), Js("King's"), Js('Lady'), Js('Laughing'), Js('Lifeless'), Js('Limp'), Js('Lion'), Js('Lizard'), Js('Man'), Js('Marsh'), Js('Memory'), Js('Mild'), Js('Milk'), Js('Mortal'), Js('Mountain'), Js('Mouse'), Js('Necrotic'), Js('Nervous'), Js('Numb'), Js('Numbing'), Js('Ogre'), Js('Orange'), Js('Pale'), Js('Paralyzing'), Js('Peaceful'), Js('Permanent'), Js('Pestilent'), Js('Petrifying'), Js('Phantom'), Js('Pig'), Js('Pink'), Js('Pygmy'), Js("Queen's"), Js('Quiet'), Js('Quivering'), Js('Rabbit'), Js('Rabid'), Js('Rasping'), Js('Rat'), Js('Red'), Js('Restless'), Js('Rickety'), Js('Rock'), Js('Rodent'), Js('Rooster'), Js('Rotting'), Js('Running'), Js('Sage'), Js('Screaming'), Js('Sedated'), Js('Serpent'), Js('Shadow'), Js('Shaking'), Js('Shaky'), Js('Sheep'), Js('Shivering'), Js('Shriveling'), Js('Silent'), Js('Silver'), Js('Sinister'), Js('Sleep'), Js('Smiling'), Js('Snake'), Js('Sniffeling'), Js('Soft'), Js('Soul'), Js('Spastic'), Js('Spider'), Js('Spine'), Js('Spirit'), Js('Spring'), Js('Steel'), Js('Sterile'), Js('Stiff'), Js('Stiffening'), Js('Stimulated'), Js('Stinging'), Js('Stomach'), Js("Stranger's"), Js('Stressed'), Js('Stressful'), Js('Stunned'), Js('Summer'), Js('Swamp'), Js('Swine'), Js('Temporary'), Js('Terrifying'), Js('Thorny'), Js('Ticklish'), Js('Tiring'), Js('Tomb'), Js('Tranquil'), Js('Tree'), Js('Trembling'), Js('Trivial'), Js('Twitching'), Js('Ugly'), Js('Undead'), Js('Vein'), Js('Violet'), Js('Volatile'), Js('Warping'), Js('Water'), Js('Weak'), Js('Weakening'), Js('Whispering'), Js('Wicked'), Js('Wild'), Js('Winter'), Js('Wired'), Js('Witch'), Js('Withering'), Js('Wizard'), Js('Wolf'), Js('Wooden'), Js('Worn'), Js('Wraith'), Js('Yellow'), Js('Zombie')]))
var.put('nm2', Js([Js('Ache'), Js('Aching'), Js('Acne'), Js('Allergy'), Js('Amnesia'), Js('Anemia'), Js('Anthrax'), Js('Anxiety'), Js('Arthritis'), Js('Asthma'), Js('Baldness'), Js('Blight'), Js('Blindness'), Js('Blisters'), Js('Body'), Js('Bones'), Js('Bronchitis'), Js('Cancer'), Js('Cannibalism'), Js('Chills'), Js('Chlamydia'), Js('Cholera'), Js('Cold'), Js('Cough'), Js('Cramps'), Js('Deafness'), Js('Death'), Js('Decay'), Js('Deficiency'), Js('Dehydration'), Js('Delirium'), Js('Delusion'), Js('Delusions'), Js('Depression'), Js('Diptheria'), Js('Disease'), Js('Dysfunctions'), Js('Ears'), Js('Ebola'), Js('Epilepsy'), Js('Euphoria'), Js('Eye'), Js('Eyes'), Js('Fatigue'), Js('Feet'), Js('Fever'), Js('Finger'), Js('Flu'), Js('Foot'), Js('Gangrene'), Js('Gonorrhea'), Js('Hallucinations'), Js('Hands'), Js('Head'), Js('Heart'), Js('Hepatitis'), Js('Herpes'), Js('Illness'), Js('Infection'), Js('Infertility'), Js('Inflammation'), Js('Influenza'), Js('Insanity'), Js('Insomnia'), Js('Intolerance'), Js('Irritation'), Js('Leprosy'), Js('Lupus'), Js('Malaria'), Js('Measles'), Js('Meningitis'), Js('Migraine'), Js('Mouth'), Js('Mutation'), Js('Nausea'), Js('Nose'), Js('Panic'), Js('Paralysis'), Js('Paranoia'), Js('Parasite'), Js('Plague'), Js('Pneumonia'), Js('Poisoning'), Js('Pox'), Js('Rabies'), Js('Rage'), Js('Rash'), Js('Salmonella'), Js('Scarring'), Js('Schizophrenia'), Js('Scurvy'), Js('Shock'), Js('Skin'), Js('Sleep Disorder'), Js('Sneeze'), Js('Soreness'), Js('Sores'), Js('Spasms'), Js('Stiffness'), Js('Stomach'), Js('Swelling'), Js('Syndrome'), Js('Syphilis'), Js('Tetanus'), Js('Throat'), Js('Tongue'), Js('Tumor'), Js('Ulcers'), Js('Vampirism'), Js('Virus'), Js('Warts')]))
pass
pass


# Add lib to the module scope
diseaseNames = var.to_python()
__all__ = ['pokemonDescriptions']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['fairyWings', 'fightMouth', 'rockLegs', 'steelEars', 'bugLegs', 'darkMouth', 'rockEars', 'fairyHorns', 'dragonWings', 'groundAttk', 'grassSkin', 'fightSnout', 'iceMouth', 'grassHorns', 'grassWings', 'normLegs', 'placeDragon', 'fightWings', 'evo', 'elecSkin', 'groundLegs', 'poisonArms', 'poisonSnout', 'steelArms', 'placeBug', 'psyTail', 'steelSkin', 'placePsychic', 'fairyArms', 'bugWings', 'poisonBeak', 'waterEars', 'flyBeak', 'placePoison', 'normalAttk', 'psyWings', 'fairyBeak', 'placeFire', 'rockMouth', 'fairyEars', 'waterMouth', 'flyMouth', 'dragonEars', 'psySnout', 'ghostWings', 'fairyTail', 'poisonEars', 'bugAttk', 'normSnout', 'groundHorns', 'fightingAttk', 'darkBeak', 'rsm', 'ghostHorns', 'poisonTail', 'bugArms', 'flyHorns', 'rockArms', 'placeDark', 'dragonHorns', 'grassMouth', 'rockTail', 'ghostSkin', 'fairyMouth', 'groundTail', 'poisonLegs', 'fightLegs', 'waterSkin', 'bugSkin', 'normTail', 'grassTail', 'poisonSkin', 'groundArms', 'psyMouth', 'fairySnout', 'flyWings', 'normArms', 'dragonSkin', 'bugMouth', 'waterLegs', 'grassAttk', 'normEars', 'darkWings', 'flyEars', 'grassEars', 'psyLegs', 'elecArms', 'darkSnout', 'psySkin', 'amnt', 'iceHorns', 'ghostLegs', 'iceEars', 'iceBeak', 'groundMouth', 'placeSteel', 'placeGround', 'darkTail', 'normMouth', 'ghostArms', 'nameGen', 'elecBeak', 'psyEars', 'steelSnout', 'waterSnout', 'fightSkin', 'psyBeak', 'grassLegs', 'darkHorns', 'elecSnout', 'drg', 'groundBeak', 'flyLegs', 'flySkin', 'dragonLegs', 'ghostEars', 'steelAttk', 'dragonTail', 'placeFairy', 'lnd', 'ghostBeak', 'poisonMouth', 'psyArms', 'fightTail', 'darkLegs', 'steelLegs', 'fireSnout', 'electricAttk', 'placeFlying', 'steelMouth', 'fairyAttk', 'fireWings', 'fairyLegs', 'darkSkin', 'fightHorns', 'ghostAttk', 'waterArms', 'elecTail', 'waterHorns', 'normBeak', 'waterBeak', 'bug', 'fireSkin', 'steelWings', 'steelTail', 'psyHorns', 'rockHorns', 'dragonMouth', 'rockAttk', 'fireLegs', 'placeNormal', 'fightArms', 'rockSnout', 'fireMouth', 'rockBeak', 'pers', 'darkArms', 'placeElectric', 'air', 'placeWater', 'fireEars', 'iceAttk', 'dragonArms', 'iceSkin', 'steelHorns', 'iceLegs', 'groundSnout', 'waterWings', 'elecWings', 'iceTail', 'ghostSnout', 'grassBeak', 'placeGrass', 'fightEars', 'placeRock', 'fightBeak', 'normWings', 'psychicAttk', 'grassSnout', 'iceArms', 'dragonAttk', 'darkAttk', 'groundEars', 'placeIce', 'wtr', 'rockSkin', 'elecEars', 'fairySkin', 'poisonWings', 'fireTail', 'flyingAttk', 'normSkin', 'ghostMouth', 'flyTail', 'fireBeak', 'steelBeak', 'waterAttk', 'normHorns', 'iceSnout', 'placeFighting', 'darkEars', 'poisonHorns', 'waterTail', 'placeGhost', 'poisonAttk', 'flyFeathers', 'elecLegs', 'iceWings', 'elecMouth', 'fireAttk', 'groundSkin', 'elecHorns', 'fireArms', 'fireHorns', 'ghostTail', 'grassArms'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['rnRsm', 'result', 'pkType', 'br', 'traits', 'name', 'rnEvo', 'name2', 'name3', 'pkm', 'descrs', 'rnAmnt', 'rnd1', 'rnPers', 'rnd2'])
    var.put('pkm', Js([Js([Js('an aardvark'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('an albatross'), Js([Js('air'), Js('water')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('an alligator'), Js([Js('land'), Js('water')]), Js([Js('skin'), Js('scales')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('none')]), Js([Js('an alpaca'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('an ant'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('an anteater'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('an antelope'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('an ape'), Js([Js('land')]), Js([Js('skin'), Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('an armadillo'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a baboon'), Js([Js('land')]), Js([Js('skin'), Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('a badger'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a barracuda'), Js([Js('water')]), Js([Js('scales')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a bat'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('a bear'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a beaver'), Js([Js('land'), Js('water')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a bee'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a bird'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a bison'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a boar'), Js([Js('land')]), Js([Js('skin'), Js('hide')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a buffalo'), Js([Js('land'), Js('water')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a butterfly'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a camel'), Js([Js('land')]), Js([Js('hide')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a caribou'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a cassowary'), Js([Js('air'), Js('land')]), Js([Js('feathers')]), Js([Js('legs'), Js('wings')]), Js('beak'), Js('none'), Js('none')]), Js([Js('a cat'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a caterpillar'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a cheetah'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a chicken'), Js([Js('air'), Js('land')]), Js([Js('feathers')]), Js([Js('legs'), Js('wings')]), Js('beak'), Js('none'), Js('none')]), Js([Js('a chimpanzee'), Js([Js('land')]), Js([Js('skin'), Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('a chinchilla'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a cobra'), Js([Js('land')]), Js([Js('skin'), Js('scales')]), Js([Js('body')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a cockroach'), Js([Js('land')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a cod'), Js([Js('water')]), Js([Js('scales')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a cow'), Js([Js('land')]), Js([Js('skin'), Js('hide')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a coyote'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a crab'), Js([Js('land'), Js('water')]), Js([Js('armor')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a crane'), Js([Js('air'), Js('land'), Js('water')]), Js([Js('feathers')]), Js([Js('legs'), Js('wings')]), Js('beak'), Js('none'), Js('none')]), Js([Js('a crocodile'), Js([Js('land'), Js('water')]), Js([Js('skin'), Js('scales')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a crow'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a deer'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('horns')]), Js([Js('a dinosaur'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('none')]), Js([Js('a dog'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a dolphin'), Js([Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a donkey'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a dove'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a dragonfly'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a duck'), Js([Js('air'), Js('land'), Js('water')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('an eagle'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('an eel'), Js([Js('water')]), Js([Js('skin')]), Js([Js('body')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('an eland'), Js([Js('land')]), Js([Js('skin'), Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('horns')]), Js([Js('an elephant'), Js([Js('land'), Js('water')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('an elk'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('an emu'), Js([Js('air'), Js('land')]), Js([Js('feathers')]), Js([Js('legs'), Js('wings')]), Js('beak'), Js('none'), Js('none')]), Js([Js('a falcon'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a ferret'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a fish'), Js([Js('water')]), Js([Js('scales')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a flamingo'), Js([Js('air'), Js('land'), Js('water')]), Js([Js('feathers')]), Js([Js('legs'), Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a fly'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a fox'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a frog'), Js([Js('land'), Js('water')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a gazelle'), Js([Js('land')]), Js([Js('hide')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('horns')]), Js([Js('a gerbil'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a giraffe'), Js([Js('land')]), Js([Js('skin'), Js('hide')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a gnu'), Js([Js('land')]), Js([Js('hide')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('horns')]), Js([Js('a goat'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('horns')]), Js([Js('a goose'), Js([Js('air'), Js('water')]), Js([Js('feathers')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a gorilla'), Js([Js('land')]), Js([Js('skin'), Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('a grasshopper'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a guinea pig'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('a gull'), Js([Js('air'), Js('land'), Js('water')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a hamster'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('a hare'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('a hawk'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('none'), Js('none')]), Js([Js('a hedgehog'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a herring'), Js([Js('water')]), Js([Js('scales')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a hippopotamus'), Js([Js('land'), Js('water')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a hornet'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a horse'), Js([Js('land')]), Js([Js('hide'), Js('hair')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a hummingbird'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('none'), Js('none')]), Js([Js('a hyena'), Js([Js('land')]), Js([Js('fur'), Js('hair')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('an ibex'), Js([Js('land')]), Js([Js('hide')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('horns')]), Js([Js('an ibis'), Js([Js('air'), Js('land'), Js('water')]), Js([Js('feathers')]), Js([Js('legs'), Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a jackal'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a jaguar'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a jellyfish'), Js([Js('water')]), Js([Js('skin')]), Js([Js('tentacles')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a kangaroo'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a koala'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a komodo dragon'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('none')]), Js([Js('a kudu'), Js([Js('land')]), Js([Js('hide')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('horns')]), Js([Js('a lark'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a lemur'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a leopard'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a lion'), Js([Js('land')]), Js([Js('fur'), Js('hair')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a llama'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a lobster'), Js([Js('water')]), Js([Js('armor')]), Js([Js('arms')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a locust'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a lyrebird'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a magpie'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a mammoth'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a manatee'), Js([Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('snout'), Js('none'), Js('none')]), Js([Js('a mandrill'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('a mole'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a mongoose'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a monkey'), Js([Js('land')]), Js([Js('skin'), Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a moose'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('horns')]), Js([Js('a mosquito'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a mouse'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a narwhal'), Js([Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a newt'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a nightingale'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('an octopus'), Js([Js('water')]), Js([Js('skin')]), Js([Js('tentacles')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('an okapi'), Js([Js('land')]), Js([Js('hide')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('none')]), Js([Js('an opossum'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('an ostrich'), Js([Js('air'), Js('land')]), Js([Js('feathers')]), Js([Js('legs'), Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('an otter'), Js([Js('land'), Js('water')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('an owl'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a panda'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a panther'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a parrot'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a partridge'), Js([Js('air'), Js('land')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a pelican'), Js([Js('air'), Js('water')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a penguin'), Js([Js('land'), Js('water')]), Js([Js('skin')]), Js([Js('legs'), Js('wings')]), Js('beak'), Js('none'), Js('none')]), Js([Js('a pheasant'), Js([Js('air'), Js('land')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a pig'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a pigeon'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a pony'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a porcupine'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('none')]), Js([Js('a prairie dog'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a quail'), Js([Js('air'), Js('land')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a rabbit'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a raccoon'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a ram'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('horns')]), Js([Js('a rat'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a raven'), Js([Js('air')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a reindeer'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('horns')]), Js([Js('a rhinoceros'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a salamander'), Js([Js('land'), Js('water')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a salmon'), Js([Js('water')]), Js([Js('scales')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a sardine'), Js([Js('water')]), Js([Js('scales')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a sea lion'), Js([Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a seahorse'), Js([Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a seal'), Js([Js('land'), Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a shark'), Js([Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a sheep'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a skunk'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a sloth'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a snake'), Js([Js('land'), Js('water')]), Js([Js('scales')]), Js([Js('body')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a spider'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a squirrel'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a swan'), Js([Js('water')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('none'), Js('none')]), Js([Js('a tapir'), Js([Js('land')]), Js([Js('hide')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a tarsier'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('ears')]), Js([Js('a termite'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a tiger'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('ears')]), Js([Js('a toad'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a turkey'), Js([Js('air'), Js('land')]), Js([Js('feathers')]), Js([Js('wings')]), Js('beak'), Js('tail'), Js('none')]), Js([Js('a turtle'), Js([Js('land'), Js('water')]), Js([Js('shell'), Js('skin')]), Js([Js('fins')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a tortoise'), Js([Js('land')]), Js([Js('shell'), Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a wallaby'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a walrus'), Js([Js('land'), Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a wasp'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a weasel'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a whale'), Js([Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a wolf'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a wolverine'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a wombat'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('ears')]), Js([Js('a yak'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('none'), Js('horns')]), Js([Js('a zebra'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')])]))
    var.put('traits', Js([]))
    var.put('pkType', Js(''))
    var.put('rnPers', ((var.get('Math').callprop('random')*var.get('pers').get('length'))|Js(0.0)))
    var.put('rnAmnt', ((var.get('Math').callprop('random')*var.get('amnt').get('length'))|Js(0.0)))
    var.put('rnEvo', ((var.get('Math').callprop('random')*var.get('evo').get('length'))|Js(0.0)))
    var.put('rnRsm', ((var.get('Math').callprop('random')*var.get('rsm').get('length'))|Js(0.0)))
    var.put('rnd1', ((var.get('Math').callprop('random')*var.get('pkm').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('pkm').get(var.get('rnd1')).get('1').get('length'))|Js(0.0)))
    if PyJsStrictEq(var.get('pkm').get(var.get('rnd1')).get('1').get(var.get('rnd2')),Js('land')):
        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('lnd').get('length'))|Js(0.0)))
        var.put('pkType', var.get('lnd').get(var.get('rnd3')))
    else:
        if PyJsStrictEq(var.get('pkm').get(var.get('rnd1')).get('1').get(var.get('rnd2')),Js('water')):
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('wtr').get('length'))|Js(0.0)))
            var.put('pkType', var.get('wtr').get(var.get('rnd3')))
        else:
            if PyJsStrictEq(var.get('pkm').get(var.get('rnd1')).get('1').get(var.get('rnd2')),Js('air')):
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('air').get('length'))|Js(0.0)))
                var.put('pkType', var.get('air').get(var.get('rnd3')))
    if PyJsStrictEq(var.get('pkType'),Js('bug')):
        def PyJs_LONG_0_(var=var):
            return var.put('pkm', Js([Js([Js('an ant'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a bee'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a butterfly'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a caterpillar'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a cockroach'), Js([Js('land')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a dragonfly'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a fly'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a grasshopper'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a hornet'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a locust'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a mosquito'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a termite'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a wasp'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')])]))
        PyJs_LONG_0_()
        var.put('rnd1', ((var.get('Math').callprop('random')*var.get('pkm').get('length'))|Js(0.0)))
    if PyJsStrictEq(var.get('pkType'),Js('dragon')):
        def PyJs_LONG_1_(var=var):
            return var.put('pkm', Js([Js([Js('an alligator'), Js([Js('land'), Js('water')]), Js([Js('skin'), Js('scales')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('none')]), Js([Js('an armadillo'), Js([Js('land')]), Js([Js('fur')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a cobra'), Js([Js('land')]), Js([Js('skin'), Js('scales')]), Js([Js('body')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a crocodile'), Js([Js('land'), Js('water')]), Js([Js('skin'), Js('scales')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a dragonfly'), Js([Js('air')]), Js([Js('skin')]), Js([Js('wings')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('an eel'), Js([Js('water')]), Js([Js('skin')]), Js([Js('body')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a komodo dragon'), Js([Js('land')]), Js([Js('skin')]), Js([Js('legs')]), Js('snout'), Js('tail'), Js('none')]), Js([Js('a narwhal'), Js([Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('mouth'), Js('none'), Js('none')]), Js([Js('a salamander'), Js([Js('land'), Js('water')]), Js([Js('skin')]), Js([Js('legs')]), Js('mouth'), Js('tail'), Js('none')]), Js([Js('a seahorse'), Js([Js('water')]), Js([Js('skin')]), Js([Js('fins')]), Js('snout'), Js('tail'), Js('ears')]), Js([Js('a snake'), Js([Js('land'), Js('water')]), Js([Js('scales')]), Js([Js('body')]), Js('mouth'), Js('tail'), Js('none')])]))
        PyJs_LONG_1_()
        var.put('rnd1', ((var.get('Math').callprop('random')*var.get('pkm').get('length'))|Js(0.0)))
    while (var.get('traits').get('length')<Js(3.0)):
        #for JS loop
        var.put('i', Js(2.0))
        while (var.get('i')<var.get('pkm').get(var.get('rnd1')).get('length')):
            try:
                var.put('rnTrait', ((var.get('Math').callprop('random')*Js(2.0))|Js(0.0)))
                if PyJsStrictEq(var.get('rnTrait'),Js(1.0)):
                    if ((var.get('traits').get('length')<Js(3.0)) and PyJsStrictNeq(var.get('pkm').get(var.get('rnd1')).get(var.get('i')),Js('none'))):
                        var.get('console').callprop('log', var.get('pkm').get(var.get('rnd1')).get(var.get('i')))
                        if (PyJsStrictEq(var.get('i'),Js(2.0)) or PyJsStrictEq(var.get('i'),Js(3.0))):
                            var.put('rndmz', ((var.get('Math').callprop('random')*var.get('pkm').get(var.get('rnd1')).get(var.get('i')).get('length'))|Js(0.0)))
                            var.get('traits').callprop('push', var.get('pkm').get(var.get('rnd1')).get(var.get('i')).get(var.get('rndmz')))
                        else:
                            var.get('traits').callprop('push', var.get('pkm').get(var.get('rnd1')).get(var.get('i')))
                        if PyJsStrictEq(var.get('traits').get('0'),var.get('traits').get('1')):
                            var.get('traits').callprop('splice', Js(1.0), Js(1.0))
                        else:
                            if (PyJsStrictEq(var.get('traits').get('1'),var.get('traits').get('2')) or PyJsStrictEq(var.get('traits').get('0'),var.get('traits').get('2'))):
                                var.get('traits').callprop('splice', Js(2.0), Js(1.0))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('console').callprop('log', Js('--'))
    var.put('descrs', Js([]))
    while 1:
        SWITCHED = False
        CONDITION = (var.get('pkType'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('bug')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_2_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_2_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('bugSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('bugSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('bugWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('bugWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('bugLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('bugLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('bugArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('bugArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('bugMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('bugMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('bugLegs').get('length'))|Js(0.0)))
                                            var.put('description', ((var.get('bugLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('bugWings').get('length'))|Js(0.0)))
                                                var.put('description', ((Js('the added bonus of ')+var.get('bugWings').get(var.get('rndm')))+Js(' wings')))
                                                var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeBug').get('length'))|Js(0.0)))
            var.put('place', var.get('placeBug').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('bugAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('bugAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('bugAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('bugAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('bugAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('dark')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_3_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_3_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('darkSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('darkWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkWings').get('length'))|Js(0.0)))
                                var.put('description', ((Js('the added bonus of ')+var.get('darkWings').get(var.get('rndm')))+Js(' wings')))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkLegs').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('darkLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkArms').get('length'))|Js(0.0)))
                                        var.put('description', ((var.get('darkArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkMouth').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('darkMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkBeak').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('darkBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkSnout').get('length'))|Js(0.0)))
                                                    var.put('description', (((Js('a ')+var.get('darkSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkEars').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('darkEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkHorns').get('length'))|Js(0.0)))
                                                            var.put('description', ((var.get('darkHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkTail').get('length'))|Js(0.0)))
                                                                var.put('description', var.get('darkTail').get(var.get('rndm')))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('darkLegs').get('length'))|Js(0.0)))
                                                                    var.put('description', ((var.get('darkLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeDark').get('length'))|Js(0.0)))
            var.put('place', var.get('placeDark').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('darkAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('darkAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('darkAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('darkAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('darkAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('dragon')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_4_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_4_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('dragonSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('dragonWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('dragonLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('dragonArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if ((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak'))):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonMouth').get('length'))|Js(0.0)))
                                        var.put('description', ((Js('a ')+var.get('dragonMouth').get(var.get('rndm')))+Js(' mouth')))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonEars').get('length'))|Js(0.0)))
                                            var.put('description', ((var.get('dragonEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonHorns').get('length'))|Js(0.0)))
                                                var.put('description', ((var.get('dragonHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonTail').get('length'))|Js(0.0)))
                                                    var.put('description', var.get('dragonTail').get(var.get('rndm')))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonLegs').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('dragonLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('dragonWings').get('length'))|Js(0.0)))
                                                            var.put('description', ((Js('the added bonus of ')+var.get('dragonWings').get(var.get('rndm')))+Js(' wings')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeDragon').get('length'))|Js(0.0)))
            var.put('place', var.get('placeDragon').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('dragonAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('dragonAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('dragonAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('dragonAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('dragonAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('electric')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_5_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_5_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('elecSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('elecWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('elecLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('elecArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('elecMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('elecBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('elecSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('elecEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('elecHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('elecTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('elecLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('elecWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('elecWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeElectric').get('length'))|Js(0.0)))
            var.put('place', var.get('placeElectric').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('electricAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('electricAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('electricAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('electricAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('electricAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('fairy')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_6_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_6_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairySkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('fairySkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('fairyWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('fairyLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('fairyArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('fairyMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('fairyBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairySnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('fairySnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('fairyEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('fairyHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('fairyTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('fairyLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('fairyWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('fairyWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeFairy').get('length'))|Js(0.0)))
            var.put('place', var.get('placeFairy').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('fairyAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('fairyAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('fairyAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('fairyAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('fairyAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('fighting')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_7_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_7_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('fightSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('fightWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('fightLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('fightArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('fightMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('fightBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('fightSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('fightEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('fightHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('fightTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('fightLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('fightWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('fightWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeFighting').get('length'))|Js(0.0)))
            var.put('place', var.get('placeFighting').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('fightingAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('fightingAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('fightingAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('fightingAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('fightingAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('fire')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_8_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_8_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('fireSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('fireWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('fireLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('fireArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('fireMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('fireBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('fireSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('fireEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('fireHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('fireTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('fireLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('fireWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('fireWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeFire').get('length'))|Js(0.0)))
            var.put('place', var.get('placeFire').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('fireAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('fireAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('fireAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('fireAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('fireAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('flying')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_9_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_9_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('flySkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('flySkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('flyWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('flyLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('flyArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('flyMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('flyBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('flySnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('flySnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('flyEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('flyHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('flyTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('flyLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('flyWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('flyWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeFlying').get('length'))|Js(0.0)))
            var.put('place', var.get('placeFlying').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('flyingAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('flyingAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('flyingAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('flyingAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('flyingAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('ghost')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_10_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_10_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('ghostSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('ghostWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('ghostLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('ghostArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('ghostMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('ghostBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('ghostSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('ghostEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('ghostHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('ghostTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('ghostLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('ghostWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('ghostWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeGhost').get('length'))|Js(0.0)))
            var.put('place', var.get('placeGhost').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('ghostAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('ghostAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('ghostAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('ghostAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('ghostAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('grass')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_11_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_11_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('grassSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('grassWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('grassLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('grassArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('grassMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('grassBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('grassSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('grassEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('grassHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('grassTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('grassLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('grassWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('grassWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeGrass').get('length'))|Js(0.0)))
            var.put('place', var.get('placeGrass').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('grassAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('grassAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('grassAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('grassAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('grassAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('ground')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_12_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_12_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('groundSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('groundWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('groundLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('groundArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('groundMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('groundBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('groundSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('groundEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('groundHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('groundTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('groundLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('groundWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('groundWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeGround').get('length'))|Js(0.0)))
            var.put('place', var.get('placeGround').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('groundAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('groundAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('groundAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('groundAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('groundAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('ice')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_13_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_13_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('iceSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('iceWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('iceLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('iceArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('iceMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('iceBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('iceSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('iceEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('iceHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('iceTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('iceLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('iceWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('iceWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeIce').get('length'))|Js(0.0)))
            var.put('place', var.get('placeIce').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('iceAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('iceAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('iceAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('iceAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('iceAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('normal')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_14_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_14_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('normSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('normSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('normWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('normWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('normLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('normLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('normArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('normArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('normMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('normMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('normBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('normBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('normSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('normSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('normEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('normEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('normHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('normHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('normTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('normTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('normLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('normLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('normWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('normWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeNormal').get('length'))|Js(0.0)))
            var.put('place', var.get('placeNormal').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('normalAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('normalAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('normalAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('normalAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('normalAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('poison')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_15_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_15_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('poisonSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('poisonWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('poisonLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('poisonArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('poisonMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('poisonBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('poisonSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('poisonEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('poisonHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('poisonTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('poisonLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('poisonWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('poisonWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placePoison').get('length'))|Js(0.0)))
            var.put('place', var.get('placePoison').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('poisonAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('poisonAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('poisonAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('poisonAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('poisonAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('psychic')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_16_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_16_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('psySkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('psySkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('psyWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('psyLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('psyArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('psyMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('psyBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('psySnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('psySnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('psyEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('psyHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('psyTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('psyLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('psyWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('psyWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placePsychic').get('length'))|Js(0.0)))
            var.put('place', var.get('placePsychic').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('psychicAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('psychicAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('psychicAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('psychicAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('psychicAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('rock')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_17_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_17_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('rockSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('rockWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('rockLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('rockArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('rockMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('rockBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('rockSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('rockEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('rockHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('rockTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('rockLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('rockWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('rockWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeRock').get('length'))|Js(0.0)))
            var.put('place', var.get('placeRock').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('rockAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('rockAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('rockAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('rockAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('rockAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('steel')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_18_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_18_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('steelSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('steelWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('steelLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('steelArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelMouth').get('length'))|Js(0.0)))
                                        var.put('description', (((Js('a ')+var.get('steelMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelBeak').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('steelBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelSnout').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('steelSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelEars').get('length'))|Js(0.0)))
                                                    var.put('description', ((var.get('steelEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelHorns').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('steelHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelTail').get('length'))|Js(0.0)))
                                                            var.put('description', var.get('steelTail').get(var.get('rndm')))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelLegs').get('length'))|Js(0.0)))
                                                                var.put('description', ((var.get('steelLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('steelWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('steelWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeSteel').get('length'))|Js(0.0)))
            var.put('place', var.get('placeSteel').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('steelAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('steelAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('steelAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('steelAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('steelAttk').get(var.get('attk2')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('water')):
            SWITCHED = True
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(3.0)):
                try:
                    def PyJs_LONG_19_(var=var):
                        return ((((((PyJsStrictEq(var.get('traits').get(var.get('i')),Js('skin')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('shell'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hair'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('feathers'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('hide'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fur'))) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('armor')))
                    if (PyJs_LONG_19_() or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('scales'))):
                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterSkin').get('length'))|Js(0.0)))
                        var.put('description', ((var.get('waterSkin').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                        var.get('descrs').callprop('push', var.get('description'))
                    else:
                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('wings')):
                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterWings').get('length'))|Js(0.0)))
                            var.put('description', ((var.get('waterWings').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                            var.get('descrs').callprop('push', var.get('description'))
                        else:
                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('legs')):
                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterLegs').get('length'))|Js(0.0)))
                                var.put('description', ((var.get('waterLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                var.get('descrs').callprop('push', var.get('description'))
                            else:
                                if (PyJsStrictEq(var.get('traits').get(var.get('i')),Js('arms')) or PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tentacles'))):
                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterArms').get('length'))|Js(0.0)))
                                    var.put('description', ((var.get('waterArms').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                    var.get('descrs').callprop('push', var.get('description'))
                                else:
                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('fins')):
                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterLegs').get('length'))|Js(0.0)))
                                        var.put('description', ((var.get('waterLegs').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                        var.get('descrs').callprop('push', var.get('description'))
                                    else:
                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('mouth')):
                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterMouth').get('length'))|Js(0.0)))
                                            var.put('description', (((Js('a ')+var.get('waterMouth').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                            var.get('descrs').callprop('push', var.get('description'))
                                        else:
                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('beak')):
                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterBeak').get('length'))|Js(0.0)))
                                                var.put('description', (((Js('a ')+var.get('waterBeak').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                var.get('descrs').callprop('push', var.get('description'))
                                            else:
                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('snout')):
                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterSnout').get('length'))|Js(0.0)))
                                                    var.put('description', (((Js('a ')+var.get('waterSnout').get(var.get('rndm')))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                    var.get('descrs').callprop('push', var.get('description'))
                                                else:
                                                    if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('ears')):
                                                        var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterEars').get('length'))|Js(0.0)))
                                                        var.put('description', ((var.get('waterEars').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                        var.get('descrs').callprop('push', var.get('description'))
                                                    else:
                                                        if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('horns')):
                                                            var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterHorns').get('length'))|Js(0.0)))
                                                            var.put('description', ((var.get('waterHorns').get(var.get('rndm'))+Js(' '))+var.get('traits').get(var.get('i'))))
                                                            var.get('descrs').callprop('push', var.get('description'))
                                                        else:
                                                            if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('tail')):
                                                                var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterTail').get('length'))|Js(0.0)))
                                                                var.put('description', var.get('waterTail').get(var.get('rndm')))
                                                                var.get('descrs').callprop('push', var.get('description'))
                                                            else:
                                                                if PyJsStrictEq(var.get('traits').get(var.get('i')),Js('body')):
                                                                    var.put('rndm', ((var.get('Math').callprop('random')*var.get('waterWings').get('length'))|Js(0.0)))
                                                                    var.put('description', ((Js('the added bonus of ')+var.get('waterWings').get(var.get('rndm')))+Js(' wings')))
                                                                    var.get('descrs').callprop('push', var.get('description'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rndPlace', ((var.get('Math').callprop('random')*var.get('placeWater').get('length'))|Js(0.0)))
            var.put('place', var.get('placeWater').get(var.get('rndPlace')))
            var.put('attk1', ((var.get('Math').callprop('random')*var.get('waterAttk').get('length'))|Js(0.0)))
            var.put('atkOne', var.get('waterAttk').get(var.get('attk1')))
            var.put('attk2', ((var.get('Math').callprop('random')*var.get('waterAttk').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('attk1'),var.get('attk2')):
                var.put('attk2', ((var.get('Math').callprop('random')*var.get('waterAttk').get('length'))|Js(0.0)))
            var.put('atkTwo', var.get('waterAttk').get(var.get('attk2')))
            break
        SWITCHED = True
        break
    var.put('name', ((((((((((((Js('This Pokemon is a ')+var.get('pkType'))+Js('-type Pokemon and '))+var.get('rsm').get(var.get('rnRsm')))+Js(' '))+var.get('pkm').get(var.get('rnd1')).get('0'))+Js('. It has '))+var.get('descrs').get('0'))+Js(', '))+var.get('descrs').get('1'))+Js(' and '))+var.get('descrs').get('2'))+Js('.')))
    var.put('name2', ((((((Js(" They're generally ")+var.get('pers').get(var.get('rnPers')))+Js(' by nature and can often be found '))+var.get('place'))+Js(". If you're out looking for them they can often be seen "))+var.get('amnt').get(var.get('rnAmnt')))+Js('.')))
    var.put('name3', ((((((Js('It tends to attack with ')+var.get('atkOne'))+Js(' and '))+var.get('atkTwo'))+Js('. It '))+var.get('evo').get(var.get('rnEvo')))+Js('.')))
    var.put('br', Js([]))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('bugSkin', Js([Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('camouflaged'), Js('dark'), Js('fluff covered'), Js('glowing'), Js('hair covered'), Js('light'), Js('patterned'), Js('thick armored'), Js('thorny'), Js('translucent')]))
var.put('bugLegs', Js([Js('ridged'), Js('armored'), Js('thick, fluffy'), Js('hair covered'), Js('thin, long'), Js('thorn covered'), Js('camouflaged'), Js('small'), Js('powerful')]))
var.put('bugWings', Js([Js('angular'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('petal-like'), Js('camouflaged'), Js('cloak-like'), Js('dark'), Js('double paired'), Js('giant'), Js('glowing'), Js('light'), Js('patterned'), Js('powerful'), Js('razor sharp'), Js('ribbon-like'), Js('small'), Js('translucent')]))
var.put('bugMouth', Js([Js('tusked'), Js('seemingly invisible'), Js('giant'), Js('powerful'), Js('little'), Js('toothed'), Js('sharp toothed'), Js('pincer-like'), Js('seemingly smiling'), Js('seemingly frowning')]))
var.put('bugArms', Js([Js('bladed'), Js('pincer-like'), Js('flexible'), Js('strong'), Js('stinger-like'), Js('claw-like'), Js('tiny'), Js('hidden')]))
var.put('darkSkin', Js([Js('black'), Js('black and crimson'), Js('black and gray'), Js('black and white'), Js('blue and crimson'), Js('blue and purple'), Js('dark'), Js('dark blue'), Js('dark glowing'), Js('deep purple'), Js('gray'), Js('red and black'), Js('shadowy'), Js('white and blue')]))
var.put('darkLegs', Js([Js('ridged'), Js('armored'), Js('thick'), Js('powerful'), Js('shaded'), Js('smoke-like'), Js('patterned'), Js('an extra pair of'), Js('gem encrusted')]))
var.put('darkArms', Js([Js('ridged'), Js('folded'), Js('shielded'), Js('strong'), Js('enormous'), Js('elongated'), Js('bladed'), Js('barbed'), Js('muscled')]))
var.put('darkWings', Js([Js('angular'), Js('smoke-like'), Js('cloak-like'), Js('dark'), Js('double paired'), Js('giant'), Js('glowing'), Js('patterned'), Js('powerful'), Js('razor sharp'), Js('translucent'), Js('ribbon-like'), Js('overgrown'), Js('barbed'), Js('reflective')]))
var.put('darkMouth', Js([Js('tusked'), Js('seemingly invisible'), Js('giant'), Js('powerful'), Js('sharp toothed'), Js('seemingly smirking'), Js('seemingly frowning'), Js('distinct lack of a visible'), Js('cavernous'), Js('toothed')]))
var.put('darkBeak', Js([Js('crescent'), Js('reinforced'), Js('razor sharp'), Js('crystal-like'), Js('thick obsidian'), Js('solid onyx'), Js('sharp, crimson'), Js('terrifying'), Js('mighty'), Js('enlarged'), Js('rugged')]))
var.put('darkSnout', Js([Js('tusked'), Js('horned'), Js('pointed'), Js('giant'), Js('stubby'), Js('sharp toothed'), Js('seemingly smirking'), Js('seemingly frowning'), Js('fuming'), Js('abyssal'), Js('toothed')]))
var.put('darkTail', Js([Js('a tail much like a whip'), Js('a tail that ends in a barbed tip'), Js('a pair of tails instead of one'), Js('several tails instead of one'), Js('a tail with the appearance of flowing smoke'), Js('a tail that ends in a sharp, blade-like curve'), Js('a tail that ends in a fan-like shape'), Js('a tail that seems to shimmer in light'), Js('an incredibly fluffy tail'), Js('a tail covered in armored plates'), Js("a tail that visibly holds the Pokemon's powers"), Js('a tail charged with dark energies'), Js('a tail that wraps itself around the body when in rest'), Js('a tail decorated by the Pokemon'), Js('a tail that pulses with energy during attacks'), Js('a tail with odd, dark pulsing symbols'), Js('a tail that seems to distort light behind and around the Pokemon')]))
var.put('darkEars', Js([Js('horn-like'), Js('wing-like'), Js('pointy'), Js('flappy'), Js('flabby'), Js('huge'), Js('jagged'), Js('ribbon-like'), Js('fan-like'), Js('stubby'), Js('nimble'), Js('enormous')]))
var.put('darkHorns', Js([Js('ridged'), Js('a crown of'), Js('a row of'), Js('blade-like'), Js('crystal'), Js('curved'), Js('glowing'), Js('obsidian'), Js('onyx'), Js('pulsing'), Js('scythe-like'), Js('sharp'), Js('thin'), Js('two sets of')]))
var.put('dragonHorns', Js([Js('ridged'), Js('a crown of'), Js('a row of'), Js('antler-like'), Js('crystal'), Js('curved'), Js('fan-like'), Js('glowing'), Js('hammer-like'), Js('mohawk-like'), Js('pulsing'), Js('sharp'), Js('stubby'), Js('thin'), Js('two sets of')]))
var.put('dragonEars', Js([Js('armored'), Js('bone-like'), Js('coiling'), Js('crystal'), Js('enormous'), Js('hammer-like'), Js('horn-like'), Js('no visible'), Js('pointy'), Js('round'), Js('smoldering'), Js('wing-like')]))
var.put('dragonSkin', Js([Js('aerodynamic'), Js('armor plated'), Js('barbed'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('boulder-like'), Js('cloud-like'), Js('crystal-like'), Js('fiery looking'), Js('glowing'), Js('metal'), Js('scaled'), Js('smooth'), Js('soft'), Js('thick'), Js('translucent')]))
var.put('dragonLegs', Js([Js('ridged'), Js('an extra pair of'), Js('armored'), Js('barbed'), Js('crystal-like'), Js('curved'), Js('enormous'), Js('massive'), Js('powerful'), Js('stubby'), Js('thick'), Js('two extra pairs of')]))
var.put('dragonArms', Js([Js('ridged'), Js('folded'), Js('armored'), Js('barbed'), Js('bat-like'), Js('blade-like'), Js('clawed'), Js('fiery'), Js('jagged'), Js('stocky'), Js('strong'), Js('winged')]))
var.put('dragonWings', Js([Js('cloud-like'), Js('rainbow'), Js('fiery'), Js('angelic'), Js('barbed'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('crystal'), Js('energy pulsing'), Js('enormous'), Js('fan-like'), Js('giant'), Js('glowing'), Js('humongous'), Js('jagged'), Js('ridged'), Js('translucent'), Js('two pairs of')]))
var.put('dragonMouth', Js([Js('tusked'), Js('bearded'), Js('blade toothed'), Js('boulder-like'), Js('cavernous'), Js('crystal toothed'), Js('fiery'), Js('metal-like'), Js('powerful'), Js('seemingly ever angry'), Js('seemingly smiling'), Js('sharp toothed'), Js('small'), Js('smoldering')]))
var.put('dragonTail', Js([Js('a barbed tail'), Js('a bladed tail'), Js('a cloud-like tail'), Js('a crystal adorned tail'), Js('a curling tail'), Js('a fan-like tail'), Js('a pair of tails'), Js('a rainbow tail'), Js('a segmented tail'), Js('a stubby tail'), Js('a tail ending in a hammer'), Js('a tail ending in double barbs'), Js('a tail like a whip'), Js('a thick tail'), Js('an armor plated tail'), Js('an incredibly long tail'), Js('an incredibly powerful tail'), Js('several tails')]))
var.put('elecSkin', Js([Js('yellow'), Js('orange'), Js('black and yellow'), Js('blue and yellow'), Js('yellow and white'), Js('statically charged'), Js('electrifying'), Js('charged'), Js('electrically charged'), Js('magnetized'), Js('jagged'), Js('sharp'), Js('sharply jagged'), Js('barbed')]))
var.put('elecLegs', Js([Js('ridged'), Js('agile'), Js('bolt-like'), Js('energy laden'), Js('energy pulsing'), Js('fast'), Js('magnetized'), Js('nimble'), Js('powerful'), Js('spiked'), Js('tiny')]))
var.put('elecArms', Js([Js('ridged'), Js('folded'), Js('bolt-like'), Js('energy laden'), Js('energy pulsing'), Js('magnetized'), Js('swift'), Js('strong'), Js('small'), Js('electrifying'), Js('an extra pair of'), Js('orb-like')]))
var.put('elecWings', Js([Js('angular'), Js('bolt-like'), Js('cloak-like'), Js('electrically laden'), Js('energized'), Js('jagged'), Js('layered'), Js('magnetic'), Js('pulsing'), Js('tiny'), Js('two pairs of')]))
var.put('elecMouth', Js([Js('bearded'), Js('gigantic'), Js('jagged'), Js('sharp toothed'), Js('small'), Js('tiny'), Js('toothed'), Js('seemingly lack of a'), Js('seemingly invisible'), Js('hidden')]))
var.put('elecBeak', Js([Js('crescent'), Js('bolt-like'), Js('bright yellow'), Js('glowing'), Js('jagged'), Js('powerful'), Js('pulsing'), Js('razor sharp')]))
var.put('elecSnout', Js([Js('tusked'), Js('horned'), Js('jagged'), Js('pointed'), Js('seemingly frowning'), Js('seemingly smirking'), Js('sharp toothed'), Js('small'), Js('smiling'), Js('stubby'), Js('thick')]))
var.put('elecTail', Js([Js('a coiling tail'), Js('a jagged tail'), Js('a jagged, fan-like tail'), Js('a lightning bolt tail'), Js('a magnetized tail'), Js('a pair of tails'), Js('a positively and a negatively charged tail'), Js('a sharp blade-like tail'), Js('a stubby orb-like tail'), Js('a tail ending in a charged orb'), Js('a tail ending in a magnet'), Js('a tail full of charged orbs'), Js('a tail laden with electric charges'), Js('a tail pulsing with electricity'), Js('several tails')]))
var.put('elecEars', Js([Js('bolt-like'), Js('coiling'), Js('oscillating'), Js('electrically charged'), Js('big, round'), Js('tiny'), Js('orb-like'), Js('magnetized'), Js('blade-like'), Js('flappy'), Js('flabby'), Js('stubby'), Js('glowing')]))
var.put('elecHorns', Js([Js('ridged'), Js('pulsing'), Js('magnetized'), Js('orb-like'), Js('coiled'), Js('bolt-like'), Js('sharp'), Js('jagged'), Js('curved'), Js('a row of'), Js('mohawk-like'), Js('stubby'), Js('two sets of')]))
var.put('fairySkin', Js([Js('blushy'), Js('coral'), Js('fluffy'), Js('glistening'), Js('glossy'), Js('glowing'), Js('luminous'), Js('pink'), Js('rose'), Js('shiny'), Js('silken'), Js('soft'), Js('sparkling'), Js('velvety')]))
var.put('fairyLegs', Js([Js('covered'), Js('feathery'), Js('fluffy'), Js('glowing'), Js('lean'), Js('shrouded'), Js('slender'), Js('slim'), Js('small'), Js('soft'), Js('stubby'), Js('tiny'), Js('wispy')]))
var.put('fairyArms', Js([Js('cloak-like'), Js('elongated'), Js('fat'), Js('fluffy'), Js('folded'), Js('lean'), Js('ribbon-like'), Js('slim'), Js('small'), Js('smooth'), Js('stubby'), Js('tiny')]))
var.put('fairyWings', Js([Js('angelic'), Js('bioluminescent'), Js('bow-like'), Js('cloud-like'), Js('enormous'), Js('fan-like'), Js('floating'), Js('fluffy'), Js('glowing'), Js('layered'), Js('ribbon-like'), Js('smooth'), Js('soft, feathery'), Js('tiny'), Js('two sets of')]))
var.put('fairyBeak', Js([Js('blunt'), Js('broad'), Js('crescent'), Js('curved'), Js('glowing'), Js('huge'), Js('pointy'), Js('shining'), Js('smiling'), Js('sparkling')]))
var.put('fairyMouth', Js([Js('bearded'), Js('blunt toothed'), Js('broad'), Js('cavernous'), Js('grinning'), Js('hidden'), Js('lack of a'), Js('shrouded'), Js('small'), Js('smiling'), Js('smirking'), Js('tiny'), Js('veiled')]))
var.put('fairySnout', Js([Js('bearded'), Js('broad'), Js('fluffy'), Js('glossy'), Js('glowing'), Js('huge'), Js('pointy'), Js('rounded'), Js('shining'), Js('shrouded'), Js('small'), Js('sparkling'), Js('stubby'), Js('tiny'), Js('veiled')]))
var.put('fairyTail', Js([Js('a bioluminescent tail'), Js('a decorated tail'), Js('a fan-like tail'), Js('a fluffy tail'), Js('a glowing tail'), Js('a long tail wrapped around its body'), Js('a long, floating tail'), Js('a long, forked tail'), Js('a ribbon-like tail'), Js('a short, stubby tail'), Js('a sparkling tail'), Js('several tails instead of one'), Js('two tails instead of one')]))
var.put('fairyEars', Js([Js('bow-like'), Js('cloud-like'), Js('enormous'), Js('flabby'), Js('flappy'), Js('fluffy'), Js('hidden'), Js('huge'), Js('pointy'), Js('puffy'), Js('ribbon-like'), Js('short'), Js('stubby'), Js('veiled')]))
var.put('fairyHorns', Js([Js('antenna-like'), Js('antler-like'), Js('coiling'), Js('crescent'), Js('curling'), Js('curving'), Js('decorated'), Js('looping'), Js('painted'), Js('pointy'), Js('short'), Js('smooth'), Js('stubby')]))
var.put('fightSkin', Js([Js('armor-like'), Js('bruised'), Js('camouflaged'), Js('coarse'), Js('decorated'), Js('deflective'), Js('nimble'), Js('patterned'), Js('smooth'), Js('stone-like'), Js('strengthened'), Js('thick')]))
var.put('fightLegs', Js([Js('ridged'), Js('agile'), Js('armored'), Js('broad'), Js('clothed'), Js('decorated'), Js('dexterous'), Js('muscled'), Js('nimble'), Js('patterned'), Js('powerful'), Js('strengthened'), Js('two sets of')]))
var.put('fightArms', Js([Js('ridged'), Js('folded'), Js('armored'), Js('barbed'), Js('blade-like'), Js('composed'), Js('energetic'), Js('hammer-like'), Js('relaxed'), Js('robust'), Js('slim'), Js('strong'), Js('toned'), Js('two sets of')]))
var.put('fightWings', Js([Js('angular'), Js('angelic'), Js('armored'), Js('blade-like'), Js('broad'), Js('cloak-like'), Js('fan-like'), Js('honed'), Js('jagged'), Js('ribbon-like'), Js('robe-like'), Js('sharp'), Js('strong')]))
var.put('fightMouth', Js([Js('tusked'), Js('foaming'), Js('focused looking'), Js('frowning'), Js('giant'), Js('lack of a'), Js('raging'), Js('seemingly angry'), Js('seemingly smirking'), Js('serious looking'), Js('smiling'), Js('content looking'), Js('tranquil looking'), Js('seemingly arrogantly smiling')]))
var.put('fightBeak', Js([Js('crescent'), Js('reinforced'), Js('barbed'), Js('blade-like'), Js('broad'), Js('decorated'), Js('jagged'), Js('powerful'), Js('razor sharp'), Js('sharp'), Js('talon-like'), Js('thin')]))
var.put('fightSnout', Js([Js('tusked'), Js('horned'), Js('broad'), Js('bruised'), Js('decorated'), Js('fierce looking'), Js('flattened'), Js('frowning'), Js('pointy'), Js('protected'), Js('seemingly arrogantly smiling'), Js('seemingly broken'), Js('seemingly smirking'), Js('serious looking'), Js('sharp'), Js('shielded'), Js('stubby')]))
var.put('fightTail', Js([Js('a leg-like tail'), Js('a long tail used for superior balance'), Js('a muscular tail'), Js('a nimble and strong tail'), Js('a prehensile tail'), Js('a ribbon-like tail'), Js('a set of prehensile tails'), Js('a set of tails like a fan'), Js('a set of two powerful tails'), Js('a tail ending in a fist-like extremity'), Js('a tail ending in a hammer'), Js('a tail like a whip'), Js('a tail that wraps around the body like a belt')]))
var.put('fightEars', Js([Js('a lack of'), Js('bolt-like'), Js('broken'), Js('fan-like'), Js('flappy'), Js('flabby'), Js('hat-like'), Js('helmet-like'), Js('jagged'), Js('mohawk-like'), Js('protective'), Js('ribbon-like'), Js('round'), Js('smoothened'), Js('stubby')]))
var.put('fightHorns', Js([Js('ridged'), Js('a crown of'), Js('a row of'), Js('aerodynamic'), Js('antler-like'), Js('blade-like'), Js('curled'), Js('curved'), Js('mohawk-like'), Js('pointed'), Js('ridge'), Js('rounded'), Js('sharp'), Js('spiral'), Js('stubby')]))
var.put('fireSkin', Js([Js('incandescent'), Js('burning'), Js('crimson'), Js('fiery'), Js('flaming'), Js('fuming'), Js('gleaming'), Js('glowing'), Js('lava-like'), Js('luminous'), Js('orange'), Js('red'), Js('red and orange'), Js('sanguine'), Js('smoking'), Js('smoldering'), Js('white and orange')]))
var.put('fireLegs', Js([Js('ridged'), Js('an extra set of'), Js('ashen'), Js('black'), Js('boulder-like'), Js('dark'), Js('fiery hot'), Js('glowing'), Js('lava stone'), Js('muscular'), Js('obsidian'), Js('powerful'), Js('smoking'), Js('strong')]))
var.put('fireArms', Js([Js('ridged'), Js('folded'), Js('agile'), Js('ashen'), Js('dark'), Js('little'), Js('muscular'), Js('nimble'), Js('obsidian'), Js('slim'), Js('smoldering'), Js('strong'), Js('stubby')]))
var.put('fireWings', Js([Js('angular'), Js('ashen'), Js('black'), Js('burning'), Js('cloak-like'), Js('crimson'), Js('dark'), Js('enormous'), Js('fan-like'), Js('fiery'), Js('flame-like'), Js('fuming'), Js('glowing'), Js('layered'), Js('luminescent'), Js('obsidian'), Js('ribbon-like'), Js('robe-like'), Js('smoldering'), Js('steaming')]))
var.put('fireMouth', Js([Js('cavernous'), Js('fiery'), Js('frowning'), Js('fuming'), Js('serious looking'), Js('sharp toothed'), Js('small'), Js('smiling'), Js('smirking'), Js('steaming')]))
var.put('fireBeak', Js([Js('crescent'), Js('black'), Js('curved'), Js('fiery'), Js('fuming'), Js('glowing'), Js('luminescent'), Js('dark'), Js('razor-sharp'), Js('sharp'), Js('steaming')]))
var.put('fireSnout', Js([Js('tusked'), Js('horned'), Js('fierce looking'), Js('bearded'), Js('black'), Js('broad'), Js('glowing'), Js('black'), Js('protected'), Js('smoldering'), Js('steaming'), Js('stubby'), Js('stumpy'), Js('thin')]))
var.put('fireTail', Js([Js('a burning tail'), Js('a flame-like tail'), Js('a fluffy flame patterned tail'), Js('a lava-like tail'), Js('a literal flame as a tail'), Js('a muscular'), Js('a smoldering tail'), Js('a stubby tail'), Js('a tail like a fan'), Js('a tail that ends in fire'), Js('a tailpipe-like tail'), Js('an obsidian tail'), Js('several tails in a fan-like pattern')]))
var.put('fireEars', Js([Js('enormous'), Js('wing-like'), Js('flame shaped'), Js('flappy'), Js('flabby'), Js('furnace-like'), Js('horn-like'), Js('huge'), Js('pointy'), Js('rounded'), Js('small'), Js('steaming'), Js('stumpy'), Js('tiny'), Js('big')]))
var.put('fireHorns', Js([Js('ridged'), Js('enormous'), Js('curved'), Js('furnace-like'), Js('stubby'), Js('huge'), Js('pointy'), Js('rounded'), Js('small'), Js('steaming'), Js('stumpy'), Js('tiny'), Js('jagged')]))
var.put('flySkin', Js([Js('armored'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('brightly colored'), Js('camouflaged'), Js('light'), Js('patterned'), Js('rough'), Js('smooth'), Js('soft'), Js('thorny'), Js('translucent')]))
var.put('flyFeathers', Js([Js('bright'), Js('brilliant'), Js('bristly'), Js('broad'), Js('colorful'), Js('colorless'), Js('delicate'), Js('elongated'), Js('fluffy'), Js('glowing'), Js('iridescent'), Js('ornamental'), Js('painted'), Js('pointed'), Js('ruffled'), Js('sharp'), Js('slender'), Js('thick'), Js('tipped')]))
var.put('flyLegs', Js([Js('an extra pair of'), Js('armored'), Js('broad'), Js('clawed'), Js('decorated'), Js('delicate'), Js('fluffy'), Js('long'), Js('muscular'), Js('nimble'), Js('powerful'), Js('slim'), Js('tiny')]))
var.put('flyWings', Js([Js('angular'), Js('angelic'), Js('armored'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('blade-like'), Js('clawed'), Js('cloak-like'), Js('cloud-like'), Js('enormous'), Js('fan-like'), Js('gigantic'), Js('huge'), Js('layered'), Js('patterned'), Js('rainbow'), Js('shield-like'), Js('translucent'), Js('two pairs of')]))
var.put('flyMouth', Js([Js('broad'), Js('cavernous'), Js('frowning'), Js('hidden'), Js('huge'), Js('lack of a'), Js('mischievous'), Js('pointed'), Js('seemingly angry'), Js('seemingly expressionless'), Js('seemingly invisible'), Js('small'), Js('smiling'), Js('tiny'), Js('toothed'), Js('tranquil looking')]))
var.put('flyBeak', Js([Js('crescent'), Js('reinforced'), Js('broad'), Js('crooked'), Js('curved'), Js('decorated'), Js('glowing'), Js('jagged'), Js('black'), Js('painted'), Js('patterned'), Js('pointy'), Js('powerful'), Js('razor sharp'), Js('seemingly frowning'), Js('seemingly smiling'), Js('seemingly smirking'), Js('sharp')]))
var.put('flyTail', Js([Js('a barbed tail'), Js('a cloak-like tail'), Js('a cloud-like tail'), Js('a fan-like tail'), Js('a muscular tail'), Js('a powerful tail'), Js('a puffy, round tail'), Js('a rainbow colored tail'), Js('a rather small tail'), Js('a ribbon-like tail'), Js('a set of tails'), Js('an elongated tail'), Js('an incredibly long, ribbon-like tail'), Js('several tails in a fan-like shape'), Js('two tails instead of one')]))
var.put('flyEars', Js([Js('an extra pair of'), Js('wing-like'), Js('antenna-like'), Js('antler-like'), Js('fan-like'), Js('feather-like'), Js('fluffy'), Js('hidden'), Js('horn-like'), Js('huge'), Js('orb-like'), Js('pointy'), Js('puffy'), Js('rounded'), Js('seemingly invisible'), Js('tiny')]))
var.put('flyHorns', Js([Js('ridged'), Js('blade-like'), Js('curled'), Js('curved'), Js('jagged'), Js('mohawk-like'), Js('pointy'), Js('rounded'), Js('sharp'), Js('small'), Js('stubby')]))
var.put('ghostSkin', Js([Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('black'), Js('black and crimson'), Js('blue and black'), Js('crimson'), Js('dark'), Js('dark blue'), Js('gaseous'), Js('glowing'), Js('hazy'), Js('luminous'), Js('purple'), Js('see through'), Js('translucent')]))
var.put('ghostLegs', Js([Js('elongated'), Js('gaseous'), Js('hanging'), Js('hidden'), Js('hovering'), Js('ribbon-like'), Js('shrouded'), Js('stumpy'), Js('suspended'), Js('tiny'), Js('veiled'), Js('wavy')]))
var.put('ghostArms', Js([Js('folded'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('blade-like'), Js('cloak-like'), Js('dangling'), Js('floating'), Js('glowing'), Js('hanging'), Js('often invisible'), Js('ribbon-like'), Js('shield-like'), Js('stretched'), Js('stubby'), Js('wavy')]))
var.put('ghostWings', Js([Js('angular'), Js('angelic'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('cloak-like'), Js('cloth-like'), Js('cloud-like'), Js('enormous'), Js('gaseous'), Js('glowing'), Js('inflatable'), Js('poncho-like'), Js('powerful'), Js('ribbon-like'), Js('shield-like'), Js('shrouded'), Js('two pairs of')]))
var.put('ghostMouth', Js([Js('tusked'), Js('cavernous'), Js('frowning'), Js('grinning'), Js('hidden'), Js('huge'), Js('serious looking'), Js('shrouded'), Js('smiling'), Js('smirking'), Js('sneering'), Js('toothed'), Js('veiled')]))
var.put('ghostBeak', Js([Js('crescent'), Js('barbed'), Js('black'), Js('blade-like'), Js('crooked'), Js('curved'), Js('dark'), Js('pointy'), Js('razor sharp'), Js('sharp'), Js('shrouded'), Js('smirking'), Js('sneering'), Js('veiled')]))
var.put('ghostSnout', Js([Js('tusked'), Js('horned'), Js('bearded'), Js('black'), Js('dark'), Js('frowning'), Js('grinning'), Js('lack of a'), Js('mostly hidden'), Js('partially hidden'), Js('serious looking'), Js('shrouded'), Js('smiling'), Js('smirking'), Js('veiled')]))
var.put('ghostTail', Js([Js('a broad tail, ribbon-like tail'), Js('a fan-like tail'), Js('a gaseous tail'), Js('a hovering tail'), Js('a long tail floating gently in the air'), Js('a long tail wrapped around its body'), Js('a long, ribbon-like tail'), Js('a spiky tail'), Js('a tail like a cape'), Js('several ribbon-like tails'), Js('several tails instead of one'), Js('two tails instead of one')]))
var.put('ghostEars', Js([Js('antenna-like'), Js('wing-like'), Js('broad'), Js('broken'), Js('curved'), Js('floppy'), Js('hat-like'), Js('horn-like'), Js('inflatable'), Js('pointy'), Js('rounded'), Js('stubby'), Js('stumpy'), Js('tiny')]))
var.put('ghostHorns', Js([Js('ridged'), Js('a crown of'), Js('antler-like'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('broken'), Js('curled'), Js('curved'), Js('flame-like'), Js('glowing'), Js('mohawk-like'), Js('moon-shaped'), Js('several rows'), Js('sharp'), Js('two pairs of')]))
var.put('grassSkin', Js([Js('bark-like'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('blossoming'), Js('camouflaged'), Js('emerald'), Js('glowing'), Js('grass-like'), Js('green'), Js('jade'), Js('leafy'), Js('lush'), Js('mossy'), Js('sprouting'), Js('thorny'), Js('verdigris'), Js('vine-like'), Js('viridian')]))
var.put('grassLegs', Js([Js('ridged'), Js('an extra pair of'), Js('bark-like'), Js('brown'), Js('elongated'), Js('flower covered'), Js('leaf covered'), Js('leaf shrouded'), Js('lean'), Js('root-like'), Js('seed shaped'), Js('slim'), Js('stumpy'), Js('thick'), Js('trunk-like'), Js('veiled')]))
var.put('grassArms', Js([Js('ridged'), Js('folded'), Js('stalk-like'), Js('blossoming'), Js('broccoli-like'), Js('fan-like'), Js('leaf'), Js('leaf-like'), Js('petal'), Js('ribbon-like'), Js('small'), Js('sprouting'), Js('stumpy'), Js('thick'), Js('thorny'), Js('vine')]))
var.put('grassWings', Js([Js('angular'), Js('blade-like'), Js('blossoming'), Js('budding'), Js('fan-like'), Js('flowering'), Js('leaf'), Js('leaf-like'), Js('needle'), Js('petal'), Js('ribbon-like'), Js('sprouting'), Js('stalk-like'), Js('two sets of')]))
var.put('grassMouth', Js([Js('bark-like'), Js('hidden'), Js('huge'), Js('lack of a'), Js('prickly'), Js('sharp toothed'), Js('smiling'), Js('smirking'), Js('thorny'), Js('tiny')]))
var.put('grassBeak', Js([Js('crescent'), Js('bark-like'), Js('blossoming'), Js('broad'), Js('curved'), Js('humongous'), Js('leaf shaped'), Js('needle'), Js('mostly overgrown'), Js('sharp'), Js('shining'), Js('stubby'), Js('thorn-like'), Js('thorny')]))
var.put('grassSnout', Js([Js('tusked'), Js('horned'), Js('bearded'), Js('blossoming'), Js('broad'), Js('flower covered'), Js('gentle'), Js('huge'), Js('leaf covered'), Js('leaf shrouded'), Js('mossy'), Js('mostly overgrown'), Js('pointy'), Js('sharp'), Js('smiling'), Js('stubby'), Js('thorny')]))
var.put('grassTail', Js([Js('a bioluminescent tail'), Js('a blossoming tail'), Js('a fan-like tail'), Js('a leafy tail'), Js('a moss covered tail'), Js('a mostly overgrown tail'), Js('a mushroom as a tail'), Js('a needle-like tail'), Js('a stubby tail'), Js('a tail full of flowers'), Js('a thorny tail'), Js('a trunk-like tail'), Js('a vine-like tail'), Js('an evergrowing tail'), Js('several vine-like tails')]))
var.put('grassEars', Js([Js('blossoming'), Js('wing-like'), Js('flower'), Js('flowery'), Js('fluffy'), Js('huge'), Js('leaf-like'), Js('leafy'), Js('mushroom'), Js('mushroom-like'), Js('needle-like'), Js('pollen-like'), Js('round'), Js('sprouting'), Js('thorny'), Js('tiny'), Js('vine-like')]))
var.put('grassHorns', Js([Js('ridged'), Js('a crown of'), Js('blossoming'), Js('curled'), Js('curved'), Js('flowering'), Js('hidden'), Js('mushroom shaped'), Js('needle'), Js('overgrown'), Js('pointy'), Js('rounded'), Js('sharp'), Js('spiky'), Js('spotted')]))
var.put('groundSkin', Js([Js('amber'), Js('brown'), Js('brown and gray'), Js('bulky'), Js('camouflaged'), Js('coarse'), Js('compact'), Js('dark'), Js('dull'), Js('dusty'), Js('gray'), Js('hazel'), Js('muddy'), Js('plated'), Js('sandy'), Js('sepia'), Js('shielded'), Js('solid'), Js('thick')]))
var.put('groundLegs', Js([Js('ridged'), Js('an extra pair of'), Js('armored'), Js('coarse'), Js('elongated'), Js('fluffy'), Js('heavy'), Js('huge'), Js('muscular'), Js('powerful'), Js('protected'), Js('robust'), Js('short'), Js('stumpy'), Js('thick')]))
var.put('groundArms', Js([Js('ridged'), Js('blade-like'), Js('clawed'), Js('dig-efficient'), Js('drill-like'), Js('elongated'), Js('fluffy'), Js('folded'), Js('lean'), Js('muscular'), Js('short'), Js('shovel-like'), Js('strong'), Js('stumpy'), Js('thick')]))
var.put('groundMouth', Js([Js('bearded'), Js('broad'), Js('cavernous'), Js('frowning'), Js('grinning'), Js('huge'), Js('lack of a'), Js('pointy'), Js('powerful'), Js('seemingly expressionless'), Js('shrouded'), Js('small'), Js('smiling'), Js('tiny'), Js('tusked'), Js('veiled')]))
var.put('groundBeak', Js([Js('blunt'), Js('bone-like'), Js('broad'), Js('crescent'), Js('curved'), Js('horn-like'), Js('huge'), Js('humongous'), Js('jagged'), Js('large'), Js('reinforced'), Js('sharp'), Js('small'), Js('stone'), Js('stubby')]))
var.put('groundSnout', Js([Js('bearded'), Js('broad'), Js('coarse'), Js('flat'), Js('frowning'), Js('grinning'), Js('horned'), Js('large'), Js('pointy'), Js('protected'), Js('reinforced'), Js('sharp toothed'), Js('shielded'), Js('small'), Js('smiling'), Js('smirking'), Js('stubby'), Js('tusked')]))
var.put('groundTail', Js([Js('a barbed tail'), Js('a bony tail'), Js('a broad tail'), Js('a bruised tail'), Js('a fab-like tail'), Js('a forked tail'), Js('a long, thin tail'), Js('a muscular tail'), Js('a powerful tail'), Js('a short, stubby tail'), Js('a shovel-like tail'), Js('a strong and nimble tail'), Js('a stubby tail'), Js('a tail suitable for digging'), Js('an armor plated tail'), Js('several tails instead of one'), Js('two tails instead of one')]))
var.put('groundEars', Js([Js('antenna-like'), Js('bone-like'), Js('broken'), Js('coarse'), Js('flabby'), Js('flappy'), Js('horn-like'), Js('huge'), Js('jagged'), Js('orb-like'), Js('pointy'), Js('rounded'), Js('stubby'), Js('thorny'), Js('wing-like')]))
var.put('groundHorns', Js([Js('ridged'), Js('a crown of'), Js('blunt'), Js('broad'), Js('broken'), Js('coarse'), Js('curled'), Js('curved'), Js('drill-like'), Js('mohawk-like'), Js('orb-like'), Js('sharp'), Js('shield-like'), Js('shovel-like'), Js('stubby')]))
var.put('iceSkin', Js([Js('azure'), Js('blue'), Js('blue and white'), Js('cobalt'), Js('frost covered'), Js('frosty'), Js('glacial'), Js('ice cold'), Js('icy'), Js('ivory'), Js('reflective'), Js('sapphire'), Js('silvery'), Js('smooth'), Js('thick'), Js('pure white')]))
var.put('iceLegs', Js([Js('ridged'), Js('an extra pair of'), Js('fat'), Js('fluffy'), Js('ice covered'), Js('muscular'), Js('powerful'), Js('short'), Js('snowy'), Js('stout'), Js('strong'), Js('stubby'), Js('thick')]))
var.put('iceArms', Js([Js('ridged'), Js('folded'), Js('cloak-like'), Js('fan-like'), Js('fat'), Js('fluffy'), Js('icicle-like'), Js('lean'), Js('muscular'), Js('ribbon-like'), Js('scarf-like'), Js('strong'), Js('stubby'), Js('warming')]))
var.put('iceWings', Js([Js('angular'), Js('cloak-like'), Js('enormous'), Js('frost covered'), Js('frosty'), Js('gigantic'), Js('icy'), Js('reflective'), Js('ribbon-like'), Js('scarf-like'), Js('shield-like'), Js('shimmering'), Js('shivering'), Js('sleeted'), Js('smooth'), Js('stalactite covered'), Js('glowing')]))
var.put('iceMouth', Js([Js('bearded'), Js('broad'), Js('cavernous'), Js('crystal'), Js('frowning'), Js('fur covered'), Js('hidden'), Js('icicle covered'), Js('icicle toothed'), Js('serious looking'), Js('smiling'), Js('smirking'), Js('sparkling'), Js('tiny')]))
var.put('iceBeak', Js([Js('crescent'), Js('broad'), Js('crystal'), Js('curved'), Js('frost covered'), Js('large, icicle-like'), Js('pointy'), Js('reflective'), Js('rimy'), Js('sapphire'), Js('sharp'), Js('silvery'), Js('sleeted'), Js('small, icicle-like')]))
var.put('iceSnout', Js([Js('tusked'), Js('horned'), Js('bearded'), Js('broad'), Js('densely icicle-covered'), Js('fluffy'), Js('frost covered'), Js('frosty'), Js('frowning'), Js('fur covered'), Js('smiling'), Js('smirking'), Js('stubby'), Js('thinly icicle-covered'), Js('tranquil looking')]))
var.put('iceTail', Js([Js('a broad, fan-like tail'), Js('a fluffy tail'), Js('a frost covered tail'), Js('a frosty tail'), Js('a long, fluffy tail wrapped around its body'), Js('a ribbon-like tail'), Js('a short and stubby tail'), Js('a tail wrapped around its body like a scarf'), Js('an icicle covered tail'), Js('an icicle-like tail'), Js('an icy, reflective tail'), Js('several tails instead of one'), Js('two tails instead of one')]))
var.put('iceEars', Js([Js('crystal-like'), Js('fluffy'), Js('frosty'), Js('furry'), Js('fuzzy'), Js('huge'), Js('ice-like'), Js('icicle'), Js('icy'), Js('pointy'), Js('reflective'), Js('round'), Js('snowball-like'), Js('snowflake-like'), Js('tiny')]))
var.put('iceHorns', Js([Js('ridged'), Js('a crown of'), Js('antler-like'), Js('broad'), Js('crystal'), Js('curved'), Js('diamond shaped'), Js('freezing'), Js('frosty'), Js('ice-like'), Js('icicle'), Js('icy, crystal-like'), Js('pointy'), Js('reflective'), Js('short'), Js('sleeted'), Js('stubby')]))
var.put('normSkin', Js([Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('coarse'), Js('dirt covered'), Js('dull'), Js('glossy'), Js('glowing'), Js('luminous'), Js('lustrous'), Js('messy'), Js('radiant'), Js('silky'), Js('smooth'), Js('unkempt'), Js('velvety'), Js('vibrant'), Js('vivid')]))
var.put('normLegs', Js([Js('ridged'), Js('an extra pair of'), Js('armored'), Js('elongated'), Js('enlarged'), Js('huge'), Js('lean'), Js('muscular'), Js('powerful'), Js('short'), Js('stour'), Js('stubby'), Js('thick'), Js('tiny'), Js('withdrawn')]))
var.put('normArms', Js([Js('ridged'), Js('folded'), Js('armored'), Js('cloak-like'), Js('elongated'), Js('fat'), Js('fluffy'), Js('lean'), Js('little'), Js('long'), Js('slim'), Js('small'), Js('strong'), Js('stubby'), Js('tiny')]))
var.put('normWings', Js([Js('angular'), Js('broad'), Js('cloak-like'), Js('elongated'), Js('enormous'), Js('fluffy'), Js('humongous'), Js('layered'), Js('pointy'), Js('ribbon-like'), Js('sharp'), Js('slender'), Js('smooth'), Js('thick'), Js('two pairs of')]))
var.put('normMouth', Js([Js('bearded'), Js('blunt toothed'), Js('broad'), Js('cavernous'), Js('frowning'), Js('grinning'), Js('hidden'), Js('humongous'), Js('serious looking'), Js('sharp toothed'), Js('small'), Js('smiling'), Js('smirking'), Js('tiny'), Js('veiled')]))
var.put('normBeak', Js([Js('crescent'), Js('blunt'), Js('broad'), Js('crooked'), Js('curved'), Js('flattened'), Js('huge'), Js('sharp'), Js('slim'), Js('thin'), Js('needle-like')]))
var.put('normSnout', Js([Js('tusked'), Js('horned'), Js('bearded'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('broad'), Js('fluffy'), Js('frowning'), Js('glowing'), Js('large'), Js('pointy'), Js('smiling'), Js('smirking'), Js('stubby')]))
var.put('normTail', Js([Js('a fluffy tail'), Js('a forked tail'), Js('a glowing tail'), Js('a long tail wrapped around its body'), Js('a ribbon-like tail'), Js('a short, rounded tail'), Js('a stubby little tail'), Js('a thick fluffy tail'), Js('an elongated tail'), Js('several tails instead of one'), Js('two tails instead of one')]))
var.put('normEars', Js([Js('enlarged'), Js('wing-like'), Js('enormous'), Js('flabby'), Js('flappy'), Js('fluffy'), Js('horn-like'), Js('humongous'), Js('large'), Js('little'), Js('pointy'), Js('rounded'), Js('stubby'), Js('tiny')]))
var.put('normHorns', Js([Js('ridged'), Js('a crown of'), Js('antler-like'), Js('blade-like'), Js('broken'), Js('curled'), Js('curved'), Js('fan-like'), Js('mohawk-like'), Js('pointy'), Js('rounded'), Js('sharp'), Js('spiked'), Js('stubby'), Js('stumpy')]))
var.put('poisonSkin', Js([Js('armored'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('camouflaged'), Js('dark'), Js('darkened'), Js('glossy'), Js('glowing'), Js('grimy'), Js('luminous'), Js('magenta'), Js('purple'), Js('shiny'), Js('silky'), Js('smooth'), Js('vibrant'), Js('violet'), Js('vivid')]))
var.put('poisonLegs', Js([Js('ridged'), Js('an extra pair of'), Js('armored'), Js('elongated'), Js('hidden'), Js('lean'), Js('long'), Js('muscular'), Js('powerful'), Js('scaly'), Js('skinny'), Js('slimy'), Js('stumpy'), Js('thin')]))
var.put('poisonArms', Js([Js('ridged'), Js('folded'), Js('armored'), Js('barbed'), Js('broad'), Js('clawed'), Js('elongated'), Js('fat'), Js('lean'), Js('little'), Js('muscular'), Js('ribbon-like'), Js('small'), Js('strong'), Js('stubby'), Js('thorny')]))
var.put('poisonWings', Js([Js('angular'), Js('barbed'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('blade-like'), Js('cloak-like'), Js('elongated'), Js('enormous'), Js('glowing'), Js('layered'), Js('pointy'), Js('reflective'), Js('ribbon-like'), Js('scaly'), Js('sharp'), Js('smooth'), Js('thin'), Js('thorny'), Js('translucent')]))
var.put('poisonMouth', Js([Js('tusked'), Js('cavernous'), Js('grinning'), Js('hidden'), Js('huge'), Js('lack of a'), Js('noxious'), Js('sharp toothed'), Js('shrouded'), Js('smirking'), Js('thorny'), Js('tiny'), Js('veiled'), Js('venomous')]))
var.put('poisonBeak', Js([Js('crescent'), Js('blunt'), Js('broad'), Js('curved'), Js('hidden'), Js('noxious'), Js('pointy'), Js('razor sharp'), Js('sharp'), Js('smirking'), Js('toothed'), Js('veiled'), Js('venomous')]))
var.put('poisonSnout', Js([Js('bearded'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('fluffy'), Js('glowing'), Js('grimy'), Js('horned'), Js('luminous'), Js('noxious'), Js('protected'), Js('shrouded'), Js('slimy'), Js('stubby'), Js('tusked'), Js('veiled'), Js('venomous')]))
var.put('poisonTail', Js([Js('a barbed tail'), Js('a bioluminescent tail'), Js('a forked tail'), Js('a glowing tail'), Js('a long tail wrapped around its body'), Js('a long, whip-like tail'), Js('a rattling tail'), Js('a slimy tail'), Js('a spiky tail'), Js('a spring-like tail'), Js('a tail with a stinger at the end'), Js('a thorny tail'), Js('a venomous tail'), Js('several tails instead of one'), Js('two tails instead of one')]))
var.put('poisonEars', Js([Js('a lack of'), Js('wing-like'), Js('chimney-like'), Js('fan-like'), Js('flabby'), Js('flappy'), Js('fluffy'), Js('gooey'), Js('hairy'), Js('horn-like'), Js('huge'), Js('mucky'), Js('pointy'), Js('spiky'), Js('stubby'), Js('vent-like')]))
var.put('poisonHorns', Js([Js('ridged'), Js('a crown of'), Js('antler-like'), Js('barbed'), Js('blade-like'), Js('broken'), Js('chimney-like'), Js('curled'), Js('curved'), Js('ejectable'), Js('fan-like'), Js('looping'), Js('mohawk-like'), Js('spiky'), Js('stinger-like'), Js('thorny'), Js('venomous'), Js('vent-like')]))
var.put('psySkin', Js([Js('armored'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('black and white'), Js('camouflaged'), Js('dark'), Js('darkened'), Js('glossy'), Js('glowing'), Js('luminous'), Js('obsidian'), Js('pink and purple'), Js('pink and white'), Js('purple'), Js('smooth'), Js('vermilion'), Js('white')]))
var.put('psyLegs', Js([Js('an extra pair of'), Js('broad'), Js('elongated'), Js('fat'), Js('hidden'), Js('hovering'), Js('lean'), Js('muscular'), Js('patterned'), Js('powerful'), Js('short'), Js('shrouded'), Js('stubby'), Js('thick'), Js('thin'), Js('veiled')]))
var.put('psyArms', Js([Js('armored'), Js('cloak-like'), Js('elongated'), Js('fan-like'), Js('fat'), Js('folded'), Js('lean'), Js('long'), Js('muscular'), Js('ribbon-like'), Js('shrouded'), Js('slender'), Js('stumpy')]))
var.put('psyWings', Js([Js('angelic'), Js('angular'), Js('armored'), Js('blade-like'), Js('body wrapping'), Js('cloak-like'), Js('darkened'), Js('enormous'), Js('gaseous'), Js('glossy'), Js('huge'), Js('reflective'), Js('ribbon-like'), Js('shadowy'), Js('smooth')]))
var.put('psyMouth', Js([Js('bearded'), Js('broad'), Js('frowning'), Js('grinning'), Js('hidden'), Js('lack of a'), Js('pointy'), Js('seemingly expressionless'), Js('serene looking'), Js('shrouded'), Js('smiling'), Js('smirking'), Js('tiny'), Js('tusked'), Js('veiled')]))
var.put('psyBeak', Js([Js('crescent'), Js('blunt'), Js('crooked'), Js('curved'), Js('flat'), Js('metal'), Js('razor sharp'), Js('sharp'), Js('shrouded'), Js('smirking'), Js('thorny'), Js('toothed'), Js('veiled')]))
var.put('psySnout', Js([Js('bearded'), Js('bioluminescent'), Js('phosphorescent'), Js('fluorescent'), Js('broad'), Js('flat'), Js('fluffy'), Js('glowing'), Js('hairy'), Js('horned'), Js('huge'), Js('humongous'), Js('large'), Js('long'), Js('protected'), Js('shrouded'), Js('small'), Js('stubby'), Js('tiny'), Js('tusked'), Js('veiled')]))
var.put('psyTail', Js([Js('a barbed tail'), Js('a bioluminescent tail'), Js('a forked tail'), Js('a long, decorated tail'), Js('a long, muscular tail'), Js('a ribbon-like tail'), Js('a spiky tail'), Js('a tail ending in a crescent shape'), Js('a tail that ends in a fan-like shape'), Js('a tail that ends in an orb shape'), Js('a tail that has been tied into a knot'), Js('a tail that hovers gently in the air'), Js('a tail that wraps completely around its body'), Js('a tail with a crystal on its tip'), Js('a tail with a gem on its tip'), Js('an armored tail'), Js('an incredibly long tail'), Js('several tails instead of one'), Js('two tails instead of one')]))
var.put('psyEars', Js([Js('antenna-like'), Js('wing-like'), Js('elongated'), Js('enormous'), Js('fan-like'), Js('flabby'), Js('flappy'), Js('fuzzy'), Js('hidden'), Js('horn-like'), Js('long'), Js('pointy'), Js('rounded'), Js('shrouded'), Js('stubby'), Js('two sets of'), Js('veiled')]))
var.put('psyHorns', Js([Js('ridged'), Js('a crown of'), Js('antenna-like'), Js('antler-like'), Js('barbed'), Js('blade-like'), Js('broken'), Js('connected'), Js('curled'), Js('curved'), Js('huge'), Js('looping'), Js('pointy'), Js('sharp'), Js('thick'), Js('two sets of')]))
var.put('rockSkin', Js([Js('crystal'), Js('gem encrusted'), Js('amber'), Js('armored'), Js('boulder-like'), Js('brown'), Js('brown and gray'), Js('bulky'), Js('compact'), Js('dark'), Js('dusty'), Js('gray'), Js('hard'), Js('hazel'), Js('muddy'), Js('plated'), Js('rock-like'), Js('sandy'), Js('sepia'), Js('shielded'), Js('solid'), Js('thick')]))
var.put('rockLegs', Js([Js('ridged'), Js('an extra pair of'), Js('armor plated'), Js('armored'), Js('coarse'), Js('heavy'), Js('huge'), Js('muscular'), Js('powerful'), Js('protected'), Js('robust'), Js('rock-like'), Js('short'), Js('stone covered'), Js('stumpy')]))
var.put('rockArms', Js([Js('ridged'), Js('folded'), Js('armor plated'), Js('armored'), Js('elongated'), Js('gem adorned'), Js('lean'), Js('muscular'), Js('rocky'), Js('rough textured'), Js('short'), Js('stalagmite-like'), Js('strong'), Js('stumpy'), Js('thick'), Js('two sets of')]))
var.put('rockMouth', Js([Js('broad'), Js('cavernous'), Js('crystal'), Js('crystal toothed'), Js('frowning'), Js('grinning'), Js('powerful'), Js('seemingly expressionless'), Js('small'), Js('stalactite toothed'), Js('stalgmite and stalactite toothed'), Js('stone'), Js('tusked')]))
var.put('rockBeak', Js([Js('crescent'), Js('reinforced'), Js('blunt'), Js('bone-like'), Js('broad'), Js('crystal'), Js('curved'), Js('gem-like'), Js('jagged'), Js('sharp'), Js('stone'), Js('stubby')]))
var.put('rockSnout', Js([Js('tusked'), Js('horned'), Js('bone covered'), Js('broad'), Js('coarse'), Js('crystal'), Js('flat'), Js('hardened'), Js('protected'), Js('shielded'), Js('stubby'), Js('large'), Js('small')]))
var.put('rockTail', Js([Js('a broad tail'), Js('a bruised tail'), Js('a gem encrusted tail'), Js('a hammer-like tail'), Js('a muscular tail'), Js('a powerful tail'), Js('a shovel-like tail'), Js('a strong and nimble tail'), Js('a stubby tail'), Js('a tail full of stalactites'), Js('a tail like a stalactite'), Js('a tail like a stalagmite'), Js('a tail suitable for digging'), Js('an armor plated tail')]))
var.put('rockEars', Js([Js('bone-like'), Js('boulder-like'), Js('broken'), Js('coarse'), Js('crystal'), Js('diamond'), Js('flappy'), Js('flabby'), Js('gem encrusted'), Js('horn-like'), Js('huge'), Js('pointy'), Js('rock-like'), Js('rounded'), Js('shield-like'), Js('stone'), Js('stubby')]))
var.put('rockHorns', Js([Js('ridged'), Js('a crown of'), Js('blunt'), Js('broad'), Js('broken'), Js('coarse'), Js('crystal'), Js('curled'), Js('curved'), Js('diamond'), Js('drill-like'), Js('gem encrusted'), Js('metal'), Js('obsidian'), Js('sharp'), Js('stone')]))
var.put('steelSkin', Js([Js('armored'), Js('bronze'), Js('copper'), Js('glistening'), Js('golden'), Js('gray'), Js('heavily armored'), Js('incredibly thick'), Js('iron'), Js('jagged'), Js('layered'), Js('magnetic'), Js('metal'), Js('reflective'), Js('sharp'), Js('shiny'), Js('silvery'), Js('smooth'), Js('spiky')]))
var.put('steelLegs', Js([Js('ridged'), Js('an extra pair of'), Js('armor plated'), Js('armored'), Js('blade-like'), Js('glistening'), Js('heavy set'), Js('honed'), Js('huge'), Js('magnetic'), Js('powerful'), Js('reflective'), Js('sharpened'), Js('shielded'), Js('smooth'), Js('spiked'), Js('steel-plated'), Js('thick')]))
var.put('steelArms', Js([Js('ridged'), Js('folded'), Js('armored'), Js('blade-like'), Js('elongated'), Js('energized'), Js('lean'), Js('metal-plated'), Js('pincer-like'), Js('reinforced'), Js('shielded'), Js('smooth'), Js('spiky'), Js('stubby'), Js('sturdy'), Js('thick')]))
var.put('steelWings', Js([Js('armored'), Js('blade-like'), Js('enormous'), Js('fan-like'), Js('honed'), Js('humongous'), Js('layered'), Js('magnetized'), Js('powerful'), Js('reflective'), Js('reinforced'), Js('sharp'), Js('shield-like'), Js('smooth'), Js('thick'), Js('thin')]))
var.put('steelMouth', Js([Js('broad'), Js('frowning'), Js('hidden'), Js('huge'), Js('jagged'), Js('lack of a'), Js('powerful'), Js('reinforced'), Js('seemingly expressionless'), Js('sharp'), Js('sharp toothed'), Js('shrouded'), Js('smiling'), Js('smirking'), Js('tusked')]))
var.put('steelBeak', Js([Js('crescent'), Js('crooked'), Js('curved'), Js('glistening'), Js('glowing'), Js('huge'), Js('humongous'), Js('luminous'), Js('metal'), Js('pincer-like'), Js('pointy'), Js('razor sharp'), Js('reinforced'), Js('sharp'), Js('shiny'), Js('smooth'), Js('steel plated')]))
var.put('steelSnout', Js([Js('bearded'), Js('broadened'), Js('hidden'), Js('metal'), Js('metal covered'), Js('metal plated'), Js('metal toothed'), Js('metal tusked'), Js('powerful'), Js('protective'), Js('reinforced'), Js('shrouded'), Js('spiky'), Js('stubby'), Js('tusked')]))
var.put('steelTail', Js([Js('a blade-like tail'), Js('a fan-like tail'), Js('a forked, blade-like tail'), Js('a glowing, bioluminescent tail'), Js('a glowing, metallic tail'), Js('a long tail wrapped around its body'), Js('a long, energized tail'), Js('a long, spiky tail'), Js('a magnetized tail'), Js('a metal scaled tail'), Js('a short, spike-like tail'), Js('a short, stumpy tail'), Js('a tail ending in a massive orb-like shape'), Js('a tail ending in a u-shape magnet'), Js('a thick, reflective tail'), Js('an armor plated tail'), Js('an elongated tail'), Js('several tails instead of one'), Js('two tails instead of one')]))
var.put('steelEars', Js([Js('a lack of'), Js('antenna-like'), Js('blade-like'), Js('cog-shaped'), Js('covered'), Js('enormous'), Js('fan-like'), Js('helmet-like'), Js('huge'), Js('jagged'), Js('pointy'), Js('shielded'), Js('spiky'), Js('thick'), Js('tiny'), Js('u-shaped')]))
var.put('steelHorns', Js([Js('ridged'), Js('a crown of'), Js('antenna-like'), Js('antler-like'), Js('barbed'), Js('coil-like'), Js('curled'), Js('curved'), Js('enormous'), Js('forked'), Js('honed'), Js('keen'), Js('looping'), Js('mohawk-like'), Js('needle-like'), Js('pointy'), Js('razor sharp'), Js('spiky'), Js('stubby'), Js('u-shaped magnet')]))
var.put('waterSkin', Js([Js('azure'), Js('bioluminescent'), Js('cerulean'), Js('coral'), Js('darkened'), Js('fluorescent'), Js('glistening'), Js('glossy'), Js('phosphorescent'), Js('salmon'), Js('sapphire'), Js('shimmering'), Js('shiny'), Js('silky'), Js('smooth'), Js('sparkling'), Js('teal'), Js('turquoise'), Js('ultramarine'), Js('velvety'), Js('white and blue')]))
var.put('waterLegs', Js([Js('ridged'), Js('an extra pair of'), Js('coral encrusted'), Js('elongated'), Js('fat'), Js('fatty'), Js('firm'), Js('lean'), Js('muscular'), Js('scaly'), Js('shell covered'), Js('shiny'), Js('smooth'), Js('steady'), Js('stubby'), Js('thick')]))
var.put('waterArms', Js([Js('an extra pair of'), Js('coral encrusted'), Js('elongated'), Js('fat'), Js('folded'), Js('long'), Js('pincer-like'), Js('ribbon-like'), Js('ridged'), Js('scaly'), Js('shell covered'), Js('short'), Js('slim'), Js('smooth'), Js('stubby')]))
var.put('waterWings', Js([Js('angelic'), Js('bioluminescent'), Js('cloak-like'), Js('enormous'), Js('fin-like'), Js('flipper-like'), Js('fluorescent'), Js('glistening'), Js('glowing'), Js('layered'), Js('phosphorescent'), Js('ribbon-like'), Js('scaly'), Js('shimmering'), Js('smooth')]))
var.put('waterMouth', Js([Js('bearded'), Js('blunt toothed'), Js('broad'), Js('cavernous'), Js('frowning'), Js('grinning'), Js('pointy'), Js('sharp toothed'), Js('shrouded'), Js('small'), Js('smiling'), Js('smirking'), Js('tusked')]))
var.put('waterBeak', Js([Js('bioluminescent'), Js('blunt'), Js('broad'), Js('crescent'), Js('curved'), Js('glistening'), Js('glowing'), Js('pointy'), Js('sapphire'), Js('seemingly smiling'), Js('shell-like'), Js('shiny'), Js('stubby'), Js('wavy')]))
var.put('waterSnout', Js([Js('bearded'), Js('bioluminescent'), Js('broad'), Js('coral covered'), Js('flat'), Js('fluffy'), Js('horned'), Js('huge'), Js('pointy'), Js('shell covered'), Js('smooth'), Js('sparkling'), Js('stubby'), Js('trumpet-like'), Js('tusked')]))
var.put('waterTail', Js([Js('a bioluminescent tail'), Js('a broad, fan-like tail'), Js('a coral covered tail'), Js('a forked tail'), Js('a glowing tail'), Js('a huge, cloak-like tail'), Js('a long, curled up tail'), Js('a long, ribbon-like tail'), Js('a long, smooth tail'), Js('a long, wavy tail'), Js('a ridged tail'), Js('a shell covered tail'), Js('a short and tiny tail'), Js('a strong, muscular tail'), Js('a stubby, fin-like tail'), Js('several tails instead of one'), Js('two tails instead of one')]))
var.put('waterEars', Js([Js('antenna-like'), Js('curled'), Js('enormous'), Js('fin-like'), Js('flabby'), Js('flappy'), Js('flipper-like'), Js('orb-like'), Js('shell covered'), Js('shell-like'), Js('short'), Js('shrouded'), Js('stubby'), Js('two sets of'), Js('wavy')]))
var.put('waterHorns', Js([Js('antler-like'), Js('a crown of'), Js('antenna-like'), Js('bioluminescent'), Js('coral covered'), Js('coral-like'), Js('curled'), Js('curved'), Js('fin-like'), Js('flipper-like'), Js('glowing'), Js('looping'), Js('ridged'), Js('shell-like'), Js('short'), Js('smooth'), Js('stubby'), Js('wavy')]))
var.put('placeBug', Js([Js('in labyrinths'), Js('during summer'), Js('in national parks'), Js('in bushes'), Js('in farmlands'), Js('in fields'), Js('in forests'), Js('in gardens'), Js('in grassy fields'), Js('in meadows'), Js('in parks'), Js('in pastures'), Js('in tree tops'), Js('in valleys'), Js('in vineyards')]))
var.put('placeDark', Js([Js('in labyrinths'), Js('in dark caves'), Js('at midnight'), Js('in caverns'), Js('in caves'), Js('in chasms'), Js('in dark forests'), Js('in dens'), Js('in grottoes'), Js('in ruins'), Js('in shadowy places'), Js('in the early morning'), Js('in the evening'), Js('in the middle of the night'), Js('in thick forests')]))
var.put('placeDragon', Js([Js('during heavy clouded weather'), Js('during periods of heavy winds'), Js('high up in the air'), Js('in canyons'), Js('in massive caves'), Js('in mountainous areas'), Js('in ruins'), Js('in towers'), Js('on deserted islands'), Js('on mountain tops')]))
var.put('placeElectric', Js([Js('in labyrinths'), Js('after thunderstorms'), Js('during the day'), Js('during the night'), Js('during thunderstorms'), Js('in dark caves'), Js('in ruins'), Js('in valleys'), Js('near power facilities'), Js('near power plants')]))
var.put('placeFairy', Js([Js('in dense forests'), Js('in hilly areas'), Js('in labyrinths'), Js('in large cave systems'), Js('in large forests'), Js('in the early morning'), Js('in the late evening hours'), Js('near mountains'), Js('near sanctuaries'), Js('near shrines')]))
var.put('placeFighting', Js([Js('in cave systems'), Js('in dense forests'), Js('in hilly areas'), Js('in labyrinths'), Js('in mountain caves'), Js('in open fields'), Js('in rocky hill areas'), Js('in towers'), Js('near cliffs'), Js('near mountain tops'), Js('near ruins')]))
var.put('placeFire', Js([Js('after forest fires'), Js('during summer'), Js('in cave systems'), Js('in deep caves'), Js('in deserty areas'), Js('near hot springs'), Js('near ruins'), Js('near volcanoes'), Js('on deserted islands'), Js('on hot summer days'), Js('on volcanic islands')]))
var.put('placeFlying', Js([Js('high in the sky'), Js('in dense forests'), Js('in gardens'), Js('in large forests'), Js('in meadows'), Js('in national parks'), Js('in open fields'), Js('in parks'), Js('in summer'), Js('in tall grass'), Js('in the evening hours'), Js('in the morning hours'), Js('in tree tops'), Js('in winter')]))
var.put('placeGhost', Js([Js('near temples'), Js('near shrines'), Js('near sanctuaries'), Js('at night'), Js('in abandoned buildings'), Js('in abandoned towers'), Js('in clock towers'), Js('in dark caves'), Js('in dark forests'), Js('in dense forests'), Js('in labyrinths'), Js('in the middle of the night'), Js('near graveyards'), Js('near ruins')]))
var.put('placeGrass', Js([Js('in bushes'), Js('in dense forests'), Js('in farmlands'), Js('in fields'), Js('in flowery meadows'), Js('in forests'), Js('in gardens'), Js('in grassy fields'), Js('in meadows'), Js('in national parks'), Js('in open fields'), Js('in parks'), Js('in pastures'), Js('in summer'), Js('in the early morning'), Js('in the evening hours'), Js('in tree tops'), Js('in valleys'), Js('in vineyards')]))
var.put('placeGround', Js([Js('at night'), Js('in cave systems'), Js('in caves'), Js('in dense forests'), Js('in deserty areas'), Js('in hilly areas'), Js('in labyrinths'), Js('in mountainous areas'), Js('in national parks'), Js('in rocky hill areas'), Js('near cliffs'), Js('near ruins'), Js('on rocky paths'), Js('on sandy paths')]))
var.put('placeIce', Js([Js('after a blizzard'), Js('after a snow storm'), Js('during a blizzard'), Js('during snowy weather'), Js('in icy cave systems'), Js('in snowlands'), Js('in snowy mountain peaks'), Js('in taigas'), Js('in tundras'), Js('in winter'), Js('on cold mountain peaks'), Js('on frozen lakes'), Js('on frozen rivers'), Js('on icy plains')]))
var.put('placeNormal', Js([Js('all around'), Js('at night'), Js('during the day'), Js('in farmlands'), Js('in fields'), Js('in forests'), Js('in gardens'), Js('in hilly areas'), Js('in national parks'), Js('in parks'), Js('in quiet towns'), Js('in the early morning'), Js('in the evening hours'), Js('near beaches'), Js('near ruins'), Js('near sanctuaries'), Js('near temples'), Js('on forest paths')]))
var.put('placePoison', Js([Js('during summer'), Js('hiding in bushes'), Js('hiding in forests'), Js('hiding in tree tops'), Js('in dense forests'), Js('in gardens'), Js('in grassy fields'), Js('in labyrinths'), Js('in meadows'), Js('in parks'), Js('in valleys'), Js('near cliffs')]))
var.put('placePsychic', Js([Js('in abandoned buildings'), Js('in abandoned towers'), Js('in cave systems'), Js('in dark caves'), Js('in dense forests'), Js('in the middle of the night'), Js('near ruins'), Js('near sanctuaries'), Js('near shrines'), Js('near temples'), Js('on deserted islands')]))
var.put('placeRock', Js([Js('in cave systems'), Js('in caverns'), Js('in caves'), Js('in deep cavern systems'), Js('in labyrinths'), Js('in mountain caves'), Js('in mountainous areas'), Js('in rocky hill areas'), Js('in rocky mountains'), Js('near cliffs'), Js('on and near hillsides'), Js('on and near mountains'), Js('on mountain peaks'), Js('on rocky paths')]))
var.put('placeSteel', Js([Js('after meteor showers'), Js('in cave systems'), Js('in caverns'), Js('in dark caves'), Js('in deep cavern systems'), Js('in labyrinths'), Js('near cliffs'), Js('near construction works'), Js('near mines'), Js('near shrines')]))
var.put('placeWater', Js([Js('around harbors'), Js('around high tides'), Js('around low tides'), Js('in forest lakes'), Js('in gentle creeks'), Js('in lagoons'), Js('in large canals'), Js('in park lakes'), Js('in rivers'), Js('in serene lakes'), Js('in swampy areas'), Js('in wild water rapids'), Js('near beaches'), Js('near calm shores'), Js('near coral reefs'), Js('near ocean fronts'), Js('near sea fronts'), Js('near steep coastal areas'), Js('near waterfalls'), Js('on oceanic islands')]))
var.put('pers', Js([Js('aggressive'), Js('apprehensive'), Js('attentive'), Js('carefree'), Js('cautious'), Js('cheerful'), Js('comical'), Js('cordial'), Js('disruptive'), Js('distrustful'), Js('easygoing'), Js('energetic'), Js('fearful'), Js('fidgety'), Js('friendly'), Js('gentle'), Js('hostile'), Js('impish'), Js('inhospitable'), Js('irritable'), Js('jittery'), Js('laid-back'), Js('lively'), Js('mischievous'), Js('placid'), Js('playful'), Js('precarious'), Js('quiet'), Js('receptive'), Js('relaxed'), Js('serene'), Js('shy'), Js('skittish'), Js('sociable'), Js('spiteful'), Js('threatening'), Js('timid'), Js('volatile'), Js('wary'), Js('watchful'), Js('whimsical')]))
var.put('amnt', Js([Js('all around you'), Js('alone or alongside one or two others'), Js('alongside a few others'), Js('alongside other Pokemon'), Js('among many other kinds of Pokemon'), Js('hidden away and on their own'), Js('hiding with several others'), Js('in huge groups'), Js('in small groups'), Js('lurking about and on their own'), Js('lurking with several others'), Js('on their own'), Js('only after giving up your search for them'), Js('only by accident')]))
var.put('wtr', Js([Js('dark'), Js('dragon'), Js('ghost'), Js('ice'), Js('poison'), Js('psychic'), Js('water')]))
var.put('lnd', Js([Js('bug'), Js('dark'), Js('electric'), Js('fairy'), Js('fighting'), Js('fire'), Js('ghost'), Js('grass'), Js('ground'), Js('ice'), Js('normal'), Js('poison'), Js('psychic'), Js('rock'), Js('steel')]))
var.put('air', Js([Js('bug'), Js('dark'), Js('dragon'), Js('electric'), Js('fairy'), Js('fire'), Js('flying'), Js('ghost'), Js('normal'), Js('poison'), Js('psychic')]))
var.put('bug', Js([Js('ant'), Js('bee'), Js('butterfly'), Js('caterpillar'), Js('cockroach'), Js('dragonfly'), Js('fly'), Js('grasshopper'), Js('hornet'), Js('locust'), Js('mosquito'), Js('termite'), Js('wasp')]))
var.put('drg', Js([Js('alligator'), Js('armadillo'), Js('cobra'), Js('crocodile'), Js('dragonfly'), Js('eel'), Js('komodo dragon'), Js('narwhal'), Js('salamander'), Js('seahorse'), Js('snake')]))
var.put('bugAttk', Js([Js('Attack Order'), Js('Bug Bite'), Js('Bug Buzz'), Js('Defend Order'), Js('Fell Stinger'), Js('Fury Cutter'), Js('Heal Order'), Js('Infestation'), Js('Leech Life'), Js('Megahorn'), Js('Pin Missile'), Js('Powder'), Js('Quiver Dance'), Js('Rage Powder'), Js('Signal Beam'), Js('Silver Wind'), Js('Spider Web'), Js('Steamroller'), Js('Sticky Web'), Js('String Shot'), Js('Struggle Bug'), Js('Tail Glow'), Js('Twineedle'), Js('U-turn'), Js('X-Scissor')]))
var.put('darkAttk', Js([Js('Assurance'), Js('Beat Up'), Js('Bite'), Js('Crunch'), Js('Dark Pulse'), Js('Dark Void'), Js('Embargo'), Js('Fake Tears'), Js('Feint Attack'), Js('Flatter'), Js('Fling'), Js('Foul Play'), Js('Hone Claws'), Js('Hyperspace Fury'), Js('Knock Off'), Js('Memento'), Js('Nasty Plot'), Js('Night Daze'), Js('Night Slash'), Js('Parting Shot'), Js('Payback'), Js('Punishment'), Js('Pursuit'), Js('Quash'), Js('Snarl'), Js('Snatch'), Js('Sucker Punch'), Js('Switcheroo'), Js('Taunt'), Js('Thief'), Js('Topsy-Turvy'), Js('Torment')]))
var.put('dragonAttk', Js([Js('Draco Meteor'), Js('Dragon Breath'), Js('Dragon Claw'), Js('Dragon Dance'), Js('Dragon Pulse'), Js('Dragon Rage'), Js('Dragon Rush'), Js('Dragon Tail'), Js('Dual Chop'), Js('Outrage'), Js('Roar of Time'), Js('Spacial Rend'), Js('Twister')]))
var.put('electricAttk', Js([Js('Bolt Strike'), Js('Charge'), Js('Charge Beam'), Js('Discharge'), Js('Eerie Impulse'), Js('Electric Terrain'), Js('Electrify'), Js('Electro Ball'), Js('Electroweb'), Js('Fusion Bolt'), Js('Ion Deluge'), Js('Magnet Rise'), Js('Magnetic Flux'), Js('Nuzzle'), Js('Parabolic Charge'), Js('Shock Wave'), Js('Spark'), Js('Thunder'), Js('Thunder Fang'), Js('Thunder Wave'), Js('Thunderbolt'), Js('Thunder Punch'), Js('Thunder Shock'), Js('Volt Switch'), Js('Volt Tackle'), Js('Wild Charge'), Js('Zap Cannon')]))
var.put('fairyAttk', Js([Js('Aromatic Mist'), Js('Baby-Doll Eyes'), Js('Charm'), Js('Crafty Shield'), Js('Dazzling Gleam'), Js('Disarming Voice'), Js('Draining Kiss'), Js('Fairy Lock'), Js('Fairy Wind'), Js('Flower Shield'), Js('Geomancy'), Js('Light of Ruin'), Js('Misty Terrain'), Js('Moonblast'), Js('Moonlight'), Js('Play Rough'), Js('Sweet Kiss')]))
var.put('fightingAttk', Js([Js('Arm Thrust'), Js('Aura Sphere'), Js('Brick Break'), Js('Bulk Up'), Js('Circle Throw'), Js('Close Combat'), Js('Counter'), Js('Cross Chop'), Js('Detect'), Js('Double Kick'), Js('Drain Punch'), Js('Dynamic Punch'), Js('Final Gambit'), Js('Flying Press'), Js('Focus Blast'), Js('Focus Punch'), Js('Force Palm'), Js('Hammer Arm'), Js('High Jump Kick'), Js('Jump Kick'), Js('Karate Chop'), Js('Low Kick'), Js('Low Sweep'), Js('Mach Punch'), Js('Mat Block'), Js('Power-Up Punch'), Js('Quick Guard'), Js('Revenge'), Js('Reversal'), Js('Rock Smash'), Js('Rolling Kick'), Js('Sacred Sword'), Js('Secret Sword'), Js('Seismic Toss'), Js('Sky Uppercut'), Js('Storm Throw'), Js('Submission'), Js('Superpower'), Js('Triple Kick'), Js('Vacuum Wave'), Js('Vital Throw'), Js('Wake-Up Slap')]))
var.put('fireAttk', Js([Js('Blast Burn'), Js('Blaze Kick'), Js('Blue Flare'), Js('Ember'), Js('Eruption'), Js('Fiery Dance'), Js('Fire Blast'), Js('Fire Fang'), Js('Fire Pledge'), Js('Fire Punch'), Js('Fire Spin'), Js('Flame Burst'), Js('Flame Charge'), Js('Flame Wheel'), Js('Flamethrower'), Js('Flare Blitz'), Js('Fusion Flare'), Js('Heat Crash'), Js('Heat Wave'), Js('Incinerate'), Js('Inferno'), Js('Lava Plume'), Js('Magma Storm'), Js('Mystical Fire'), Js('Overheat'), Js('Sacred Fire'), Js('Searing Shot'), Js('Sunny Day'), Js('V-create'), Js('Will-O-Wisp')]))
var.put('flyingAttk', Js([Js('Acrobatics'), Js('Aerial Ace'), Js('Aeroblast'), Js('Air Cutter'), Js('Air Slash'), Js('Bounce'), Js('Brave Bird'), Js('Chatter'), Js('Defog'), Js('Dragon Ascent'), Js('Drill Peck'), Js('Feather Dance'), Js('Fly'), Js('Gust'), Js('Hurricane'), Js('Mirror Move'), Js('Oblivion Wing'), Js('Peck'), Js('Pluck'), Js('Roost'), Js('Sky Attack'), Js('Sky Drop'), Js('Tailwind'), Js('Wing Attack')]))
var.put('ghostAttk', Js([Js('Astonish'), Js('Confuse Ray'), Js('Curse'), Js('Destiny Bond'), Js('Grudge'), Js('Hex'), Js('Lick'), Js('Night Shade'), Js('Nightmare'), Js('Ominous Wind'), Js('Phantom Force'), Js('Shadow Ball'), Js('Shadow Claw'), Js('Shadow Force'), Js('Shadow Punch'), Js('Shadow Sneak'), Js('Spite'), Js('Trick-or-Treat')]))
var.put('grassAttk', Js([Js('Absorb'), Js('Aromatherapy'), Js('Bullet Seed'), Js('Cotton Guard'), Js('Cotton Spore'), Js('Energy Ball'), Js("Forest's Curse"), Js('Frenzy Plant'), Js('Giga Drain'), Js('Grass Knot'), Js('Grass Pledge'), Js('Grass Whistle'), Js('Grassy Terrain'), Js('Horn Leech'), Js('Ingrain'), Js('Leaf Blade'), Js('Leaf Storm'), Js('Leaf Tornado'), Js('Leech Seed'), Js('Magical Leaf'), Js('Mega Drain'), Js('Needle Arm'), Js('Petal Blizzard'), Js('Petal Dance'), Js('Power Whip'), Js('Razor Leaf'), Js('Seed Bomb'), Js('Seed Flare'), Js('Sleep Powder'), Js('Solar Beam'), Js('Spiky Shield'), Js('Spore'), Js('Stun Spore'), Js('Synthesis'), Js('Vine Whip'), Js('Wood Hammer'), Js('Worry Seed')]))
var.put('groundAttk', Js([Js('Bone Club'), Js('Bone Rush'), Js('Bonemerang'), Js('Bulldoze'), Js('Dig'), Js('Drill Run'), Js('Earth Power'), Js('Earthquake'), Js('Fissure'), Js("Land's Wrath"), Js('Magnitude'), Js('Mud Bomb'), Js('Mud Shot'), Js('Mud Sport'), Js('Mud-Slap'), Js('Precipice Blades'), Js('Rototiller'), Js('Sand Tomb'), Js('Sand Attack'), Js('Spikes'), Js('Thousand Arrows'), Js('Thousand Waves')]))
var.put('iceAttk', Js([Js('Aurora Beam'), Js('Avalanche'), Js('Blizzard'), Js('Freeze-Dry'), Js('Freeze Shock'), Js('Frost Breath'), Js('Glaciate'), Js('Hail'), Js('Haze'), Js('Ice Ball'), Js('Ice Beam'), Js('Ice Burn'), Js('Ice Fang'), Js('Ice Punch'), Js('Ice Shard'), Js('Icicle Crash'), Js('Icicle Spear'), Js('Icy Wind'), Js('Mist'), Js('Powder Snow'), Js('Sheer Cold')]))
var.put('normalAttk', Js([Js('Acupressure'), Js('After You'), Js('Assist'), Js('Attract'), Js('Barrage'), Js('Baton Pass'), Js('Belly Drum'), Js('Bestow'), Js('Bide'), Js('Bind'), Js('Block'), Js('Body Slam'), Js('Boomburst'), Js('Camouflage'), Js('Captivate'), Js('Celebrate'), Js('Chip Away'), Js('Comet Punch'), Js('Confide'), Js('Constrict'), Js('Conversion'), Js('Conversion 2'), Js('Copycat'), Js('Covet'), Js('Crush Claw'), Js('Crush Grip'), Js('Cut'), Js('Defense Curl'), Js('Disable'), Js('Dizzy Punch'), Js('Double Hit'), Js('Double Slap'), Js('Double Team'), Js('Double-Edge'), Js('Echoed Voice'), Js('Encore'), Js('Endeavor'), Js('Endure'), Js('Entrainment'), Js('Explosion'), Js('Extreme Speed'), Js('Facade'), Js('Fake Out'), Js('False Swipe'), Js('Feint'), Js('Flail'), Js('Flash'), Js('Focus Energy'), Js('Follow Me'), Js('Foresight'), Js('Frustration'), Js('Fury Attack'), Js('Fury Swipes'), Js('Giga Impact'), Js('Glare'), Js('Growl'), Js('Growth'), Js('Guillotine'), Js('Happy Hour'), Js('Harden'), Js('Head Charge'), Js('Headbutt'), Js('Heal Bell'), Js('Helping Hand'), Js('Hidden Power'), Js('Hold Back'), Js('Hold Hands'), Js('Horn Attack'), Js('Horn Drill'), Js('Howl'), Js('Hyper Beam'), Js('Hyper Fang'), Js('Hyper Voice'), Js('Judgment'), Js('Last Resort'), Js('Leer'), Js('Lock-On'), Js('Lovely Kiss'), Js('Lucky Chant'), Js('Me First'), Js('Mean Look'), Js('Mega Kick'), Js('Mega Punch'), Js('Metronome'), Js('Milk Drink'), Js('Mimic'), Js('Mind Reader'), Js('Minimize'), Js('Morning Sun'), Js('Natural Gift'), Js('Nature Power'), Js('Noble Roar'), Js('Odor Sleuth'), Js('Pain Split'), Js('Pay Day'), Js('Perish Song'), Js('Play Nice'), Js('Pound'), Js('Present'), Js('Protect'), Js('Psych Up'), Js('Quick Attack'), Js('Rage'), Js('Rapid Spin'), Js('Razor Wind'), Js('Recover'), Js('Recycle'), Js('Reflect Type'), Js('Refresh'), Js('Relic Song'), Js('Retaliate'), Js('Return'), Js('Roar'), Js('Rock Climb'), Js('Round'), Js('Safeguard'), Js('Scary Face'), Js('Scratch'), Js('Screech'), Js('Secret Power'), Js('Self-Destruct'), Js('Sharpen'), Js('Shell Smash'), Js('Simple Beam'), Js('Sing'), Js('Sketch'), Js('Skull Bash'), Js('Slack Off'), Js('Slam'), Js('Slash'), Js('Sleep Talk'), Js('Smelling Salts'), Js('Smokescreen'), Js('Snore'), Js('Soft-Boiled'), Js('Sonic Boom'), Js('Spike Cannon'), Js('Spit Up'), Js('Splash'), Js('Stockpile'), Js('Stomp'), Js('Strength'), Js('Struggle'), Js('Substitute'), Js('Super Fang'), Js('Supersonic'), Js('Swagger'), Js('Swallow'), Js('Sweet Scent'), Js('Swift'), Js('Swords Dance'), Js('Tackle'), Js('Tail Slap'), Js('Tail Whip'), Js('Take Down'), Js('Techno Blast'), Js('Teeter Dance'), Js('Thrash'), Js('Tickle'), Js('Transform'), Js('Tri Attack'), Js('Trump Card'), Js('Uproar'), Js('Vice Grip'), Js('Weather Ball'), Js('Whirlwind'), Js('Wish'), Js('Work Up'), Js('Wrap'), Js('Wring Out'), Js('Yawn')]))
var.put('poisonAttk', Js([Js('Acid'), Js('Acid Armor'), Js('Acid Spray'), Js('Belch'), Js('Clear Smog'), Js('Coil'), Js('Cross Poison'), Js('Gastro Acid'), Js('Gunk Shot'), Js('Poison Fang'), Js('Poison Gas'), Js('Poison Jab'), Js('Poison Powder'), Js('Poison Sting'), Js('Poison Tail'), Js('Sludge'), Js('Sludge Bomb'), Js('Sludge Wave'), Js('Smog'), Js('Toxic'), Js('Toxic Spikes'), Js('Venom Drench'), Js('Venoshock')]))
var.put('psychicAttk', Js([Js('Agility'), Js('Ally Switch'), Js('Amnesia'), Js('Barrier'), Js('Calm Mind'), Js('Confusion'), Js('Cosmic Power'), Js('Dream Eater'), Js('Extrasensory'), Js('Future Sight'), Js('Gravity'), Js('Guard Split'), Js('Guard Swap'), Js('Heal Block'), Js('Heal Pulse'), Js('Healing Wish'), Js('Heart Stamp'), Js('Heart Swap'), Js('Hyperspace Hole'), Js('Hypnosis'), Js('Imprison'), Js('Kinesis'), Js('Light Screen'), Js('Lunar Dance'), Js('Luster Purge'), Js('Magic Coat'), Js('Magic Room'), Js('Meditate'), Js('Miracle Eye'), Js('Mirror Coat'), Js('Mist Ball'), Js('Power Split'), Js('Power Swap'), Js('Power Trick'), Js('Psybeam'), Js('Psychic'), Js('Psycho Boost'), Js('Psycho Cut'), Js('Psycho Shift'), Js('Psyshock'), Js('Psystrike'), Js('Psywave'), Js('Reflect'), Js('Rest'), Js('Role Play'), Js('Skill Swap'), Js('Stored Power'), Js('Synchronoise'), Js('Telekinesis'), Js('Teleport'), Js('Trick'), Js('Trick Room'), Js('Wonder Room'), Js('Zen Headbutt')]))
var.put('rockAttk', Js([Js('Ancient Power'), Js('Diamond Storm'), Js('Head Smash'), Js('Power Gem'), Js('Rock Blast'), Js('Rock Polish'), Js('Rock Slide'), Js('Rock Throw'), Js('Rock Tomb'), Js('Rock Wrecker'), Js('Rollout'), Js('Sandstorm'), Js('Smack Down'), Js('Stealth Rock'), Js('Stone Edge'), Js('Wide Guard')]))
var.put('steelAttk', Js([Js('Autotomize'), Js('Bullet Punch'), Js('Doom Desire'), Js('Flash Cannon'), Js('Gear Grind'), Js('Gyro Ball'), Js('Heavy Slam'), Js('Iron Defense'), Js('Iron Head'), Js('Iron Tail'), Js("King's Shield"), Js('Magnet Bomb'), Js('Metal Burst'), Js('Metal Claw'), Js('Metal Sound'), Js('Meteor Mash'), Js('Mirror Shot'), Js('Shift Gear'), Js('Steel Wing')]))
var.put('waterAttk', Js([Js('Aqua Jet'), Js('Aqua Ring'), Js('Aqua Tail'), Js('Brine'), Js('Bubble'), Js('Bubble Beam'), Js('Clamp'), Js('Crabhammer'), Js('Dive'), Js('Hydro Cannon'), Js('Hydro Pump'), Js('Muddy Water'), Js('Octazooka'), Js('Origin Pulse'), Js('Rain Dance'), Js('Razor Shell'), Js('Scald'), Js('Steam Eruption'), Js('Soak'), Js('Surf'), Js('Water Gun'), Js('Water Pledge'), Js('Water Pulse'), Js('Water Shuriken'), Js('Water Sport'), Js('Water Spout'), Js('Waterfall'), Js('Whirlpool'), Js('Withdraw')]))
var.put('evo', Js([Js('could still evolve, but it requires a special stone'), Js('could still evolve, but only under rare circumstances'), Js('has already evolved once, but can still evolve one more time'), Js('has evolve once and can still evolve into one of two potential evolutions'), Js('has evolved once and can evolve no more'), Js('has evolved twice and can evolve no more'), Js('has evolved twice, but can still evolve once more'), Js("hasn't evolved yet and there are no known evolutions"), Js("hasn't evolved yet, but could do so once"), Js("hasn't evolved yet, but could do so twice")]))
var.put('rsm', Js([Js('bears resemblance to'), Js('closely resembles'), Js('faintly looks like'), Js('is similar to'), Js('looks a little like'), Js('looks a lot like'), Js('shares features with'), Js('slightly resembles'), Js('somewhat resembles')]))
pass
pass


# Add lib to the module scope
pokemonDescriptions = var.to_python()
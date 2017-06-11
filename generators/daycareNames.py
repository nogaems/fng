__all__ = ['daycareNames']

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
var.put('nm1', Js([Js('A Place To Grow'), Js('Above And Beyond'), Js('Alphabet Kids'), Js('Angel Academy'), Js('Apple Blossoms'), Js('Baby Steps'), Js('Beach Babies'), Js('Big Dreams'), Js('Big Hearts'), Js('Big Playhouse'), Js('Big Smiles'), Js('Blooming Kids'), Js('Bright Beginnings'), Js('Bright Eyes'), Js('Bright Future'), Js('Bright Horizons'), Js('Bright Minds'), Js('Brighter Horizons'), Js('Buds and Blooms'), Js('Building Blocks'), Js('Bumble Bees'), Js('Bundles of Joy'), Js('Busy Bees'), Js('Butterflies'), Js('Candy Cane'), Js('Caring Hearts'), Js('Caring and Sharing'), Js('Castle Gardens'), Js('Caterpillar Corner'), Js('Cheeky Monkeys'), Js('Chickadees'), Js("Children's Den"), Js('Comfort Zone'), Js('Cornerstone'), Js('Cradles of Love'), Js('Creative Care'), Js('Creative Castle'), Js('Creative Cubs'), Js('Creative Hearts'), Js('Cutie Pies'), Js('Dandelily'), Js('Dandelion'), Js('Daydreams'), Js('Do Re Mi'), Js('Dollhouse'), Js('Dragonfly'), Js('Dreamland'), Js('Duck Duck Goose'), Js('Early Learners'), Js('EduKids'), Js('Educastle'), Js('Enchanted Forest'), Js('Everyday Sunshine'), Js('Fairy Godmother'), Js('Fairytales'), Js('Family Tree'), Js('Firefly'), Js('First Steps'), Js('Fun In The Sun'), Js('Fundecational'), Js('Funny Bunnies'), Js('Funshine'), Js('Gingerbread House'), Js('Great Adventures'), Js('Growing Everyday'), Js('Growing Pains'), Js('Growing Patch'), Js('Growing Tree'), Js('Happy Days'), Js('Happy Faces'), Js('Happy Feet'), Js('Happy Hands'), Js('Happy Hearts'), Js('Happy Memories'), Js('Happy Trails'), Js('Helping Hands'), Js('Hop Scotch'), Js('Itty Bitties'), Js('Jelly Bean'), Js('Jitter Bug'), Js('Kids Castle'), Js('Kids Clubhouse'), Js('Kids Corner'), Js('Kids Garden'), Js('Kids Palace'), Js('Kids Paradise'), Js('Kidspace'), Js('Laugh and Learn'), Js('Laugh-a-lot'), Js('Leaps and Bounds'), Js('Learning Forest'), Js('Learning Ladder'), Js('Learning Tree'), Js('Lilypad'), Js('Little Adventures'), Js('Little Angels'), Js('Little Bugs'), Js('Little Cubs'), Js('Little Devils'), Js('Little Ducklings'), Js('Little Einsteins'), Js('Little Feet Big Steps'), Js('Little Giggles'), Js('Little Gumdrops'), Js('Little Hands and Feet'), Js('Little Haven'), Js('Little Journeys'), Js('Little Lambs'), Js('Little Lives'), Js('Little Lookout'), Js('Little Miracles'), Js('Little Orchids'), Js('Little Rabbits'), Js('Little Rascals'), Js('Little Rockers'), Js('Little Sprouts'), Js('Little Stars'), Js('Little Wonders'), Js('Live and Learn'), Js('Lots of Love'), Js('Love, Learn, Play'), Js('Lovebugs'), Js('Loving Arms'), Js('Loving Hands'), Js('Lullabies'), Js('Lullabies and Laughter'), Js('Lullaby Babies'), Js('Magical Moments'), Js('Making Memories'), Js("Mama Bear's"), Js('Miles of Smiles'), Js('Milk and Cookies'), Js('Mini Miracles'), Js('Mini Munchkins'), Js('Mother Goose'), Js('Mother Hen'), Js("Mother Hen's Little Chicks"), Js('Mother Land'), Js('Munchkins'), Js('New Beginnings'), Js('Nurture Zone'), Js('Once Upon A Time'), Js('Open Arms'), Js('Over the Rainbow'), Js("Owl's Nest"), Js('Peace of Mind'), Js('Piggyback Ride'), Js('Pigtails'), Js('Playful Minds'), Js('Playhouse'), Js('Precious Gems'), Js('Precious Moments'), Js('Pumpkin Patch'), Js('Rainbow'), Js('Rainbow Grove'), Js('Rainbow Kids'), Js('Rainbow Path'), Js('Rainbows and Sunshine'), Js('Raising Stars'), Js('Rascals'), Js('Reading Rainbows'), Js('Ready, Set, Go'), Js('Rising Stars'), Js("Robin's Nest"), Js('Rock-A-By Baby'), Js('Rugrats'), Js('Small World'), Js('Step by Step'), Js('Stepping Stones'), Js('Story Time'), Js('Strong Roots'), Js('Sunrise and Shine'), Js('Sunshine'), Js('Sweet Hearts'), Js('Sweet Peas'), Js('Teachable Moments'), Js('Teddy Bear'), Js('Tender Moments'), Js('The Cocoon'), Js('Tiny Blessings'), Js('Tiny Toddlers'), Js('Tiny Toes'), Js('Tiny Town'), Js('Tiny Treasures'), Js('Tippy Toes'), Js('Toddler Town'), Js('Tot Spot'), Js('Treetops'), Js('Tutor Time'), Js('Twinkle Toes'), Js('Under My Wings'), Js('Wee Care'), Js('Wee Hours'), Js('Wee Watch'), Js('Wiggles and Giggles'), Js('Wish Upon A Star'), Js('Wiz Kids'), Js('Wonder Kids'), Js('Wonderland'), Js('Young Explorers')]))
var.put('nm2', Js([Js('Childcare'), Js('Childcare Center'), Js('Daycare'), Js('Daycare Center'), Js('Kindergarten'), Js('Nursery School'), Js('Playgroup'), Js('Pre-School')]))
pass
pass


# Add lib to the module scope
daycareNames = var.to_python()
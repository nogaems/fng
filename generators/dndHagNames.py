__all__ = ['dndHagNames']

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
    var.put('nm1', Js([Js('Acrid'), Js('Ancient'), Js('Angry'), Js('Antique'), Js('Antsy'), Js('Arrogant'), Js('Auntie'), Js('Babbling'), Js('Baggy'), Js('Batty'), Js('Bawdy'), Js('Bickering'), Js('Biting'), Js('Bitter'), Js('Bizarre'), Js('Black'), Js('Blaring'), Js('Blathering'), Js('Bony'), Js('Bumbling'), Js('Bumpy'), Js('Cackling'), Js('Cheeky'), Js('Chittering'), Js('Chuckling'), Js('Cold'), Js('Cooking'), Js('Coughing'), Js('Crabby'), Js('Crackling'), Js('Crafty'), Js('Craven'), Js('Crazy'), Js('Crinkling'), Js('Croaking'), Js('Crooked'), Js('Cruel'), Js('Crumbling'), Js('Delirious'), Js('Demonic'), Js('Depraved'), Js('Deranged'), Js('Despicable'), Js('Disfigured'), Js('Dismal'), Js('Dread'), Js('Dreaming'), Js('Drooling'), Js('Dusty'), Js('Erratic'), Js('Feeble'), Js('Feisty'), Js('Filthy'), Js('Flaky'), Js('Frail'), Js('Frantic'), Js('Gabby'), Js('Giddy'), Js('Giggling'), Js('Gloomy'), Js('Glum'), Js('Granny'), Js('Gray'), Js('Greasy'), Js('Greedy'), Js('Grouchy'), Js('Grubby'), Js('Haunting'), Js('Heckling'), Js('Humming'), Js('Hungry'), Js('Icky'), Js('Jaded'), Js('Jolly'), Js('Knobby'), Js('Knotty'), Js('Laughing'), Js('Lone'), Js('Lonely'), Js('Lurking'), Js('Mad'), Js('Moldy'), Js('Murky'), Js('Muttering'), Js('Nosy'), Js('Nutty'), Js('Old'), Js('Outlandish'), Js('Pale'), Js('Paltry'), Js('Pesky'), Js('Putrid'), Js('Ragged'), Js('Raggedy'), Js('Rambling'), Js('Rickety'), Js('Rotten'), Js('Salty'), Js('Sassy'), Js('Screeching'), Js('Shabby'), Js('Shady'), Js('Shaggy'), Js('Shaky'), Js('Shoddy'), Js('Shrieking'), Js('Silent'), Js('Silver'), Js('Singing'), Js('Skinny'), Js('Sleeping'), Js('Slumbering'), Js('Smelly'), Js('Snappy'), Js('Snickering'), Js('Snoopy'), Js('Stinking'), Js('Stumbling'), Js('Twitching'), Js('Vicious'), Js('Volatile'), Js('Weary'), Js('Whistling'), Js('Wicked'), Js('Wild'), Js('Wretched'), Js('Wrinkling')]))
    var.put('nm2', Js([Js('Ada'), Js('Addie'), Js('Adeline'), Js('Agnes'), Js('Alberta'), Js('Alice'), Js('Alicia'), Js('Allie'), Js('Alma'), Js('Alta'), Js('Amanda'), Js('Amelia'), Js('Amy'), Js('Andrea'), Js('Angela'), Js('Anita'), Js('Ann'), Js('Anna'), Js('Anne'), Js('Annette'), Js('Annie'), Js('Antoinette'), Js('April'), Js('Arlene'), Js('Audrey'), Js('Barbara'), Js('Beatrice'), Js('Becky'), Js('Belinda'), Js('Bernice'), Js('Bertha'), Js('Bessie'), Js('Beth'), Js('Bette'), Js('Bettie'), Js('Betty'), Js('Beulah'), Js('Beverly'), Js('Billie'), Js('Blanche'), Js('Bobbie'), Js('Bonnie'), Js('Brenda'), Js('Carla'), Js('Carmen'), Js('Carol'), Js('Carole'), Js('Caroline'), Js('Carolyn'), Js('Carrie'), Js('Catherine'), Js('Cathy'), Js('Cecelia'), Js('Celia'), Js('Charlene'), Js('Charlotte'), Js('Cheryl'), Js('Christina'), Js('Christine'), Js('Cindy'), Js('Claire'), Js('Clara'), Js('Claudia'), Js('Cleo'), Js('Colleen'), Js('Connie'), Js('Constance'), Js('Cora'), Js('Crystal'), Js('Cynthia'), Js('Daisy'), Js('Dana'), Js('Darlene'), Js('Dawn'), Js('Deanna'), Js('Debbie'), Js('Deborah'), Js('Debra'), Js('Della'), Js('Delores'), Js('Denise'), Js('Diana'), Js('Diane'), Js('Dianne'), Js('Dolores'), Js('Donna'), Js('Dora'), Js('Doreen'), Js('Doris'), Js('Dorothea'), Js('Dorothy'), Js('Edith'), Js('Edna'), Js('Effie'), Js('Eileen'), Js('Elaine'), Js('Eleanor'), Js('Eliza'), Js('Elizabeth'), Js('Ella'), Js('Ellen'), Js('Eloise'), Js('Elsie'), Js('Elva'), Js('Emily'), Js('Emma'), Js('Erma'), Js('Essie'), Js('Estella'), Js('Estelle'), Js('Esther'), Js('Ethel'), Js('Etta'), Js('Eula'), Js('Eunice'), Js('Eva'), Js('Evelyn'), Js('Fannie'), Js('Faye'), Js('Felicia'), Js('Fern'), Js('Flora'), Js('Florence'), Js('Flossie'), Js('Frances'), Js('Freda'), Js('Frieda'), Js('Gail'), Js('Gayle'), Js('Geneva'), Js('Genevieve'), Js('Georgia'), Js('Geraldine'), Js('Gertrude'), Js('Gina'), Js('Gladys'), Js('Glenda'), Js('Gloria'), Js('Goldie'), Js('Grace'), Js('Gwendolyn'), Js('Hannah'), Js('Harriet'), Js('Hattie'), Js('Hazel'), Js('Heather'), Js('Heidi'), Js('Helen'), Js('Henrietta'), Js('Hilda'), Js('Holly'), Js('Ida'), Js('Imogene'), Js('Ina'), Js('Inez'), Js('Irene'), Js('Irma'), Js('Isabel'), Js('Isabelle'), Js('Iva'), Js('Jackie'), Js('Jacqueline'), Js('Jamie'), Js('Jan'), Js('Jane'), Js('Janet'), Js('Janice'), Js('Janie'), Js('Janis'), Js('Jean'), Js('Jeanette'), Js('Jeanne'), Js('Jeannette'), Js('Jennie'), Js('Jennifer'), Js('Jessie'), Js('Jill'), Js('Jo'), Js('Joan'), Js('Joann'), Js('Joanne'), Js('Jodi'), Js('Jody'), Js('Johnnie'), Js('Josephine'), Js('Joy'), Js('Joyce'), Js('Juanita'), Js('Judith'), Js('Judy'), Js('Julia'), Js('Julie'), Js('June'), Js('Karen'), Js('Karla'), Js('Katherine'), Js('Kathleen'), Js('Kathryn'), Js('Kathy'), Js('Katie'), Js('Kay'), Js('Kelly'), Js('Kim'), Js('Kimberly'), Js('Kristen'), Js('Kristin'), Js('Kristine'), Js('Laura'), Js('Laurie'), Js('Laverne'), Js('Lela'), Js('Lena'), Js('Leola'), Js('Leona'), Js('Leslie'), Js('Lila'), Js('Lillian'), Js('Lillie'), Js('Linda'), Js('Lisa'), Js('Lizzie'), Js('Lois'), Js('Lola'), Js('Lorene'), Js('Loretta'), Js('Lori'), Js('Lorraine'), Js('Lottie'), Js('Louise'), Js('Lucile'), Js('Lucille'), Js('Lucy'), Js('Luella'), Js('Lula'), Js('Lydia'), Js('Lynda'), Js('Lynn'), Js('Lynne'), Js('Mabel'), Js('Mable'), Js('Madeline'), Js('Mae'), Js('Maggie'), Js('Mamie'), Js('Marcella'), Js('Marcia'), Js('Margaret'), Js('Margie'), Js('Marguerite'), Js('Maria'), Js('Marian'), Js('Marianne'), Js('Marie'), Js('Marilyn'), Js('Marion'), Js('Marjorie'), Js('Marlene'), Js('Marsha'), Js('Martha'), Js('Mary'), Js('Maryann'), Js('Matilda'), Js('Mattie'), Js('Maude'), Js('Maureen'), Js('Maxine'), Js('May'), Js('Melanie'), Js('Melinda'), Js('Melissa'), Js('Melody'), Js('Michele'), Js('Michelle'), Js('Mildred'), Js('Minnie'), Js('Miriam'), Js('Mollie'), Js('Monica'), Js('Muriel'), Js('Myrna'), Js('Myrtle'), Js('Nancy'), Js('Nannie'), Js('Naomi'), Js('Natalie'), Js('Nell'), Js('Nellie'), Js('Nettie'), Js('Nicole'), Js('Nina'), Js('Nora'), Js('Norma'), Js('Ola'), Js('Olga'), Js('Olive'), Js('Ollie'), Js('Opal'), Js('Ora'), Js('Pam'), Js('Pamela'), Js('Pat'), Js('Patricia'), Js('Patsy'), Js('Patti'), Js('Patty'), Js('Paula'), Js('Paulette'), Js('Pauline'), Js('Pearl'), Js('Peggy'), Js('Penny'), Js('Phyllis'), Js('Priscilla'), Js('Rachel'), Js('Ramona'), Js('Rebecca'), Js('Regina'), Js('Renee'), Js('Rhonda'), Js('Rita'), Js('Roberta'), Js('Robin'), Js('Rosa'), Js('Rosalie'), Js('Rose'), Js('Rosemarie'), Js('Rosemary'), Js('Rosie'), Js('Roxanne'), Js('Ruby'), Js('Ruth'), Js('Sadie'), Js('Sallie'), Js('Sally'), Js('Sandra'), Js('Sandy'), Js('Sara'), Js('Sarah'), Js('Shannon'), Js('Shari'), Js('Sharon'), Js('Sheila'), Js('Shelia'), Js('Shelley'), Js('Shelly'), Js('Sheri'), Js('Sherri'), Js('Sherry'), Js('Sheryl'), Js('Shirley'), Js('Sonya'), Js('Sophia'), Js('Sophie'), Js('Stacey'), Js('Stacy'), Js('Stella'), Js('Stephanie'), Js('Sue'), Js('Susan'), Js('Susie'), Js('Suzanne'), Js('Sylvia'), Js('Tamara'), Js('Tami'), Js('Tammie'), Js('Tammy'), Js('Tanya'), Js('Teresa'), Js('Terri'), Js('Terry'), Js('Thelma'), Js('Theresa'), Js('Tina'), Js('Toni'), Js('Tonya'), Js('Tracey'), Js('Traci'), Js('Tracy'), Js('Valerie'), Js('Vanessa'), Js('Velma'), Js('Vera'), Js('Verna'), Js('Veronica'), Js('Vicki'), Js('Vickie'), Js('Vicky'), Js('Victoria'), Js('Viola'), Js('Violet'), Js('Virgie'), Js('Virginia'), Js('Vivian'), Js('Wanda'), Js('Wendy'), Js('Willie'), Js('Wilma'), Js('Winifred'), Js('Yolanda'), Js('Yvette'), Js('Yvonne')]))
    var.put('nm3', Js([Js('Beast'), Js('Beetle'), Js('Bitter'), Js('Blind'), Js('Blood'), Js('Bog'), Js('Bone'), Js('Boulder'), Js('Branch'), Js('Chain'), Js('Chalk'), Js('Chicken'), Js('Clot'), Js('Cold'), Js('Creep'), Js('Critter'), Js('Crypt'), Js('Dark'), Js('Dead'), Js('Devil'), Js('Dirt'), Js('Doll'), Js('Dreck'), Js('Dust'), Js('Fang'), Js('Filth'), Js('Fire'), Js('Flame'), Js('Flesh'), Js('Fowl'), Js('Frog'), Js('Gnat'), Js('Grave'), Js('Grease'), Js('Green'), Js('Grim'), Js('Grime'), Js('Gristle'), Js('Gunk'), Js('Horn'), Js('Ink'), Js('Knuckle'), Js('Lard'), Js('Light'), Js('Marble'), Js('Marsh'), Js('Meat'), Js('Mire'), Js('Moon'), Js('Mouse'), Js('Muck'), Js('Mud'), Js('Nerve'), Js('Night'), Js('Ooze'), Js('Pest'), Js('Pig'), Js('Powder'), Js('Quill'), Js('Rat'), Js('Raw'), Js('Red'), Js('Rock'), Js('Rodent'), Js('Root'), Js('Rubble'), Js('Salt'), Js('Scale'), Js('Scrap'), Js('Silt'), Js('Slime'), Js('Slop'), Js('Smoke'), Js('Snail'), Js('Snake'), Js('Soil'), Js('Soot'), Js('Spider'), Js('Spite'), Js('Spot'), Js('Sprig'), Js('Stew'), Js('Stitch'), Js('Stone'), Js('Swamp'), Js('Tallow'), Js('Tear'), Js('Thatch'), Js('Titch'), Js('Toad'), Js('Toe'), Js('Twig'), Js('Twist'), Js('Vein'), Js('Vermin'), Js('Waste'), Js('Wax'), Js('Web'), Js('Wood'), Js('Wrinkle')]))
    var.put('nm4', Js([Js('chewer'), Js('wart'), Js('teeth'), Js('gums'), Js('bones'), Js('wallow'), Js('tooth'), Js('willow'), Js('stealer'), Js('mouth'), Js('wiggle'), Js('back'), Js('bend'), Js('bite'), Js('biter'), Js('bone'), Js('breath'), Js('cheek'), Js('cheeks'), Js('chin'), Js('cough'), Js('cougher'), Js('counter'), Js('cracker'), Js('finger'), Js('fingers'), Js('foot'), Js('feet'), Js('growth'), Js('hand'), Js('hands'), Js('heart'), Js('hide'), Js('hook'), Js('joint'), Js('joints'), Js('knee'), Js('knees'), Js('leg'), Js('legs'), Js('mask'), Js('mind'), Js('mouth'), Js('body'), Js('sister'), Js('face'), Js('babbler'), Js('baker'), Js('belcher'), Js('boggle'), Js('bristle'), Js('cackle'), Js('carver'), Js('cleaver'), Js('cobble'), Js('coddler'), Js('crackle'), Js('cradle'), Js('cradler'), Js('crinkle'), Js('croaker'), Js('dabble'), Js('dangler'), Js('dipper'), Js('dribble'), Js('dribbler'), Js('fiddle'), Js('fidget'), Js('giggle'), Js('giggler'), Js('goggle'), Js('jangle'), Js('jiggle'), Js('jumbler'), Js('lurker'), Js('meddler'), Js('mingle'), Js('mingler'), Js('mumbler'), Js('mutterer'), Js('nibbler'), Js('nuzzle'), Js('paddle'), Js('paddler'), Js('prattler'), Js('rambler'), Js('ramble'), Js('rattle'), Js('rattler'), Js('rumbler'), Js('scrambler'), Js('scratcher'), Js('shifter'), Js('shuffler'), Js('sifter'), Js('singer'), Js('skewer'), Js('soother'), Js('spitter'), Js('startler'), Js('startle'), Js('squirmer'), Js('stumbler'), Js('stumble'), Js('surge'), Js('switcher'), Js('tangler'), Js('tickler'), Js('tinkerer'), Js('toppler'), Js('trampler'), Js('tremble'), Js('trembler'), Js('trick'), Js('trickle'), Js('tumbler'), Js('twitch'), Js('twitcher'), Js('waddle'), Js('waggle'), Js('whistle'), Js('whistler'), Js('whittle'), Js('wiggle'), Js('wrangle'), Js('wrangler')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
            var.put('names', (((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd3'), Js(1.0))
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
dndHagNames = var.to_python()
story_1 = "It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) !"
story_2 = "This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!"
story_3 = "Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!"
n = input("Please, pick one of the templates: 1, 2 or 3")
if n == '1':
  number = input('Please, type number')
  measure_of_time = input('Please, type measure of time')
  mode_of_transportation = input('Please, type mode of transporation')
  adjective = input('Please, type adjective')
  adjective2 = input('Please, type one more adjective')
  noun = input('Please, type a noun')
  color = input('Please, type color')
  part_of_the_body = input('Please, type part of the body')
  verb = input('Please, type a verb')
  number2 = input('Please, type another number')
  noun2 = input('Please, type another noun')
  noun3 = input('Please, type a another noun')
  part_of_the_body2 = input('Please, type another part of the body')
  noun4 = input('Please, type another noun')
  adjective3 = input('Please, type another adjective')
  silly_word = input('Please, type any silly word')
  story_1 = story_1.replace('(Number)', number).replace('(Measure of time)', measure_of_time).replace('(Mode of Transportation)', mode_of_transportation).replace('(Adjective)', adjective).replace('(Adjective2)', adjective2).replace('(Noun)', noun).replace('(Color)', color).replace('(Part of the Body )', part_of_the_body).replace('(Verb)', verb).replace('(Number2)', number2).replace('(Noun2)', noun2).replace('(Noun3)', noun3).replace('( Part of the Body 2)', part_of_the_body2).replace('noun4', noun4).replace('( Adjective3)', adjective3).replace('(Silly Word)', silly_word)
  print(story_1)
elif n == '2':
  proper_noun = input("Please, type proper noun: person's name")
  noun = input('Please, type a noun')
  adjective = input('Please, type adjective: feeling)')
  verb = input('Please, type a verb')
  adjective2 = input('Please, type another adjective: feeling)')
  animal = input('Please, type an animal')
  verb2 = input('Please, type another verb')
  color = input('Please, type color')
  verb3 = input('Please, type a verb: ending in ing')
  adverb = input('Please, type a adverb: ending in ly')
  number = input('Please, type a number')
  measure_of_time = input('Please, type measure of time')
  silly_word = input('Please, type any silly word')
  noun2 = input('Please, type another noun')
  story_2 = story_2.replace('( Proper Noun (Person’s Name))', proper_noun).replace('(Noun)', noun).replace('(Adjective (Feeling))', adjective).replace('(Verb)', verb).replace('(Adjective (Feeling) 2)', adjective2).replace('(Animal)', animal).replace('(Verb2)', verb2).replace('(Color)', color).replace('( Verb (ending in ing) )', verb3).replace('(Adverb (ending in ly))', adverb).replace('(Number)', number).replace('(Measure of Time)', measure_of_time).replace('(Silly Word)', silly_word).replace('(Noun2)', noun2)
  print(story_2)
else:
  proper_noun = input("Please, type proper noun: person's name")
  adjective = input('Please, type adjective')
  color = input('Please, type color')
  animal = input('Please, type an animal')
  place = input('Please, type a place')
  adjective2 = input('Please, type another adjective')
  magical_creature = input('Please, type a magical creature (plural)')
  adjective3 = input('Please, type another adjective')
  magical_creature2 = input('Please, type another magical creature (plural)')
  room_in_a_house = input('Please, type a room in a house')
  noun = input('Please, type a noun')
  noun2 = input('Please, type another noun')
  noun3 = input('Please, type a noun; plural')
  adjective4 = input('Please, type one more adjective')
  noun4 = input('Please, type another noun; plural')
  number = input('Please, type a number')
  verb = input('Please, type a verb')
  measure_of_time = input('Please, type measure of time')
  verb2 = input('Please, type a verb: ending in ing')
  adjective5 = input('Please, type one more adjective')
  noun5 = input('Please, type another noun')
  story_3 = story_3.replace('(Proper Noun (Person’s Name) )', proper_noun).replace('(Adjective)', adjective).replace('(Color)', color).replace('(Animal)', animal).replace('(Place)', place).replace('(Adjective2)', adjective2).replace('(Magical Creature (Plural))', magical_creature).replace('(Adjective3)', adjective3).replace('(Magical Creature (Plural)2)', magical_creature2).replace('( Room in a House)', room_in_a_house).replace('(Noun)', noun).replace('(Noun2)', noun2).replace('(Noun(Plural)3)', noun3).replace('(Adjective4)', adjective4).replace('( Noun (Plural)4)', noun4).replace('(Number)', number).replace('( Measure of time)', measure_of_time).replace('(Verb (ending in ing))', verb2).replace('(Adjective5)', adjective5).replace('(Noun5)', noun5)
  print(story_3)


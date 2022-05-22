import random

input("ready to start?")
#Put your questions or phrases in the array(line right below)
questions = ['Time Military time: Trieze Heures','Quinze Heures: ','Vingt Heures: ','zero heure: ',"form of Avoir: j'_ ",'form of Avoir: Nous','Form of Avoir: Tu','Forms of Avoir: Vous','Forms of Avoir: Il/Elle/On','Forms of Avoir: Ils/Elles','Past participles+meaning: Regarder','Past participles+meaning: Choisir','Past participles+meaning:perdre','Past participles+meaning:Prendre','Past participles+meaning:Mettre','Past participles+meaning: avoir','Past participles+meaning:lire','Past participles+meaning:Voir','Past participles+meaning:Etre','Past participles+meaning:faire','What is the longest river?: ','What is the name of the valley with castles','Nick name of the valley french and english: ','Castles built for protection: ','Castles built for entertaining: ','French Royal Symbol: ','Symbole of Francois 1: ','Largest Renaissance castle: ',' Castle of Henri 2, Catherine de medici and Diane de poiters',"Customer: La carte s'il vous plait(tranlate): ",'server: Voila(translate)','customer(translate): je vous drais','Server: Vous avez choisi(translate): ','Customer:Donnez-moi(translate)','Server:Et avez ca?(translate): ',"Customer: c'est degoutant(translate)",'server: Comment trouvez-vous(translate)','Customer:Ca fait combien(translate)','Server:oui tout desuite(translate):',"L'assiette",'Le sel','Je mange','Le bol','Le poivre','Je bois','Le verre','la fourchette',"j'ai",'Le serviette','la cuillere','essuyer','La tasse','le couteau','mettre la table','Name three Repas(Meals): ','Sandwiches','Pains(Bread) ','Viandes(meat): ','Fruit']
print("Good luck on your finals!")
for i in questions:
    quizQuestion = random.choice(questions)
    print(quizQuestion)
    isTheAnsCorrect = input("What is the answer: ")
    questions.remove(quizQuestion)
    len(questions)

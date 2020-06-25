import random

def motivation():
	mot = ["O sucesso nasce do querer, da determinação e persistência em se chegar a um objetivo. Mesmo não atingindo o alvo, quem busca e vence obstáculos, no mínimo fará coisas admiráveis.",
	"A persistência é o caminho do êxito.",
	"Determinação, coragem e autoconfiança são fatores decisivos para o sucesso. Se estamos possuídos por uma inabalável determinação, conseguiremos superá-los. Independentemente das circunstâncias, devemos ser sempre humildes, recatados e despidos de orgulho.",
	"Agir, eis a inteligência verdadeira. Serei o que quiser. Mas tenho que querer o que for. O êxito está em ter êxito, e não em ter condições de êxito. Condições de palácio tem qualquer terra larga, mas onde estará o palácio se não o fizerem ali?",
	"Lute. Acredite. Conquiste. Perca. Deseje. Espere. Alcance. Invada. Caia. Seja tudo o quiser ser, mas acima de tudo, seja você sempre.",
	"Só existe um êxito: a capacidade de levar a vida que se quer.",
	"A vitalidade é demonstrada não apenas pela persistência, mas pela capacidade de começar de novo.",
	"A coragem não é ausência do medo; é a persistência apesar do medo.",
	"Só se pode alcançar um grande êxito quando nos mantemos fiéis a nós mesmos.",
	"O homem não teria alcançado o possível se, repetidas vezes, não tivesse tentado o impossível.",
	"Todo mundo é capaz de sentir os sofrimentos de um amigo. Ver com agrado os seus êxitos exige uma natureza muito delicada."
	"Lute com determinação, abrace a vida com paixão, perca com classe e vença com ousadia, porque o mundo pertence a quem se atreve e a vida é muito para ser insignificante.",
	"Força de ânimo e coragem na adversidade servem para conquistar o êxito, mais do que um exército.",
	"Creia em si, mas não duvide sempre dos outros.",
	"Dois homens não podem passar meia hora juntos sem que um conquiste uma evidente superioridade em relação ao outro.",
	"Não deixe que as pessoas te façam desistir daquilo que você mais quer na vida. Acredite. Lute. Conquiste. E acima de tudo, seja feliz!",
	"As únicas grandes companhias que conseguirão ter êxito são aquelas que consideram os seus produtos obsoletos antes que os outros o façam.",
	"Talento é dom, é graça. E sucesso nada tem a ver com sorte, mas com determinação e trabalho.",
	"Para ter um negócio de sucesso, alguém, algum dia, teve que tomar uma atitude de coragem.",
	"Nenhum mentiroso tem uma memória suficientemente boa para ser um mentiroso de êxito.",
	"Estar decidido, acima de qualquer coisa, é o segredo do êxito.",
	"Para obter êxito no mundo temos de parecer loucos mas sermos espertos.",
	"A disciplina é a mãe do êxito.",
	"O segredo do êxito na vida de um homem está em preparar-se para aproveitar a ocasião, quando ela se apresenta.",
	"O êxito começa no exato momento em que o homem decide o que quer e começa a trabalhar para consegui-lo.",	
	"A disciplina é a alma de um exército; torna grandes os pequenos contingentes, proporciona êxito aos fracos, e estima todos.",	
	"A raiz do mal reside no fato de se insistir demasiadamente que no êxito da competição está a principal fonte de felicidade.",	
	"O êxito parece doce a quem não o alcança.",	
	"A persistência realiza o impossível.",	
	"Persistência é a irmã gêmea da excelência. Uma é a mãe da qualidade, a outra é a mãe do tempo.",	
	"Eu escolho um homem que não duvide de minha coragem, que não me acredite inocente, que tenha a coragem de me tratar como uma mulher.",	
	"Ai daqueles que pararem com sua capacidade de sonhar, de invejar sua coragem de anunciar e denunciar. Ai daqueles que, em lugar de visitar de vez em quando o amanha pelo profundo engajamento com o hoje, com o aqui e o agora, se atrelarem a um passado de exploração e de rotina.",	
	"Suba o primeiro degrau com fé. Não é necessário que você veja toda a escada. Apenas dê o primeiro passo.",	
	"Você tem que acordar cada manhã com determinação se você pretende ir para a cama com satisfação.",	
	"As pessoas não carecem de força, carecem de determinação.",	
	"A verdadeira esperança é uma qualidade, uma determinação heroica da alma. E a mais elevada forma de esperança é o desespero superado.",	
	"Conserve os olhos fixos num ideal sublime, e lute sempre pelo que deseja, pois só os fracos desistem e só quem luta é digno de vida.",	
	"A esperança não será a prova de um sentido oculto da Existência., uma coisa que merece que se lute por ela?",	
	"O êxito da vida não se mede pelo caminho que você conquistou, mas sim pelas dificuldades que superou no caminho.",	
	"A impaciência é um grande obstáculo para o bom êxito.",
	"Não procure ser um homem com êxito, e sim um homem com valores.",	
	"O êxito é fácil de obter. O difícil é merecê-lo.",	
	"O êxito na vida não significa apenas ser bem sucedido, mas também sobrepor-se aos fracassos.",	
	"Tudo deveria se tornar o mais simples possível, mas não simplificado.",	
	"Comece fazendo o que é necessário, depois o que é possível, e de repente você estará fazendo o impossível.",
	"O erro acontece de vários modos, enquanto ser correto é possível apenas de um modo.",	
	"Não é possível ser bom pela metade.",	
	"O milagre não prova o impossível; serve, apenas, como confirmação do que é possível.",	
	"As pessoas que resolviam as coisas em geral tinham muita persistência e um pouco de sorte. Se a gente persistisse o bastante, a sorte em geral chegava. Mas a maioria das pessoas não podia esperar a sorte, por isso desistia.",	
	"Tudo o que um sonho precisa para ser realizado é alguém que acredite que ele possa ser realizado.",	
	"A nossa maior glória não reside no fato de nunca cairmos, mas sim em levantarmo-nos sempre depois de cada queda.",	
	"Transportai um punhado de terra todos os dias e fareis uma montanha.",	
	"Seja como os pássaros que, ao pousarem um instante sobre ramos muito leves, sentem-nos ceder, mas cantam! Eles sabem que possuem asas.",	
	"A força não provém da capacidade física. Provém de uma vontade indomável.",	
	"O número dos que nos invejam confirma as nossas capacidades.",	
	"Nas pessoas de capacidade limitada, a modéstia não passa de mera honestidade, mas em quem possui grande talento, é hipocrisia.",	
	"É capaz quem pensa que é capaz.",	
	"Quem sabe concentrar-se numa coisa e insistir nela como único objetivo, obtém a capacidade de fazer qualquer coisa.",	
	"O ser capaz mora perto da necessidade.",
	"A capacidade pouco vale sem oportunidade.",	
	"Acredite em si próprio e chegará um dia em que os outros não terão outra escolha senão acreditar com você.",	
	"Se a sua vida for a melhor coisa que já te aconteceu, acredite, você tem mais sorte do que pode imaginar.",	
	"Quer você acredite que consiga fazer uma coisa ou não, você está certo.",	
	"Acredite em si. Engate a mente na sua boa estrela e reconheça que a sua luz interior o conduzirá sempre para cima e para a frente.",	
	"Ninguém é assim tão velho que não acredite que poderá viver por mais um ano.",	
	"Gostaria que você soubesse que existe dentro de si uma força capaz de mudar sua vida. Basta que lute e aguarde um novo amanhecer.",	
	"Jamais desista das pessoas que ama. Jamais desista de ser feliz. Lute sempre pelos seus sonhos. Seja profundamente apaixonado pela vida. Pois a vida é um espetáculo imperdível.",	
	"Ame mesmo que isso cause sofrimento, mesmo que todo mundo fale para desistir. Lute pelo que você quer.",	
	"Maravilhas nunca faltaram ao mundo; o que sempre falta é a capacidade de senti-las e admirá-las.",
	"Deus, ao criar o homem, superestimou a Sua capacidade.",
	"Inteligência é a capacidade de se adaptar à mudança.",
	"Capacidade de saber cada vez mais sobre cada vez menos, até saber tudo sobre nada.",
	"O amor é a arte de criar algo com a ajuda da capacidade do outro.",
	"A liderança é a capacidade de conseguir que as pessoas façam o que não querem fazer e gostem de o fazer.",
	"Tato é a capacidade de se descrever os outros tal como eles se julgam.",
	"A sabedoria dos homens é proporcional não à sua experiência, mas à sua capacidade de adquirir experiência.",
	"Pensamento duplo indica a capacidade de ter na mente, ao mesmo tempo, duas opiniões contraditórias e aceitar ambas.",
	]
	return mot

def emoji():
	em = ['😄', '😃', '😀', '😊', '☺', '😉', '😍', '😘', '😚','😗', '😙', '😜', '😝','😛','✌','👊','👍','💪','🌷','🙌','🌟']
	return em
 
t = motivation()
print(f'"{random.choice(motivation())}" Bot motivacional {random.choice(emoji())}')
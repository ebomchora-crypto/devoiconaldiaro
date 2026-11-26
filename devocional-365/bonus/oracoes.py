from base import *
P=[cover("PRESENTE ESPECIAL · BÔNUS 3","Orações para Cada Momento","Orações curtas para o dia a dia: da manhã à noite, na família, no trabalho, na doença, no medo e na gratidão")]
def o(t,txt,nota=""):
    return f"<h3>{t}</h3>"+"".join(f"<p>{x}</p>" for x in txt.split("\n"))+(f"<p class='small'>{nota}</p>" if nota else "")
secs=[
("Começar o dia",[
 o("Oferecimento do dia","Senhor, eu vos agradeço por mais este dia. Ofereço-vos tudo o que eu pensar, falar e fizer hoje: meu trabalho, minhas alegrias e minhas dificuldades. Guardai-me do pecado e fazei de mim um instrumento do vosso amor para quem eu encontrar. Maria, minha Mãe, segurai minha mão durante este dia. Amém."),
 o("Ao Espírito Santo","Vinde, Espírito Santo, enchei os corações dos vossos fiéis e acendei neles o fogo do vosso amor. Enviai o vosso Espírito e tudo será criado, e renovareis a face da terra.\nÓ Deus, que instruístes os corações dos vossos fiéis com a luz do Espírito Santo, concedei-nos que, pelo mesmo Espírito, saibamos o que é reto e gozemos sempre da sua consolação. Por Cristo, nosso Senhor. Amém."),
 o("Ao Anjo da Guarda","Santo Anjo do Senhor, meu zeloso guardador, se a ti me confiou a piedade divina, sempre me rege, me guarda, me governa e me ilumina. Amém."),
]),
("Ângelus (ao meio-dia)",[
 "<p class='small'>Tradicionalmente rezado às 6h, ao meio-dia e às 18h, lembrando a Encarnação de Jesus.</p><div class='vr'><p><b>V.</b> O Anjo do Senhor anunciou a Maria.</p><p><b>R.</b> E ela concebeu do Espírito Santo.</p><p><i>Ave, Maria…</i></p><p><b>V.</b> Eis aqui a serva do Senhor.</p><p><b>R.</b> Faça-se em mim segundo a vossa palavra.</p><p><i>Ave, Maria…</i></p><p><b>V.</b> E o Verbo se fez carne.</p><p><b>R.</b> E habitou entre nós.</p><p><i>Ave, Maria…</i></p><p><b>V.</b> Rogai por nós, santa Mãe de Deus.</p><p><b>R.</b> Para que sejamos dignos das promessas de Cristo.</p></div><p><b>Oremos.</b> Infundi, Senhor, a vossa graça em nossas almas, para que nós, que pela anunciação do Anjo conhecemos a encarnação de Cristo, vosso Filho, por sua paixão e cruz sejamos conduzidos à glória da ressurreição. Pelo mesmo Cristo, Senhor nosso. Amém.</p>",
 o("Antes das refeições","Abençoai, Senhor, esta mesa, os alimentos que vamos receber e as mãos que os prepararam. Dai pão a quem tem fome e fome de vós a quem tem pão. Amém."),
 o("Depois das refeições","Obrigado, Senhor, pelo alimento que recebemos. Que nunca falte o pão em nossa mesa nem em nenhuma mesa. Amém."),
]),
("Terminar o dia",[
 o("Breve exame da noite","1. Agradeça: pelo que posso agradecer hoje?\n2. Reveja: em que momentos senti Deus perto? Em que me afastei dele?\n3. Peça perdão pelo que fez de errado.\n4. Entregue o dia de amanhã nas mãos de Deus."),
 o("Antes de dormir","Senhor, terminou mais um dia. Obrigado por tudo o que vivi. Perdoai as minhas faltas e cuidai de mim e dos que amo durante esta noite. Afastai os maus pensamentos e os pesadelos, e dai-me um sono tranquilo. Em vossas mãos entrego o meu espírito. Maria, Mãe querida, cobri-me com o vosso manto. Amém."),
 o("Comunhão espiritual","<i>Para quando não for possível comungar.</i>\nMeu Jesus, eu creio que estais presente no Santíssimo Sacramento. Eu vos amo acima de todas as coisas e desejo receber-vos em minha alma. Já que agora não posso receber-vos sacramentalmente, vinde ao menos espiritualmente ao meu coração. Eu vos abraço e me uno inteiramente a vós. Não permitais que eu jamais me separe de vós. Amém."),
]),
("Pela família",[
 o("Pela minha família","Senhor Jesus, que vivestes em família com Maria e José, abençoai a minha casa. Dai-nos paciência uns com os outros, capacidade de perdoar e alegria de estar juntos. Afastai de nós as brigas, os vícios e tudo o que nos divide. Que o nosso lar seja um lugar de paz onde vós sejais o centro. Sagrada Família de Nazaré, protegei-nos. Amém."),
 o("Pelos filhos","Pai do céu, eu vos entrego os meus filhos. Vós os amais mais do que eu. Protegei-os dos perigos do corpo e da alma, das más companhias e dos vícios. Dai-lhes saúde, sabedoria e fé. Onde eu não puder estar, estejam os vossos anjos. Maria, Mãe de Jesus, cuidai deles como cuidastes do vosso Filho. Amém."),
 o("Pelo casamento","Senhor, obrigado pela pessoa que colocastes ao meu lado. Renovai o nosso amor a cada dia. Ensinai-nos a escutar, a pedir perdão e a perdoar. Nos momentos difíceis, sede a nossa força. Que o nosso amor seja reflexo do vosso. Amém."),
]),
("Trabalho e sustento",[
 o("Antes do trabalho","Senhor, abençoai o meu trabalho de hoje. Dai-me disposição, honestidade e sabedoria. Que eu trate bem as pessoas com quem convivo e faça tudo como se fosse para vós. São José, operário, rogai por mim. Amém."),
 o("Por quem procura emprego","Pai de bondade, vós conheceis a minha necessidade. Abri as portas certas e dai-me um trabalho digno, com o qual eu possa sustentar a minha família. Afastai de mim o desânimo e dai-me perseverança para continuar procurando. Confio na vossa providência. Amém."),
 o("A São José","Glorioso São José, guardião de Jesus e esposo de Maria, que sustentastes a Sagrada Família com o trabalho das vossas mãos, olhai pela minha casa e pelas minhas necessidades. Protegei os trabalhadores, os desempregados e os pais de família. Alcançai-me uma vida justa e uma boa morte, nos braços de Jesus e Maria. Amém."),
]),
("Saúde e sofrimento",[
 o("Pela saúde de um doente","Senhor Jesus, que passastes pelo mundo curando os enfermos, olhai com amor por (nome). Aliviai a sua dor, dai sabedoria aos médicos e força aos que cuidam dele(a). Se for da vossa vontade, devolvei-lhe a saúde. E, em tudo, dai-lhe a vossa paz. Nossa Senhora, Saúde dos enfermos, rogai por ele(a). Amém."),
 o("Na ansiedade e no medo","Jesus, meu coração está inquieto. Vós dissestes: \"Não se perturbe o vosso coração\". Eu entrego em vossas mãos aquilo que me preocupa e que não posso controlar. Acalmai os meus pensamentos, aliviai o aperto no meu peito e dai-me a vossa paz. Jesus, eu confio em vós. Amém.","Se a ansiedade for frequente ou intensa, procure também ajuda de um profissional de saúde. Cuidar da mente também é cuidar do dom que Deus nos deu."),
 o("No momento de uma decisão","Espírito Santo, preciso decidir e não sei qual caminho seguir. Iluminai a minha mente, tirai de mim a pressa e o medo, e mostrai-me o que é melhor segundo a vontade de Deus. Que eu tenha paz na escolha que fizer. Maria, Mãe do bom conselho, rogai por mim. Amém."),
]),
("Luto e esperança",[
 o("Pelos falecidos","Dai-lhes, Senhor, o descanso eterno, e brilhe para eles a vossa luz. Descansem em paz. Amém."),
 o("Por alguém que partiu","Senhor da vida, recebei (nome) na vossa casa. Perdoai as suas faltas e dai-lhe a alegria de contemplar o vosso rosto. Consolai o nosso coração na saudade e dai-nos a esperança de nos reencontrarmos um dia na vossa glória. Maria, Mãe das Dores, ficai conosco. Amém."),
]),
("Proteção e caminho",[
 o("A São Miguel Arcanjo","São Miguel Arcanjo, defendei-nos no combate, sede o nosso refúgio contra as maldades e ciladas do demônio. Ordene-lhe Deus, instantemente o pedimos, e vós, príncipe da milícia celeste, pela virtude divina, precipitai no inferno a Satanás e aos outros espíritos malignos que andam pelo mundo para perder as almas. Amém."),
 o("Antes de viajar","Senhor, acompanhai-me nesta viagem. Guardai-me de todo perigo no caminho e protegei também os que ficam. Que eu chegue em paz ao meu destino e volte em paz para casa. Nossa Senhora, protegei os que viajam. Amém."),
 o("Antes de estudar ou de uma prova","Espírito Santo, dai-me atenção, memória e calma. Abençoai o meu esforço e afastai a ansiedade. Que eu use bem a inteligência que me destes. Amém."),
]),
("Gratidão",[
 o("Oração de agradecimento","Obrigado, Senhor, pela vida, pela fé e pelas pessoas que colocastes no meu caminho. Obrigado pelas graças que vejo e pelas que nem percebo. Obrigado até pelas dificuldades que me fizeram crescer. Que toda a minha vida seja um grande \"obrigado\" a vós. Com Maria, eu canto: a minha alma engrandece o Senhor! Amém."),
 "<div class='box'>\"Em tudo dai graças, pois esta é a vontade de Deus a vosso respeito em Cristo Jesus\" (1Ts 5,18).</div>",
]),
]
for t,items in secs:
    P.append(page(t,"".join(items)))
build("Bonus-3-Oracoes-para-Cada-Momento",P)

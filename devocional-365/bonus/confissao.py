from base import *
P=[cover("PRESENTE ESPECIAL · BÔNUS 2","Guia da Confissão","Como se preparar, exame de consciência completo e o passo a passo para voltar ao abraço do Pai")]
P.append(page("O abraço do Pai","""
<p>A Confissão, também chamada Sacramento da Reconciliação ou da Penitência, é o encontro com a misericórdia de Deus. Jesus deu aos apóstolos o poder de perdoar os pecados: "A quem perdoardes os pecados, eles serão perdoados" (Jo 20,23). Por meio do padre, é o próprio Cristo quem nos perdoa.</p>
<p>Lembre-se da parábola do filho que volta para casa (Lc 15,11-24): o pai <b>corre</b> ao seu encontro antes mesmo de ouvir o pedido de perdão. É assim que Deus espera você.</p>
<div class="box">Maria é chamada "Refúgio dos pecadores". Antes de se confessar, peça a ela coragem e um coração sincero.</div>
<h3>Os cinco passos de uma boa confissão</h3>
<ol><li><b>Exame de consciência:</b> lembrar com calma os pecados cometidos.</li>
<li><b>Arrependimento:</b> sentir dor por ter ofendido a Deus, que é tão bom.</li>
<li><b>Propósito:</b> decidir, com a ajuda da graça, não voltar a pecar e evitar as ocasiões de pecado.</li>
<li><b>Confissão:</b> dizer os pecados ao padre com sinceridade.</li>
<li><b>Penitência:</b> cumprir o que o padre indicar, como sinal de conversão.</li></ol>
"""))
def ex(title,items,intro=""):
    return f"<h3>{title}</h3>"+(f"<p class='small'>{intro}</p>" if intro else "")+"<ul class='q'>"+"".join(f"<li>{esc(i)}</li>" for i in items)+"</ul>"
P.append(page("Exame de consciência (1)","""<p>Leia com calma, em um lugar silencioso. Peça antes ao Espírito Santo: <i>"Vinde, Espírito Santo, iluminai a minha consciência para que eu reconheça meus pecados com sinceridade e sem medo."</i></p>"""+
ex("1º mandamento: Amar a Deus sobre todas as coisas",["Deixei de rezar por longos períodos ou rezei só por obrigação?","Duvidei da fé de propósito, ou tive vergonha de ser cristão?","Recorri a horóscopo, simpatias, cartomantes, amuletos ou práticas de magia e superstição?","Coloquei dinheiro, trabalho, prazer ou alguma pessoa acima de Deus?","Desesperei da misericórdia de Deus ou abusei dela, pecando porque \"depois é só confessar\"?"])+
ex("2º mandamento: Não usar o santo nome de Deus em vão",["Usei o nome de Deus, de Jesus, de Maria ou dos santos com falta de respeito?","Blasfemei, falei mal de Deus ou da Igreja com desprezo?","Fiz promessas a Deus e não cumpri, ou jurei em falso?"])+
ex("3º mandamento: Guardar domingos e festas",["Faltei à Missa aos domingos ou em dias santos de guarda sem motivo grave?","Cheguei atrasado ou fiquei distraído de propósito durante a Missa?","Trabalhei ou fiz outros trabalhar sem necessidade no domingo, deixando de lado o descanso e a família?"])
))
P.append(page("Exame de consciência (2)",
ex("4º mandamento: Honrar pai e mãe",["Desrespeitei, maltratei ou abandonei meus pais, especialmente na velhice ou na doença?","Como pai ou mãe, deixei de educar meus filhos na fé, de dar bom exemplo ou de dedicar tempo a eles?","Fui causa de brigas e divisões na minha família?"])+
ex("5º mandamento: Não matar",["Agredi alguém com atos ou palavras? Guardei ódio, rancor ou desejo de vingança?","Coloquei em risco a minha vida ou a dos outros (bebida ao volante, drogas, imprudência)?","Participei, aconselhei ou apoiei um aborto?","Descuidei da minha saúde de forma grave, ou desejei a morte de alguém?","Neguei perdão a quem me pediu?"])+
ex("6º e 9º mandamentos: Não pecar contra a castidade e não desejar a mulher (ou o homem) do próximo",["Fui infiel no matrimônio, em atos, conversas ou pensamentos consentidos?","Consumi pornografia ou alimentei pensamentos e desejos impuros de forma consciente?","Tive relações sexuais fora do matrimônio?","Desrespeitei o meu corpo ou o corpo de outra pessoa?"])
))
P.append(page("Exame de consciência (3)",
ex("7º e 10º mandamentos: Não furtar e não cobiçar as coisas alheias",["Roubei, enganei no troco, soneguei impostos, fraudei ou fiquei com o que não era meu?","Deixei de pagar dívidas ou salários justos?","Fui desonesto no trabalho, faltando com minhas obrigações?","Desperdicei dinheiro em jogos ou luxos, deixando a família passar necessidade?","Tive inveja dos bens ou do sucesso dos outros?"])+
ex("8º mandamento: Não levantar falso testemunho",["Menti, mesmo em coisas pequenas?","Fiz fofoca, espalhei defeitos alheios ou caluniei alguém?","Julguei os outros sem conhecer a verdade?","Revelei segredos que me foram confiados?"])+
ex("Mandamentos da Igreja",["Deixei de me confessar ao menos uma vez por ano?","Deixei de comungar ao menos na Páscoa?","Comunguei em estado de pecado grave, sem antes me confessar?","Deixei de observar o jejum e a abstinência nos dias indicados pela Igreja?","Deixei de ajudar a Igreja nas suas necessidades, conforme minhas possibilidades?"])
))
P.append(page("Exame de consciência (4)","<p class='small'>Os sete pecados capitais são as raízes de muitos outros pecados. Olhar para eles ajuda a conhecer a si mesmo.</p>"+
ex("Os pecados capitais",["Soberba: me achei melhor que os outros, quis sempre ter razão, desprezei alguém?","Avareza: fui apegado demais ao dinheiro e às coisas, ou deixei de ajudar quem precisava?","Luxúria: deixei os desejos desordenados governarem minhas escolhas?","Ira: perdi o controle, gritei, ofendi, guardei raiva?","Gula: comi ou bebi em excesso, sem moderação?","Inveja: fiquei triste com o bem dos outros ou alegre com o mal deles?","Preguiça: fui negligente com a oração, com o trabalho ou com minhas obrigações?"])+
ex("Omissões",["Deixei de fazer o bem que podia fazer?","Vi alguém precisando e fingi que não vi?","Deixei de defender a verdade ou alguém injustiçado por medo?"])+
"<div class='box'>Se lembrar de algo grave que não estava nesta lista, também confesse. O exame é um guia, não uma lista completa.</div>"))
P.append(page("Na hora da confissão","""
<ol>
<li>Faça o <b>Sinal da Cruz</b>. O padre pode dizer uma breve saudação ou ler um trecho da Palavra.</li>
<li>Diga: <i>"Padre, abençoe-me porque pequei. Minha última confissão foi há (tempo aproximado)."</i></li>
<li><b>Diga seus pecados</b> com simplicidade, sem rodeios e sem justificativas. Para os pecados graves, diga também, se possível, quantas vezes aconteceram.</li>
<li>Termine dizendo: <i>"Destes pecados e de todos os da minha vida, peço perdão a Deus."</i></li>
<li><b>Ouça os conselhos</b> do padre e a penitência que ele indicar.</li>
<li>Reze o <b>Ato de Contrição</b> quando o padre pedir.</li>
<li>O padre dará a <b>absolvição</b>. Responda: <i>"Amém."</i></li>
<li>Agradeça e cumpra a penitência o quanto antes.</li>
</ol>
<h3>Ato de Contrição</h3>
<p>Meu Deus, eu me arrependo de todo o coração de vos ter ofendido, porque sois infinitamente bom e digno de ser amado sobre todas as coisas. Proponho firmemente, com o auxílio da vossa graça, emendar-me e evitar as ocasiões de pecado. Senhor, tende piedade de mim, pecador. Amém.</p>
"""))
P.append(page("Dúvidas comuns","""
<h3>Tenho vergonha. E se o padre me julgar?</h3><p>O padre está ali como instrumento da misericórdia de Deus, e ele mesmo também se confessa. Ele já ouviu de tudo e é obrigado ao <b>sigilo absoluto</b>: nunca pode revelar o que ouviu, sob nenhuma circunstância.</p>
<h3>E se eu esquecer um pecado?</h3><p>Se você esqueceu sem querer, ele também foi perdoado. Se lembrar depois de um pecado grave, mencione-o na próxima confissão.</p>
<h3>Faz muito tempo que não me confesso. E agora?</h3><p>Não tem problema. Diga isso ao padre logo no início. Ele vai ajudar você. Quanto mais tempo longe, maior será a alegria do reencontro.</p>
<h3>Com que frequência devo me confessar?</h3><p>A Igreja pede ao menos uma vez por ano, e sempre antes de comungar se houver pecado grave. Muitos santos recomendam a confissão frequente, por exemplo uma vez por mês, como caminho de crescimento.</p>
<h3>Depois da confissão</h3><p>Agradeça a Deus, cumpra a penitência e, se puder, participe da Missa e comungue. Escolha um ponto concreto para melhorar e peça a Maria que o ajude a perseverar.</p>
<div class="box">"Haverá mais alegria no céu por um só pecador que se converte do que por noventa e nove justos que não precisam de conversão" (Lc 15,7).</div>
<p class="small">Este guia é um auxílio pessoal. Em caso de dúvidas, converse com um sacerdote.</p>
"""))
build("Bonus-2-Guia-da-Confissao",P)

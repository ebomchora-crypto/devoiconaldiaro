import glob, html, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dados")
meses = []
for f in sorted(glob.glob(D + "/*.txt")):
    tema = ""; dias = []
    for ln in open(f, encoding="utf-8").read().splitlines():
        if ln.startswith("#"): tema = ln[1:].strip(); continue
        if ln.strip(): 
            p = ln.split("|"); assert len(p) == 6, ln[:60]; dias.append(p)
    meses.append((tema, dias))
assert sum(len(d) for _, d in meses) == 365
e = html.escape
misterios = ["Gozosos","Dolorosos","Gloriosos","Luminosos","Dolorosos","Gozosos","Gloriosos"]
semana = ["segunda","terça","quarta","quinta","sexta","sábado","domingo"]

css = """
@page{size:148mm 210mm;margin:14mm 13mm 16mm 13mm}
*{box-sizing:border-box}
body{font-family:'Georgia','Times New Roman',serif;color:#1f1f1f;font-size:10.6pt;line-height:1.5;margin:0}
.pg{page-break-after:always;min-height:178mm;position:relative}
.cover{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;height:178mm;background:#fff}
.cover h1{font-size:34pt;margin:.1em 0;color:#7a1f2b;font-style:italic}
.cover .sub{font-size:13pt;color:#555}
.cover .cross{font-size:40pt;color:#7a1f2b}
h2{color:#7a1f2b;text-align:center;font-size:15pt;margin:0 0 .6em}
h3{font-size:11pt;margin:.9em 0 .2em;color:#7a1f2b}
.pray p{margin:.2em 0 .6em}
.dia{text-align:center;margin-bottom:.8em}
.dia .n{font-family:Arial,sans-serif;font-size:10pt;letter-spacing:.12em;color:#7a1f2b}
.dia .t{font-size:15pt;font-weight:bold;margin:.15em 0}
.dia .m{font-size:9pt;color:#777;font-family:Arial,sans-serif}
.box{background:#f1eeee;border-radius:3px;padding:.7em .9em;font-style:italic;margin:.6em 0}
.lbl{font-weight:bold;margin:.9em 0 .15em}
.prop{border-left:3px solid #7a1f2b;padding:.1em .7em;margin:.8em 0}
.oracao{text-align:center;font-style:italic;margin-top:1em}
.terco{position:absolute;bottom:0;left:0;right:0;text-align:center;font-size:8.5pt;color:#777;font-family:Arial,sans-serif}
.mes{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;height:178mm}
.mes h2{font-size:22pt}
.ln{border-bottom:1px solid #b9a98a;height:7.2mm}.diario{margin-top:1.1em;border-top:1px dashed #b9a98a;padding-top:.5em}.diario .h{font-family:Arial,sans-serif;font-size:8.5pt;letter-spacing:.1em;color:#7a1f2b;text-transform:uppercase}.latim{font-style:italic;color:#555}.cant h3{margin-top:1.1em}ul.ind{list-style:none;padding:0;font-size:10pt}
ul.ind li{margin:.25em 0}
"""

oracoes = """
<h3>Sinal da Cruz</h3><p>Pelo sinal da Santa Cruz, livrai-nos, Deus, nosso Senhor, dos nossos inimigos. Em nome do Pai, e do Filho, e do Espírito Santo. Amém.</p>
<h3>Credo</h3><p>Creio em Deus Pai todo-poderoso, Criador do céu e da terra; e em Jesus Cristo, seu único Filho, nosso Senhor, que foi concebido pelo poder do Espírito Santo, nasceu da Virgem Maria, padeceu sob Pôncio Pilatos, foi crucificado, morto e sepultado; desceu à mansão dos mortos, ressuscitou ao terceiro dia, subiu aos céus, está sentado à direita de Deus Pai todo-poderoso, donde há de vir a julgar os vivos e os mortos. Creio no Espírito Santo, na santa Igreja Católica, na comunhão dos santos, na remissão dos pecados, na ressurreição da carne, na vida eterna. Amém.</p>
<h3>Pai-Nosso</h3><p>Pai nosso, que estais nos céus, santificado seja o vosso nome, venha a nós o vosso reino, seja feita a vossa vontade, assim na terra como no céu. O pão nosso de cada dia nos dai hoje, perdoai-nos as nossas ofensas, assim como nós perdoamos a quem nos tem ofendido, e não nos deixeis cair em tentação, mas livrai-nos do mal. Amém.</p>
<h3>Ave-Maria</h3><p>Ave, Maria, cheia de graça, o Senhor é convosco, bendita sois vós entre as mulheres e bendito é o fruto do vosso ventre, Jesus. Santa Maria, Mãe de Deus, rogai por nós, pecadores, agora e na hora da nossa morte. Amém.</p>
<h3>Glória ao Pai</h3><p>Glória ao Pai, ao Filho e ao Espírito Santo. Como era no princípio, agora e sempre. Amém.</p>
<h3>Oração de Fátima</h3><p>Ó meu Jesus, perdoai-nos, livrai-nos do fogo do inferno, levai as almas todas para o céu, e socorrei principalmente as que mais precisarem. Amém.</p>
<h3>Salve-Rainha</h3><p>Salve, Rainha, Mãe de misericórdia, vida, doçura e esperança nossa, salve! A vós bradamos, os degredados filhos de Eva. A vós suspiramos, gemendo e chorando neste vale de lágrimas. Eia, pois, advogada nossa, esses vossos olhos misericordiosos a nós volvei. E depois deste desterro, mostrai-nos Jesus, bendito fruto do vosso ventre. Ó clemente, ó piedosa, ó doce sempre Virgem Maria. Rogai por nós, santa Mãe de Deus, para que sejamos dignos das promessas de Cristo. Amém.</p>
<h3>Lembrai-vos (Oração de São Bernardo)</h3><p>Lembrai-vos, ó piíssima Virgem Maria, de que nunca se ouviu dizer que algum daqueles que tenham recorrido à vossa proteção, implorado a vossa assistência e reclamado o vosso socorro, fosse por vós desamparado. Animado eu, pois, com igual confiança, a vós, Virgem entre todas singular, como a Mãe recorro, de vós me valho e, gemendo sob o peso dos meus pecados, me prostro aos vossos pés. Não rejeiteis as minhas súplicas, ó Mãe do Filho de Deus humanado, mas dignai-vos de as ouvir propícia e de me alcançar o que vos rogo. Amém.</p>
"""

mist = """
<h3>Mistérios Gozosos (segundas e sábados)</h3><p>1. A Anunciação do anjo a Maria. 2. A Visitação de Maria a Isabel. 3. O Nascimento de Jesus em Belém. 4. A Apresentação do Menino Jesus no Templo. 5. A perda e o encontro do Menino Jesus no Templo.</p>
<h3>Mistérios Luminosos (quintas-feiras)</h3><p>1. O Batismo de Jesus no Jordão. 2. As bodas de Caná. 3. O anúncio do Reino de Deus e o convite à conversão. 4. A Transfiguração de Jesus. 5. A instituição da Eucaristia.</p>
<h3>Mistérios Dolorosos (terças e sextas)</h3><p>1. A agonia de Jesus no Horto das Oliveiras. 2. A flagelação de Jesus. 3. A coroação de espinhos. 4. Jesus carrega a cruz até o Calvário. 5. A crucifixão e morte de Jesus.</p>
<h3>Mistérios Gloriosos (quartas-feiras e domingos)</h3><p>1. A Ressurreição de Jesus. 2. A Ascensão de Jesus ao céu. 3. A vinda do Espírito Santo sobre os apóstolos. 4. A Assunção de Nossa Senhora. 5. A coroação de Nossa Senhora no céu.</p>
"""
como = """
<h3>Como rezar o terço</h3>
<p>1. Faça o Sinal da Cruz e reze o Credo no crucifixo. 2. Na primeira conta grande, reze um Pai-Nosso; nas três contas pequenas, três Ave-Marias; depois o Glória. 3. Anuncie o 1º mistério e reze um Pai-Nosso. 4. Reze dez Ave-Marias meditando o mistério, e termine com o Glória e a Oração de Fátima. 5. Repita para os demais mistérios. 6. Ao final, reze a Salve-Rainha e faça o Sinal da Cruz.</p>
"""

apres = """
<h2>Apresentação</h2>
<p>Este devocional foi pensado para acompanhar você durante um ano inteiro, um dia por vez, tendo Maria como mestra e companheira. Cada dia traz uma <b>meditação com Maria</b>, uma passagem da <b>Palavra de Deus</b>, um <b>propósito concreto</b> para o dia, uma <b>pequena oração</b> e um espaço para o seu <b>diário espiritual</b> e para a <b>gratidão</b>. Ao fim de cada mês há uma <b>revisão</b> (exame de consciência, gratidão e propósito). No início do livro você encontra o roteiro do <b>Santo Terço</b>, um guia de <b>adoração em silêncio</b>, <b>cantos marianos</b> e uma página de <b>intenções</b>. Reserve de 5 a 10 minutos, de preferência sempre no mesmo horário.</p>
<p>Os 12 meses seguem um caminho: <b>janeiro</b>, começar com Maria; <b>fevereiro</b>, seguir Jesus; <b>março</b>, o Sermão da Montanha; <b>abril</b>, o poder de Jesus; <b>maio</b>, o mês de Maria; <b>junho</b>, as parábolas; <b>julho</b>, discípulos em missão; <b>agosto</b>, o Evangelho de João; <b>setembro</b>, misericórdia até a cruz; <b>outubro</b>, o Rosário; <b>novembro</b>, a eternidade; <b>dezembro</b>, Advento e Natal.</p>
<p><b>Como usar:</b> 1) Faça o sinal da cruz e peça a ajuda do Espírito Santo. 2) Leia a meditação. 3) Abra a sua Bíblia e leia a passagem indicada; o resumo ajuda, mas não substitui o texto sagrado. 4) Assuma o propósito do dia. 5) Reze a oração e uma Ave-Maria. 6) Anote no diário e agradeça. 7) Se puder, reze também o terço indicado no rodapé. <i>Este é um material digital em PDF, para ler no celular, tablet ou computador, ou para imprimir.</i></p>
<p><i>Os resumos bíblicos são paráfrases. As orações tradicionais (Credo, Pai-Nosso, Ave-Maria, Salve-Rainha, Lembrai-vos) são de domínio comum da Igreja. Os textos de meditação, os propósitos e as orações breves são originais desta obra.</i></p>
"""


adoracao = """
<h2>Momento de Adoração em Silêncio</h2>
<p>A adoração é estar diante de Deus sem pressa e sem pedir nada, apenas reconhecendo a grandeza dele. Reserve de 10 a 15 minutos, uma vez por semana ou sempre que puder.</p>
<h3>Como fazer</h3>
<p><b>1. Acomode-se.</b> Sente-se com a coluna reta e as mãos abertas no colo. Desligue o celular.<br>
<b>2. Faça o Sinal da Cruz</b> e diga em silêncio: "Senhor, eu estou aqui".<br>
<b>3. Reconheça quem ele é.</b> Repita devagar, uma frase de cada vez: "Tu és Santo. Tu és o Criador. Tu és meu Pai. Tu és bom."<br>
<b>4. Fique em silêncio</b> por alguns minutos. Se a mente se distrair, volte com calma para a frase "Jesus, eu confio em ti".<br>
<b>5. Una-se a Maria.</b> Peça a ela: "Mãe, adora comigo teu Filho".<br>
<b>6. Termine agradecendo</b> e rezando uma Ave-Maria.</p>
<p><i>Se puder, faça a adoração diante do Santíssimo Sacramento em uma igreja ou capela.</i></p>
"""
cantos = """
<h2>Cantos e Louvores Marianos</h2>
<p>Cantar é rezar duas vezes. Estes são cantos antigos da Igreja, de domínio público, com tradução para o português. Você pode rezá-los em voz alta ou procurar suas versões em canto gregoriano para ouvir.</p>
<div class="cant">
<h3>Salve, Rainha (Salve Regina)</h3>
<p class="latim">Salve, Regina, Mater misericordiae; vita, dulcedo et spes nostra, salve. Ad te clamamus, exsules filii Hevae. Ad te suspiramus, gementes et flentes in hac lacrimarum valle. Eia ergo, advocata nostra, illos tuos misericordes oculos ad nos converte. Et Iesum, benedictum fructum ventris tui, nobis post hoc exsilium ostende. O clemens, o pia, o dulcis Virgo Maria.</p>
<p>(Em português, veja a Salve-Rainha na página de orações.)</p>
<h3>Ave, Estrela do Mar (Ave Maris Stella)</h3>
<p class="latim">Ave, maris stella, Dei Mater alma, atque semper Virgo, felix caeli porta. Sumens illud "Ave" Gabrielis ore, funda nos in pace, mutans Hevae nomen. Solve vincla reis, profer lumen caecis, mala nostra pelle, bona cuncta posce.</p>
<p>Salve, estrela do mar, Mãe santa de Deus, sempre Virgem, feliz porta do céu. Acolhendo aquele "Ave" dos lábios de Gabriel, firma-nos na paz, mudando o nome de Eva. Desata as correntes dos culpados, dá luz aos cegos, afasta os nossos males e alcança-nos todos os bens.</p>
<h3>Rainha do Céu (Regina Caeli)</h3>
<p class="latim">Regina caeli, laetare, alleluia: quia quem meruisti portare, alleluia, resurrexit, sicut dixit, alleluia: ora pro nobis Deum, alleluia.</p>
<p>Rainha do céu, alegrai-vos, aleluia, porque aquele que merecestes trazer em vosso seio, aleluia, ressuscitou como disse, aleluia. Rogai a Deus por nós, aleluia.</p>
<h3>Sob a Vossa Proteção (Sub Tuum Praesidium)</h3>
<p class="latim">Sub tuum praesidium confugimus, Sancta Dei Genetrix; nostras deprecationes ne despicias in necessitatibus, sed a periculis cunctis libera nos semper, Virgo gloriosa et benedicta.</p>
<p>Sob a vossa proteção nos refugiamos, santa Mãe de Deus. Não desprezeis as nossas súplicas em nossas necessidades, mas livrai-nos sempre de todos os perigos, ó Virgem gloriosa e bendita.</p>
<h3>O Canto de Maria (paráfrase do Magnificat, Lc 1,46-55)</h3>
<p>Minha alma engrandece o Senhor, e meu espírito se alegra em Deus, meu Salvador, porque ele olhou para a humildade de sua serva. De agora em diante todas as gerações me chamarão feliz, pois o Poderoso fez grandes coisas por mim, e santo é o seu nome. Sua misericórdia se estende de geração em geração sobre os que o temem. Ele derrubou os poderosos de seus tronos e levantou os humildes; encheu de bens os famintos e despediu os ricos de mãos vazias. Socorreu Israel, seu servo, lembrando-se de sua misericórdia, como prometeu aos nossos pais.</p>
</div>
"""
intencoes = """
<h2>Minhas Intenções</h2>
<p>Escreva aqui as pessoas e as causas pelas quais você quer rezar durante este ano. Volte a esta página sempre que precisar.</p>
<h3>Por minha família</h3>""" + '<div class="ln"></div>'*3 + """
<h3>Pelos meus amigos e por quem sofre</h3>""" + '<div class="ln"></div>'*3 + """
<h3>Pelos falecidos</h3>""" + '<div class="ln"></div>'*2 + """
<h3>Minhas graças a pedir</h3>""" + '<div class="ln"></div>'*3 + """
<h3>Graças recebidas</h3>""" + '<div class="ln"></div>'*3

revisao = """
<h2>Revisão do Mês</h2>
<p><i>Pare um pouco e olhe para os últimos dias com Deus.</i></p>
<h3>Gratidão: pelo que sou grato neste mês?</h3>""" + '<div class="ln"></div>'*3 + """
<h3>Crescimento: em que cresci na fé?</h3>""" + '<div class="ln"></div>'*2 + """
<h3>Exame de consciência: o que preciso melhorar?</h3>""" + '<div class="ln"></div>'*2 + """
<h3>Disciplina: consegui manter minha oração diária? O que me ajudou?</h3>""" + '<div class="ln"></div>'*2 + """
<h3>Intercessão: por quem vou rezar no próximo mês?</h3>""" + '<div class="ln"></div>'*2 + """
<h3>Meu propósito para o próximo mês</h3>""" + '<div class="ln"></div>'*2

out = ['<html><head><meta charset="utf-8"><style>%s</style></head><body>' % css]
out.append('<div class="pg cover"><div class="cross">✝</div><h1>365 dias com Maria</h1><div class="sub">Devocional diário para rezar<br>a Palavra e o terço com Nossa Senhora</div></div>')
out.append('<div class="pg">%s</div>' % apres)
out.append('<div class="pg pray"><h2>Santo Terço</h2>%s%s</div>' % (como, mist))
out.append('<div class="pg pray"><h2>Orações</h2>%s</div>' % oracoes)
out.append('<div class="pg pray">%s</div>' % adoracao)
out.append('<div class="pg pray cant">%s</div>' % cantos)
out.append('<div class="pg pray">%s</div>' % intencoes)
n = 0
for (tema, dias) in meses:
    out.append('<div class="pg mes"><h2>%s</h2></div>' % e(tema))
    for (t, ref, pal, med, prop, jac) in dias:
        n += 1
        mis = misterios[(n-1) % 7]
        out.append(
          '<div class="pg"><div class="dia"><div class="n">DIA %d</div><div class="t">%s</div><div class="m">%s</div></div>'
          '<div class="box">%s</div>'
          '<div class="lbl">Palavra de Deus (%s)</div><div>%s <i>Leia o texto completo na sua Bíblia.</i></div>'
          '<div class="prop"><b>Propósito do dia:</b> %s</div>'
          '<div class="oracao">%s<br>Ave, Maria, cheia de graça…</div>'
          '<div class="diario"><div class="h">Hoje agradeço por</div><div class="ln"></div><div class="h" style="margin-top:.7em">Meu diário espiritual</div><div class="ln"></div><div class="ln"></div><div class="ln"></div></div>'
          '<div class="terco">Terço de hoje: Mistérios %s</div></div>'
          % (n, e(t), e(tema.split("—")[0].strip()), e(med), e(ref), e(pal), e(prop), e(jac), mis))
    out.append('<div class="pg pray">%s</div>' % revisao)
out.append('<div class="pg pray"><h2>Oração final</h2><p>Maria, minha Mãe, coloca a tua mão sobre mim. Guarda os meus pensamentos, meus sentimentos, minhas palavras e minhas ações, para que eu viva como teu Filho Jesus me ensina. Conduze-me hoje, amanhã e sempre. Em nome do Pai, e do Filho, e do Espírito Santo. Amém.</p></div>')
out.append('</body></html>')
open(os.path.join(os.path.dirname(D), "devocional-365-dias-com-maria.html"), "w", encoding="utf-8").write("\n".join(out))
print("ok", n)

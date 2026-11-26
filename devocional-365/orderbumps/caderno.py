from base import *
def L(n,h=6.0): return ''.join(f'<div style="border-bottom:1px solid #b9a98a;height:{h}mm"></div>' for _ in range(n))
def H(t): return f'<h3>{t}</h3>'
P=[cover("365 DIAS COM MARIA · COMPLEMENTO","Caderno de Intenções e Graças","Um diário de 12 meses para anotar seus pedidos, agradecer e acompanhar o que Deus vai fazendo na sua vida")]
P.append(page("Como usar este caderno","""
<p>Este caderno foi pensado para ser <b>imprimido</b> (em A5 ou A4) ou preenchido em um aplicativo de anotações no tablet. Ele acompanha o seu devocional de 365 dias com Maria.</p>
<h3>Rotina sugerida</h3>
<ol>
<li><b>No início do mês:</b> leia o tema, escolha um propósito e escreva suas intenções.</li>
<li><b>Durante o mês:</b> quando uma graça chegar, grande ou pequena, anote na página de graças.</li>
<li><b>No fim de cada semana:</b> escreva três motivos de gratidão.</li>
<li><b>No fim do ano:</b> releia tudo e faça o balanço. Você vai se surpreender.</li>
</ol>
<div class="box">Anotar fortalece a memória da fé. Quando a dúvida vier, você poderá reler o que Deus já fez.</div>
<p class="small">Uma graça nem sempre é o que pedimos. Às vezes é força, paz, uma pessoa que aparece, um novo olhar. Anote tudo o que perceber.</p>
"""))
P.append(page("Meu ano com Maria","""
<h3>Minha intenção principal para este ano</h3>"""+L(3)+"""
<h3>Uma palavra para guiar o meu ano (ex.: confiança, paz, perdão)</h3>"""+L(1)+"""
<h3>O que quero pedir a Deus por intercessão de Maria</h3>"""+L(4)+"""
<h3>Pessoas por quem quero rezar durante o ano</h3>"""+L(4)+"""
<h3>Meu compromisso de oração (horário, lugar, quantidade)</h3>"""+L(3)))
meses=[
("Janeiro","Santa Maria, Mãe de Deus (1º de janeiro)","Começar o ano entregando-o a Maria. Pense em como quer viver os próximos 12 meses."),
("Fevereiro","Nossa Senhora de Lourdes (11 de fevereiro)","Rezar pelos doentes e por quem cuida deles."),
("Março","São José (19 de março)","Confiar a São José o trabalho, a família e o sustento."),
("Abril","Tempo Pascal e Divina Misericórdia","Viver a alegria da Ressurreição e a misericórdia de Deus."),
("Maio","Mês de Maria","Aproximar-se de Nossa Senhora todos os dias, com o terço ou uma Ave-Maria."),
("Junho","Mês do Sagrado Coração de Jesus","Pedir um coração manso e humilde, como o de Jesus."),
("Julho","Mês do Preciosíssimo Sangue","Agradecer a salvação e rezar pelos que se afastaram."),
("Agosto","Assunção de Nossa Senhora (15 de agosto) e mês das vocações","Rezar por padres, religiosos e pela vocação de cada um."),
("Setembro","Nossa Senhora das Dores (15 de setembro) e mês da Bíblia","Ler a Palavra de Deus e unir as dores à cruz de Jesus."),
("Outubro","Mês do Rosário e das Missões","Rezar o terço em família e pelos missionários."),
("Novembro","Todos os Santos e Fiéis Defuntos","Rezar pelos que já partiram e pedir a intercessão dos santos."),
("Dezembro","Imaculada Conceição (8 de dezembro), Advento e Natal","Preparar o coração para o Natal e agradecer o ano vivido."),
]
for m,tema,prop in meses:
    P.append(page(m,f"""
<div class="box"><b>Tema do mês:</b> {esc(tema)}<br><b>Sugestão:</b> {esc(prop)}</div>
<h3>Meu propósito para este mês</h3>{L(2)}
<h3>Minhas intenções deste mês</h3>{L(5)}
<h3>Pessoas por quem vou rezar</h3>{L(3)}
<h3>Versículo ou frase que quero guardar</h3>{L(2)}
"""))
    P.append(page(f"{m}: graças e gratidão",f"""
<h3>Graças recebidas neste mês (data e o que aconteceu)</h3>{L(5)}
<h3>Semana 1: três motivos de gratidão</h3>{L(2,5.6)}
<h3>Semana 2: três motivos de gratidão</h3>{L(2,5.6)}
<h3>Semana 3: três motivos de gratidão</h3>{L(2,5.6)}
<h3>Semana 4: três motivos de gratidão</h3>{L(2,5.6)}
<h3>Como foi minha oração neste mês? O que me ajudou?</h3>{L(2,5.6)}
"""))
P.append(page("Balanço do ano","""
<h3>As maiores graças que recebi neste ano</h3>"""+L(5)+"""
<h3>Pedidos que Deus atendeu (do jeito dele)</h3>"""+L(4)+"""
<h3>Pedidos que continuam e que entrego com confiança</h3>"""+L(4)+"""
<h3>O que aprendi sobre mim e sobre Deus</h3>"""+L(3)+"""
<h3>Meu propósito para o próximo ano</h3>"""+L(2)))
P.append(page("Páginas livres","<p class='small'>Use para anotar reflexões, orações próprias, pensamentos do dia e do que mais quiser.</p>"+L(22)))
build("Order-Bump-2-Caderno-de-Intencoes-e-Gracas",P)

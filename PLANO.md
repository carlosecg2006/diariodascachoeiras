# Diário das Cachoeiras — Plano do app

Um diário de cachoeiras que mistura diário de papel com álbum de fotos. Você registra as cachoeiras que visitou, guarda as fotos de cada uma, coleciona broches (conquistas) e encontra cachoeiras e trilhas por perto.

## Decisões já tomadas

- **Formato: PWA.** O site é o próprio app. A pessoa abre o link no celular e adiciona à tela de início (no iPhone, pelo Safari: Compartilhar → "Adicionar à Tela de Início"). Funciona no iPhone e no Android, é grátis e atualiza sozinho.
- **Privado e pessoal.** Só entra quem for convidado, com login. Cada pessoa tem o próprio diário. **Não há troca de informações entre as pessoas:** ninguém vê o diário, as fotos ou as avaliações dos outros.
- **Banco, login e fotos:** Supabase.
- **Dados das cachoeiras e trilhas:** OpenStreetMap (gratuito).
- **Rota:** o app abre o Google Maps ou o Waze já com o destino.
- **Previsão do tempo:** Open-Meteo (gratuita).
- **Arte e ilustrações:** feitas pelo Claude (capa de couro, traços a lápis, broches, mesa de madeira, polaroids).

## Visual geral

- Fundo: mesa de madeira escura.
- O livro fica sobre a mesa. Na borda do app, ao lado do livro, ficam três atalhos:
  - Configurações
  - Coleção de broches (conquistas)
  - Busca de cachoeiras (o mapa)
- Estilo de álbum feito à mão: traços a lápis, letra de mão, fita adesiva e clipes segurando as polaroids, rabiscos nos cantos, manchas de café.
- **Celular:** uma página por vez.
- **Tela grande (computador, tablet deitado):** o livro aberto com as duas páginas lado a lado.
- **Sons:** página virando, câmera de polaroid, broche sendo pregado.

---

## 1. O livro

### Capa
- Ao entrar, aparece um livro fechado com capa de couro escrito "Diário das Cachoeiras".
- Ao tocar, o livro abre com animação.
- **Livro que envelhece:** quanto mais você usa, mais gasta fica a capa de couro.

### Páginas
- Cada página comporta **6 cachoeiras**.
- Enquanto houver espaço, a próxima vaga aparece como um **quadrado pontilhado com um "+"**, tudo desenhado a lápis.
  - Na primeira vez que a pessoa entra, a primeira página tem só o "+".
  - Exemplo: com 5 cachoeiras na página, a 6ª vaga é o "+". Com a página cheia, o "+" passa para a página seguinte.
- **Virar páginas com o dedo**, com animação de papel.
- **Sumário** nas primeiras páginas.
- **Mapa desenhado à mão** na última página, com todas as cachoeiras visitadas.
- **Fitinha marcadora** para pular direto para as favoritas.
- **Diário cheio vira "Volume II"**, e os volumes antigos ficam numa estante.

### Ordem e filtros
- **Padrão:** ordem de registro (a primeira registrada vem primeiro).
- Filtros e ordenações que a pessoa pode escolher:
  - Avaliação: da maior para a menor, ou o contrário
  - Data da visita
  - Data do registro
  - Estado
  - (outros a definir)

### Cada cachoeira na página
Cada cachoeira ocupa uma vaga da página e tem 4 partes, cada uma com sua ação:

| Parte | O que aparece | Ao tocar |
|---|---|---|
| **Título** | Nome da cachoeira e, ao lado, a data da visita | Abre o mapa com a rota até lá |
| **Fotos** | Pilha de polaroids vista de cima | Abre a galeria de fotos |
| **Estrelas** | Avaliação de 5 estrelas | Muda a avaliação na hora, quantas vezes quiser |
| **Botão "Detalhes"** | Botão embaixo | Abre os detalhes daquela cachoeira |

- **Carimbo de visitado**, como o de passaporte, com a data. Com check-in por GPS na cachoeira, vira "verificado".

---

## 2. Adicionar uma cachoeira (o "+")

- Tocar no "+" abre o formulário da visita.
- No campo do título, ao digitar, aparecem sugestões de cachoeiras para você tocar e escolher.
- **Cachoeira que não está no mapa:** dá para cadastrar uma nova normalmente. Ela entra no diário, mas **não tem rota**.
- Você adiciona as fotos e os detalhes (veja abaixo).

### Fotos
- **Até 10 fotos por cachoeira**, pensadas como "as 10 melhores" daquela visita.
- As fotos são comprimidas ao enviar. O plano gratuito do Supabase (1 GB) comporta cerca de 2 a 3 mil fotos.

---

## 3. Detalhes da cachoeira

Abre pelo botão "Detalhes".

- **Avaliações separadas**, além das 5 estrelas gerais:
  - Segurança
  - Movimento (vazia ou cheia)
  - (outras a definir, por exemplo: trilha, água, beleza)
- **"Como foi":** um texto livre, como num diário.
- **Ficha da visita:**
  - Com quem foi (nomes escritos à mão, só para você)
  - Dificuldade da trilha
  - Tempo de caminhada
  - Se dá para nadar
  - Temperatura da água
  - Se é paga
  - Onde estacionar
  - Se estava cheia
- **Galeria** com as fotos em polaroid, legenda em letra de mão embaixo de cada uma.

---

## 4. Broches (conquistas)

- A coleção fica numa **faixa de tecido**, como a de escoteiro, ou numa jaqueta jeans, com os broches pregados.
- **Os broches exigem check-in por GPS** na cachoeira. Sem check-in, a visita entra no diário, mas não conta para os broches.
- Exemplos de broches:
  - Primeira cachoeira
  - 5, 10 e 25 cachoeiras visitadas
  - Cachoeira com mais de 50 m
  - Três cachoeiras num mesmo fim de semana
  - Visitou no nascer do sol
  - Trilha difícil
  - Cachoeiras em 3 estados diferentes
  - "Desbravador": registrou uma cachoeira que não estava no mapa

---

## 5. Mapa e busca (o "maps de cachoeiras")

Um mapa próprio para cachoeiras, meio Pokémon GO, mas focado em buscar.

- Mostra as cachoeiras e trilhas mais próximas.
- Ordena e filtra por:
  - Mais perto
  - Mais seguras
  - Mais bem avaliadas
  - Mais ou menos movimento
  - Dificuldade
  - Se dá para nadar
  - Gratuita
  - Se dá para chegar de carro
- **Névoa no mapa:** as regiões vão se revelando conforme você visita cachoeiras.
- **Lista "quero ir":** a cachoeira aparece no diário como um post-it colado, esperando a visita.
- Tocar numa cachoeira abre a rota no Google Maps ou no Waze.

> **Em aberto:** como não há troca de dados entre as pessoas, segurança, avaliação e movimento só existem para as cachoeiras que você mesmo já avaliou. Falta decidir de onde vêm esses dados para cachoeiras que você ainda não visitou.

---

## 6. Segurança

- **Alerta de chuva e tromba d'água:** aviso quando há chuva prevista na região da cachoeira.
- **Mapa baixado** antes da trilha, para usar sem sinal.
- **Horário do pôr do sol**, para ninguém ficar no escuro na trilha.
- **Compartilhar a localização** com alguém de confiança (por WhatsApp, por exemplo).
- **Acesso rápido aos Bombeiros (193).**

---

## 7. Sem sinal (offline)

- O app guarda as fotos e o registro da visita no celular e envia quando a internet voltar.
- No iPhone, o envio acontece quando a pessoa abre o app de novo, não em segundo plano.
- No iPhone, as notificações só funcionam com o app adicionado à tela de início.
- Passo a passo com imagens, dentro do app, de como adicionar à tela de início.

---

## 8. Extras

- **Exportar o diário em PDF**, para imprimir como um livro de verdade.
- **Retrospectiva do ano:** cachoeiras visitadas, quilômetros de trilha, favorita do ano.
- **Nome final do app e endereço do site:** a definir.

---

## Ordem de construção

### Fase 1 — Primeira versão
- Login por convite
- Livro: capa, animação de abrir, páginas com 6 vagas, "+" a lápis, virar páginas, duas páginas em tela grande
- Adicionar cachoeira: busca por nome, cadastro de nova, até 10 fotos, data
- Cada cachoeira: título com rota, galeria, estrelas editáveis, detalhes
- Ordem e filtros do diário
- Funcionar sem sinal (guardar e enviar depois)
- Mesa de madeira e atalhos na borda

### Fase 2
- Check-in por GPS e carimbo verificado
- Broches e a faixa de broches
- Mapa e busca com filtros
- Lista "quero ir" com post-its
- Alerta de chuva, pôr do sol, 193 e compartilhar localização
- Sons

### Fase 3
- Névoa no mapa
- Sumário, mapa desenhado à mão, fitinha marcadora
- Livro que envelhece
- Volume II e estante
- Mapa baixado para usar offline
- Exportar em PDF
- Retrospectiva do ano

## Perguntas em aberto

- **Apagar uma cachoeira:** a vaga fica vazia ou as outras "sobem" para preencher? (resposta anterior ficou ambígua)
- **Voltar à mesma cachoeira:** vira um registro novo ou as fotos entram no registro que já existe?
- **Dados do mapa** para cachoeiras que você ainda não visitou (veja a seção 5).
- **Nome final e endereço do site.**

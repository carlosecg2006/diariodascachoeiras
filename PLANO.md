# Diário das Cachoeiras — Plano do app

Um diário de cachoeiras que mistura diário de papel com álbum de fotos. Você registra as cachoeiras que visitou, guarda as fotos de cada uma, coleciona broches (conquistas) e encontra cachoeiras e trilhas por perto.

## Decisões já tomadas

- **Formato: PWA.** O site é o próprio app. A pessoa abre o link no celular e adiciona à tela de início (no iPhone, pelo Safari: Compartilhar → "Adicionar à Tela de Início"). Funciona no iPhone e no Android, é grátis e atualiza sozinho.
- **Privado.** Só entra quem for convidado, com login.
- **Banco, login e fotos:** Supabase.
- **Dados das cachoeiras e trilhas:** OpenStreetMap (gratuito). Avaliações, segurança e movimento vêm dos próprios usuários.
- **Rota:** o app abre o Google Maps ou o Waze já com o destino.
- **Previsão do tempo:** Open-Meteo (gratuita).

## Visual geral

- Fundo: mesa de madeira escura.
- O livro fica sobre a mesa. Na borda do app, ao lado do livro, ficam três atalhos:
  - Configurações
  - Coleção de broches (conquistas)
  - Busca de cachoeiras (o mapa)
- Estilo de álbum feito à mão: traços a lápis, letra de mão, fita adesiva e clipes segurando as polaroids, rabiscos nos cantos, manchas de café.

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

### Cada cachoeira na página
- Nome da cachoeira e, ao lado, a data da visita.
- Embaixo, uma **pilha de fotos polaroid vista de cima**.
- Embaixo das fotos, as **5 estrelas** de avaliação e o botão **"Ver detalhes"**.
- **Carimbo de visitado**, como o de passaporte, com a data.

> Ponto a validar no protótipo: 6 cachoeiras com tudo isso ficam apertadas numa tela de celular. Se precisar, a página mostra só nome, data e polaroids, e as estrelas e os detalhes aparecem no post.

---

## 2. Adicionar uma cachoeira (o "+")

- Tocar no "+" abre o formulário da visita.
- No campo do título, ao digitar, aparecem sugestões de cachoeiras para você tocar e escolher.
- Com a cachoeira escolhida, **tocar no título abre o mapa com a rota** até lá.
- Você adiciona as fotos e os detalhes (veja a ficha da visita abaixo).

---

## 3. O post de cada cachoeira (modal estilo Instagram)

Tocar numa cachoeira do diário abre um modal parecido com um post do Instagram.

- **Fotos como polaroids** que você arrasta para o lado, com legenda em letra de mão embaixo de cada uma.
- **Avaliação de 5 estrelas.**
- **"Como foi":** um texto livre, como num diário.
- **Ficha da visita:**
  - Com quem foi (marcando amigos)
  - Dificuldade da trilha
  - Tempo de caminhada
  - Se dá para nadar
  - Temperatura da água
  - Se é paga
  - Onde estacionar
  - Se estava cheia
- **Carimbo verificado:** se você fizer check-in pelo GPS na cachoeira, o carimbo de visitado vira "verificado".
- **Comentários** dos amigos.

---

## 4. Broches (conquistas)

- A coleção fica numa **faixa de tecido**, como a de escoteiro, ou numa jaqueta jeans, com os broches pregados.
- Exemplos de broches:
  - Primeira cachoeira
  - 5, 10 e 25 cachoeiras visitadas
  - Cachoeira com mais de 50 m
  - Três cachoeiras num mesmo fim de semana
  - Visitou no nascer do sol
  - Trilha difícil
  - Cachoeiras em 3 estados diferentes
  - Foi com 5 amigos diferentes
  - "Descobridor": registrou uma cachoeira que ninguém do grupo tinha registrado

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

> Segurança, avaliação e movimento vêm das avaliações do grupo. No começo terão poucos dados, e o mapa vai "enchendo" com o uso.

---

## 6. Segurança

- **Alerta de chuva e tromba d'água:** aviso quando há chuva prevista na região da cachoeira.
- **Mapa baixado** antes da trilha, para usar sem sinal.
- **Horário do pôr do sol**, para ninguém ficar no escuro na trilha.
- **Compartilhar a localização** com alguém de confiança.
- **Acesso rápido aos Bombeiros (193).**

---

## 7. Entre amigos

- Ver o diário dos amigos e comentar nos posts.
- **Visita em grupo:** quando vão juntos, o mesmo post aparece no diário de todos.
- **Retrospectiva do ano:** cachoeiras visitadas, quilômetros de trilha, favorita do ano.

---

## 8. Sem sinal (offline)

- O app guarda as fotos e o registro da visita no celular e envia quando a internet voltar.
- No iPhone, o envio acontece quando a pessoa abre o app de novo, não em segundo plano.
- No iPhone, as notificações só funcionam com o app adicionado à tela de início.
- Passo a passo com imagens, dentro do app, de como adicionar à tela de início.

---

## Ordem de construção

### Fase 1 — Primeira versão
- Login por convite
- Livro: capa, animação de abrir, páginas com 6 vagas, "+" a lápis, virar páginas
- Adicionar cachoeira: busca por nome, fotos, data, ficha da visita
- Post estilo Instagram: polaroids, estrelas, "como foi"
- Botão de rota (Google Maps ou Waze)
- Funcionar sem sinal (guardar e enviar depois)
- Mesa de madeira e atalhos na borda

### Fase 2
- Broches e a faixa de broches
- Mapa e busca com filtros
- Lista "quero ir" com post-its
- Alerta de chuva, pôr do sol, 193 e compartilhar localização
- Amigos: ver diários, comentários, visita em grupo
- Check-in por GPS e carimbo verificado

### Fase 3
- Névoa no mapa
- Sumário, mapa desenhado à mão, fitinha marcadora
- Livro que envelhece
- Volume II e estante
- Mapa baixado para usar offline
- Retrospectiva do ano

## Pendências

- As skills de Expo, EAS e React Native instaladas em `.claude/skills/` eram para o caminho de app nativo. Com a escolha do PWA, trocar por skills de web (Next.js, por exemplo) antes de começar a construir.

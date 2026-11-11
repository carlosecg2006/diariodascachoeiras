# PWA em vez de app nativo

O app é um site que funciona como app no celular (PWA), instalado pela opção "Adicionar à Tela de Início", e não um app de loja feito com Expo ou React Native. Como o app é privado e só para pessoas convidadas, a loja não traz vantagem, e um app nativo no iPhone exigiria a conta de desenvolvedor da Apple (US$ 99 por ano) e reinstalação pelo TestFlight a cada 90 dias. O PWA é grátis no iPhone e no Android e se atualiza sozinho.

## Consequências

- No iPhone, o envio do que foi guardado sem sinal só acontece quando a pessoa abre o app de novo, não em segundo plano.
- No iPhone, as notificações só funcionam com o app adicionado à tela de início.
- Voltar para um app nativo depois significaria reescrever as telas.

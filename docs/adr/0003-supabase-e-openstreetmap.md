# Supabase para dados e fotos, OpenStreetMap para as cachoeiras

O login, o banco de dados e o armazenamento das fotos ficam no Supabase, e a lista de cachoeiras e trilhas do mapa vem do OpenStreetMap. Os dois são gratuitos na escala de um grupo pequeno, e o Supabase junta login por link mágico, banco com busca por distância e armazenamento de fotos num lugar só. A troca de qualquer um deles depois exigiria migrar dados e reescrever a parte do app que fala com eles.

## Consequências

- O plano gratuito do Supabase tem 1 GB para fotos, cerca de 2.500 fotos de 400 KB. Por isso cada visita tem no máximo 10 fotos, guardadas com até 2000 px.
- O que o OpenStreetMap não tiver marcado como cachoeira precisa ser cadastrado como cachoeira particular.

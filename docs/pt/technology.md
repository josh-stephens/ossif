# Tecnologia

A tecnologia da OSSIF serve à sua missão — ela não é a missão em si. Se uma ferramenta mais simples funcionar, use a ferramenta mais simples. Os designs abaixo representam a arquitetura pretendida; a implementação deve ser incremental e pragmática.

## O Portal de Conversação Avatar

A "porta de entrada" da OSSIF. Um lugar onde qualquer pessoa pode se envolver em um diálogo estruturado sobre eventos atuais, políticas e engajamento cívico.

### O que ele faz:

O Avatar não é uma autoridade. Ele é um **moderador, coach e explicador**. Ele faz quatro coisas bem:

1. **Clarificar alegações** — "O que estamos afirmando? Vamos separar as alegações fatuais das opiniões."
2. **Solicitar evidências** — "O que faria você mudar de ideia sobre isso?"
3. **Evidenciar compensações (*tradeoffs*)** — "Quem se beneficia? Quem paga? Quais são os riscos?"
4. **Manter a humanidade** — "Sem bodes expiatórios, sem crueldade como política, sem desumanização."

### Como funciona:

- Os usuários fazem login para falar com o Avatar da OSSIF, que segue os princípios da OSSIF em todas as interações.
- As conversas produzem um **comprovante estruturado**: alegações feitas, evidências fornecidas, incertezas identificadas, ações propostas (registro de voto, contato com seu representante, datas de reuniões comunitárias).
- Às vezes, o fundador (ou outros voluntários da OSSIF) estará ao vivo em vez da IA — conversas transmitidas sobre eventos atuais com pessoas fazendo seu check-in diário.
- O Avatar adapta seu estilo de comunicação ao usuário, mantendo princípios consistentes.

### Princípios de design:

- O Avatar nunca reivindica autoridade — ele faz perguntas e fornece estruturas.
- Todas as conversas são opcionalmente graváveis e exportáveis.
- O sistema deve parecer uma conversa com um amigo atencioso, não um interrogatório.

## Tokens de Confiança

Um token digital não monetário que representa o compromisso com os princípios da OSSIF. Não é uma criptomoeda no sentido financeiro — é um **sinal de reputação**.

### Conceito central:

- Cada entidade sapiente pode ganhar **um** Token de Confiança ao demonstrar compreensão e compromisso com os princípios da OSSIF.
- O token não tem valor monetário — seu valor vem inteiramente do capital social que representa.
- Possuir o token significa que você foi avaliado como "consciente" — você entende a estrutura e concordou com seus princípios.
- O token pode ser revogado por um comitê em caso de violações públicas e documentadas dos princípios centrais.
- A revogação inclui uma explicação clara e um caminho para a restauração.

### Decisões de design:

- **Um token, uma entidade, um voto** — sem acumulação, sem vantagem por riqueza.
- **Tokens de marcação (*placeholders*)** para entidades públicas (governos, corporações, figuras públicas) com status padrão baseado em ações públicas.
- **1 token = 1 voto** para direcionar as prioridades da OSSIF (advocacia, alcance, alocação de recursos).
- **API pública** para que qualquer pessoa possa verificar o status de qualquer entidade na OSSIF.
- **Blockchain com permissão** para o livro-razão — publicamente verificável, gerenciado por comitê para revogação.

### O que o token NÃO é:

- Não é uma moeda — não pode ser comprado, vendido ou trocado.
- Não é uma pontuação de crédito social — é binário (você tem ou não tem, com base em critérios transparentes).
- Não é um portão para serviços básicos — a participação na OSSIF não exige um token.

### Considerações:

- O processo de avaliação deve ser objetivo e testável, não subjetivo ou político.
- A privacidade deve ser protegida — o sistema verifica o compromisso, não vigia o comportamento.
- O componente de blockchain deve ser usado apenas se agregar valor genuíno em relação a alternativas mais simples.
- O sistema deve ser escalável para potencialmente bilhões de entidades (incluindo IAs sapientes).

## Camada de Comunidade e Governança

A infraestrutura democrática da OSSIF.

### Componentes:

**Estatuto de Princípios Públicos**
- Curto, concreto, passível de emendas.
- O documento que as pessoas realmente leem e assinam.
- Versão controlada com registros de alterações claros.

**Processo de Deliberação**
- Discussão estruturada com requisitos de evidência.
- Modelo de proposta: objetivo, evidência, danos/riscos, mitigação, custo, o que a invalidaria.
- Deliberação comunitária seguida de votação.
- Resultados publicados com permissão para relatórios de minoria.

**Sistema de Conflito e Moderação**
- Processo de apelação claro.
- Decisões registradas.
- Proteções contra o abuso do poder de moderação.

### Prevenindo a "captura pelo fundador":

A estrutura de governança é explicitamente projetada para que:
- O fundador não tenha autoridade especial permanente.
- Os princípios possam ser alterados por voto da comunidade.
- A liderança seja rotativa e eleita.
- Todas as decisões de governança sejam públicas e auditáveis.

## O Fundo de Ajuda Mútua (Renda Básica de Dignidade)

Um programa piloto de apoio material que demonstra os valores da OSSIF na prática.

### Design:

- **Contribuições opcionais** com níveis sugeridos (não "metade da sua renda" como regra).
- **Distribuição igualitária** entre todas as contas dos participantes, limitada a um teto razoável.
- **Elegibilidade clara, tetos e regras auditáveis**.
- **Nenhum acordo político exigido para receber ajuda** — desconectado de crenças.
- **Relatórios transparentes**: quanto foi coletado, quantos foram ajudados, quais foram os resultados.

### Alternativas de nomes (melhores que "UBI"):

- Renda Básica de Dignidade
- Dividendo de Estabilidade Cívica
- Dividendo de Participação
- Garantia de Piso Humano

### Princípio fundamental:

Separar "incentivos de participação" de "ajuda" — isso nunca deve se tornar um pagamento por crença.

## A Biblioteca de Registros Vivos

Um arquivo de acesso aberto de todas as interações, decisões e discussões da OSSIF.

### Propósito:

- **Aprendizado coletivo** — todos aprendem com as perguntas e o racínio uns dos outros.
- **Transparência** — mostra como as decisões foram alcançadas e como os princípios foram aplicados.
- **Melhoria contínua** — a análise de perguntas comuns e mal-entendidos alimenta The Primer.
- **Responsabilidade** — registro público das ações de governança.

### Implementação:

- Pesquisável por tópico, data e tipo.
- Licença aberta (Creative Commons) para todo o conteúdo.
- Acessível via interface web simples.
- Exportável para uso offline, pesquisa ou remixagem.

## Conta e Identidade OSSIF

### Requisitos:

- **ID Sapiente** — um identificador único que preserva a privacidade.
- **Baseado em SSO** com capacidade de transferência para outros sistemas de identidade.
- **Configuração de localização** até o nível da cidade para organização local.
- **Sem filtro de palavrões** nos nomes de exibição — liberdade de expressão na identidade.
- **Transparente e seguro** — baseado em blockchain se isso agregar valor genuíno, mais simples se não agregar.

## Princípios Técnicos

Em todos os sistemas:

- **Interfaces HTML simples** — rápidas, acessíveis, funcionam em qualquer dispositivo.
- **Sem dependências externas** onde for possível — funciona offline, funciona em hardware antigo.
- **Tudo em código aberto** — código, conteúdo, algoritmos, modelos de dados.
- **Privacidade por padrão** — minimização de dados, compartilhamento baseado em consentimento, armazenamento local primeiro.
- **Exportável** — qualquer coisa que um usuário crie ou com a qual interaja pode ser baixada como texto simples.
- **Acessível** — amigável para leitores de tela, modos de alto contraste, conversão de texto em fala, funções ARIA.

## Prioridade de Implementação

1. **Este repositório** — os documentos que você está lendo agora.
2. **Um site simples** — renderiza estes documentos com navegação limpa.
3. **O Portal Avatar** — mesmo que um chatbot básico que siga os princípios de conversação da OSSIF.
4. **Protótipo do The Primer** — uma versão adaptativa do kit de ferramentas de pensamento crítico.
5. **Ferramentas de governança** — infraestrutura de proposta/votação.
6. **Piloto do Token de Confiança** — prova de conceito em pequena escala.
7. **Piloto de Ajuda Mútua** — fundo minúsculo com tetos rígidos e transparência total.

Cada fase deve ser utilizável e valiosa por si só. Nenhuma fase depende da conclusão de todas as fases anteriores. Comece pequeno, entregue algo, itere.

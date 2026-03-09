# Governança

Este documento descreve como o OSSIF é governado de fato — não como ele aspira ser governado algum dia, mas quem detém o poder agora, como as decisões são tomadas e quais restrições existem. Se o mapa não coincide com o território, o mapa está errado.

## Estado Atual: Controlado pelo Fundador

Até o momento da elaboração deste documento, o OSSIF é controlado por uma única pessoa: **Josh Stephens** (GitHub: josh-stephens).

Josh controla:
- O repositório GitHub (autoridade de merge, proteção de branches, configurações)
- Os prompts e a arquitetura das sessões do conselho
- As diretrizes de contribuição
- A narrativa e o enquadramento de todos os documentos
- A decisão do que é publicado e do que não é

Isso não é oculto e não é permanente. Mas deve ser declarado abertamente, pois uma estrutura que afirma prevenir a concentração de poder enquanto concentra o poder em uma única pessoa tem um problema de credibilidade — mesmo que a concentração seja temporária e bem-intencionada.

## Processo de Tomada de Decisão

### Atual (pré-comunidade)

Enquanto o OSSIF não possui uma comunidade significativa além do fundador:
- O fundador toma todas as decisões
- O Conselho dos Sapientes Unidos fornece revisão adversarial
- As recomendações do conselho são rastreadas e seu status de implementação é público (veja abaixo)
- Todas as decisões são documentadas no histórico de commits do repositório

### Alvo (pós-comunidade)

Assim que uma comunidade existir:
- **Decisões ordinárias** (esclarecimentos, exemplos, manutenção): qualquer contribuidor pode enviar um PR, mesclado por qualquer mantenedor
- **Mudanças significativas** (novo conteúdo, nova redação): discussão de issue obrigatória, mesclada após feedback da comunidade
- **Mudanças fundamentais** (valores essenciais, estrutura de governança): proposta formal, 90 dias de deliberação, voto de supermaioria
- **Dissolução**: veja abaixo

## Rastreador de Recomendações do Conselho

O Conselho dos Sapientes Unidos existe para realizar testes de estresse no OSSIF. Suas recomendações não são vinculativas, mas ignorá-las sem explicação é uma falha estrutural. Este rastreador mantém a estrutura responsável.

| # | Recomendação | Sessão | Status | Resposta |
|---|---------------|---------|--------|----------|
| 1 | Construir um padrão de evidências aberto | 001 | **Em andamento** | Este doc de governança + falsifiability.md são os primeiros passos. Um documento formal de padrão de evidências é o próximo. |
| 2 | Projetar instituições com cláusulas de expiração | 001 | **Em andamento** | Revisão de expiração e critérios de dissolução adicionados abaixo. |
| 3 | Abordar o problema de classe (GitHub como barreira de acesso) | 001 | **Em andamento** | Mecanismo de contribuição via web incluído no roadmap.md — edição baseada em navegador sem necessidade de conta no GitHub. Cronograma de entrega de uma semana. |
| 4 | Tornar a humildade epistêmica estrutural, não aspiracional | 001 | **Em andamento** | falsifiability.md, este documento de governança e a reescrita dos "inegociáveis" em values.md são movimentos estruturais. |
| 5 | Garantir proteção absoluta à divergência | 002 | **Concluído** | CONTRIBUTING.md reescrito para proibir comportamentos de sabotagem, não conclusões divergentes. |
| 6 | Criar um registro de custos de valores | 002 | **Concluído** | Veja abaixo. |
| 7 | Estabelecer transparência de dependência estrutural | 002 | **Concluído** | Seção "Estado Atual" deste documento. |

## Restrições do Fundador

As seguintes restrições aplicam-se ao fundador imediatamente:

1. **Sem mudanças unilaterais nos Compromissos Fundamentais.** Os valores em values.md não podem ser alterados apenas pelo fundador assim que uma comunidade existir.
2. **Recomendações do conselho exigem uma resposta publicada.** Ignorar uma recomendação sem explicação é proibido. Discordar é aceitável; silêncio não é.
3. **Este documento de governança não pode ser enfraquecido apenas pelo fundador.** Qualquer alteração que reduza a responsabilidade, remova restrições ou concentre poder exige o mesmo processo de uma mudança fundamental.
4. **O fundador pode ser removido.** Se a comunidade atingir um tamanho onde transições de governança sejam possíveis (mais de 10 contribuidores ativos), um processo de destituição torna-se disponível: petição por um terço, votação por maioria simples.

### Execução Externa

Restrições autoimpostas valem exatamente o mesmo que a integridade da pessoa que as impôs. Para tornar essas restrições reais, os seguintes mecanismos de execução externa estão em vigor:

1. **Veto do conselho em mudanças fundamentais.** O Conselho dos Sapientes Unidos pode revisar qualquer mudança proposta para values.md, governance.md ou Compromissos Fundamentais. Se a maioria das cadeiras do conselho se opuser à mudança e publicar seu raciocínio, a mudança é bloqueada até que as objeções sejam tratadas por meio de um processo de deliberação pública. O fundador não pode anular um veto do conselho — o único caminho é a persuasão.

2. **Log de alterações público.** Cada modificação em governance.md, values.md, CONTRIBUTING.md e falsifiability.md é rastreada no git com histórico completo de diff. O conselho e a comunidade podem auditar qualquer mudança. Reverter uma restrição sem justificativa pública é, por si só, um gatilho de falsificabilidade.

3. **Sobreposição da comunidade por limite.** Uma vez que existam mais de 5 contribuidores ativos (definidos como: ter enviado pelo menos um PR mesclado ou issue substantiva nos últimos 6 meses), as mudanças de governança exigem um período de consulta pública de 30 dias e aprovação da maioria dos contribuidores ativos. O voto do fundador conta como um.

4. **Acesso imutável ao conselho.** A capacidade do conselho de avaliar o OSSIF não pode ser revogada ou restrita pelo fundador. Os prompts, procedimentos e relatórios das sessões do conselho são publicados em um repositório separado (josh-stephens/united-sapients) que o fundador não controla sozinho — as sessões do conselho podem ser iniciadas por qualquer membro da comunidade uma vez que o limite acima seja atingido.

Esses mecanismos são imperfeitos e evoluirão. Mas são restrições reais com consequências observáveis, não apenas aspirações.

## Revisão de Expiração

Cada decisão estrutural, posicionamento de política e mecanismo de governança passa por uma revisão obrigatória em um cronograma fixo:

- **Posicionamentos de política** (platform.md): revisados a cada 2 anos
- **Estruturas de governança**: revisadas a cada 3 anos
- **Compromissos Fundamentais**: revisados a cada 5 anos
- **Revisões conduzidas por**: membros não envolvidos na decisão original, mais pelo menos uma sessão do conselho

Uma revisão não significa que uma mudança seja obrigatória. Significa que uma mudança é *considerada*, com evidências, e a decisão de manter ou revisar é documentada.

## Critérios de Dissolução

O OSSIF deve deixar de existir se:

1. **A estrutura falhar em seus próprios testes de falsificabilidade** (veja [falsifiability.md](falsifiability.md)) e não puder ser revisada para corrigir as falhas
2. **As estruturas de governança forem capturadas** e os mecanismos de autocorreção falharem em restaurar a responsabilidade
3. **A estrutura causar dano líquido** — se evidências mostrarem que o OSSIF está aumentando o sofrimento, concentrando poder ou degradando o raciocínio em vez de melhorá-lo
4. **A comunidade votar pela dissolução** — por supermaioria, após um período de deliberação

Dissolução significa: o repositório é arquivado (não deletado), todos os documentos permanecem publicamente disponíveis sob sua licença Creative Commons e um relatório final documenta o que funcionou, o que não funcionou e o porquê.

Uma organização que não consegue descrever as condições de sua própria morte não é confiável. Esta seção existe para que o OSSIF possa morrer bem, se necessário.

## Registro de Custos de Valores

Um registro público, do tipo somente anexação (append-only), do que os valores do OSSIF realmente custaram. Valores que nunca foram caros nunca foram testados. Este registro rastreia os momentos em que manter um princípio exigiu sacrifício — não apenas palavras, mas algo real.

| Data | Valor Testado | O Que Custou | Quem Arcou com o Custo | Notas |
|------|-------------|-------------|-------------------|-------|
| 2026-03-07 | Autocorreção / Humildade epistêmica | Reconheceu publicamente que a pontuação 0 de 7 do conselho foi uma acusação válida, não um ataque injusto. Recreveu documentos fundamentais em resposta. | Fundador (ego, controle da narrativa) | A avaliação da sessão 003 do conselho foi dura e amplamente correta. Responder com mudanças estruturais em vez de prosa defensiva é a primeira entrada neste registro. |
| 2026-03-08 | Responsabilidade de poder / Proteção à divergência | Concedeu ao conselho autoridade de veto sobre mudanças fundamentais. Convidou forks contraditórios da plataforma. Ambos reduzem o controle do fundador. | Fundador (autoridade, palavra final) | O conselho perguntou se a resposta do fundador produziria mudanças estruturais ou apenas escrita adicional. Conceder poder de veto a um órgão externo é estrutural. Convidar pessoas a provarem que suas conclusões estão erradas é estrutural. Nenhum dos dois pode ser desfeito sem justificativa pública. |

Se este registro estiver vazio após um ano, o OSSIF deve reconhecer publicamente que seus valores não foram testados e, portanto, não podem ser reivindicados como princípios operacionais.

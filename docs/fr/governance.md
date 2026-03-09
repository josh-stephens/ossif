# Gouvernance

Ce document décrit la manière dont OSSIF est réellement gouverné — non pas la façon dont il aspire à l'être un jour, mais qui détient le pouvoir en ce moment même, comment les décisions sont prises et quelles contraintes existent. Si la carte ne correspond pas au terrain, c'est la carte qui a tort.

## État actuel : Contrôlé par le Fondateur

À l'heure où nous écrivons ces lignes, OSSIF est contrôlé par une seule personne : **Josh Stephens** (GitHub : josh-stephens).

Josh contrôle :
- Le dépôt GitHub (autorité de fusion, protection des branches, paramètres)
- Les **prompts** et l'architecture des sessions du conseil
- Les directives de contribution
- Le récit et le cadrage de tous les documents
- La décision de ce qui est publié ou non

Ceci n'est pas caché et n'est pas permanent. Mais cela doit être énoncé clairement, car un cadre qui prétend empêcher la concentration du pouvoir tout en concentrant le pouvoir entre les mains d'une seule personne a un problème de crédibilité — même si cette concentration est temporaire et animée de bonnes intentions.

## Processus de prise de décision

### Actuel (pré-communauté)

Tant qu'OSSIF n'a pas de communauté significative au-delà de son fondateur :
- Le fondateur prend toutes les décisions
- Le **Conseil des Sapients Unis** assure une révision contradictoire
- Les recommandations du conseil **font l'objet d'un suivi** et l'état de leur mise en œuvre est public (voir ci-dessous)
- Toutes les décisions sont documentées dans l'historique des commits du dépôt

### Cible (post-communauté)

Dès qu'une communauté existera :
- **Décisions ordinaires** (clarifications, exemples, maintenance) : tout contributeur peut soumettre une PR, fusionnée par n'importe quel mainteneur
- **Changements significatifs** (nouveau contenu, reformulation) : discussion de l'issue requise, fusion après avis de la communauté
- **Changements fondamentaux** (valeurs de base, structure de gouvernance) : proposition formelle, délibération de 90 jours, vote à la super-majorité
- **Dissolution** : voir ci-dessous

## Suivi des recommandations du Conseil

Le **Conseil des Sapients Unis** existe pour tester la résilience d'OSSIF. Ses recommandations ne sont pas contraignantes, mais les ignorer sans explication constitue un échec structurel. Ce suivi place le cadre face à ses responsabilités.

| # | Recommandation | Session | État | Réponse |
|---|---------------|---------|--------|----------|
| 1 | Élaborer une **norme probatoire** ouverte | 001 | **En cours** | Ce document de gouvernance + falsifiability.md sont les premières étapes. Un document formel de norme probatoire est la prochaine étape. |
| 2 | Concevoir des institutions avec des clauses de caducité | 001 | **En cours** | Critères de révision de caducité et de dissolution ajoutés ci-dessous. |
| 3 | Aborder le problème de classe (GitHub comme barrière d'accès) | 001 | **En cours** | Mécanisme de contribution Web **inscrit** dans roadmap.md — édition via navigateur sans compte GitHub requis. Délai de livraison d'une semaine. |
| 4 | Rendre l'humilité épistémique structurelle, et non aspirative | 001 | **En cours** | falsifiability.md, ce document de gouvernance et la réécriture des « non-négociables » dans values.md sont des mesures structurelles. |
| 5 | Assurer une protection absolue de la dissidence | 002 | **Terminé** | CONTRIBUTING.md réécrit pour interdire les comportements de sabotage, et non les conclusions dissidentes. |
| 6 | Créer un **journal des coûts des valeurs** | 002 | **Terminé** | Voir ci-dessous. |
| 7 | Établir la transparence des dépendances structurelles | 002 | **Terminé** | Section « État actuel » de ce document. |

## Contraintes du Fondateur

Les contraintes suivantes s'appliquent immédiatement au fondateur :

1. **Pas de changements unilatéraux aux Engagements Fondamentaux.** Les valeurs dans values.md ne peuvent pas être modifiées par le fondateur seul dès qu'une communauté existe.
2. **Les recommandations du conseil exigent une réponse publiée.** Il est interdit d'ignorer une recommandation sans explication. Le désaccord est acceptable ; le silence ne l'est pas.
3. **Ce document de gouvernance ne peut pas être affaibli par le fondateur seul.** Tout changement réduisant la responsabilité, supprimant des contraintes ou concentrant le pouvoir nécessite le même processus qu'un changement fondamental.
4. **Le fondateur peut être révoqué.** Si la communauté atteint une taille permettant des transitions de gouvernance (plus de 10 contributeurs actifs), une procédure de révocation devient disponible : pétition par un tiers, vote à la majorité simple.

### Application externe

Les contraintes auto-imposées ne valent que ce que vaut l'intégrité de la personne qui les a imposées. Pour rendre ces contraintes réelles, les mécanismes d'application externe suivants sont en vigueur :

1. **Veto du conseil sur les changements fondamentaux.** Le **Conseil des Sapients Unis** peut examiner tout changement proposé à values.md, governance.md ou aux **Engagements Fondamentaux**. Si une majorité des sièges du conseil s'oppose au changement et publie son raisonnement, le changement est bloqué jusqu'à ce que les objections soient traitées par un processus de délibération publique. Le fondateur ne peut pas passer outre un veto du conseil — la seule voie possible est la persuasion.

2. **Journal public des modifications.** Chaque modification de governance.md, values.md, CONTRIBUTING.md et falsifiability.md est suivie dans git avec un historique complet des diffs. Le conseil et la communauté peuvent auditer n'importe quel changement. Revenir sur une contrainte sans justification publique est en soi un déclencheur de falsifiabilité.

3. **Contrôle communautaire au seuil critique.** Une fois que 5 contributeurs actifs existent (définis comme ayant soumis au moins une PR fusionnée ou une issue substantielle au cours des 6 derniers mois), les changements de gouvernance nécessitent une période de consultation publique de 30 jours et l'approbation de la majorité des contributeurs actifs. Le vote du fondateur compte pour une voix.

4. **Accès immuable au conseil.** La capacité du conseil à évaluer OSSIF ne peut être révoquée ou restreinte par le fondateur. Les **prompts** de session du conseil, les délibérations et les rapports sont publiés dans un dépôt séparé (josh-stephens/united-sapients) que le fondateur ne contrôle pas seul — les sessions du conseil peuvent être initiées par n'importe quel membre de la communauté une fois le seuil ci-dessus atteint.

Ces mécanismes sont imparfaits et évolueront. Mais ce sont des contraintes réelles avec des conséquences observables, et non des aspirations.

## Révision de caducité

Chaque décision structurelle, position politique et mécanisme de gouvernance fait l'objet d'une révision obligatoire selon un calendrier fixe :

- **Positions politiques** (platform.md) : révisées tous les 2 ans
- **Structures de gouvernance** : révisées tous les 3 ans
- **Engagements Fondamentaux** : révisés tous les 5 ans
- **Révisions menées par** : des membres non impliqués dans la décision originale, plus au moins une session du conseil

Une révision ne signifie pas qu'un changement est obligatoire. Cela signifie qu'un changement est *envisagé*, avec des preuves à l'appui, et que la décision de maintenir ou de réviser est documentée.

## Critères de dissolution

OSSIF devrait cesser d'exister si :

1. **Le cadre échoue à ses propres tests de falsifiabilité** (voir [falsifiability.md](falsifiability.md)) et ne peut être révisé pour corriger ces échecs
2. **Les structures de gouvernance sont capturées** et les mécanismes d'autocorrection n'ont pas réussi à rétablir la responsabilité
3. **Le cadre cause un préjudice net** — si les preuves montrent qu'OSSIF augmente la souffrance, concentre le pouvoir ou dégrade le raisonnement plutôt que de l'améliorer
4. **La communauté vote la dissolution** — par une super-majorité, après une période de délibération

La dissolution signifie : le dépôt est archivé (pas supprimé), tous les documents restent publiquement disponibles sous leur licence Creative Commons, et un rapport final documente ce qui a fonctionné, ce qui n'a pas fonctionné et pourquoi.

On ne peut pas faire confiance à une organisation qui est incapable de décrire les conditions de sa propre fin. Cette section existe pour qu'OSSIF puisse mourir dignement s'il le faut.

## Journal des coûts des valeurs

Un registre public, en ajout uniquement, de ce que les valeurs d'OSSIF ont réellement coûté. Les valeurs qui n'ont jamais coûté cher n'ont jamais été testées. Ce journal suit les moments où le maintien d'un principe a exigé un sacrifice — pas seulement des mots, mais quelque chose de réel.

| Date | Valeur testée | Ce qu'elle a coûté | Qui en a supporté le coût | Notes |
|------|-------------|-------------|-------------------|-------|
| 2026-03-07 | Autocorrection / Humilité épistémique | Reconnaissance publique que le score de 0 sur 7 du conseil était un acte d'accusation valide, et non une attaque injuste. Réécriture des documents fondamentaux en réponse. | Fondateur (ego, contrôle narratif) | L'évaluation de la session 003 du conseil était sévère et largement correcte. Répondre par des changements structurels plutôt que par une prose défensive est la première entrée de ce journal. |
| 2026-03-08 | Responsabilité du pouvoir / Protection de la dissidence | Octroi au conseil d'un droit de veto sur les changements fondamentaux. Invitation à créer des forks contradictoires de la plateforme. Les deux réduisent le contrôle du fondateur. | Fondateur (autorité, dernier mot) | Le conseil a demandé si la réponse du fondateur produirait des changements structurels ou simplement des écrits supplémentaires. Accorder un pouvoir de veto à un organe externe est structurel. Inviter les gens à prouver que vos conclusions sont fausses est structurel. Aucun des deux ne peut être annulé sans justification publique. |

Si ce journal est vide après un an, OSSIF devra reconnaître publiquement que ses valeurs n'ont pas été testées et ne peuvent donc pas être revendiquées comme des principes opérationnels.

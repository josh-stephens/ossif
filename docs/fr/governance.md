# Gouvernance

Ce document décrit la manière dont OSSIF est réellement gouverné — non pas la manière dont il aspire à être gouverné un jour, mais qui détient le pouvoir en ce moment, comment les décisions sont prises et quelles contraintes existent. Si la carte ne correspond pas au terrain, c'est la carte qui a tort.

## État actuel : Contrôlé par le fondateur

À l'heure où nous écrivons ces lignes, OSSIF est contrôlé par une seule personne : **Josh Stephens** (GitHub : josh-stephens).

Josh contrôle :
- Le dépôt GitHub (autorité de fusion, protection des branches, paramètres)
- Les prompts et l'architecture des sessions du conseil
- Les directives de contribution
- La narration et le cadrage de tous les documents
- La décision de ce qui est publié et de ce qui ne l'est pas

Ce n'est pas caché, et ce n'est pas permanent. Mais cela doit être énoncé clairement, car un cadre qui prétend empêcher la concentration du pouvoir tout en concentrant le pouvoir en une seule personne a un problème de crédibilité — même si cette concentration est temporaire et animée de bonnes intentions.

## Processus de prise de décision

### Actuel (avant la communauté)

Tant qu'OSSIF n'a pas de communauté significative au-delà de son fondateur :
- Le fondateur prend toutes les décisions.
- Le Conseil des Sapients Unis fournit un examen contradictoire.
- Les recommandations du conseil font l'objet d'un suivi et l'état de leur mise en œuvre est public (voir ci-dessous).
- Toutes les décisions sont documentées dans l'historique des commits du dépôt.

### Cible (après la communauté)

Une fois qu'une communauté existera :
- **Décisions ordinaires** (clarifications, exemples, maintenance) : tout contributeur peut soumettre une PR, fusionnée par n'importe quel mainteneur.
- **Changements significatifs** (nouveau contenu, reformulation) : discussion de l'issue requise, fusion après consultation de la communauté.
- **Changements fondamentaux** (valeurs centrales, structure de gouvernance) : proposition formelle, délibération de 90 jours, vote à la majorité qualifiée.
- **Dissolution** : voir ci-dessous.

## Suivi des recommandations du Conseil

Le Conseil des Sapients Unis existe pour mettre OSSIF à l'épreuve. Ses recommandations ne sont pas contraignantes, mais les ignorer sans explication constitue un échec structurel. Ce suivi permet de responsabiliser le cadre.

| # | Recommandation | Session | État | Réponse |
|---|---------------|---------|--------|----------|
| 1 | Établir un standard probatoire ouvert | 001 | **En cours** | Ce document de gouvernance + [falsifiability.md](falsifiability.md) sont les premières étapes. Un document formel définissant ce standard est la prochaine étape. |
| 2 | Concevoir des institutions avec des clauses de caducité | 001 | **En cours** | Révision de caducité et critères de dissolution ajoutés ci-dessous. |
| 3 | Aborder le problème de classe (GitHub comme barrière d'accès) | 001 | **Non commencé** | Reconnu. Nécessite un chemin de participation hors GitHub. |
| 4 | Rendre l'humilité épistémique structurelle et non aspirative | 001 | **En cours** | [falsifiability.md](falsifiability.md), ce document de gouvernance et la réécriture des « non-négociables » dans [values.md](values.md) sont des mesures structurelles. |
| 5 | Garantir une protection absolue de la dissidence | 002 | **Terminé** | CONTRIBUTING.md réécrit pour interdire les comportements de sabotage, et non les conclusions dissidentes. |
| 6 | Créer un journal des coûts des valeurs | 002 | **Terminé** | Voir ci-dessous. |
| 7 | Établir la transparence des dépendances structurelles | 002 | **Terminé** | Section « État actuel » de ce document. |

## Contraintes imposées au fondateur

Les contraintes suivantes s'appliquent immédiatement au fondateur :

1. **Pas de changements unilatéraux aux Engagements Fondamentaux.** Les valeurs dans [values.md](values.md) ne peuvent pas être modifiées par le seul fondateur une fois qu'une communauté existe.
2. **Les recommandations du Conseil exigent une réponse publiée.** Ignorer une recommandation sans explication est interdit. Le désaccord est acceptable ; le silence ne l'est pas.
3. **Ce document de gouvernance ne peut être affaibli par le seul fondateur.** Tout changement réduisant la responsabilité, supprimant des contraintes ou concentrant le pouvoir nécessite le même processus qu'un changement fondamental.
4. **Le fondateur peut être démis de ses fonctions.** Si la communauté atteint une taille permettant des transitions de gouvernance (plus de 10 contributeurs actifs), un processus de révocation devient possible : pétition d'un tiers, vote à la majorité simple.

Ces contraintes sont actuellement auto-imposées, ce qui signifie qu'elles reposent sur l'intégrité du fondateur. C'est une faiblesse honnête. L'objectif est d'évoluer vers une application externe à mesure que la communauté grandit.

## Révision de caducité

Chaque décision structurelle, position politique et mécanisme de gouvernance fait l'objet d'une révision obligatoire selon un calendrier fixe :

- **Positions de politique générale** ([platform.md](platform.md)) : révisées tous les 2 ans.
- **Structures de gouvernance** : révisées tous les 3 ans.
- **Engagements Fondamentaux** : révisés tous les 5 ans.
- **Révisions menées par** : des membres non impliqués dans la décision originale, plus au moins une session du conseil.

Une révision ne signifie pas qu'un changement est obligatoire. Cela signifie qu'un changement est *envisagé*, avec des preuves à l'appui, et que la décision de maintenir ou de réviser est documentée.

## Critères de dissolution

OSSIF devrait cesser d'exister si :

1. **Le cadre échoue à ses propres tests de falsifiabilité** (voir [falsifiability.md](falsifiability.md)) et ne peut être révisé pour corriger ces échecs.
2. **Les structures de gouvernance sont captées** et les mécanismes d'auto-correction ont échoué à rétablir la responsabilité.
3. **Le cadre cause un préjudice net** — si les preuves montrent qu'OSSIF augmente la souffrance, concentre le pouvoir ou dégrade le raisonnement au lieu de l'améliorer.
4. **La communauté vote la dissolution** — à la majorité qualifiée, après une période de délibération.

La dissolution signifie : le dépôt est archivé (pas supprimé), tous les documents restent publiquement disponibles sous leur licence Creative Commons, et un rapport final documente ce qui a fonctionné, ce qui n'a pas fonctionné et pourquoi.

Une organisation qui ne peut décrire les conditions de sa propre mort ne mérite pas la confiance. Cette section existe pour qu'OSSIF puisse mourir dignement si nécessaire.

## Journal des coûts des valeurs

Un enregistrement public, à ajout exclusif, de ce que les valeurs d'OSSIF ont réellement coûté. Les valeurs qui n'ont jamais été coûteuses n'ont jamais été testées. Ce journal suit les moments où le respect d'un principe a exigé un sacrifice — pas seulement des mots, mais quelque chose de réel.

| Date | Valeur testée | Ce qu'elle a coûté | Qui en a porté le coût | Notes |
|------|-------------|-------------|-------------------|-------|
| 2026-03-07 | Auto-correction / Humilité épistémique | A reconnu publiquement que le score de 0 sur 7 du conseil était un acte d'accusation valide, et non une attaque injuste. Réécriture des documents fondamentaux en réponse. | Fondateur (ego, contrôle de la narration) | L'évaluation de la session 003 du conseil a été sévère et largement correcte. Répondre par des changements structurels plutôt que par une prose défensive est la première entrée de ce journal. |

Si ce journal est vide après un an, OSSIF devra reconnaître publiquement que ses valeurs n'ont pas été testées et ne peuvent donc pas être revendiquées comme principes opérationnels.

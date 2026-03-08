# Gouvernance

Ce document décrit la manière dont l'OSSIF est réellement gouverné — non pas comme il aspire à l'être un jour, mais qui détient le pouvoir actuellement, comment les décisions sont prises et quelles contraintes existent. Si la carte ne correspond pas au territoire, c'est la carte qui a tort.

## État actuel : Contrôlé par le Fondateur

Au moment de la rédaction de ce document, l'OSSIF est contrôlé par une seule personne : **Josh Stephens** (GitHub : josh-stephens).

Josh contrôle :
- Le dépôt GitHub (autorité de fusion, protection des branches, paramètres)
- Les invites des sessions du conseil et l'architecture
- Les directives de contribution
- Le récit et le cadrage de tous les documents
- La décision de ce qui est publié ou non

Ceci n'est pas caché et n'est pas permanent. Mais cela doit être énoncé clairement, car un cadre qui prétend empêcher la concentration du pouvoir tout en le concentrant entre les mains d'une seule personne a un problème de crédibilité — même si cette concentration est temporaire et part de bonnes intentions.

## Processus de Prise de Décision

### Actuel (avant la communauté)

Tant que l'OSSIF n'a pas de communauté significative au-delà de son fondateur :
- Le fondateur prend toutes les décisions.
- Le Conseil des Sapients Unis fournit une révision contradictoire.
- Les recommandations du conseil font l'objet d'un suivi et l'état de leur mise en œuvre est public (voir ci-dessous).
- Toutes les décisions sont documentées dans l'historique des commits du dépôt.

### Cible (après la communauté)

Une fois qu'une communauté existera :
- **Décisions ordinaires** (clarifications, exemples, maintenance) : tout contributeur peut soumettre une PR, fusionnée par n'importe quel mainteneur.
- **Changements significatifs** (nouveau contenu, remaniement rédactionnel) : discussion sur un "issue" requise, fusion après consultation de la communauté.
- **Changements fondamentaux** (Engagements Fondamentaux, structure de gouvernance) : proposition formelle, délibération de 90 jours, vote à la majorité qualifiée.
- **Dissolution** : voir ci-dessous.

## Suivi des Recommandations du Conseil

Le Conseil des Sapients Unis existe pour tester la résistance de l'OSSIF. Ses recommandations ne sont pas contraignantes, mais les ignorer sans explication constitue un échec structurel. Ce suivi responsabilise le cadre.

| # | Recommandation | Session | État | Réponse |
|---|---------------|---------|--------|----------|
| 1 | Établir une norme de preuve ouverte | 001 | **En cours** | Ce document de gouvernance + falsifiability.md sont les premières étapes. Un document formel sur les normes de preuve est la prochaine étape. |
| 2 | Concevoir des institutions avec des clauses de caducité (sunset clause) | 001 | **En cours** | Critères de révision périodique et de caducité ajoutés ci-dessous. |
| 3 | Aborder le problème de classe (GitHub comme barrière d'accès) | 001 | **Non commencé** | Reconnu. Nécessite une voie de participation hors GitHub. |
| 4 | Rendre l'humilité épistémique structurelle et non aspirationnelle | 001 | **En cours** | falsifiability.md, ce document de gouvernance et la réécriture des « non-négociables » dans values.md sont des mesures structurelles. |
| 5 | Garantir une protection absolue de la dissidence | 002 | **Terminé** | CONTRIBUTING.md a été réécrit pour interdire les comportements de sabotage, et non les conclusions dissidentes. |
| 6 | Créer un journal des coûts des valeurs | 002 | **Terminé** | Voir ci-dessous. |
| 7 | Établir la transparence de la dépendance structurelle | 002 | **Terminé** | Section « État actuel » de ce document. |

## Contraintes du Fondateur

Les contraintes suivantes s'appliquent immédiatement au fondateur :

1. **Pas de changements unilatéraux aux Engagements Fondamentaux.** Les valeurs dans values.md ne peuvent pas être modifiées par le seul fondateur une fois qu'une communauté existe.
2. **Les recommandations du conseil exigent une réponse publiée.** Il est interdit d'ignorer une recommandation sans explication. Le désaccord est acceptable ; le silence ne l'est pas.
3. **Ce document de gouvernance ne peut pas être affaibli par le seul fondateur.** Tout changement réduisant la responsabilité, supprimant des contraintes ou concentrant le pouvoir nécessite le même processus qu'un changement fondamental.
4. **Le fondateur peut être destitué.** Si la communauté atteint une taille permettant des transitions de gouvernance (plus de 10 contributeurs actifs), un processus de révocation devient disponible : pétition par un tiers, vote à la majorité simple.

Ces contraintes sont actuellement auto-imposées, ce qui signifie qu'elles reposent sur l'intégrité du fondateur. C'est une faiblesse honnête. L'objectif est d'évoluer vers une application externe à mesure que la communauté grandit.

## Clauses de caducité et révision périodique

Chaque décision structurelle, position politique et mécanisme de gouvernance fait l'objet d'une révision obligatoire selon un calendrier fixe (clauses de caducité) :

- **Positions politiques** (platform.md) : révisées tous les 2 ans.
- **Structures de gouvernance** : révisées tous les 3 ans.
- **Engagements Fondamentaux** : révisés tous les 5 ans.
- **Révisions effectuées par** : des membres non impliqués dans la décision originale, plus au moins une session du conseil.

Une révision ne signifie pas qu'un changement est obligatoire. Cela signifie qu'un changement est *envisagé*, avec des preuves, et que la décision de maintenir ou de réviser est documentée.

## Critères de Dissolution

L'OSSIF devrait cesser d'exister si :

1. **Le cadre échoue à ses propres tests de falsifiabilité** (voir [falsifiability.md](falsifiability.md)) et ne peut être révisé pour remédier aux échecs.
2. **Les structures de gouvernance sont capturées** et les mécanismes d'auto-correction n'ont pas réussi à rétablir la responsabilité.
3. **Le cadre cause un préjudice net** — si des preuves montrent que l'OSSIF augmente la souffrance, concentre le pouvoir ou dégrade le raisonnement au lieu de l'améliorer.
4. **La communauté vote la dissolution** — à la majorité qualifiée, après une période de délibération.

La dissolution signifie : le dépôt est archivé (et non supprimé), tous les documents restent publiquement disponibles sous leur licence Creative Commons, et un rapport final documente ce qui a fonctionné, ce qui n'a pas fonctionné et pourquoi.

Une organisation incapable de décrire les conditions de sa propre mort ne peut être digne de confiance. Cette section existe pour que l'OSSIF puisse mourir dignement s'il le faut.

## Journal des coûts des valeurs

Un registre public, en ajout uniquement, de ce que les valeurs de l'OSSIF ont réellement coûté. Des valeurs qui n'ont jamais coûté cher n'ont jamais été testées. Ce journal suit les moments où le maintien d'un principe a nécessité un sacrifice — pas seulement des mots, mais quelque chose de concret.

| Date | Valeur Testée | Ce que cela a coûté | Qui a supporté le coût | Notes |
|------|-------------|-------------|-------------------|-------|
| 2026-03-07 | Auto-correction / Humilité épistémique | Reconnaissance publique que le score de 0 sur 7 du conseil était un acte d'accusation valide et non une attaque injuste. Réécriture des documents fondamentaux en réponse. | Fondateur (ego, contrôle du récit) | L'évaluation de la session 003 du conseil était sévère et largement correcte. Répondre par des changements structurels plutôt que par une prose défensive est la première entrée de ce journal. |

Si ce journal est vide après un an, l'OSSIF devra reconnaître publiquement que ses valeurs n'ont pas été testées et ne peuvent donc pas être revendiquées comme principes opérationnels.

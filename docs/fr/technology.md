# Technologie

La technologie de l'OSSIF sert sa mission — elle n'est pas la mission elle-même. Si un outil plus simple fonctionne, utilisez l'outil le plus simple. Les conceptions ci-dessous représentent l'architecture finale ; l'implémentation doit être incrémentale et pragmatique.

## Portail de Conversation Avatar

La « porte d'entrée » de l'OSSIF. Un lieu où n'importe qui peut entamer un dialogue structuré sur l'actualité, les politiques publiques et l'engagement civique.

### Ce qu'il fait :

L'Avatar n'est pas une autorité. C'est un **modérateur, un coach et un vulgarisateur**. Il remplit quatre fonctions essentielles :

1. **Clarifier les affirmations** — « Qu'affirmons-nous ? Séparons les affirmations factuelles des opinions. »
2. **Demander des preuves** — « Qu'est-ce qui vous ferait changer d'avis à ce sujet ? »
3. **Mettre en lumière les compromis** — « Qui en bénéficie ? Qui paie ? Quels sont les risques ? »
4. **Agir avec humanité** — « Pas de boucs émissaires, pas de cruauté érigée en politique, pas de déshumanisation. »

### Comment ça fonctionne :

- Les utilisateurs se connectent pour parler à l'Avatar OSSIF, qui suit les principes de l'OSSIF dans toutes les interactions.
- Les conversations produisent un **reçu structuré** : affirmations faites, preuves fournies, incertitudes identifiées, actions proposées (inscription sur les listes électorales, contacter votre représentant, dates de réunions communautaires).
- Parfois, le fondateur (ou d'autres bénévoles de l'OSSIF) sera en direct à la place de l'IA — des conversations diffusées sur l'actualité avec des personnes effectuant leur suivi quotidien.
- L'Avatar adapte son style de communication à l'utilisateur tout en maintenant des principes constants.

### Principes de conception :

- L'Avatar ne revendique jamais d'autorité — il pose des questions et fournit des cadres de réflexion.
- Toutes les conversations peuvent être enregistrées et exportées en option.
- Le système doit donner l'impression de parler à un ami réfléchi, et non à un interrogateur.

## Jetons de Confiance

Un jeton numérique non monétaire qui représente l'engagement envers les principes de l'OSSIF. Ce n'est pas une crypto-monnaie au sens financier — c'est un **signal de réputation**.

### Concept central :

- Chaque entité sapiente peut obtenir **un** Jeton de Confiance en démontrant sa compréhension et son engagement envers les principes de l'OSSIF.
- Le jeton n'a aucune valeur monétaire — sa valeur provient entièrement du capital social qu'il représente.
- Posséder le jeton signifie que vous avez été évalué comme **« cognizant »** — vous comprenez le cadre, maîtrisez ses outils et avez accepté ses principes.
- Le jeton peut être révoqué par un comité en cas de violations publiques et documentées des Engagements Fondamentaux.
- La révocation inclut une explication claire et un chemin vers la restauration.

### Décisions de conception :

- **Un jeton, une entité, un vote** — pas d'accumulation, pas d'avantage lié à la richesse.
- **Jetons de substitution** (placeholders) pour les entités publiques (gouvernements, entreprises, personnalités publiques) avec un statut par défaut basé sur les actions publiques.
- **1 jeton = 1 vote** pour orienter les priorités de l'OSSIF (plaidoyer, rayonnement, allocation des ressources).
- **API publique** pour que n'importe qui puisse vérifier le statut OSSIF de n'importe quelle entité.
- **Blockchain avec permissions** pour le registre — vérifiable publiquement, gérée par un comité pour les révocations.

### Ce que le jeton n'est PAS :

- **Pas une monnaie** — il ne peut être ni acheté, ni vendu, ni échangé.
- **Pas un score de crédit social** — c'est binaire (vous l'avez ou vous ne l'avez pas, sur la base de critères transparents et de l'adhésion aux principes).
- **Pas une barrière aux services de base** — la participation à l'OSSIF ne nécessite pas de jeton.

### Considérations :

- Le processus d'évaluation doit être objectif et testable, et non subjectif ou partisan.
- La vie privée doit être protégée — le système vérifie l'engagement, il ne surveille pas les comportements.
- Le composant blockchain ne doit être utilisé que s'il apporte une réelle valeur ajoutée par rapport à des alternatives plus simples.
- Le système doit pouvoir s'adapter à potentiellement des milliards d'entités (y compris les IA sapientes).

## Couche de Communauté et de Gouvernance

L'infrastructure démocratique de l'OSSIF.

### Composants :

**Charte Publique des Principes**
- Courte, concrète, amendable.
- Le document que les gens lisent et signent réellement.
- Contrôlée par version avec des journaux de modifications (changelogs) clairs.

**Processus de Délibération**
- Discussion structurée avec des exigences en matière de preuves.
- Modèle de proposition : objectif, preuves, préjudices/risques, atténuation, coût, critères d'infirmation (ce qui prouverait que l'idée est mauvaise).
- Délibération communautaire suivie d'un vote.
- Résultats publiés avec rapports minoritaires autorisés.

**Système de Conflits et de Modération**
- Processus d'appel clair.
- Décisions consignées.
- Garde-fous contre l'abus du pouvoir de modération.

### Empêcher la « capture par le fondateur » :

La structure de gouvernance est explicitement conçue de manière à ce que :
- Le fondateur n'ait aucune autorité spéciale permanente.
- Les principes puissent être modifiés par un vote de la communauté.
- Le leadership soit tournant et élu.
- Toutes les décisions de gouvernance soient publiques et auditables.

## Le Fonds d'Entraide (Revenu de Dignité de Base)

Un programme pilote de soutien matériel qui démontre les valeurs de l'OSSIF en pratique.

### Conception :

- **Contributions volontaires** avec des paliers suggérés (pas de règle rigide sur le pourcentage du revenu).
- **Distribution égale** sur tous les comptes des participants, avec un plafond raisonnable.
- **Éligibilité, plafonds et règles auditables clairs.**
- **Aucun accord politique requis pour recevoir de l'aide** — déconnecté des convictions personnelles.
- **Rapports transparents** : montants collectés, nombre de personnes aidées, résultats obtenus.

### Alternatives de dénomination :

- Revenu de Dignité de Base
- Dividende de Stabilité Civique
- Dividende de Participation
- Garantie de Plancher Humain

### Principe clé :

Séparer les « incitations à la participation » de l'« aide » — cela ne doit jamais devenir un paiement en échange d'une croyance ou d'une allégeance.

## La Bibliothèque d'Archives Vivantes

Une archive en libre accès de toutes les interactions, décisions et discussions de l'OSSIF.

### Objectif :

- **Apprentissage collectif** — tout le monde apprend des questions et des raisonnements des autres.
- **Transparence** — montre comment les décisions ont été prises, comment les principes ont été appliqués.
- **Amélioration continue** — l'analyse des questions courantes et des malentendus alimente The Primer.
- **Responsabilité** — registre public des actions de gouvernance.

### Implémentation :

- Consultable par sujet, date et type.
- Licence libre (Creative Commons) pour tout le contenu.
- Accessible via une interface web simple.
- Exportable pour une utilisation hors ligne, la recherche ou le remixage.

## Compte et Identité OSSIF

### Exigences :

- **ID Sapient** — un identifiant unique préservant la vie privée.
- **Basé sur le SSO** avec la possibilité de transfert vers d'autres systèmes d'identité.
- **Paramètre de localisation** jusqu'au niveau de la ville pour l'organisation locale.
- **Pas de filtre de grossièretés** sur les noms d'affichage — liberté d'expression dans l'identité.
- **Transparent et sûr** — basé sur la blockchain si cela apporte une valeur réelle, plus simple sinon.

## Principes Techniques

À travers tous les systèmes :

- **Interfaces HTML simples** — rapides, accessibles, fonctionnent sur n'importe quel appareil.
- **Pas de dépendances externes** dans la mesure du possible — fonctionne hors ligne, fonctionne sur du vieux matériel.
- **Tout en open source** — code, contenu, algorithmes, modèles de données.
- **Confidentialité par défaut** — minimisation des données, partage basé sur le consentement, stockage local prioritaire.
- **Exportable** — tout ce qu'un utilisateur crée ou avec quoi il interagit peut être téléchargé en texte brut.
- **Accessible** — compatible avec les lecteurs d'écran, modes à haut contraste, synthèse vocale, rôles ARIA.

## Priorité d'Implémentation

1. **Ce dépôt** — les documents que vous lisez actuellement.
2. **Un site web simple** — affiche ces documents avec une navigation claire.
3. **Le Portail Avatar** — même un chatbot basique qui suit les principes de conversation de l'OSSIF.
4. **Le prototype de The Primer** — une version adaptative de la boîte à outils de pensée critique.
5. **Outils de gouvernance** — infrastructure de proposition et de vote.
6. **Pilote du Jeton de Confiance** — preuve de concept à petite échelle.
7. **Pilote d'Entraide** — petit fonds avec des plafonds stricts et une transparence totale.

Chaque phase doit être utilisable et précieuse en soi. Aucune phase ne dépend de l'achèvement de toutes les phases précédentes. Commencez petit, livrez quelque chose, itérez.

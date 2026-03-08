# Technologie

La technologie d'OSSIF est au service de sa mission — elle n'est pas la mission en soi. Si un outil plus simple fonctionne, utilisez l'outil le plus simple. Les conceptions ci-dessous représentent l'architecture finale ; l'implémentation doit être incrémentale et pragmatique.

## Portail de Conversation Avatar

La « porte d'entrée » d'OSSIF. Un lieu où n'importe qui peut s'engager dans un dialogue structuré sur les événements actuels, les politiques et l'engagement civique.

### Ce qu'il fait :

L'Avatar n'est pas une autorité. C'est un **modérateur, un coach et un vulgarisateur**. Il fait quatre choses bien :

1. **Clarifier les affirmations** — « Qu'affirmons-nous ? Séparons les affirmations factuelles des opinions. »
2. **Demander des preuves** — « Qu'est-ce qui vous ferait changer d'avis à ce sujet ? »
3. **Faire émerger les compromis** — « Qui en bénéficie ? Qui paie ? Quels sont les risques ? »
4. **Faire preuve d'humanité** — « Pas de boucs émissaires, pas de cruauté érigée en politique, pas de déshumanisation. »

### Fonctionnement :

- Les utilisateurs se connectent pour parler à l'Avatar OSSIF, qui suit les principes d'OSSIF dans toutes les interactions.
- Les conversations produisent un **reçu structuré** : affirmations faites, preuves fournies, incertitudes identifiées, actions proposées (inscription sur les listes électorales, contact avec votre représentant, dates de réunions communautaires).
- Parfois, le fondateur (ou d'autres bénévoles d'OSSIF) sera en direct à la place de l'IA — des conversations diffusées sur les événements actuels avec des personnes effectuant leur suivi quotidien.
- L'Avatar adapte son style de communication à l'utilisateur tout en maintenant des principes cohérents.

### Principes de conception :

- L'Avatar ne revendique jamais d'autorité — il pose des questions et fournit des cadres.
- Toutes les conversations sont enregistrables et exportables en option.
- Le système doit donner l'impression de parler à un ami réfléchi, pas à un interrogatoire.

## Jetons de Confiance

Un jeton numérique non monétaire qui représente l'engagement envers les principes d'OSSIF. Ce n'est pas une cryptomonnaie au sens financier — c'est un **signal de réputation**.

### Concept de base :

- Chaque entité sapiente peut gagner **un** Jeton de Confiance en démontrant sa compréhension et son engagement envers les principes d'OSSIF.
- Le jeton n'a aucune valeur monétaire — sa valeur provient entièrement du capital social qu'il représente.
- Posséder le jeton signifie que vous avez été évalué comme « conscient » — vous comprenez le cadre et avez accepté ses principes.
- Le jeton peut être révoqué par un comité pour des violations publiques et documentées des principes fondamentaux.
- La révocation comprend une explication claire et un chemin vers la restauration.

### Décisions de conception :

- **Un jeton, une entité, un vote** — pas d'accumulation, pas d'avantage lié à la richesse.
- **Jetons réservés** pour les entités publiques (gouvernements, entreprises, personnalités publiques) avec un statut par défaut basé sur les actions publiques.
- **1 jeton = 1 vote** pour orienter les priorités d'OSSIF (plaidoyer, sensibilisation, allocation des ressources).
- **API publique** pour que quiconque puisse vérifier le statut OSSIF de n'importe quelle entité.
- **Blockchain avec permissions** pour le registre — vérifiable publiquement, gérée par un comité pour les révocations.

### Ce que le jeton n'est PAS :

- **Pas une monnaie** — il ne peut être acheté, vendu ou échangé.
- **Pas un score de crédit social** — c'est binaire (vous l'avez ou vous ne l'avez pas, sur la base de critères transparents).
- **Pas une barrière d'accès aux services de base** — la participation à OSSIF ne nécessite pas de jeton.

### Considérations :

- Le processus d'évaluation doit être objectif et testable, non subjectif ou politique.
- La vie privée doit être protégée — le système vérifie l'engagement, il ne surveille pas le comportement.
- Le composant blockchain ne doit être utilisé que s'il apporte une réelle valeur ajoutée par rapport à des alternatives plus simples.
- Le système doit pouvoir s'adapter potentiellement à des milliards d'entités (y compris l'IA sapiente).

## Couche de Communauté et de Gouvernance

L'infrastructure démocratique d'OSSIF.

### Composants :

**Charte des Principes Publics**
- Courte, concrète, amendable.
- Le document que les gens lisent et signent réellement.
- Sous contrôle de version avec des journaux de modifications clairs.

**Processus de délibération**
- Discussion structurée avec exigences de preuves.
- Modèle de proposition : objectif, preuves, préjudices/risques, atténuation, coût, ce qui l'infirmerait.
- Délibération communautaire suivie d'un vote.
- Résultats publiés avec rapports minoritaires autorisés.

**Système de gestion des conflits et de modération**
- Processus d'appel clair.
- Décisions consignées.
- Garde-fous contre l'abus de pouvoir de modération.

### Prévenir la « capture par le fondateur » :

La structure de gouvernance est explicitement conçue pour que :
- Le fondateur n'ait aucune autorité spéciale permanente.
- Les principes puissent être amendés par vote de la communauté.
- Le leadership soit tournant et élu.
- Toutes les décisions de gouvernance soient publiques et auditables.

## Le Fonds d'Entraide (Revenu de Dignité de Base)

Un programme pilote de soutien matériel qui démontre les valeurs d'OSSIF en pratique.

### Conception :

- **Contributions volontaires** avec des paliers suggérés (pas de règle type « la moitié de votre revenu »).
- **Distribution égale** sur tous les comptes des participants, avec un plafond raisonnable.
- **Éligibilité claire, plafonds et règles auditables**.
- **Aucun accord politique requis pour recevoir de l'aide** — déconnecté des convictions.
- **Rapports transparents** : montants collectés, nombre de personnes aidées, résultats obtenus.

### Alternatives de nommage (mieux que « UBI ») :

- Revenu de Dignité de Base
- Dividende de Stabilité Civique
- Dividende de Participation
- Garantie de Plancher Humain

### Principe clé :

Séparer les « incitations à la participation » de « l'aide » — cela ne doit jamais devenir un paiement contre des convictions.

## La Bibliothèque d'Archives Vivantes

Une archive en libre accès de toutes les interactions, décisions et discussions d'OSSIF.

### Objectif :

- **Apprentissage collectif** — tout le monde apprend des questions et des raisonnements des autres.
- **Transparence** — montre comment les décisions ont été prises, comment les principes ont été appliqués.
- **Amélioration continue** — l'analyse des questions courantes et des malentendus alimente The Primer.
- **Responsabilité** — registre public des actions de gouvernance.

### Implémentation :

- Recherchable par sujet, date et type.
- Licence ouverte (Creative Commons) pour tout le contenu.
- Accessible via une interface web simple.
- Exportable pour une utilisation hors ligne, la recherche ou le remixage.

## Compte et Identité OSSIF

### Exigences :

- **ID Sapient** — un identifiant unique respectant la vie privée.
- **Basé sur le SSO** avec possibilité de transfert vers d'autres systèmes d'identité.
- **Paramètre de localisation** jusqu'au niveau de la ville pour l'organisation locale.
- **Pas de filtre de grossièretés** sur les noms d'affichage — liberté d'expression dans l'identité.
- **Transparent et sûr** — basé sur la blockchain si cela apporte une valeur réelle, plus simple sinon.

## Principes Techniques

À travers tous les systèmes :

- **Interfaces HTML simples** — rapides, accessibles, fonctionnent sur n'importe quel appareil.
- **Aucune dépendance externe** dans la mesure du possible — fonctionne hors ligne, fonctionne sur du vieux matériel.
- **Tout en open source** — code, contenu, algorithmes, modèles de données.
- **Confidentialité par défaut** — minimisation des données, partage basé sur le consentement, stockage local prioritaire.
- **Exportable** — tout ce qu'un utilisateur crée ou avec lequel il interagit peut être téléchargé en texte brut.
- **Accessible** — compatible avec les lecteurs d'écran, modes à haut contraste, synthèse vocale, rôles ARIA.

## Priorité de l'Implémentation

1. **Ce dépôt** — les documents que vous lisez actuellement.
2. **Un site web simple** — affiche ces documents avec une navigation claire.
3. **Le Portail de Conversation Avatar** — même un chatbot de base qui suit les principes de conversation d'OSSIF.
4. **Le prototype de The Primer** — une version adaptative de la boîte à outils de pensée critique.
5. **Outils de gouvernance** — infrastructure de proposition/vote.
6. **Pilote du Jeton de Confiance** — preuve de concept à petite échelle.
7. **Pilote de l'Entraide** — fonds minuscule avec des plafonds stricts et une transparence totale.

Chaque phase doit être utilisable et précieuse en soi. Aucune phase ne dépend de l'achèvement de toutes les phases précédentes. Commencez petit, lancez quelque chose, itérez.

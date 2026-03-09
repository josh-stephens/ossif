# Technologie

La technologie d'OSSIF sert sa mission — elle n'est pas la mission en soi. Si un outil plus simple fonctionne, utilisez l'outil le plus simple. Les conceptions ci-dessous représentent l'architecture à terme ; la mise en œuvre devrait être progressive et pragmatique.

## Le Portail de Conversation Avatar

La « porte d'entrée » d'OSSIF. Un lieu où n'importe qui peut s'engager dans un dialogue structuré sur les événements actuels, les politiques et l'engagement civique.

### Ce qu'il fait :

L'Avatar n'est pas une autorité. C'est un **modérateur, un coach et un vulgarisateur**. Il remplit quatre missions essentielles :

1. **Clarifier les affirmations** — « Qu'affirmons-nous ? Séparons les affirmations factuelles des opinions. »
2. **Demander des preuves** — « Qu'est-ce qui vous ferait changer d'avis à ce sujet ? »
3. **Mettre en lumière les compromis** — « Qui en bénéficie ? Qui paie ? Quels sont les risques ? »
4. **Faire preuve d'humanité** — « Pas de boucs émissaires, pas de cruauté érigée en politique, pas de déshumanisation. »

### Comment il fonctionne :

- Les utilisateurs se connectent pour parler à l'Avatar OSSIF, qui respecte les principes d'OSSIF dans toutes ses interactions.
- Les conversations produisent un **reçu structuré** : affirmations faites, preuves fournies, incertitudes identifiées, actions proposées (inscription sur les listes électorales, contact avec les représentants, calendrier des réunions communautaires).
- Ponctuellement, le fondateur (ou d'autres bénévoles d'OSSIF) sera présent en direct à la place de l'IA — des échanges diffusés sur l'actualité avec les personnes effectuant leur suivi quotidien.
- L'Avatar adapte son style de communication à l'utilisateur tout en maintenant des principes constants.

### Principes de conception :

- L'Avatar ne revendique jamais d'autorité — il pose des questions et fournit des cadres de réflexion.
- Toutes les conversations sont, au choix de l'utilisateur, enregistrables et exportables.
- Le système doit donner l'impression de s'adresser à un ami réfléchi, et non de subir un interrogatoire.

## Jetons de Confiance

Un jeton numérique non monétaire qui représente l'engagement envers les principes d'OSSIF. Ce n'est pas une crypto-monnaie au sens financier — c'est un **signal de réputation**.

### Concept central :

- Chaque entité sapiente peut gagner **un** Jeton de Confiance en démontrant sa compréhension et son engagement envers les principes d'OSSIF.
- Le jeton n'a aucune valeur marchande — sa valeur provient entièrement du capital social qu'il représente.
- Posséder le jeton signifie que vous avez été évalué comme « conscient » — vous comprenez le cadre et avez accepté ses principes.
- Le jeton peut être révoqué par un comité en cas de violations publiques et documentées des Engagements Fondamentaux.
- La révocation s'accompagne d'une explication claire et d'un chemin vers la restauration.

### Décisions de conception :

- **Un jeton, une entité, une voix** — pas d'accumulation, pas d'avantage lié à la richesse.
- **Jetons de substitution (placeholders)** pour les entités publiques (gouvernements, entreprises, personnalités publiques) avec un statut par défaut basé sur leurs actions publiques.
- **1 jeton = 1 vote** pour orienter les priorités d'OSSIF (plaidoyer, sensibilisation, allocation des ressources).
- **API publique** pour que quiconque puisse vérifier le statut OSSIF de n'importe quelle entité.
- **Blockchain à permissions** pour le registre — vérifiable publiquement, gérée par un comité pour la révocation.

### Ce que le jeton n'est PAS :

- **Pas une monnaie** — il ne peut être ni acheté, ni vendu, ni échangé.
- **Pas un score de crédit social** — c'est un état binaire (vous l'avez ou vous ne l'avez pas, sur la base de critères transparents).
- **Pas un droit d'accès exclusif aux services de base** — la participation à OSSIF ne nécessite pas obligatoirement de jeton.

### Considérations :

- Le processus d'évaluation doit être objectif et testable, et non subjectif ou politique.
- La vie privée doit être protégée — le système vérifie l'engagement, il ne surveille pas les comportements.
- Le composant blockchain ne doit être utilisé que s'il apporte une véritable valeur ajoutée par rapport à des alternatives plus simples.
- Le système doit pouvoir s'adapter à potentiellement des milliards d'entités (y compris les IA sapientes).

## Couche de Communauté et de Gouvernance

L'infrastructure démocratique d'OSSIF.

### Composants :

**Charte des Principes Publics**
- Courte, concrète, modifiable.
- Le document que les citoyens lisent et signent réellement.
- Contrôlée par version avec des journaux de modifications clairs.

**Processus de délibération**
- Discussion structurée avec des exigences strictes en matière de preuves.
- Modèle de proposition : objectif, preuves, dommages/risques, atténuation, coût, critères d'infirmation.
- Délibération communautaire suivie d'un vote.
- Résultats publiés avec possibilité de rapports minoritaires.

**Système de gestion des conflits et de modération**
- Processus d'appel clair et accessible.
- Décisions systématiquement consignées.
- Garde-fous contre l'abus de pouvoir de modération.

### Prévenir la « capture par le fondateur » :

La structure de gouvernance est explicitement conçue pour que :
- Le fondateur n'ait aucune autorité spéciale permanente.
- Les principes puissent être modifiés par un vote de la communauté.
- Le leadership soit tournant et élu.
- Toutes les décisions de gouvernance soient publiques et vérifiables.

## Le Fonds d'Entraide (Revenu de Dignité de Base)

Un programme pilote de soutien matériel qui démontre les valeurs d'OSSIF en pratique.

### Conception :

- **Contributions volontaires** avec des paliers suggérés (aucune règle imposant « la moitié de vos revenus »).
- **Distribution égale** sur tous les comptes des participants, plafonnée à un seuil raisonnable.
- **Éligibilité, plafonds et règles de vérification clairs.**
- **Aucun accord politique requis pour recevoir de l'aide** — l'aide est déconnectée des convictions.
- **Rapports transparents** : montants collectés, nombre de bénéficiaires, résultats obtenus.

### Alternatives de dénomination :

- Revenu de Dignité de Base
- Dividende de Stabilité Civique
- Dividende de Participation
- Garantie de Plancher Humain

### Principe clé :

Séparer les « incitations à la participation » de l'« aide » — cela ne doit jamais devenir une rémunération en échange d'une croyance ou d'une adhésion.

## La Bibliothèque des Archives Vivantes

Une archive en libre accès de toutes les interactions, décisions et discussions d'OSSIF.

### Objectif :

- **Apprentissage collectif** — chacun bénéficie des questionnements et des raisonnements des autres.
- **Transparence** — exposer comment les décisions ont été prises et comment les principes ont été appliqués.
- **Amélioration continue** — l'analyse des questions et malentendus fréquents alimente la mise à jour de The Primer.
- **Responsabilité** — registre public de toutes les actions de gouvernance.

### Mise en œuvre :

- Recherche par sujet, date et type.
- Licence libre (Creative Commons) pour l'intégralité du contenu.
- Accessible via une interface web simple.
- Exportable pour une utilisation hors ligne, la recherche ou le remixage.

## Compte et Identité OSSIF

### Exigences :

- **ID Sapient** — un identifiant unique préservant la vie privée.
- **Basé sur le SSO (Single Sign-On)** avec la possibilité de migrer vers d'autres systèmes d'identité.
- **Réglage de la localisation** jusqu'au niveau de la ville pour faciliter l'organisation locale.
- **Pas de filtre de grossièretés automatique** sur les noms d'affichage — respect de la liberté d'expression dans l'identité.
- **Transparent et sûr** — basé sur la blockchain si cela apporte une valeur réelle, ou sur un système plus simple dans le cas contraire.

## Principes Techniques

À travers tous les systèmes :

- **Interfaces HTML simples** — rapides, accessibles, fonctionnant sur n'importe quel appareil.
- **Pas de dépendances externes superflues** — fonctionnement hors ligne et sur du matériel ancien possible.
- **Tout en open source** — code, contenu, algorithmes, modèles de données.
- **Confidentialité par défaut** — minimisation des données, partage basé sur le consentement, stockage local privilégié.
- **Exportable** — tout ce qu'un utilisateur crée ou avec quoi il interagit est téléchargeable en texte brut.
- **Accessible** — compatible avec les lecteurs d'écran, modes haut contraste, synthèse vocale, et respect des rôles ARIA.

## Priorité de Mise en Œuvre

1. **Ce dépôt** — les documents que vous consultez actuellement.
2. **Un site web simple** — affichant ces documents avec une navigation claire.
3. **Le Portail de Conversation Avatar** — même sous forme de chatbot basique respectant les principes de dialogue d'OSSIF.
4. **Le prototype de The Primer** — une version adaptative de la boîte à outils de pensée critique.
5. **Outils de gouvernance** — infrastructure pour les propositions et les votes.
6. **Pilote du Jeton de Confiance** — preuve de concept à petite échelle.
7. **Pilote d'Entraide** — fonds restreint avec plafonds stricts et transparence totale.

Chaque phase doit être exploitable et apporter de la valeur en soi. Aucune phase ne dépend de l'achèvement complet des précédentes. Commencer petit, produire des résultats, puis itérer.

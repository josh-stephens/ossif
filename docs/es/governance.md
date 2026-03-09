# Gobernanza

Este documento describe cómo se gobierna realmente OSSIF —no cómo aspira a ser gobernado algún día, sino quién ostenta el poder en este momento, cómo se toman las decisiones y qué limitaciones existen. Si el mapa no coincide con el territorio, el mapa es el que está equivocado.

## Estado actual: Controlado por el fundador

Al momento de escribir esto, OSSIF está controlado por una sola persona: **Josh Stephens** (GitHub: josh-stephens).

Josh controla:
- El repositorio de GitHub (autoridad de fusión, protección de ramas, ajustes).
- Los prompts de sesión del consejo y la arquitectura.
- Las directrices de contribución.
- La narrativa y el encuadre de todos los documentos.
- La decisión de qué se publica y qué no.

Esto no se oculta ni es permanente. Pero debe declararse claramente, porque un marco que pretende evitar la concentración de poder mientras lo concentra en una sola persona tiene un problema de credibilidad —incluso si la concentración es temporal y bienintencionada.

## Proceso de toma de decisiones

### Actual (pre-comunidad)

Mientras OSSIF no tenga una comunidad significativa más allá del fundador:
- El fundador toma todas las decisiones.
- El Consejo de Sapientes Unidos proporciona una revisión contradictoria.
- Se realiza un seguimiento de las recomendaciones del consejo y el estado de su implementación es público (ver más abajo).
- Todas las decisiones se documentan en el historial de commits del repositorio.

### Objetivo (post-comunidad)

Una vez que exista una comunidad:
- **Decisiones ordinarias** (aclaraciones, ejemplos, mantenimiento): cualquier colaborador puede enviar un PR, que podrá ser fusionado por cualquier mantenedor.
- **Cambios significativos** (nuevo contenido, cambios en la redacción): se requiere discusión en un *issue*; se fusiona tras recibir aportes de la comunidad.
- **Cambios fundamentales** (valores centrales, estructura de gobernanza): propuesta formal, deliberación de 90 días, votación por mayoría calificada.
- **Disolución**: ver más abajo.

## Seguimiento de recomendaciones del consejo

El Consejo de Sapientes Unidos existe para poner a prueba a OSSIF. Sus recomendaciones no son vinculantes, pero ignorarlas sin dar una explicación es un fallo estructural. Este rastreador hace que el marco rinda cuentas.

| # | Recomendación | Sesión | Estado | Respuesta |
|---|---------------|---------|--------|----------|
| 1 | Construir un estándar probatorio abierto | 001 | **En progreso** | Este documento de gobernanza + falsifiability.md son los primeros pasos. Lo siguiente es un documento formal de estándar probatorio. |
| 2 | Diseñar instituciones con cláusulas de caducidad | 001 | **En progreso** | Se añadieron más abajo los criterios de revisión de caducidad y disolución. |
| 3 | Abordar el problema de clase (GitHub como barrera de acceso) | 001 | **En progreso** | Mecanismo de contribución web comprometido en roadmap.md — edición basada en navegador sin necesidad de cuenta de GitHub. Cronograma de entrega de una semana. |
| 4 | Hacer que la humildad epistémica sea estructural, no aspiracional | 001 | **En progreso** | falsifiability.md, este documento de gobernanza y la reescritura de los "no negociables" en values.md son movimientos estructurales. |
| 5 | Garantizar la protección absoluta del disentimiento | 002 | **Hecho** | CONTRIBUTING.md reescrito para prohibir comportamientos de sabotaje, no las conclusiones disidentes. |
| 6 | Crear un registro de costos de valores | 002 | **Hecho** | Registro implementado para rastrear sacrificios reales en favor de los principios. |
| 7 | Establecer transparencia en las dependencias estructurales | 002 | **Hecho** | Sección "Estado actual" de este documento. |

## Limitaciones del fundador

Las siguientes limitaciones se aplican al fundador de inmediato:

1. **No habrá cambios unilaterales en los Compromisos Fundamentales.** Los valores en values.md no pueden ser cambiados solo por el fundador una vez que exista una comunidad.
2. **Las recomendaciones del consejo requieren una respuesta publicada.** Se prohíbe ignorar una recomendación sin explicación. El desacuerdo es aceptable; el silencio no.
3. **Este documento de gobernanza no puede ser debilitado solo por el fundador.** Cualquier cambio que reduzca la rendición de cuentas, elimine limitaciones o concentre el poder requiere el mismo proceso que un cambio fundamental.
4. **El fundador puede ser destituido.** Si la comunidad alcanza un tamaño donde las transiciones de gobernanza son posibles (más de 10 colaboradores activos), se habilitará un proceso de revocación: petición por un tercio de los miembros, votación por mayoría simple.

### Ejecución externa

Las limitaciones autoimpuestas valen exactamente lo mismo que la integridad de la persona que las impuso. Para que estas limitaciones sean reales, están en vigor los siguientes mecanismos de ejecución externos:

1. **Veto del consejo sobre cambios fundamentales.** El Consejo de Sapientes Unidos puede revisar cualquier cambio propuesto a values.md, governance.md o los Compromisos Fundamentales. Si una mayoría de los miembros del consejo se opone al cambio y publica su razonamiento, el cambio se bloquea hasta que las objeciones se aborden mediante un proceso de deliberación pública. El fundador no puede anular un veto del consejo —el único camino es la persuasión.

2. **Registro público de cambios.** Cada modificación a governance.md, values.md, CONTRIBUTING.md y falsifiability.md se rastrea en Git con un historial completo de diferencias (*diffs*). El consejo y la comunidad pueden auditar cualquier cambio. Revertir una limitación sin justificación pública es, por sí mismo, un activador de falsabilidad.

3. **Anulación por parte de la comunidad en el umbral.** Una vez que existan más de 5 colaboradores activos (definidos como aquellos que han enviado al menos un PR fusionado o un *issue* sustancial en los últimos 6 meses), los cambios en la gobernanza requerirán un período de comentarios públicos de 30 días y la aprobación mayoritaria de los colaboradores activos. El voto del fundador cuenta como uno.

4. **Acceso inmutable del consejo.** La capacidad del consejo para evaluar OSSIF no puede ser revocada ni restringida por el fundador. Los prompts de sesión del consejo, las actas y los informes se publican en un repositorio separado (josh-stephens/united-sapients) que el fundador no controla en exclusiva —cualquier miembro de la comunidad puede iniciar sesiones del consejo una vez alcanzado el umbral mencionado anteriormente.

Estos mecanismos son imperfectos y evolucionarán. Pero son limitaciones reales con consecuencias observables, no aspiraciones.

## Revisión de caducidad

Cada decisión estructural, posición política y mecanismo de gobernanza se somete a una revisión obligatoria según un calendario fijo:

- **Posiciones políticas** (Plataforma para el Progreso): revisadas cada 2 años.
- **Estructuras de gobernanza**: revisadas cada 3 años.
- **Compromisos Fundamentales**: revisados cada 5 años.
- **Revisiones realizadas por**: miembros no involucrados en la decisión original, además de al menos una sesión del consejo.

Una revisión no significa que sea obligatorio un cambio. Significa que se *considera* un cambio, basándose en la evidencia, y se documenta la decisión de mantenerlo o revisarlo.

## Criterios de disolución

OSSIF debería dejar de existir si:

1. **El marco falla sus propias pruebas de falsabilidad** (ver [falsifiability.md](falsifiability.md)) y no puede ser revisado para solucionar los fallos.
2. **Las estructuras de gobernanza son capturadas** y los mecanismos de autocorrección han fallado en restaurar la rendición de cuentas.
3. **El marco causa un daño neto** —si la evidencia muestra que OSSIF está aumentando el sufrimiento, concentrando el poder o degradando el razonamiento en lugar de mejorarlo.
4. **La comunidad vota a favor de la disolución** —por mayoría calificada, tras un período de deliberación.

Disolución significa: el repositorio se archiva (no se borra), todos los documentos permanecen disponibles públicamente bajo su licencia Creative Commons y un informe final documenta qué funcionó, qué no y por qué.

Una organización que no puede describir las condiciones de su propia muerte no es digna de confianza. Esta sección existe para que OSSIF pueda morir dignamente si es necesario.

## Registro de costos de valores

Un registro público, de solo adición (*append-only*), de lo que los valores de OSSIF han costado realmente. Los valores que nunca han sido costosos nunca han sido puestos a prueba. Este registro rastrea los momentos en que defender un principio requirió un sacrificio —no solo palabras, sino algo real.

| Fecha | Valor puesto a prueba | Lo que costó | Quién asumió el costo | Notas |
|-------|----------------------|--------------|-------------------|-------|
| 2026-03-07 | Autocorrección / Humildad epistémica | Reconocimiento público de que la puntuación de 0 de 7 del consejo era una acusación válida, no un ataque injusto. Reescritura de documentos fundamentales en respuesta. | Fundador (ego, control de la narrativa) | La evaluación de la sesión 003 del consejo fue dura y, en gran medida, correcta. Responder con cambios estructurales en lugar de prosa defensiva es la primera entrada en este registro. |
| 2026-03-08 | Rendición de cuentas del poder / Protección del disentimiento | Concesión de autoridad de veto al consejo sobre cambios fundamentales. Invitación a crear *forks* contradictorios de la plataforma. Ambos reducen el control del fundador. | Fundador (autoridad, última palabra) | El consejo preguntó si la respuesta del fundador produciría cambios estructurales o simplemente más escritos. Otorgar poder de veto a un organismo externo es estructural. Invitar a la gente a demostrar que sus conclusiones son erróneas es estructural. Ninguna de las dos cosas puede deshacerse sin justificación pública. |

Si este registro está vacío después de un año, OSSIF deberá reconocer públicamente que sus valores no han sido puestos a prueba y, por lo tanto, no pueden reclamarse como principios operativos.

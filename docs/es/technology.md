# Tecnología

La tecnología de OSSIF sirve a su misión; no es la misión en sí misma. Si una herramienta más simple funciona, úsala. Los diseños a continuación representan la arquitectura final; la implementación debería ser incremental y pragmática.

## El Portal de Conversación Avatar

La "puerta de entrada" de OSSIF. Un lugar donde cualquier persona puede entablar un diálogo estructurado sobre eventos actuales, políticas y compromiso cívico.

### Qué hace:

El Avatar no es una autoridad. Es un **moderador, mentor y explicador**. Hace cuatro cosas bien:

1. **Clarificar afirmaciones** — "¿Qué estamos afirmando? Separemos las afirmaciones fácticas de las opiniones".
2. **Solicitar evidencia** — "¿Qué te haría cambiar de opinión sobre esto?".
3. **Visibilizar compensaciones** — "¿Quién se beneficia? ¿Quién paga? ¿Cuáles son los riesgos?".
4. **Mantenlo humano** — "Sin chivos expiatorios, sin la crueldad como política institucional, sin deshumanización".

### Cómo funciona:

- Los usuarios inician sesión para hablar con el Avatar de OSSIF, el cual sigue los principios de OSSIF en todas las interacciones.
- Las conversaciones producen un **recibo estructurado**: afirmaciones realizadas, evidencia proporcionada, incertidumbres identificadas, acciones propuestas (registro de voto, contactar a su representante, fechas de reuniones comunitarias).
- A veces el fundador (u otros voluntarios de OSSIF) estarán en vivo en lugar de la IA: conversaciones transmitidas sobre eventos actuales con personas realizando su registro diario.
- El Avatar adapta su estilo de comunicación al usuario mientras mantiene principios consistentes.

### Principios de diseño:

- El Avatar nunca reclama autoridad: hace preguntas y proporciona marcos de trabajo.
- Todas las conversaciones son opcionalmente grabables y exportables.
- El sistema debe sentirse como hablar con un amigo reflexivo, no como un interrogatorio.

## Tokens de Confianza

Un token digital no monetario que representa el compromiso con los principios de OSSIF. No es una criptomoneda en el sentido financiero; es una **señal de reputación**.

### Concepto central:

- Cada entidad sapiente puede ganar **un** Token de Confianza demostrando comprensión y compromiso con los principios de OSSIF.
- El token no tiene valor monetario; su valor proviene enteramente del capital social que representa.
- Poseer el token significa que has sido evaluado como **"cognoscente"**: comprendes el marco y has aceptado sus principios.
- El token puede ser revocado por un comité debido a violaciones públicas y documentadas de los principios fundamentales.
- La revocación incluye una explicación clara y un camino hacia la restauración.

### Decisiones de diseño:

- **Un token, una entidad, un voto** — sin acumulación, sin ventajas por riqueza.
- **Tokens de reserva (placeholders)** para entidades públicas (gobiernos, corporaciones, figuras públicas) con un estado por defecto basado en sus acciones públicas.
- **1 token = 1 voto** para dirigir las prioridades de OSSIF (defensa, divulgación, asignación de recursos).
- **API pública** para que cualquier persona pueda verificar el estado en OSSIF de cualquier entidad.
- **Blockchain con permisos** para el registro: verificable públicamente, gestionado por un comité para las revocaciones.

### Lo que el token NO es:

- **No es una moneda**: no se puede comprar, vender ni intercambiar.
- **No es un sistema de crédito social**: es binario (se posee o no se posee, basándose en criterios transparentes).
- **No es una puerta de acceso a servicios básicos**: la participación en OSSIF no requiere un token.

### Consideraciones:

- El proceso de evaluación debe ser objetivo y comprobable, no subjetivo o político.
- La privacidad debe ser protegida: el sistema verifica el compromiso, no vigila el comportamiento.
- El componente de blockchain debe usarse solo si realmente agrega valor sobre alternativas más simples.
- El sistema debe poder escalar potencialmente a miles de millones de entidades (incluyendo IA sapiente).

## Capa de Comunidad y Gobernanza

La infraestructura democrática de OSSIF.

### Componentes:

**Carta Pública de Principios**
- Corta, concreta, enmendable.
- El documento que la gente realmente lee y firma.
- Con control de versiones y registros de cambios claros.

**Proceso de Deliberación**
- Discusión estructurada con requisitos de evidencia.
- Plantilla de propuesta: objetivo, evidencia, daños/riesgos, mitigación, costo, qué la invalidaría.
- Deliberación comunitaria seguida de votación.
- Resultados publicados con permiso para informes de minorías.

**Sistema de Conflicto y Moderación**
- Proceso de apelación claro.
- Decisiones registradas.
- Protecciones contra el abuso del poder de moderación.

### Prevención de la "captura por el fundador":

La estructura de gobernanza está diseñada explícitamente para que:
- El fundador no tenga autoridad especial permanente.
- Los principios puedan ser enmendados por voto de la comunidad.
- El liderazgo sea rotativo y electo.
- Todas las decisiones de gobernanza sean públicas y auditables.

## El Fondo de Ayuda Mutua (Ingreso Básico de Dignidad)

Un programa piloto de apoyo material que demuestra los valores de OSSIF en la práctica.

### Diseño:

- **Aportaciones voluntarias** con niveles sugeridos (no como una regla de "la mitad de tus ingresos").
- **Distribución equitativa** entre todas las cuentas de los participantes, con un tope razonable.
- **Elegibilidad, topes y reglas auditables claras**.
- **No se requiere acuerdo político para recibir ayuda**: desvinculado de las creencias.
- **Informes transparentes**: cuánto se recaudó, a cuántos se ayudó, cuáles fueron los resultados.

### Alternativas de nombre (mejores que "Renta Básica Universal"):

- Ingreso Básico de Dignidad
- Dividendo de Estabilidad Cívica
- Dividendo de Participación
- Garantía de Suelo Humano

### Principio clave:

Separar los "incentivos de participación" de la "ayuda"; nunca debe convertirse en un pago por creencias.

## La Biblioteca del Registro Vivo

Un archivo de acceso abierto de todas las interacciones, decisiones y discusiones de OSSIF.

### Propósito:

- **Aprendizaje colectivo**: todos aprenden de las preguntas y razonamientos de los demás.
- **Transparencia**: muestra cómo se llegó a las decisiones y cómo se aplicaron los principios.
- **Mejora continua**: el análisis de preguntas comunes y malentendidos retroalimenta a The Primer.
- **Rendición de cuentas**: registro público de las acciones de gobernanza.

### Implementación:

- Buscable por tema, fecha y tipo.
- Licencia abierta (Creative Commons) para todo el contenido.
- Accesible a través de una interfaz web sencilla.
- Exportable para uso sin conexión, investigación o remezcla.

## Cuenta e Identidad de OSSIF

### Requisitos:

- **ID Sapiente**: un identificador único que preserva la privacidad.
- **Basado en SSO** con capacidad de transferencia a otros sistemas de identidad.
- **Configuración de ubicación** hasta el nivel de ciudad para la organización local.
- **Sin filtro de obscenidades** en los nombres de usuario: libertad de expresión en la identidad.
- **Transparente y seguro**: basado en blockchain si eso aporta un valor real, o más simple si no es así.

## Principios Técnicos

En todos los sistemas:

- **Interfaces HTML simples**: rápidas, accesibles, funcionan en cualquier dispositivo.
- **Sin dependencias externas** donde sea posible: funciona sin conexión, funciona en hardware antiguo.
- **Todo de código abierto**: código, contenido, algoritmos, modelos de datos.
- **Privacidad por defecto**: minimización de datos, intercambio basado en el consentimiento, almacenamiento local primero.
- **Exportable**: cualquier cosa que un usuario cree o con la que interactúe puede descargarse como texto plano.
- **Accesible**: compatible con lectores de pantalla, modos de alto contraste, texto a voz, roles ARIA.

## Prioridad de Implementación

1. **Este repositorio**: los documentos que estás leyendo ahora mismo.
2. **Un sitio web simple**: renderiza estos documentos con una navegación limpia.
3. **El Portal Avatar**: incluso un chatbot básico que siga los principios de conversación de OSSIF.
4. **El prototipo de The Primer**: una versión adaptativa del kit de herramientas de pensamiento crítico.
5. **Herramientas de gobernanza**: infraestructura de propuestas y votación.
6. **Piloto del Token de Confianza**: prueba de concepto a pequeña escala.
7. **Piloto de Ayuda Mutua**: fondo minúsculo con topes estrictos y total transparencia.

Cada fase debe ser utilizable y valiosa por sí misma. Ninguna fase depende de completar todas las fases anteriores. Empezar con poco, lanzar algo, iterar.

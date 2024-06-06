# NeuronalTrade

## Descripción

NeuronalTrade es una aplicación de trading automatizado para criptomonedas, diseñada para analizar y operar en los mercados en tiempo real. Utiliza indicadores técnicos y estrategias avanzadas para generar señales de compra y venta, además de llevar un registro detallado de las ganancias acumuladas. La aplicación está construida utilizando Python y varias bibliotecas de análisis de datos y visualización.

## Características

### Indicadores Técnicos
- **RSI (Relative Strength Index)**: Calcula y monitorea el RSI para generar señales de compra y venta.
- **Stochastic RSI**: Analiza la versión estocástica del RSI para proporcionar señales de trading más precisas.
- **MACD (Moving Average Convergence Divergence)**: Utiliza la diferencia entre medias móviles para identificar tendencias y señales de trading.
- **Bandas de Bollinger**: Evalúa la volatilidad del mercado y genera señales basadas en las bandas superior e inferior.
- **EMA 200 (Exponential Moving Average)**: Utiliza la media móvil exponencial de 200 períodos para identificar la tendencia general del mercado.

### Alertas en Tiempo Real
- Monitoreo continuo de los principales pares de criptomonedas (BTCUSDT, ETHUSDT, etc.).
- Generación de alertas en tiempo real basadas en los indicadores técnicos configurados.

### Gestión de Ganancias
- **Calendario de Ganancias**: Registro de las ganancias acumuladas diarias, permitiendo un seguimiento detallado del rendimiento.

### Pruebas y Validación
- Pruebas unitarias y end-to-end para asegurar la fiabilidad y precisión de las señales y el registro de ganancias.

## Instalación

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/tuusuario/neuronaltrade.git
    cd neuronaltrade
    ```

2. **Crear un entorno virtual**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. **Instalar las dependencias**
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Iniciar el Sistema de Alertas
1. **Configurar las credenciales de API** (si es necesario).
2. **Ejecutar el script principal**:
    ```bash
    python Class/Alerts_Live_3.py
    ```

3. **Seleccionar el indicador deseado**:
    - 1: RSI
    - 2: Stochastic RSI
    - 3: MACD
    - 4: Bandas de Bollinger
    - 5: EMA 200
    - 6: Media Móvil (MM)

### Visualizar el Calendario de Ganancias
La sección del calendario de ganancias permite agregar y visualizar las ganancias acumuladas por día, proporcionando una herramienta de seguimiento detallada.

## Contribución

1. **Fork del proyecto**
2. **Crear una rama para tu característica**:
    ```bash
    git checkout -b feature/nueva-caracteristica
    ```
3. **Realizar commit de tus cambios**:
    ```bash
    git commit -m 'Agregar nueva característica'
    ```
4. **Hacer push a la rama**:
    ```bash
    git push origin feature/nueva-caracteristica
    ```
5. **Crear un Pull Request**

## Milestones

### Milestone 1: Configuración Inicial y Diseño de la Arquitectura

**Descripción:**
a) Configurar el entorno de desarrollo, incluyendo la instalación de herramientas y dependencias necesarias.
b) Diseñar la arquitectura del proyecto, identificando los componentes principales y las interacciones entre ellos.
c) Crear el repositorio en GitHub y configurar la estructura de carpetas y archivos iniciales.
d) Definir el esquema de la base de datos y los modelos de datos necesarios para el proyecto.

### Milestone 2: Implementación de Funcionalidades Básicas

**Descripción:**
a) Desarrollar las clases y objetos necesarios para implementar las funcionalidades básicas del proyecto.
b) Diseñar el modelo de base de datos y crear las tablas y relaciones correspondientes.
c) Generar gráficos y visualizaciones preliminares que se utilizarán en la interfaz de usuario.
d) Integrar APIs de terceros para acceder a datos o servicios necesarios para el proyecto.

### Milestone 3: Desarrollo de Funcionalidades Avanzadas

**Descripción:**
a) Implementar algoritmos para el análisis en tiempo real de datos de criptomonedas.
b) Desarrollar la lógica para enviar notificaciones en tiempo real a los usuarios.
c) Integrar servicios de mensajería para enviar alertas a través de diferentes canales.
d) Crear un simulador de estrategias de trading que permita a los usuarios probar diferentes enfoques.
e) Crear gráficos para la visualización de los indicadores.

### Milestone 4: Diseño Web

**Descripción:**
En esta etapa del proyecto, nos enfocaremos en el diseño visual y la creación de la interfaz de usuario para la aplicación web. Se desarrollarán las vistas y páginas principales del proyecto, así como también los componentes reutilizables de la interfaz, como el footer, menú de navegación, botones, etc. El objetivo es crear una interfaz de usuario atractiva, coherente y fácil de usar para los usuarios finales del proyecto. Este hito nos permitirá visualizar y planificar la estructura y el diseño de la aplicación web, asegurando que se cumplan los requisitos de usabilidad y experiencia de usuario.

### Milestone 5: Despliegue y Lanzamiento

**Descripción:**
a) Preparar el sistema para el despliegue en un entorno de producción.
b) Configurar el servidor de producción y realizar las optimizaciones necesarias.
c) Desplegar la aplicación en el servidor en línea y realizar pruebas finales.
d) Lanzar oficialmente el proyecto y promocionarlo a la comunidad a través de canales adecuados.

### Milestone 6: Optimización y Pruebas

**Descripción:**
a) Realizar pruebas de rendimiento para identificar cuellos de botella y áreas de mejora.
b) Ejecutar pruebas exhaustivas de las funcionalidades implementadas para asegurar su correcto funcionamiento.
c) Depurar errores y problemas encontrados durante las pruebas y corregirlos.
d) Documentar la implementación del proyecto y crear una guía de usuario para los usuarios finales.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

# Árbol de Expresión: [ ( x - y ) * z ] / ( m + n ** p)

## 📝 Representaciones de la expresión

| Notación | Expresión |
|----------|-----------|
| **Infija** | `((x - y) * z) / (m + (n ** p))` |
| **Prefija** | `/ * - x y z + m ** n p` |
| **Postfija** | `x y - z * m n p ** + /` |

## 🌳 Árbol de Expresión
```mermaid
graph TD
    R["/"]
    M["*"]
    P["+"]
    S["-"]
    E["**"]
    X["x"]
    Y["y"]
    Z["z"]
    M2["m"]
    N["n"]
    P2["p"]
    
    R --> M
    R --> P
    M --> S
    M --> Z
    S --> X
    S --> Y
    P --> M2
    P --> E
    E --> N
    E --> P2
    
    style R fill:#ff6b6b,stroke:#cc0000,stroke-width:3px
    style M fill:#feca57,stroke:#ff9f43,stroke-width:2px
    style P fill:#feca57,stroke:#ff9f43,stroke-width:2px
    style S fill:#feca57,stroke:#ff9f43,stroke-width:2px
    style E fill:#feca57,stroke:#ff9f43,stroke-width:2px
    style X fill:#48dbfb,stroke:#0abde3,stroke-width:2px
    style Y fill:#48dbfb,stroke:#0abde3,stroke-width:2px
    style Z fill:#48dbfb,stroke:#0abde3,stroke-width:2px
    style M2 fill:#48dbfb,stroke:#0abde3,stroke-width:2px
    style N fill:#48dbfb,stroke:#0abde3,stroke-width:2px
    style P2 fill:#48dbfb,stroke:#0abde3,stroke-width:2px
```

## 📊 Propiedades del Árbol

| Característica | Valor |
|----------------|-------|
| **Raíz** | `/` (división) |
| **Altura** | 3 |
| **Total de nodos** | 11 |
| **Nodos hoja** | 6 (x, y, z, m, n, p) |
| **Nodos internos** | 5 (/, *, -, +, **) |

## 🔍 Recorridos del Árbol

| Recorrido | Secuencia |
|-----------|-----------|
| **Preorden** | `/ * - x y z + m ** n p` |
| **Inorden** | `x - y * z / m + n ** p` |
| **Postorden** | `x y - z * m n p ** + /` |

## 📝 Evaluación (ejemplo con valores)

Si: `x=10, y=3, z=2, m=5, n=2, p=3`
```
1. x - y = 10 - 3 = 7
2. (x - y) * z = 7 * 2 = 14
3. n ** p = 2 ** 3 = 8
4. m + (n ** p) = 5 + 8 = 13
5. [(x - y) * z] / [m + (n ** p)] = 14 / 13 ≈ 1.077
```

## 🎨 Versión con etiquetas descriptivas
```mermaid
graph TD
    R["/ <br/>(División)"]
    M["* <br/>(Multiplicación)"]
    P["+ <br/>(Suma)"]
    S["- <br/>(Resta)"]
    E["** <br/>(Potencia)"]
    X["x <br/>(variable)"]
    Y["y <br/>(variable)"]
    Z["z <br/>(variable)"]
    M2["m <br/>(variable)"]
    N["n <br/>(base)"]
    P2["p <br/>(exponente)"]
    
    R --> M
    R --> P
    M --> S
    M --> Z
    S --> X
    S --> Y
    P --> M2
    P --> E
    E --> N
    E --> P2
```

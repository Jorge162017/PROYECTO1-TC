"""
====================================================
 Construcción de AFN (Glushkov)
----------------------------------------------------
 Este módulo convierte una expresión regular en notación 
 postfija en un Autómata Finito No Determinista (AFN),
 aplicando el algoritmo de construcción de Glushkov 
 (también conocido como construcción de posiciones).

 Características:
 - No utiliza transiciones ε explícitas como Thompson, 
   sino que construye los estados basados en las posiciones
   de los símbolos dentro de la expresión regular.
 - Cada símbolo terminal genera un estado único.
 - Los operadores conectan los sub-autómatas:
     • '.' → Concatenación
     • '+' → Unión (OR lógico)
     • '*' → Cerradura de Kleene (0 o más repeticiones)

 Funciones principales:
 - toAFN(postfix: str):
     Construye un AFN a partir de la expresión regular 
     en notación postfija.
 - initializeOrAppend(dictionary, key, append):
     Inicializa o agrega transiciones en el AFN.
 - displaceTransitions(afn, delta: int):
     Ajusta índices de estados para unir sub-AFN sin colisiones.
 - newAFN(transitions, accepted):
     Crea un nuevo AFN a partir de transiciones y estado final.

 Ejemplo:
   Expresión: "a*b._+"
   Resultado: AFN representado como diccionario con transiciones 
              y estado(s) de aceptación.

 En resumen:
   RegEx (postfijo) ➝ AFN (no determinista) con construcción de Glushkov.
====================================================
"""


type AFNTransitions = list[dict[str, list[AFNState]]]
type AFNState = int


def toAFN(postfix: str):
    stack = []
    for char in postfix:
        match char:
            case ".":  # Concatenate
                afn2 = stack.pop()
                afn1 = stack.pop()

                afn1OriginalLength = len(afn1["transitions"])
                newAccepted = afn2["accepted"] + afn1OriginalLength

                # Add epsilon transition to start of AFN2
                afn1Accepted = afn1["accepted"]
                initializeOrAppend(
                    afn1["transitions"][afn1Accepted], "_", afn1OriginalLength
                )

                # Map AFN2 transitions to start at the end of AFN1
                mappedAFN2Transitions = displaceTransitions(afn2, afn1OriginalLength)
                afn1["transitions"] += mappedAFN2Transitions

                # Set new accepted
                afn1["accepted"] = newAccepted
                stack.append(afn1)

            case "+":  # Logical OR
                afn2 = stack.pop()
                afn1 = stack.pop()

                lenAfn1 = len(afn1["transitions"])
                afn = newAFN([{"_": [2, 2 + lenAfn1]}, {}], 1)
                afnLength = len(afn["transitions"])
                mappedAFN1Transitions = displaceTransitions(afn1, afnLength)

                afn1Accepted = afn1["accepted"]
                initializeOrAppend(mappedAFN1Transitions[afn1Accepted], "_", 1)

                afnLength += lenAfn1
                mappedAFN2Transitions = displaceTransitions(afn2, afnLength)

                afn2Accepted = afn2["accepted"]
                initializeOrAppend(mappedAFN2Transitions[afn2Accepted], "_", 1)

                mappedAFN1Transitions += mappedAFN2Transitions
                afn["transitions"] += mappedAFN1Transitions
                stack.append(afn)

            case "*":  # 0 or more
                received = stack.pop()

                afn = newAFN([{"_": [1, 2]}, {}], 1)
                afnLength = len(afn["transitions"])
                mappedReceivedTransitions = displaceTransitions(received, afnLength)

                receivedAccepted = received["accepted"]
                initializeOrAppend(mappedReceivedTransitions[receivedAccepted], "_", 1)
                mappedReceivedTransitions[receivedAccepted]["_"].append(2)

                afn["transitions"] += mappedReceivedTransitions
                stack.append(afn)

            case _:
                stack.append(newAFN([{char: [1]}, {}], 1))
    return stack.pop()


def initializeOrAppend(dictionary: dict, key: str, append):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(append)


def displaceTransitions(afn, delta: int):
    return [
        {
            word: [d + delta for d in destinations]
            for (word, destinations) in transition.items()
        }
        for transition in afn["transitions"]
    ]


def newAFN(transitions: AFNTransitions, accepted: AFNState):
    return {
        "transitions": transitions,
        "accepted": accepted,
    }


if __name__ == "__main__":
    exampleAFN = toAFN("a*b._+")
    print(exampleAFN)

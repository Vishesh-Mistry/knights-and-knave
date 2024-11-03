from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is a knight or a knave but not both.
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # If A is a knight then his sentence is true.
    Implication(AKnight, And(AKnight, AKnave)),

    # If A is a knave then his sentence if false, meaning if A is a Knave, then he is not a knight and a knave.
    Implication(AKnight, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Both A and B are knight and a knave but not both.
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # Anything said by A is true if A is a knight.
    Implication(AKnight, And(AKnave, BKnave)),
    # if A is a knave, then anything said by him is false.
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Both A and B are knight and a knave but not both.
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # if A is a knight then his sentences are true.
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # Sentences of A are false if A is a Knave.
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a knight then his sentences are true.
    Implication(BKnight, Or(And(AKnight, BKnave), And(BKnight, AKnave))),
    # If B is a knave then its sentences are false.
    Implication(BKnave, Or(And(AKnight, BKnave), And(BKnight, AKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # All the characters are either knights or knaves but not both.
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),

    # Implication for A if A is Knight and if A is a Knave.
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    # Implication for B if A is Knight and if B is a Knave.
    Implication(BKnight, And(AKnave, CKnave)),
    Implication(BKnave, And(Not(AKnave), Not(CKnave))),

    # Implication for C if A is Knight and if C is a Knave.
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

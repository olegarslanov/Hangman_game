"""
trigubi kabuciu simboliai naudojami tam, kad butu galima ideti kelias
eilutes teksto ir simboliu, kurie sudarys norima atvaizda. "\\" reikia
dvigubinti kadangi '\' tai spec. simbolis, kuris atvaizduos nieka ""
"""

hangman_parts = [
    """
    """,
    """
        _ _
      /     \\
     /       \\
    """,
    """
       |
       |
       |
       |
       |
       |_ _
      /     \\
     /       \\
    """,
    """
        ________
       |
       |
       |
       |
       |
       |_ _
      /     \\
     /       \\
    """,
    """
        ________
       |
       |       O
       |
       |
       |
       |_ _
      /     \\
     /       \\
    """,
    """
        ________
       |
       |       O
       |       |
       |
       |
       |_ _
      /     \\
     /       \\
    """,
    """
        ________
       |
       |       O
       |      /|
       |
       |
       |_ _
      /     \\
     /       \\
    """,
    """
        ________
       |
       |       O
       |      /|\\
       |
       |
       |_ _
      /     \\
     /       \\
    """,
    """
        ________
       |
       |       O
       |      /|\\
       |      /
       |
       |_ _
      /     \\
     /       \\
    """,
    """
        ________
       |
       |       O
       |      /|\\
       |      / \\
       |
       |_ _
      /     \\
     /       \\
    """,
    """
        ________
       |       |
       |       O
       |      /|\\
       |      / \\
       |
       |_ _
      /     \\
     /       \\
    """,
]

GAME_WELCOME = """
                Welcome to the game:

         H  H
         H  H HHHH HHHH  HHH HHHH  HHHH HHH
         HHHH    H H  H H  H H H H    H H  H
         H  H  HHH H  H H  H H H H  HHH H  H
         H  H H  H H  H H  H H H H H  H H  H
         H  H HHHH H  H  HHH H H H HHHH H  H
                           H
                        HHH
"""

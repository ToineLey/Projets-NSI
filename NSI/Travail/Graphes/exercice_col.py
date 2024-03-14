from graphe import Graphe2,mex,coloriage

g = Graphe2()
g.ajouter_arc_no("Bretagne", "Pays de la Loire")
g.ajouter_arc_no("Bretagne", "Normandie")
g.ajouter_arc_no("Provence-Alpes-Côte d'Azur", "Occitanie")
g.ajouter_arc_no("Provence-Alpes-Côte d'Azur", "Auvergne-Rhône-Alpes")
g.ajouter_arc_no("Occitanie", "Auvergne-Rhône-Alpes")
g.ajouter_arc_no("Occitanie", "Nouvelle Aquitaine")
g.ajouter_arc_no("Grand Est", "Ile-de-France")
g.ajouter_arc_no("Grand Est", "Hauts-de-France")
g.ajouter_arc_no("Grand Est", "Bourgogne-Franche-Comté")
g.ajouter_arc_no("Ile-de-France", "Centre - Val de Loire")
g.ajouter_arc_no("Ile-de-France", "Bourgogne-Franche-Comté")
g.ajouter_arc_no("Ile-de-France", "Hauts-de-France")
g.ajouter_arc_no("Ile-de-France", "Normandie")
g.ajouter_arc_no("Hauts-de-France", "Normandie")
g.ajouter_arc_no("Normandie", "Pays de la Loire")
g.ajouter_arc_no("Normandie", "Centre - Val de Loire")
g.ajouter_arc_no("Pays de la Loire", "Centre - Val de Loire")
g.ajouter_arc_no("Pays de la Loire", "Nouvelle Aquitaine")
g.ajouter_arc_no("Centre - Val de Loire", "Nouvelle Aquitaine")
g.ajouter_arc_no("Centre - Val de Loire", "Auvergne-Rhône-Alpes")
g.ajouter_arc_no("Centre - Val de Loire", "Bourgogne-Franche-Comté")
g.ajouter_arc_no("Bourgogne-Franche-Comté", "Auvergne-Rhône-Alpes")
g.ajouter_arc_no("Nouvelle Aquitaine", "Auvergne-Rhône-Alpes")
g.ajouter_sommet("Guadeloupe")
g.ajouter_sommet("Martinique")
g.ajouter_sommet("Guyane")
g.ajouter_sommet("Mayotte")
g.ajouter_sommet("La Réunion")
g.ajouter_sommet("Corse")

for i in range(len(g.adj)):
    print(g.degre(i))
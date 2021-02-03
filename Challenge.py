# import library to create genome diagram
from Bio import SeqIO
from Bio.Graphics import GenomeDiagram

# import library to parse file
from reportlab.lib import colors
from reportlab.lib.units import cm

# read genome file
record = SeqIO.read("Genome.gb", "genbank")

# make diagram for the genome
gd_diagram = GenomeDiagram.Diagram("DNA sequence visualization")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

# add features to diagram
for feature in record.features:
    if feature.type != "gene":
        continue
    if len(gd_feature_set) % 2 == 0:
        #add colors to diagram
        color = colors.green
    else:
        color = colors.darkcyan


    gd_feature_set.add_feature(feature, color=color, label=True, label_size=20, label_color=color)

# draw diagram
gd_diagram.draw(format="circular", circular=True, pagesize=(18 * cm, 18 * cm),start=0, end=len(record), circle_core=0.6)

# save diagram as PNG
gd_diagram.write("Circular_Gene.png", "PNG")
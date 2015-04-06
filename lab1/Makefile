
# stevo.bailey@eecs.berkeley.edu


#############################################
#				Variables                   #
#############################################

top = lab1

#############################################
#				Build Rules                 #
#############################################

pdf:
	pdflatex ${top}.tex

bbl:
	bibtex ${top}.aux

all:
	make pdf 
	-make bbl
	make pdf
	make pdf

.DEFAULT_GOAL := all

# don't delete intermediate files
.SECONDARY: 

#############################################
#               Clean                       #
#############################################

.PHONY: clean pdf bbl all

clean:
	rm -rf *.aux *.log *.synctex.gz *.blg *.bbl *.pdf

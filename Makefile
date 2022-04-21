FIGURE_FILES = $(wildcard figures/*.png)
AUDIO_FILES = $(wildcard audio/*.wav)
CSV_FILES = $(wildcard data/*.csv)

# Run Jupyter Notebook to obtain the figures and table
.PHONY : all
all :
	jupyter execute index.ipynb

# Clean Figures and Table
.PHONY : clean
clean :
	rm -f $(FIGURE_FILES)
	rm -f $(AUDIO_FILES)
	rm -f $(CSV_FILES)


#Create Environment
.PHONY: env
env:
	mamba env create -f environment.yml -p ~/envs/ligo
	bash -ic 'conda activate ligo;python -m ipykernel install --user --name ligo --display-name "IPython - ligo"'

	
.PHONY : variables
variables :
	@echo FIGURE_FILES: $(FIGURE_FILES)
	@echo AUDIO_FILES: $(AUDIO_FILES)
	@echo CSV_FILES: $(CSV_FILES)



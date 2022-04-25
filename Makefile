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

# build the jupyter-book on local machine
.PHONY: html
html:
	jupyter-book build .

# build the jupyter-book in the hub
.PHONY: html-hub
html-hub:
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html
	python -m http.server

.PHONY : variables
variables :
	@echo FIGURE_FILES: $(FIGURE_FILES)
	@echo AUDIO_FILES: $(AUDIO_FILES)
	@echo CSV_FILES: $(CSV_FILES)



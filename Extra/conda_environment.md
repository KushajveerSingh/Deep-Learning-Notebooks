# fastai environment

1. Create conda environment `conda create -n fastai python=3.8 anaconda`

2. Install jupyterlab with extensions.

    ```
    conda install -c conda-forge nodejs
    python3.8 -m pip install jupyterlab==2.0.1
    conda install -c conda-forge jupyter_nbextensions_configurator
    python3.8 -m pip install jupyterlab_server==1.0.7
    

    ############### github extension ###############
    jupyter labextension install @jupyterlab/github
    
    # Goto Github account settings -> Developer Settings -> personal access tokens -> Generate new token.
    
    pip install jupyterlab_github
    jupyter notebook --generate-config
    code /home/kushaj/.jupyter/jupyter_notebook_config.py 

    # Add this line to the above file
    c.GitHubConfig.access_token = '< YOUR_ACCESS_TOKEN >'

    # Use case
    # There is plugin button in the left-sidebar from where you can enter github repo name.
    ################################################
    

    ############### nbdime extension ###############
    pip install nbdime

    # Use case
    # In top-bar there is a button called `git which you can press to view the diff in jupyter.
    ################################################


    ################ toc extension #################
    jupyter labextension install @jupyterlab/toc

    # Use case
    # There is plugin button in the left-sidebar from where you can view table of contents.
    ################################################


    ############# quickopen extension ##############
    python3.8 -m pip install jupyterlab-quickopen
    jupyter labextension install @parente/jupyterlab-quickopen

    # Use case
    # There is plugin button in the left-sidebar from where you can search for files. A keyboard shortcut can also be assigned.
    ################################################


    ############### topbar extension ###############
    python3.8 -m pip install nbresuse
    jupyter labextension install jupyterlab-topbar-extension
    jupyter labextension install jupyterlab-logout
    jupyter labextension install jupyterlab-theme-toggle
    jupyter labextension install jupyterlab-system-monitor
    ################################################


    ########## go-to-definition extension ##########
    jupyter labextension install @krassowski/jupyterlab_go_to_definition

    # Use case
    # alt-click -> mouse shortcut
    # ctrl-alt-b -> keyboard shortcut
    ################################################


    ########## language-server extension ###########
    python3.8 -m pip install jupyter-lsp
    jupyter labextension install @krassowski/jupyterlab-lsp
    python3.8 -m pip install python-language-server[all]

    # Use case
    # Hover over any piece of code, if underline appears press Ctrl to get a tooltip
    # Critical errors have red underline, warnings are orange
    # Place cursor on a variable, function, etc and all the usages will be highlighted
    # Rename variable, function and more names using F2 shortcut
    # A diagnostic panel can also be displayed by searching "Show diagnostics panel" in jupyterlab commands pallete
    ################################################


    ############### matplotlib extension ###############
    python3.8 -m pip install ipympl
    jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-matplotlib

    # Use case
    # Add "%matplotlib widget" magic function in your notebook
    ################################################


    ######## collapsible-headings extension ########
    jupyter labextension install @aquirdturtle/collapsible_headings
    ################################################


    ############### latex extension ################
    python3.8 -m pip install jupyterlab_latex
    jupyter labextension install @jupyterlab/latex

    # Need to install texlive-full, xelatex, .bib file processor
    ################################################
    ```

3. Edit User Preferences in Jupyter lab. Goto "Settings -> Advanced Settings Editor -> Notebook -> User Preferences" and use this JSON file.

    ```json
    {
        "codeCellConfig": {
            "lineNumbers": true,
            "codeFolding": true,
        },
            
        "kernelShutdown": true,
            
        "markdownCellConfig": {
            "autoClosingBrackets": true,
            "lineNumbers": true,
            "codeFolding": true,
        }
    }
    ```

    Goto "Settings -> Advanced Settings Editor -> Document Manager -> User Preferences" and use this JSON file.

    ```json
    {
        "autosaveInterval": 60,
    }
    ```

4. Install main deep learning libraries.

    ```
    ################### pytorch ####################
    conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
    ################################################


    ########### fastai related packages ############
    # fastcore
    git clone https://github.com/fastai/fastcore
    cd fastcore
    python3.8 -m pip install -e ".[dev]"

    # fastai v2
    git clone https://github.com/fastai/fastai2
    cd fastai2
    python3.8 -m pip install -e ".[dev]"

    # fastai v2 medical
    python3.8 -m pip install pyarrow==0.16.0
    python3.8 -m pip install pydicom kornia opencv-python scikit-image

    # nbdev
    git clone https://github.com/fastai/nbdev
    python3.8 -m pip install -e nbdev
    ################################################
    ```

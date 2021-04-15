# **auto_free_fea_sim**

This is intended to be a free framework to be used by everyone in batch FEA simulation.
The idea is to use this programs in WSL, but it's perfectly suitable for use in a Linux workstation.

The main ideia consists in running a batch of simulations inside WSL, using a parametric model and to capture those results.
This process offers advantages where one have a lot of similar models that have to be simulated in FEA.

## Instalation Steps

1. Install Ubuntu 18.04(yes, it has to the 18.04 version, I didn't get this to work on the 20.04 version)
2. Run the **main.sh** script there's inside the **installing_sm** folder
3. Follow the instructions on **installing_podman.md**(and yes, it can be Docker, but since to run Docker one must have admin privileges, this approach does not)

That's it. It seems simple, but it took me awhile to come with this setup, hope you enjoy it. :)

*Note*: This was tested on WSL2, it still pending the test on WSL1. This *should* work in a Linux setup, but this is not tested yet.

## Simulation Steps

1. Prepare a file, it could be an spreadsheet or a bunch of text files, with the parameters for the models and the loads
2. Create the parametric model in Salome-Meca, using the parameters in the Notebook.
3. Create the mesh for the model, idealy using parameters to define the mesh size too, and export the mesh
4. Dump the model from Salome-Meca to a .py script
5. Edit the script to import the parameters. The example provided uses a json file that is changed in every cycle
6. Prepare the Code-Aster .comm file for the simulation setup
7. Run the simulation to check the results
8. In the RunStage folder take the Code Aster .comm and export file
9. Don't forget to set the Code Aster to export the results in text mode, so they can be read afterwards
8. Edit the .comm file, that is another .py script, and import the loads

In the **example** folder there is an example of the workflow in this process. If there's any doubt, please send me an e-mail, I'll try to answer ASAP.

Email: 

## TO-DO
- [ ] Get the results directly from the .comm file
- [ ] Enhance the CLI interface
- [ ] Automate the podman installation
- [ ] Improve the Welcome page
- [ ] Provide the **example**

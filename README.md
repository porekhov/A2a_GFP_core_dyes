# A2a_GFP_core_dyes

calculate_label_volume_MD.py, script for estimation of the volume accessible for a fluorescent label

<img width="730" alt="volume_MC" src="https://github.com/porekhov/A2a_GFP_core_dyes/assets/83649586/07c4b9e5-b95e-4ee9-b441-942d6723fa42">

**Figure 1.** Schematic illustration of the approach.

The accessible volume over the molecular dynamics trajectory is estimated based on the Monte Carlo approach. A set of random points is generated in the rectangular box enclosing the label. The volume is further obtained as the box volume multiplied by the ratio of the number of points found in the vicinity of the label to the total number of points, Vacc = Vbox x (N_near_label/N_total)

The number of random points required for good convergence depends on the total accessible volume and should be justified depending on the system in hand. In the present study, 10000 points were sufficient (see the figure).

<img width="417" alt="volume_vs_num_points" src="https://github.com/porekhov/A2a_GFP_core_dyes/assets/83649586/5fb90510-d72f-42d1-89c8-6d19f9648a11">

**Figure 2.** Estimated accessible volume as a function of the number of random points.

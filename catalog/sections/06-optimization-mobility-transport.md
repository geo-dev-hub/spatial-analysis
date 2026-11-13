# Section 6 — Optimization, location science, mobility, transport

- **Original source section:** 6
- **Source pages:** 9–11
- **Source transcription:** [pages 6–10](../../source-inventory/pages-06-10.md) and [pages 11–15](../../source-inventory/pages-11-15.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** none yet

This section brings together optimisation problems, logistics, accessibility, transport planning, human mobility, positioning and robotics. It includes exact optimisation methods, heuristics, models, software, metrics and applied workflows. Keep the problem definition visible: many similarly named methods solve different objectives or operate under different constraints.

## Location-allocation and spatial optimization

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Covering and median: p-median, p-center, p-dispersion, set covering, maximal covering (MCLP), MEXCLP, MALP, BACOP, hypercube queuing | Facility-location models / optimisation problems / queueing models | 10 | Captured; names not individually verified |
| Capacitated and hub location, p-hub median, hierarchical, stochastic and robust facility location | Facility-location problem variants / optimisation models | 10 | Captured; names not individually verified |
| Districting: redistricting, ReCom, MCMC and Flip, compactness scores (Polsby-Popper, Reock, Schwartzberg), territory design, set partitioning | Districting and partitioning methods / sampling methods / compactness metrics | 10 | Captured; names not individually verified |
| Land-use allocation, spatial reserve design (Marxan), art gallery problem, sensor and camera placement, cell tower siting | Spatial allocation / reserve design / coverage and placement problems | 10 | Captured; names not individually verified |
| Heuristics: genetic algorithms, simulated annealing, NSGA-II, particle swarm, ant colony, tabu search, GRASP, variable neighborhood search, matheuristics | Metaheuristics / multi-objective optimisation methods | 10 | Captured; names not individually verified |
| Exact methods: branch-and-bound, Lagrangian relaxation, Benders decomposition, min-cost flow, transportation and assignment problems, Hungarian algorithm; quantum annealing and QAOA (experimental) | Exact optimisation methods / mathematical programming / experimental quantum methods | 10 | Captured; names not individually verified |

## Logistics

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Multi-depot VRP, periodic routing, inventory-routing, drone-truck routing, school bus routing | Vehicle-routing problem variants | 10 | Captured; names not individually verified |
| Snow plow and waste collection arc routing, ride-hailing dispatch, bike rebalancing | Arc-routing and dispatch optimisation problems | 10 | Captured; names not individually verified |
| ETA prediction (WDR, DeepTTE, graph neural networks), OR-Tools | Prediction models / software toolkit | 10 | Captured; names not individually verified |

## Accessibility and spatial interaction

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Gravity models, Huff model, Hansen accessibility, Reilly's law, 2SFCA and variants, cumulative opportunities, impedance decay | Spatial interaction models / accessibility measures | 10 | Captured; names not individually verified |
| Radiation model, intervening opportunities, origin-destination flow models, equity accessibility (Gini, Lorenz) | Interaction and flow models / equity measures | 10 | Captured; names not individually verified |
| Trade area analysis (drive-time, Huff, analog), cannibalization, retail gravity, 15-minute city metrics | Retail and urban analysis methods / spatial indicators | 10 | Captured; names not individually verified |

## Transport planning

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Four-step model: trip generation, gravity distribution, mode choice (multinomial and nested logit), assignment | Transport modelling framework / statistical models / network assignment | 10–11 | Captured; names not individually verified |
| Traffic assignment: user equilibrium, Frank-Wolfe, Wardrop equilibrium, dynamic traffic assignment, cell transmission model | Network equilibrium / optimisation / traffic-flow models | 10–11 | Captured; names not individually verified |
| Activity-based and simulation: MATSim, SUMO, ActivitySim, UrbanSim, car-following (IDM, Gipps) | Simulation frameworks / software / behavioural models | 11 | Captured; names not individually verified |
| O-D estimation from counts, GTFS processing, transit accessibility, crash hotspot and empirical Bayes screening | Estimation methods / data processing / accessibility / safety analysis | 11 | Captured; names not individually verified |
| Traffic forecasting: DCRNN, STGCN, Graph WaveNet, ASTGCN, GMAN, PDFormer, STID | Spatiotemporal forecasting model architectures | 11 | Captured; names not individually verified |

## Human mobility and trajectories

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Trajectory processing: stop and stay-point detection, compression (SQUISH, STTrace, opening window, TD-TR), imputation, route recovery | Trajectory processing algorithms | 11 | Captured; names not individually verified |
| Similarity and clustering: dynamic time warping, LCSS, Fréchet, TRACLUS, T-DBSCAN, trajectory similarity search | Similarity measures / clustering algorithms / query methods | 11 | Captured; names not individually verified |
| Patterns: flock, convoy, swarm; transport mode detection; activity inference | Moving-object patterns / classification and inference methods | 11 | Captured; names not individually verified |
| Mobility models: exploration and preferential return, Lévy flights, continuous-time random walks; metrics (radius of gyration, entropy, predictability) | Mobility models / movement metrics | 11 | Captured; names not individually verified |
| Next-location prediction: Markov, DeepMove, LSTPM, GETNext, STAN, Flashback; POI recommendation | Sequential prediction models / recommendation systems | 11 | Captured; names not individually verified |
| Time geography: space-time prisms, potential path areas, activity spaces | Spatial-temporal constructs / analytical methods | 11 | Captured; names not individually verified |
| Movement ecology: MCP, KDE, LoCoH, Brownian bridge, step selection, resource selection functions | Movement ecology estimators / models | 11 | Captured; names not individually verified |
| Mobile phone CDR analysis, footfall estimation, segregation from mobility | Data analysis workflows / population and mobility measures | 11 | Captured; names not individually verified |

## Positioning, navigation, robotics

| Source entry | Proposed type (unverified) | Source page | Review status |
| --- | --- | ---: | --- |
| Haversine, Vincenty and Karney geodesics, great-circle and rhumb lines | Geodesic calculations / navigation methods | 11 | Captured; names not individually verified |
| GNSS: RTK, PPP, Kalman and particle filters, dead reckoning, trilateration, Wi-Fi and Bluetooth fingerprinting, UWB, Wi-Fi RTT, magnetic fingerprinting, pedestrian dead reckoning | Positioning methods / estimation filters / sensor technologies | 11 | Captured; names not individually verified |
| SLAM: EKF-SLAM, FastSLAM, GraphSLAM, ORB-SLAM, LOAM, LIO-SAM; visual odometry, loop closure, pose graph optimization | Simultaneous localisation and mapping algorithms / robotics workflows | 11 | Captured; names not individually verified |
| Planning: RRT and RRT*, PRM, D* Lite, hybrid A*, Dubins and Reeds-Shepp curves, potential fields, coverage path planning, navigation meshes, social force crowd models | Motion-planning algorithms / geometric path models / crowd models | 11 | Captured; names not individually verified |
| Maritime and aviation: weather routing (isochrone method), CPA/TCPA collision avoidance, AIS trajectory prediction and anomaly analysis, UAV mission planning, 3D path planning | Domain-specific routing / collision avoidance / prediction and planning workflows | 11 | Captured; names not individually verified |

## Decisions for the next pass

1. Separate the optimisation problem from the algorithm used to solve it.
2. Record objective functions, constraints, decision variables and units for location-allocation examples.
3. Distinguish accessibility measures from the models used to estimate travel or interaction.
4. Treat GTFS processing and transit routing as data and network workflows with explicit feed versions and service assumptions.
5. Record temporal resolution, sampling bias and privacy constraints for mobility data.
6. Verify named software, forecasting architectures and robotics systems against original publications and maintained documentation.

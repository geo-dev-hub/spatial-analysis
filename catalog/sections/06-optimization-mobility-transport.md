# Section 6 — Optimization, location science, mobility, transport

- **Original source section:** 6
- **Source pages:** 9–11
- **Source transcription:** [pages 6–10](../../source-inventory/pages-06-10.md) and [pages 11–15](../../source-inventory/pages-11-15.md)
- **Review state:** source entries extracted into this index; not every entry independently verified
- **Current canonical records:** [The p-median problem](../../algorithms/optimization/p-median.md); [Capacitated p-median](../../algorithms/optimization/capacitated-p-median.md); [Discrete p-center](../../algorithms/optimization/p-center.md); [Location set covering](../../algorithms/optimization/set-covering.md); [Maximal covering location](../../algorithms/optimization/maximal-covering.md); [Backup coverage (r-covering)](../../algorithms/optimization/backup-coverage.md); [M/M/c queueing model](../../algorithms/optimization/mmc-queue.md); [Maximum expected covering (MEXCLP)](../../algorithms/optimization/mexclp.md); [Two-step floating catchment area](../../algorithms/optimization/two-step-fca.md) (first audited facility-location and accessibility models; remaining entries are still unverified)

This section brings together optimisation problems, logistics, accessibility, transport planning, human mobility, positioning and robotics. It includes exact optimisation methods, heuristics, models, software, metrics and applied workflows. Keep the problem definition visible: many similarly named methods solve different objectives or operate under different constraints.

## First audited location model

The [p-median lesson](../../algorithms/optimization/p-median.md) states the uncapacitated facility-location objective and assignment constraints. A tested exact exhaustive solver provides a small-instance oracle, with an interactive notebook. It does not include capacities, maximum service thresholds, stochastic demand or equity constraints.

## First audited location and accessibility models

The [p-median lesson](../../algorithms/optimization/p-median.md) states the uncapacitated facility-location objective and assignment constraints. A tested exact exhaustive solver provides a small-instance oracle, with an interactive notebook. The [2SFCA lesson](../../algorithms/optimization/two-step-fca.md) adds a binary-catchment accessibility measure balancing provider supply and population demand, with a tested implementation and notebook. The [p-center lesson](../../algorithms/optimization/p-center.md) minimizes the maximum nearest-facility cost when exactly p sites open, with a tested exact small-instance solver and visual lab. The [set-covering lesson](../../algorithms/optimization/set-covering.md) minimizes the number of sites needed to reach every demand point within a threshold, with an exact small-instance solver, tests, walkthrough, exercise and visual lab. The [MCLP lesson](../../algorithms/optimization/maximal-covering.md) selects at most p facilities to maximize weighted demand within a service threshold, with an exact small-instance solver, tests, intern walkthrough, exercise and visual lab. These are distinct models: p-median minimizes total assignment cost, p-center minimizes worst-case cost, set covering minimizes the number of facilities needed to cover everyone, MCLP maximizes threshold coverage, and 2SFCA measures supply-to-demand accessibility. The capacitated p-median baseline enforces deterministic scalar facility limits but does not model queues, split demand, stochastic capacity or service levels. A separate [accessibility equity diagnostics lesson](../../algorithms/optimization/accessibility-equity.md) measures population-weighted Lorenz/Gini distributions, lower-tail access, threshold shortfall and caller-defined group gaps. The [equity-constrained maximal-covering model](../../algorithms/optimization/equity-constrained-covering.md) adds explicit group coverage floors to a threshold-covering problem, with an exact tiny-instance solver and unit-test suite. Both are scoped teaching tools; the floors and groups remain policy choices, not a universal fairness rule. More general equity-constrained location optimisation remains future work.

## Capacity-constrained location

The [capacitated p-median lesson](../../algorithms/optimization/capacitated-p-median.md) and exact tiny-instance implementation add indivisible demand quantities and hard facility capacities to the assignment model. A test suite, intern walkthrough, exercise and visual notebook compare the constrained solution with the uncapacitated p-median baseline. It is not a queueing model and does not allow demand splitting.

## Expected coverage under busy units

The [MEXCLP lesson](../../algorithms/optimization/mexclp.md) adds an availability-aware objective to the deterministic location models. Its exact small-instance solver, tests, intern walkthrough, exercise and interactive lab assume equal independent busy fractions and allow multiple units at one candidate site. This is distinct from deterministic r-covering and from M/M/c queueing; the adjusted MEXCLP and hypercube queueing model remain outside this implementation.

## Location-allocation and spatial optimization

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Covering and median: p-median, p-center, p-dispersion, set covering, maximal covering (MCLP), MEXCLP, MALP, BACOP, hypercube queuing | Facility-location models / optimisation problems / queueing models | 10 | Not checked — intake only |
| Capacitated and hub location, p-hub median, hierarchical, stochastic and robust facility location | Facility-location problem variants / optimisation models | 10 | Not checked — intake only |
| Districting: redistricting, ReCom, MCMC and Flip, compactness scores (Polsby-Popper, Reock, Schwartzberg), territory design, set partitioning | Districting and partitioning methods / sampling methods / compactness metrics | 10 | Not checked — intake only |
| Land-use allocation, spatial reserve design (Marxan), art gallery problem, sensor and camera placement, cell tower siting | Spatial allocation / reserve design / coverage and placement problems | 10 | Not checked — intake only |
| Heuristics: genetic algorithms, simulated annealing, NSGA-II, particle swarm, ant colony, tabu search, GRASP, variable neighborhood search, matheuristics | Metaheuristics / multi-objective optimisation methods | 10 | Not checked — intake only |
| Exact methods: branch-and-bound, Lagrangian relaxation, Benders decomposition, min-cost flow, transportation and assignment problems, Hungarian algorithm; quantum annealing and QAOA (experimental) | Exact optimisation methods / mathematical programming / experimental quantum methods | 10 | Not checked — intake only |

## Logistics

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Multi-depot VRP, periodic routing, inventory-routing, drone-truck routing, school bus routing | Vehicle-routing problem variants | 10 | Not checked — intake only |
| Snow plow and waste collection arc routing, ride-hailing dispatch, bike rebalancing | Arc-routing and dispatch optimisation problems | 10 | Not checked — intake only |
| ETA prediction (WDR, DeepTTE, graph neural networks), OR-Tools | Prediction models / software toolkit | 10 | Not checked — intake only |

## Accessibility and spatial interaction

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Gravity models, Huff model, Hansen accessibility, Reilly's law, 2SFCA and variants, cumulative opportunities, impedance decay | Spatial interaction models / accessibility measures | 10 | Not checked — intake only |
| Radiation model, intervening opportunities, origin-destination flow models, equity accessibility (Gini, Lorenz) | Interaction and flow models / equity measures | 10 | Not checked — intake only |
| Trade area analysis (drive-time, Huff, analog), cannibalization, retail gravity, 15-minute city metrics | Retail and urban analysis methods / spatial indicators | 10 | Not checked — intake only |

## Transport planning

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Four-step model: trip generation, gravity distribution, mode choice (multinomial and nested logit), assignment | Transport modelling framework / statistical models / network assignment | 10–11 | Not checked — intake only |
| Traffic assignment: user equilibrium, Frank-Wolfe, Wardrop equilibrium, dynamic traffic assignment, cell transmission model | Network equilibrium / optimisation / traffic-flow models | 10–11 | Not checked — intake only |
| Activity-based and simulation: MATSim, SUMO, ActivitySim, UrbanSim, car-following (IDM, Gipps) | Simulation frameworks / software / behavioural models | 11 | Not checked — intake only |
| O-D estimation from counts, GTFS processing, transit accessibility, crash hotspot and empirical Bayes screening | Estimation methods / data processing / accessibility / safety analysis | 11 | Not checked — intake only |
| Traffic forecasting: DCRNN, STGCN, Graph WaveNet, ASTGCN, GMAN, PDFormer, STID | Spatiotemporal forecasting model architectures | 11 | Not checked — intake only |

## Human mobility and trajectories

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Trajectory processing: stop and stay-point detection, compression (SQUISH, STTrace, opening window, TD-TR), imputation, route recovery | Trajectory processing algorithms | 11 | Not checked — intake only |
| Similarity and clustering: dynamic time warping, LCSS, Fréchet, TRACLUS, T-DBSCAN, trajectory similarity search | Similarity measures / clustering algorithms / query methods | 11 | Not checked — intake only |
| Patterns: flock, convoy, swarm; transport mode detection; activity inference | Moving-object patterns / classification and inference methods | 11 | Not checked — intake only |
| Mobility models: exploration and preferential return, Lévy flights, continuous-time random walks; metrics (radius of gyration, entropy, predictability) | Mobility models / movement metrics | 11 | Not checked — intake only |
| Next-location prediction: Markov, DeepMove, LSTPM, GETNext, STAN, Flashback; POI recommendation | Sequential prediction models / recommendation systems | 11 | Not checked — intake only |
| Time geography: space-time prisms, potential path areas, activity spaces | Spatial-temporal constructs / analytical methods | 11 | Not checked — intake only |
| Movement ecology: MCP, KDE, LoCoH, Brownian bridge, step selection, resource selection functions | Movement ecology estimators / models | 11 | Not checked — intake only |
| Mobile phone CDR analysis, footfall estimation, segregation from mobility | Data analysis workflows / population and mobility measures | 11 | Not checked — intake only |

## Positioning, navigation, robotics

| Source entry | Provisional kind | Source page | Verification status |
|---|---|---:|--- |
| Haversine, Vincenty and Karney geodesics, great-circle and rhumb lines | Geodesic calculations / navigation methods | 11 | Not checked — intake only |
| GNSS: RTK, PPP, Kalman and particle filters, dead reckoning, trilateration, Wi-Fi and Bluetooth fingerprinting, UWB, Wi-Fi RTT, magnetic fingerprinting, pedestrian dead reckoning | Positioning methods / estimation filters / sensor technologies | 11 | Not checked — intake only |
| SLAM: EKF-SLAM, FastSLAM, GraphSLAM, ORB-SLAM, LOAM, LIO-SAM; visual odometry, loop closure, pose graph optimization | Simultaneous localisation and mapping algorithms / robotics workflows | 11 | Not checked — intake only |
| Planning: RRT and RRT*, PRM, D* Lite, hybrid A*, Dubins and Reeds-Shepp curves, potential fields, coverage path planning, navigation meshes, social force crowd models | Motion-planning algorithms / geometric path models / crowd models | 11 | Not checked — intake only |
| Maritime and aviation: weather routing (isochrone method), CPA/TCPA collision avoidance, AIS trajectory prediction and anomaly analysis, UAV mission planning, 3D path planning | Domain-specific routing / collision avoidance / prediction and planning workflows | 11 | Not checked — intake only |

## Decisions for the next pass

1. Separate the optimisation problem from the algorithm used to solve it.
2. Record objective functions, constraints, decision variables and units for location-allocation examples.
3. Distinguish accessibility measures from the models used to estimate travel or interaction.
4. Treat GTFS processing and transit routing as data and network workflows with explicit feed versions and service assumptions.
5. Record temporal resolution, sampling bias and privacy constraints for mobility data.
6. Verify named software, forecasting architectures and robotics systems against original publications and maintained documentation.

## Backup coverage extension

The [backup-coverage lesson](../../algorithms/optimization/backup-coverage.md) and [Python package](../../implementations/python/backup-coverage/README.md) introduce deterministic r-covering: demand is counted only when at least r distinct selected candidate facilities are within the service threshold. The package includes tests, an intern walkthrough, exercise and executable notebook. This is a redundancy screen, not a reliability probability; shared infrastructure, correlated failures, capacity and queues are outside scope.

## Service queueing extension

The [M/M/c lesson](../../algorithms/optimization/mmc-queue.md) and [implementation](../../implementations/python/mmc-queue/README.md) introduce Erlang-C steady-state waiting for one FCFS queue feeding identical parallel servers. Tests, an intern walkthrough, an exercise and an executable notebook accompany the package. The assumptions are explicit: Poisson arrivals, exponential service, stationarity, an infinite queue and identical servers. It is an operations model, not a geographic accessibility measure.

## Bibliographic checks on the scoped location models

The following foundational citation metadata has been checked against publisher or authoritative bibliographic records and corrected where necessary:

- **p-center:** Hakimi (1964), *Operations Research*, 12(3), 450–459, [10.1287/opre.12.3.450](https://doi.org/10.1287/opre.12.3.450). **p-median:** Hakimi (1964), same paper, and Hakimi (1965), *Operations Research*, 13(3), 462–475, [10.1287/opre.13.3.462](https://doi.org/10.1287/opre.13.3.462), which directly treats the distribution of p switching centres.
- **Location set covering:** Toregas, Swain, ReVelle and Bergman (1971), *Operations Research*, 19(6), 1363–1373, [10.1287/opre.19.6.1363](https://doi.org/10.1287/opre.19.6.1363).
- **Maximal covering:** Church and ReVelle (1974), *Papers of the Regional Science Association*, 32(1), 101–118, [10.1111/j.1435-5597.1974.tb00902.x](https://doi.org/10.1111/j.1435-5597.1974.tb00902.x); and their distinct 1976 theoretical-links paper, *Geographical Analysis*, 8(4), 406–415, [10.1111/j.1538-4632.1976.tb00547.x](https://doi.org/10.1111/j.1538-4632.1976.tb00547.x).
- **Backup coverage:** Hogan and ReVelle (1986), *Management Science*, 32(11), 1434–1444, [10.1287/mnsc.32.11.1434](https://doi.org/10.1287/mnsc.32.11.1434).
- **MEXCLP:** Daskin (1983), *Transportation Science*, 17(1), 48–70, [10.1287/trsc.17.1.48](https://doi.org/10.1287/trsc.17.1.48); Batta, Dolan and Krishnamurthy (1989), *Transportation Science*, 23(4), 277–287, [10.1287/trsc.23.4.277](https://doi.org/10.1287/trsc.23.4.277).
- **2SFCA and E2SFCA:** Radke and Mu (2000), *Geographic Information Sciences*, 6(2), 105–112, [10.1080/10824000009480538](https://doi.org/10.1080/10824000009480538); Luo and Wang (2003), *Environment and Planning B: Planning and Design*, 30(6), 865–884, [10.1068/b29120](https://doi.org/10.1068/b29120); Luo and Qi (2009), *Health & Place*, 15(4), 1100–1107, [10.1016/j.healthplace.2009.06.002](https://doi.org/10.1016/j.healthplace.2009.06.002), with its [2011 erratum](https://doi.org/10.1016/j.healthplace.2010.10.006).

This pass checks bibliographic identity and metadata for these cited foundations. It does not verify every technical claim, every model variant or every grouped source entry in Section 6.

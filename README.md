# GEDc
GEDc. Computes the graph edit distance between a single query graph and a data graph or between a single query graph and a database of graphs.

## Environment
GEDc requires Python 3 running on a machine with 64-bit Linux. Ensure that the `./bin/GEDc` binary is available and executable in your working directory.

## Installation
```sh
git clone https://github.com/SNUCSE-CTA/GEDc.git
cd GEDc
```

## Usage
```sh
python3 GEDc.py <query_file_path> <data_file_path>
```

## Input
Accepts the following input files:
 - Query File: The query graph file that defines the structure to search for.
 - Data File: Either a single data graph file or a database of graphs to compare against.

## Output
Outputs the graph edit distance along with additional details about the computation.

Example output:

```sh
ged(G_12710, G_15698) = 7
  [Result] Ans                 : 0
  [Result] BranchDistance_TIME : 0.0000
  [Result] DATA_NUM_BRANCHES   : 7
  [Result] DFS_depth_cnt       : 49
  [Result] FILTERING_TIME      : 0.0001
  [Result] HUNGARIAN_TIME      : 0.0000
  [Result] HUNGARIAN_TIME_BMao : 0.0000
  [Result] Hungarian_Vertices  : 0
  [Result] NUM_CANDIDATES      : 1
  [Result] NUM_FILTERED        : 0
  [Result] TOTAL_TIME          : 0.1369
  [Result] TotalMaxQueueSize   : 0
  [Result] TotalSearchSpace    : 0
  [Result] VERIFY_TIME         : 0.1368
```

## License
Distributed under Apache License 2.0. See LICENSE for more information.

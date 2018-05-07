# Based on recommendations from
#    https://www.mail-archive.com/slurm-dev@lists.llnl.gov/msg00964.html
#
# Memlocks the slurmd process's memory so that when a node starts swapping,
# the slurmd will continue to respond
SLURMD_OPTIONS="-M"

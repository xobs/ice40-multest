# ICE40 MUL tester

Test that the ICE40 multiplier is being correctly inferred by Yosys.

## Usage

Install cocotb and yosys, then run:

```sh
$ make
```

This will use Yosys to generate `dspmul.v` which contains inferred `SB_MAC16` blocks.  If these are not present, then your version of Yosys does not do DSP inference.

It will then generate 256 random 32-bit pairs and run them through this inferred block, as well as through a standard Verilog "*" operator.  For good measure, it also does a simply Python "*".

## Sim Libraries

This repo comes with the Yosys simulation files for the ICE40.  You can use other simulation libraries, such as `sb_ice_syn.v` from Lattice.  To do this, run:

```sh
$ make ICE40_CELLS=sb_ice_syn.v
```
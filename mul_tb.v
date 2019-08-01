module tb(
    input [31:0] a,
    input [31:0] b,
    output [63:0] x,
    input clk,
    input [0] backend
);

reg [31:0] result;
assign x = result;

reg [63:0] sm_x;
simplemul simplemul(
    .a(a),
    .b(b),
    .clk(clk),
    .x(sm_x)
);

reg [63:0] dspm_x;
dspmul dspmul(
    .a(a),
    .b(b),
    .clk(clk),
    .x(dspm_x)
);

always @(*)
begin
    case (backend)
        1'b0: assign result = sm_x;
        1'b1: assign result = dspm_x;
    endcase
end

// Dump waves
// initial begin
// $dumpfile("dump.vcd");
// $dumpvars(0, tb);
// end

endmodule
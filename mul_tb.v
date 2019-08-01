module tb(
    input [31:0] a,
    input [31:0] b,
    output [31:0] x,
    input clk,
    input [0] backend
);

reg [31:0] sm_x;
simplemul simplemul(
    .a(a),
    .b(b),
    .clk(clk),
    .x(sm_x)
);

        assign x = sm_x;
always @(*)
begin
    if (backend == 1'b0)
    begin
    end
end

// Dump waves
// initial begin
// $dumpfile("dump.vcd");
// $dumpvars(0, tb);
// end

endmodule
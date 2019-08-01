module simplemul(
    input [31:0] a,
    input [31:0] b,
    output [63:0] x,
    input clk
);

reg [63:0] result;
assign x = result;

always @(posedge clk)
begin
    result <= a * b;
end

endmodule
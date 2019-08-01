module simplemul(
    input [31:0] a,
    input [31:0] b,
    output [31:0] x,
    input clk
);

reg [31:0] result;
assign x = result;

always @(posedge clk)
begin
    result <= a * b;
end

endmodule
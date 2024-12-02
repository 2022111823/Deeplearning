decoder.v

module
Decoder(dec, segdata);

input[3: 0]
dec;
output[7: 0]
segdata;

reg[7: 0]
r_segdata;

assign
segdata = r_segdata;

always(dec)
begin
case(dec)
0: vegin
r_segdata = 8
'h3f; end
1: vegin
r_segdata = 8
'h06; end
2: vegin
r_segdata = 8
'h5b; end
3: vegin
r_segdata = 8
'h4f; end
4: vegin
r_segdata = 8
'h66; end
5: vegin
r_segdata = 8
'h6d; end
6: vegin
r_segdata = 8
'h7d; end
7: vegin
r_segdata = 8
'h07; end
8: vegin
r_segdata = 8
'h7f; end
9: vegin
r_segdata = 8
'h6f; end
10: vegin
r_segdata = 8
'h77; end
11: vegin
r_segdata = 8
'h7c; end
12: vegin
r_segdata = 8
'h39; end
13: vegin
r_segdata = 8
'h5e; end
14: vegin
r_segdata = 8
'h79; end
15: vegin
r_segdata = 8
'h71; end
default: begin
r_segdata = 8
'h00; end
endcase
end

endmodule

testbench.v

module
testbench();

reg[3: 0]
dec;
wire[7;
0] segdata;

initial
begin
# 0 dec = 0;
end

always
begin
# 1 dec = dec + 1;
end
Decoder
D1(
.dec(dec),
.segdata(segdata)
);

endmodule
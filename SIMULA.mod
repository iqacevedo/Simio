param d{i in 1..100, j in 1..100} >= 0;

var x {i in 1..100,j in 1..3} binary;

subject to r1: sum{i in 1..100} x[i,1] = 30;
subject to r2: sum{i in 1..100} x[i,2] = 31;
subject to r3: sum{i in 1..100} x[i,3] = 39;
subject to r4{i in 1..100}: sum{j in 1..3} x[i,j] = 1;

minimize z: sum {i in 1..100, j in 1..3} x[i,j]*d[i,j];

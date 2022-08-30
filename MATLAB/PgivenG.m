function [out] = PgivenG(i,n)
out = (((1+i)^n)-i*n-1)/((i^2)*(1+i)^n);
end
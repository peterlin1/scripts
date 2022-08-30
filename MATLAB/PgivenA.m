function [out] = PgivenA(i,n)
%calculates Future value given Annuity
%P = A * ((1 - (1 / (1 + i)^n)) / i)
%A = annuiy
%i = equiv interest
%n = periods
out = ((1 - (1 / ((1 + i)^n))) / i);
end
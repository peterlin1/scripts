function [out] = FgivenA(i,n)
%calculates Future value given Annuity
%A = annuiy
%i = equiv interest
%n = periods
out = (((1+i)^n - 1)/i);
end
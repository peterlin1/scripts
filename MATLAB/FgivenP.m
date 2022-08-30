function [out] = FgivenP(i,n)
%calculates Future value given Annuity
%P = Present Value
%i = equiv interest
%n = periods
out = (1+i)^n;
end
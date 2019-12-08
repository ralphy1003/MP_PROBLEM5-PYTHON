%PROBLEM 5-MATLAB
n=[0:199];
FCT = 'Please enter a function for the user input x(n):';
x = input(FCT);
for a = 1:numel(n)
    if n(a) == 0
	y(a) = (-1.5*x(a))+(2*x(a+1))+(-0.5*x(a+2));
    elseif (n(a) > 0) && (n(a) <= 198)
	y(a) = (0.5*x(a+1))+(-0.5*x(a-1));
    elseif n(a) == 199
	y(a) = (1.5*x(a))+(-2*x(a-1))+(0.5*x(a-2));
    end
end
plot(n,x,'m','linewidth',2.5)
title('Graph of x(n) and y(n)')
hold on
plot(n,y,'--r','linewidth',1.5)
legend('x(n)','y(n)')